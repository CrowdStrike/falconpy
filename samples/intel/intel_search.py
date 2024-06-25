#!/usr/bin/env python3
r"""CrowdStrike Falcon Intel API search example using the FalconPy library.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |   Falcon Intelligence
`-------'                         `-------'

This sample searches Falcon Intelligence for all actor,
indicator or report matches to a specified string.

If only one result is returned for a category, full details
for the record are displayed.

A maximum of 50,000 results per category will be returned.

Creation date: 03.30.23 - jshcodes@CrowdStrike

This application requires:
    pyfiglet
    termcolor
    tabulate
    crowdstrike-falconpy v1.3.0+
"""

import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from concurrent.futures import ThreadPoolExecutor
from csv import writer, QUOTE_ALL
from datetime import datetime
try:
    from pyfiglet import figlet_format
except ImportError as no_figlet:
    raise SystemExit("The pyfiglet library must be installed.\n"
                     "Install it with `python3 -m pip install pyfiglet`."
                     ) from no_figlet
try:
    from termcolor import colored
except ImportError as no_termcolor:
    raise SystemExit("The termcolor library must be installed.\n"
                     "Install it with `python3 -m pip install termcolor"
                     ) from no_termcolor
try:
    from tabulate import tabulate
except ImportError as no_tabulate:
    raise SystemExit("The tabulate library must be installed.\n"
                     "Install it with `python3 -m pip install tabulate`."
                     ) from no_tabulate
try:
    from falconpy import Intel
except ImportError as no_falconpy:
    raise SystemExit("The CrowdStrike FalconPy library must be installed.\n"
                     "Install it with `python3 -m pip install crowdstrike-falconpy`."
                     ) from no_falconpy


class Progress:
    """Class to track our start time and progress indicator."""

    start_time = datetime.utcnow().timestamp()
    progress = ["|", "/", "-", "\\", "-"]
    pos = 0

    def next(self):
        """Display the indicator and increment the indicator position."""
        print(f"  {colored('[', 'yellow')}{bold(self.progress[self.pos])}{colored(']', 'yellow')} "
              f"{bold('Processing, please wait...')}",
              end="\r",
              flush=True
              )
        self.increment()

    def increment(self):
        """Increment the indicator position."""
        self.pos += 1
        if self.pos == len(self.progress) - 1:
            self.pos = 0


def parse_command_line():
    """Parse any provided command line arguments and return the namespace."""
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter,
                            epilog="For a list of table formats check this page: "
                            "https://github.com/astanin/python-tabulate#table-format"
                            )
    requir = parser.add_argument_group("required arguments")
    requir.add_argument("-f", "--find",
                        required=True,
                        help="Search string to identify"
                        )
    requir.add_argument("-k", "--client_id",
                        required=True,
                        help="CrowdStrike API client ID"
                        )
    requir.add_argument("-s", "--client_secret",
                        required=True,
                        help="CrowdStrike API client secret"
                        )
    parser.add_argument("-r", "--reverse",
                        help="Reverse the sort.",
                        default=False,
                        action="store_true"
                        )
    parser.add_argument("-t", "--types",
                        help="Types to search (indicator, report or actor). Comma delimited."
                        )
    parser.add_argument("-tf", "--table_format",
                        help="Set the table format.",
                        default="fancy_grid"
                        )
    parser.add_argument("-o", "--output_prefix",
                        help="Output filename prefix for storing results (CSV format).",
                        default=None
                        )
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )

    parsed = parser.parse_args()
    allow = ["indicator", "report", "actor"]
    parsed.types = [t for t in parsed.types.split(",") if t in allow] if parsed.types else allow

    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)

    return parsed


def bold(val: str):
    """Format the provided string for bold terminal output and return it."""
    return colored(val, attrs=["bold"])


# pylint: disable=E0606
def batch_get(func: object, filt: str, catg: str):
    """Asynchronously retrieve Falcon Intelligence API results."""
    offset = 0
    running = True
    returned = []
    notified = False
    while running:
        lookup = func(filter=filt, offset=offset, limit=5000, fields="__full__")
        total = lookup["body"]["meta"].get("pagination", {}).get("total", 0)
        if not notified:
            notify = f"Retrieving {total:,} {catg} results."
            if total > 50000:
                notify = f"Retrieving first 50,000 of {total:,} {catg} results."
            print(notify)
            notified = True
        else:
            progress.next()
        if lookup["body"]["resources"]:
            offset += len(lookup["body"]["resources"])
            returned.extend(lookup["body"]["resources"])
        if offset >= total:
            running = False

    return returned


