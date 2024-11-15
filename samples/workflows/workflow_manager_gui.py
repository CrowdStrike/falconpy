"""Falcon Fusion SOAR workflow manager.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy 1.4.1+
`-------'                         `-------'

 ██       ██                 ██       ████  ██
░██      ░██                ░██      ░██░  ░██
░██   █  ░██  ██████  ██████░██  ██ ██████ ░██  ██████  ███     ██
░██  ███ ░██ ██░░░░██░░██░░█░██ ██ ░░░██░  ░██ ██░░░░██░░██  █ ░██
░██ ██░██░██░██   ░██ ░██ ░ ░████    ░██   ░██░██   ░██ ░██ ███░██
░████ ░░████░██   ░██ ░██   ░██░██   ░██   ░██░██   ░██ ░████░████
░██░   ░░░██░░██████ ░███   ░██░░██  ░██   ███░░██████  ███░ ░░░██
░░       ░░  ░░░░░░  ░░░    ░░  ░░   ░░   ░░░  ░░░░░░  ░░░    ░░░
 ████     ████
░██░██   ██░██                               █████
░██░░██ ██ ░██  ██████   ███████   ██████   ██░░░██  █████  ██████
░██ ░░███  ░██ ░░░░░░██ ░░██░░░██ ░░░░░░██ ░██  ░██ ██░░░██░░██░░█
░██  ░░█   ░██  ███████  ░██  ░██  ███████ ░░██████░███████ ░██ ░
░██   ░    ░██ ██░░░░██  ░██  ░██ ██░░░░██  ░░░░░██░██░░░░  ░██
░██        ░██░░████████ ███  ░██░░████████  █████ ░░██████░███
░░         ░░  ░░░░░░░░ ░░░   ░░  ░░░░░░░░  ░░░░░   ░░░░░░ ░░░

This sample demonstrates how to leverage the Workflows API to provide
the following functionality:
  - List all workflows
    - Results can be exported to CSV
  - Execute a workflow
  - List all executions for a workflow
    - Results can be exported to CSV
  - Print the results of a workflow execution
  - Import a workflow
  - Export a workflow
  - Optional logging of results to a file

This version leverages the Gooey project to implement a simple GUI, command line
arguments are supported but not required to specify execution configuration.

Creation date: 11.06.2024 - Initial version, jlangdev@CrowdStrike
Modification date: 11.08.2024 - Refactoring, jshcodes@CrowdStrike
Modification date: 11.10.2024 - Add graphical interface, jshcodes@CrowdStrike

This sample requires the following packages:
- crowdstrike-falconpy >= 1.4.1
- darkdetect
- gooey
- requests
- tabulate
"""
import csv
import os
import sys
import logging
from argparse import RawTextHelpFormatter, Namespace, ArgumentError
from json import dumps, dump, loads
from os import getenv
from typing import List, Union
import requests
import darkdetect
from tabulate import tabulate
from gooey import Gooey, GooeyParser
from falconpy import Workflows, Result, APIError


MENU = [
    {
        "type": "AboutDialog",
        "menuTitle": "About",
        "name": "Falcon Fusion SOAR Workflow Manager",
        "description": "\n\n\nA graphical application for managing Falcon Fusion SOAR workflows\n"
                       "\n                   Built using the CrowdStrike FalconPy project",
        "version": "0.1",
        "copyright": "2024",
        "website": "https://github.com/crowdstrike/falconpy"
    }, {
        "type": "Link",
        "menuTitle": "Falcon Fusion SOAR API documentation",
        "url": "https://www.falconpy.io/Service-Collections/Workflows.html"
    }, {
        "type": "Link",
        "menuTitle": "Falcon Fusion SOAR console documentation",
        "url": "https://falcon.crowdstrike.com/documentation/page/dc4f8c45/workflows-falcon-fusion"
    }, {
        "type": "Link",
        "menuTitle": "CrowdStrike Developer Center",
        "url": "https://developer.crowdstrike.com"
    }, {
        "type": "Link",
        "menuTitle": "More FalconPy code samples",
        "url": "https://github.com/crowdstrike/falconpy/tree/main/samples#falconpy-sample-library"
    }
]
DARK_MODE = darkdetect.isDark()


