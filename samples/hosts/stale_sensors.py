r"""CrowdStrike Unattended Stale Sensor Environment Detector.

         _______ ___ ___ _______ _______ _______ ______
        |   _   |   Y   |   _   |   _   |   _   |   _  \
        |.  1___|.  |   |   1___|   1___|.  1___|.  |   \
        |.  |___|.  |   |____   |____   |.  __)_|.  |    \
        |:  1   |:  1   |:  1   |:  1   |:  1   |:  1    /
        |::.. . |::.. . |::.. . |::.. . |::.. . |::.. . /
        `-------`-------`-------`-------`-------`------'

stale_sensors.py - Detects devices that haven't checked into
                   CrowdStrike for a specified period of time.

REQUIRES: crowdstrike-falconpy v0.9.0+, python-dateutil, tabulate

This example will work for all CrowdStrike regions. In order to produce
results for the US-GOV-1 region, pass the '-g' argument.

- jshcodes@CrowdStrike; 09.01.21
- ray.heffer@crowdstrike.com; 03.29.22 - Added new argument for Grouping Tags (--grouping, -g)
- @morcef, jshcodes@CrowdStrike; 06.05.22 - More reasonable date calcs, Linting, Easier arg parsing
                                            Easier base_url handling, renamed grouping_tag to tag
- jshcodes@Crowdstrike; 11.02.22 - Added CSV output options and cleaner date outputs.
- nmills@forbarr; 22.05.24 - Fixed deprecation warning on date function, 
                                            Added new arg to accept hostname pattern
                                            Batch the call to hide_hosts to avoid API error
"""
import csv
import re
from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime, timedelta, timezone
from dateutil import parser as dparser
from tabulate import tabulate
try:
    from falconpy import Hosts
except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy

def parse_command_line() -> object:
    """Parse command-line arguments and return them back as an ArgumentParser object."""
    parser = ArgumentParser(
        description=__doc__,
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
        '-m',
        '--mssp',
        help='Child CID to access (MSSP only)',
        required=False,
        default=None
        )
    parser.add_argument(
        '-g',
        '--govcloud',
        help='Use the US-GOV-1 region',
        required=False,
        action="store_const",
        const="usgov1",
        default="auto"
    )
    parser.add_argument(
        '-d',
        '--days',
        help='Number of days since a host was seen before it is considered stale',
        required=False,
        default=10
        )
    parser.add_argument(
        '-r',
        '--reverse',
        help='Reverse sort (defaults to ASC)',
        required=False,
        action="store_true",
        default=False
        )
    parser.add_argument(
        '-x',
        '--remove',
        help='Remove hosts identified as stale',
        required=False,
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-t',
        '--tag',
        help='Falcon Grouping Tag name for the hosts',
        required=False,
        default=None
        )
    parser.add_argument(
        '-c',
        '--csv',
        help='Export results to CSV',
        required=False,
        default=False,
        action="store_true"
        )
    parser.add_argument(
        '-o',
        '--output_file',
        help='File to output CSV results to. Ignored when "-c" is not specified.',
        required=False,
        default="stale_results.csv"
        )
    parser.add_argument(
        '-q',
        '--quotes',
        help='Quote non-numeric fields in CSV output.',
        required=False,
        default=False,
        action="store_true"
        )
    parser.add_argument(
        "-f", "--filter-by-os",
        help="OS filter (windows, macos, linux)",
        default=None,
        choices=["windows", "mac", "linux", "k8s"],
        required=False,
        dest="osfilter"
    )
    parser.add_argument(
        "-p", "--host-pattern",
        help="filter hostnames by regex",
        default=r".*",
        required=False,
        dest="hostfilter"
    )
    return parser.parse_args()

def connect_api(key: str, secret: str, base_url: str, child_cid: str = None) -> Hosts:
    """Connect to the API and return an instance of the Hosts Service Class."""
    return Hosts(client_id=key, client_secret=secret, base_url=base_url, member_cid=child_cid)


def get_host_details(id_list: list) -> list:
    """Retrieve a list containing device infomration based upon the ID list provided."""
    returned = falcon.get_device_details(ids=id_list)["body"]["resources"]
    if not returned:
        returned = []
    return returned


