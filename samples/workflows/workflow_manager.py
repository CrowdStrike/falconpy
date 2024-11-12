"""Falcon Fusion SOAR workflow manager.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
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
  - List all workflows                            (-l or --list-workflows)
  - Execute a workflow                            (-e or --execute)
  - List all executions for a workflow            (-le or --list-executions)
  - Print the results of a workflow execution     (-g or --get_result)
  - Import a workflow                             (-im {FILENAME} or --import-workflow {FILENAME})
  - Export a workflow                             (-ex {FILENAME} or --export-workflow {FILENAME})

Creation date: 11.06.2024 - jlangdev@CrowdStrike
Modification date: 11.08.2024 - jshcodes@CrowdStrike

This sample requires the following packages:
- crowdstrike-falconpy >= 1.4.1
- tabulate
- termcolor
"""
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from json import dumps, loads
from os import getenv
from tabulate import tabulate
from termcolor import colored
from falconpy import Workflows, Result, APIError


def consume_arguments() -> Namespace:
    """Consume the provided command line."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Activate API debugging",
                        action="store_true",
                        required=False
                        )
    wflow = parser.add_argument_group("workflow arguments")
    wflow.add_argument("-i", "--id",
                       help="Workflow definition or execution ID",
                       required=False
                       )
    wflow.add_argument("-p", "--payload",
                       help="Workflow execution payload",
                       required=False,
                       default="{}"
                       )
    cmds = parser.add_argument_group("command arguments")
    cmds.add_argument("-e", "--execute",
                      help="Execute the workflow specified",
                      required=False,
                      action="store_true"
                      )
    cmds.add_argument("-g", "--get-result",
                      dest="get_result",
                      help="Retrieve a workflow execution result",
                      required=False,
                      action="store_true"
                      )
    cmds.add_argument("-l", "--list-workflows",
                      dest="list_workflows",
                      help="List all workflows",
                      required=False,
                      action="store_true"
                      )
    cmds.add_argument("-le", "--list-executions",
                      dest="list_executions",
                      help="List the executions for the workflow specified",
                      required=False,
                      action="store_true"
                      )
    cmds.add_argument("-ex", "--export-workflow",
                      dest="export_workflow",
                      help="Export a workflow to a local file.\n"
                           "Provide a filename for this argument. Example: 'exported.yml'",
                      required=False
                      )
    cmds.add_argument("-im", "--import-workflow",
                      dest="import_workflow",
                      help="Import a workflow from a local file.\n"
                           "Provide a filename for this argument. Example: 'to_import.yml'",
                      required=False
                      )
    cmds.add_argument("-n", "--workflow-name",
                      help="Name for the imported workflow",
                      required=False
                      )
    cmds.add_argument("-v", "--validate-only",
                      dest="validate",
                      help="Validate the workflow only, do not save upon import",
                      required=False,
                      default=False,
                      action="store_true"
                      )
    frmt = parser.add_argument_group("formatting arguments")
    frmt.add_argument("-j", "--json",
                      help="Display execution results in JSON format",
                      required=False,
                      action="store_true"
                      )
    frmt.add_argument("-t", "--table-format",
                      dest="table_format",
                      help="Tabular display format",
                      required=False,
                      default="simple"
                      )
    auth = parser.add_argument_group("authentication arguments "
                                     "(environment authentication supported)"
                                     )
    auth.add_argument("-k", "--falcon-client-id",
                      dest="client_id",
                      help="CrowdStrike Falcon API ID",
                      required=False,
                      default=getenv("FALCON_CLIENT_ID")
                      )
    auth.add_argument("-s", "--falcon-client-secret",
                      dest="client_secret",
                      help="CrowdStrike Falcon API secret",
                      required=False,
                      default=getenv("FALCON_CLIENT_SECRET")
                      )
    auth.add_argument("-b", "--base-url",
                      dest="base_url",
                      help="CrowdStrike Region (US1, US2, EU1, USGOV1, USGOV2) \n"
                           "Full URL is also supported.",
                      required=False,
                      default="auto"
                      )

    return parser.parse_args()


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


def display_executions(sdk: Workflows, definition_id: str, tformat: str, use_json: bool):
    """Display the execution list to the terminal."""
    exec_list = get_executions(sdk, definition_id=definition_id)
    if exec_list:
        if use_json:
            print(dumps(exec_list, indent=4))
        else:
            display_keys = {"execution_id": "ID",
                            "status": "Status",
                            "start_timestamp": "Start",
                            "end_timestamp": "End"
                            }
            print(colored(EXECUTION_HEADER, "red", attrs=["bold"]))
            print(tabulate(exec_list, headers=display_keys, tablefmt=tformat))
    else:
        print("No executions found.")


def display_workflows(sdk: Workflows, tformat: str, use_json: bool):
    """Display the workflow list to the terminal."""
    workflow_list = get_workflows(sdk)
    if workflow_list:
        if use_json:
            print(dumps(workflow_list, indent=4))
        else:
            display_keys = {"id": "ID",
                            "name": "Name",
                            "enabled": "Enabled",
                            "type": "Type",
                            "last_modified_timestamp": "Last modified",
                            "version": "Version"
                            }
            print(colored(WORKFLOW_HEADER, "red", attrs=["bold"]))
            print(tabulate(workflow_list,
                           headers=display_keys,
                           tablefmt=tformat
                           ))
    else:
        print("No workflows found.")


def execute_workflow(sdk: Workflows, definition_id: str, payload: str):
    """Execute the specified workflow."""
    print(f"Attempting to execute workflow {definition_id}")
    if definition_id in [w["id"] for w in get_workflows(sdk)]:
        try:
            result: Result = sdk.execute(definition_id=definition_id, body=loads(payload))
            if result.status_code == 200:
                print(f"Workflow execution {result.data} triggered successfully")
            else:
                for err in result.errors:
                    print(f"[{err['code']}] {err['message']}")
        except APIError as failure:
            print(failure)
    else:
        print("Invalid workflow ID.")


def display_execution_results(sdk: Workflows, definition_id: str, use_json: bool):
    """Display the results for the specified execution."""
    print(colored(RESULT_HEADER, "red", attrs=["bold"]))
    try:
        for result in sdk.execution_results(ids=definition_id).data:
            for activity in result.get("activities"):
                output = activity.get("result")
                if use_json:
                    output = dumps(output, indent=4)
                print(output)
    except APIError as err:
        print(err)


def export_workflow(sdk: Workflows, definition_id: str, filename: str):
    """Export the specified workflow to a YAML file."""
    print(colored(EXPORT_HEADER, "red", attrs=["bold"]))
    print(f"Exporting workflow {definition_id} to {filename}...\n")
    try:
        with open(filename, "wb") as export_file:
            export_file.write(sdk.export_definition(id=definition_id).data)
    except APIError as err:
        print(err)


def import_workflow(sdk: Workflows, name: str, filename: str, validate_only: bool):
    """Import the specified YAML file as a workflow."""
    print(colored(IMPORT_HEADER, "red", attrs=["bold"]))
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
               bool(cmd_line.export_workflow),
               bool(cmd_line.import_workflow)
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
            # Invalid login, show an error and then exit
            fail_msg = colored("Invalid CrowdStrike API credentials or region specified.",
                               "red",
                               attrs=["bold"]
                               )
            print(LOGIN_FAIL.format(fail_msg))
            return

        if cmd_line.execute:
            execute_workflow(workflows, cmd_line.id, cmd_line.payload)

        if cmd_line.list_executions:
            display_executions(workflows, cmd_line.id, cmd_line.table_format, cmd_line.json)

        if cmd_line.list_workflows:
            display_workflows(workflows, cmd_line.table_format, cmd_line.json)

        if cmd_line.get_result:
            display_execution_results(workflows, cmd_line.id, cmd_line.json)

        if cmd_line.export_workflow:
            export_workflow(workflows, cmd_line.id, cmd_line.export_workflow)

        if cmd_line.import_workflow:
            import_workflow(workflows,
                            cmd_line.workflow_name,
                            cmd_line.import_workflow,
                            cmd_line.validate
                            )


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
    \ = /     {}
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
    main()
