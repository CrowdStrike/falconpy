r"""CrowdStrike Falcon Discover simple example.

             ______
          .-'      `-.
        .'            `.
       /                \
      ;                 ;`
      |   CrowdStrike   |;
      ;      Falcon     ;|
      '\               / ;
       \`.           .' /
        `.`-._____.-' .'
          / /`_____.-'
         / / /
        / / /   ______   __
       / / /   |   _  \ |__.-----.----.-----.--.--.-----.----.
      / / /    |.  |   \|  |__ --|  __|  _  |  |  |  -__|   _|
     / / /     |.  |    |__|_____|____|_____|\___/|_____|__|
    / / /      |:  1    /
   / / /       |::.. . /           FalconPy v1.0.1
  / / /        `------'
 / / /
 \/_/

Creation date: 02.08.2022 - jshcodes@CrowdStrike
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
from tabulate import tabulate
try:
    from falconpy import Discover, Hosts
except ImportError as no_falconpy:
    raise SystemExit("The crowdstrike-falconpy package must be installed "
                     "in order to run this program.\n\nInstall with the command: "
                     "python3 -m pip install crowdstrike-falconpy") from no_falconpy

def parse_command_line() -> object:
    """Parse any received inbound command line parameters."""
    parser = ArgumentParser(
        description=__doc__,
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        '-k',
        '--client_id',
        help='CrowdStrike Falcon API key ID.\n'
        'You can also use the `FALCON_CLIENT_ID` environment variable to specify this value.',
        required=False
    )
    parser.add_argument(
        '-s',
        '--client_secret',
        help='CrowdStrike Falcon API key secret.\n'
        'You can also use the `FALCON_CLIENT_SECRET` environment variable to specify this value.',
        required=False
    )
    parser.add_argument(
        '-b',
        '--base_url',
        help='CrowdStrike API region (us1, us2, eu1, usgov1)'
        ' NOT required unless you are using `usgov1`.',
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
        '-d',
        '--debug',
        help='Enable API debugging',
        required=False,
        default=False,
        action="store_true"
    )
    parser.add_argument(
        '-f',
        '--format',
        help='Table format to use for display.\n'
        '(plain, simple, github, grid, fancy_grid, pipe, orgtbl, jira, presto, \n'
        'pretty, psql, rst, mediawiki, moinmoin, youtrack, html, unsafehtml, \n'
        'latext, latex_raw, latex_booktabs, latex_longtable, textile, tsv)',
        required=False
    )
    return parser.parse_args()
def get_sort_key(sorting) -> list:
    """Return the sort column value for sorting operations."""
    return sorting["hostname"]
# Retrieve all inbound command line parameters if args debug is present
args = parse_command_line()
# Set constants based upon received inputs
BASE_URL = "auto"
if args.base_url:
    BASE_URL = args.base_url
if args.client_id:
    CLIENT_ID = args.client_id
else:
    CLIENT_ID = os.getenv("FALCON_CLIENT_ID", "Not set")
if args.client_secret:
    CLIENT_SECRET = args.client_secret
else:
    CLIENT_SECRET = os.getenv("FALCON_CLIENT_SECRET", "Not set")
if not args.reverse:
    SORT = False
else:
    SORT = bool(args.reverse)
# add debug with logging put after parser 
if args.debug:
    logging.basicConfig(level=logging.DEBUG)

TABLE_FORMATS = [
    "plain", "simple", "github", "grid", "fancy_grid", "pipe", "orgtbl", "jira", "presto",
    "pretty", "psql", "rst", "mediawiki", "moinmoin", "youtrack", "html", "unsafehtml",
    "latex", "latex_raw", "latex_booktabs", "latex_longtable", "textile", "tsv"
]
TABLE_FORMAT = "fancy_grid"
if args.format:
    table_format = args.format.strip().lower()
    if table_format in TABLE_FORMATS:
        TABLE_FORMAT = table_format
# Headers used in our result display table
HEADERS = {
    "hostname": "Hostname",
    "current_local": "Local IP",
    "current_external": "External IP",
    "plat": "Platform",
    "osver": "Version"
}
hosts = Hosts(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    debug=args.debug
)
# Connect to the Discover API
discover = Discover(auth_object=hosts)
# Empty list to hold our results
identified = []
# Query for a complete list of discovered hosts. Maxes out at 100.
host_lookup = discover.query_hosts()
if host_lookup.get("status_code") == 200:
    identified_hosts = host_lookup["body"]["resources"]
    if not identified_hosts:
        # No hosts returned for this search
        print("No hosts identified")
    else:
        # Retrieve all details for all discovered hosts
        host_detail = discover.get_hosts(ids=identified_hosts)["body"]["resources"]
        # Add each host's relevant detail to our `identified` list so we can display it
        for host in host_detail:
            found = {
                "hostname": host.get("hostname", "Not identified"),
                "current_local": host.get("current_local_ip", "Unknown"),
                "current_external": host.get("external_ip", "Unknown"),
                "plat": host.get("platform_name", "Unknown"),
                "osver": host.get("os_version", "Unknown")
            }
            # Append this result to our display list
            identified.append(found)
        # All findings have been tabulated, show the results
        print(tabulate(tabular_data=sorted(identified, key=get_sort_key, reverse=SORT),
                       headers=HEADERS,
                       tablefmt=TABLE_FORMAT
                       ))
else:
    # An error has occurred, output the detail
    error_detail = host_lookup["body"]["errors"]
    for err in error_detail:
        ecode = err["code"]
        emsg = err["message"]
        print(f"[{ecode}] {emsg}")
