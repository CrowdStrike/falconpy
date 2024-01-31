#!/usr/bin/env python3
r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

       __                                       ___  ___   ___
  .'|=|  |    .'|=|`.     .'|        .'|   .'|=|_.' |   | |   |
.'  | |  |  .'  | |  `. .'  |      .'  | .'  |      `.  |_|  .'
|   |=|.'   |   | |   | |   |      |   | |   |        `.   .'
|   |       `.  | |  .' |   |  ___ |   | `.  |  ___    |   |
|___|         `.|=|.'   |___|=|_.' |___|   `.|=|_.'    |___|

       ___                    ___        ___
  .'|=|_.'   .'| |`.     .'|=|_.'   .'|=|_.'   .'|   .'|
.'  |      .'  | |  `. .'  |  ___ .'  |      .'  | .' .'
|   |      |   |=|   | |   |=|_.' |   |      |   |=|.:
`.  |  ___ |   | |   | |   |  ___ `.  |  ___ |   |   |'.
  `.|=|_.' |___| |___| |___|=|_.'   `.|=|_.' |___|   |_|

This program will check if a specific host group is properly
assigned to a list of Prevention Policies.

Created by: @Don-Swanson-Adobe
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import APIHarnessV2, APIError
from termcolor import colored

def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-m", "--mssp",
                        help="List groups in all child CIDs (MSSP parents only)",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-c", "--child",
                        help="List groups in a specific child CID (MSSP parents only)",
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
    req.add_argument("-g", "--group_name",
                     help="Group name to check",
                     required=True
                     )
    req.add_argument("-p", "--policy_ids",
                     help="Policy IDs to confirm (comma delimit)",
                     required=True
                     )
    parsed = parser.parse_args()
    if not parsed.client_id or not parsed.client_secret:
        parser.error("You must provide CrowdStrike API credentials using the '-k' and '-s' arguments.")

    return parsed


# Let's shine up the screen output a bit with a couple of constants
THERE = colored("is", "green", attrs=["bold"])
NOT_THERE = colored("is NOT", "red", attrs=["bold"])

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
    cids = [{"name": cid_name[0]["name"], "child_cid": cmd_line.child}]
else:
    # If not, we'll just run this in our current tenant
    cids = [{"name": "CrowdStrike"}]

for cid in cids:
    print(f"CID: {cid['name']}")
    if cmd_line.mssp or cmd_line.child:
        auth["member_cid"] = cid["child_cid"]
    # Open the SDK using a context manager so it automatically logs us out when we're done
    with APIHarnessV2(**auth) as sdk:
        # Parse thru the groups available to identify our match
        # This will return a list of one dictionary on success
        gid = [g for g in sdk.command("queryCombinedHostGroups").data if g["name"] == cmd_line.group_name]
        if gid:
            # Check for bad policy ID input
            try:
                policies = sdk.command("getPreventionPolicies", ids=cmd_line.policy_ids).data
            except APIError as api_error:
                # Stop processing if the policy IDs are not valid
                raise SystemExit(f"One or more of the policy IDs provided is invalid ({api_error.message}).")
            for policy in policies:
                # Use a quick comprehension to identify if there is a match, empty list = no match
                status = THERE if [g for g in policy["groups"] if g["id"] == gid[0]["id"]] else NOT_THERE
                print(
                    f"The {colored(cmd_line.group_name, 'white', attrs=['bold'])} group "
                    f"{status} assigned to the {colored(policy['name'], 'white', attrs=['underline'])} "
                    f"({policy['id']}) [{policy['platform_name']}] policy."
                    )
        else:
            print(f"The {cmd_line.group_name} group does not exist within {cid['name']}.")
