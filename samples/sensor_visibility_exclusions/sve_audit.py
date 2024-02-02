#!/usr/bin/env python3
"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

   ▄▄▄▄▄   ▄███▄      ▄      ▄▄▄▄▄   ████▄ █▄▄▄▄
  █     ▀▄ █▀   ▀      █    █     ▀▄ █   █ █  ▄▀
▄  ▀▀▀▀▄   ██▄▄    ██   █ ▄  ▀▀▀▀▄   █   █ █▀▀▌
 ▀▄▄▄▄▀    █▄   ▄▀ █ █  █  ▀▄▄▄▄▀    ▀████ █  █
           ▀███▀   █  █ █                    █
                   █   ██                   ▀

    ▄   ▄█    ▄▄▄▄▄   ▄█ ███   ▄█ █    ▄█    ▄▄▄▄▀ ▀▄    ▄
     █  ██   █     ▀▄ ██ █  █  ██ █    ██ ▀▀▀ █      █  █
█     █ ██ ▄  ▀▀▀▀▄   ██ █ ▀ ▄ ██ █    ██     █       ▀█
 █    █ ▐█  ▀▄▄▄▄▀    ▐█ █  ▄▀ ▐█ ███▄ ▐█    █        █
  █  █   ▐             ▐ ███    ▐     ▀ ▐   ▀       ▄▀
   █▐
   ▐
            ▄▄▄          █           ▀
            █▄▄ ▀▄▀ █▀▀  █  █ █ █▀▀  █  █▀█ █▀█ █▀▀
            █▄▄ ▄▀▄ █▄▄  █▄ █▄█ ▄▄█  █  █▄█ █ █ ▄▄█

This script outputs the list of active sensor visibility exclusions
and their details for either the current CID or for a specific / each
Child CID (Flight Control scenarios). This can be useful for regular
audits of sensor visibility exclusions across multiple CIDs.

Developed by @Don-Swanson-Adobe
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import APIHarnessV2, APIError


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-m", "--mssp",
                        help="List exclusions in all child CIDs (MSSP parents only)",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-c", "--child",
                        help="List exclusions in a specific child CID (MSSP parents only)",
                        default=None
                        )
    parser.add_argument("-o", "--output_file",
                        help="File to output results to",
                        default="sensor_visibility_audit.txt"
                        )
    req = parser.add_argument_group("Required arguments")
    req.add_argument("-k", "--client_id",
                     help="CrowdStrike Falcon API key",
                     default=os.getenv("FALCON_CLIENT_ID")
                     )
    req.add_argument("-s", "--client_secret",
                     help="CrowdStrike Falcon API secret",
                     default=os.getenv("FALCON_CLIENT_SECRET")
                     )
    parsed = parser.parse_args()
    if not parsed.client_id or not parsed.client_secret:
        parser.error("You must provide CrowdStrike API credentials using the '-k' and '-s' arguments.")

    return parsed


# Consume any command line arguments
cmd_line = consume_arguments()

# Activate debugging if requested
if cmd_line.debug:
    logging.basicConfig(level=logging.DEBUG)

# Create our base authentication dictionary (parent / child)
auth = {
    "client_id": cmd_line.client_id,
    "client_secret": cmd_line.client_secret,
    "debug": cmd_line.debug,
    "pythonic": True
}
local = APIHarnessV2(**auth)
# If we are in MSSP mode, retrieve our child CID details
if cmd_line.mssp:
    try:
        cids = local.command("getChildren", ids=local.command("queryChildren").data)
    except APIError as api_erorr:
        # Assume they do not have access to Flight Control
        raise SystemExit("This API client does not have access to the Flight Control API scope.")
    if not cids:
        raise SystemExit("No child CIDs were found within this tenant.")
elif cmd_line.child:
    try:
        cid_name = local.command("getChildren", ids=cmd_line.child)
    except APIError as api_error:
        # Throw an error if they provided us an invalid CID or do not have access to Flight Control
        if api_error.code == 403:
            raise SystemExit("This API client does not have access to the Flight Control API scope.")
        elif api_error.code == 400:
            raise SystemExit("Invalid child CID provided.")
        else:
            raise SystemExit(api_error.message)
    if cid_name:
        cids = [{"name": cid_name[0]["name"], "child_cid": cmd_line.child}]
    else:
        raise SystemExit("The provided child CID was not found within this tenant.")
else:
    # If not, we'll just run this in our current tenant
    try:
        cid_id = local.command("GetSensorInstallersCCIDByQuery").data[0][:-3].lower()
    except APIError as api_error:
        # They do not have access to the sensor downloads service collection with this key
        cid_id = f"Sensor Download scope required  "
    cids = [{"name": "My CrowdStrike tenant",
            "child_cid": cid_id
            }]

# Open the output file using a context manager so it autocloses
with open(cmd_line.output_file, 'a+') as file_object:
    for cid in cids:
        if cmd_line.mssp or cmd_line.child:
            # Authenticate to the child if necessary
            auth["member_cid"] = cid["child_cid"]
        spot = 38 - len(cid["name"])
        header = f"\n\n{'*¯'*20}*\n* "+cid["name"]
        header = f"{header}{' '*spot}*\n* CID: "+cid["child_cid"]+f" *\n{'*¯'*20}*\n"
        print(header)
        file_object.write(header)
        # Connect to the API using a context manager so we autologout
        with APIHarnessV2(**auth) as falcon:
            # Query for the list of SVEs in the CID, pull the details and display / log the results
            response = falcon.command("querySensorVisibilityExclusionsV1")
            if response:
                sveresponse = falcon.command("getSensorVisibilityExclusionsV1", ids=response.data)
                for detail in sveresponse.data:
                    details = [
                        "Sensor Visibility Exclusion: " + detail.get("value"),
                        "Creator: " + detail.get("created_by"),
                        "Created on: " + detail.get("created_on"),
                        "Last Modified by: " + detail.get("modified_by"),
                        "Last Modified on: " + detail.get("last_modified")
                    ]
                    print("\n".join(details))
                    file_object.write("\n".join(details)+"\n")
            else:
                print("No exclusions found")
                file_object.write("No exclusions found\n")
