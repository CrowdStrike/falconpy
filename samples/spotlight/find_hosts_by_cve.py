"""
 ______                         __ _______ __         __ __
|      |.----.-----.--.--.--.--|  |     __|  |_.----.|__|  |--.-----.
|   ---||   _|  _  |  |  |  |  _  |__     |   _|   _||  |    <|  -__|
|______||__| |_____|________|_____|_______|____|__|  |__|__|__|_____|
                     _______             __   __ __       __    __
                    |   _   .-----.-----|  |_|  |__.-----|  |--|  |_
                    |   1___|  _  |  _  |   _|  |  |  _  |     |   _|
                    |____   |   __|_____|____|__|__|___  |__|__|____|
                    |:  1   |__|                   |_____|
                    |::.. . |
                    `-------'               Find hosts by CVE

Creation date: 01.13.2021 - jshcodes@CrowdStrike

This solution requires the crowdstrike-falconpy (v0.8.6+) and tabulate packages.
    python3 -m pip install crowdstrike-falconpy tabulate

Required API scopes
    Hosts: READ
    Spotlight: READ
"""
from argparse import ArgumentParser, RawTextHelpFormatter
import json
import sys
try:
    from tabulate import tabulate
except ImportError as no_tabulate:
    raise SystemExit(
        "The tabulate library is not installed.\n"
        "Install this package using the following command:\n"
        "   python3 -m pip install tabulate"
        ) from no_tabulate
try:
    from falconpy import SpotlightVulnerabilities, Hosts, OAuth2
except ImportError as no_falconpy:
    raise SystemExit(
        "The crowdstrike-falconpy package is not installed.\n"
        "Install this package using the following command:\n"
        "   python3 -m pip install crowdstrike-falconpy"
        ) from no_falconpy


class SpotlightCVEMatch():  # pylint: disable=R0902
    """Class to represent a returned match to a CVE vulnerability."""

    def __init__(self, api_response):  # pylint: disable=R0912
        """Initialize the object and set all attributes based upon the inbound API response."""
        self.cve = None
        self.score = 0
        self.severity = None
        self.cve_description = None
        self.created_on = None
        self.updated_on = None
        self.hostname = "Unknown"
        self.local_ip = "Unknown"
        self.os_version = "Unknown"
        self.service_provider = "Unknown"
        self.remediation = "Not found"
        self.status = "open"

        cve_detail = api_response["cve"]
        if "id" in cve_detail:
            self.cve = cve_detail["id"]
        if "base_score" in cve_detail:
            self.score = cve_detail["base_score"]
        if "severity" in cve_detail:
            self.severity = cve_detail["severity"]
        if "created_timestamp" in api_response:
            self.created_on = api_response["created_timestamp"]
        if "updated_timestamp" in api_response:
            self.updated_on = api_response["updated_timestamp"]
        if "status" in api_response:
            self.status = api_response["status"]

        host_detail = []
        detail_lookup = hosts.get_device_details(ids=api_response["aid"])
        if "resources" in detail_lookup["body"]:
            host_detail = detail_lookup["body"]["resources"]

        if host_detail:
            for host in host_detail:
                if "hostname" in host:
                    self.hostname = host["hostname"]
                if "local_ip" in host:
                    self.local_ip = host["local_ip"]
                if "os_version" in host:
                    self.os_version = host["os_version"]
                if "service_provider" in host:
                    self.service_provider = host["service_provider"]
        else:
            # No host details are returned, show the AID for this entry
            self.hostname = api_response["aid"]

        try:
            self.remediation = self.chunk_long_description(
                    spotlight.get_remediations_v2(
                        ids=api_response["remediation"]["ids"]
                        )["body"]["resources"][0]["action"],
                    32
                    )
        except KeyError:
            pass

        if not self.remediation:
            self.remediation = "Not found"

        self.cve_description = self.chunk_long_description(
            api_response['cve']['description'].strip(),
            30
            )

    @staticmethod
    def chunk_long_description(desc, col_width) -> str:
        """Chunks a long string by delimiting with CR based upon column length."""
        desc_chunks = []
        chunk = ""
        for word in desc.split():
            new_chunk = f"{chunk} {word.strip()}"
            if len(new_chunk) >= col_width:
                if new_chunk[0] == " ":
                    new_chunk = new_chunk[1:]
                desc_chunks.append(new_chunk.strip())
                chunk = ""
            else:
                chunk = new_chunk

        delim = "\n"
        desc_chunks.append(chunk.strip())

        return delim.join(desc_chunks)

    def _to_json(self):
        """Return the entire object in JSON format."""
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False)

    def to_object(self):
        """Return the entire object."""
        return json.loads(self._to_json())