def get_hosts(date_filter: str, tag_filter: str, os_filter: str) -> list:
    """Retrieve a list of hosts IDs that match the last_seen date filter."""
    filter_string = f"last_seen:<='{date_filter}Z'"
    if tag_filter:
        filter_string = f"{filter_string} + tags:*'*{tag_filter}*'"
    if os_filter:
        os_filter = os_filter.title()
        if os_filter == "K8s":
            os_filter = "K8S"
        filter_string = f"{filter_string} + platform_name:'{os_filter}'"
        x = falcon.query_devices_by_filter_scroll(
        limit=5000,
        filter=filter_string
    )["body"]["resources"]
    return falcon.query_devices_by_filter_scroll(
        limit=5000,
        filter=filter_string
    )["body"]["resources"]


def calc_stale_date(num_days: int) -> str:
    """Calculate the 'stale' datetime based upon the number of days provided by the user."""
    today = datetime.now(timezone.utc)
    return str(today - timedelta(days=num_days)).replace(" ", "T")


def parse_host_detail(detail: dict, found: list):
    """Parse the returned host detail and add it to the stale list."""
    now = datetime.now(timezone.utc)
    then = dparser.parse(detail["last_seen"])
    distance = (now - then).days
    tagname = detail.get("tags", "")
    newtag = "\n".join(tagname)
    found.append([
        detail.get("hostname", "Unknown"),
        detail.get("device_id", "Unknown"),
        detail.get("local_ip", "Unknown"),
        newtag,
        dparser.parse(detail["last_seen"], ignoretz=True),
        f"{distance} days"
        ])

    return found


def hide_hosts(id_list: list) -> dict:
    """Hide hosts identified as stale."""
    return falcon.perform_action(action_name="hide_host", body={"ids": id_list})


# Parse our command line
args = parse_command_line()

# Set our stale date to 120 days if not present, make sure they didn't give us garbage
STALE_DAYS = 120
if args.days:
    try:
        STALE_DAYS = int(args.days)
    except ValueError as bad_day_value:
        raise SystemExit("Invalid value specified for days. Integer required.") from bad_day_value

# Calculate our stale date filter
STALE_DATE = calc_stale_date(STALE_DAYS)

# Connect to the API
falcon = connect_api(args.client_id, args.client_secret, args.govcloud, args.mssp)

# List to hold our identified hosts
stale = []
# For each stale host identified
pattern = args.hostfilter
if args.hostfilter != r".*":
    print(f"Pattern is: {re.escape(pattern)}")

for host in get_host_details(get_hosts(STALE_DATE, args.tag, args.osfilter)):
    # Retrieve host detail
    if 'hostname' in host:
        if re.findall(pattern, host['hostname']):
            stale = parse_host_detail(host, stale)

# If we produced stale host results
if stale:
    # Display only is the default
    if not bool(args.remove):
        sorted_results = sorted(stale, key=lambda x: (x[4], x[0]), reverse=args.reverse)
        fields = ["Hostname", "Device ID", "Local IP", "Tag", "Last Seen", "Stale Period"]
        if args.csv:
            with open(args.output_file, "w", newline="", encoding="utf-8") as csv_file:
                QUOTES = csv.QUOTE_MINIMAL
                if args.quotes:
                    QUOTES = csv.QUOTE_NONNUMERIC
                writer = csv.writer(csv_file, dialect="excel", quoting=QUOTES)
                writer.writerow(fields)
                writer.writerows(sorted_results)
                print(f"Results written to {args.output_file}.")
        else:
            stale_display = tabulate(
                sorted_results,
                fields
                )
            print(f"\n{stale_display}")
    else:
        # Remove the hosts
        host_list = [x[1] for x in stale]
        batch_size = 50
        for i in range(0, len(host_list), batch_size):
            batch = host_list[i:i + batch_size]
            remove_result = hide_hosts(batch)
            if remove_result["status_code"] == 202:
                for deleted in remove_result["body"]["resources"]:
                    print(f"Removed host {deleted['id']}")
            else:
                for deleted in remove_result["body"]["errors"]:
                    print(f"[{deleted['code']}] {deleted['message']}")
else:
    print("No stale hosts identified for the range specified.")
