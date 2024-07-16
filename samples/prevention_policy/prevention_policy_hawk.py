r"""CrowdStrike Falcon Prevention Policy Maintenance utility.

CrowdStrike's
 _______                              __   __
|   _   .----.-----.--.--.-----.-----|  |_|__.-----.-----.
|.  1   |   _|  -__|  |  |  -__|     |   _|  |  _  |     |
|.  ____|__| |_____|\___/|_____|__|__|____|__|_____|__|__|
|:  |
|::.|             _______       __ __
`---'            |   _   .-----|  |__.----.--.--.               .  .
                 |.  1   |  _  |  |  |  __|  |  |            .  .  .  .
                 |.  ____|_____|__|__|____|___  |            .  |  |  .
                 |:  |                    |_____|         .  |        |  .
                 |::.|                                    .              .
                 `---'      ___     ___    _________    . |  (\.|\/|./)  | .   ___   ____
                           |   |   |   |  /    _    \   .   (\ |||||| /)   .  |   | /   /
                           |   |___|   | |    /_\    |  |  (\  |/  \|  /)  |  |   |/   /
                           |           | |           |    (\   |    |   /)    |       /
                           |    ___    | |    ___    |   (\   / \  / \   /)   |       \
                           |   |   |   | |   |   |   |    \              /    |   |\   \
                           |___|   |___| |___|   |___|     \____/\/\____/     |___| \___\
                                                               |0\/0|
                                                                \/\/          FalconPy v1.4.4
                                                                 \/

Creation date: 2022.02.11           Modification: 2022.05.11
    jhseceng@CrowdStrike                jshcodes@CrowdStrike
    jshcodes@CrowdStrike


Leverages the FalconPy API SDK to update prevention policies within CrowdStrike Falcon.

This solution requires the FalconPy SDK. This project
can be accessed here: https://github.com/CrowdStrike/falconpy
"""
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
from enum import Enum
from tabulate import tabulate
try:
    from falconpy import PreventionPolicy