def parse_command_line() -> object:
    """Parse the command line for inbound configuration parameters."""
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
        '-b',
        '--base_url',
        help='CrowdStrike API region (us1, us2, eu1, usgov1)\n'
        'NOT required unless you are using `usgov1`',
        required=False
        )
    parser.add_argument(
        '-c',
        '--cve',
        help='CVE IDs to search for. (ex: CVE-2022-12345,CVE-2022-54321)\n'
        'Delimit with a comma (no spaces). The string CVE- is not required.\n'
        'When not provided, all matches with a valid severity are returned.',
        required=False
        )
    parser.add_argument(
        '-x',
        '--exclude',
        help='List of columns to exclude from the display.\n'
        'Delimit with a comma (no spaces).\n'
        '(cve, score, severity, cve_description, created_on, updated_on,\n'
        'hostname, local_ip, os_version, service_provider, remediation)',
        required=False
        )
    parser.add_argument(
        '-i',
        '--include',
        help='List of columns to include in the display, comma-separated.\n'
        'If specified, only these columns will be displayed.\n'
        '(cve, score, severity, cve_description, created_on, updated_on,\n'
        'hostname, local_ip, os_version, service_provider, remediation)',
        required=False
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
    parser.add_argument(
        '-o',
        '--sort',
        help='Sort results by display column.\n'
        "(cve, score, severity, cve_description, created_on, updated_on,\n"
        "hostname, local_ip, os_version, service_provider, remediation, status)",
        required=False
        )
    parser.add_argument(
        '-r',
        '--reverse',
        help='Reverse the sort direction.',
        action="store_true",
        required=False
        )
    parser.add_argument(
        '-p',
        '--hide_progress',
        help='Hide progress indicator as data is retrieved.',
        action="store_false",
        required=False
        )
    parser.add_argument(
        '-d',
        '--deduplicate',
        help='Remove duplicate entries based on hostname and local_ip.',
        action="store_true",
        required=False
        )

    return parser.parse_args()


def inform(msg: str):
    """Provide informational updates to the user as the program progresses."""
    if PROGRESS:
        print(f"\r{' ' * 80}\r{msg}", end='', flush=True)


def get_spotlight_matches(cves: list) -> list:
    """Retrieve a list of matches to the CVEs specified."""
    # Unspecified searches return all with a severity
    filter_string = "cve.severity:!'UNKNOWN'"
    if cves:
        filter_string = f"cve.id:{cves}"
    returned = spotlight.query_vulnerabilities(filter=filter_string)
    if returned["status_code"] >= 400:
        raise SystemExit(returned["body"]["errors"][0]["message"])

    return returned["body"]["resources"]


def remove_exclusions(resultset: dict) -> dict:
    """Remove requested columns from the table display."""
    if INCLUDE:
        return [{key: result[key] for key in INCLUDE} for result in resultset]

    for result in resultset:
        for exclusion in EXCLUDE:
            del result[exclusion]

    return resultset


def get_match_details(match_list: list) -> list:
    """Retrieve details for individual matches to the specified CVEs."""
    returned = []
    seen = set()
    inform("[ Retrieve matches ]")
    match_results = spotlight.get_vulnerabilities(ids=match_list)
    if match_results["status_code"] >= 400:
        raise SystemExit(match_results["body"]["errors"][0]["message"])

    for result in match_results["body"]["resources"]:
        row = SpotlightCVEMatch(result).to_object()
        if args.deduplicate:
            unique_id = (row['hostname'], row['local_ip'])
            if unique_id not in seen:
                seen.add(unique_id)
                inform(f"[ {row['cve']} ] Found {row['hostname']}/{row['local_ip']}")
                returned.append(row)
        else:
            inform(f"[ {row['cve']} ] Found {row['hostname']}/{row['local_ip']}")
            returned.append(row)

    reversing = False
    if SORT_REVERSE:
        reversing = True

    inform("[ Results sort ]")
    returned = sorted(returned, key=lambda item: item[SORT], reverse=reversing)

    return returned


# Allow formats for our tabular output
TABLE_FORMATS = [
    "plain", "simple", "github", "grid", "fancy_grid", "pipe", "orgtbl", "jira", "presto",
    "pretty", "psql", "rst", "mediawiki", "moinmoin", "youtrack", "html", "unsafehtml",
    "latex", "latex_raw", "latex_booktabs", "latex_longtable", "textile", "tsv"
]

# Consume inbound command line parameters
args = parse_command_line()
BASE = "us1"
if args.base_url:
    BASE = args.base_url

CVE_LIST = []
if args.cve:
    for cve in args.cve.upper().split(","):
        if "CVE-" not in cve:
            CVE_LIST.append(f"CVE-{cve}")
        else:
            CVE_LIST.append(cve)

EXCLUDE = []
if args.exclude:
    EXCLUDE = args.exclude.split(",")

INCLUDE = []
if args.include:
    INCLUDE = args.include.split(",")

TABLE_FORMAT = "fancy_grid"
if args.format:
    table_format = args.format.strip().lower()
    if table_format in TABLE_FORMATS:
        TABLE_FORMAT = table_format

SORT = "created_on"
if args.sort:
    sort_types = ["cve", "score", "severity", "cve_description", "created_on", "updated_on",
                  "hostname", "local_ip", "os_version", "service_provider", "remediation", "status"
                  ]
    sort_type = args.sort.strip().lower()
    if sort_type in sort_types:
        SORT = sort_type

SORT_REVERSE = args.reverse
PROGRESS = args.hide_progress

# Connect to the API and create instances of the SpotlightVulnerabilities and Hosts Service Classes
auth = OAuth2(client_id=args.client_id,
              client_secret=args.client_secret,
              base_url=BASE
              )
spotlight = SpotlightVulnerabilities(auth_object=auth)
hosts = Hosts(auth_object=auth)

# Headers used for our results display
HEADERS = {
    "cve": "CVE",
    "score": "Score",
    "severity": "Severity",
    "cve_description": "Description",
    "created_on": "Created",
    "updated_on": "Updated",
    "hostname": "Host",
    "local_ip": "IP Address",
    "os_version": "Operating System",
    "service_provider": "Service Provider",
    "remediation": "Remediation",
    "status": "Status"
}

# Run the process
inform("[ Process startup ]")
details = get_match_details(get_spotlight_matches(CVE_LIST))

# Clear the progress message
print("\r" + " " * 80 + "\r", end='', flush=True)

# Display results
print(
    tabulate(
        tabular_data=remove_exclusions(details),
        headers=HEADERS,
        tablefmt=TABLE_FORMAT
        )
    )
