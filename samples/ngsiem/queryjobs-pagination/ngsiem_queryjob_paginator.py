#!/usr/bin/env python3
"""
NG-SIEM QueryJob paginator (FalconPy) — retrieves all results from a
QueryJob using cursor-based pagination via the `around` parameter.

Uses the FalconPy NGSIEM service class with OAuth2 authentication.
The pagination mechanism is identical to direct LogScale QueryJobs:
  1. Create a QueryJob and poll until done
  2. Collect the initial 200-event buffer
  3. If hasMoreEvents="true", use cursor-based `around` pagination to
     walk backward through time and collect remaining events

Usage:
    export FALCON_CLIENT_ID="your-client-id"
    export FALCON_CLIENT_SECRET="your-client-secret"
    python ngsiem_queryjob_paginator.py -q '#event_simpleName=ProcessRollup2'

    # Optional flags:
    python ngsiem_queryjob_paginator.py -q '...' -r search-all --start 1h --end now
    python ngsiem_queryjob_paginator.py -q '...' -b https://api.us-2.crowdstrike.com
    python ngsiem_queryjob_paginator.py -q '...' -m CHILD_CID  # MSSP / flight control

Requirements:
    pip install crowdstrike-falconpy
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

from falconpy import NGSIEM

# ── Defaults ──────────────────────────────────────────────────────────
START = "15m"
END = "now"
PAGE_SIZE = 200
MAX_EVENTS = 0      # 0 = unlimited
OUTPUT_FILE = "ngsiem_queryjob_results.json"
DEFAULT_REPO = "search-all"
# ──────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="NG-SIEM QueryJob paginator with cursor-based pagination (FalconPy).",
        epilog="""Authentication (flags take precedence over environment variables):
  -k / FALCON_CLIENT_ID       OAuth2 client ID
  -s / FALCON_CLIENT_SECRET   OAuth2 client secret
  -b / FALCON_BASE_URL        CrowdStrike API base URL (default: US-1)
  -m / FALCON_MEMBER_CID      Child CID for MSSP / flight control

NG-SIEM repositories: search-all, investigate_view, third-party,
                      falcon_for_it_view, forensics_view""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-k", "--client-id",
        default=os.environ.get("FALCON_CLIENT_ID", ""),
        help="OAuth2 client ID (or set FALCON_CLIENT_ID)",
    )
    parser.add_argument(
        "-s", "--client-secret",
        default=os.environ.get("FALCON_CLIENT_SECRET", ""),
        help="OAuth2 client secret (or set FALCON_CLIENT_SECRET)",
    )
    parser.add_argument(
        "-b", "--base-url",
        default=os.environ.get("FALCON_BASE_URL", ""),
        help="CrowdStrike API base URL (default: US-1)",
    )
    parser.add_argument(
        "-m", "--member-cid",
        default=os.environ.get("FALCON_MEMBER_CID", ""),
        help="Child CID for MSSP / flight control",
    )
    parser.add_argument(
        "-q", "--query",
        required=True,
        help="CQL query string. Wrap in single quotes to preserve double quotes.",
    )
    parser.add_argument("-r", "--repo", default=DEFAULT_REPO, help=f"Repository (default: {DEFAULT_REPO})")
    parser.add_argument("--start", default=START, help=f"Start time (default: {START})")
    parser.add_argument("--end", default=END, help=f"End time (default: {END})")
    parser.add_argument("-o", "--output", default=OUTPUT_FILE, help=f"Output file (default: {OUTPUT_FILE})")
    parser.add_argument("--max-events", type=int, default=MAX_EVENTS, help="Max events to retrieve (default: unlimited)")
    parser.add_argument("--page-size", type=int, default=PAGE_SIZE, help=f"Events per page (default: {PAGE_SIZE})")
    return parser.parse_args()


def start_search(ngsiem: NGSIEM, repo: str, query_string: str,
                 start: str, end: str, around: dict | None = None) -> str:
    """Create a QueryJob and return its ID."""
    kwargs = {
        "repository": repo,
        "query_string": query_string,
        "start": start,
        "end": end,
        "is_live": False,
    }
    if around:
        kwargs["around"] = around

    resp = ngsiem.start_search(**kwargs)
    if resp["status_code"] != 200:
        sys.exit(f"Failed to start search: {resp}")
    return resp["resources"]["id"]