except ImportError as no_falconpy:
    raise SystemExit(
        "The crowdstrike-falconpy package must be installed to use this program."
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
    GRAY = "\033[90m"
    LIGHTGRAY = "\033[37m"
    LIGHTYELLOW = "\033[93m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    LIGHTRED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
    DIM = "\033[2m"


class SensitivityColor(Enum):
    """Enum to represent the colors for each sensitivity setting."""

    DISABLED = Color.GRAY
    CAUTIOUS = Color.CYAN
    MODERATE = Color.YELLOW
    AGGRESSIVE = Color.LIGHTRED
    EXTRA_AGGRESSIVE = Color.RED


def shiny_description(incoming):
    """Shine up the description so it's purty."""
    incoming = f"{Color.CYAN}{incoming}"
    incoming = incoming.replace(
                    "CrowdStrike's",
                    f"{Color.LIGHTRED}CrowdStrike{Color.END}'s{Color.DARKCYAN}"
                    )
    incoming = incoming.replace("    `---'", f"    {Color.END}{Color.CYAN}`---'{Color.END}")
    incoming = incoming.replace("|. ", f"{Color.END}{Color.CYAN}|. ")
    incoming = incoming.replace("|:  |", f"{Color.CYAN}|:  |")
    incoming = incoming.replace("|::.|", f"{Color.CYAN}|::.|")
    incoming = incoming.replace(r"(\.", fr"{Color.END}{Color.RED}(\.")
    incoming = incoming.replace(r"(\ ", fr"{Color.END}{Color.RED}(\ ")
    incoming = incoming.replace(
                    "                           |",
                    f"{Color.RED}                           |"
                    )
    incoming = incoming.replace(
                    ".  |        |  .",
                    f".  {Color.LIGHTYELLOW}|        |{Color.END}{Color.BOLD}  .{Color.END}"
                    )
    incoming = incoming.replace(
                    ".  |  |  .",
                    f".  {Color.LIGHTYELLOW}|  |{Color.END}{Color.BOLD}  .{Color.END}"
                    )
    incoming = incoming.replace(" . ", f" {Color.END}{Color.BOLD}. ")
    incoming = incoming.replace(")  |", f")  {Color.LIGHTYELLOW}|{Color.END}")
    incoming = incoming.replace("|  (", f"{Color.LIGHTYELLOW}|{Color.END}  (")
    incoming = incoming.replace("___     ___ ", f"{Color.RED}___     ___ ")
    incoming = incoming.replace(r"       \/\/", fr"       {Color.RED}\/\/{Color.END}")
    incoming = incoming.replace(
                    "FalconPy v1.0",
                    f"{Color.END}{Color.BOLD}{Color.LIGHTRED}Falcon"
                    f"{Color.LIGHTYELLOW}Py {Color.LIGHTGRAY}v1.0{Color.END}"
                    )
    incoming = incoming.replace(r"        \/", fr"        {Color.RED}\/{Color.END}")
    incoming = incoming.replace("|  .", f"|  {Color.BOLD}.{Color.END}")
    incoming = incoming.replace("___   ____", f"{Color.END}{Color.RED}___   ____")
    incoming = incoming.replace("|   | /   /", f"{Color.END}{Color.RED}|   | /   /")
    incoming = incoming.replace("|   |/   /", f"{Color.END}{Color.RED}|   |/   /")
    incoming = incoming.replace(
                    r"/_\    |  |",
                    fr"/_\    |  {Color.LIGHTYELLOW}{Color.BOLD}|{Color.END}{Color.RED}"
                    )
    incoming = incoming.replace(
                    f"/)  {Color.LIGHTYELLOW}|{Color.END}",
                    f"/)  {Color.BOLD}{Color.LIGHTYELLOW}|"
                    )
    incoming = incoming.replace(
                    f"{Color.BOLD}. |",
                    f"{Color.BOLD}. {Color.LIGHTYELLOW}|{Color.END}"
                    )
    incoming = incoming.replace(
                    r"|0\/0|",
                    fr"|{Color.PURPLE}0{Color.RED}\/{Color.PURPLE}0{Color.RED}|"
                    )
    incoming = incoming.replace(
                    "jhseceng@CrowdStrike",
                    f"{Color.YELLOW}jhseceng{Color.END}@{Color.RED}CrowdStrike{Color.END}"
                    )
    incoming = incoming.replace(
                    "jshcodes@CrowdStrike",
                    f"{Color.GREEN}jshcodes{Color.END}@{Color.RED}CrowdStrike{Color.END}"
                    )
    incoming = incoming.replace(
                    "Creation date:",
                    f"{Color.UNDERLINE}Creation date:{Color.END}{Color.UNDERLINE}"
                    )
    incoming = incoming.replace(
                    "Modification:",
                    f"{Color.UNDERLINE}Modification:{Color.END}{Color.UNDERLINE}"
                    )
    incoming = incoming.replace(".11", f".11{Color.END}")
    return incoming


def do_fail(errors_received: list):
    """Parse the error list and display the result."""
    for err in errors_received:
        emsg = err["message"]
        ecode = err["code"]
        print(f"[{Color.RED}{ecode}{Color.END}] {Color.YELLOW}{emsg}{Color.END}")


def get_policy_payload(settings_to_change: list,
                       set_to_value: bool,
                       sensitivity: str = "Moderate",
                       scope: str = "both"
                       ):
    """Create a properly formatting prevention policy setting payload."""
    def get_sensitivity(sense_value):
        returned = False
        for sens in AVAILABLE_SENSITIVITIES:
            if sens.upper() == sense_value.upper():
                returned = sense_value.upper()
        if not returned:
            raise SystemExit("Invalid sensitivity option.")
        return returned

    def set_branch_value(inval, scp, working):
        if scp in ["detection", "both"]:
            working["value"]["detection"] = inval
        if scp in ["prevention", "both"]:
            working["value"]["prevention"] = inval

        return working

    policy_settings = []
    for setting in settings_to_change:  # pylint: disable=R1702
        for setting_type in AVAILABLE_SETTINGS:
            if setting.lower() == setting_type.lower():
                pol_set = {}
                pol_set["id"] = setting_type
                pol_set["value"] = {}
                if setting_type in ["CloudAntiMalware", "OnSensorMLSlider", "AdwarePUP"]:
                    set_value = None
                    if "," in sensitivity:
                        sensitivity = sensitivity.split(",")
                        pol_set = set_branch_value(sensitivity[0], "detection", pol_set)
                        pol_set = set_branch_value(sensitivity[1], "prevention", pol_set)
                    else:
                        set_value = get_sensitivity(sensitivity)
                        pol_set = set_branch_value(set_value, scope, pol_set)
                        set_value = True
                else:
                    pol_set["value"]["enabled"] = set_to_value

                policy_settings.append(pol_set)

    return policy_settings


def query_policy(search_str: str = None):
    """Register the users listed in our data file by UID."""
    filter_str = None
    if search_str:
        filter_str = f"name:*'*{search_str}*'"
    # Call the API to update the requested account.
    response = falcon_policy.query_combined_policies(filter=filter_str)
    returned = False
    if response["status_code"] == 200:
        returned = response['body']['resources']
    else:
        do_fail(response["body"]["errors"])

    if not returned:
        raise SystemExit(NO_RESULTS)

    return returned


def get_updated_policy_detail(pol_id: str = None):
    """Requery for the latest policy data."""
    if pol_id:
        response = falcon_policy.get_policies(ids=pol_id)
        if response["status_code"] == 200:
            returned = response["body"]["resources"]
        else:
            do_fail(response["body"]["errors"])

    return returned


def get_policy_id(policy_search: str):
    """Search for a Prevention Policy ID by using a partial name."""
    returned = False
    search_result = falcon_policy.query_policies(filter=f"name:*'{policy_search}*'")
    if search_result["status_code"] == 200:
        if search_result["body"]["resources"]:
            returned = search_result["body"]["resources"][0]  # Return the first match only
        else:
            print(f"Unable to find policy ID matching search string: {policy_search}")
    else:
        do_fail(search_result["body"]["errors"])

    return returned


# pylint: disable=R0912,R0914,R0915     ಥ﹏ಥ
def print_prevention_policy_data(policies: list,
                                 display_settings: bool = False,
                                 quietly: bool = False
                                 ):
    """List the details of the prevention policy."""
    policies_detail = []
    headers = {}
    if len(policies) == 1:
        display_settings = True
    # if not display_settings:
    #     headers["select"] = "Select"
    headers["id"] = f"{Color.BOLD}Policy{Color.END}"
    headers["platform"] = f"{Color.BOLD}Platform{Color.END}"
    headers["enabled"] = f"{Color.BOLD}Enabled{Color.END}"
    if display_settings:
        headers["settings"] = f"{Color.BOLD}Policy configuration{Color.END}"
    # cnt = 0
    for policy in policies:  # pylint: disable=R1702
        # cnt += 1
        id_display = [
                Color.BOLD,
                policy["name"],
                Color.END,
                "\n",
                Color.LIGHTBLUE,
                policy["id"],
                Color.END,
                "\n",
                policy["description"]
                ]
        policy_detail = {}
        # if not display_settings:
        #     policy_detail["select"] = cnt
        policy_detail["id"] = "".join(id_display)
        policy_detail["platform"] = policy["platform_name"]
        enable = policy["enabled"]
        enable_color = Color.LIGHTGRAY
        if bool(enable):
            enable_color = Color.GREEN
        enable = f"{enable_color}{enable}{Color.END}"
        policy_detail["enabled"] = enable
        if display_settings:
            settings = policy["prevention_settings"]
            set_list = []
            for setting in settings:
                set_name = setting["name"]
                header_shown = False
                for subset in setting["settings"]:
                    nam = f"{subset['name']} [{Color.DARKCYAN}{subset['id']}{Color.END}]"
                    typ = subset["type"]
                    val = ""
                    if typ == "toggle":
                        val_set = subset["value"]["enabled"]
                        val = f"{Color.GRAY}Disabled{Color.END}"
                        if val_set:
                            val = f"{Color.GREEN}Enabled{Color.END}"
                    else:
                        cnt = 0
                        stub = ""
                        for ml_key, ml_val in subset["value"].items():
                            if cnt:
                                stub = ", "
                            cnt += 1
                            slide_color = SensitivityColor[ml_val.upper()].value
                            vals = [
                                f"{val}{stub}{ml_key.title()}",
                                " is ",
                                f"{slide_color}{ml_val.lower().replace('_', ' ')}{Color.END}"
                                ]
                            val = "".join(vals)
                            val_set = bool(ml_val != "DISABLED")

                    if not header_shown and val_set or (not quietly and not header_shown):
                        set_list.append(f"\n{Color.UNDERLINE}{Color.BOLD}{set_name}{Color.END}")
                        header_shown = True

                    result = f"{nam} ({val})"
                    if not quietly or val_set:
                        set_list.append(result)

            policy_detail["settings"] = "\n".join(set_list)

        policies_detail.append(policy_detail)

    heading = TABLE_HEADER
    if not display_settings:
        heading = SHORT_HEADER
    print(heading)
    print(tabulate(policies_detail, headers, tablefmt="fancy_grid"))


def consume_command_line():
    """Consume the arguments provided by the command line and return the argument parser."""
    parser = ArgumentParser(description=shiny_description(__doc__),
                            formatter_class=RawTextHelpFormatter
                            )
    parser.add_argument("-debug", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    # Display
    view = parser.add_argument_group("optional display arguments")
    view.add_argument("-r", "--show_settings",
                      help="Display policy settings",
                      action="store_true",
                      required=False,
                      default=False
                      )
    view.add_argument("-z", "--verbose",
                      help="Show all settings, including disabled",
                      action="store_true",
                      required=False,
                      default=False
                      )
    # Mgmt
    mgmt = parser.add_argument_group("optional management arguments")
    mgmt.add_argument("-e", "--enable",
                      help="Enable the policy",
                      action="store_true",
                      required=False
                      )
    mgmt.add_argument("-d", "--disable",
                      help="Disable the policy",
                      action="store_true",
                      required=False
                      )
    mgmt.add_argument("-x", "--delete",
                      help="Delete the policy",
                      action="store_true",
                      required=False
                      )

    # Update
    upd = parser.add_argument_group("optional update arguments")
    upd.add_argument("-i", "--policy_id",
                     help="ID of a policy to update",
                     required=False
                     )
    upd.add_argument("-p", "--policy_search_string",
                     help="String to match against policy name",
                     required=False
                     )
    upd.add_argument("-t", "--policy_setting",
                     help="Policy settings to modify (Comma delimit)",
                     required=False
                     )
    upd.add_argument("-v", "--policy_setting_value",
                     help="Enabled / Disable the setting (True / False)",
                     required=False
                     )
    upd.add_argument("-m", "--policy_sensitivity",
                     help="Sensitivity setting for slider policies.\n"
                     "(Disabled, Cautious, Moderate, Aggressive, Extra_Aggressive)\n"
                     "Case-insensitive, comma delimited strings accepted (detection,prevention)",
                     required=False
                     )
    upd.add_argument("-o", "--scope",
                     help="Sensitivity scope (detection / prevention / both).",
                     required=False
                     )
    # Always required
    req = parser.add_argument_group("required arguments")
    req.add_argument("-f", "--falcon_client_id", 
                     help="Falcon Client ID", 
                     required=True)
    req.add_argument("-s", "--falcon_client_secret", 
                     help="Falcon Client Secret", 
                     required=True)

    parsed = parser.parse_args()
    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)
    

    return parsed

def do_policy_delete(pol_id: str = None):
    """Delete the policy using the provided ID."""
    if pol_id:
        resp = falcon_policy.delete_policies(ids=pol_id)
        if resp["status_code"] != 200:
            do_fail(resp["body"]["errors"])


def show_policies(pol_search: str = None, display_settings: bool = False, be_silent: bool = False):
    """Show the policies listing."""
    print_prevention_policy_data(query_policy(pol_search), display_settings, be_silent)


def determine_arguments(arg_list: ArgumentParser):  # pylint: disable=R0912
    """Review the contents of the argument parser and create necessary variables."""
    cmd = "query"
    pol_search_string = arg_list.policy_search_string
    pol_setting = None
    if arg_list.policy_setting:
        pol_setting = arg_list.policy_setting.split(",")
        cmd = "update"
    pol_sensitivity = "DISABLED"
    if arg_list.policy_sensitivity:
        pol_sensitivity = arg_list.policy_sensitivity
    pol_setting_value = False
    if arg_list.policy_setting_value is not None:
        if "t" in arg_list.policy_setting_value.lower():
            pol_setting_value = True
        if "f" in arg_list.policy_setting_value.lower():
            pol_setting_value = False
        if arg_list.policy_setting_value.lower() == "enable":
            pol_setting_value = True
        if arg_list.policy_setting_value.lower() == "disable":
            pol_setting_value = False
    slide_scope = "both"
    if arg_list.scope:
        if arg_list.scope.lower() in ["detection", "prevention", "both"]:
            slide_scope = arg_list.scope.lower()

    activating = None
    if arg_list.disable or arg_list.enable:
        cmd = "enable_disable"
        if arg_list.disable:
            activating = "disable"
        if arg_list.enable:
            activating = "enable"

    if arg_list.delete:
        cmd = "delete"

    if arg_list.delete or arg_list.disable or arg_list.enable:
        if not arg_list.policy_id and not pol_search_string:
            raise SystemExit(
                "Policy ID (-i) or Search String (-p) are required to perform this operation"
                )

    qmode = True
    if arg_list.verbose:
        qmode = False

    pol_id = None
    if arg_list.policy_id:
        pol_id = arg_list.policy_id

    return cmd, pol_search_string, pol_setting, pol_sensitivity, pol_setting_value, \
        activating, slide_scope, pol_id, arg_list.show_settings, qmode


def do_update(pol_id, settings_payload):
    """Perform an update."""
    resp = falcon_policy.update_policies(id=pol_id, settings=settings_payload)
    if resp["status_code"] != 200:
        do_fail(resp["body"]["errors"])


def do_action(pol_id, action):
    """Enable or disable a policy."""
    resp = falcon_policy.perform_policies_action(ids=pol_id, action_name=action)
    if resp["status_code"] != 200:
        do_fail(resp["body"]["errors"])


def find_pol_id(pol_id, pol_search):
    """Find our policy ID."""
    returned = False
    if not pol_id:
        if pol_search:
            returned = get_policy_id(policy_search=pol_search)
    else:
        returned = pol_id

    return returned


# pylint: disable=R0913
def process_arguments(command,
                      policy_search_string,
                      policy_setting,
                      policy_sensitivity,
                      policy_setting_value,
                      activate,
                      slider_scope,
                      policy_id,
                      show_settings,
                      quiet_mode
                      ):
    """Execute the requests."""
    if command.lower() == "query":
        if not quiet_mode:
            show_settings = True
        show_policies(policy_search_string, show_settings, quiet_mode)
    elif command.lower() == "update":
        policy_id = find_pol_id(policy_id, policy_search_string)
        if policy_id:
            policy_payload = get_policy_payload(policy_setting,
                                                set_to_value=policy_setting_value,
                                                sensitivity=policy_sensitivity,
                                                scope=slider_scope
                                                )
            do_update(policy_id, policy_payload)
        print_prevention_policy_data(get_updated_policy_detail(policy_id),
                                     show_settings,
                                     quiet_mode
                                     )
    elif command.lower() == "enable_disable":
        policy_id = find_pol_id(policy_id, policy_search_string)
        if activate:
            do_action(policy_id, activate)
        print_prevention_policy_data(
            get_updated_policy_detail(policy_id),
            show_settings,
            quiet_mode
            )
    elif command.lower() == "delete":
        policy_id = find_pol_id(policy_id, policy_search_string)
        do_policy_delete(policy_id)
        print_prevention_policy_data(policy_search_string, show_settings, quiet_mode)
    else:
        print(f"{command} is not a valid command.")


TABLE_HEADER = fr"""{Color.MAGENTA}
  ___  ____ ____ _  _ ____ _  _ ___ _ ____ _  _    ___  ____ _    _ ____ _ ____ ____
  |__] |__/ |___ |  | |___ |\ |  |  | |  | |\ |    |__] |  | |    | |    | |___ [__
  |    |  \ |___  \/  |___ | \|  |  | |__| | \|    |    |__| |___ | |___ | |___ ___]{Color.END}
"""

SHORT_HEADER = fr"""{Color.MAGENTA}
  ___  ____ ____ _  _ ____ _  _ ___ _ ____ _  _
  |__] |__/ |___ |  | |___ |\ |  |  | |  | |\ |
  |    |  \ |___  \/  |___ | \|  |  | |__| | \|

                             ___  ____ _    _ ____ _ ____ ____
                             |__] |  | |    | |    | |___ [__
                             |    |__| |___ | |___ | |___ ___]{Color.END}
"""
NO_RESULTS = fr"""{Color.YELLOW}
_  _ ____    ____ ____ ____ _  _ _    ___ ____
|\ | |  |    |__/ |___ [__  |  | |     |  [__
| \| |__|    |  \ |___ ___] |__| |___  |  ___]{Color.END}
"""

AVAILABLE_SETTINGS = [
    "UnknownDetectionRelatedExecutables", "UnknownExecutables", "ScriptBasedExecutionMonitoring",
    "CloudAntiMalware", "OnSensorMLSlider", "CustomBlacklisting", "PreventSuspiciousProcesses",
    "DetectOnWrite", "QuarantineOnWrite", "EndUserNotifications", "InterpreterOnly",
    "UnknownDetectionRelatedExecutables", "SensorTamperingProtection", "AdditionalUserModeData",
    "EngineProtectionV2", "HTTPDetections", "RedactHTTPDetectionDetails", "FileEncryption",
    "HardwareEnhancedExploitDetection", "FirmwareAnalysisExtraction", "FileSystemAccess", "Locky",
    "WindowsLogonBypassStickyKeys", "CredentialDumping", "AutomatedRemediation", "ForceDEP",
    "JavascriptViaRundll32", "ProcessHollowing", "DriveByDownload", "ChopperWebshell",
    "ApplicationExploitationActivity", "VolumeShadowCopyProtect", "VolumeShadowCopyAudit",
    "Cryptowall", "BackupDeletion", "SEHOverwriteProtection", "NullPageAllocation", "ForceASLR",
    "HeapSprayPreallocation", "SuspiciousKernelDrivers", "IntelPrevention", "MaliciousPowershell",
    "SuspiciousRegistryOperations", "NextGenAV", "AdwarePUP", "InterpreterProtection"
    ]

AVAILABLE_SENSITIVITIES = ["Disabled", "Cautious", "Moderate", "Aggressive", "Extra_Aggressive"]

if __name__ == "__main__":
    # Retrieve any provided command line arguments
    args = consume_command_line()

    # Authenticate using our provided falcon client_id and client_secret and debugging if activated
    falcon_policy = PreventionPolicy(client_id=args.falcon_client_id,
                                     client_secret=args.falcon_client_secret, 
                                     debug=args.debug
                                     )

    # Review the provided arguments and then perform the request
    process_arguments(*determine_arguments(args))

    # Discard our token on our way out the door
    falcon_policy.auth_object.revoke(falcon_policy.token)