def get_font_size() -> int:
    """Return the specified font point size for terminal output.

    Specify this value as the first argument (integer) when executing the application.
    """
    returned = None
    try:
        if "-" not in sys.argv[1]:
            returned = int(sys.argv[1])
            # Pop it out of the list so it doesn't
            # interfere with argument parsing
            sys.argv.pop(1)
    except (IndexError, ValueError):
        pass

    return returned


def check_for_autostart() -> bool:
    """Check to see if the command line specifies automatic execution."""
    returned = False
    try:
        if "-" not in sys.argv[1]:
            if sys.argv[1].lower() in ["run", "go", "exec", "force"]:
                returned = True
                sys.argv.pop(1)
    except (IndexError, ValueError):
        pass

    return returned


def get_image_dir():
    """Identify the current program image directory."""
    returned = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(f"{returned}/asset/program_icon.png"):
        returned = f"{returned}/asset"

    return returned


def gui_image(img: str, local_img: str):
    """Retrieve GUI program images from GitHub before launching the interface."""
    curpath = os.path.dirname(os.path.abspath(__file__))
    loc_array = ["https://raw.githubusercontent.com/CrowdStrike/",
                 "falconpy/refs/heads/main/samples/workflows/asset/"
                 ]
    loc = "".join(loc_array)
    if not max(os.path.exists(f"{curpath}/{local_img}"),
               os.path.exists(f"{curpath}/asset/{local_img}")
               ):
        try:
            result = requests.get(f"{loc}{img}", timeout=5)
            if result.status_code == 200:
                img_data = result.content
                with open(f"{curpath}/{local_img}", "wb") as gui_icon:
                    gui_icon.write(img_data)
        except (requests.exceptions.Timeout, PermissionError, OSError):
            pass


def prefill_check(what: str = "ID") -> str:
    """Detect if environment authentication is in use and inform the user."""
    returned = f"CrowdStrike Falcon API {what}"
    if getenv(f"FALCON_CLIENT_{what.upper()}"):
        returned = f"{returned}\n(pre-filled from environment or command line)"

    return returned


def attempt_to_prefill_workflow_ids() -> Union[List[str], None]:
    """Attempt to lookup workflow names and IDs before the GUI loads.

    This functionality only works when environment authentication is in use, or valid
    credentials are provided on the command line using the -k and -s arguments.
    """
    returned: List[str] = []
    tmp_id = getenv("FALCON_CLIENT_ID")
    tmp_sec = getenv("FALCON_CLIENT_SECRET")
    tmp_base = "auto"
    tmp_debug = False
    cnt = 0
    for arg in sys.argv:
        if arg in ["-k", "--client_id"]:
            tmp_id = sys.argv[cnt+1]
        if arg in ["-s", "--client_secret"]:
            tmp_sec = sys.argv[cnt+1]
        if arg in ["-b", "--base_url"]:
            tmp_base = sys.argv[cnt+1]
        if arg in ["-d", "--debug"]:
            tmp_debug = True
        if arg in ["-g", "--get_result", "--skip_preflight", "-sk", "-h"]:
            tmp_id = None
            returned = None
            break
        cnt += 1
    if min(bool(tmp_id), bool(tmp_sec)):
        with Workflows(client_id=tmp_id,
                       client_secret=tmp_sec,
                       base_url=tmp_base,
                       debug=tmp_debug,
                       pythonic=True
                       ) as flows:
            try:
                for flow in flows.search_definitions().data:
                    returned.append(f"{flow.get('id')} ({flow.get('name')})")
            except APIError:
                pass

    return returned


def check_action() -> int:
    """Check to see if a default action was specified on the command line."""
    returned = 0
    arglist = {
        "-l": 0,
        "--list_workflows": 0,
        "-e": 1,
        "--execute": 1,
        "-le": 2,
        "--list-executions": 2,
        "-g": 3,
        "--get_result": 3
    }
    try:
        for arg in sys.argv:
            returned = arglist.get(arg, returned)
    except (IndexError, ValueError):
        pass
    return returned