def delete_search(ngsiem: NGSIEM, repo: str, job_id: str) -> None:
    """Delete a QueryJob to free server resources."""
    ngsiem.stop_search(repository=repo, id=job_id)


def poll_until_done(ngsiem: NGSIEM, repo: str, job_id: str) -> dict:
    """Poll a QueryJob until done and return the result payload."""
    while True:
        resp = ngsiem.get_search_status(repository=repo, id=job_id)
        if resp["status_code"] == 404:
            return {"done": True, "events": [], "metaData": {}}
        if resp["status_code"] != 200:
            sys.exit(f"Poll failed ({resp['status_code']}): {resp}")

        resources = resp.get("resources") or resp.get("body", {})
        if resources.get("done", False):
            return resources

        wait_ms = resources.get("metaData", {}).get("pollAfter", 500)
        time.sleep(wait_ms / 1000.0)


def main():
    args = parse_args()

    if not args.client_id or not args.client_secret:
        sys.exit("Error: set FALCON_CLIENT_ID and FALCON_CLIENT_SECRET "
                 "(environment variables or -k/-s flags)")

    ssl_verify = os.environ.get("CA_BUNDLE") or True

    ngsiem_kwargs = {
        "client_id": args.client_id,
        "client_secret": args.client_secret,
        "ssl_verify": ssl_verify,
    }
    if args.base_url:
        ngsiem_kwargs["base_url"] = args.base_url
    if args.member_cid:
        ngsiem_kwargs["member_cid"] = args.member_cid

    with NGSIEM(**ngsiem_kwargs) as ngsiem:
        if ngsiem.token_fail_reason:
            sys.exit(f"Authentication failed: {ngsiem.token_fail_reason}")

        repo = args.repo
        query_string = args.query
        start = args.start
        end = args.end
        output_file = args.output
        max_events = args.max_events
        page_size = args.page_size

        print(f"Query:  {query_string}")
        print(f"Repo:   {repo}")
        print(f"Range:  {start} → {end}")
        print()

        # Step 1: Initial query
        job_id = start_search(ngsiem, repo, query_string, start, end)
        print(f"QueryJob created: {job_id}")

        data = poll_until_done(ngsiem, repo, job_id)
        delete_search(ngsiem, repo, job_id)

        meta = data.get("metaData", {})
        has_more = meta.get("extraData", {}).get("hasMoreEvents", "false")
        processed = meta.get("processedEvents", "?")

        all_events: list[dict] = list(data.get("events", []))
        seen_ids: set[str] = {e.get("@id", "") for e in all_events}

        print(f"  Initial buffer: {len(all_events)} events  "
              f"(processedEvents={processed}  hasMoreEvents={has_more})")

        # Step 2: Cursor pagination using `around`
        # LogScale returns newest events first; the last event in the buffer is
        # the oldest. Anchor on it and request numberOfEventsBefore to walk
        # backward through time.
        page = 0
        while has_more == "true" and all_events:
            if max_events and len(all_events) >= max_events:
                all_events = all_events[:max_events]
                break

            oldest = all_events[-1]
            anchor_id = oldest.get("@id", "")
            anchor_ts = oldest.get("@timestamp")
            if not anchor_id or anchor_ts is None:
                break

            page += 1
            cursor_job_id = start_search(ngsiem, repo, query_string, start, end, around={
                "eventId": anchor_id,
                "timestamp": int(anchor_ts),
                "numberOfEventsBefore": page_size,
                "numberOfEventsAfter": 0,
            })

            cursor_data = poll_until_done(ngsiem, repo, cursor_job_id)
            delete_search(ngsiem, repo, cursor_job_id)

            events = cursor_data.get("events", [])
            new_events = [e for e in events if e.get("@id", "") not in seen_ids]

            if not new_events:
                break

            for e in new_events:
                seen_ids.add(e.get("@id", ""))
            all_events.extend(new_events)

            print(f"  page {page}: +{len(new_events)} events  (total: {len(all_events)})")
            time.sleep(0.5)

        if max_events and len(all_events) > max_events:
            all_events = all_events[:max_events]

    print(f"\nDone. {len(all_events)} total events.")

    with open(output_file, "w") as f:
        json.dump(all_events, f, indent=2)
    print(f"Results written to {output_file}")


if __name__ == "__main__":
    main()
