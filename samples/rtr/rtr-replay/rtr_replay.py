r"""Replay the command history of a historical CrowdStrike Falcon RTR session.

 _______ _______ ______         _______ _______ _______ _____   _______ ___ ___
|   _   |       |   _  \       |   _   |   _   |   _   |     | |   _   |   Y   |
|.  l   |.|   | |.  l   \      |.  l   |.  1___|.  1   |.    | |.  1   |.  1   |
|.  _   `-|.  |-|.  _   /      |.  l   |.  __) |.  ____|.    | |.  _   |.  _   |
|:  l   | |:  | |:  l   \      |:  l   |:  |   |:  |   |:  . | |:  |   |:  |   |
|::.. . | |::.| |::.. .  /     |::.. . |::.|   |::.|   |::. :| |::.|:. |::.|:. |
`-------' `---' `------^'      `-------`---'   `---'   `--:--' `--- ---`--- ---'

                                                     RTR Audit Session Replay
                                                     Uses: RealTimeResponseAudit
                                                     Scope: real-time-response-audit:read

Retrieve and display the full command history of a historical RTR session.

Modes:
  Replay a specific session:   rtr_replay.py -k KEY -s SECRET -i SESSION_ID
  List recent sessions:        rtr_replay.py -k KEY -s SECRET --list [--limit N]
  Demo (no credentials):       rtr_replay.py --demo

Credentials may also be supplied via environment variables:
  FALCON_CLIENT_ID / FALCON_CLIENT_SECRET

NOTE: The real-time-response-audit:read API scope is required. This is distinct
from the real-time-response:read scope used for live RTR sessions.

Created by: Manjula Wickramasuriya (@Manjula101) - Enterprise Security Lab
Modified by: jshcodes@CrowdStrike
"""
import os
from datetime import datetime
from argparse import ArgumentParser, RawTextHelpFormatter

from falconpy import RealTimeResponseAudit  # pylint: disable=import-error


# ── Demo fixture ──────────────────────────────────────────────────────────────

_DEMO_SESSION = {
    "id": "demo-session-abc123",
    "device_id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
    "hostname": "WIN-WORKSTATION-42",
    "user_id": "analyst@example.com",
    "created_at": "2024-11-15T09:12:00Z",
    "updated_at": "2024-11-15T09:18:34Z",
    "duration": 394.0,
    "platform_name": "Windows",
    "pwd": "C:\\Windows\\System32",  # nosec B105 - present working directory, not a password
    "offline_queued": False,
    "logs": [
        {
            "id": 1,
            "base_command": "pwd",
            "command_string": "pwd",
            "current_directory": "C:\\Windows\\System32",
            "created_at": "2024-11-15T09:12:05Z",
        },
        {
            "id": 2,
            "base_command": "ls",
            "command_string": "ls -la",
            "current_directory": "C:\\Windows\\System32",
            "created_at": "2024-11-15T09:12:18Z",
        },
        {
            "id": 3,
            "base_command": "cd",
            "command_string": "cd C:\\Users\\Suspect\\AppData\\Roaming",
            "current_directory": "C:\\Windows\\System32",
            "created_at": "2024-11-15T09:13:45Z",
        },
        {
            "id": 4,
            "base_command": "ls",
            "command_string": "ls",
            "current_directory": "C:\\Users\\Suspect\\AppData\\Roaming",
            "created_at": "2024-11-15T09:13:47Z",
        },
        {
            "id": 5,
            "base_command": "get",
            "command_string": "get suspicious.exe",
            "current_directory": "C:\\Users\\Suspect\\AppData\\Roaming",
            "created_at": "2024-11-15T09:14:02Z",
        },
    ],
}


# ── Argument parsing ──────────────────────────────────────────────────────────