def check_for_json_format() -> int:
    """Check to see if JSON formatted output was specified."""
    returned = 1
    try:
        if "-j" in sys.argv:
            returned = 0
    except (IndexError, ValueError):
        pass

    return returned


def mode_label() -> str:
    """Return the appropriate label HEX code for our current color mode."""
    returned = "#000000"
    if DARK_MODE:
        returned = "#aaaaaa"

    return returned


def mode_background() -> str:
    """Return the appropriate background HEX code for our current color mode."""
    returned = "#ffffff"
    if DARK_MODE:
        returned = "#141414"

    return returned


@Gooey(advanced=True,
       program_name="Falcon Fusion SOAR Workflow Manager",
       program_description="List, execute, review and manage Fusion workflows.",
       default_size=(1100, 610),
       terminal_font_family='Courier New',
       terminal_font_size=get_font_size(),
       auto_start=check_for_autostart(),
       show_stop_warning=False,
       show_success_modal=False,
       show_restart_button=False,
       use_cmd_args=True,
       tabbed_groups=True,
       image_dir=get_image_dir(),
       menu=[{"name": "Help", "items": MENU}],
       header_bg_color=mode_background(),
       body_bg_color=mode_background(),
       footer_bg_color=mode_background(),
       terminal_font_color=mode_label(),
       sidebar_bg_color=mode_background(),
       terminal_panel_color=mode_background()
       )
