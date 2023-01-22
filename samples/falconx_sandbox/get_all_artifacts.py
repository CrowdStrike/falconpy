# pylint: disable=W1401
"""Retrieve all artifacts from all available Falcon X reports.

 _______       __
|   _   .---.-|  .----.-----.-----.
|.  1___|  _  |  |  __|  _  |     |
|.  __) |___._|__|____|_____|__|__|
|:  |
|::.|
`---'
 ___       __         __ __ __
|   .-----|  |_.-----|  |  |__.-----.-----.-----.----.-----.
|.  |     |   _|  -__|  |  |  |  _  |  -__|     |  __|  -__|
|.  |__|__|____|_____|__|__|__|___  |_____|__|__|____|_____|
|:  |                         |_____|
|::.|
`---'                               CrowdStrike FalconPy


Creation date: 01.12.2021 - jshcodes@CrowdStrike

You will need the following scopes on your API keys:
    Falcon Intelligence Sandbox: READ, WRITE
"""
import os
import json
import argparse
from falconpy import FalconXSandbox


def parse_command_line() -> object:
    """Parse the command line for inbound configuration parameters."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
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
        help='CrowdStrike API region (us1, us2, eu1, usgov1)'
        ' NOT required unless you are using `usgov1`',
        required=False
    )

    return parser.parse_args()


def get_artifact_list() -> list:
    """Create a list of artifacts to be downloaded."""
    formats = ["csv", "json", "stix", "maec"]
    types = ["broad", "strict"]
    artifacts_to_retrieve = []
    # Get a list of available reports
    reports = sandbox.query_reports()   # Use the filter parameter to prune this initial list
    if "resources" not in reports["body"]:
        raise SystemExit("Unable to access Falcon Intelligence reports, check permissions.")
    if not reports["body"]["resources"]:
        raise SystemExit("No reports found.")

    for report_id in reports["body"]["resources"]:
        print(f"Checking report {report_id} for artifacts.")
        # Retrieve report details for this report
        report_details = sandbox.get_reports(ids=report_id)
        # Retrieve a list of artifacts found within the report
        # Only return artifacts matching our formats / types specified above
        for key, val in report_details["body"]["resources"][0].items():
            for format_ in formats:
                for type_ in types:
                    check = f"{type_}_{format_}_artifact_id"
                    if check in key:
                        artifacts_to_retrieve.append([val, format_, type_, report_id])

    return artifacts_to_retrieve


def retrieve_all_artifacts():
    """Retrieve all artifacts found within the list of artifacts returned."""
    download_message = "No artifacts found within any reports reviewed."
    # Loop thru all artifacts selected for download and download them according to format
    for artifact in get_artifact_list():
        if not os.path.exists(artifact[3]):
            os.mkdir(artifact[3])
        content = sandbox.get_artifacts(id=artifact[0])
        save_filename = f"{artifact[3]}/{artifact[1]}_{artifact[2]}_{artifact[0]}"
        if isinstance(content, dict):
            with open(save_filename, "w", encoding="utf-8") as save_file:
                if isinstance(content["body"], list):
                    # JSON format
                    json.dump(content["body"], save_file)
                else:
                    if "objects" in content["body"]:
                        # STIX format
                        json.dump(content["body"]["objects"], save_file)
                    if "observable_objects" in content["body"]:
                        # MAEC format
                        json.dump(content["body"]["observable_objects"], save_file)
        else:
            # CSV format
            with open(save_filename, "wb") as save_file:
                save_file.write(content)

        print(f"Downloaded {artifact[1].upper()} format ({artifact[2]}) to {save_filename}")
        download_message = "Downloads complete."

    print(download_message)


args = parse_command_line()
if not args.base_url:
    BASE = "us1"
else:
    BASE = args.base_url

sandbox = FalconXSandbox(client_id=args.client_id,
                         client_secret=args.client_secret,
                         base_url=BASE
                         )

retrieve_all_artifacts()
