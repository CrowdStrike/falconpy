r"""CrowdStrike Falcon Detects Advisor utility.

@@@@@@@   @@@@@@@@  @@@@@@@  @@@@@@@@   @@@@@@@  @@@@@@@   @@@@@@
@@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@
@@!  @@@  @@!         @@!    @@!       !@@         @@!    !@@
!@!  @!@  !@!         !@!    !@!       !@!         !@!    !@!
@!@  !@!  @!!!:!      @!!    @!!!:!    !@!         @!!    !!@@!!
!@!  !!!  !!!!!:      !!!    !!!!!:    !!!         !!!     !!@!!!
!!:  !!!  !!:         !!:    !!:       :!!         !!:         !:!
:!:  !:!  :!:         :!:    :!:       :!:         :!:        !:!
 :::: ::   :: ::::     ::     :: ::::   ::: :::     ::    :::: ::
:: :  :   : :: ::      :     : :: ::    :: :: :     :     :: : :

                           ,
                         /'/            /'
                       /' /           /'
                    ,/'  /    _____,/'.     ,   O  ____     ____     ____
                   /`--,/   /'    /'  |    /  /' /'    )--/'    )--)'    )--
                 /'    /  /'    /'    |  /' /'  '---,   /'    /' /'
             (,/'     (_,(___,/(__   _|/(__(__(___,/   (___,/' /'

                                CrowdStrike FalconPy v1.0
                                02.12.22 - jshcodes@CrowdStrike

This utility returns a list of a detections, which can be customized
by passing a FQL filter (-f) when executed. Results are displayed to
the console or dumped (-d) to a JSON save file. Console displays can
be sorted based upon available display fields. (-o, -r)

More detail regarding specific detections can be retrieved by
specifying the detection ID with the -i argument.

Detection status (-u) and visibility (-x, -v) can be adjusted and
detections can be assigned (-a) to a specified UID. (Email address
of a user already existing within your Falcon tenant.)

Several updates can be performed against multiple detections
simultaneously.

Use the --no-color (-n) argument to disable color console output.

Use the --table_fmt (-t) argument to adjust list display formatting.
"""
# pylint: disable=C0209
import json
from datetime import date
from argparse import ArgumentParser, RawTextHelpFormatter
try:
    from tabulate import tabulate
except ImportError as no_tabulate:
    raise SystemExit("The tabulate package must be installed "
                     "in order to use this program."
                     ) from no_tabulate
try:
    from falconpy import Detects, UserManagement
except ImportError as no_falconpy:
    raise SystemExit("The crowdstrike-falconpy package must be "
                     "installed in order to use this program."
                     ) from no_falconpy


