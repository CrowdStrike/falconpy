#!/usr/bin/env python3
r"""RTR Script manager.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

      ()                      _ _ _
      /\                _/_  ' ) ) )
     /  )  _. __  o _   /     / / / __.  ____  __.  _,  _  __
    /__/__(__/ (_<_/_)_<__   / ' (_(_/|_/ / <_(_/|_(_)_</_/ (_
                  /                                 /|
                 '                                 |/

This program can upload and delete RTR scripts from your CrowdStrike tenant.
For MSSP scenarios, scripts can be uploaded and removed from all tenants,
or a specific child.

Developed by @Don-Swanson-Adobe, modified by jshcodes@CrowdStrike

Requirements:
    crowdstrike-falconpy >= 1.3.0
    tabulate
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import APIHarnessV2, APIError
from tabulate import tabulate


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-a", "--action",
                        help="Action to perform (default is 'create')",
                        choices=["create", "c", "remove", "r", "list", "l"],
                        default="create"
                        )
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-m", "--mssp",
                        help="Handle script within all child CIDs (MSSP parents only)",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-c", "--child",
                        help="Handle scripts within in a specific child CID (MSSP parents only)",
                        default=None
                        )
    parser.add_argument("-t", "--table_format",
                        help="Output table format",
                        default="simple"
                        )
    fil = parser.add_argument_group("File arguments")
    fil.add_argument("-p", "--filepath",
                     help="Path to the script to be uploaded",
                     default=None
                     )
    fil.add_argument("-n", "--filename",
                     help="Name for the uploaded script (defaults to script filename)"
                     )
    fil.add_argument("-x", "--description",
                     help="Script description"
                     )
    fil.add_argument("-o", "--platform",
                     help="Script platform (defaults to Windows)",
                     default="windows",
                     choices=["windows", "linux", "mac"]
                     )
    fil.add_argument("-y", "--comment",
                     help="Script upload comment",
                     default=""
                     )
    fil.add_argument("-z", "--permission",
                     help="Script permissions (public, private, group, defaults to private)",
                     choices=["public", "private", "group"],
                     default="private",
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
    if parsed.action.lower() in ["c", "create"]:
        if not parsed.filepath:
            parser.error("You must specify the name of the file to be uploaded.")
        if not parsed.filename:
            parsed.filename = os.path.basename(parsed.filepath)
    elif parsed.action.lower() in ["r", "remove"]:
        if not parsed.filename:
            parser.error("You must specify the name of the file to be removed.")

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
        raise SystemExit(
            "This API client does not have access to the Flight Control API scope."
            )
    if not cids:
        raise SystemExit("No child CIDs were found within this tenant.")
elif cmd_line.child:
    try:
        cid_name = local.command("getChildren", ids=cmd_line.child)
    except APIError as api_error:
        # Throw an error if they provided us an invalid CID or do not have access to Flight Control
        if api_error.code == 403:
            raise SystemExit(
                "This API client does not have access to the Flight Control API scope."
                )
        elif api_error.code == 400:
            raise SystemExit("Invalid child CID provided.")
        else:
            raise SystemExit(api_error.message)
    if cid_name:
        cids.append({"name": cid_name[0]["name"], "child_cid": cmd_line.child})
    else:
        raise SystemExit("The provided child CID was not found within this tenant.")
else:
    cids.append({"name": "My CrowdStrike tenant", "child_cid": None})

success = False
#Setup the payload with the variables from above
create_payload = {
    "description": cmd_line.description,
    "name": cmd_line.filename,
    "comments_for_audit_log": cmd_line.comment,
    "permission_type": cmd_line.permission,
    "platform": [cmd_line.platform]
}
for cid in cids:
    if cid["child_cid"]:
        auth["member_cid"] = cid["child_cid"]
    falcon = APIHarnessV2(**auth)
    if cmd_line.action in ["create", "c"]:
        with open(cmd_line.filepath, "rb") as file_content:
            file_upload = {'file': file_content}
            try:
                print(f"\nCreating script within {cid['name']}")
                response = falcon.command("RTR_CreateScripts",
                                            data=create_payload,
                                            files=file_upload
                                            )
                success = True
            except APIError as api_error:
                print(api_error.message)
    elif cmd_line.action in ["list", "l"]:
        try:
            all_ids = falcon.command("RTR_ListScripts").data
            script_details = falcon.command("RTR_GetScripts", ids=all_ids).data
            for scr in script_details:
                hold_keys = {"name": "Name",
                                "description": "Description",
                                "platform": "Platform",
                                "permission_type": "Permissions",
                                "comment_for_audit_log" : "Comments"
                                }
                for key in [k for k in scr.keys() if k not in hold_keys]:
                    scr.pop(key)
                scr["platform"] = scr.get("platform", ["Not set"])[0]
            print(tabulate(tabular_data=script_details, headers=hold_keys, tablefmt=cmd_line.table_format))
        except APIError as api_error:
            print(api_error.message)
    else:
        # Remove
        script_id = None
        try:
            # Find script ID
            script_id = falcon.command("RTR_ListScripts",
                                        filter=f"name:'{cmd_line.filename}'"
                                        ).data[0]
        except APIError as api_error:
            raise SystemExit(api_error.message)
        except IndexError:
            print(f"\nSpecified script was not found on {cid['name']}")
        if script_id:
            print(f"\nRemoving {script_id} from {cid['name']}")
            # Remove script
            try:
                response = falcon.command("RTR_DeleteScripts", ids=script_id)
                success = True
            except APIError as api_error:
                print(api_error.message)

    if cmd_line.action not in ["list", "l"]:
        op_type = "Upload" if cmd_line.action in ["create", "c"] else "Delete"
        status = "completed successfully" if success else "failed"
        print(f"{op_type} operation {status}.")
