#!/usr/bin/env python3
r"""High Activity Hosts - CrowdStrike Falcon Endpoint Behavior Analytics.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

This script identifies the most active and highest-risk hosts in your
CrowdStrike Falcon environment by compositing data from five Falcon APIs
into a single weighted activity score per host.

Data Sources:
    The following Falcon APIs are queried and merged per host.  The three
    optional sources degrade gracefully when their API scopes are missing.

    - Hosts          Query device IDs (FQL filter + pagination) and fetch
                     full metadata: hostname, OS, platform, IP, last_seen.
    - Alerts         Cursor-based pagination through the combined alerts
                     endpoint.  Each alert's numeric severity (0-100) is
                     bucketed into low / medium / high / critical.
    - RTR Audit      Counts Real Time Response admin sessions per host.
                     Optional; skip with --no-rtr.
    - Spotlight      Per-host vulnerability counts by CVSS severity plus
                     CISA Known Exploited Vulnerabilities (KEV) status.
                     Optional; skip with --no-spotlight.
    - Zero Trust     Per-host Zero Trust Assessment posture scores.
                     Optional; skip with --no-zta.

Activity Score:
    A composite score is calculated for each host so results can be ranked
    by a single sortable metric.  The formula weights each signal:

    - Severity-weighted alerts:
        low * 1, medium * 2, high * 5, critical * 10
    - RTR sessions:        each * 5
    - Spotlight vulns:     critical * 15, high * 8, CISA KEV * 40
    - ZTA posture penalty: score < 30 adds +40, score < 60 adds +15
    - Recency bonus:       last seen < 1 hr +100, < 24 hr +50, < 72 hr +25

    Hosts are classified into three tiers based on their score:
    high activity (> 300), moderate activity (> 200), or normal activity.

High activity hosts may indicate:
    - Security incident investigation targets
    - Frequently administered endpoints
    - Mission-critical servers requiring monitoring
    - Compromised systems generating alerts

Display Modes:
    Simple (default when rich is not installed, or with --simple):
        Sequential pipeline that fetches all data before rendering a
        static tabulate-formatted table.

    Interactive (default when rich and readchar are installed):
        Progressive-loading mode.  Host IDs and metadata are fetched
        first (fast path), then alert, RTR, Spotlight, and ZTA data
        are enriched in a background daemon thread.  The interactive
        table renders immediately and updates live as pages of data
        arrive through incremental callbacks.

        If the interactive UI crashes at runtime, the script falls back
        to simple mode automatically.

Output:
    Results are displayed in the console and can optionally be exported
    to CSV (--output) with flattened severity, vulnerability, and ZTA
    columns for integration with SIEMs or reporting tools.

Demo Mode:
    Use the --demo flag to run without valid API credentials.  Generates
    deterministic synthetic data that mirrors the real pipeline's output
    structure, including severity breakdowns, Spotlight counts, and ZTA
    scores.

Requirements:
    crowdstrike-falconpy >= 1.3.0
    tabulate

Optional (for interactive mode):
    rich
    readchar

Created by: Manjula Wickramasuriya (@Manjula101) - Enterprise Security Lab
Modified and then overarchitected by: jshcodes@CrowdStrike
"""
import os
import sys
import csv
import logging
from datetime import datetime, timedelta
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from typing import List, Dict, Optional
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Thread

# Deferred imports: these are set to None at module level so the script can
# display --help output without requiring third-party packages to be installed.
# They are populated inside main() after argument parsing succeeds.
tabulate = None          # tabulate library for formatted console tables
Indicator = None         # FalconPy progress indicator (spinner animation)
Hosts = None             # FalconPy Hosts Service Class
Alerts = None            # FalconPy Alerts Service Class
RealTimeResponseAudit = None  # FalconPy RTR Audit Service Class
SpotlightVulnerabilities = None  # FalconPy Spotlight Service Class
ZeroTrustAssessment = None       # FalconPy ZTA Service Class


def consume_arguments() -> Namespace:
    """Parse and validate command line arguments.

    Builds a comprehensive CLI with two argument groups: general options
    and API credentials.  Credentials can be supplied via flags or
    environment variables, and are only required when not running in
    ``--demo`` mode.

    Returns:
        Namespace: Parsed command line arguments containing all user
                   options for the analysis run.

    Raises:
        SystemExit: If required arguments are missing in non-demo mode,
                    or if limit/days values are not positive integers.
    """
    # Use RawTextHelpFormatter so the module docstring (ASCII art banner)
    # renders correctly in the --help output
    parser = ArgumentParser(
        description=__doc__,
        formatter_class=RawTextHelpFormatter
    )

    # --demo: Allow users to see the script's output without needing
    # real CrowdStrike API credentials; uses synthetic sample data
    parser.add_argument(
        "-d", "--demo",
        help="Run in demo mode with sample data "
             "(no API credentials required)",
        action="store_true",
        default=False
    )
    # --limit: Controls how many of the top-scoring hosts appear in
    # the final results table; keeps output manageable for large envs
    parser.add_argument(
        "-l", "--limit",
        help="Number of top active hosts to display (default: 10)",
        type=int,
        default=10
    )
    # --days: Sets the look-back window for all queries (hosts, alerts,
    # RTR sessions); shorter windows focus on recent activity
    parser.add_argument(
        "-t", "--days",
        help="Number of days to analyze for activity (default: 7)",
        type=int,
        default=7
    )
    # --output: When provided, results are written to a CSV file in
    # addition to console display, enabling integration with SIEMs or
    # reporting tools
    parser.add_argument(
        "-o", "--output",
        help="Output CSV file path (optional, displays to console "
             "if not provided)",
        default=None
    )
    # --filter: Appended to the built-in date-range FQL filter so
    # users can scope results (e.g., platform_name:'Windows')
    parser.add_argument(
        "-f", "--filter",
        help="Additional FQL filter to apply to host query",
        default=None
    )
    # --table_format: Passed directly to the tabulate library; lets
    # users pick Markdown, RST, HTML, etc. for easy copy-paste
    parser.add_argument(
        "--table_format",
        help="Table format for console output (default: simple)",
        choices=['plain', 'simple', 'grid', 'fancy_grid',
                 'pipe', 'orgtbl', 'rst', 'mediawiki',
                 'html', 'latex'],
        default="simple"
    )
    # --sort: Overrides the default activity_score descending sort;
    # useful when you care more about alert count or recency
    parser.add_argument(
        "--sort",
        help="Sort results by field (default: activity_score)",
        choices=['hostname', 'activity_score', 'alerts',
                 'rtr_sessions', 'last_seen'],
        default="activity_score"
    )
    # --no-rtr: Skips the RTR Audit API call, which requires extra
    # permissions; useful for read-only API keys
    parser.add_argument(
        "--no-rtr",
        help="Skip RTR session analysis (faster but less complete)",
        action="store_true",
        default=False
    )
    # --no-spotlight: Skips the Spotlight API call, which requires extra
    # permissions; useful when vulnerability data is not needed
    parser.add_argument(
        "--no-spotlight",
        help="Skip Spotlight vulnerability analysis",
        action="store_true",
        default=False
    )
    # --no-zta: Skips the Zero Trust Assessment API call
    parser.add_argument(
        "--no-zta",
        help="Skip Zero Trust Assessment analysis",
        action="store_true",
        default=False
    )
    # --workers: Tunes parallelism for alert page processing; higher
    # values speed up large environments at the cost of API rate limits
    parser.add_argument(
        "--workers",
        help="Number of parallel workers for alert processing (default: 10)",
        type=int,
        default=10
    )
    # --debug: Enables DEBUG-level logging AND FalconPy SDK debug mode,
    # which logs raw HTTP requests/responses for troubleshooting
    parser.add_argument(
        "--debug",
        help="Enable API debugging output",
        action="store_true",
        default=False
    )
    # --simple: Forces the classic tabulate-based output even when the
    # rich library is installed; helpful for piping output or CI runs
    parser.add_argument(
        "--simple",
        help="Use simple table output (disable interactive mode). "
             "Interactive mode is the default when the rich library "
             "is installed. Install rich and readchar for interactive "
             "mode: pip install rich readchar",
        action="store_true",
        default=False
    )

    # Separate argument group for API credentials so they appear
    # under their own heading in --help output
    req = parser.add_argument_group(
        "API credentials (not required in demo mode)"
    )
    # -k: CrowdStrike OAuth2 Client ID; falls back to env var so
    # credentials don't need to appear in shell history
    req.add_argument(
        "-k", "--client_id",
        help="CrowdStrike Falcon API Client ID",
        default=os.getenv("FALCON_CLIENT_ID")
    )
    # -s: CrowdStrike OAuth2 Client Secret; same env-var fallback
    req.add_argument(
        "-s", "--client_secret",
        help="CrowdStrike Falcon API Client Secret",
        default=os.getenv("FALCON_CLIENT_SECRET")
    )
    # -b: Controls which CrowdStrike cloud region to target; "auto"
    # uses the SDK's automatic region discovery via the token endpoint
    req.add_argument(
        "-b", "--base_url",
        help="CrowdStrike API base URL (default: auto-discover)",
        default=os.getenv("FALCON_BASE_URL", "auto")
    )
    # -m: For Managed Security Service Providers (MSSPs) who need to
    # query a specific child tenant rather than the parent CID
    req.add_argument(
        "-m", "--member_cid",
        help="Child CID to access (MSSP only)",
        default=None
    )

    # Execute the actual argument parsing against sys.argv
    parsed = parser.parse_args()

    # Validate credentials are provided unless in demo mode —
    # demo mode generates synthetic data so no API calls are made
    if not parsed.demo:
        if not parsed.client_id or not parsed.client_secret:
            parser.error(
                "CrowdStrike API credentials are required unless "
                "using --demo mode.\n"
                "Provide credentials using '-k' and '-s' arguments "
                "or set environment variables:\n"
                "  FALCON_CLIENT_ID\n"
                "  FALCON_CLIENT_SECRET"
            )

    # Validate positive integers — zero or negative values would
    # produce empty or nonsensical results
    if parsed.limit < 1:
        parser.error("Limit must be a positive integer")
    if parsed.days < 1:
        parser.error("Days must be a positive integer")

    return parsed