class Color:  # pylint: disable=R0903
    """Class to represent the text color codes used for terminal output."""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    LIGHTBLUE = "\033[94m"
    GREEN = "\033[32m"
    LIGHTGREEN = "\033[92m"
    LIGHTYELLOW = "\033[93m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    LIGHTRED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def parse_command_line():  # pylint: disable=R0914
    """Ingest the provided command line parameters and handle any input errors."""
    # Configure argument parsing
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-k", "--falcon_client_id",
                        help="CrowdStrike Falcon API Client ID",
                        required=True
                        )
    parser.add_argument("-s", "--falcon_client_secret",
                        help="CrowdStrike Falcon API Client Secret",
                        required=True
                        )
    parser.add_argument("-c", "--command",
                        help="Command to perform, one of:\n"
                        "list, update, view.",
                        required=False
                        )
    parser.add_argument("-t", "--table_format",
                        help="Table format to use for display, one of:\n"
                        "plain, simple, github, grid, fancy_grid, pipe, orgtbl, \n"
                        "jira, presto, pretty, psql, rst, mediawiki, moinmoin, \n"
                        "youtrack, html, unsafehtml, latext, latex_raw, \n"
                        "latex_booktabs, latex_longtable, textile, or tsv.",
                        required=False
                        )
    parser.add_argument("-f", "--filter",
                        help="FQL filter to use to filter detections",
                        required=False
                        )
    parser.add_argument("-o", "--sort",
                        help="Field to sort by, one of:\n"
                        "id, device_id, status, hostname, tactic, technique, or first_occurrence\n"
                        "Defaults to first_occurrence (asc)",
                        required=False
                        )
    parser.add_argument("-r", "--reverse",
                        help="Reverse the sort order",
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-l", "--limit",
                        help="Total number of detections to display (Max: 1000)",
                        required=False
                        )
    parser.add_argument("-n", "--no_color",
                        help="Disable color output in result displays",
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-i", "--detection_id",
                        help="Detection ID(s) to review or update (comma-delimited)\n"
                        "A maximum of 20 IDs may be specified",
                        required=False
                        )
    parser.add_argument("-a", "--assign",
                        help="UID (email address) of the user to assign the detection",
                        required=False
                        )
    parser.add_argument("-u", "--update_status",
                        help="Status to set for the detection, one of:\n"
                        "new, in_progress, true_positive, false_positive,\n"
                        "ignored, closed, or reopened",
                        required=False
                        )
    parser.add_argument("-x", "--hide",
                        help="Hide this detection from the Falcon console",
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-v", "--show",
                        help="Show this detection in the Falcon console",
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-d", "--dump_to_file",
                        action="store_true",
                        help="Export results to a file. (JSON format)\n"
                        "Exported results contain more complete data than \n"
                        "results rendered to the terminal.",
                        required=False
                        )
    parser.add_argument("-q", "--fql_help",
                        help="Display extended filtering documentation",
                        required=False,
                        action="store_true"
                        )
    args = parser.parse_args()
    cmd, stat, assn, do_dump, tbl_fmt, filt, \
        col, det, srt, rev, lmt = argument_handling(arguments=args)

    for cmd_part in cmd.split(","):
        if cmd_part in ["list", "update", "view", "show", "hide", "assign", "fql"]:
            if cmd_part in ["update", "view", "show", "hide", "assign"]:
                if not det:
                    parser.error("You must provide a Detection ID to use this command.")
                else:
                    det = args.detection_id
        else:
            parser.error(f"The {cmd_part} command is not recognized.")

    c_id = args.falcon_client_id
    c_secret = args.falcon_client_secret
    tod = date.today().strftime("%Y-%m-%d")

    if "," in cmd:
        if ("list" in cmd or "view" in cmd):
            cmd_list = cmd.split(",")
        if "list" in cmd:
            cmd_list.remove("list")
            cmd_list.append("list")
        if "view" in cmd:
            # Move the list command to the end
            cmd_list.remove("view")        
            cmd_list.append("view")

        cmd = ",".join(cmd_list)

    return cmd, c_id, c_secret, do_dump, tbl_fmt, det, filt, stat, col, assn, srt, rev, lmt, tod


def create_action_list(parsed: object):
    """Create a list of actions to perform based upon the arguments provided."""
    t_delim = ""
    t_cmd = ""
    t_det = None
    t_stat = None
    t_assgn = None

    def action_string(act: str, dlm: str, new_val: str):
        returning = f"{act}{dlm}{new_val}"
        dlm = ","

        return returning, dlm

    if parsed.command:
        t_cmd = parsed.command.lower()
        t_delim = ","
    if parsed.detection_id:
        t_det = parsed.detection_id
    if parsed.hide:
        t_cmd, t_delim = action_string(t_cmd, t_delim, "hide")
    if parsed.show:
        t_cmd, t_delim = action_string(t_cmd, t_delim, "show")
    if parsed.update_status:
        t_stat = parsed.update_status.lower()
        t_cmd, t_delim = action_string(t_cmd, t_delim, "update")
    if parsed.assign:
        t_assgn = parsed.assign
        t_cmd, t_delim = action_string(t_cmd, t_delim, "assign")
    if parsed.fql_help:
        t_cmd, t_delim = action_string(t_cmd, t_delim, "fql")
    if not t_cmd and parsed.detection_id:
        t_cmd = "view"
    if not t_cmd:
        t_cmd = "list"

    return t_cmd, t_det, t_stat, t_assgn