def chunk_long_description(desc: str, col_width: int = 120) -> str:
    """Chunk a long string by delimiting with CR based upon column length."""
    desc_chunks = []
    chunk = ""
    for word in desc.split():
        new_chunk = f"{chunk}{word.strip()} "
        if len(new_chunk) >= col_width:
            desc_chunks.append(new_chunk)
            chunk = ""
        else:
            chunk = new_chunk

    delim = "\n"
    desc_chunks.append(chunk)

    return delim.join(desc_chunks)


def simple_list_display(keyval: str, record: dict, title: str, no_val: bool = False):
    """Dynamic handler for displaying information provided as simple lists."""
    if keyval in record:
        if len(record[keyval]):
            if no_val:
                result = ", ".join(list(record[keyval]))
            else:
                result = ", ".join(m["value"].title() for m in record[keyval])
            print(f"{bold(title)}: {result}\n")


def large_list_display(keyval: str, record: dict, title: str):
    """Dynamic handler for displaying list information with an underlined header."""
    if keyval in record:
        if len(record[keyval]):
            res = ", ".join(t["value"].title() for t in record[keyval])
            res = f"{chunk_long_description(res)}"
            res = f"{colored(title, attrs=['bold', 'underline'])}\n{res}"
            print(f"{res}\n")


def actor_type_and_capability(record: dict):
    """Display an actor's capability, origins and type."""
    if "capability" in record or "origins" in record:
        spacer1 = ""
        spacer2 = ""
        cap = ""
        orig = ""
        typ = ""
        if "actor_type" in record:
            typ = record["actor_type"].title()
            typ = f"{bold('Actor type')}: {typ}"
            spacer1 = " " * 5
        if "capability" in record:
            cap = record["capability"]["value"]
            cap = f"{bold('Capability')}: {cap}"
            spacer2 = " " * 5
        if "origins" in record:
            if len(record["origins"]):
                orig = ", ".join([o["value"] for o in record["origins"]])
                orig = f"{bold('Origins')}: {orig}"
        print(f"{typ}{spacer1}{cap}{spacer2}{orig}\f")


def actor_activity_dates(record: dict):
    """Display first and last activity date for an actor."""
    first = ""
    last = ""
    dspace = ""
    if "first_activity_date" in record:
        first = datetime.fromtimestamp(record["first_activity_date"])
        if "last_activity_date" in record:
            if record["last_activity_date"] < record["first_activity_date"]:
                first = datetime.fromtimestamp(record["last_activity_date"])
        first = f"{bold('First activity')}: {first.strftime('%m-%d-%Y')}"
        dspace = " " * 5
    if "last_activity_date" in record:
        last = datetime.fromtimestamp(record["last_activity_date"])
        if "first_activity_date" in record:
            if record["first_activity_date"] > record["last_activity_date"]:
                last = datetime.fromtimestamp(record["first_activity_date"])
        last = f"{bold('Most recent activity')}: {last.strftime('%m-%d-%Y')}"
    print(f"{first}{dspace}{last}\n")


def display_single_actor(actor: dict):
    """Display the results for a single actor search."""
    actor_name = "   ".join([n.title() for n in actor["name"].split(" ")])
    print(colored(figlet_format(actor_name, font="chunky", width=220), "magenta"))
    # First and Last activity dates
    actor_activity_dates(actor)
    if "known_as" in actor:
        aka = ", ".join(list(actor['known_as'].split(',')))
        aka = f"{chunk_long_description(aka)}"
        aka = f"{colored('Otherwise known as', attrs=['bold', 'underline'])}\n{aka}"
        print(f"{aka}\n")
    if actor["description"]:
        print(colored("Adversary description", attrs=["bold", "underline"]))
        print(f"{chunk_long_description(actor['description'])}\n")
    # Actor capability, origin and type
    actor_type_and_capability(actor)
    # Motivations
    simple_list_display("motivations", actor, "Motivations")
    # Objectives
    simple_list_display("objectives", actor, "Objectives")
    # Capabilities
    simple_list_display("capabilities", actor, "Capabilities")
    # Target Regions
    simple_list_display("target_regions", actor, "Targeted regions")
    # Target Countries
    large_list_display("target_countries", actor, "Targeted countries")
    # Target industries
    large_list_display("target_industries", actor, "Targeted industries")
    # Kill chain
    if "kill_chain" in actor:
        chain = actor["kill_chain"]
        print(colored("Tactics, Techniques and Procedures", attrs=["bold", "underline"]))
        for key, val in chain.items():
            if "rich_text_" not in key:
                if val[:3] != "\r\n\t" and val[:3] != "CVE":
                    val = "\r\n\t" + val
                key = " ".join([k.title() for k in key.split("_")]).replace("And", "and")
                print(f"{bold(key)}: {chunk_long_description(val, 100)}\n")
    # eCrime Kill chain
    if "ecrime_kill_chain" in actor:
        ekc = actor["ecrime_kill_chain"]
        print(colored("ECrime Tactics, Techniques and Procedures", attrs=["underline"]))
        for key, val in ekc.items():
            if "rich_text_" not in key and val:
                key = " ".join([k.title() for k in key.split("_")]).replace("And", "and")
                print(f"{bold(key)}: {val}")


