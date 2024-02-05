#!/usr/bin/env python3
r"""Create Host Groups (and add them to Prevention Policies).

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

 __  __                .           ___
 |   |    __.    ____ _/_        .'   \  .___    __.  ,   . \,___,
 |___|  .'   \  (      |         |       /   \ .'   \ |   | |    \
 |   |  |    |  `--.   |         |    _  |   ' |    | |   | |    |
 /   /   `._.' \___.'  \__/       `.___| /      `._.' `._/| |`---'
                                                            \
                     .----------------.
                    | .--------------. |
                    | |      _       | |
                    | |     | |      | |
                    | |  ___| |___   | |
                    | | |___   ___|  | |
                    | |     | |      | |
                    | |     |_|      | |
                    | |              | |
                    | '--------------' |
                     '----------------'
 .___                                     .
 /   \ .___    ___  _   __   ___  , __   _/_   `   __.  , __
 |,_-' /   \ .'   ` |   /  .'   ` |'  `.  |    | .'   \ |'  `.
 |     |   ' |----' `  /   |----' |    |  |    | |    | |    |
 /     /     `.___,  \/    `.___, /    |  \__/ /  `._.' /    |

                .___          .
                /   \   __.   |   `   ___  `   ___    ____
                |,_-' .'   \  |   | .'   ` | .'   `  (
                |     |    |  |   | |      | |----'  `--.
                /      `._.' /\__ /  `._.' / `.___, \___.'

This script will create a host group. If a list of prevention policy IDs
are provided, the newly created host group is added to each policy in the
list. This can assist with complex group creation that may be difficult
to perform in the console.

Please note: If you set custom and/or criteria using the API, editing the
group in the Falcon console will remove this criteria upon save.

Developed by Don-Swanson-Adobe

Dynamic Host group examples with custom and/or criteria

AND Example (Product is Windows AND Type is Server):
    "platform_name:'Windows'+product_type_desc:'Server'"

OR Example (OS is Win Server 2008 R2 OR OS is Windows 7):
"os_version:'Windows Server 2008 R2',os_version:'Windows 7'"
OR Example (OS is Win Server 2008 R2 OR OS is Windows 7)
"(os_version:'Windows Server 2008 R2',os_version:'Windows 7')"

Mixed Use Example (Must Have a DEV Sensor Tag and a T1 or T2 Sensor Tag)
"(tags:'SensorGroupingTags/DEV'+tags:'SensorGroupingTags/T1),(tags:'SensorGroupingTags/DEV'+tags:'SensorGroupingTags/T2')"
"tags:'SensorGroupingTags/DEV'+(tags:'SensorGroupingTags/T1',tags:'SensorGroupingTags/T2')"
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import APIHarnessV2, APIError, Result


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-c", "--child",
                        help="Perform operations in a specific child CID (MSSP parents only)",
                        default=None
                        )
    grp = parser.add_argument_group("Group arguments")
    grp.add_argument("-n", "--group_name",
                     help="Name to use for newly created Host Group",
                     required=True
                     )
    grp.add_argument("-e", "--group_description",
                     help="Description to use for newly created Host Group"
                     )
    grp.add_argument("-t", "--group_type",
                     help="Type of Host Group to create (dynamic or static, defaults to dynamic)",
                     choices=["dynamic", "static"],
                     default="dynamic"
                     )
    grp.add_argument("-a", "--assignment_rule",
                     help="Assignment rule for the newly created Host Group (enclose in double quotes)"
                     )
    grp.add_argument("-p", "--policies",
                     help="Prevention Policies IDs to assign this Host Group to (comma delimit)"
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
        parser.error(
            "You must provide CrowdStrike API credentials using the '-k' and '-s' arguments."
            )
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
if cmd_line.child:
    # Authenticate to the child if necessary
    auth["member_cid"] = cmd_line.child
falcon = APIHarnessV2(**auth)
# Create Host Group
body_payload = {
    "resources": [{
            "assignment_rule": cmd_line.assignment_rule,
            "description": cmd_line.group_description,
            "group_type": cmd_line.group_type,
            "name": cmd_line.group_name
            }]
        }
try:
    response = falcon.command("createHostGroups", body=body_payload)
except APIError as api_error:
    raise SystemExit(api_error.message)

print(f"New Group ID: {response.data[0]['id']}")
group_id = response.data[0]["id"]
if cmd_line.policies:
    # Attach new group to policy
    for policy in cmd_line.policies.split(","):
        body_payload = {
            "action_parameters": [{
                        "name": "group_id",
                        "value": group_id
                    }],
                    "ids": [policy]
                    }
        try:
            response: Result = falcon.command("performPreventionPoliciesAction",
                                    action_name="add-host-group",
                                    body=body_payload
                                    )
            print(f"{cmd_line.group_name} successfully added to prevention policy (ID: {policy})")
        except APIError as api_error:
            print(api_error.message)
