"""
stale_sensors.py - Detects devices that haven't checked into
                   CrowdStrike for a specified period of time.

REQUIRES: FalconPy v0.8.6+, tabulate

- jshcodes@CrowdStrike, 09.01.21
"""
from datetime import datetime, timedelta, timezone
from argparse import RawTextHelpFormatter
import argparse
from tabulate import tabulate
try:
    from falconpy import Hosts
except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy


def parse_command_line() -> object:
    """
    Parses command-line arguments and returns them back as an object.
    """
    header = """
         _______ ___ ___ _______ _______ _______ ______
        |   _   |   Y   |   _   |   _   |   _   |   _  \\
        |.  1___|.  |   |   1___|   1___|.  1___|.  |   \\
        |.  |___|.  |   |____   |____   |.  __)_|.  |    \\
        |:  1   |:  1   |:  1   |:  1   |:  1   |:  1    /
        |::.. . |::.. . |::.. . |::.. . |::.. . |::.. . /
        `-------`-------`-------`-------`-------`------'

    CrowdStrike Unattended Stale Sensor Environment Detector
    """
    parser = argparse.ArgumentParser(
        description=header,
        formatter_class=RawTextHelpFormatter
        )
    parser.add_argument(
        '-k',
        '--client_id',
        help='CrowdStrike Falcon API key ID',
        required=True
        )
    parser.add_argument(
        '-s',
        '--client_secret',
        help='CrowdStrike Falcon API key secret',
        required=True
        )
    parser.add_argument(
        '-b',
        '--base_url',
        help='CrowdStrike API region (us1, us2, eu1, usgov1)'
        ' NOT required unless you are using `usgov1`',
        required=False
    )
    parser.add_argument(
        '-d',
        '--days',
        help='Number of days since a host was seen before it is considered stale',
        required=False
        )
    parser.add_argument(
        '-r',
        '--reverse',
        help='Reverse sort (defaults to ASC)',
        required=False,
        action="store_true"
        )
    parser.add_argument(
        '-x',
        '--remove',
        help='Remove hosts identified as stale',
        required=False,
        action='store_true'
    )

    return parser.parse_args()


def connect_api(key: str, secret: str, base_url: str) -> Hosts:
    """
    Connects to the API and returns an instance of the Hosts Service Class.
    """
    return Hosts(client_id=key, client_secret=secret, base_url=base_url)


def get_host_details(id_list: list) -> list:
    """
    Retrieves a list containing device infomration based upon the ID list provided.
    """
    return falcon.get_device_details(ids=id_list)["body"]["resources"]


def get_hosts(date_filter: str) -> list:
    """
    Retrieves a list of hosts IDs that match the last_seen date filter.
    """
    return falcon.query_devices_by_filter_scroll(
        limit=5000,
        filter=f"last_seen:<='{date_filter}Z'"
    )["body"]["resources"]


def get_sort_key(sorting) -> list:
    """
    Sorting method for table display.
    Column 4 = Stale Period
    Column 0 = Hostname
    """
    return (sorting[4], sorting[0])


def calc_stale_date(num_days: int) -> str:
    """
    Calculates the "stale" datetime based upon the number of days
    provided by the user.
    """
    today = datetime.strptime(str(datetime.now(timezone.utc)), "%Y-%m-%d %H:%M:%S.%f%z")
    return str(today - timedelta(days=num_days)).replace(" ", "T")[:-6]


def parse_host_detail(detail: dict, found: list):
    """
    Parses the returned host detail and adds it to the stale list.
    """
    now = datetime.strptime(str(datetime.now(timezone.utc)), "%Y-%m-%d %H:%M:%S.%f%z")
    then = datetime.strptime(detail["last_seen"], "%Y-%m-%dT%H:%M:%S%z")
    distance = (now - then).days
    found.append([
        detail.get("hostname", "Unknown"),
        detail.get("device_id", "Unknown"),
        detail.get("local_ip", "Unknown"),
        detail["last_seen"],
        f"{distance} days"
        ])

    return found


def hide_hosts(id_list: list) -> dict:
    """
    Hides hosts identified as stale.
    """
    return falcon.perform_action(action_name="hide_host", body={"ids": id_list})


# Parse our command line
args = parse_command_line()
# Default SORT to ASC if not present
if not args.reverse:
    SORT = False
else:
    SORT = bool(args.reverse)

if not args.base_url:
    BASE = "us1"
else:
    BASE = args.base_url

# Credentials
api_client_id = args.client_id
api_client_secret = args.client_secret
if not api_client_id and not api_client_secret:
    raise SystemExit("Invalid API credentials provided.")

# Set our stale date to 120 days if not present
if not args.days:
    STALE_DAYS = 120
else:
    try:
        STALE_DAYS = int(args.days)
    except ValueError as bad_day_value:
        raise SystemExit("Invalid value specified for days. Integer required.") from bad_day_value

# Do not hide hosts if it is not requested
if not args.remove:
    HIDE = False
else:
    HIDE = bool(args.remove)

# Calculate our stale date filter
STALE_DATE = calc_stale_date(STALE_DAYS)

# Connect to the API
falcon = connect_api(api_client_id, api_client_secret, BASE)

# List to hold our identified hosts
stale = []
# For each stale host identified
try:
    for host in get_host_details(get_hosts(STALE_DATE)):
        # Retrieve host detail
        stale = parse_host_detail(host, stale)
except KeyError:
    raise SystemExit("Unable to communicate with CrowdStrike API, check credentials and try again.")

# If we produced stale host results
if stale:
    # Display only
    if not HIDE:
        headers = ["Hostname", "Device ID", "Local IP", "Last Seen", "Stale Period"]
        print(f"\n{tabulate(sorted(stale, key=get_sort_key, reverse=SORT), headers)}")
    else:
        # Remove the hosts
        host_list = [x[1] for x in stale]
        remove_result = hide_hosts(host_list)["body"]["resources"]
        for deleted in remove_result:
            print(f"Removed host {deleted['id']}")
else:
    print("No stale hosts identified for the range specified.")