def display_single_report(report: dict):
    """Display results for a single report search."""
    names = report["name"].split(" ")
    friendly_name = names[0]
    if len(names) > 1:
        proper_name = " ".join(names[1:])
    else:
        proper_name = friendly_name
    print(colored(figlet_format(friendly_name.replace("-", " "),
                                width=220,
                                font="starwars"
                                ),
                  "magenta"
                  ),
          end="\r"
          )
    print(f"{bold(proper_name)}\n")
    created = ""
    dspace = ""
    last_mod = ""
    if "created_date" in report:
        created = datetime.fromtimestamp(report["created_date"])
        created = f"{bold('Created on')}: {created.strftime('%m-%d-%Y %H:%M:%S')}"
        dspace = " " * 5
    if "last_modified_date" in report:
        last_mod = datetime.fromtimestamp(report["last_modified_date"])
        last_mod = f"{bold('Last modification:')}: {last_mod.strftime('%m-%d-%Y %H:%M:%S')}"
    if created or last_mod:
        print(f"{created}{dspace}{last_mod}\n")
    # Tags
    simple_list_display("tags", report, "Tags")
    # Target Countries
    simple_list_display("target_countries", report, "Target countries")
    # Target Industries
    simple_list_display("target_industries", report, "Target industries")
    # Motivations
    simple_list_display("motivations", report, "Motivations")
    if "description" in report:
        desc = report['description']
        cur_pos = 0
        running = True
        while running:
            cur_pos = desc.find("[vc")
            end_pos = desc.find("]", cur_pos)
            if not end_pos:
                end_pos = len(desc)
            if cur_pos != -1 and end_pos != -1:
                desc = f"{desc[:cur_pos]}{desc[end_pos+1:]}"
            cur_pos = desc.find("[/vc")
            end_pos = desc.find("]", cur_pos)
            if not end_pos:
                end_pos = len(desc)
            if cur_pos != -1 and end_pos != -1:
                desc = f"{desc[:cur_pos]}{desc[end_pos+1:]}"
            if "[vc" not in desc and "[/vc" not in desc:
                running = False
        desc = desc.replace("\n", "\n\n\t")
        print(chunk_long_description(desc))