def argument_handling(arguments: object):
    """Review parsing results and set required values."""
    s_do_dump = False
    s_tbl_fmt = "fancy_grid"
    s_filt = None
    s_col = False
    s_srt = "first_occurrence"
    s_rev = False
    s_lmt = 1000
    s_cmd, s_det, s_stat, s_assgn = create_action_list(parsed=arguments)

    if arguments.dump_to_file:
        s_do_dump = True
    if arguments.table_format:
        s_tbl_fmt = arguments.table_format.lower()
    if arguments.filter:
        # Can't fiddle with the FQL's case. You'll need to be specific.
        s_filt = arguments.filter
    if arguments.sort:
        s_srt = arguments.sort
    if arguments.reverse:
        s_rev = True
    if arguments.no_color:
        s_col = True
    if arguments.limit:
        if arguments.limit.isdigit():
            if int(arguments.limit) <= 1000:
                s_lmt = int(arguments.limit)

    return s_cmd, s_stat, s_assgn, s_do_dump, s_tbl_fmt, s_filt, s_col, s_det, s_srt, s_rev, s_lmt


def show_result(results: list, style: str, sorting: str, reversing: bool):
    """Display detail table for retrieved actions."""
    display_headers = {
                "display_id": "Detection",
                "hostname": "Hostname / Agent ID",
                "tactic": "Tactic",
                "technique": "Technique",
                "timestamp": "Date occurred"
                }

    end_result = []
    for item in results:
        end_result.append(clean_result(item))
    # Sort our results
    end_result = sorted(end_result, key=lambda item: item[sorting], reverse=reversing)
    # Remove sort-only columns
    for row in end_result:
        row.pop("id", None)
        row.pop("status", None)
        row.pop("first_occurrence", None)
        row.pop("device_id", None)
    print(f"{Color.MAGENTA}{LIST_BANNER}{Color.END}")
    print(tabulate(tabular_data=end_result,
                   headers=display_headers,
                   tablefmt=style
                   ))


def clean_result(itm: dict, extend: bool = False) -> dict:
    """Clean an individual result."""
    fields = [
        "display_id", "status", "id", "device_id", "hostname", "tactic", "technique", "timestamp"
        ]
    cln = {}
    if extend:
        cln["behaviors"] = []
        fields.pop()
        fields.pop()
        fields.pop()
    for field in fields:
        cln[field] = ""

    cln["status"] = itm["status"]
    cln["id"] = itm["detection_id"]
    if not extend:
        cln["id"] = cln["id"].split(":")[2]
        clor = select_status_color(itm["status"])
        cln["display_id"] = f"{clor}{clean_status_string(itm['status'])}{Color.END}\n{cln['id']}"
        if itm.get("assigned_to_name", None):
            nam = itm["assigned_to_name"]
            cln["display_id"] = f"{cln['display_id']}\n{Color.LIGHTGREEN}{nam}{Color.END}"
    cln["device_id"] = itm["device"]["device_id"]
    cln["hostname"] = itm["device"].get("hostname", cln["device_id"])
    bcnt = 0
    for beh in itm["behaviors"]:
        if bcnt == 0:
            cln["first_occurrence"] = beh["timestamp"]
            bcnt += 1
        if extend:
            behave = {}
            behave["description"] = beh["description"]
            behave["tactic"] = beh["tactic"]
            behave["tactic_id"] = beh["tactic_id"]
            behave["technique"] = beh["technique"]
            behave["technique_id"] = beh["technique_id"]
            behave["timestamp"] = beh["timestamp"]
            cln["behaviors"].append(behave)
        else:
            cln["tactic"] = f"{cln['tactic']}\n{beh['tactic']} ({beh['tactic_id']})"
            cln["technique"] = f"{cln['technique']}\n{beh['technique']} ({beh['technique_id']})"
            cln["timestamp"] = f"{cln['timestamp']}\n{beh['timestamp']}"

    if extend:
        cln["assigned"] = itm.get("assigned_to_name", "Unassigned")
        cln["external_ip"] = itm["device"].get("external_ip", "Not available")
        cln["local_ip"] = itm["device"].get("local_ip", "Not available")
        cln["platform_name"] = itm["device"].get("platform_name", "Not available")
        cln["os_version"] = itm["device"].get("os_version", "Not available")
        cln["agent_version"] = itm["device"].get("agent_version", "Not available")
    else:
        cln["hostname"] = f"{Color.BOLD}{cln['hostname']}{Color.END}\n{itm['device']['device_id']}"

    return cln


