r"""Retrieve the contents of a scheduled report and save it to a file.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |      FalconPy SDK
`-------'                         `-------'

 _______        __             __         __           __
|     __|.----.|  |--.-----.--|  |.--.--.|  |.-----.--|  |
|__     ||  __||     |  -__|  _  ||  |  ||  ||  -__|  _  |
|_______||____||__|__|_____|_____||_____||__||_____|_____|

             ______                          __
            |   __ \.-----.-----.-----.----.|  |_.-----.
            |      <|  -__|  _  |  _  |   _||   _|__ --|
            |___|__||_____|   __|_____|__|  |____|_____|
                          |__|

____ ____ ____ _  _ _    ___ ____    ___  ____ _ _ _ _  _ _    ____ ____ ___  ____ ____
|__/ |___ [__  |  | |     |  [__     |  \ |  | | | | |\ | |    |  | |__| |  \ |___ |__/
|  \ |___ ___] |__| |___  |  ___]    |__/ |__| |_|_| | \| |___ |__| |  | |__/ |___ |  \

Accepts a Scheduled Report ID and downloads every successful execution result.

Files are saved as [REPORT ID]_[EXECUTION ID].rpt in JSON format.

Requires the Report Executions: READ scope

Creation date: 10.26.22 - jshcodes@CrowdStrike
"""

import json
from argparse import ArgumentParser, RawTextHelpFormatter
from falconpy import ReportExecutions


def consume_arguments():
    """Consume our required command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    required = parser.add_argument_group("required_arguments")
    required.add_argument("-k", "--falcon_client_id",
                        help="CrowdStrike API Client ID",
                        required=True
                        )
    required.add_argument("-s", "--falcon_client_secret",
                        help="CrowdStrike API Client Secret",
                        required=True
                        )
    required.add_argument("-r", "--report", help="ID of the report to retrieve", required=True)
    return parser.parse_args()


def retrieve_report_executions(sdk: ReportExecutions, rptid: str):
    """Retrieve the list of execution IDs that match this report ID."""
    print(f"🔍 Searching for executions of {rptid}")
    execution_id_lookup = sdk.reports_executions_query(filter=f"scheduled_report_id:'{rptid}'")
    if not execution_id_lookup["status_code"] == 200:
        raise SystemExit("⛔ Unable to retrieve report executions from "
                         "the CrowdStrike API, check API key permissions."
                         )

    # Give the SDK back so we can feed our results to the next method easily
    return sdk, execution_id_lookup["body"]["resources"]


def get_report_execution_runs(sdk: ReportExecutions, id_list: list):
    """Retrieve the list of execution runs for each execution ID."""
    print(f"✅ Found {len(id_list)} executions of this report available.")
    # Retrieve the status of these IDs
    exec_status_lookup = sdk.report_executions_get(id_list)
    if not exec_status_lookup["status_code"] == 200:
        raise SystemExit("⛔ Unable to retrieve execution statuses from the CrowdStrike API.")
    print(f"⚠️  This execution has run {len(exec_status_lookup['body']['resources'])} times.")

    # Give the SDK back as well so we can easily feed it to our next method call
    return sdk, exec_status_lookup["body"]["resources"]


def process_executions(sdk: ReportExecutions, run_list: list):
    """Process the results of the executions, this solution only handles completed runs."""
    saved = 0
    for exec_status in run_list:
        status = exec_status["status"]
        exec_id = exec_status["id"]
        rpt_id = exec_status["scheduled_report_id"]
        if status.upper() == "DONE":
            report_detail = sdk.get_download(exec_id)
            if report_detail:
                if isinstance(report_detail, dict):
                    try:
                        with open(f"{rpt_id}_{exec_id}.rpt", "w", encoding="utf-8") as json_output:
                            json.dump(report_detail, json_output)
                        saved += 1
                        print(f"📥 {exec_id} successfully saved to {rpt_id}_{exec_id}.rpt")
                    except json.JSONDecodeError:
                        print(f"❗ Unable to decode results of report run {exec_id} for ")
                else:
                    with open(f"{rpt_id}_{exec_id}.rpt", "wb") as csv_output:
                        csv_output.write(report_detail)
                    saved += 1
            else:
                print(f"⛔ Unable to retrieve report for execution {exec_id} of {rpt_id}.")
        else:
            print(f"⏩ Skipping {exec_id} as not yet finished.")
    # Return back the number of successful saves
    return saved


if __name__ == "__main__":
    # Consume any provided command line arguments
    cmdline = consume_arguments()
    # Create an instance of the ReportExecutions Service Class
    falcon = ReportExecutions(client_id=cmdline.falcon_client_id,
                              client_secret=cmdline.falcon_client_secret
                              )
    # Retrieve our report executions, and process them, saving any that
    # have completed successfully to individual files (JSON format).
    # Let's be fancy and leverage list expansion to provide arguments from
    # one method to the subsequent one. It's like inception for Python. ♜
    SUCCESSFUL = process_executions(
        *get_report_execution_runs(*retrieve_report_executions(falcon, cmdline.report))
        )
    # Inform the user of the result
    print(f"🏁 Retrieval complete, {SUCCESSFUL} report results were downloaded.")
