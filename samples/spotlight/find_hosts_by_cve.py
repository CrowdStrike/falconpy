"""Retrieve hosts by CVE vulnearbility.

Creation date: 01.13.2021 - jshcodes@CrowdStrike

This solution requires crowdstrike-falconpy v0.8.6+
"""
from argparse import ArgumentParser, RawTextHelpFormatter
from tabulate import tabulate
from falconpy import SpotlightVulnerabilities, Hosts, OAuth2

BANNER = """
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
"""


def parse_command_line() -> object:
    """Parse the command line for inbound configuration parameters."""
    parser = ArgumentParser(
        description=BANNER,
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
        'Delimit with a comma (no spaces). The string CVE- is not required.',
        required=True
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
        help='Sort results by creation time (asc or desc).',
        required=False
    )

    return parser.parse_args()


def get_spotlight_matches(cves: list) -> list:
    """Retrieve a list of matches to the CVEs specified."""
    returned = spotlight.query_vulnerabilities(
        filter=f"cve.id:{cves}",
        sort=f"created_timestamp|{SORT}"
        )
    if returned["status_code"] >= 400:
        raise SystemExit(returned["body"]["errors"][0]["message"])

    return returned["body"]["resources"]


def remove_exclusions(resultset: dict) -> dict:
    """Remove requested columns from the table display."""
    for result in resultset:
        for exclusion in EXCLUDE:
            if not isinstance(result, str):
                del result[exclusion]

    return resultset


def chunk_long_description(desc, col_width) -> str:
    """Chunks a long string by delimiting with CR based upon column length."""
    desc_chunks = []
    chunk = ""
    for word in desc.split():
        new_chunk = f"{chunk} {word.strip()}"
        if len(new_chunk) >= col_width:
            desc_chunks.append(new_chunk)
            chunk = ""
        else:
            chunk = new_chunk

    delim = "\n"

    return delim.join(desc_chunks)


def get_match_details(match_list: list) -> list:
    """Retrieve details for individual matches to the specified CVEs."""
    returned = []
    match_results = spotlight.get_vulnerabilities(ids=match_list)
    if match_results["status_code"] >= 400:
        raise SystemExit(match_results["body"]["errors"][0]["message"])

    for result in match_results["body"]["resources"]:
        impacted_host_hostname = "Not found"
        impacted_host_local_ip = "Not found"
        impacted_host_os_version = "Not found"
        impacted_host_service_provider = "Not found"

        host_detail = hosts.get_device_details(ids=result["aid"])["body"]["resources"]
        for host in host_detail:
            if "hostname" in host:
                impacted_host_hostname = host["hostname"]
            if "local_ip" in host:
                impacted_host_local_ip = host["local_ip"]
            if "os_version" in host:
                impacted_host_os_version = host["os_version"]
            if "service_provider" in host:
                impacted_host_service_provider = host["service_provider"]
        try:
            remediation = chunk_long_description(
                spotlight.get_remediations_v2(
                    ids=result["remediation"]["ids"]
                    )["body"]["resources"][0]["action"],
                30
                )
        except KeyError:
            remediation = "Not found"
        if not remediation:
            remediation = "Not found"
        description = chunk_long_description(result["cve"]["description"].strip(), 15)

        row = {
            "cve": result["cve"]["id"],
            "score": result["cve"]["base_score"],
            "severity": result["cve"]["severity"],
            "cve_description": description,
            "created_on": result["created_timestamp"],
            "updated_on": result["updated_timestamp"],
            "hostname": impacted_host_hostname,
            "local_ip": impacted_host_local_ip,
            "os_version": impacted_host_os_version,
            "service_provider": impacted_host_service_provider,
            "remediation": remediation
        }
        returned.append(row)

    return returned

TABLE_FORMATS = [
    "plain", "simple", "github", "grid", "fancy_grid", "pipe", "orgtbl", "jira", "presto",
    "pretty", "psql", "rst", "mediawiki", "moinmoin", "youtrack", "html", "unsafehtml",
    "latex", "latex_raw", "latex_booktabs", "latex_longtable", "textile", "tsv"
]

args = parse_command_line()
BASE = "us1"
if args.base_url:
    BASE = args.base_url

CVE_LIST = []
for cve in args.cve.upper().split(","):
    if "CVE-" not in cve:
        CVE_LIST.append(f"CVE-{cve}")
    else:
        CVE_LIST.append(cve)
EXCLUDE = []
if args.exclude:
    EXCLUDE = args.exclude.split(",")

TABLE_FORMAT = "grid"
if args.format:
    table_format = args.format.strip().lower()
    if table_format in TABLE_FORMATS:
        TABLE_FORMAT = table_format

SORT = "asc"
if args.sort:
    sort_dir = args.sort.strip().lower()
    if sort_dir in ["asc", "desc"]:
        SORT = sort_dir

auth = OAuth2(client_id=args.client_id,
              client_secret=args.client_secret,
              base_url=BASE
              )
spotlight = SpotlightVulnerabilities(auth_object=auth)
hosts = Hosts(auth_object=auth)

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
    "remediation": "Remediation"
}

details = get_match_details(get_spotlight_matches(CVE_LIST))
print(
    tabulate(
        tabular_data=remove_exclusions(details),
        headers=remove_exclusions(HEADERS),
        tablefmt=TABLE_FORMAT
        )
    )