def generate_demo_data(limit: int) -> List[Dict]:
    """Generate sample data for demo mode.

    Produces synthetic host records that mirror the structure returned by
    the real API pipeline (``query_high_activity_hosts``).  Metrics are
    deterministically varied using the loop index so the output always
    looks realistic: higher-ranked hosts get more alerts and sessions,
    with a modular wobble to avoid perfectly linear decay.

    The data structure for each host dict matches what ``display_results``
    and ``export_to_csv`` expect:
        - hostname / device_id: identifying information
        - alerts / severity_breakdown: total count plus per-severity counts
        - rtr_sessions: simulated admin session count
        - activity_score: weighted composite score
        - last_seen / platform_name / os_version / local_ip: metadata
        - status: human-readable activity tier label

    Args:
        limit: Number of sample hosts to generate.

    Returns:
        List[Dict]: List of sample host dictionaries sorted by
                    activity_score descending.
    """
    # Accumulator for generated host records
    demo_hosts = []
    # Cycle through platforms to simulate a heterogeneous environment
    platforms = ['Windows', 'Linux', 'Mac']
    # Anchor point for computing relative last_seen timestamps
    base_date = datetime.utcnow()

    for i in range(limit):
        # Create a declining alert count with periodic bumps (i % 5)
        # so the distribution looks organic rather than monotonically
        # decreasing
        total_alerts = max(0, 50 - (i * 3) + (i % 5))

        # Create severity breakdown (realistic distribution) — mirrors
        # the proportions typically seen in production Falcon tenants
        critical = int(total_alerts * 0.15)  # 15% critical
        high = int(total_alerts * 0.25)  # 25% high
        medium = int(total_alerts * 0.35)  # 35% medium
        # Remainder assigned to low to guarantee counts sum correctly
        low = total_alerts - critical - high - medium  # Rest are low

        # Store the per-severity counts in the same dict shape that
        # count_alerts_by_host returns from real API data
        severity_breakdown = {
            'low': low,
            'medium': medium,
            'high': high,
            'critical': critical
        }

        # RTR sessions also decline with index; modular bump (i % 3)
        # simulates sporadic admin activity on mid-ranked hosts
        rtr_sessions = max(0, 15 - (i * 1) + (i % 3))
        # Spread last_seen times across the analysis window so hosts
        # have varying recency, which affects the activity score bonus
        hours_since = i * 4 + (i % 6)
        last_seen = base_date - timedelta(hours=hours_since)

        # Calculate activity score using the same severity multipliers
        # as calculate_activity_score to keep demo output consistent
        # with real results
        activity_score = (
            (low * 1) + (medium * 2) + (high * 5) + (critical * 10) +
            (rtr_sessions * 5)
        )
        # Spotlight vulnerability scoring for demo data
        spotlight_critical = max(0, 5 - i)
        spotlight_high = max(0, 12 - i)
        spotlight_kev = max(0, 2 - (i // 3))
        activity_score += (
            spotlight_critical * 15 +
            spotlight_high * 8 +
            spotlight_kev * 40
        )
        # ZTA scoring for demo data
        zta_overall = max(10, 95 - (i * 8))
        if zta_overall < 30:
            activity_score += 40
        elif zta_overall < 60:
            activity_score += 15
        # Recent hosts get a bonus, matching the real scoring logic
        if hours_since < 24:
            activity_score += 50

        # Build the host dict with all fields that display_results
        # and export_to_csv reference
        demo_hosts.append({
            # Zero-padded hostname for consistent column width
            'hostname': f'HOST{str(i+1).zfill(6)}.example.com',
            # Fake device ID; zero-padded to 32 chars like a real UUID
            'device_id': f'demo{str(i+1).zfill(32)}',
            'alerts': total_alerts,
            'severity_breakdown': severity_breakdown,
            'rtr_sessions': rtr_sessions,
            'activity_score': activity_score,
            # ISO 8601 format matching the Falcon API response
            'last_seen': last_seen.strftime('%Y-%m-%dT%H:%M:%SZ'),
            # Round-robin platform assignment
            'platform_name': platforms[i % 3],
            # Alternate between "Server" and "10" to simulate mixed
            # workstation/server environments
            'os_version': (f'{platforms[i % 3]} '
                          f'{"Server" if i % 4 == 0 else "10"}'),
            # Deterministic IPs that wrap at .254 and increment subnet
            'local_ip': f'192.168.{(i // 254) + 1}.{(i % 254) + 1}',
            # Three-tier status label matching the real scoring thresholds
            'status': (
                'high activity' if activity_score > 300
                else 'moderate activity' if activity_score > 200
                else 'normal activity'
            ),
            'spotlight_vulns': {
                'critical': max(0, 5 - i),
                'high': max(0, 12 - i),
                'medium': max(0, 20 - (i * 2)),
                'low': max(0, 8 - i),
                'cisa_kev': max(0, 2 - (i // 3)),
                'total': max(0, 45 - (i * 3))
            },
            'zta_score': {
                'overall': max(10, 95 - (i * 8)),
                'sensor_config': max(15, 90 - (i * 7)),
                'os_signal': max(20, 92 - (i * 6))
            },
        })

    # Return hosts sorted highest activity first, matching the real
    # pipeline's sort order
    return sorted(demo_hosts, key=lambda x: x['activity_score'],
                  reverse=True)


def fetch_device_details(
    hosts_api: "Hosts",
    device_ids: List[str],
    max_workers: int = 5
) -> Dict[str, Dict]:
    """Fetch device details in parallel batches.

    The Falcon Hosts API returns full device metadata (hostname, OS,
    last_seen, IP, etc.) via ``get_device_details``, but each call
    accepts at most 5 000 IDs.  This function splits the full ID list
    into batches and, when multiple batches are needed, fetches them
    concurrently using a thread pool.

    Args:
        hosts_api: Authenticated Hosts service class instance.
        device_ids: List of device IDs to fetch details for.
        max_workers: Number of parallel workers for batch fetching
                     (default: 5).

    Returns:
        Dict[str, Dict]: Mapping of device_id to a normalized device
                         details dict with default counters for alerts,
                         rtr_sessions, and activity_score (populated
                         later by the enrichment step).
    """
    # Accumulator keyed by device_id for O(1) lookup during enrichment
    hosts_by_id = {}
    logging.info("Fetching device details for %d devices", len(device_ids))

    # Split into batches of 5000 (API maximum per request) to stay
    # within the Falcon API's per-call payload limit
    batch_size = 5000
    batches = [
        device_ids[i:i+batch_size]
        for i in range(0, len(device_ids), batch_size)
    ]

    logging.info(
        "Processing %d device detail batches of up to %d IDs",
        len(batches), batch_size
    )

    # For single batch, no need for parallel execution — avoids thread
    # pool overhead when the entire ID list fits in one API call
    if len(batches) == 1:
        try:
            # Iterate over the pythonic result; each item is a device dict
            for device in hosts_api.get_device_details(ids=device_ids):
                # Normalize into a flat dict with safe defaults so
                # downstream code never has to handle missing keys
                hosts_by_id[device['device_id']] = {
                    'device_id': device['device_id'],
                    'hostname': device.get('hostname', 'Unknown'),
                    'last_seen': device.get('last_seen', 'Unknown'),
                    'platform_name': device.get('platform_name', 'Unknown'),
                    'os_version': device.get('os_version', 'Unknown'),
                    'local_ip': device.get('local_ip', 'Unknown'),
                    # Counters initialized to zero; enrichment fills these
                    'alerts': 0,
                    'rtr_sessions': 0,
                    'activity_score': 0
                }
        except Exception as err:  # pylint: disable=broad-except
            # Broad catch because various HTTP/auth errors are possible
            logging.error("Error fetching device details: %s", err)
    else:
        # Multiple batches — fetch in parallel to reduce wall-clock time
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit each batch as its own future and map it back to an
            # index for logging purposes
            future_to_batch = {
                executor.submit(
                    hosts_api.get_device_details,
                    ids=batch
                ): idx
                for idx, batch in enumerate(batches)
            }

            # Process futures as they complete (not necessarily in order)
            for future in as_completed(future_to_batch):
                batch_idx = future_to_batch[future]
                try:
                    # Same normalization as the single-batch path
                    for device in future.result():
                        hosts_by_id[device['device_id']] = {
                            'device_id': device['device_id'],
                            'hostname': device.get('hostname', 'Unknown'),
                            'last_seen': device.get('last_seen', 'Unknown'),
                            'platform_name': (
                                device.get('platform_name', 'Unknown')
                            ),
                            'os_version': device.get('os_version', 'Unknown'),
                            'local_ip': device.get('local_ip', 'Unknown'),
                            'alerts': 0,
                            'rtr_sessions': 0,
                            'activity_score': 0
                        }
                    logging.debug(
                        "Completed device batch %d", batch_idx + 1
                    )
                except Exception as err:  # pylint: disable=broad-except
                    # Log and continue — partial results are still useful
                    logging.warning(
                        "Error fetching device batch %d: %s",
                        batch_idx + 1, err
                    )

    logging.info("Fetched details for %d devices", len(hosts_by_id))
    return hosts_by_id


def query_high_activity_hosts(
    hosts_api: "Hosts",
    alerts_api: "Alerts",
    rtr_api: Optional["RealTimeResponseAudit"],
    days: int,
    limit: int,
    additional_filter: Optional[str] = None,
    max_workers: int = 10,
    spotlight_api=None,
    zta_api=None
) -> List[Dict]:
    """Query Falcon APIs for hosts with high activity.

    Implements the "simple mode" sequential pipeline (used when the
    interactive UI is unavailable or ``--simple`` is set).  The pipeline
    has four numbered steps printed to the console:

    1. Paginate through ``query_devices_by_filter`` to collect ALL device
       IDs that match the date/FQL filter.
    2. Fetch full device metadata via ``fetch_device_details``.
    3. Count alerts per device via ``count_alerts_by_host``.
    4. Count RTR sessions per device via ``count_rtr_sessions_by_host``
       (skipped if ``rtr_api`` is None).

    Steps 2-4 run concurrently inside a thread pool to minimize total
    wall-clock time.

    Args:
        hosts_api: Authenticated Hosts service class instance.
        alerts_api: Authenticated Alerts service class instance.
        rtr_api: Authenticated RTR Audit service class or None.
        days: Number of days to analyze.
        limit: Maximum number of hosts to return.
        additional_filter: Optional additional FQL filter string.
        max_workers: Parallel workers for alert page processing.

    Returns:
        tuple: (top_hosts list, total_analyzed int) where top_hosts
               contains at most ``limit`` host dicts sorted by score.
    """
    # Calculate the date range for the query — all timestamps are UTC
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    # FQL (Falcon Query Language) date filter using '>=' for inclusive start
    date_filter = f"last_seen:>='{start_date.strftime('%Y-%m-%d')}'"

    # Build the FQL filter — '+' is the FQL AND operator
    fql_filter = date_filter
    if additional_filter:
        # Append user-supplied filter to narrow results further
        fql_filter = f"{date_filter}+{additional_filter}"

    logging.info("Querying ALL hosts with filter: %s", fql_filter)

    # Step 1: Get ALL device IDs (paginate if necessary) — the Hosts
    # API only returns IDs here, not full details (two-step pattern)
    all_device_ids = []
    offset = 0
    batch_size = 5000  # API max per page

    # Print progress inline; \r overwrites the line as counts grow
    print("\n[1/4] Querying hosts...", end="", flush=True)
    while True:
        # query_devices_by_filter returns only IDs (lightweight);
        # sort by last_seen descending so most-recent hosts come first
        device_ids_result = hosts_api.query_devices_by_filter(
            filter=fql_filter,
            limit=batch_size,
            offset=offset,
            sort="last_seen.desc"
        )

        # Empty result or no data means we have exhausted all pages
        if not device_ids_result or not device_ids_result.data:
            break

        # Convert the pythonic result to a plain list for accumulation
        batch = list(device_ids_result.data)
        all_device_ids.extend(batch)
        # Overwrite the progress line with updated total
        print(
            f"\r[1/4] Querying hosts... {len(all_device_ids)} found",
            end="", flush=True
        )
        logging.info("Retrieved %d device IDs (total: %d)",
                     len(batch), len(all_device_ids))

        # Stop if we got less than batch size (last page) — the API
        # returns fewer results only when no more pages remain
        if len(batch) < batch_size:
            break

        # Advance offset for next page of device IDs
        offset += batch_size

    # Early return if no hosts match the filter
    if not all_device_ids:
        print("\r[1/4] Querying hosts... 0 found")
        logging.warning("No devices found matching filter")
        return []

    print(f"\r[1/4] Querying hosts... {len(all_device_ids)} found ✓")
    logging.info("Total devices to analyze: %d", len(all_device_ids))

    # Steps 2-4: Fetch data in parallel — device details, alerts, and
    # RTR sessions are independent of each other, so run concurrently
    progress = Indicator(style="moon")  # pylint: disable=not-callable
    # Show a spinner while the three parallel jobs run
    print(f"[2-4] Fetching host data in parallel... {progress}",
          end="", flush=True)

    # Initialize result containers — populated by the futures below
    hosts_by_id = {}
    alert_counts = {}
    severity_counts = {}
    missing_sev = 0
    rtr_counts = {}

    # Use 3 workers max because there are exactly 3 independent tasks
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Launch all three steps concurrently using futures
        future_to_step = {}

        # Step 2: Fetch full device metadata for all discovered IDs
        future_details = executor.submit(
            fetch_device_details,
            hosts_api,
            all_device_ids
        )
        future_to_step[future_details] = 'details'

        # Step 3: Count alerts per host with severity breakdown
        future_alerts = executor.submit(
            count_alerts_by_host,
            alerts_api,
            all_device_ids,
            start_date,
            max_workers
        )
        future_to_step[future_alerts] = 'alerts'

        # Step 4: Count RTR sessions (only if the API object exists)
        if rtr_api:
            future_rtr = executor.submit(
                count_rtr_sessions_by_host,
                rtr_api,
                all_device_ids,
                start_date
            )
            future_to_step[future_rtr] = 'rtr'

        # Wait for all to complete and display as they finish — print
        # each step's result on its own line for clear progress feedback
        for future in as_completed(future_to_step.keys()):
            step = future_to_step[future]

            if step == 'details':
                # Unpack the device_id -> host dict mapping
                hosts_by_id = future.result()
                print(f"\n[2/4] Device details complete: "
                      f"{len(hosts_by_id)} hosts ✓" + " " * 20)

            elif step == 'alerts':
                # Unpack the three-tuple: per-host counts, severities,
                # and count of alerts that lacked severity data
                alert_counts, severity_counts, missing_sev = future.result()
                total_alerts = sum(alert_counts.values())
                print(f"\n[3/4] Alerts complete: {total_alerts} alerts "
                      f"found ✓")

            elif step == 'rtr':
                # Unpack RTR session counts per device
                rtr_counts = future.result()
                total_rtr = sum(rtr_counts.values())
                print(f"\n[4/4] RTR sessions complete: {total_rtr} "
                      f"sessions found ✓")

        # Handle no-rtr case — when the user passed --no-rtr or RTR
        # API authentication failed, skip RTR entirely
        if not rtr_api:
            rtr_counts = {}
            print("[4/4] Skipping RTR session analysis (--no-rtr)")
            logging.info("Skipping RTR session analysis (--no-rtr)")

    # Merge results into hosts_by_id — alerts and RTR counts were
    # collected separately and now need to be attached to each host
    for device_id, count in alert_counts.items():
        if device_id in hosts_by_id:
            hosts_by_id[device_id]['alerts'] = count
            # Store severity breakdown for activity scoring — defaults
            # to all-zero dict if the device had no severity data
            hosts_by_id[device_id]['severity_breakdown'] = (
                severity_counts.get(
                    device_id,
                    {'low': 0, 'medium': 0, 'high': 0, 'critical': 0}
                )
            )

    # Merge RTR session counts into each host's record
    for device_id, count in rtr_counts.items():
        if device_id in hosts_by_id:
            hosts_by_id[device_id]['rtr_sessions'] = count

    # Merge Spotlight vulnerability data
    if spotlight_api:
        print("\n[5/6] Fetching Spotlight vulnerabilities...",
              end="", flush=True)
        try:
            spotlight_data = fetch_spotlight_by_host(
                spotlight_api, all_device_ids
            )
            for device_id, vulns in spotlight_data.items():
                if device_id in hosts_by_id:
                    hosts_by_id[device_id]['spotlight_vulns'] = vulns
            if spotlight_data:
                print(f"\r[5/6] Spotlight complete: "
                      f"{len(spotlight_data)} hosts with vulns ✓")
            else:
                print("\r[5/6] Spotlight: no data returned "
                      "(check API scopes)")
        except Exception as spotlight_err:
            print(f"\r[5/6] Spotlight error: {spotlight_err}")

    # Merge ZTA score data
    if zta_api:
        print("\n[6/6] Fetching Zero Trust scores...",
              end="", flush=True)
        try:
            zta_data = fetch_zta_scores_by_host(
                zta_api, all_device_ids
            )
            for device_id, scores in zta_data.items():
                if device_id in hosts_by_id:
                    hosts_by_id[device_id]['zta_score'] = scores
            if zta_data:
                print(f"\r[6/6] ZTA complete: "
                      f"{len(zta_data)} hosts scored ✓")
            else:
                print("\r[6/6] ZTA: no data returned "
                      "(check API scopes)")
        except Exception as zta_err:
            print(f"\r[6/6] ZTA error: {zta_err}")

    # Step 5: Calculate activity scores — the composite score combines
    # severity-weighted alerts, RTR sessions, and recency bonus
    print("\nCalculating activity scores...", end="", flush=True)
    enriched_hosts = []
    for host in hosts_by_id.values():
        # Compute the weighted score for this host
        score = calculate_activity_score(host, days)
        host['activity_score'] = score
        # Three-tier status system for quick visual triage
        if score > 300:
            host['status'] = 'high activity'
        elif score > 200:
            host['status'] = 'moderate activity'
        else:
            host['status'] = 'normal activity'
        enriched_hosts.append(host)

    print("\rCalculating activity scores... done ✓")

    # Log info about missing severity data if any — these alerts were
    # defaulted to 'medium' severity in count_alerts_by_host
    if missing_sev > 0:
        logging.info(
            "%d alerts missing severity data (defaulted to medium)",
            missing_sev
        )

    # Sort by activity score descending so highest-risk hosts come first
    enriched_hosts.sort(key=lambda x: x['activity_score'],
                        reverse=True)

    # Return top N hosts plus total count analyzed so the display
    # layer can show "top 10 of 5,342 hosts analyzed"
    return enriched_hosts[:limit], len(enriched_hosts)


def count_alerts_by_host(
    alerts_api: "Alerts",
    device_ids: List[str],
    start_date: datetime,
    max_workers: int = 10,
    quiet: bool = False,
    progress_callback=None,
    incremental_callback=None
) -> tuple:
    """Count alerts per host by severity, processing pages as they arrive.

    Uses the combined alerts endpoint with cursor-based (``after``)
    pagination, which avoids the 10 000-result ceiling imposed by
    offset-based pagination.  Each page of results is processed
    immediately via ``process_page`` so that partial alert/severity
    counts can be surfaced to the interactive UI through the optional
    ``incremental_callback`` before all pages have been fetched.

    Severity mapping (numeric Falcon severity -> bucket):
        - 0-30   -> low
        - 31-60  -> medium
        - 61-80  -> high
        - 81-100 -> critical
        - None   -> medium (conservative default for missing data)

    Args:
        alerts_api: Authenticated Alerts service class instance.
        device_ids: List of device IDs to query.
        start_date: Start date for alert query.
        max_workers: Unused (kept for API compatibility with callers
                     that were written for the earlier threaded design).
        quiet: Suppress stdout progress messages (used when the
               interactive UI handles its own progress display).
        progress_callback: Optional callable(loaded_count) invoked after
                           each page for external progress tracking.
        incremental_callback: Optional callable(alert_counts, severity_counts)
            invoked after each page is processed, allowing the caller to
            apply partial results to host dicts incrementally.

    Returns:
        tuple: (alert_counts, severity_counts, missing_severity_count) where:
            - alert_counts: Dict[str, int] mapping device_id to total alerts
            - severity_counts: Dict[str, Dict[str, int]] mapping device_id
              to severity breakdown {'low': X, 'medium': Y, 'high': Z,
              'critical': W}
            - missing_severity_count: int count of alerts with missing
              severity data
    """
    # defaultdict(int) auto-initializes unseen device_ids to 0
    alert_counts = defaultdict(int)
    # Nested defaultdict creates a fresh severity bucket dict per device
    severity_counts = defaultdict(
        lambda: {'low': 0, 'medium': 0, 'high': 0, 'critical': 0}
    )
    # Track how many alerts had no severity field for QA logging
    missing_severity_count = 0
    # Convert to set for O(1) membership checks inside the hot loop
    device_id_set = set(device_ids)

    # Time filter for alerts — only include alerts created on or after
    # the analysis start date
    alert_filter = (
        f"created_timestamp:>='{start_date.strftime('%Y-%m-%d')}'"
    )

    # FalconPy Indicator helper for animated spinner in progress output
    progress = Indicator(style="moon")  # pylint: disable=not-callable

    def process_page(alerts: List[Dict]):
        """Process a single page of alerts into running accumulators.

        Classifies each alert's numeric severity into a named bucket
        and increments the per-device counters.  Modifies the outer
        ``alert_counts``, ``severity_counts``, and
        ``missing_severity_count`` via closure.
        """
        nonlocal missing_severity_count
        for alert in alerts:
            device_id = None
            severity = None

            # Alerts may come in different shapes depending on the
            # endpoint version; try multiple paths to extract device_id
            if isinstance(alert, dict):
                # Primary: nested device object (combined endpoint)
                # Fallback 1: host_ids list (legacy format)
                # Fallback 2: flat device_id field
                device_id = (
                    alert.get('device', {}).get('device_id') or
                    alert.get('host_ids', [None])[0] or
                    alert.get('device_id')
                )
                # Numeric severity (0-100 scale)
                severity = alert.get('severity')

            # Only count alerts that belong to hosts in our query set
            if device_id and device_id in device_id_set:
                alert_counts[device_id] += 1

                # Map numeric severity to named bucket
                if severity is None:
                    # Default to medium when severity is missing to
                    # avoid under-counting risk
                    severity_counts[device_id]['medium'] += 1
                    missing_severity_count += 1
                elif severity <= 30:
                    severity_counts[device_id]['low'] += 1
                elif severity <= 60:
                    severity_counts[device_id]['medium'] += 1
                elif severity <= 80:
                    severity_counts[device_id]['high'] += 1
                else:
                    # 81-100: most dangerous alerts
                    severity_counts[device_id]['critical'] += 1

    try:
        logging.info("Counting alerts with filter: %s", alert_filter)

        # Cursor token for cursor-based pagination (None = first page)
        after_token = None
        # 500 per page balances throughput vs. memory usage
        limit = 500
        page_count = 0
        total_alerts = 0

        # Paginate through all alert pages until exhausted
        while True:
            try:
                # Use cursor-based pagination: pass 'after' token on
                # subsequent pages to continue from where we left off
                if after_token:
                    result = alerts_api.get_alerts_combined(
                        filter=alert_filter,
                        limit=limit,
                        after=after_token
                    )
                else:
                    # First page — no cursor token yet
                    result = alerts_api.get_alerts_combined(
                        filter=alert_filter,
                        limit=limit
                    )

                # Null result means the API returned nothing useful
                if not result:
                    break

                # Handle both pythonic (result.data) and raw dict
                # response formats from FalconPy
                if hasattr(result, 'data'):
                    # Pythonic mode: result is a Result object
                    alerts = result.data
                    # Extract the cursor for the next page
                    after_token = (result.meta.after
                                   if hasattr(result, 'meta') else None)
                else:
                    # Raw dict mode: dig into the JSON body
                    alerts = result.get('body', {}).get('resources', [])
                    meta = result.get('body', {}).get('meta', {})
                    after_token = meta.get('pagination', {}).get('after')

                # No alerts on this page means we have reached the end
                if not alerts:
                    break

                page_count += 1
                total_alerts += len(alerts)

                # Process page immediately — results accumulate
                # into alert_counts and severity_counts so partial
                # data is available even if later pages fail
                process_page(alerts)

                # Update inline progress indicator if not suppressed
                if not quiet:
                    print(
                        f"\r[3/4] Counting alerts per host... "
                        f"{progress} "
                        f"({total_alerts} found, page {page_count})",
                        end="", flush=True
                    )

                # Notify external progress tracker (e.g., LoadingState)
                if progress_callback:
                    progress_callback(len(alert_counts))

                # Fire incremental callback so caller can update
                # host dicts with partial results after each page —
                # this enables the interactive UI to show live scores
                if incremental_callback:
                    incremental_callback(
                        dict(alert_counts),
                        dict(severity_counts)
                    )

                logging.debug("Fetched page %d with %d alerts",
                              page_count, len(alerts))

                # No cursor token means this was the last page
                if not after_token:
                    break

            except Exception as err:  # pylint: disable=broad-except
                # Log and break — partial results collected so far
                # are still returned to the caller
                logging.warning("Error fetching alerts page: %s", err)
                break

        # If no pages were fetched at all, return empty results
        if page_count == 0:
            logging.info("No alerts found in time range")
            return dict(alert_counts), dict(severity_counts), 0

        logging.info(
            "Retrieved alert counts for %d devices with %d total "
            "alerts from %d pages",
            len(alert_counts), total_alerts, page_count
        )

        # Warn if any alerts were missing severity — helps operators
        # identify data quality issues in their Falcon tenant
        if missing_severity_count > 0:
            logging.warning(
                "%d alerts had missing severity data (defaulted to medium)",
                missing_severity_count
            )

    except Exception as err:  # pylint: disable=broad-except
        # Outer catch for unexpected failures (auth, network, etc.)
        logging.warning("Error counting alerts: %s", err)

    # Convert defaultdicts to regular dicts for cleaner serialization
    return dict(alert_counts), dict(severity_counts), missing_severity_count


def count_rtr_sessions_by_host(
    rtr_api: "RealTimeResponseAudit",
    device_ids: List[str],
    start_date: datetime
) -> Dict[str, int]:
    """Count RTR sessions per host using RTR Audit API.

    Real Time Response (RTR) sessions represent interactive admin
    sessions where an analyst connected to a host.  High session counts
    often indicate active incident investigation or heavy administrative
    maintenance.

    Note: The RTR Audit API requires specific RBAC permissions
    (``Real Time Response Audit: Read``).  If the caller's API key
    lacks this scope, the function logs a warning and returns an empty
    dict so the rest of the pipeline can still complete.

    Args:
        rtr_api: Authenticated RTR Audit service class instance.
        device_ids: List of device IDs to query.
        start_date: Start date for session query.

    Returns:
        Dict[str, int]: Mapping of device_id to session count.  Empty
                        dict if the API call fails or returns no data.
    """
    # Auto-initializing counter; unseen devices default to 0
    session_counts = defaultdict(int)

    # Query RTR sessions created on or after the analysis start date;
    # ISO 8601 format required by the RTR Audit filter syntax
    session_filter = (
        f"created_at:>='{start_date.strftime('%Y-%m-%dT%H:%M:%SZ')}'"
    )

    try:
        # Fetch audit session records — limit set to API maximum (1000)
        sessions_result = rtr_api.audit_sessions(
            filter=session_filter,
            limit="1000"  # API max per request
        )

        # Only process if the API returned a non-empty response
        if sessions_result and sessions_result.data:
            for session in sessions_result.data:
                # Extract the device_id from each session record
                device_id = session.get('device_id')
                # Only count sessions for devices in our query set to
                # avoid inflating counts with unrelated hosts
                if device_id and device_id in device_ids:
                    session_counts[device_id] += 1

    except Exception as err:
        # RTR Audit often fails due to missing permissions — log
        # clearly so the user knows to check their API key scopes
        logging.warning("Error querying RTR sessions: %s", err)
        logging.warning("RTR audit may require additional permissions")

    # Convert to regular dict for consistent return type
    return dict(session_counts)


def fetch_spotlight_by_host(
    spotlight_api: "SpotlightVulnerabilities",
    device_ids: List[str],
    incremental_callback=None
) -> Dict[str, Dict]:
    """Fetch Spotlight vulnerability counts per host.

    Queries the Spotlight Vulnerabilities API to get a per-host
    breakdown of vulnerability severity and CISA KEV status.

    Args:
        spotlight_api: Authenticated SpotlightVulnerabilities service class.
        device_ids: List of device IDs to query.
        incremental_callback: Optional callable invoked after each PAGE
            of vulnerability data is processed (during pagination within
            each batch of AIDs). The callback receives the accumulated
            vuln_by_host dict, enabling the UI to show results as pages
            arrive rather than waiting for entire batches to complete.

    Returns:
        Dict mapping device_id to vulnerability summary dict with keys:
        critical, high, medium, low, cisa_kev, total.
    """
    vuln_by_host = {}
    device_id_set = set(device_ids)

    if not device_ids:
        return vuln_by_host

    try:
        # Process device IDs in batches to stay within API limits
        first_batch_size = min(10, len(device_ids))
        batch_size = 100

        # Priority batch: first 10 hosts (already sorted by score)
        batches = [device_ids[:first_batch_size]]
        # Remaining in normal chunks, starting after the priority batch
        remaining = device_ids[first_batch_size:]
        for i in range(0, len(remaining), batch_size):
            batches.append(remaining[i:i + batch_size])

        for batch in batches:
            # Build FQL filter — use comma-separated aid values for OR
            aid_filters = [f"aid:'{aid}'" for aid in batch]
            aid_filter = ",".join(aid_filters)

            try:
                # Paginate through results using the after token
                after = None
                while True:
                    kwargs = {
                        "filter": f"status:'open'+({aid_filter})",
                        "facet": ["cve"],
                        "limit": 5000
                    }
                    if after:
                        kwargs["after"] = after

                    result = (
                        spotlight_api.query_vulnerabilities_combined(
                            **kwargs
                        )
                    )

                    if not result:
                        break

                    # Check status code — pythonic Result objects are
                    # always truthy, so we must check status explicitly
                    status = getattr(result, 'status_code', None)
                    if status is None and isinstance(result, dict):
                        status = result.get('status_code')
                    if status and status != 200:
                        # Extract error details for logging
                        err_msg = ""
                        if hasattr(result, 'errors'):
                            err_msg = str(result.errors)
                        elif isinstance(result, dict):
                            errs = result.get('body', {}).get(
                                'errors', [])
                            err_msg = str(errs)
                        raise RuntimeError(
                            f"HTTP {status}: {err_msg}"
                        )

                    # Extract resources from pythonic or raw response
                    # (match the pattern used by count_alerts_by_host)
                    if hasattr(result, 'data'):
                        vulns = result.data if result.data else []
                        after = (
                            result.meta.after
                            if hasattr(result, 'meta')
                            and hasattr(result.meta, 'after')
                            else None
                        )
                    elif isinstance(result, dict):
                        body = result.get('body', {})
                        vulns = body.get('resources', [])
                        meta = body.get('meta', {})
                        after = meta.get(
                            'pagination', {}
                        ).get('after')
                    else:
                        break

                    for vuln in vulns:
                        if not isinstance(vuln, dict):
                            continue
                        aid = vuln.get('aid')
                        if not aid or aid not in device_id_set:
                            continue

                        if aid not in vuln_by_host:
                            vuln_by_host[aid] = {
                                'critical': 0, 'high': 0,
                                'medium': 0, 'low': 0,
                                'cisa_kev': 0, 'total': 0
                            }

                        vuln_by_host[aid]['total'] += 1

                        # Classify by CVSS base score from cve facet
                        cve = vuln.get('cve', {})
                        severity = cve.get('base_score', 0)
                        if severity >= 9.0:
                            vuln_by_host[aid]['critical'] += 1
                        elif severity >= 7.0:
                            vuln_by_host[aid]['high'] += 1
                        elif severity >= 4.0:
                            vuln_by_host[aid]['medium'] += 1
                        else:
                            vuln_by_host[aid]['low'] += 1

                        # Check CISA KEV status
                        cisa = cve.get('cisa_info', {})
                        if cisa and cisa.get('is_cisa_kev'):
                            vuln_by_host[aid]['cisa_kev'] += 1

                    # Fire incremental callback after each page
                    if incremental_callback:
                        incremental_callback(vuln_by_host)

                    # Stop if no pagination token
                    if not after:
                        break

            except Exception as batch_err:
                logging.error(
                    "Error fetching Spotlight batch: %s", batch_err
                )
                continue

    except Exception as err:
        logging.error("Error querying Spotlight: %s", err)

    return vuln_by_host


def fetch_zta_scores_by_host(
    zta_api: "ZeroTrustAssessment",
    device_ids: List[str]
) -> Dict[str, Dict]:
    """Fetch Zero Trust Assessment scores per host.

    Queries the ZTA API using get_assessments_by_score to retrieve
    overall ZTA scores, then filters to just our target device IDs.
    The API doesn't support filtering by aid directly, so we fetch
    all scores and match client-side.

    Args:
        zta_api: Authenticated ZeroTrustAssessment service class.
        device_ids: List of device IDs to query.

    Returns:
        Dict mapping device_id to ZTA summary dict with keys:
        overall, sensor_config, os_signal.
    """
    zta_by_host = {}
    device_id_set = set(device_ids)
    target_count = len(device_id_set)

    try:
        after = None
        while True:
            kwargs = {
                "filter": "score:>=0",
                "limit": 1000
            }
            if after:
                kwargs["after"] = after

            result = zta_api.get_assessments_by_score(**kwargs)

            if not result:
                break

            # Check status code — pythonic Result objects are
            # always truthy, so we must check status explicitly
            status = getattr(result, 'status_code', None)
            if status is None and isinstance(result, dict):
                status = result.get('status_code')
            if status and status != 200:
                err_msg = ""
                if hasattr(result, 'errors'):
                    err_msg = str(result.errors)
                elif isinstance(result, dict):
                    errs = result.get('body', {}).get(
                        'errors', [])
                    err_msg = str(errs)
                raise RuntimeError(
                    f"HTTP {status}: {err_msg}"
                )

            # Extract resources from response
            # (match the pattern used by count_alerts_by_host)
            if isinstance(result, dict):
                body = result.get('body', {})
                assessments = body.get('resources', [])
                meta = body.get('meta', {})
                paging = meta.get('pagination', {})
                after = paging.get('after')
            elif hasattr(result, 'data'):
                assessments = (
                    result.data if result.data else []
                )
                after = (
                    result.meta.after
                    if hasattr(result, 'meta')
                    and hasattr(result.meta, 'after')
                    else None
                )
            else:
                break

            if not assessments:
                break

            for entry in assessments:
                if not isinstance(entry, dict):
                    continue
                aid = entry.get('aid')
                if not aid or aid not in device_id_set:
                    continue

                overall = entry.get('score', 0)
                zta_by_host[aid] = {
                    'overall': overall,
                    'sensor_config': 0,
                    'os_signal': 0
                }

            # Stop early if we found all our target hosts
            if len(zta_by_host) >= target_count:
                break
            # Stop if no more pages
            if not after:
                break

    except Exception as err:
        logging.warning("Error querying ZTA: %s", err)

    return zta_by_host


def calculate_activity_score(host: Dict, days: int) -> int:
    """Calculate overall activity score for a host.

    The score is a single composite metric that combines three signals
    into one sortable number:

    1. **Severity-weighted alerts** -- higher-severity alerts contribute
       exponentially more to the score so that a host with one critical
       alert ranks higher than a host with several low alerts.
    2. **RTR session count** -- each session adds 5 points because admin
       activity is a meaningful (but lower-weight) signal.
    3. **Recency bonus** -- hosts that checked in recently get a bonus
       because they represent live, actionable endpoints:
       - < 1 hour  -> +100 points
       - < 24 hours -> +50 points
       - < 72 hours -> +25 points

    Args:
        host: Host information dictionary containing at minimum
              ``severity_breakdown``, ``rtr_sessions``, and
              ``last_seen`` keys.
        days: Number of days in the analysis period (reserved for
              future normalization; currently unused in the formula).

    Returns:
        int: Calculated activity score (higher = more active/risky).
    """
    # Start from zero; each component adds to the total
    score = 0

    # Alerts scored by severity with multipliers:
    # Low (0-30): 1x, Medium (31-60): 2x, High (61-80): 5x,
    # Critical (81-100): 10x — the exponential weighting ensures
    # critical alerts dominate the ranking
    severity_breakdown = host.get('severity_breakdown', {})
    score += severity_breakdown.get('low', 0) * 1
    score += severity_breakdown.get('medium', 0) * 2
    score += severity_breakdown.get('high', 0) * 5
    score += severity_breakdown.get('critical', 0) * 10

    # RTR sessions indicate admin activity (5 points each) — less
    # weight than alerts because sessions are operator-initiated
    score += host['rtr_sessions'] * 5

    # Spotlight vulnerability risk — critical vulns and CISA KEV items
    # add significant risk to a host's activity profile
    spotlight = host.get('spotlight_vulns', {})
    score += spotlight.get('critical', 0) * 15
    score += spotlight.get('high', 0) * 8
    score += spotlight.get('cisa_kev', 0) * 40

    # Zero Trust posture risk — low ZTA scores indicate poor security
    # configuration which increases the host's risk profile
    zta_score = host.get('zta_score', {}).get('overall', 100)
    if zta_score < 30:
        score += 40   # Poorly configured — high additional risk
    elif zta_score < 60:
        score += 15   # Moderate concern

    # Recent activity adds bonus points — prioritizes hosts that are
    # currently online so analysts can take immediate action
    last_seen = host.get('last_seen', '')
    if last_seen and last_seen != 'Unknown':
        try:
            # Parse ISO 8601 timestamp; strip fractional seconds
            # (some Falcon responses include microseconds)
            last_seen_dt = datetime.strptime(
                last_seen.split('.')[0],
                '%Y-%m-%dT%H:%M:%S'
            )
            # Calculate hours elapsed since the host last reported in
            hours_since = (
                (datetime.utcnow() - last_seen_dt).total_seconds()
                / 3600
            )
            # Tiered bonus: more recent = higher bonus
            if hours_since < 1:
                score += 100   # Very recently active — highest bonus
            elif hours_since < 24:
                score += 50    # Active today — moderate bonus
            elif hours_since < 72:
                score += 25    # Active within 3 days — small bonus
        except (ValueError, AttributeError):
            # Malformed timestamp — skip the recency bonus silently
            pass

    return score


def query_hosts_fast(
    hosts_api: "Hosts",
    days: int,
    additional_filter: Optional[str] = None,
    quiet: bool = False
) -> tuple:
    """Query and fetch host details quickly (Steps 1-2 only).

    This is the "fast path" used by the interactive UI.  It executes
    only the two fastest operations -- querying device IDs and fetching
    device details -- and returns immediately.  The slower alert and RTR
    enrichment happen later in a background thread
    (``enrich_hosts_background``) so the interactive table can render
    within seconds even for large environments.

    **Two-step host querying approach:**

    Step 1 -- ``query_devices_by_filter``: Returns only device *IDs*
    (lightweight, fast).  Paginates in 5 000-ID pages until all matching
    hosts are collected.  This is the Falcon "query" pattern: IDs first.

    Step 2 -- ``fetch_device_details``: Takes the collected IDs and
    fetches full metadata (hostname, OS, last_seen, etc.) in batches.
    This is the Falcon "get" pattern: details by ID.

    Together they implement the standard Falcon two-step query-then-get
    pattern that keeps the query call fast and the get call targeted.

    Args:
        hosts_api: Authenticated Hosts service class instance.
        days: Number of days to analyze.
        additional_filter: Optional additional FQL filter string.
        quiet: Suppress stdout progress messages (used when the
               interactive UI manages its own display).

    Returns:
        tuple: (hosts_by_id dict, all_device_ids list, start_date)
               where hosts_by_id maps device_id to host dict with
               ``_loading=True`` flag set, ready for background
               enrichment.
    """
    # Compute the UTC date window for the FQL filter
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    # Build FQL date filter: only hosts seen within the window
    date_filter = f"last_seen:>='{start_date.strftime('%Y-%m-%d')}'"

    # Combine with any user-supplied FQL filter using '+' (FQL AND)
    fql_filter = date_filter
    if additional_filter:
        fql_filter = f"{date_filter}+{additional_filter}"

    # --- Step 1: Collect ALL device IDs via paginated query ---
    all_device_ids = []
    offset = 0
    # 5000 is the API maximum per page for query_devices_by_filter
    batch_size = 5000

    if not quiet:
        print("Querying hosts...", end="", flush=True)
    while True:
        # Query for IDs only (no metadata) sorted by most recent first
        device_ids_result = hosts_api.query_devices_by_filter(
            filter=fql_filter,
            limit=batch_size,
            offset=offset,
            sort="last_seen.desc"
        )

        # No result or empty data means all pages have been consumed
        if not device_ids_result or not device_ids_result.data:
            break

        # Materialize the pythonic iterator into a list
        batch = list(device_ids_result.data)
        all_device_ids.extend(batch)
        if not quiet:
            # Overwrite the same line with updated count
            print(
                f"\rQuerying hosts... {len(all_device_ids)} found",
                end="", flush=True
            )

        # Fewer results than batch_size means this is the last page
        if len(batch) < batch_size:
            break
        # Advance offset to the next page
        offset += batch_size

    # Early return with empty containers if no hosts match
    if not all_device_ids:
        if not quiet:
            print("\rQuerying hosts... 0 found")
        return {}, [], start_date

    if not quiet:
        print(
            f"\rQuerying hosts... {len(all_device_ids)} found ✓  "
            "Fetching details...",
            end="", flush=True
        )

    # --- Step 2: Fetch full device metadata for all collected IDs ---
    hosts_by_id = fetch_device_details(hosts_api, all_device_ids)

    # Mark all hosts as loading (enrichment pending) so the interactive
    # UI can show a spinner or placeholder for alert/RTR columns
    for host in hosts_by_id.values():
        host['_loading'] = True

    if not quiet:
        print(
            f"\rQuerying hosts... {len(all_device_ids)} found ✓  "
            f"Details: {len(hosts_by_id)} hosts ✓"
        )

    # Return the partially-built host dict, the full ID list (needed
    # by the background enrichment thread), and the start date
    return hosts_by_id, all_device_ids, start_date


def enrich_hosts_background(
    hosts_by_id: Dict[str, Dict],
    all_device_ids: List[str],
    start_date: datetime,
    alerts_api: "Alerts",
    rtr_api: Optional["RealTimeResponseAudit"],
    loading_state,
    days: int,
    max_workers: int = 10,
    spotlight_api=None,
    zta_api=None
):
    """Enrich host dicts in-place with alert, RTR, Spotlight, and ZTA data.

    This function is designed to run in a daemon thread started by
    ``main()`` when interactive mode is active.  It mutates the same
    host dicts that the interactive UI is rendering, so the table
    updates live as data arrives.  Thread safety is achieved through
    the ``loading_state`` object which coordinates progress between
    this thread and the UI thread.

    All four enrichment sources run concurrently:

    - **Alerts** run in this thread with incremental callbacks for
      progressive UI updates (page-by-page).
    - **Spotlight** runs in its own thread with incremental callbacks
      for progressive UI updates (page-by-page within each batch).
    - **RTR** and **ZTA** each run in their own thread and apply
      results to host dicts when complete, so the UI reflects their
      data as soon as each API returns.

    Args:
        hosts_by_id: Mapping of device_id to host dict (modified in-place).
        all_device_ids: List of all device IDs.
        start_date: Start date for queries.
        alerts_api: Authenticated Alerts service class.
        rtr_api: Authenticated RTR Audit service class or None.
        loading_state: Thread-safe loading state tracker that the
                       interactive UI polls for progress updates.
        days: Number of days for analysis period.
        max_workers: Parallel workers for alert processing.
        spotlight_api: Authenticated SpotlightVulnerabilities or None.
        zta_api: Authenticated ZeroTrustAssessment or None.
    """
    def _recalc_score(host):
        """Recalculate activity score and status for a host."""
        score = calculate_activity_score(host, days)
        host['activity_score'] = score
        if score > 300:
            host['status'] = 'high activity'
        elif score > 200:
            host['status'] = 'moderate activity'
        else:
            host['status'] = 'normal activity'

    def _apply_partial_alerts(partial_counts, partial_severities):
        """Apply partial alert results to host dicts as they arrive."""
        for device_id, count in partial_counts.items():
            if device_id in hosts_by_id:
                host = hosts_by_id[device_id]
                host['alerts'] = count
                host['severity_breakdown'] = (
                    partial_severities.get(
                        device_id,
                        {'low': 0, 'medium': 0,
                         'high': 0, 'critical': 0}
                    )
                )
                _recalc_score(host)
                host['_loading'] = False

    _spotlight_recalc_counter = [0]  # Mutable container for closure

    def _apply_partial_spotlight(partial_vulns):
        """Apply Spotlight results to host dicts as pages complete."""
        enriched = 0
        for device_id, vulns in partial_vulns.items():
            if device_id in hosts_by_id:
                host = hosts_by_id[device_id]
                host['spotlight_vulns'] = vulns
                enriched += 1
        _spotlight_recalc_counter[0] += enriched
        # Recalculate scores every 50 hosts to avoid flicker
        if _spotlight_recalc_counter[0] >= 50:
            for did in list(hosts_by_id):
                if 'spotlight_vulns' in hosts_by_id[did]:
                    _recalc_score(hosts_by_id[did])
            _spotlight_recalc_counter[0] = 0
        loading_state.update_spotlight(enriched)

    # --- Worker functions that fetch AND apply in one shot ---
    # Each runs in its own thread and writes results directly into
    # hosts_by_id so the UI picks them up on the next render cycle.

    def _rtr_worker():
        """Fetch RTR sessions and apply to host dicts."""
        try:
            rtr_counts = count_rtr_sessions_by_host(
                rtr_api, all_device_ids, start_date
            )
            rtr_enriched = 0
            for device_id, count in rtr_counts.items():
                if device_id in hosts_by_id:
                    host = hosts_by_id[device_id]
                    host['rtr_sessions'] = count
                    _recalc_score(host)
                    rtr_enriched += 1
            loading_state.update_rtr(
                len(all_device_ids), complete=True
            )
        except Exception as err:  # pylint: disable=broad-except
            logging.error("Background RTR loading failed: %s", err)
            loading_state.update_rtr(0, complete=True)
            loading_state.set_error(f"RTR loading error: {err}")

    def _spotlight_worker():
        """Fetch Spotlight vulns and apply to host dicts."""
        try:
            logging.info(
                "Spotlight worker started for %d hosts",
                len(all_device_ids)
            )
            # Sort by current activity score so priority batch
            # targets the hosts the user is actually looking at
            sorted_ids = sorted(
                all_device_ids,
                key=lambda did: hosts_by_id.get(did, {}).get(
                    'activity_score', 0
                ),
                reverse=True
            )
            spotlight_data = fetch_spotlight_by_host(
                spotlight_api, sorted_ids,
                incremental_callback=_apply_partial_spotlight
            )
            logging.info(
                "Spotlight worker got data for %d hosts",
                len(spotlight_data)
            )
            spotlight_enriched = 0
            for device_id, vulns in spotlight_data.items():
                if device_id in hosts_by_id:
                    host = hosts_by_id[device_id]
                    host['spotlight_vulns'] = vulns
                    _recalc_score(host)
                    spotlight_enriched += 1
            # Also set empty spotlight_vulns on hosts that had no data
            # so the UI shows 0/0 instead of "--" for those hosts
            for device_id in all_device_ids:
                if (device_id in hosts_by_id
                        and 'spotlight_vulns' not in
                        hosts_by_id[device_id]):
                    hosts_by_id[device_id]['spotlight_vulns'] = {
                        'critical': 0, 'high': 0, 'medium': 0,
                        'low': 0, 'cisa_kev': 0, 'total': 0
                    }
            if not spotlight_data and all_device_ids:
                logging.warning(
                    "Spotlight returned no data for %d hosts "
                    "(check API scopes: "
                    "spotlight-vulnerabilities:read)",
                    len(all_device_ids)
                )
                loading_state.set_error(
                    "Spotlight: no data (check API scopes)"
                )
            # Final score recalculation for all hosts
            for device_id in all_device_ids:
                if device_id in hosts_by_id:
                    _recalc_score(hosts_by_id[device_id])
            # Report total host count so progress bar reaches 100%
            loading_state.update_spotlight(
                len(all_device_ids), complete=True
            )
        except Exception as err:
            logging.error(
                "Background Spotlight loading failed: %s", err
            )
            loading_state.update_spotlight(0, complete=True)
            loading_state.set_error(
                f"Spotlight loading error: {err}"
            )

    def _zta_worker():
        """Fetch ZTA scores and apply to host dicts."""
        try:
            logging.info(
                "ZTA worker started for %d hosts",
                len(all_device_ids)
            )
            zta_data = fetch_zta_scores_by_host(
                zta_api, all_device_ids
            )
            logging.info(
                "ZTA worker got data for %d hosts",
                len(zta_data)
            )
            zta_enriched = 0
            for device_id, scores in zta_data.items():
                if device_id in hosts_by_id:
                    host = hosts_by_id[device_id]
                    host['zta_score'] = scores
                    _recalc_score(host)
                    zta_enriched += 1
            # Also set empty zta_score on hosts that had no data
            # so the UI shows 0 instead of "--"
            for device_id in all_device_ids:
                if (device_id in hosts_by_id
                        and 'zta_score' not in
                        hosts_by_id[device_id]):
                    hosts_by_id[device_id]['zta_score'] = {
                        'overall': 0, 'sensor_config': 0,
                        'os_signal': 0
                    }
            if not zta_data and all_device_ids:
                logging.warning(
                    "ZTA returned no data for %d hosts "
                    "(check API scopes: "
                    "zero-trust-assessment:read)",
                    len(all_device_ids)
                )
                loading_state.set_error(
                    "ZTA: no data (check API scopes)"
                )
            # Report total host count so progress bar reaches 100%
            loading_state.update_zta(
                len(all_device_ids), complete=True
            )
        except Exception as err:
            logging.error(
                "Background ZTA loading failed: %s", err
            )
            loading_state.update_zta(0, complete=True)
            loading_state.set_error(
                f"ZTA loading error: {err}"
            )

    # --- Launch worker threads ---
    # Each thread fetches data AND applies it to host dicts, so
    # results appear in the UI as soon as each API returns.
    workers = []
    if rtr_api:
        t = Thread(target=_rtr_worker, daemon=True)
        t.start()
        workers.append(t)
    else:
        loading_state.update_rtr(0, complete=True)

    if spotlight_api:
        t = Thread(target=_spotlight_worker, daemon=True)
        t.start()
        workers.append(t)
    else:
        loading_state.update_spotlight(0, complete=True)

    if zta_api:
        t = Thread(target=_zta_worker, daemon=True)
        t.start()
        workers.append(t)
    else:
        loading_state.update_zta(0, complete=True)

    # --- Alerts: run in this thread with incremental callbacks ---
    try:
        alert_counts, severity_counts, _ = count_alerts_by_host(
            alerts_api, all_device_ids, start_date, max_workers,
            quiet=True,
            progress_callback=loading_state.update_alerts,
            incremental_callback=_apply_partial_alerts
        )

        # Final pass: apply complete results and clear loading for
        # any hosts not yet updated (including zero-alert hosts).
        for device_id, count in alert_counts.items():
            if device_id in hosts_by_id:
                host = hosts_by_id[device_id]
                host['alerts'] = count
                host['severity_breakdown'] = (
                    severity_counts.get(
                        device_id,
                        {'low': 0, 'medium': 0,
                         'high': 0, 'critical': 0}
                    )
                )
                _recalc_score(host)
                host['_loading'] = False

        # Clear loading for hosts with zero alerts
        for device_id in all_device_ids:
            if (device_id in hosts_by_id
                    and hosts_by_id[device_id].get('_loading')):
                host = hosts_by_id[device_id]
                _recalc_score(host)
                host['_loading'] = False

        loading_state.update_alerts(
            len(all_device_ids), complete=True
        )

    except Exception as err:  # pylint: disable=broad-except
        logging.error("Background alert loading failed: %s", err)
        # Clear loading flag on all hosts so the UI stops showing
        # "loading..." and renders the data that IS available
        for device_id in all_device_ids:
            if device_id in hosts_by_id:
                hosts_by_id[device_id]['_loading'] = False
        loading_state.update_alerts(
            len(all_device_ids), complete=True
        )
        loading_state.set_error(f"Alert loading error: {err}")


def display_results(
    hosts: List[Dict],
    table_format: str,
    days: int,
    limit: int,
    demo_mode: bool,
    include_rtr: bool,
    total_analyzed: int
) -> None:
    """Display results to console in formatted table.

    Renders the enriched host list as a tabulate-formatted table with
    ranked rows, severity breakdowns, and status indicators.  This is
    the "simple mode" display path (as opposed to the interactive
    rich-based UI).

    Args:
        hosts: List of host information dictionaries (already sorted).
        table_format: Table format style for tabulate (e.g., 'simple',
                      'grid', 'pipe').
        days: Number of days analyzed (shown in header).
        limit: Number of hosts displayed (shown in header).
        demo_mode: Whether running in demo mode (shows banner).
        include_rtr: Whether RTR data is included (adds column).
        total_analyzed: Total number of hosts analyzed (shown in footer).
    """
    # Print a prominent banner when in demo mode so users do not
    # mistake synthetic data for real Falcon telemetry
    if demo_mode:
        print("\n" + "=" * 80)
        print("DEMO MODE - Sample Data Only".center(80))
        print("Use without --demo flag for real API data".center(80))
        print("=" * 80 + "\n")

    # Print the section header with analysis parameters
    print(f"\nTop {limit} High Activity Hosts (Last {days} Days)")
    print("=" * 80)

    # Handle the empty-results edge case gracefully
    if not hosts:
        print("No hosts found matching the specified criteria.")
        return

    # Prepare table data — build a list of rows to pass to tabulate
    table_data = []
    # Include the RTR Sessions column only when RTR data was collected
    if include_rtr:
        headers = ['Rank', 'Hostname', 'Activity Score',
                   'Alerts (L/M/H/C)', 'RTR Sessions',
                   'Vulns (C/H)', 'ZTA', 'Last Seen',
                   'Status']
    else:
        headers = ['Rank', 'Hostname', 'Activity Score',
                   'Alerts (L/M/H/C)',
                   'Vulns (C/H)', 'ZTA', 'Last Seen',
                   'Status']

    for idx, host in enumerate(hosts, 1):
        # Format severity breakdown as "total (low/med/high/crit)"
        # for compact display in a single column
        sev = host.get('severity_breakdown',
                       {'low': 0, 'medium': 0, 'high': 0, 'critical': 0})
        alert_display = (
            f"{host['alerts']} "
            f"({sev['low']}/{sev['medium']}/{sev['high']}/{sev['critical']})"
        )

        # Format last seen date for readability — strip the 'T'
        # separator and fractional seconds from ISO 8601
        last_seen = host['last_seen']
        if isinstance(last_seen, str) and 'T' in last_seen:
            try:
                dt_obj = datetime.strptime(
                    last_seen.split('.')[0],
                    '%Y-%m-%dT%H:%M:%S'
                )
                # Show date and time without seconds for brevity
                last_seen = dt_obj.strftime('%Y-%m-%d %H:%M')
            except ValueError:
                # If parsing fails, display the raw string
                pass

        # Prepend a visual indicator based on activity tier —
        # warning icon for high/moderate, checkmark for normal
        status_msg = ("⚠️  " if host['status'] == 'high activity'
                      else "⚠️  " if host['status'] == 'moderate activity'
                      else "✓  ")

        # Build the row list; order must match headers above
        row = [
            idx,
            host['hostname'][:40],  # Truncate long hostnames to 40 chars
            host['activity_score'],
            alert_display,  # Show total with severity breakdown
        ]

        # Conditionally include RTR column to keep table compact when
        # RTR data is not available
        if include_rtr:
            row.append(host['rtr_sessions'])

        # Spotlight vulns column (critical/high)
        spot = host.get('spotlight_vulns', {})
        row.append(
            f"{spot.get('critical', 0)}/{spot.get('high', 0)}"
        )

        # ZTA score column
        zta = host.get('zta_score', {})
        row.append(zta.get('overall', '--'))

        # Append the remaining columns (shared by both layouts)
        row.extend([
            last_seen,
            f"{status_msg}{host['status']}"
        ])

        table_data.append(row)

    # Render the table using the tabulate library with column alignment
    print(  # pylint: disable=not-callable
        tabulate(
            table_data, headers=headers,
            tablefmt=table_format,
            colalign=(
                "right", "left", "right",
                "right", "right" if include_rtr else "left",
                "left" if include_rtr else "left",
                "left"
            )
        )
    )
    # Show how many hosts are displayed vs. total analyzed
    print(f"\nShowing top {len(hosts)} of {total_analyzed} "
          f"hosts analyzed")

    # Display summary statistics for the displayed subset
    total_alerts = sum(h['alerts'] for h in hosts)
    total_rtr = sum(h['rtr_sessions'] for h in hosts)

    print(f"Total alerts: {total_alerts:,}")
    if include_rtr:
        print(f"Total RTR sessions: {total_rtr:,}")
    # Trailing newline for visual separation
    print()


def export_to_csv(
    hosts: List[Dict],
    output_path: str,
    days: int,
    include_rtr: bool
) -> None:
    """Export results to CSV file.

    Writes all host records to a CSV with flattened severity columns,
    followed by comment lines summarizing the analysis.  The CSV uses
    UTF-8 encoding for broad compatibility and includes a header row.

    Args:
        hosts: List of host information dictionaries.
        output_path: Path to output CSV file.
        days: Number of days analyzed (written to summary footer).
        include_rtr: Whether RTR data is included (affects summary).

    Raises:
        SystemExit: If the file cannot be written (IOError).
    """
    try:
        # Open with newline='' per csv module docs to prevent double
        # newlines on Windows; UTF-8 for international hostnames
        with open(output_path, 'w', newline='',
                  encoding='utf-8') as csvfile:
            # Handle empty results — write a placeholder message
            if not hosts:
                csvfile.write("No hosts found\n")
                print(f"Empty results exported to {output_path}")
                return

            # Define column order — severity_breakdown is flattened
            # into four separate columns for easier spreadsheet use
            fieldnames = ['rank', 'hostname', 'device_id',
                          'activity_score', 'alerts',
                          'alerts_low', 'alerts_medium', 'alerts_high',
                          'alerts_critical',
                          'rtr_sessions',
                          'spotlight_critical', 'spotlight_high',
                          'spotlight_medium', 'spotlight_low',
                          'spotlight_cisa_kev',
                          'zta_overall', 'zta_sensor_config',
                          'zta_os_signal',
                          'last_seen', 'platform_name',
                          'os_version', 'local_ip', 'status']
            # DictWriter handles mapping dict keys to column positions
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header row with column names
            writer.writeheader()

            # Write data rows — one per host
            for idx, host in enumerate(hosts, 1):
                # Copy to avoid mutating the original host dict
                row = host.copy()
                # Add rank (1-based) which is not part of the host dict
                row['rank'] = idx
                # Flatten severity breakdown into individual columns
                # so each severity level gets its own sortable column
                sev = host.get('severity_breakdown',
                               {'low': 0, 'medium': 0, 'high': 0,
                                'critical': 0})
                row['alerts_low'] = sev['low']
                row['alerts_medium'] = sev['medium']
                row['alerts_high'] = sev['high']
                row['alerts_critical'] = sev['critical']
                # Remove nested dict before writing — DictWriter would
                # serialize it as a string otherwise
                row.pop('severity_breakdown', None)
                # Flatten spotlight vulnerability data into individual columns
                spot = host.get('spotlight_vulns', {})
                row['spotlight_critical'] = spot.get('critical', 0)
                row['spotlight_high'] = spot.get('high', 0)
                row['spotlight_medium'] = spot.get('medium', 0)
                row['spotlight_low'] = spot.get('low', 0)
                row['spotlight_cisa_kev'] = spot.get('cisa_kev', 0)
                row.pop('spotlight_vulns', None)
                # Flatten ZTA score data into individual columns
                zta = host.get('zta_score', {})
                row['zta_overall'] = zta.get('overall', '')
                row['zta_sensor_config'] = zta.get('sensor_config', '')
                row['zta_os_signal'] = zta.get('os_signal', '')
                row.pop('zta_score', None)
                writer.writerow(row)

            # Write summary as comment lines (prefixed with #) so
            # they are ignored by most CSV parsers but visible in
            # text editors
            csvfile.write("\n# Analysis Summary\n")
            csvfile.write(f"# Period: Last {days} days\n")
            csvfile.write(f"# Total hosts: {len(hosts)}\n")
            total_alerts = sum(h['alerts'] for h in hosts)
            csvfile.write(f"# Total alerts: {total_alerts:,}\n")
            if include_rtr:
                total_rtr = sum(h['rtr_sessions'] for h in hosts)
                csvfile.write(f"# Total RTR sessions: {total_rtr:,}\n")
            # Record generation timestamp for audit trail
            timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            csvfile.write(f"# Generated: {timestamp} UTC\n")

        # Confirm successful export to the user
        print(f"\nResults exported to: {output_path}")

    except IOError as err:
        # File system errors (permissions, disk full, etc.)
        print(f"Error writing to CSV file: {err}", file=sys.stderr)
        print("Check file path permissions and disk space.",
              file=sys.stderr)
        raise SystemExit(1) from err


def main():
    """Run the high activity hosts analysis.

    Orchestrates the full pipeline:
    1. Parse CLI arguments and configure logging.
    2. Import third-party dependencies (deferred to allow ``--help``
       to work without them).
    3. Branch into demo mode (synthetic data) or live API mode.
    4. In live mode, authenticate to Falcon APIs and choose between
       interactive (progressive loading) or simple (sequential) display.
    5. Optionally export results to CSV.
    """
    # Parse command line arguments (validates credentials and ranges)
    args = consume_arguments()

    # Configure logging BEFORE importing/using APIs so any import-time
    # log messages are captured at the correct level
    if args.debug:
        # DEBUG shows raw HTTP calls and internal SDK state
        logging.basicConfig(level=logging.DEBUG)
    else:
        # WARNING suppresses routine info; only problems surface
        logging.basicConfig(level=logging.WARNING)

    # Import dependencies after argument parsing to allow --help to
    # succeed even when third-party packages are not installed
    global tabulate, Hosts, Alerts, RealTimeResponseAudit, Indicator, SpotlightVulnerabilities, ZeroTrustAssessment
    try:
        # tabulate: formats list-of-lists into aligned ASCII/HTML tables
        from tabulate import tabulate  # pylint: disable=W0621
    except ImportError as no_tabulate:
        raise SystemExit(
            "The tabulate package must be installed.\n"
            "Install it with: pip install tabulate\n"
            "  Docs: https://pypi.org/project/tabulate/"
        ) from no_tabulate

    try:
        # FalconPy Service Classes: each wraps a group of related
        # CrowdStrike API endpoints with auth, pagination, and
        # pythonic response handling
        from falconpy import (  # pylint: disable=W0621
            Hosts,
            Alerts,
            Indicator,
            RealTimeResponseAudit,
            SpotlightVulnerabilities,
            ZeroTrustAssessment
        )
    except ImportError as no_falconpy:
        raise SystemExit(
            "The crowdstrike-falconpy package must be installed.\n"
            "Install it with: pip install crowdstrike-falconpy\n"
            "  Docs: https://github.com/CrowdStrike/falconpy"
        ) from no_falconpy

    # Run in demo mode or query real API — demo mode bypasses all
    # network calls and uses generate_demo_data instead
    if args.demo:
        # Generate synthetic host data for the requested limit
        hosts = generate_demo_data(args.limit)
        total_analyzed = args.limit
        # Demo data always includes RTR counts
        include_rtr = True
        # Demo mode: no progressive loading needed, go straight to
        # display since all data is available instantly
        _display_mode(args, hosts, total_analyzed, include_rtr, demo=True)
    else:
        # Connect to Falcon APIs using OAuth2 credentials
        try:
            # Hosts API: query device IDs and fetch device details
            hosts_api = Hosts(
                client_id=args.client_id,
                client_secret=args.client_secret,
                base_url=args.base_url,
                member_cid=args.member_cid,
                debug=args.debug,
                pythonic=True  # Return Result objects instead of raw dicts
            )
            # Alerts API: query and count security alerts per host
            alerts_api = Alerts(
                client_id=args.client_id,
                client_secret=args.client_secret,
                base_url=args.base_url,
                member_cid=args.member_cid,
                debug=args.debug,
                pythonic=True
            )

            # RTR Audit API is optional — requires extra RBAC permissions
            rtr_api = None
            if not args.no_rtr:
                try:
                    # Attempt to instantiate RTR Audit; may fail if the
                    # API key lacks Real Time Response Audit scope
                    rtr_api = RealTimeResponseAudit(
                        client_id=args.client_id,
                        client_secret=args.client_secret,
                        base_url=args.base_url,
                        member_cid=args.member_cid,
                        debug=args.debug,
                        pythonic=True
                    )
                except Exception as rtr_err:
                    # Graceful degradation: continue without RTR data
                    logging.warning(
                        "RTR Audit API unavailable: %s", rtr_err
                    )
                    logging.warning("Continuing without RTR data")

            # Spotlight API is optional — requires Spotlight Vulnerabilities scope
            spotlight_api = None
            if not args.no_spotlight:
                try:
                    spotlight_api = SpotlightVulnerabilities(
                        client_id=args.client_id,
                        client_secret=args.client_secret,
                        base_url=args.base_url,
                        member_cid=args.member_cid,
                        debug=args.debug,
                        pythonic=True
                    )
                except Exception as spotlight_err:
                    logging.warning(
                        "Spotlight API unavailable: %s", spotlight_err
                    )
                    logging.warning(
                        "Continuing without vulnerability data"
                    )

            # Zero Trust Assessment API is optional
            zta_api = None
            if not args.no_zta:
                try:
                    zta_api = ZeroTrustAssessment(
                        client_id=args.client_id,
                        client_secret=args.client_secret,
                        base_url=args.base_url,
                        member_cid=args.member_cid,
                        debug=args.debug,
                        pythonic=True
                    )
                except Exception as zta_err:
                    logging.warning(
                        "ZTA API unavailable: %s", zta_err
                    )
                    logging.warning(
                        "Continuing without Zero Trust data"
                    )

            logging.info("Successfully authenticated to Falcon APIs")
            # Track whether RTR is available for display/export logic
            include_rtr = rtr_api is not None

            # Check if interactive mode is available — requires the
            # 'rich' and 'readchar' packages plus a local module
            use_interactive = False
            interactive_mode_fn = None
            get_console_domain_fn = None
            loading_state_cls = None
            # Only attempt interactive mode when not writing to CSV
            # and not explicitly using --simple
            if not args.simple and not args.output:
                try:
                    # Local module providing the rich-based interactive UI
                    from interactive_ui import (  # pylint: disable=C0415
                        interactive_mode as _interactive_mode,
                        is_available as interactive_available,
                        LoadingState
                    )
                    # Local module mapping API base URLs to Falcon console
                    # domains for building clickable host links
                    from console_urls import (  # pylint: disable=C0415
                        get_console_domain
                    )
                    # Verify runtime dependencies (rich, readchar) exist
                    if interactive_available():
                        use_interactive = True
                        interactive_mode_fn = _interactive_mode
                        get_console_domain_fn = get_console_domain
                        loading_state_cls = LoadingState
                except ImportError:
                    # Fall back to simple mode silently
                    use_interactive = False

            if use_interactive:
                # Progressive loading: fetch hosts fast (Steps 1-2), then
                # enrich in background while the UI is already running —
                # this gives the user a table to interact with in seconds
                console_domain = get_console_domain_fn(
                    alerts_api.base_url
                )
                # Execute the fast path: query IDs + fetch details only
                hosts_by_id, all_device_ids, start_date = (
                    query_hosts_fast(
                        hosts_api, args.days, args.filter,
                        quiet=True  # UI handles display
                    )
                )

                # Exit early if no hosts match the filter
                if not hosts_by_id:
                    print("No hosts found matching criteria.")
                    return

                # Build host list for UI (interactive mode gets all hosts,
                # it has its own pagination — no need to slice to limit)
                hosts = list(hosts_by_id.values())
                total_analyzed = len(hosts_by_id)

                # Create loading state tracker — shared between the
                # background enrichment thread and the interactive UI
                loading_state = loading_state_cls(
                    total_hosts=len(all_device_ids),
                    include_rtr=include_rtr,
                    include_spotlight=(spotlight_api is not None),
                    include_zta=(zta_api is not None)
                )

                # Launch background enrichment thread — fetches alerts
                # and RTR sessions, updating host dicts in-place
                enrichment_thread = Thread(
                    target=enrich_hosts_background,
                    args=(
                        hosts_by_id,
                        all_device_ids,
                        start_date,
                        alerts_api,
                        rtr_api,
                        loading_state,
                        args.days,
                        args.workers,
                        spotlight_api,
                        zta_api
                    ),
                    daemon=True  # Dies when main thread exits
                )
                enrichment_thread.start()

                # Launch interactive UI immediately with partial data —
                # scores will update in real-time as the background
                # thread processes alert pages
                try:
                    interactive_mode_fn(
                        hosts_data=hosts,
                        console_domain=console_domain,
                        days_back=args.days,
                        total_analyzed=total_analyzed,
                        loading_state=loading_state
                    )
                except Exception as err:  # pylint: disable=broad-except
                    # If the rich UI crashes, fall back gracefully to
                    # the simple tabulate-based display
                    logging.error(
                        "Interactive mode failed: %s", err
                    )
                    print(f"\n⚠️  Interactive mode error: {err}")
                    print("Falling back to simple output...\n")
                    # Wait for enrichment to finish for fallback — cap
                    # at 5 minutes to avoid hanging indefinitely
                    enrichment_thread.join(timeout=300)
                    display_results(
                        hosts, args.table_format, args.days,
                        args.limit, False, include_rtr,
                        total_analyzed
                    )
            else:
                # Simple mode: use original sequential flow — all data
                # is fetched before anything is displayed
                hosts, total_analyzed = query_high_activity_hosts(
                    hosts_api, alerts_api, rtr_api,
                    args.days, args.limit,
                    args.filter, args.workers,
                    spotlight_api=spotlight_api,
                    zta_api=zta_api
                )
                # Route to display (may still try interactive if rich
                # is available via _display_mode)
                _display_mode(
                    args, hosts, total_analyzed,
                    include_rtr, demo=False,
                    api_base_url=alerts_api.base_url
                )

        except Exception as err:
            # Catch-all for API authentication or connection failures
            logging.error("Error connecting to Falcon API: %s", err)
            raise SystemExit(
                f"API Error: {err}\n\n"
                "Troubleshooting:\n"
                "  - Verify your Client ID and Secret are correct\n"
                "  - Ensure API client has Hosts:READ scope\n"
                "  - Check base URL matches your Falcon region\n"
                "  - Run with --debug flag for detailed output"
            ) from err

    # Export to CSV if requested — runs after display regardless of
    # whether interactive or simple mode was used
    if args.output:
        export_to_csv(hosts, args.output, args.days, include_rtr)


def _display_mode(
    args, hosts, total_analyzed, include_rtr,
    demo=False, api_base_url=None
):
    """Handle display mode routing (simple or interactive).

    This helper decides between the rich-based interactive UI and the
    simple tabulate-based table.  It is called from ``main()`` in both
    demo mode and live simple-mode paths (but NOT the live progressive-
    loading path, which launches interactive_mode directly).

    Args:
        args: Parsed command line arguments.
        hosts: List of enriched host dictionaries.
        total_analyzed: Total number of hosts analyzed.
        include_rtr: Whether RTR data is included.
        demo: Whether running in demo mode.
        api_base_url: API base URL for console domain detection
                      (None in demo mode).
    """
    # Sort results if the user specified a non-default sort field
    if args.sort != 'activity_score':
        # Numeric fields should sort descending; hostname sorts ascending
        reverse = args.sort in ['activity_score', 'alerts',
                                'rtr_sessions']
        hosts.sort(key=lambda x: x.get(args.sort, ''),
                   reverse=reverse)

    # Determine display mode — attempt interactive first, fall back
    # to simple if dependencies are missing or user passed --simple
    use_interactive = False
    interactive_mode_fn = None
    get_console_domain_fn = None
    # Skip interactive check when writing to CSV (no terminal output)
    # or when --simple was explicitly requested
    if not args.simple and not args.output:
        try:
            # Attempt to import the local interactive UI module
            from interactive_ui import (  # pylint: disable=C0415
                interactive_mode as _interactive_mode,
                is_available as interactive_available
            )
            # Import console URL mapper for building Falcon links
            from console_urls import (  # pylint: disable=C0415
                get_console_domain
            )
            # Verify runtime deps (rich, readchar) are actually importable
            if interactive_available():
                use_interactive = True
                interactive_mode_fn = _interactive_mode
                get_console_domain_fn = get_console_domain
        except ImportError:
            # Dependencies not installed — will use simple mode
            use_interactive = False

    if use_interactive:
        # Determine the Falcon console domain for host detail links
        if demo:
            # In demo mode use the default US-1 console domain
            console_domain = 'falcon.crowdstrike.com'
        else:
            # Map the API base URL to the corresponding console URL
            console_domain = get_console_domain_fn(api_base_url)

        try:
            # Launch the rich-based interactive table UI
            interactive_mode_fn(
                hosts_data=hosts,
                console_domain=console_domain,
                days_back=args.days,
                total_analyzed=total_analyzed
            )
        except Exception as err:  # pylint: disable=broad-except
            # Graceful degradation: if interactive mode crashes,
            # fall back to the simple table
            logging.error("Interactive mode failed: %s", err)
            print(f"\n⚠️  Interactive mode error: {err}")
            print("Falling back to simple table output...\n")
            display_results(
                hosts, args.table_format, args.days,
                args.limit, demo, include_rtr,
                total_analyzed
            )
    else:
        # Simple mode: render a static tabulate table
        display_results(hosts, args.table_format, args.days,
                        args.limit, demo, include_rtr,
                        total_analyzed)

        # Nudge the user to install interactive mode dependencies
        # when they are missing (skip if they explicitly chose --simple
        # or are writing to a file)
        if not args.simple and not args.output:
            print(
                "💡 Tip: Install 'rich' and 'readchar' for "
                "interactive mode:\n"
                "   pip install rich readchar\n"
            )


# Standard Python entry point guard — ensures main() only runs when
# the script is executed directly, not when imported as a module
if __name__ == "__main__":
    _exit_code = 0
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl+C during long API queries — exit cleanly without traceback
        print("\n\nOperation cancelled by user.")
    except Exception as err:
        # Last-resort handler for any unhandled exception; ensures a
        # non-zero exit code and logs the error for debugging
        logging.error("Unexpected error: %s", err)
        print(f"\nError: {err}", file=sys.stderr)
        _exit_code = 1
    finally:
        # Flush output before exit so buffered text (tables, etc.) is visible
        sys.stdout.flush()
        sys.stderr.flush()
        # Use os._exit to avoid hanging on atexit handlers from
        # ThreadPoolExecutor or background daemon threads
        os._exit(_exit_code)  # pylint: disable=protected-access