def display_single_indicator(indicator: dict):
    """Display results for a single indicator search."""
    name = indicator["indicator"]
    print(f"\n{colored(name, attrs=['bold', 'underline'])}\n")
    if "published_date" in indicator:
        pub_date = datetime.fromtimestamp(indicator["published_date"])
        pub_date = f"{bold('Publish date')}: {pub_date.strftime('%m-%d-%Y %H:%M:%S')}"
        print(pub_date)
    if "last_updated" in indicator:
        last_update = datetime.fromtimestamp(indicator["last_updated"])
        last_update = f"{bold('Last updated')}: {last_update.strftime('%m-%d-%Y %H:%M:%S')}"
        print(last_update)
    # Indicator Type
    ind_type = indicator["type"]
    removed = ""
    deleted = indicator["deleted"]
    if deleted:
        removed = colored("Deleted", "red", attrs=["bold"])
    print(f"{bold('Indicator type')}: {ind_type}     {removed}")
    # Domain Types
    simple_list_display("domain_types", indicator, "Domain types", no_val=True)
    # IP Address Types
    simple_list_display("ip_address_types", indicator, "IP address types", no_val=True)
    # Malicious Confidence
    if "malicious_confidence" in indicator:
        mal_confidence = indicator["malicious_confidence"]
        mal_confidence = f"{bold('Confidence')}: {mal_confidence}"
        print(mal_confidence)
    # Malware Families
    simple_list_display("malware_families", indicator, "Malware families", no_val=True)
    # Targets
    simple_list_display("targets", indicator, "Targets")
    # Threat Types
    simple_list_display("threat_types", indicator, "Threat types", no_val=True)
    # Kill Chain
    simple_list_display("kill_chains", indicator, "Kill chain", no_val=True)
    if "labels" in indicator:
        label_list = [
            f"{lab['name']} ({datetime.fromtimestamp(lab['last_valid_on']).strftime('%m-%d-%Y')})"
            for lab in indicator["labels"]
            ]
        labels = ", ".join(label_list)
        if indicator["labels"]:
            print(f"{bold('Labels')}: {chunk_long_description(labels)}")

    if "vulnerabilities" in indicator:
        vulns = "\n".join([f"  • {i}" for i in indicator["vulnerabilities"]])
        vulns = f"\n{bold('Vulnerabilities')}\n{vulns}"
        if indicator["vulnerabilities"]:
            print(vulns)

    if "relations" in indicator:
        related = "\n".join([f"  • {i['indicator']}" for i in indicator["relations"]])
        related = f"\n{bold('Related indicators')}\n{related}"
        if indicator["relations"]:
            print(related)


def display_actors(actor_list: list, direction: bool, table_style: str, output_prefix: str):
    """Display the results for an actors search sorted by actor name."""
    # Sort by actor name
    actors = sorted(actor_list,
                    key=lambda x: x["name"],
                    reverse=direction
                    )
    if actors:
        if output_prefix:
            with open(f"{output_prefix}_actors.csv", "w", encoding="utf-8") as csv_output:
                csv_writer = writer(csv_output, quoting=QUOTE_ALL)
                csv_writer.writerow(["Name", "ID"])
                for row in actors:
                    csv_writer.writerow([row["name"], f"ADV-{row['id']}"])

        if len(actors) != 1:
            print(colored(figlet_format("Actors", font="cyberlarge"), "magenta"), end="\r")
            print(tabulate([{
                bold("Name"): res["name"],
                bold("ID"): f"ADV-{res['id']}"
            } for res in actors], headers="keys", tablefmt=table_style))
        else:
            display_single_actor(actors[0])


def display_indicators(ind_list: list, direction: bool, table_style: str, output_prefix: str):
    """Display the results for an indicators search sorted by indicator value."""
    indicators = sorted(ind_list,
                        key=lambda x: x["indicator"].replace("https://", ""),
                        reverse=direction
                        )
    if indicators:
        if output_prefix:
            with open(f"{output_prefix}_indicators.csv", "w", encoding="utf-8") as csv_output:
                csv_writer = writer(csv_output, quoting=QUOTE_ALL)
                csv_writer.writerow(["Indicator", "Type"])
                for row in indicators:
                    csv_writer.writerow([row["indicator"], row["type"]])
        if len(indicators) != 1:
            print(colored(figlet_format("Indicators", font="cyberlarge"), "magenta"), end="\r")
            print(tabulate([{
                bold("Indicator"): f"{res['indicator'][:100]}"
                                   f"{'...' if len(res['indicator']) >= 100 else ''}",
                bold("Type"): res["type"]
                } for res in indicators], headers="keys", tablefmt=table_style)
                )
        else:
            display_single_indicator(indicators[0])


def display_reports(rep_list: list, direction: bool, table_style: str, output_prefix: str):
    """Display the results for a reports search sorted by report name."""
    reports = sorted(rep_list,
                     key=lambda x: report_name_sort(x["name"]),
                     reverse=direction
                     )
    if reports:
        if output_prefix:
            with open(f"{output_prefix}_reports.csv", "w", encoding="utf-8") as csv_output:
                csv_writer = writer(csv_output, quoting=QUOTE_ALL)
                csv_writer.writerow(["Name", "Type"])
                for row in reports:
                    csv_writer.writerow([row["name"], row["type"].get("name")])
        if len(reports) != 1:
            print(colored(figlet_format("Reports", font="cyberlarge"), "magenta"), end="\r")
            print(tabulate([{
                bold("Name"): f"{res['name'][:100]}{'...' if len(res['name']) >= 100 else ''}",
                bold("Type"): res["type"].get("name")
                } for res in reports], headers="keys", tablefmt=table_style)
                )
        else:
            display_single_report(reports[0])