def get_details(item_list: list) -> object:  # list or dict
    """Retrieve the details for the item list provided."""
    details = falcon_detects.get_detect_summaries(ids=item_list)
    if details["status_code"] == 200:
        details = details["body"]["resources"]

    return details


def dump_output(prefix: str, output_data: list):
    """Dump retrieved data results to JSON formatted output files."""
    output_file = f"{prefix}_detects.json"
    with open(output_file, "w", encoding="utf-8") as result_file:
        json.dump(output_data, result_file, indent=4)

    print("Detects data export completed.")


def list_elements(perform_dump: bool,
                  today_val: str,
                  table_fmt: str,
                  search_filter: str,
                  sort_field: str,
                  sort_reverse: bool,
                  max_rows: int
                  ):  # pylint: disable=R0913
    """Look up all elements of the specified type and display their details."""
    def error_display(err_branch):
        for err in err_branch:
            ecode = err["code"]
            emsg = err["message"]
            print(f"[{ecode}] {emsg}")
    id_lookup = falcon_detects.query_detects(filter=search_filter, limit=max_rows)
    if id_lookup["status_code"] == 200:
        items = id_lookup["body"]["resources"]
        if items:
            item_details = get_details(item_list=items)
            if isinstance(item_details, list):
                if perform_dump:
                    dump_output(prefix=today_val, output_data=item_details)
                else:
                    show_result(results=item_details,
                                style=table_fmt,
                                sorting=sort_field,
                                reversing=sort_reverse
                                )
            else:
                error_display(item_details["body"]["errors"])
        else:
            raise SystemExit("No detections available to retrieve.")
    else:
        if "errors" in id_lookup["body"]:
            error_display(id_lookup["body"]["errors"])
        else:
            raise SystemExit("Unable to retrieve list of detection IDs for the filter specified.")


def display_detail(detection: str):
    """Display detailed information for the specified detection."""
    filter_string = create_id_filter(detection)
    detail_lookup = falcon_detects.query_detects(filter=filter_string)
    if detail_lookup["status_code"] == 200:
        detailed = get_details(item_list=detail_lookup["body"]["resources"])
        if not isinstance(detailed, list):
            raise SystemExit("Detection not found for the ID specified.")
        for detailer in detailed:
            result = clean_result(detailer, extend=True)
            print(f"{Color.MAGENTA}{SUMMARY_BANNER}{Color.END}")
            print(f"%-15s {Color.CYAN}{result['id']}{Color.END}" % "Detection:")
            clr = select_status_color(result["status"])
            stat_disp = clean_status_string(result["status"])
            print(f"%-15s {clr}{stat_disp}{Color.END}" % "Status:")
            aclr = ""
            if result['assigned'] != "Unassigned":
                aclr = Color.LIGHTGREEN
            print(f"%-15s {aclr}{result['assigned']}{Color.END}" % "Assigned to:")
            print(f"%-15s {Color.BOLD}{result['hostname']}{Color.END}" % "Hostname:")
            print(f"%-15s {result['device_id']}" % "Agent ID:")
            print(f"%-15s {result['agent_version']}" % "Agent version:")
            print(f"%-15s {result['platform_name']} ({result['os_version']})" % "Platform:")
            if result["external_ip"] != "Not available":
                print(f"%-15s {result['external_ip']}" % "External IP:")
            if result["local_ip"] != "Not available":
                print(f"%-15s {result['local_ip']}" % "Local IP:")
            print(f"{Color.MAGENTA}{DETAIL_BANNER}{Color.END}")
            for ioc in result["behaviors"]:
                print(f"%-15s {Color.BOLD}{ioc['tactic']}{Color.END}" % "Tactic:",
                      f"({ioc['tactic_id']})"
                      )
                print(f"%-15s {Color.RED}{ioc['technique']}{Color.END}" % "Technique:",
                      f"({ioc['technique_id']})"
                      )
                clean_ts = ioc["timestamp"].replace("T", " at ").replace("Z", "")
                print(f"%-15s {clean_ts}" % "Occurred:")
                full_description = clean_description(ioc["description"].replace(". ", ".\n"))
                print(f"{'═' * 72}")
                print(f"{full_description}\n")
    else:
        raise SystemExit("Detection not found for the ID specified.")


