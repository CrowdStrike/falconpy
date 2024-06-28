r"""Spotlight results quick report generator.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |      FalconPy SDK
`-------'                         `-------'

       ____          __  ___      __   __
      / __/__  ___  / /_/ (_)__ _/ /  / /_
     _\ \/ _ \/ _ \/ __/ / / _ `/ _ \/ __/
    /___/ .__/\___/\__/_/_/\_, /_//_/\__/
       /_/                /___/
          ____       _     __     ___                    __
         / __ \__ __(_)___/ /__  / _ \___ ___  ___  ____/ /_
        / /_/ / // / / __/  '_/ / , _/ -_) _ \/ _ \/ __/ __/
        \___\_\_,_/_/\__/_/\_\ /_/|_|\__/ .__/\___/_/  \__/
                                       /_/

This example requires crowdstrike-falconpy v1.3.0 or greater.

Easy Object Authentication is also demonstrated in this sample.
"""
import logging
import json
import time
from datetime import datetime
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import Hosts, SpotlightVulnerabilities, _VERSION


SEVERITIES = ["unknown", "none", "low", "medium", "high", "critical"]
CVE_BANNER = r"""
  ______     _______
 / ___\ \   / / ____|___
| |    \ \ / /|  _| / __|
| |___  \ V / | |___\__ \
 \____|  \_/  |_____|___/
"""
HOSTS_BANNER = r"""
 _   _           _
| | | | ___  ___| |_ ___
| |_| |/ _ \/ __| __/ __|
|  _  | (_) \__ \ |_\__ \
|_| |_|\___/|___/\__|___/
"""
RESULTS_BANNER = r"""
 ____                 _ _
|  _ \ ___  ___ _   _| | |_ ___
| |_) / _ \/ __| | | | | __/ __|
|  _ <  __/\__ \ |_| | | |_\__ \
|_| \_\___||___/\__,_|_|\__|___/
"""
HOST_AUTH = None


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    req = parser.add_argument_group("required arguments")
    req.add_argument("-k", "--client_id", help="CrowdStrike Falcon API Client ID.", required=True)
    req.add_argument("-s", "--client_secret",
                     help="CrowdStrike Falcon API Client Secret.",
                     required=True
                     )
    parser.add_argument("--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-d", "--days",
                        help="Include days from X days backwards (3-45).",
                        default=0
                        )
    parser.add_argument("-f", "--file",
                        help="File to import data from.\n"
                        "Data is queried from the API if this argument is not provided.",
                        default=None
                        )
    parser.add_argument("-o", "--output",
                        help="File to output results to.\n"
                        "Output is not performed if this argument is not provided.",
                        default=None
                        )
    parser.add_argument("-a", "--allow_dupes",
                        help="Allow duplicates.",
                        default=False,
                        action="store_true"
                        )
    
    
    parsed = parser.parse_args()
    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)
    

    return parsed


def query_spotlight(key: str, secret: str, days: str, aft: str = None):
    """Retrieve a batch of Spotlight Vulnerability matches."""

    def do_query(qfilter: str):
        returned = spotlight.query_vulnerabilities_combined(
            filter=qfilter,
            after=aft,
            sort="updated_timestamp|asc",
            limit=400,
            facet="cve"
            )

        return returned["status_code"], returned

    spotlight = SpotlightVulnerabilities(client_id=key, client_secret=secret)

    global HOST_AUTH  # pylint: disable=W0603
    HOST_AUTH = spotlight  # Save this here so we can use it to auth to hosts

    query_filter = "cve.id:!['']+status:!'closed'+status:!'expired'"
    if int(days) >= 3:
        query_filter = f"{query_filter}+last_seen_within:'{days}'"
    stat, all_results = do_query(query_filter)
    while stat == 429:
        print("Rate limit met, waiting 0.5 seconds to retry.")
        time.sleep(0.5)
        stat, all_results = do_query(query_filter)
    if stat != 200:
        raise SystemExit("Unable to retrieve Spotlight Vulnerability matches.")

    return all_results["body"]["meta"]["pagination"]["total"], \
           all_results["body"]["meta"]["pagination"]["after"], \
           len(all_results["body"]["resources"]), \
           all_results["body"]["resources"]


def get_total_sensor_count():
    """Retrieve the total number of available sensors within the tenant."""
    hosts = Hosts(auth_object=HOST_AUTH)
    returned = hosts.query_devices()
    if returned["status_code"] != 200:
        returned = "Unknown"
    else:
        returned = returned["body"]["meta"]["pagination"]["total"]

    return returned


def get_worst_hostname(host_id: str):
    """Retrieve the hostname for the host with the most Spotlight matches."""
    hosts = Hosts(auth_object=HOST_AUTH)
    returned = hosts.get_device_details(host_id)
    if returned["status_code"] != 200:
        returned = host_id
    else:
        returned = f"{returned['body']['resources'][0]['hostname']} ({host_id})"

    return returned


def inform(msg: str):
    """Send dynamic command line updates."""
    print(f"{msg}", end="\r", flush=True)


