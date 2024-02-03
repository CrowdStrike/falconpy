#!/usr/bin/env python3
r"""User lookup utility.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

            (`-').->(`-')  _   (`-')  (`-').->
     .->    ( OO)_  ( OO).-/<-.(OO )  ( OO)_
,--.(,--.  (_)--\_)(,------.,------,)(_)--\_)
|  | |(`-')/    _ / |  .---'|   /`. '/    _ /
|  | |(OO )\_..`--.(|  '--. |  |_.' |\_..`--.
|  | | |  \.-._)   \|  .--' |  .   .'.-._)   \
\  '-'(_ .'\       /|  `---.|  |\  \ \       /
 `-----'    `-----' `------'`--' '--' `-----'

This script will list all users in a CID, or child CID(s).

Developed by @Don-Swanson-Adobe
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import APIHarnessV2, APIError
from tabulate import tabulate


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-m", "--mssp",
                        help="List users in all child CIDs (MSSP parents only)",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-c", "--child",
                        help="List users in a specific child CID (MSSP parents only)",
                        default=None
                        )
    parser.add_argument("-t", "--table_format",
                        help="Output table format",
                        default="simple"
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
cids = []
local = APIHarnessV2(**auth)
# If we are in MSSP mode, retrieve our child CID details
if cmd_line.mssp:
    try:
        cids.extend(local.command("getChildren", ids=local.command("queryChildren").data))
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
        cids.append({"name": cid_name[0]["name"], "child_cid": cmd_line.child})
    else:
        raise SystemExit("The provided child CID was not found within this tenant.")

# Return results for the current tenant when using MSSP "all" mode as well
if not cmd_line.child:
    try:
        cid_id = local.command("GetSensorInstallersCCIDByQuery").data[0][:-3].lower()
    except APIError as api_error:
        # They do not have access to the sensor downloads service collection with this key
        cid_id = f"Sensor Download scope required  "
    cids.append({"name": "My CrowdStrike tenant", "child_cid": cid_id})

details = []
table_headers = ["First Name", "Last Name", "UID", "UUID", "Tenant", "CID"]
for cid in cids:
    if cmd_line.mssp or cmd_line.child:
        if cid["name"] != "My CrowdStrike tenant":
            auth["member_cid"] = cid["child_cid"]
        else:
            auth.pop("member_cid")
    with APIHarnessV2(**auth) as falcon:
        response = falcon.command("RetrieveUser", ids=falcon.command("RetrieveUserUUIDsByCID").data)
        for user in response.data:
            details.append([
                user['firstName'],
                user['lastName'],
                user['uid'],
                user['uuid'],
                cid["name"],
                user['customer']
            ])
if not cmd_line.mssp or cmd_line.child:
    # Remove the MSSP centric columns if we're not in MSSP mode
    for det in details:
        det.pop()
        det.pop()
    table_headers.pop()
    table_headers.pop()
print(__doc__[438:810])  # Fancy table header pulled from the sample's docstring
print(tabulate(tabular_data=details, headers=table_headers, tablefmt=cmd_line.table_format))
