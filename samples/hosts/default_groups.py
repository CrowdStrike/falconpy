#!/usr/bin/env python3
r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

·▄▄▄▄  ▄▄▄ .·▄▄▄ ▄▄▄· ▄• ▄▌▄▄▌  ▄▄▄▄▄     ▄▄ • ▄▄▄        ▄• ▄▌ ▄▄▄·.▄▄ ·
██▪ ██ ▀▄.▀·▐▄▄·▐█ ▀█ █▪██▌██•  •██      ▐█ ▀ ▪▀▄ █·▪     █▪██▌▐█ ▄█▐█ ▀.
▐█· ▐█▌▐▀▀▪▄██▪ ▄█▀▀█ █▌▐█▌██▪   ▐█.▪    ▄█ ▀█▄▐▀▀▄  ▄█▀▄ █▌▐█▌ ██▀·▄▀▀▀█▄
██. ██ ▐█▄▄▌██▌.▐█ ▪▐▌▐█▄█▌▐█▌▐▌ ▐█▌·    ▐█▄▪▐█▐█•█▌▐█▌.▐▌▐█▄█▌▐█▪·•▐█▄▪▐█
▀▀▀▀▀•  ▀▀▀ ▀▀▀  ▀  ▀  ▀▀▀ .▀▀▀  ▀▀▀     ·▀▀▀▀ .▀  ▀ ▀█▄▀▪ ▀▀▀ .▀    ▀▀▀▀

This script was developed to setup the default groups in a new CID.
It should be run once to create the necessary groups and populate
them with the appropriate assignment rules.

Note: This sample demonstrates pythonic response handling using the
      Advanced Uber Class (APIHarnessV2).

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
                        help="Create groups for all child CIDs (MSSP parents only).",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-c", "--child",
                        help="Create groups in a specific child CID (MSSP parents only).",
                        default=None
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


def add_group(sdk: APIHarnessV2, name: str, rule: str):
    """Add the group the the CID."""
    if rule == "staticByID":
        BODY = {"resources": [{
            "group_type": "staticByID",
            "name": name
        }]}
    elif rule == "none":
        BODY = {"resources": [{
            "group_type": "dynamic",
            "name": name
        }]}
    else:
        BODY = {"resources": [{
            "group_type": "dynamic",
            "name": name,
            "assignment_rule": rule
        }]}
    try:
        sdk.command("createHostGroups", body=BODY)
        print(f"{name} group created successfully")
    except APIError as api_error:
        print(api_error.message)



#### UPDATE THE FOLLOWING DICTIONARY TO MATCH YOUR ENVIRONMENT ##########
# One group will be created for each dictionary item.
# Groups are defined as "Group Name": "Assignment Rule"
groups = {
    "Sensor Uninstall Group": "staticByID",
    "Phase 0": "none",
    "Phase 1": "hostname:*'*'",
    "Active Policy": "none",
    "Windows Servers": "platform_name:'Windows'+product_type_desc:'Server'",
    "DEV Updates": "tags:'SensorGroupingTags/DEV'",
    "Golden Images": "tags:'FalconGroupingTags/GoldenImage'",
    "Windows 7 and Server 2008 R2 Hosts": "(os_version:'Windows Server 2008 R2',os_version:'Windows 7')"
}
#########################################################################

# Consume the command line
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
# If we are in MSSP mode, retrieve our child CID details
if cmd_line.mssp:
    parent = APIHarnessV2(**auth)
    cids = parent.command("getChildren", ids=parent.command("queryChildren").data)
elif cmd_line.child:
    parent = APIHarnessV2(**auth)
    try:
        cid_name = parent.command("getChildren", ids=cmd_line.child)
    except APIError as api_error:
        # Throw an error if they provided us an invalid CID
        raise SystemExit(api_error.message)
    cids = [{"name": cid_name[0]["name"]}]
else:
    # If not, we'll just run this in our current tenant
    cids = [{"name": "CrowdStrike"}]

# Do the needful for each CID
for cid in cids:
    print(f"Processing {cid['name']}")
    if cmd_line.mssp:
        # If we're a parent, add this child's CID to our authentication request
        auth["member_cid"] = cid["child_cid"]
    elif cmd_line.child:
        auth["member_cid"] = cmd_line.child
    # Authenticate to the API
    falcon = APIHarnessV2(**auth)
    # Add groups with variable names dependent on CID Name
    # (Useful for at a glance reporting of All Hosts and RFM Hosts)
    groups.update({
        cid["name"] + " - All": "hostname:*'*'",
        cid["name"] + " - RFM": "reduced_functionality_mode:'yes'"
        })

    # Create the groups in the CID
    for name,rule in groups.items():
        add_group(falcon, name, rule)