def process_matches(arg: Namespace):
    """Process Spotlight Vulnerability matches."""
    retrieved = 0
    valid = 0
    if arg.file:
        with open(arg.file, "r", encoding="utf-8") as loader:
            matches = json.load(loader)
            for match_list in matches["sensor"].values():
                valid += sum(len(x) for x in match_list.values())
    else:
        matches = {}
        matches["sensor"] = {}
        matches["cve"] = {}
        for sev in SEVERITIES:
            matches["cve"][sev] = {}
        after = None
        total = 1
        while retrieved <= total:
            total, after, returned, result = query_spotlight(key=arg.client_id,
                                                             secret=arg.client_secret,
                                                             days=arg.days,
                                                             aft=after
                                                             )
            retrieved += returned
            for match in result:
                aid = match.get("aid")
                cve = match.get("cve", {})
                cve_id = cve["id"]
                severity_match = cve.get("severity", "unknown").lower()
                if aid not in matches["sensor"]:
                    matches["sensor"][aid] = {}
                    for sev in SEVERITIES:
                        matches["sensor"][aid][sev] = []
                if cve_id not in matches["sensor"][aid][severity_match] or arg.allow_dupes:
                    matches["sensor"][aid][severity_match].append(cve_id)
                if cve_id not in matches["cve"][severity_match].keys():
                    matches["cve"][severity_match][cve_id] = []
                if aid not in matches["cve"][severity_match][cve_id] or arg.allow_dupes:
                    matches["cve"][severity_match][cve_id].append(aid)
            inform(f" {formatted(retrieved)} of {formatted(total)}")
        msg = f"{' '*30}\n{formatted(retrieved)} total matches retrieved"
        if arg.allow_dupes:
            msg = f"{msg}."
        else:
            for match_list in matches["sensor"].values():
                valid += sum(len(x) for x in match_list.values())

            dupes = retrieved - valid
            msg = f"{msg}, {formatted(dupes)} duplicate{'s' if dupes > 1 else ''} discarded."
        inform(msg)

    return matches, retrieved if arg.allow_dupes else valid


def formatted(num_to_format: int):
    """Format integers for terminal output."""
    return f"{num_to_format:,}"


def process_results(output_file: str, matches: dict, total_matched: int):  # pylint: disable=R0914
    """Write the output file and display the results."""
    total_hosts = get_total_sensor_count()
    total_cve_matches = sum(len(m) for m in matches["cve"].values())
    worst_aid = max(matches["sensor"],
                    key=lambda x: sum(len(matches["sensor"][x][sev]) for sev in SEVERITIES)
                    )
    worst_host = get_worst_hostname(worst_aid)
    worst_aid_count = sum(len(matches["sensor"][worst_aid][sev]) for sev in SEVERITIES)
    total_host_pct = f"{100 * len(matches['sensor']) / total_hosts:0.2f}"
    total_host_match_pct = f"{100 * worst_aid_count / total_cve_matches:0.2f}"
    worst_critical = max(matches["cve"]["critical"],
                         key=lambda x: len(matches["cve"]["critical"][x])
                         )
    worst_critical_count = formatted(len(matches['cve']['critical'][worst_critical]))
    worst_high = max(matches["cve"]["high"], key=lambda x: len(matches["cve"]["high"][x]))
    worst_high_count = formatted(len(matches['cve']['high'][worst_high]))
    worst_medium = max(matches["cve"]["medium"], key=lambda x: len(matches["cve"]["medium"][x]))
    worst_medium_count = formatted(len(matches['cve']['medium'][worst_medium]))
    worst_low = max(matches["cve"]["low"], key=lambda x: len(matches["cve"]["low"][x]))
    worst_low_count = formatted(len(matches['cve']['low'][worst_low]))

    print(RESULTS_BANNER)
    print(f"{formatted(total_cve_matches)} CVEs produced "
          f"{formatted(total_matched)} Spotlight Vulnerability matches across "
          f"{formatted(total_hosts)} sensors"
          )
    print(HOSTS_BANNER)
    print(f"{formatted(len(matches['sensor']))} hosts "
          "were identified with Spotlight Vulnerability matches "
          f"({total_host_pct}% of total sensors)"
          )
    print(f"Worst host: {worst_host} "
          f"({formatted(worst_aid_count)} matches for "
          f"{total_host_match_pct}% of total CVEs matched)"
          )
    print(CVE_BANNER)
    print(f"{formatted(total_cve_matches)} matched CVEs ("
          f"{len(matches['cve']['critical'])} critical, "
          f"{len(matches['cve']['high'])} high, "
          f"{len(matches['cve']['medium'])} medium, "
          f"{len(matches['cve']['low'])} low)"
          )
    print(f"Critical CVE with the most matches: {worst_critical} "
          f"({worst_critical_count} matched hosts)"
          )
    print(f"High CVE with the most matches: {worst_high} ({worst_high_count} matched hosts)")
    print(f"Medium CVE with the most matches: {worst_medium} ({worst_medium_count} matched hosts)")
    print(f"Low CVE with the most matches: {worst_low} ({worst_low_count} matched hosts)")
    if output_file:
        with open(args.output, "w", encoding="utf-8") as save_file:
            json.dump(matches, save_file, indent=4)
        print(f"The data used in this report has been saved to {output_file}")

if __name__ == "__main__":
    vers = _VERSION.split(".")
    main_minor = float(f"{vers[0]}.{vers[1]}")
    patch = int(vers[2])
    if main_minor < 1.2 or (main_minor == 1.2 and patch < 2):
        raise SystemExit("This sample requires crowdstrike-falconpy v1.2.2 or greater.")
    start_time = datetime.now().timestamp()
    args = consume_arguments()
    if args.file:
        HOST_AUTH = Hosts(client_id=args.client_id, client_secret=args.client_secret, debug=args.debug)
    process_results(args.output, *process_matches(args))
    total_run_time = datetime.now().timestamp() - start_time
    print(f"\nReport generated in {total_run_time:,.2f} seconds.")