def create_id_filter(incoming: str) -> str:
    """Create a `or` style FQL filter based upon the ID(s) provided."""
    generated = ""
    delim = ""
    left = ""
    right = ""
    for d_id in incoming.split(","):
        if len(d_id) > 2:
            left = "("
            right = ")"
        if generated:
            delim = ","
        generated = f"{left}{generated}{delim}detection_id:*'*{d_id}'{right}"

    return generated


def select_status_color(incoming: str) -> str:
    """Select the appropriate color based upon status."""
    returned = Color.LIGHTBLUE
    if incoming in ["in_progress", "reopened"]:
        returned = Color.LIGHTYELLOW
    if incoming == "true_positive":
        returned = Color.LIGHTRED
    if incoming == "new":
        returned = Color.YELLOW
    if incoming == "closed":
        returned = Color.GREEN

    return returned


def clean_description(incoming: str) -> str:
    """Format behavior description strings for output."""
    description = []
    for desc in incoming.split("\n"):
        part = ""
        for piece in desc.split():
            delim = ""
            if len(part) > 60:
                description.append(part)
                part = ""
            if part:
                delim = " "
            part = f"{part}{delim}{piece}"
        description.append(part)

    return "\n".join(description)


def clean_status_string(incoming: str) -> str:
    """Format the status string for output."""
    stats = []
    stat_val = incoming.replace("_", " ").split()
    for val in stat_val:
        new_val = val.title()
        stats.append(new_val)

    return " ".join(stats)


def update_detection_status(detection: str, status_val: str):
    """Update the detection to the provided status."""
    filter_string = create_id_filter(detection)
    detail_lookup = falcon_detects.query_detects(filter=filter_string)
    if detail_lookup["status_code"] == 200:
        upd = detail_lookup["body"]["resources"]
        update_result = falcon_detects.update_detects_by_ids(ids=upd, status=status_val)
        if update_result["status_code"] == 200:
            stat_disp = clean_status_string(status_val)
            for updated in detection.split(","):
                print(f"Changed {updated} status to {stat_disp}.")
        else:
            errors = update_result["body"]["errors"]
            for err in errors:
                ecode = err.get("code", 500)
                emsg = err["message"]
                print(f"[{ecode}] {emsg}")
    else:
        raise SystemExit("Unable to locate detection for the ID specified.")


def update_detection_visibility(detection: str, visible: bool):
    """Update the detection to the provided visibility."""
    filter_string = create_id_filter(detection)
    detail_lookup = falcon_detects.query_detects(filter=filter_string)
    if detail_lookup["status_code"] == 200:
        upd = detail_lookup["body"]["resources"]
        if not upd:
            raise SystemExit("Unable to locate detection for the ID specified.")
        if not visible:
            detected = falcon_detects.get_detect_summaries(ids=upd)
            mapped = {}
            for det in detected["body"]["resources"]:
                mapped[det["detection_id"].split(":")[2]] = det["detection_id"]
        update_result = falcon_detects.update_detects_by_ids(ids=upd, show_in_ui=visible)
        if update_result["status_code"] == 200:
            for updated in detection.split(","):
                if visible:
                    print(f"Detection {updated} set to visible.")
                else:
                    print(f"Detection {updated} set to hidden.")
                    print(f"Detection ID: {Color.BOLD}{mapped[updated]}{Color.END}")
                    print("You will need to provide this value to",
                          "support in order to restore this record.")
        else:
            errors = update_result["body"]["errors"]
            for err in errors:
                ecode = err.get("code", 500)
                emsg = err["message"]
                print(f"[{ecode}] {emsg}")
    else:
        raise SystemExit("Unable to locate detection for the ID specified.")