def consume_arguments() -> Namespace:  # pylint: disable=R0915
    """Consume the provided command line."""
    parser = GooeyParser(description=__doc__,
                         formatter_class=RawTextHelpFormatter,
                         exit_on_error=False
                         )
    cmds = parser.add_argument_group("Command",
                                     description="Workflow command to perform",
                                     gooey_options={"label_color": mode_label(),
                                                    "help_color": mode_label()
                                                    }
                                     )
    excl = cmds.add_mutually_exclusive_group("Action",
                                             gooey_options={"initial_selection": check_action(),
                                                            "label_color": mode_label(),
                                                            "help_color": mode_label()
                                                            }
                                             )
    excl.add_argument("-l", "--list_workflows",
                      help="List all workflows",
                      required=False,
                      action="store_true",
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    excl.add_argument("-e", "--execute",
                      help="Execute the workflow specified on the Workflow tab",
                      required=False,
                      action="store_true",
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    excl.add_argument("-le", "--list_executions",
                      help="List the executions for the workflow specified",
                      required=False,
                      action="store_true",
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    excl.add_argument("-g", "--get_result",
                      help="Retrieve a workflow execution result",
                      required=False,
                      action="store_true",
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    excl.add_argument("-ex", "--workflow_export",
                      help="Export a workflow",
                      required=False,
                      action="store_true",
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    excl.add_argument("-im", "--workflow_import",
                      help="Import a workflow",
                      required=False,
                      action="store_true",
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    wflow = parser.add_argument_group("Workflow",
                                      description="Workflow or execution ID and workflow payload",
                                      gooey_options={"columns": 1,
                                                     "label_color": mode_label(),
                                                     "help_color": mode_label()
                                                     }
                                      )
    wflow.add_argument("-i", "--id",
                       help="Workflow definition ID",
                       required=False,
                       choices=attempt_to_prefill_workflow_ids(),
                       gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                       )
    wflow.add_argument("-ei", "--execution_id",
                       help="Workflow execution ID",
                       required=False,
                       gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                       )
    wflow.add_argument("-p", "--payload",
                       help="Workflow execution payload",
                       required=False,
                       default='{\n    "key": "value"\n}',
                       widget="Textarea",
                       gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                       )
    imp = parser.add_argument_group("Import",
                                    description="Import a workflow from a file",
                                    gooey_options={"label_color": mode_label(),
                                                   "help_color": mode_label()
                                                   }
                                    )
    imp.add_argument("-n", "--workflow_name",
                     help="Name for the imported workflow",
                     required=False,
                     gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                     )
    imp.add_argument("-v", "--validate_only",
                     dest="validate",
                     help="Validate the workflow only, do not save upon import",
                     required=False,
                     default=False,
                     widget="BlockCheckbox",
                     action="store_true",
                     gooey_options={"checkbox_label": " Validate only",
                                    "label_color": mode_label(),
                                    "help_color": mode_label()
                                    }
                     )
    imp.add_argument("-iw", "--import_workflow",
                     help="Location of the YAML workflow file to import",
                     required=False,
                     widget="FileChooser",
                     gooey_options={"default_dir": os.path.dirname(os.path.abspath(__file__)),
                                    "wildcard": "YAML files (*.yml)|*.yml",
                                    "message": "Select YAML file",
                                    "label_color": mode_label(), "help_color": mode_label()
                                    }
                     )
    exp = parser.add_argument_group("Export",
                                    description="Export a workflow to a file",
                                    gooey_options={"label_color": mode_label(),
                                                   "help_color": mode_label()
                                                   }
                                    )
    exp.add_argument("-ew", "--export_workflow",
                     help="Location to save the exported workflow (YAML format)\n"
                          "Use the Workflow tab to specify the desired workflow ID",
                     required=False,
                     widget="FileSaver",
                     gooey_options={"default_dir": os.path.dirname(os.path.abspath(__file__)),
                                    "default_file": "exported.yml", "message": "Specify YAML file",
                                    "label_color": mode_label(), "help_color": mode_label()
                                    }
                     )
    auth = parser.add_argument_group("Environment",
                                     description="Authentication and program execution options",
                                     gooey_options={"columns": 3,
                                                    "label_color": mode_label(),
                                                    "help_color": mode_label()
                                                    }
                                     )
    auth.add_argument("-k", "--client_id",
                      help=prefill_check(),
                      required=False,
                      default=getenv("FALCON_CLIENT_ID"),
                      widget="PasswordField",
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    auth.add_argument("-s", "--client_secret",
                      help=prefill_check("secret"),
                      required=False,
                      default=getenv("FALCON_CLIENT_SECRET"),
                      widget="PasswordField",
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    auth.add_argument("-b", "--base_url",
                      help="CrowdStrike Region\n('auto' not implemented for usgov1 or usgov2)",
                      required=False,
                      default="auto",
                      choices=["auto", "us1", "us2", "eu1", "usgov1", "usgov2"],
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    auth.add_argument("-lf", "--logfile",
                      help="Log output results to a local file as well as the console",
                      required=False,
                      widget="FileSaver",
                      gooey_options={"default_dir": os.path.dirname(os.path.abspath(__file__)),
                                     "default_file": "workflow-manager.log",
                                     "message": "Specify log file",
                                     "label_color": mode_label(), "help_color": mode_label()
                                     }
                      )
    auth.add_argument("-d", "--debug",
                      help=" Activate API debugging",
                      action="store_true",
                      required=False,
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )

    auth.add_argument("-o", "--compress_output",
                      help=" Compress display output",
                      action="store_true",
                      default=False,
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    auth.add_argument("-sk", "--skip_preflight",
                      help=" Skip preflight API lookups",
                      default=False,
                      action="store_true",
                      gooey_options={"visible": False}
                      )
    frmt = auth.add_mutually_exclusive_group("Format",
                                             gooey_options={
                                                 "initial_selection": check_for_json_format(),
                                                 "show_border": False,
                                                 "show_underline": True,
                                                 "label_color": mode_label(),
                                                 "help_color": mode_label()
                                                 }
                                             )
    frmt.add_argument("-j", "--json",
                      help="Display execution results in JSON format",
                      required=False,
                      action="store_true",
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )
    frmt.add_argument("-t", "--table_format",
                      help="Tabular display format\n"
                           "Selecting CSV format will output to a file and display a table "
                           "to the console using simple format",
                      required=False,
                      default="simple",
                      choices=["plain", "simple", "github", "grid", "simple_grid", "rounded_grid",
                               "heavy_grid", "mixed_grid", "double_grid", "fancy_grid", "outline",
                               "simple_outline", "rounded_outline", "heavy_outline",
                               "mixed_outline", "double_outline", "fancy_outline", "pipe", "csv",
                               "orgtbl", "asciidoc", "jira", "presto", "pretty", "psql", "rst",
                               "mediawiki", "moinmoin", "youtrack", "html", "unsafehtml", "latex",
                               "latex_raw", "latex_booktabs", "latex_longtable", "textile", "tsv"
                               ],
                      gooey_options={"label_color": mode_label(), "help_color": mode_label()}
                      )

    arglist = sys.argv
    for arg in arglist:
        if arg in ["-h", "--help"]:
            parser.print_help()
            sys.exit(0)

    hold_id = None
    try:
        parsed = parser.parse_args()
    except ArgumentError as bad_arg:
        if "invalid choice" in bad_arg.message:
            cnt = 0
            arglist = sys.argv
            for arg in arglist:
                if arg in ["-i", "--id"]:
                    hold_id = sys.argv[cnt+1]
                    sys.argv.pop(cnt+1)
                    sys.argv.pop(cnt)
                cnt += 1
        else:
            raise bad_arg
    finally:
        parsed = parser.parse_args()
        if hold_id:
            parsed.id = hold_id

    return parsed


def get_workflows(sdk: Workflows):
    """Print a list of workflows within the tenant to the screen."""
    workflow_list = []
    pop_keys = ["trigger", "actions", "description", "conditions", "loops"]
    for workflow in sdk.search_definitions().data:
        pop_list = [k for k in pop_keys if k in workflow]
        workflow["type"] = "Unknown"
        if "conditions" in workflow:
            workflow["type"] = "Event"
        if "trigger" in workflow:
            if "schedule" in workflow["trigger"]:
                workflow["type"] = "Scheduled"
            if "event" not in workflow["trigger"]:
                workflow["type"] = "On demand"
        for key in pop_list:
            workflow.pop(key)
        workflow_list.append(workflow)

    return workflow_list


def get_executions(sdk: Workflows, definition_id: str):
    """Retrieve all executions for the specified workflow."""
    execution_list = []
    pop_keys = ["definition_id", "definition_version", "ancestor_executions",
                "retryable", "trigger", "activities", "loops"
                ]
    if definition_id in [w["id"] for w in get_workflows(sdk)]:
        for execution in sdk.search_executions(filter=f"definition_id:'{definition_id}'").data:
            pop_list = [k for k in pop_keys if k in execution]
            for key in pop_list:
                execution.pop(key)
            execution_list.append(execution)
    else:
        print("Invalid workflow ID")

    return execution_list


def log_write(logging_file: str, json_mode: bool, log_text: str):
    """Perform the log action."""
    with open(logging_file, "a", encoding="utf-8") as logfile:
        logfile.write("\n")
        if json_mode:
            dump(log_text, logfile, indent=4)
        else:
            logfile.write(log_text)


def display_executions(sdk: Workflows,
                       tformat: str,
                       use_json: bool,
                       log: str,
                       definition_id: str = None
                       ):
    """Display the execution list to the terminal."""
    if not definition_id:
        print("Invalid workflow ID specified.")
        return
    exec_list = get_executions(sdk, definition_id=definition_id.split(" ", maxsplit=1)[0])
    if exec_list:
        if use_json:
            if log:
                log_write(log, use_json, exec_list)
            print(dumps(exec_list, indent=4))
        else:
            display_keys = {"execution_id": "ID",
                            "status": "Status",
                            "start_timestamp": "Start",
                            "end_timestamp": "End"
                            }
            if log:
                log_write(log, use_json, f"{EXECUTION_HEADER}\n"
                          f"{tabulate(exec_list, headers=display_keys, tablefmt=tformat)}"
                          )
            if tformat.lower() == "csv":
                output_file = "workflow_executions.csv"
                with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=display_keys.keys())
                    writer.writeheader()
                    writer.writerows(exec_list)
                print(f"Tabular results shown below have been output to {output_file}")
                tformat = "simple"
            print(EXECUTION_HEADER)
            print(tabulate(exec_list, headers=display_keys, tablefmt=tformat))
    else:
        print("No executions found.")


def display_workflows(sdk: Workflows, tformat: str, use_json: bool, log: str):
    """Display the workflow list to the terminal."""
    workflow_list = get_workflows(sdk)
    if workflow_list:
        if use_json:
            if log:
                log_write(log, use_json, workflow_list)
            print(dumps(workflow_list, indent=4))
        else:
            display_keys = {"id": "ID",
                            "name": "Name",
                            "enabled": "Enabled",
                            "type": "Type",
                            "last_modified_timestamp": "Last modified",
                            "version": "Version"
                            }
            if log:
                log_write(log, use_json, f"{WORKFLOW_HEADER}\n"
                          f"{tabulate(workflow_list, headers=display_keys, tablefmt=tformat)}"
                          )
            if tformat.lower() == "csv":
                output_file = "workflows.csv"
                with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=display_keys.keys())
                    writer.writeheader()
                    writer.writerows(workflow_list)
                print(f"Tabular results shown below have been output to {output_file}")
                tformat = "simple"
            print(WORKFLOW_HEADER)
            print(tabulate(workflow_list,
                           headers=display_keys,
                           tablefmt=tformat
                           ))
    else:
        print("No workflows found.")


def fix_quotes(inbound: str):
    """Format the payload string and remove disallowed characters."""
    returned = inbound.replace('‘', '"').replace('’', '"').replace('“', '"').replace('”', '"')
    return loads(returned)


def execute_workflow(sdk: Workflows, payload: str, log: str, definition_id: str = None):
    """Execute the specified workflow."""
    def inform(msg: str):
        """Display and log the output."""
        if log:
            log_write(log, False, msg)
        print(msg)

    if not definition_id:
        print("Invalid workflow ID specified.")
        return

    definition_id = definition_id.split(" ", maxsplit=1)[0]
    inform(f"Attempting to execute workflow {definition_id}")
    if definition_id in [w["id"] for w in get_workflows(sdk)]:
        try:
            result: Result = sdk.execute(definition_id=definition_id, body=fix_quotes(payload))
            if result.status_code == 200:
                inform(f"Workflow execution {result.data} triggered successfully")
            else:
                for err in result.errors:
                    inform(f"[{err['code']}] {err['message']}")
        except APIError as failure:
            output = failure.message
            if log:
                log_write(log, False, output)
            print(output)

    else:
        inform("Invalid workflow ID specified.")


def display_execution_results(sdk: Workflows, execution_id: str, use_json: bool, log: str):
    """Display the results for the specified execution."""
    if not execution_id:
        print("Invalid execution ID specified.")
        return
    print(RESULT_HEADER)
    try:
        for result in sdk.execution_results(ids=execution_id).data:
            for activity in result.get("activities"):
                output = activity.get("result")
                if log:
                    log_write(log, use_json, output if use_json else str(output))
                if use_json:
                    output = dumps(output, indent=4)
                print(output)
    except APIError as err:
        print(err)


def export_workflow(sdk: Workflows, definition_id: str, filename: str):
    """Export the specified workflow to a YAML file."""
    if not definition_id:
        print("You must specify a workflow definition ID to export.")
    else:
        definition_id = definition_id.split(" ", maxsplit=1)[0]
        print(EXPORT_HEADER)
        print(f"Exporting workflow {definition_id} to {filename}...\n")
        try:
            with open(filename, "wb") as export_file:
                export_file.write(sdk.export_definition(id=definition_id).data)
        except APIError as err:
            print(err)


def import_workflow(sdk: Workflows, name: str, filename: str, validate_only: bool):
    """Import the specified YAML file as a workflow."""
    print(IMPORT_HEADER)
    stub = "Validat" if validate_only else "Import"
    nam = "a new workflow" if not name else name
    print(f"{stub}ing {filename} as {nam}...\n")
    try:
        response: Result = sdk.import_definition(name=name,
                                                 data_file=filename,
                                                 validate_only=validate_only
                                                 )
        if response.status_code == 200:
            if validate_only:
                print("Workflow import passes validation.")
            else:
                print(f"Workflow imported successfully [{response.data[0].get('id')}].")
    except APIError as err:
        print(err)


def main():
    """Execute the main routine."""
    cmd_line = consume_arguments()
    _debug = False
    if cmd_line.debug:
        # Activate debug logging
        logging.basicConfig(level=logging.DEBUG)
        _debug = True
    # Check for a specified action, if not present, set the default to list all workflows
    if not max(cmd_line.execute,
               cmd_line.list_workflows,
               cmd_line.list_executions,
               cmd_line.get_result,
               cmd_line.workflow_export,
               cmd_line.workflow_import
               ):
        cmd_line.list_workflows = True
    # Open the Service Collection as a context manager so we log out automatically
    with Workflows(debug=_debug,
                   pythonic=True,
                   client_id=cmd_line.client_id,
                   client_secret=cmd_line.client_secret,
                   base_url=cmd_line.base_url
                   ) as workflows:

        if not workflows.token_valid:
            print(LOGIN_FAIL)
            return

        if cmd_line.execute:
            execute_workflow(workflows, cmd_line.payload, cmd_line.logfile, cmd_line.id)

        if cmd_line.list_executions:
            display_executions(workflows,
                               cmd_line.table_format,
                               cmd_line.json,
                               cmd_line.logfile,
                               cmd_line.id
                               )

        if cmd_line.list_workflows:
            display_workflows(workflows,
                              cmd_line.table_format,
                              cmd_line.json,
                              cmd_line.logfile
                              )

        if cmd_line.get_result:
            display_execution_results(workflows,
                                      cmd_line.execution_id,
                                      cmd_line.json,
                                      cmd_line.logfile
                                      )

        if cmd_line.workflow_export:
            export_workflow(workflows, cmd_line.id, cmd_line.export_workflow)

        if cmd_line.workflow_import:
            import_workflow(workflows,
                            cmd_line.workflow_name,
                            cmd_line.import_workflow,
                            cmd_line.validate
                            )
        if not cmd_line.compress_output:
            # Divide multiple execution results in the console display with a horizontal rule
            print(f"\n{'_' * 120}\n")


WORKFLOW_HEADER = r"""
_ _ _ ____ ____ _  _ ____ _    ____ _ _ _ ____
| | | |  | |__/ |_/  |___ |    |  | | | | [__
|_|_| |__| |  \ | \_ |    |___ |__| |_|_| ___]
"""

EXECUTION_HEADER = r"""
_ _ _ ____ ____ _  _ ____ _    ____ _ _ _    ____ _  _ ____ ____ _  _ ___ _ ____ _  _ ____
| | | |  | |__/ |_/  |___ |    |  | | | |    |___  \/  |___ |    |  |  |  | |  | |\ | [__
|_|_| |__| |  \ | \_ |    |___ |__| |_|_|    |___ _/\_ |___ |___ |__|  |  | |__| | \| ___]
"""

RESULT_HEADER = r"""
____ _  _ ____ ____ _  _ ___ _ ____ _  _    ____ ____ ____ _  _ _    ___ ____
|___  \/  |___ |    |  |  |  | |  | |\ |    |__/ |___ [__  |  | |     |  [__
|___ _/\_ |___ |___ |__|  |  | |__| | \|    |  \ |___ ___] |__| |___  |  ___]
"""

IMPORT_HEADER = r"""
_ _  _ ___  ____ ____ ___
| |\/| |__] |  | |__/  |
| |  | |    |__| |  \  |
"""

EXPORT_HEADER = r"""
____ _  _ ___  ____ ____ ___
|___  \/  |__] |  | |__/  |
|___ _/\_ |    |__| |  \  |
"""

LOGIN_FAIL = r"""

   _\\/|(/_
   >_   _ /
   (_)-(_)
    ) o (
    \ = /     Invalid CrowdStrike API credentials or region specified.
     |W|
     | |
   __| |__
  / \ u / \
 |   `-'   |
 |__|   |__|
  |||ADM|||
  |||   |||
  |||   |||
"""


if __name__ == "__main__":
    gui_image("program_icon.png", "program_icon.png")
    gui_image("running_icon.png", "running_icon.png")
    gui_image("config_icon.png", "config_icon.png")
    main()