def consume_arguments() -> object:
    """Consume provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        "-k", "--falcon_client_id",
        help="CrowdStrike Falcon API client ID.\nCan also be set via FALCON_CLIENT_ID env var.",
        required=False,
        default=os.getenv("FALCON_CLIENT_ID"),
    )
    parser.add_argument(
        "-s", "--falcon_client_secret",
        help="CrowdStrike Falcon API client secret.\n"
             "Can also be set via FALCON_CLIENT_SECRET env var.",
        required=False,
        default=os.getenv("FALCON_CLIENT_SECRET"),
    )
    parser.add_argument(
        "-b", "--base_url",
        help="CrowdStrike region base URL.\nOnly required for GovCloud users (usgov1).",
        required=False,
        default="auto",
    )
    parser.add_argument(
        "-i", "--session_id",
        help="RTR session ID to replay.",
        required=False,
        default=None,
    )
    parser.add_argument(
        "--list",
        help="List recent RTR sessions instead of replaying one.",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--limit",
        help="Maximum number of sessions to return when using --list (default: 10).",
        required=False,
        default=10,
        type=int,
    )
    parser.add_argument(
        "--demo",
        help="Run in demo mode using built-in fixture data (no credentials required).",
        action="store_true",
        default=False,
    )

    return parser.parse_args()


# ── Formatting helpers ────────────────────────────────────────────────────────


def format_datetime(iso_str: str) -> str:
    """Parse an ISO 8601 datetime string and return a human-readable local string.

    Returns the raw string unchanged if parsing fails.
    """
    if not iso_str:
        return "—"
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    except ValueError:
        return iso_str


def format_duration(seconds: float) -> str:
    """Format a float duration in seconds as a human-readable string."""
    if seconds is None:
        return "—"
    total = int(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}h {minutes:02d}m {secs:02d}s"
    return f"{minutes}m {secs:02d}s"


# ── Display functions ─────────────────────────────────────────────────────────


def print_session_header(session: dict):
    """Print a formatted header block summarising the session metadata."""
    sep = "=" * 70
    print(sep)
    print("  RTR SESSION REPLAY")
    print(sep)
    print(f"  Session ID  : {session.get('id', '—')}")
    print(f"  Host        : {session.get('hostname', '—')} ({session.get('device_id', '—')})")
    print(f"  Operator    : {session.get('user_id', '—')}")
    print(f"  Platform    : {session.get('platform_name', '—')}")
    print(f"  Started     : {format_datetime(session.get('created_at'))}")
    print(f"  Ended       : {format_datetime(session.get('updated_at'))}")
    print(f"  Duration    : {format_duration(session.get('duration'))}")
    print(f"  Queued      : {'yes' if session.get('offline_queued') else 'no'}")
    print(sep)


def print_command_log(logs: list):
    """Print each command entry in chronological order with its context."""
    if not logs:
        print("  [no commands recorded for this session]")
        return

    # Sort chronologically; API should return ordered, but be defensive.
    ordered = sorted(logs, key=lambda e: (e.get("created_at") or "", e.get("id") or 0))

    print(f"  Commands ({len(ordered)}):")
    print("  " + "-" * 68)
    for entry in ordered:
        timestamp = format_datetime(entry.get("created_at"))
        cwd = entry.get("current_directory") or "—"
        cmd = entry.get("command_string") or entry.get("base_command") or "—"
        print(f"  [{timestamp}]")
        print(f"    cwd : {cwd}")
        print(f"    cmd : {cmd}")
        print()


def print_session(session: dict):
    """Print the full replay output (header + command log) for a session."""
    print_session_header(session)
    print_command_log(session.get("logs", []))


# ── API interaction ───────────────────────────────────────────────────────────


def call_audit_sessions(sdk: RealTimeResponseAudit,
                        fql_filter: str = None,
                        limit: int = None,
                        offset: str = None) -> dict:
    """Call audit_sessions() and return the response body.

    Raises SystemExit on non-200 API responses, printing the error details.

    Args:
        sdk: Authenticated RealTimeResponseAudit service class instance.
        fql_filter: Optional FQL query string (e.g. "hostname:'myhost'").
        limit: Maximum sessions to return per page (1–1000).
        offset: Pagination cursor from a prior response.

    Returns:
        The response body dict containing 'resources' and 'meta'.
    """
    kwargs = {"with_command_info": True}
    if fql_filter:
        kwargs["filter"] = fql_filter
    if limit is not None:
        kwargs["limit"] = str(limit)
    if offset is not None:
        kwargs["offset"] = str(offset)

    response = sdk.audit_sessions(**kwargs)
    status = response.get("status_code")

    if status != 200:
        errors = response.get("body", {}).get("errors", [])
        for err in errors:
            print(f"[{err.get('code', '?')}] {err.get('message', 'Unknown error')}")
        raise SystemExit(f"API returned HTTP {status}. Check credentials and API scope.")

    return response["body"]


def find_session_by_id(sdk: RealTimeResponseAudit, session_id: str) -> dict:
    """Page through all audit sessions and return the one matching session_id.

    The audit endpoint does not support FQL filtering on the 'id' field, so
    this function performs a paginated client-side scan.

    Args:
        sdk: Authenticated RealTimeResponseAudit service class instance.
        session_id: The RTR session ID to locate.

    Returns:
        The matching session dict, or None if not found.
    """
    page_size = 1000
    offset = None

    while True:
        body = call_audit_sessions(sdk, limit=page_size, offset=offset)
        resources = body.get("resources") or []

        for session in resources:
            if session.get("id") == session_id:
                return session

        # Advance cursor; stop when exhausted.
        pagination = (body.get("meta") or {}).get("pagination") or {}
        next_offset = pagination.get("next")
        total = pagination.get("total", 0)
        fetched_so_far = (pagination.get("offset") or 0) + len(resources)

        if not next_offset or fetched_so_far >= total or not resources:
            break

        offset = next_offset

    return None


# ── Action handlers ───────────────────────────────────────────────────────────


def replay_session(sdk: RealTimeResponseAudit, session_id: str):
    """Retrieve and display the command history of a specific RTR session.

    Args:
        sdk: Authenticated RealTimeResponseAudit service class instance.
        session_id: The RTR session ID string to replay.
    """
    session = find_session_by_id(sdk, session_id)

    if not session:
        print(f"[WARN] No audit data found for session ID: {session_id}")
        print("       Possible reasons:")
        print("         - Session ID does not exist or is incorrect")
        print("         - Session predates the audit log retention window")
        print("         - API key lacks real-time-response-audit:read scope")
        return

    print_session(session)


def list_sessions(sdk: RealTimeResponseAudit, limit: int = 10):
    """List recent RTR sessions with a brief summary per session.

    Args:
        sdk: Authenticated RealTimeResponseAudit service class instance.
        limit: How many sessions to retrieve (max 1000).
    """
    body = call_audit_sessions(sdk, limit=limit)
    sessions = body.get("resources") or []

    if not sessions:
        print("[INFO] No RTR sessions found.")
        return

    sep = "-" * 70
    print(f"Recent RTR Sessions (showing {len(sessions)}):")
    print(sep)
    for session in sessions:
        cmd_count = len(session.get("logs") or [])
        print(
            f"  {session.get('id', '—'):<40} "
            f"host={session.get('hostname', '—'):<20} "
            f"cmds={cmd_count}"
        )
    print(sep)


def run_demo():
    """Display a replay using built-in fixture data; makes no API calls."""
    print("[INFO] Running in demo mode — no API calls made\n")
    print_session(_DEMO_SESSION)


# ── Entry point ───────────────────────────────────────────────────────────────


if __name__ == "__main__":
    args = consume_arguments()

    # Demo mode: no credentials required.
    if args.demo or (not args.falcon_client_id and not args.falcon_client_secret):
        run_demo()
        raise SystemExit(0)

    # Credential check.
    if not args.falcon_client_id or not args.falcon_client_secret:
        print("[ERROR] Provide API credentials via -k/-s arguments or "
              "FALCON_CLIENT_ID/FALCON_CLIENT_SECRET environment variables.")
        print("        Use --demo to run without credentials.")
        raise SystemExit(1)

    # Connect to the API.
    audit_sdk = RealTimeResponseAudit(
        client_id=args.falcon_client_id,
        client_secret=args.falcon_client_secret,
        base_url=args.base_url,
    )

    # Dispatch to the requested action.
    if args.list:
        list_sessions(audit_sdk, limit=args.limit)
    elif args.session_id:
        replay_session(audit_sdk, args.session_id)
    else:
        print("[ERROR] Specify a session ID with -i SESSION_ID, or use --list to browse sessions.")
        print("        Use --demo to see example output without credentials.")
        raise SystemExit(1)