def not_found(tlist: list, search_string: str):
    """Display a properly formatted results not found message."""
    fail_msg = "No"
    if "actor" in tlist:
        remain = len([t for t in tlist if t != 'actor'])
        if remain == 0:
            spot = ""
        if remain == 1:
            spot = " or"
        if remain == 2:
            spot = ","
        fail_msg = f"{fail_msg} actor{spot}"
    if "indicator" in tlist:
        remain = len([t for t in tlist if t != 'indicator'])
        fail_msg = f"{fail_msg} indicator{' or' if remain > 0 else ''}"
    if "report" in tlist:
        fail_msg = f"{fail_msg} report"
    fail_msg = f"{fail_msg} matches found for {bold(search_string)}."

    raise SystemExit(fail_msg)


# pylint: disable=R0913
def perform_search(sdk: Intel, srch: str, types: list, tformat: str, rev: bool, prfx: str):
    """Search to identify if the search string matches an indicator, report, or actor."""
    print(f"Searching Falcon Threat Intelligence for {bold(srch)}.")
    # Search each result type asynchronously
    futures = {}
    with ThreadPoolExecutor() as executor:
        if "actor" in types:
            futures["actors"] = executor.submit(
                batch_get, func=sdk.query_actor_entities, filt=f"name:*'*{srch}*'", catg="actor"
                )
        if "indicator" in types:
            futures["indicators"] = executor.submit(
                batch_get, func=sdk.query_indicator_entities,
                filt=f"indicator:*'*{srch}*'", catg="indicator"
                )
        if "report" in types:
            futures["reports"] = executor.submit(
                batch_get, func=sdk.query_report_entities, filt=f"name:*'*{srch}*'", catg="report"
                )
    act_result, ind_result, rep_result = ([], [], [])
    for cat, fut in futures.items():
        if cat == "actors":
            act_result = fut.result()
            display_actors(act_result, rev, tformat, prfx)

        if cat == "indicators":
            ind_result = fut.result()
            display_indicators(ind_result, rev, tformat, prfx)

        if cat == "reports":
            rep_result = fut.result()
            display_reports(rep_result, rev, tformat, prfx)

    if not ind_result and not rep_result and not act_result:
        not_found(types, srch)

    return len(act_result), len(ind_result), len(rep_result)


def report_name_sort(rpt_name: str):
    """Return a sort key based upon the report name."""
    rptn = rpt_name.split(" ")
    try:
        rpta = rptn[0].split("-")
        returned = (rpta[0], rpta[1])
    except IndexError:
        returned = (rptn[0], "")

    return returned


def show_result_totals(act_cnt: int, ind_cnt: int, rep_cnt: int, typ_list: list):
    """Display the totals for each result type."""
    if max([act_cnt, ind_cnt, rep_cnt]):
        totstub = "\nTotal"
        tots = ""
        if "actor" in typ_list:
            acts = bold(f"{act_cnt:,}")
            tots = f"{tots}{totstub} actors: {acts}"
        if "indicator" in typ_list:
            inds = bold(f"{ind_cnt:,}")
            tots = f"{tots}{totstub} indicators: {inds}"
        if "report" in typ_list:
            reps = bold(f"{rep_cnt:,}")
            tots = f"{tots}{totstub} reports: {reps}"
        print(tots)


def main(args: Namespace):
    """Search for a specified string and identify if it matches an indicator, report, or actor."""
    # Perform the search using an authenticated instance of the Intel Service Class
    ret = perform_search(Intel(client_id=args.client_id, client_secret=args.client_secret, debug=args.debug),
                         args.find,               # Search string
                         args.types,              # Types to display
                         args.table_format,       # Table format
                         args.reverse,            # Reverse sort boolean,
                         args.output_prefix       # Output file prefix
                         )
    return *ret, args.types


if __name__ == "__main__":
    # Start the timer and configure the progress indicator
    progress = Progress()
    # Parse command line arguments, run the routine, and show the result totals
    show_result_totals(*main(parse_command_line()))
    # Show the total execution time
    exec_time = bold(f"{datetime.utcnow().timestamp() - progress.start_time:,.2f}")
    print(f"Execution time: {exec_time} seconds")
