r"""CrowdStrike Falcon Sensor Update Policy management utilty.

______     _ _               _    _             _
| ___ \   | (_)             | |  | |           | |
| |_/ /__ | |_  ___ _   _   | |  | | ___  _ __ | | __
|  __/ _ \| | |/ __| | | |  | |/\| |/ _ \| '_ \| |/ /
| | | (_) | | | (__| |_| |  \  /\  / (_) | | | |   <
\_|  \___/|_|_|\___|\__, |   \/  \/ \___/|_| |_|_|\_\
                     __/ |
                    |___/    for Sensor Update Policies

                                   FalconPy v1.4.4

Creation date: 05.06.2022 - jshcodes@CrowdStrike

Required packages
  crowdstrike-falconpy
  tabulate

Multiple simultaneous actions may be performed against
multiple Sensor Update Policy records using this utility.
"""
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
from tabulate import tabulate
try:
    from falconpy import (
        SensorUpdatePolicy,
        HostGroup,
        __version__ as FALCONPY_VERSION
    )
except ImportError as no_falconpy:
    RED = "\033[91m"
    YEL = "\033[33m"
    NOCOL = "\033[0m"
    BOLD = "\033[1m"
    raise SystemExit(fr"""{RED}
_  _ ____    ____ ____ _    ____ ____ _  _ ___  _   _
|\ | |  |    |___ |__| |    |    |  | |\ | |__]  \_/
| \| |__|    |    |  | |___ |___ |__| | \| |      |{YEL}   ヽ༼ຈʖ̯ຈ༽ﾉ{NOCOL}

This application requires CrowdStrike FalconPy v1.0+
Install it with: {BOLD}python3 -m pip install crowdstrike-falconpy{NOCOL}
""") from no_falconpy


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


def connect_sensor_update_api(key: str, sec: str, kid: str, base: str):
    """Connect to the sensor update policies service collection."""
    return SensorUpdatePolicy(client_id=key, client_secret=sec, member_cid=kid, base_url=base)


def connect_host_group_api(key: str, sec: str, kid: str, base: str):
    """Connect to the Host Group service collection."""
    return HostGroup(client_id=key, client_secret=sec, member_cid=kid, base_url=base)


def generate_api_error_list(error_object: list):
    """Display all error messages received from the API."""
    error_list = []
    for err in error_object:
        error_list.append(f"[{err['code']}] {err['message']}")
    return "\n".join(error_list)


def step_indicator():
    """Super lazy progress indicator."""
    global INDICATOR_POSITION  # pylint: disable=W0603
    INDICATOR_POSITION += 1  # pylint: disable=E0602
    if INDICATOR_POSITION > len(INDICATOR) - 1:
        INDICATOR_POSITION = 0
    return INDICATOR[INDICATOR_POSITION]


def shiny_help_text(inbound: str):
    """Shine up the help text display."""
    inbound = inbound.replace("______", f"{Color.BLUE}______")
    inbound = inbound.replace("|___/", f"|___/{Color.END}")
    inbound = inbound.replace("Creation date:", f"{Color.BOLD}Creation date:{Color.END}")
    inbound = inbound.replace("Required packages", f"{Color.UNDERLINE}{Color.BOLD}Required packages{Color.END}")
    inbound = inbound.replace("Sensor Update Policies", f"{Color.DARKCYAN}Sensor Update Policies{Color.END}")
    inbound = inbound.replace("jshcodes@CrowdStrike",
                              f"{Color.GREEN}jshcodes{Color.END}{Color.BOLD}@{Color.RED}CrowdStrike{Color.END}"
                              )
    return inbound