def assign_detection(detection: str, assignee: str):
    """Look up the UUID for the UID provided and assign the detection to the discovered UUID."""
    filter_string = create_id_filter(detection)
    detail_lookup = falcon_detects.query_detects(filter=filter_string)
    if detail_lookup["status_code"] == 200:
        upd = detail_lookup["body"]["resources"]
        if not upd:
            raise SystemExit("Unable to locate detection for the ID specified.")

        falcon_users = UserManagement(auth_object=falcon_detects.auth_object)
        user_lookup = falcon_users.retrieve_user_uuid(uid=assignee)
        if user_lookup["status_code"] == 200:
            uuid = user_lookup["body"]["resources"][0]
        else:
            raise SystemExit("Unable to locate user ID for user email provided.")
        update_result = falcon_detects.update_detects_by_ids(ids=upd, assigned_to_uuid=uuid)
        if update_result["status_code"] == 200:
            for updated in detection.split(","):
                print(f"Detection {updated} assigned to {assignee}.")
        else:
            errors = update_result["body"]["errors"]
            for err in errors:
                ecode = err.get("code", 500)
                emsg = err["message"]
                print(f"[{ecode}] {emsg}")
    else:
        raise SystemExit("Unable to locate detection for the ID specified.")


LIST_BANNER = r"""
 _____         __               __   __
|     \.-----.|  |_.-----.----.|  |_|__|.-----.-----.-----.
|  --  |  -__||   _|  -__|  __||   _|  ||  _  |     |__ --|
|_____/|_____||____|_____|____||____|__||_____|__|__|_____|
"""

DETAIL_BANNER = r"""
 ______         __                 __
|   __ \.-----.|  |--.---.-.--.--.|__|.-----.----.-----.
|   __ <|  -__||     |  _  |  |  ||  ||  _  |   _|__ --|
|______/|_____||__|__|___._|\___/ |__||_____|__| |_____|
"""

SUMMARY_BANNER = r"""
 _____         __               __   __
|     \.-----.|  |_.-----.----.|  |_|__|.-----.-----.
|  --  |  -__||   _|  -__|  __||   _|  ||  _  |     |
|_____/|_____||____|_____|____||____|__||_____|__|__|

 _______
|     __|.--.--.--------.--------.---.-.----.--.--.
|__     ||  |  |        |        |  _  |   _|  |  |
|_______||_____|__|__|__|__|__|__|___._|__| |___  |
                                            |_____|
"""

STATUS_TYPES = [
    "new", "in_progress", "true_positive", "false_positive", "ignored", "closed", "reopened"
    ]

DALEK = r"""
____    __    ____  ___      .______      .__   __.  __  .__   __.   _______  __
\   \  /  \  /   / /   \     |   _  \     |  \ |  | |  | |  \ |  |  /  _____||  |
 \   \/    \/   / /  ^  \    |  |_)  |    |   \|  | |  | |   \|  | |  |  __  |  |
  \            / /  /_\  \   |      /     |  . `  | |  | |  . `  | |  | |_ | |  |
   \    /\    / /  _____  \  |  |\  \----.|  |\   | |  | |  |\   | |  |__| | |__|
    \__/  \__/ /__/     \__\ | _| `._____||__| \__| |__| |__| \__|  \______| (__)

                _n____n__
               /         \---||--<
     ___      /___________\
              _|____|____|_       EXTERMINATE!!!!
              _|____|____|_
  _____        |    |    |
              --------------
              | || || || ||\
      ____    | || || || || \++++++++------<
              ===============
              |   |  |  |   |
    _____    (| O | O| O| O |)
             |   |   |   |   |
            (| O | O | O | O |)
 ___         |   |   |   |    |
           (| O |  O | O  | O |)
    ____    |   |    |    |    |
           (| O |  O |  O |  O |)
           ======================

Hiding a detection will remove the record from all search results moving
forward. If you need to access this record again, you will need to contact
support to restore it to your instance. THIS SHOULD BE CONSIDERED PERMANENT!
"""

