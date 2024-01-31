#!/usr/bin/env python3
r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

 __   __  _______  _______  _______
|  | |  ||       ||       ||       |
|  |_|  ||   _   ||  _____||_     _|
|       ||  | |  || |_____   |   |
|       ||  |_|  ||_____  |  |   |
|   _   ||       | _____| |  |   |
|__| |__||_______||_______|  |___|
         _______  ______    _______  __   __  _______  _______
        |       ||    _ |  |       ||  | |  ||       ||       |
        |    ___||   | ||  |   _   ||  | |  ||    _  ||  _____|
        |   | __ |   |_||_ |  | |  ||  |_|  ||   |_| || |_____
        |   ||  ||    __  ||  |_|  ||       ||    ___||_____  |
        |   |_| ||   |  | ||       ||       ||   |     _____| |
        |_______||___|  |_||_______||_______||___|    |_______|

This script will output a list of all Host Groups, for Flight Control
scenarios it will display all the host groups in all child CIDs.
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
                        help="List groups in all child CIDs (MSSP parents only)",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-c", "--child",
                        help="List groups in a specific child CID (MSSP parents only)",
                        default=None
                        )
    parser.add_argument("-t", "--table_format",
                        help="Table format to use for tabular display",
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

# Do the needful for each CID in the list
for cid in cids:
    print(f"\n{cid['name']} host groups")
    if cmd_line.mssp:
        # If we're a parent, add this child's CID to our authentication request
        auth["member_cid"] = cid["child_cid"]
    elif cmd_line.child:
        auth["member_cid"] = cmd_line.child
    # Demonstrating using the SDK interface as a context manager
    # This will automatically discard the bearer token when exiting the context.
    with APIHarnessV2(**auth) as sdk:
        # Fields we want to display
        keep = {"id": "ID", "name": "Name", "description": "Description"}
        # Sometimes list comprehension is ridiculously cool...
        results = [{k: v for k, v in d.items() if k in keep} for d in sdk.command("queryCombinedHostGroups")]
        print(tabulate(tabular_data=results, headers=keep, tablefmt=cmd_line.table_format))