def consume_arguments():
    """Consume arguments from the command line."""
    desc = shiny_help_text(__doc__)
    parser = ArgumentParser(description=desc, formatter_class=RawTextHelpFormatter)
    # Debug
    parser.add_argument("-debug", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    # List
    disp = parser.add_argument_group("list arguments")
    disp.add_argument("-l", "--list_all", 
                      help="Show all policies (Default action)", 
                      required=False, 
                      action="store_true")
    disp.add_argument("-k", "--kernels", 
                      help="Show kernel build compatibility details", 
                      required=False, 
                      action="store_true")
    disp.add_argument("-b", "--builds", 
                      help="Show available builds", 
                      required=False, 
                      action="store_true")
    disp.add_argument("-o", "--host_groups", 
                      help="Show available host groups", 
                      required=False, 
                      action="store_true")
    disp.add_argument("-m", "--maintenance",
                      help="Show maintenance or a specific uninstall token",
                      required=False,
                      action="store_true"
                      )
    disp.add_argument("-v", "--show_members", 
                      help="Show policy members in results", 
                      required=False, 
                      action="store_true")
    disp.add_argument("-z", "--show_groups",
                      help="Show host groups assigned to policies in results",
                      required=False,
                      action="store_true"
                      )
    # Search
    srch = parser.add_argument_group("search arguments")
    srch.add_argument("-q", "--search_string", 
                      help="String to match against policy or host group name", 
                      required=False)
    # Create
    crt = parser.add_argument_group("create arguments")
    crt.add_argument("-c", "--create", 
                     help="Create a new policy", 
                     required=False, action="store_true")
    # Update
    upd = parser.add_argument_group("update and delete arguments")
    upd.add_argument("-d", "--disable", 
                     help="Disable the policy", 
                     required=False, 
                     action="store_true")
    upd.add_argument("-e", "--enable", 
                     help="Enable the policy", 
                     required=False, 
                     action="store_true")
    upd.add_argument("-x", "--disable_uninstall_protection",
                     help="Disable uninstall protection for the policy",
                     required=False,
                     action="store_true"
                     )
    upd.add_argument("-u", "--enable_uninstall_protection",
                     help="Enable uninstall protection for the policy",
                     required=False,
                     action="store_true"
                     )
    upd.add_argument("-p", "--precedence",
                     help="Set policy precedence (will apply list in order received)\n"
                     "Use the policy_id argument to provide the list",
                     required=False,
                     action="store_true"
                     )
    upd.add_argument("-r", "--remove", 
                     help="Remove the policy", 
                     required=False, 
                     action="store_true")
    upd.add_argument("-g", "--add_host_group", 
                     help="Add host group to the specified policy\n(comma delimit)", 
                     required=False)
    upd.add_argument("-y", "--yank_host_group",
                     help="Remove host group from the specified policy\n(comma delimit)",
                     required=False
                     )
    # IDs and platform names for updates
    idg = parser.add_argument_group("required arguments for updating or removing policies")
    idg.add_argument("-i", "--policy_id", 
                     help="ID(s) of the policy to update or remove (comma delimit)", 
                     required=False)
    idg.add_argument("-n", "--platform_name", 
                     help="Platform name for policy precedence configurations", 
                     required=False)
    # MSSP
    msp = parser.add_argument_group("MSSP arguments")
    msp.add_argument("-w", "--member_cid", 
                     help="Child CID (MSSP access)", 
                     required=False)
    # Other
    oth = parser.add_argument_group("other arguments")
    oth.add_argument("-t", "--base_url", 
                     help="Specify the API base URL",
                     required=False)
    # Always required
    req = parser.add_argument_group("always required arguments")
    req.add_argument("-f", "--falcon_client_id",
                     help="Falcon Client ID", 
                     required=True)
    req.add_argument("-s", "--falcon_client_secret", 
                     help="Falcon Client Secret", 
                     required=True)



def process_command_line():  # pylint: disable=R0912,R0915
    """Process the consumed command line arguments."""
    args = consume_arguments()

    command_to_perform = []
    update_type = None
    flag_type = None
    if args.disable or args.enable or args.policy_id or args.enable_uninstall_protection or args.disable_uninstall_protection:
        command_to_perform.append("update")
        if args.disable:
            flag_type = "DISABLE"
        if args.enable:
            flag_type = "ENABLE"
        if args.enable_uninstall_protection:
            update_type = "ENABLE_UNINSTALL"
        if args.disable_uninstall_protection:
            update_type = "DISABLE_UNINSTALL"
        if not args.policy_id:
            raise SystemExit(ID_REQUIRED)

    if args.remove:
        command_to_perform.append("remove")
        if not args.policy_id:
            raise SystemExit(ID_REQUIRED)

    if args.kernels:
        command_to_perform.append("kernel")

    if args.builds:
        command_to_perform.append("builds")

    if args.host_groups:
        command_to_perform.append("host_groups")

    if args.create:
        command_to_perform.append("create")

    if args.maintenance:
        command_to_perform.append("maintenance")

    if args.precedence:
        command_to_perform.append("precedence")
        if not args.policy_id:
            raise SystemExit(ID_REQUIRED)
        if not args.platform_name:
            raise SystemExit("You must specify a platform name to use this function.")

    group_id = None
    if args.add_host_group:
        command_to_perform = "add_host_group"
        if not args.policy_id:
            raise SystemExit(ID_REQUIRED)
        group_id = args.add_host_group.split(",")

    if args.yank_host_group:
        command_to_perform = "del_host_group"
        if not args.policy_id:
            raise SystemExit(ID_REQUIRED)
        group_id = args.yank_host_group.split(",")

    if args.policy_id:
        args.policy_id = args.policy_id.split(",")

    hide_members = True
    if args.show_members:
        hide_members = False

    hide_groups = True
    if args.show_groups:
        hide_groups = False

    mssp_access = None
    if args.member_cid:
        mssp_access = args.member_cid
    
    base_url = "auto"
    if args.base_url:
        base_url = args.base_url
    
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    return command_to_perform, args.falcon_client_id, args.falcon_client_secret, args.search_string,\
        args.policy_id, update_type, flag_type, hide_members, args.platform_name, group_id,\
        hide_groups, mssp_access, base_url, args.debug 


def hide_members_column():
    """Show or hide the members column."""
    member_detail = []
    members = "No members found"
    lookup = falcon.query_combined_policy_members()
    if lookup["status_code"] == 200:
        for member in lookup["body"]["resources"]:
            print(f" Loading policies... {step_indicator()}", end="\r", flush="True")
            memb = f"{member.get('hostname', 'Not available')} ({member.get('local_ip', 'Not available')})\n"
            memb = f"{memb}{Color.DARKCYAN}{member['device_id']}{Color.END}"
            member_detail.append(memb)
        members = "\n".join(member_detail)

    return members


def clean_groups_column(group_list: list):
    """Clean the host groups column."""
    if group_list:
        group_detail = ""
        cnt = 0
        for polgroup in group_list:
            cnt += 1
            if 1 < cnt <= len(group_list):
                group_detail = f"{group_detail}\n"
            group_detail = f"{group_detail}{Color.BOLD}{polgroup['name']}\n{Color.DARKCYAN}{polgroup['id']}{Color.END}"
    else:
        group_detail = "None specified"

    return group_detail

def list_policies(search_string: str = None):  # pylint: disable=R0914,R0915
    """List all sensor update policies."""
    def pop_keys(incoming: dict):
        """Remove all unnecessary keys"""
        incoming.pop("id")
        incoming.pop("cid")
        incoming.pop("description")
        incoming.pop("created_by")
        incoming.pop("created_timestamp")
        incoming.pop("groups")
        incoming.pop("modified_by")
        incoming.pop("modified_timestamp")
        incoming.pop("name")
        incoming.pop("platform_name")
        incoming.pop("enabled")

        return incoming

    def get_uninst_color(incoming: str):
        """Retrieve the color for uninstall protection."""
        if incoming == "ENABLED":
            selected_color = Color.GREEN
        if incoming == "DISABLED":
            selected_color = Color.RED
        if incoming == "IGNORE":
            selected_color = Color.YELLOW

        return selected_color

    def get_version(incoming: dict):
        """Retrieve and colorize the version number."""
        ver = incoming["settings"].get("sensor_version", "Not found")
        if ver == "":
            ver = f"{Color.MAGENTA}Not set{Color.END}"
        return ver

    def calc_filter(search_val: str):
        calced_search_filter = None
        if search_val:
            calced_search_filter=f"name:*'*{search_val}*'"
        return calced_search_filter

    def get_table_headers():
        head = {
            "name" : "Name",
            "platform_name": "Platform",
            "enabled": "Enabled",
            "version": "Sensor version",
            "build": "Build",
            "uninstall": "Uninstall Protection"
            }
        if not HIDE:
            head["members"] = "Members"
        if not GROUP_HIDE:
            head["groups"] = "Groups"

        return head

    def format_build(incoming: dict):
        bld = incoming["settings"].get("build", f"{Color.MAGENTA}Not set{Color.END}")
        if bld == "":
            bld = f"{Color.MAGENTA}Not set{Color.END}"

        return bld

    print(f" Loading policies... {step_indicator()}", end="\r", flush="True")
    search_filter=calc_filter(search_string)
    policy_list = falcon.query_combined_policies_v2(filter=search_filter)
    print(f" Loading policies... {step_indicator()}", end="\r", flush="True")
    policies = policy_list["body"]["resources"]
    if not policies:
        raise SystemExit(NO_RESULTS_FOUND)
    for policy in policies:
        print(f" Loading policies... {step_indicator()}", end="\r", flush="True")
        nam = f"{Color.BOLD}{policy['name']}{Color.END}\n{Color.CYAN}{policy['id']}{Color.END}"
        if policy["description"]:
            nam = f"{nam}\n{policy['description']}"
        plat = policy["platform_name"]
        enable_color = Color.GREEN if bool(policy["enabled"]) else Color.RED
        enab = f"{enable_color}{policy['enabled']}{Color.END}"
        grou = clean_groups_column(policy["groups"])
        policy = pop_keys(policy)
        policy["name"] = nam
        policy["platform_name"] = plat
        policy["enabled"] = enab
        uninst = policy["settings"].get("uninstall_protection", "Not found")
        uninst_color = get_uninst_color(uninst)
        policy["uninstall"] = f"{uninst_color}{uninst}{Color.END}"
        policy["version"] = get_version(policy)
        policy["build"] = format_build(policy)
        policy.pop("settings")
        if not HIDE:
            policy["members"] = hide_members_column()
        print(f" Loading policies... {step_indicator()}", end="\r", flush="True")
        if not GROUP_HIDE:
            policy["groups"] = grou

    print(tabulate(policies, get_table_headers(), tablefmt="fancy_grid"))


def update_policies(id_to_update: str, update_style: str = "", flag_style: str = ""):
    """Enable or disable the policy or it's uninstallation protection."""
    keywords = {
        "id": id_to_update,
    }
    update_result = None
    if update_style in ["ENABLE_UNINSTALL", "DISABLE_UNINSTALL"]:
        if update_style == "ENABLE_UNINSTALL":
            keywords["uninstall_protection"] = "ENABLED"
        if update_style == "DISABLE_UNINSTALL":
            keywords["uninstall_protection"] = "DISABLED"
        update_result = falcon.update_policies_v2(**keywords)
    if flag_style in ["ENABLE", "DISABLE"]:
        update_result = falcon.perform_policies_action(action_name=flag_style.lower(), ids=id_to_update)
    if update_result:
        if update_result["status_code"] != 200:
            raise SystemExit(generate_api_error_list(update_result["body"]["errors"]))

# pylint: disable=E0606
def list_kernel_compatibility():
    """List all available kernels."""
    kernel_list_lookup = falcon.query_combined_kernels()
    if kernel_list_lookup["status_code"] != 200:
        raise SystemExit(generate_api_error_list(kernel_list_lookup["body"]["errors"]))
    kernel_list = kernel_list_lookup["body"]["resources"]
    if not kernel_list:
        raise SystemExit(NO_RESULTS_FOUND)

    for kernel in kernel_list:
        kernel.pop("id")
        vend = kernel["vendor"]
        distro = kernel["distro"]
        distro_ver = kernel["distro_version"]
        arch = kernel["architecture"]
        flav = kernel['flavor']
        if flav:
            flav = f" {flav}"
        vers = kernel["version"]
        rel = kernel["release"]
        base_support = "\n".join(kernel["base_package_supported_sensor_versions"])
        if kernel["ztl_supported_sensor_versions"]:
            ztl_support = "\n".join(kernel["ztl_supported_sensor_versions"])
        else:
            ztl_support = "None"
        if kernel["ztl_module_supported_sensor_versions"]:
            ztl_module = "\n".join(kernel["ztl_module_supported_sensor_versions"])
        else:
            ztl_module = "None"
        kernel.pop("vendor")
        kernel.pop("distro")
        kernel.pop("distro_version")
        kernel.pop("architecture")
        kernel.pop("flavor")
        kernel.pop("version")
        kernel.pop("release")
        kernel.pop("base_package_supported_sensor_versions")
        kernel.pop("ztl_supported_sensor_versions")
        kernel.pop("ztl_module_supported_sensor_versions")
        kernel.pop("created_timestamp")
        kernel.pop("modified_timestamp")
        det = f"{vend} {Color.BOLD}{distro}{Color.END} ({distro_ver}/{arch}{flav})\n"
        det = f"{det}Release: {Color.CYAN}{rel}{Color.END}\n{vers}"
        kernel["detail"] = det
        kernel["base"] = base_support
        kernel["ztl"] = ztl_support
        kernel["ztl_module"] = ztl_module

    headers = {
        "detail": "Kernel",
        "base": "Sensor versions",
        "ztl": "ZTL versions",
        "ztl_module": "ZTL module versions"
    }
    print(tabulate(kernel_list, headers, tablefmt="fancy_grid"))


def get_builds():
    """Retrieve the list of builds from the API."""
    build_lookup = falcon.query_combined_builds()
    if build_lookup["status_code"] != 200:
        raise SystemExit(generate_api_error_list(build_lookup["body"]["errors"]))
    build_list = build_lookup["body"]["resources"]
    return build_list


def list_builds():
    """List all available builds."""
    builds = get_builds()
    if not builds:
        raise SystemExit(NO_RESULTS_FOUND)
    headers = {
        "build": "Build",
        "platform": "Platform",
        "sensor_version": "Sensor version"
    }
    print(tabulate(builds, headers, tablefmt="fancy_grid"))


def unique_list(list_to_dedupe: list):
    """Remove duplicates from a list."""
    list_set = set(list_to_dedupe)
    return list(list_set)


def delete_policy(policy_to_delete: str):
    """Delete a sensor update policy."""
    remove_result = falcon.delete_policies(ids=policy_to_delete)
    if remove_result["status_code"] != 200:
        raise SystemExit(generate_api_error_list(remove_result["body"]["errors"]))


def get_build_response(builds: dict, avail: list):
    """Ask the user for the desired build id."""
    acceptable_build = False
    while not acceptable_build:
        print(tabulate(builds, tablefmt="fancy_grid"))
        build_to_use = input("Build for this policy (q = Quit)? ")
        if build_to_use.lower() == "q":
            raise SystemExit("Creation cancelled.")
        if build_to_use in avail:
            acceptable_build = True
        else:
            cont = input("You've entered an invalid build. Press enter to continue or 'q' to quit. ")
            if cont.lower() == "q":
                raise SystemExit("Creation cancelled.")

        return build_to_use


def get_platform_response(plats: dict, avail: list):
    """Ask the user for the desired platform."""
    acceptable_platform = False
    while not acceptable_platform:
        print(tabulate(plats, tablefmt="fancy_grid"))
        plat_to_use = input("Platform for this policy? ")
        if plat_to_use.lower() == "q":
            raise SystemExit("Creation cancelled.")
        if plat_to_use in avail:
            acceptable_platform = True
        else:
            cont = input("You've entered in invalid platform. Press enter to continue or 'q' to quit. ")
            if cont.lower() == "q":
                raise SystemExit("Creation cancelled.")

        return plat_to_use

def create_policy():
    """Create a new sensor update policy."""
    builds = get_builds()
    avail_builds = sorted(unique_list([x["build"] for x in builds]))
    avail_plats = sorted(unique_list([y["platform"] for y in builds]))
    all_platforms = []
    for platform in avail_plats:
        plat = {}
        plat["Platform"] = platform
        all_platforms.append(plat)
    all_builds = []
    for build in avail_builds:
        bld = {}
        bld["Build"] = build
        all_builds.append(bld)
    name_to_use = input("Name to use for the new policy? ")
    policy_desc = input("Description to use for this policy? ")
    build_id = get_build_response(all_builds, avail_builds)
    plat_id = get_platform_response(all_platforms, avail_plats)
    creation = falcon.create_policies_v2(platform_name=plat_id,
                                         description=policy_desc,
                                         name=name_to_use,
                                         build=build_id
                                         )
    if creation["status_code"] != 201:
        raise SystemExit(generate_api_error_list(creation["body"]["errors"]))



def show_token(id_for: str = "MAINTENANCE"):
    """Display uninstall and bulk maintenance tokens."""
    maint_token_lookup = falcon.reveal_uninstall_token(device_id=id_for)
    if maint_token_lookup["status_code"] != 200:
        raise SystemExit("Unable to retrieve maintenance tokens.")
    maint_token = maint_token_lookup["body"]["resources"][0]["uninstall_token"]
    disp_text = "Bulk maintenance token: "
    if id_for != "MAINTENANCE":
        disp_text = f"Uninstall token for {id_for}: "
    print(f"{disp_text}{Color.BOLD}{maint_token}{Color.END}")


def set_precedence(id_list: list, platform: str):
    """Set policy precedence by passing a list and a platform name."""
    update_result = falcon.set_policies_precedence(ids=id_list, platform_name=platform)
    if update_result["status_code"] != 200:
        raise SystemExit("Unable to set policy precedence.")

def change_host_group(id_to_change: str, ids_to_update: str, style: str = "add_host_group"):
    """Add or remove host groups from the policy."""
    id_list = ",".join(id_to_change)
    action_parameters = {
        "name": "group_id",
        "value": id_list    # Must be comma delimited string
    }
    action_name = None
    if style == "add_host_group":
        action_name = "add-host-group"
    if style == "del_host_group":
        action_name = "remove-host-group"

    update_result = falcon.perform_policies_action(action_name=action_name,
                                                   ids=ids_to_update,
                                                   action_parameters=[action_parameters]
                                                   )
    if update_result["status_code"] != 200:
        raise SystemExit("Unable to change host group assignments.")

def list_host_groups(search_str: str = ""):
    """List all available host groups."""
    search_filter = None
    if search_str:
        search_filter = f"name:*'*{search_str}*'"
    host_group_lookup = falcon_groups.query_combined_host_groups(filter=search_filter)
    if host_group_lookup["status_code"] != 200:
        raise SystemExit(generate_api_error_list(host_group_lookup["body"]["errors"]))
    host_groups = host_group_lookup["body"]["resources"]
    if not host_groups:
        raise SystemExit(NO_RESULTS_FOUND)
    headers = {
        "name": "Name",
        "group_type": "Group Type",
        "assignemnt_rule": "Rule"
    }
    for hgroup in host_groups:
        nam = hgroup["name"]
        nam = f"{Color.BOLD}{nam}\n{Color.DARKCYAN}{hgroup['id']}{Color.END}"
        nam = f"{nam}\n{hgroup['description']}"
        rule = hgroup.get("assignment_rule", "Not set")
        gtype = hgroup["group_type"]
        hgroup.pop("id")
        hgroup.pop("group_type")
        hgroup.pop("description")
        if rule != "Not set":
            hgroup.pop("assignment_rule")
        hgroup.pop("created_by")
        hgroup.pop("created_timestamp")
        hgroup.pop("modified_by")
        hgroup.pop("modified_timestamp")
        hgroup["name"] = nam
        hgroup["group_type"] = gtype
        hgroup["rule"] = rule

    print(tabulate(host_groups, headers, tablefmt="fancy_grid"))


NO_RESULTS_FOUND = fr"""{Color.YELLOW}
_  _ ____    ____ ____ ____ _  _ _    ___ ____
|\ | |  |    |__/ |___ [__  |  | |     |  [__
| \| |__|    |  \ |___ ___] |__| |___  |  ___]{Color.END}
"""

ID_REQUIRED = fr"""{Color.YELLOW}
_ ___     _  _ ____ ___    ___  ____ ____ _  _ _ ___  ____ ___
| |  \    |\ | |  |  |     |__] |__/ |  | |  | | |  \ |___ |  \
| |__/    | \| |__|  |     |    |  \ |__|  \/  | |__/ |___ |__/{Color.END}

You must specify a list of IDs using the '-i' argument to use this function.
"""

INVALID_VERSION = fr"""{Color.LIGHTRED}
_ _  _ _  _ ____ _    _ ___     _  _ ____ ____ ____ _ ____ _  _
| |\ | |  | |__| |    | |  \    |  | |___ |__/ [__  | |  | |\ |
| | \|  \/  |  | |___ | |__/     \/  |___ |  \ ___] | |__| | \|{Color.END}{Color.YELLOW}   ¯\_( ͡° ͜ʖ ͡°)_/¯{Color.END}

This application requires CrowdStrike FalconPy v{Color.BOLD}1.0+{Color.END}
Install it with: {Color.BOLD}python3 -m pip install crowdstrike-falconpy{Color.END}
"""

if int(FALCONPY_VERSION.split(".", maxsplit=1)[0]) < 1:
    raise SystemExit(INVALID_VERSION)

INDICATOR = ["|", "/", "-", "\\"]
INDICATOR_POSITION = 0

command, client_id, client_secret, API_SEARCH, policy_id, which_update, \
    enable_disable, HIDE, platform_name, hg_id, GROUP_HIDE, member_cid, base_url, debug = process_command_line()
falcon = connect_sensor_update_api(client_id, client_secret, member_cid, base_url, debug)
falcon_groups = connect_host_group_api(client_id, client_secret, member_cid, base_url, debug)

if "kernel" in command:
    list_kernel_compatibility()

if "builds" in command:
    list_builds()

if "host_groups" in command:
    list_host_groups(API_SEARCH)
    if API_SEARCH:
        API_SEARCH = None

if "update" in command:
    for pid in policy_id:
        update_policies(pid, which_update, enable_disable)

if "remove" in command:
    for pid in policy_id:
        delete_policy(pid)

if "create" in command:
    create_policy()

if "precedence" in command:
    set_precedence(policy_id, platform_name)

if "add_host_group" in command or "del_host_group" in command:
    change_host_group(hg_id, policy_id, command)

if "maintenance" in command:
    if policy_id:
        for pid in policy_id:
            show_token(pid)
    else:
        show_token()


list_policies(API_SEARCH)