# Format looks a little off here in order to display in the console properly
# Show in the console using the -q command line argument.
FQL_HELP = r"""
 _______ _______ ___         ___ ___       __
|   _   |   _   |   |       |   Y   .-----|  .-----.
|.  1___|.  |   |.  |       |.  1   |  -__|  |  _  |
|.  __) |.  |   |.  |___    |.  _   |_____|__|   __|
|:  |   |:  1   |:  1   |   |:  |   |        |__|
|::.|   |::..   |::.. . |   |::.|:. |
`---'   `----|:.`-------'   `--- ---'
             `--'

FQL Documentation: https://falconpy.io/Usage/Falcon-Query-Language.html

FILTERS
Filter options are broken out into four categories:
    General, Behavioral, Devices and Miscellaneous

Include all provided FQL filters in double quotes in order to preserve formatting!

Wildcards may be used but should also position an asterisk before the first quote.

    Example: -f "device.hostname:*'*search-string*'"

General
    Example: -f "status:'in_progress'"

adversary_ids	        date_updated	last_behavior	    max_severity_displayname
assigned_to_name	detection_id	max_confidence	    seconds_to_resolved
cid	                first_behavior	max_severity	    seconds_to_triaged
status

Behavioral - behaviors.filter
    Example: -f "behaviors.tactic:'Execution'"

alleged_filetype	md5	                                    sha256
behavior_id	        objective	                            tactic
cmdline	                parent_details.parent_cmdline	            technique
confidence	        parent_details.parent_md5	            timestamp
contral_graph_id	parent_details.parent_process_id	    triggering_process_id
device_id	        parent_details.parent_process_graph_id	    triggering_process_graph_id
filename	        parent_details.parent_sha256	            user_id
ioc_source	        pattern_disposition	                    user_name
ioc_type	        scenario
ioc_value	        severity

Devices - device.filter
    Example: -f "device.platform_name:'Linux'"

agent_load_flags	first_seen	        platform_name
agent_local_time	hostname	        product_type
agent_version	        last_seen	        product_type_desc
bios_manufacturer	local_ip	        release_group
bios_version	        mac_address	        reduced_functionality_mode
cid	                machine_domain	        serial_number
config_id_base	        major_version	        site_name
config_id_build	        minor_version	        status
config_id_platform	modified_timestamp	system_product_name
cpu_signature	        os_version	        system_manufacturer
device_id	        ou
external_ip	        platform_id

Miscellaneous
    Example: -f "hostinfo.domain:*'*search-string*'"

hostinfo.domain	                        quarantined_files.id
hostinfo.active_directory_dn_display	quarantined_files.paths
quarantined_files.sha256                quarantined_files.state

"""

if __name__ == "__main__":
    # Parse the command line arguments and set our variables
    command, key, secret, dump, fmt, det_id, \
        fql, status, nocol, assigned, sort, reverse, limit, today = parse_command_line()
    # Authenticate using our provided falcon client_id and client_secret
    falcon_detects = Detects(client_id=key, client_secret=secret)
    # If token_fail_reason contains any value, we failed to authenticate
    if falcon_detects.token_fail_reason:
        # Report the authentication failure reason and stop processing
        raise SystemExit(falcon_detects.token_fail_reason)
    # Turn off the colors if they're feeling monochromatic
    if nocol:
        for attr in dir(Color):
            if "__" not in attr:
                setattr(Color, attr, "")
    # Perform the operation they requested based upon their inputs
    try:
        for action in command.split(","):
            if action == "list":
                # Display to console or dump to file
                list_elements(perform_dump=dump,
                              today_val=today,
                              table_fmt=fmt,
                              search_filter=fql,
                              sort_field=sort,
                              sort_reverse=reverse,
                              max_rows=limit
                              )
            elif action == "view":
                # View the details of the specified detection
                display_detail(detection=det_id)
            elif action == "update":
                # Update the detection status
                update_detection_status(detection=det_id, status_val=status)
            elif action in ["show", "hide"]:
                # Update the detection visibility
                SHOWING = True
                PROCEED = True
                if action == "hide":
                    PROCEED = False
                    SHOWING = False
                    # That's dangerous, have a dalek and make sure it's really what you wanna do
                    print(DALEK)
                    confirm = input("If you wish to proceed, please type the word 'exterminate': ")
                    if confirm == "exterminate":
                        # They really wanna do it
                        PROCEED = True
                    else:
                        # On second thought...
                        print(f"Hide action cancelled. Record(s) {det_id} not modified.")
                if PROCEED:
                    # Perform the update
                    update_detection_visibility(detection=det_id, visible=SHOWING)
            elif action == "assign":
                # Assign the detection to the specified UID
                assign_detection(detection=det_id, assignee=assigned)
            elif action == "fql":
                # Display FQL filtering help
                print(FQL_HELP)
    except Exception as errored:  # pylint: disable=W0703  # Catching any variation
        raise SystemExit(f"Command failed with error: {str(errored)}.") from errored
    # Discard our token on our way out
    falcon_detects.auth_object.revoke(falcon_detects.token)
