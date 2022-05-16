r"""CrowdStrike incident triage.

  _____            _     _            _
  \_   \_ __   ___(_) __| | ___ _ __ | |_ ___
   / /\/ '_ \ / __| |/ _` |/ _ \ '_ \| __/ __|
/\/ /_ | | | | (__| | (_| |  __/ | | | |_\__ \
\____/ |_| |_|\___|_|\__,_|\___|_| |_|\__|___/

            _____      _
           /__   \_ __(_) __ _  __ _  ___
             / /\/ '__| |/ _` |/ _` |/ _ \
            / /  | |  | | (_| | (_| |  __/
            \/   |_|  |_|\__,_|\__, |\___|
                               |___/

                        for FalconPy v1.1.1

Requirements
    - crowdstrike-falconpy (v1.1.1+)
    - tabulate

Search, review and modify incidents within a CrowdStrike Falcon tenant.

A complete list of available incident filters can be found at:
https://falconpy.io/Service-Collections/Incidents.html#available-filters
"""
from argparse import ArgumentParser, RawTextHelpFormatter
from enum import Enum
from tabulate import tabulate
try:
    from falconpy import (
        Incidents,
        UserManagement,
        __version__ as FALCONPY_VERSION
    )
except ImportError as no_falconpy:
    raise SystemExit(
        "The CrowdStrike FalconPy SDK is not installed. Application cannot continue."
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


class Status(Enum):
    """Enum used to describe status values."""

    NEW = 20
    REOPENED = 25
    INPROGRESS = 30
    CLOSED = 40


class StatusColor(Enum):
    """Enum to describe colors used for status displays."""

    NEW = Color.LIGHTYELLOW
    REOPENED = Color.YELLOW
    INPROGRESS = Color.LIGHTBLUE
    CLOSED = Color.GREEN


def consume_arguments():
    """Consume any user provided arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    upd = parser.add_argument_group("update arguments")
    upd.add_argument("-a", "--assign",
                     help="Email of the user to assign this incident to",
                     required=False
                     )
    upd.add_argument("-d", "--description",
                     help="Description to apply to the incident",
                     required=False
                     )
    upd.add_argument("-i", "--incident",
                     help="Incident ID to modify",
                     required=False
                     )
    upd.add_argument("-n", "--name",
                     help="Name to apply to the incident",
                     required=False
                     )
    upd.add_argument("-r", "--remove_tags",
                     help="Tags to remove (comma delimit)\nCase sensitive",
                     required=False
                     )
    upd.add_argument("-t", "--add_tags",
                     help="Tags to add (comma delimit)",
                     required=False
                     )
    upd.add_argument("-u", "--status",
                     help="Status to change to (Integer or String)",
                     required=False
                     )
    upd.add_argument("-x", "--unassign",
                     help="Remove the assignment from the incident",
                     required=False,
                     action="store_true"
                     )
    srch = parser.add_argument_group("search arguments")
    srch.add_argument("-f", "--filter",
                      help="FQL string to use to filter incidents",
                      required=False
                      )
    req = parser.add_argument_group("required arguments")
    req.add_argument("-k", "--falcon_client_id",
                     help="CrowdStrike Falcon API Client ID",
                     required=False
                     )
    req.add_argument("-s", "--falcon_client_secret",
                     help="CrowdStrike Falcon API Client Secret",
                     required=False
                     )

    return parser.parse_args()


def open_sdk(client_id: str, client_secret: str):
    """Create instances of our two Service Classes and return them."""
    inc_object = Incidents(client_id=client_id, client_secret=client_secret)
    um_object = UserManagement(auth_object=inc_object.auth_object)

    return inc_object, um_object


def hard_fail(incoming_error: dict):
    """Retrieve error information and display it as part of the system exit."""
    emsg = incoming_error["message"]
    ecode = incoming_error["code"]
    raise SystemExit(f"[{ecode}] {emsg}")


def get_incident_ids(filter_string: str):
    """Retrieve all available incident IDs."""
    params = {}
    if filter_string:
        params = {
            "filter": filter_string
        }
    incident_id_lookup = sdk.query_incidents(**params)
    if incident_id_lookup["status_code"] != 200:
        hard_fail(incident_id_lookup["body"]["errors"][0])

    if not incident_id_lookup["body"]["resources"]:
        NO_RESULTS =[Color.LIGHTRED,
            "_  _ ____    ____ ____ ____ _  _ _    ___ ____",
            "|\ | |  |    |__/ |___ [__  |  | |     |  [__",
            "| \| |__|    |  \ |___ ___] |__| |___  |  ___]",
            Color.END
            ]
        raise SystemExit("\n".join(NO_RESULTS))

    return incident_id_lookup["body"]["resources"]


def get_incident_data(id_list: list):
    """Retrieve incident details using the IDs provided."""
    incident_detail_lookup = sdk.get_incidents(ids=id_list)
    if incident_detail_lookup["status_code"] != 200:
        hard_fail(incident_detail_lookup["body"]["errors"][0])

    return incident_detail_lookup["body"]["resources"]


def chunk_long_description(desc, col_width) -> str:
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


def get_user_detail(uuid: str):
    """Retrieve assigned to user information for tabular display."""
    lookup_result = users.retrieve_user(ids=uuid)
    if lookup_result["status_code"] != 200:
        hard_fail(lookup_result["body"]["errors"][0])
    user_info = lookup_result["body"]["resources"][0]
    first = user_info["firstName"]
    last = user_info["lastName"]
    uid = user_info["uid"]

    return f"{first} {last} ({uid})"


def incident_information(inc_data: dict):
    """Parse incident overview information for tabular display."""
    inc_info = []
    inc_info.append(inc_data.get("name", ""))
    inc_info.append(f"{Color.BOLD}{inc_data['incident_id'].split(':')[2]}{Color.END}")
    inc_info.append(f"Start: {inc_data.get('start', 'Unknown').replace('T', ' ')}")
    inc_info.append(f"  End: {inc_data.get('end', 'Unknown').replace('T', ' ')}")
    assigned = inc_data.get("assigned_to", None)
    if assigned:
        inc_info.append(f"\n{Color.UNDERLINE}Assignment{Color.END}")
        inc_info.append(get_user_detail(assigned))
    if inc_data.get("description", None):
        inc_info.append(" ")
        inc_info.append(chunk_long_description(inc_data["description"], 50))

    return "\n".join(inc_info)


def hosts_information(inc_data: dict):
    """Parse hosts information for tabular display."""
    returned = ""
    if "hosts" in inc_data:
        host_str = []
        for host in inc_data["hosts"]:
            host_info = []
            host_info.append(
                f"{Color.BOLD}{host.get('hostname', 'Unidentified')}{Color.END}"
                f" ({host.get('platform_name', 'Not available')})"
                )
            host_info.append(
                f"{Color.DARKCYAN}{host.get('device_id', 'Not available')}{Color.END}"
                )
            host_info.append(f"  Int: {host.get('local_ip', 'Not available')}")
            host_info.append(f"  Ext: {host.get('external_ip', 'Not available')}")
            first = host.get('first_seen', 'Unavailable').replace('T', ' ').replace('Z', ' ')
            host_info.append(f"First: {first}")
            last = host.get('last_seen', 'Unavailable').replace('T', ' ').replace('Z', ' ')
            host_info.append(f" Last: {last}")
            host_str.append("\n".join(host_info))
        if host_str:
            returned = "\n".join(host_str)
        else:
            returned = "Unidentified"

    return returned


def check_version():
    """Confirm the running version of FalconPy, exit on incompatible versions."""
    version_detail = FALCONPY_VERSION.split(".")
    version_fail = False
    if float(f"{version_detail[0]}.{version_detail[1]}") < 1.1:
        version_fail = True
    elif float(f"{version_detail[0]}.{version_detail[1]}") == 1.1:
        if int(version_detail[2]) < 1:
            version_fail = True
    if version_fail:
        raise SystemExit(
            "This application requires CrowdStrike FalconPy v1.1.1."
            f" You currently have v{FALCONPY_VERSION} installed."
            )


def status_information(inc_data: dict):
    """Parse status information for tabular display."""
    inc_status = [
        f"{StatusColor[Status(inc_data['status']).name].value}"
        f"{Status(inc_data['status']).name.title().replace('Inp','InP')}{Color.END}"
        ]
    tag_list = inc_data.get("tags", [])
    if tag_list:
        inc_status.append(" ")
        tag_list = [f"{Color.MAGENTA}{tg}{Color.END}" for tg in tag_list]
        inc_status.extend(tag_list)

    return "\n".join(inc_status)


def show_incident_table(incident_listing: list):
    """Display all returned incidents in tabular fashion."""
    if not incident_listing:
        hard_fail({"message": "No incidents found", "code": 404})

    headers = {
        "status": f"{Color.BOLD}Status{Color.END}",
        "incident": f"{Color.BOLD}Incident{Color.END}",
        "hostname": f"{Color.BOLD}Host{Color.END}",
        "tactics": f"{Color.BOLD}Tactics{Color.END}",
        "techniques": f"{Color.BOLD}Techniques{Color.END}",
        "objectives": f"{Color.BOLD}Objective{Color.END}s"
    }
    incident_list = []
    for inc in incident_listing:
        inc_detail = {}
        inc_detail["status"] = status_information(inc)
        inc_detail["incident"] = incident_information(inc)
        inc_detail["hostname"] = hosts_information(inc)
        inc_detail["tactics"] = "\n".join(inc["tactics"])
        inc_detail["techniques"] = "\n".join(inc["techniques"])
        inc_detail["objectives"] = "\n".join(inc["objectives"])
        incident_list.append(inc_detail)

    print(tabulate(incident_list, headers=headers, tablefmt="fancy_grid"))


def get_incident_full_id(partial: str):
    """Retrieve the full incident ID based off of the partial ID provided."""
    search_result = sdk.query_incidents()
    if search_result["status_code"] != 200:
        hard_fail(search_result["body"]["errors"][0])
    found = False
    for inc in search_result["body"]["resources"]:
        incnum = inc.split(":")[2]
        if incnum == partial:
            found = inc
            break

    if not found:
        hard_fail({"message": "Unable to find incident ID specified.", "code": 404})

    return found


def update_status(inc_id: str, stat_val: int or str):
    """Update the incident status to the status value provided."""
    stat_int = stat_val
    if not stat_val.isnumeric():
        try:
            stat_int = Status(stat_val.upper()).value
        except AttributeError:
            hard_fail({"message": "Invalid status specified.", "code": 500})
    stat_change = any(int(stat_enum.value) == int(stat_int) for stat_enum in Status)
    if not stat_change:
        print(stat_change)
        for stat_enum in Status:
            print(stat_enum.value)
        hard_fail({"message": "Invalid status specified.", "code": 500})

    change_result = sdk.perform_incident_action(ids=get_incident_full_id(inc_id),
                                                update_status=stat_int
                                                )
    if change_result["status_code"] != 200:
        hard_fail(change_result["body"]["errors"][0])


def update_name(inc_id: str, name: str):
    """Update the incident name to the value provided."""
    change_result = sdk.perform_incident_action(ids=get_incident_full_id(inc_id),
                                                update_name=name
                                                )
    if change_result["status_code"] != 200:
        hard_fail(change_result["body"]["errors"][0])


def tagging(inc_id: str, tags: list, untag: bool = False):
    """Assign or remove all tags provided."""
    action = {
        "ids": get_incident_full_id(inc_id)
    }
    if untag:
        action["delete_tag"] = tags
    else:
        action["add_tag"] = tags
    change_result = sdk.perform_incident_action(**action)
    if change_result["status_code"] != 200:
        hard_fail(change_result["body"]["errors"][0])


def assignment(inc_id: str, assign_to: str = "", unassign: bool = False):
    """Assign the incident specified to the user specified."""
    if unassign:
        change_result = sdk.perform_incident_action(ids=get_incident_full_id(inc_id),
                                                    unassign=True
                                                    )
        if change_result["status_code"] != 200:
            hard_fail(change_result["body"]["errors"][0])
    else:
        lookup_result = users.retrieve_user_uuid(uid=assign_to)

        if lookup_result["status_code"] != 200:
            hard_fail(lookup_result["body"]["errors"][0])
        change_result = sdk.perform_incident_action(
            ids=get_incident_full_id(inc_id),
            update_assigned_to_v2=lookup_result["body"]["resources"][0]
            )
        if change_result["status_code"] != 200:
            hard_fail(change_result["body"]["errors"][0])


def check_for_missing_arguments(arg_list: ArgumentParser):
    """Confirm an incident ID has been provided for update oriented operations."""
    # These updates require an incident ID to be specified
    check_args = [
        arg_list.status, arg_list.name, arg_list.add_tags, arg_list.remove_tags,
        arg_list.unassign, arg_list.assign, arg_list.description
        ]
    missing_incident_id = [bool(arg) for arg in check_args]
    if max(missing_incident_id):
        # Make sure we have an incident ID for operations that require it
        if not arg_list.incident:
            hard_fail({
                "message": "You must provide an incident ID to perform this operation.",
                "code": 500
                })


def update_description(inc_id: str, desc_str: str):
    """Update the incident description to the value provided."""
    change_result = sdk.perform_incident_action(ids=get_incident_full_id(inc_id),
                                                update_description=desc_str
                                                )
    if change_result["status_code"] != 200:
        hard_fail(change_result["body"]["errors"][0])


BANNER = fr"""{Color.BOLD}{Color.DARKCYAN}
  _____            _     _            _     {Color.YELLOW} _____      _{Color.DARKCYAN}
  \_   \_ __   ___(_) __| | ___ _ __ | |__ {Color.YELLOW} /__   \_ __(_) __ _  __ _  ___{Color.DARKCYAN}
   / /\/ '_ \ / __| |/ _` |/ _ \ '_ \| __/  {Color.YELLOW}  / /\/ '__| |/ _` |/ _` |/ _ \{Color.DARKCYAN}
/\/ /_ | | | | (__| | (_| |  __/ | | | |_   {Color.YELLOW} / /  | |  | | (_| | (_| |  __/{Color.DARKCYAN}
\____/ |_| |_|\___|_|\__,_|\___|_| |_|\__|  {Color.YELLOW} \/   |_|  |_|\__,_|\__, |\___|
                                                                |___/{Color.END}  for {Color.LIGHTRED}CrowdStrike{Color.RED} Falcon{Color.END}
"""
# Check for an invalid version of FalconPy
check_version()
# Consume any provided command line arguments
args = consume_arguments()
# Create instances of our two Service Classes; Incidents and UserManagement
sdk, users = open_sdk(args.falcon_client_id, args.falcon_client_secret)
# Check for a passed lookup filter
FILTER = None
if args.filter:
    FILTER = args.filter
# Retrieve a list of all incident IDs
incident_ids = get_incident_ids(FILTER)
# Retrieve the details for all incident IDs returned
incidents = get_incident_data(incident_ids)
# Check for any missing argument combinations
check_for_missing_arguments(args)
# Run through all arguments, performing any requested updates
if args.status:
    # Perform a status change
    update_status(inc_id=args.incident, stat_val=args.status)
if args.name:
    # Perform a name change
    update_name(inc_id=args.incident, name=args.name)
if args.add_tags:
    # Add tags
    tagging(inc_id=args.incident, tags=args.add_tags.split(","), untag=False)
if args.remove_tags:
    # Remove tags
    tagging(inc_id=args.incident, tags=args.remove_tags.split(","), untag=True)
if args.unassign:
    # Remove the current assignment
    assignment(inc_id=args.incident, unassign=True)
if args.assign:
    # Assign the incident to a user
    assignment(inc_id=args.incident, assign_to=args.assign)
if args.description:
    # Perform a description change
    update_description(inc_id=args.incident, desc_str=args.description)

print(BANNER)
# Any updates required are complete. Show our result table.
show_incident_table(get_incident_data(incident_ids))
