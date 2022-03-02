r"""CrowdStrike Falcon Bulk User Maintenance utility.

 ___ ___                   ___ ___                                                    __
|   Y   .-----.-----.----.|   Y   .---.-.-----.---.-.-----.-----.--------.-----.-----|  |_
|.  |   |__ --|  -__|   _||.      |  _  |     |  _  |  _  |  -__|        |  -__|     |   _|
|.  |   |_____|_____|__|  |. \_/  |___._|__|__|___._|___  |_____|__|__|__|_____|__|__|____|
|:  1   |                 |:  |   |                 |_____|
|::.. . |                 |::.|:. |                          CrowdStrike FalconPy v1.0
`-------'                 `--- ---'


Creation date: 2020.11.06 - jhseceng@CrowdStrike
Modification date: 2022.02.10 - jshcodes@CrowdStrike

Leverages the FalconPy API SDK to add and remove users within Falcon.
Accepts the commands add, remove, update, getroles

This solution requires the FalconPy SDK. This project
can be accessed here: https://github.com/CrowdStrike/falconpy

"""

import json
from argparse import ArgumentParser, RawTextHelpFormatter
try:
    from tabulate import tabulate
except ImportError as no_tabulate:
    raise SystemExit(
        "The tabulate package must be installed in order to use this program."
        ) from no_tabulate
try:
    from falconpy import UserManagement
except ImportError as no_falconpy:
    raise SystemExit(
        "The crowdstrike-falconpy package must be installed to use this program."
        ) from no_falconpy


class Color:  # pylint: disable=R0903
    """Class to represent the text color codes used for terminal output."""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    LIGHTBLUE = "\033[94m"
    GREEN = "\033[32m"
    LIGHTGREEN = "\033[92m"
    LIGHTYELLOW = "\033[93m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    LIGHTRED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def inform(msg: str):
    """Provide informational updates to the user as the program progresses."""
    print("  %-80s" % msg, end="\r", flush=True)  # pylint: disable=C0209


def register_user(file):
    """Register the users listed in our data file by UID."""
    users = import_users_from_file(file)
    for user in users['resources']:
        # Call the API to update the requested account.
        register_response = falcon_user.create_user(first_name=user['first_name'],
                                                    last_name=user['last_name'],
                                                    uid=user['uid']
                                                    )
        if register_response["status_code"] == 201:
            print(f"Successfully {Color.GREEN}registered{Color.END} user",
                  f"{Color.BOLD}{user['uid']}{Color.END}")
        else:
            for err in register_response["body"]["errors"]:
                ecode = err["code"]
                emsg = err["message"]
                print(f"Registration failed for {user['uid']} with response:",
                      f"{Color.BOLD}{ecode} {emsg}{Color.END}"
                      )


def delete_users(file):
    """Delete the users listed in our data file by UID."""
    # Call the API to update the requested account.
    users = import_users_from_file(file)
    for user in users["resources"]:
        # Grab the UUID for this UID
        user_uuid = falcon_user.retrieve_user_uuid(uid=user["uid"])["body"]
        if "resources" in user_uuid:
            user_uuid = user_uuid["resources"][0]
            # Delete the record using the UUID
            update_response = falcon_user.delete_user(user_uuid=user_uuid)
            if update_response["status_code"] == 200:
                print(f"Successfully {Color.RED}removed{Color.END} user account",
                      f"{Color.BOLD}{user['uid']}{Color.END}.")
            else:
                for err in update_response["body"]["errors"]:
                    ecode = err["code"]
                    emsg = err["message"]
                    print(f"Delete failed for {user['uid']} with response:",
                          f"{Color.BOLD}{ecode} {emsg}{Color.END}"
                          )
        else:
            print(f"User {Color.BOLD}{user['uid']}{Color.END} defined",
                  "in data file does not exist in your Falcon tenant."
                  )


def update_users(file):
    """Update the users in our data file based upon the roles lists in the data file."""
    users = import_users_from_file(file)
    for user in users["resources"]:
        if user["role_list"]:
            user_uuid = falcon_user.retrieve_user_uuid(uid=user["uid"])["body"]
            if "resources" in user_uuid:
                user_uuid = user_uuid["resources"][0]
                old = falcon_user.get_user_role_ids(user_uuid=user_uuid)["body"]["resources"]
                if old:
                    falcon_user.revoke_user_role_ids(user_uuid=user_uuid, ids=old)
                update_response = falcon_user.grant_user_role_ids(user_uuid=user_uuid,
                                                                  role_ids=user['role_list']
                                                                  )
                if update_response["status_code"] == 200:
                    print(f"Successfully {Color.LIGHTBLUE}updated{Color.END} the",
                          f"{Color.BOLD}{user['uid']}{Color.END} account.")
                else:
                    for err in update_response["body"]["errors"]:
                        ecode = err["code"]
                        emsg = err["message"]
                        print(f"Update failed for {user['uid']} with response:",
                              f"{Color.BOLD}{ecode} {emsg}{Color.END}"
                              )
            else:
                print(f"User {Color.BOLD}{user['uid']}{Color.END} defined in",
                      "data file does not exist in your Falcon tenant."
                      )
        else:
            print(f"No update performed for user {Color.BOLD}{user['uid']}{Color.END}.")


def get_roles():
    """Retrieve the assigned roles for the specified user."""
    response = falcon_user.get_available_role_ids()
    if response['status_code'] == 200:
        print('The following roles are available for assignment\n')
        for role_name in response["body"]["resources"]:
            print(role_name)
    else:
        print('Failed to get available roles')


def import_users_from_file(file):
    """Import our user data file and return the results."""
    with open(file, newline='', encoding="utf-8") as load_file:
        users = json.load(load_file)

        return users


def list_users(table_fmt: str, sorting: str, reversing: bool):  # pylint: disable=R0915
    """List all current users within the tenant."""

    def lookup_fail(resultset: dict):
        for err in resultset["body"]["errors"]:
            ecode = err["code"]
            emsg = err["message"]
            print(f"Lookup failed with response: {Color.BOLD}{ecode} {emsg}{Color.END}")

    def sort_header(title: str):
        return f"{Color.BOLD}{Color.BLUE}{title}{Color.END}"

    def standard_header(title: str):
        return f"{Color.BOLD}{title}{Color.END}"

    def format_headers():
        created_headers = {}
        if sorting == "firstName":
            created_headers["firstName"] = sort_header("First Name")
        else:
            created_headers["firstName"] = standard_header("First Name")
        if sorting == "lastName":
            created_headers["lastName"] = sort_header("Last Name")
        else:
            created_headers["lastName"] = standard_header("Last Name")
        if sorting == "uid":
            created_headers["uid"] = sort_header("User ID")
        else:
            created_headers["uid"] = standard_header("User ID")
        if sorting == "uuid":
            created_headers["uuid"] = sort_header("UUID")
        else:
            created_headers["uuid"] = standard_header("UUID")
        if sorting == "roles":
            created_headers["roles"] = sort_header("Roles")
        else:
            created_headers["roles"] = standard_header("Roles")

        return created_headers

    def retrieve_roles(user_uuid: str):
        rolez = []
        role_lookup = falcon_user.get_user_role_ids(user_uuid=user_uuid)
        if role_lookup["status_code"] == 200:
            if role_lookup["body"]["resources"]:
                for role_id in role_lookup["body"]["resources"]:
                    rolez.append(role_id)
            else:
                rolez.append("User has no roles assigned")
        else:
            rolez.append("Unable to retrieve user roles")

        return "\n".join(rolez)

    table_headers = format_headers()
    user_list = []
    inform("Retrieving user list")
    id_list_lookup = falcon_user.retrieve_user_uuids_by_cid()
    if id_list_lookup["status_code"] == 200:
        inform("Retrieve user details")
        id_list = falcon_user.retrieve_user(ids=id_list_lookup["body"]["resources"])
        if id_list["status_code"] == 200:
            for user in id_list["body"]["resources"]:
                inform(f"Retrieving roles for {user['uid']}")
                user.pop("customer")
                user["roles"] = retrieve_roles(user["uuid"])
                user_list.append(user)
            user_list = sorted(user_list, key=lambda item: item[sorting], reverse=reversing)
            print(f"{Color.MAGENTA}{USER_BANNER}{Color.END}")
            print(tabulate(tabular_data=user_list, headers=table_headers, tablefmt=table_fmt))
        else:
            lookup_fail(id_list)
    else:
        lookup_fail(id_list_lookup)


def parse_command_line():
    """Ingest the provided command line parameters and handle any input errors."""
    # Configure argument parsing
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument('-d', '--data_file', help='File name of user data file', required=False)
    parser.add_argument('-c',
                        '--command',
                        help='Action to perform (list/add/remove/update/getroles)',
                        required=False
                        )
    parser.add_argument("-k", "--falcon_client_id", help="Falcon Client ID", required=True)
    parser.add_argument("-s", "--falcon_client_secret", help="Falcon Client Secret", required=True)
    parser.add_argument("-m", "--mssp", help="Child CID to access", required=False)
    parser.add_argument("-o", "--sort",
                        help="Field to sort by, one of:\n"
                        "firstName, lastName, roles, uid, uuid\n"
                        "Defaults to lastName (asc)",
                        required=False
                        )
    parser.add_argument("-r", "--reverse",
                        help="Reverse the sort order",
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-n", "--no_color",
                        help="Disable color output in result displays",
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-t", "--table_format",
                        help="Table format to use for display, one of:\n"
                        "plain, simple, github, grid, fancy_grid, pipe, orgtbl, \n"
                        "jira, presto, pretty, psql, rst, mediawiki, moinmoin, \n"
                        "youtrack, html, unsafehtml, latext, latex_raw, \n"
                        "latex_booktabs, latex_longtable, textile, or tsv.",
                        required=False
                        )
    args = parser.parse_args()

    cmd = "list"
    if args.command:
        cmd = args.command.lower()
    # Only execute our defined commands
    if cmd in ["add", "remove", "update", "getroles", "list"]:
        if not args.data_file and cmd not in ["getroles", "list"]:
            parser.error(f"The {cmd} command requires the -d arguments to also be specified.")
        file = args.data_file
        falcon_client_id = args.falcon_client_id
        falcon_secret = args.falcon_client_secret
        mssp = None
        if args.mssp:
            mssp = args.mssp
        colors = False
        if args.no_color:
            colors = args.no_color
        table_style = "fancy_grid"
        if args.table_format:
            table_style = args.table_format
        sort = "lastName"
        if args.sort:
            sort = args.sort
        if sort not in ["firstName", "lastName", "roles", "uid", "uuid"]:
            parser.error(f"The {sort} sort option is not recognized."
                         "\nAllowed options: firstName, lastName, roles, uid, uuid")
        reverse = False
        if args.reverse:
            reverse = args.reverse
    else:
        parser.error(f"The {cmd} command is not recognized.")

    return cmd, file, falcon_client_id, falcon_secret, mssp, colors, table_style, sort, reverse


USER_BANNER = r"""
 _____     _                   _   _                 _     _     _   _
|  ___|_ _| | ___ ___  _ __   | | | |___  ___ _ __  | |   (_)___| |_(_)_ __   __ _
| |_ / _` | |/ __/ _ \| '_ \  | | | / __|/ _ \ '__| | |   | / __| __| | '_ \ / _` |
|  _| (_| | | (_| (_) | | | | | |_| \__ \  __/ |    | |___| \__ \ |_| | | | | (_| |
|_|  \__,_|_|\___\___/|_| |_|  \___/|___/\___|_|    |_____|_|___/\__|_|_| |_|\__, |
                                                                             |___/
"""

if __name__ == "__main__":
    # Parse the command line arguments and set our variables
    command, filename, client_id, client_secret, child_cid, no_colors, tables, \
        sort_column, sort_direction = parse_command_line()
    if no_colors:
        for attr in dir(Color):
            if "__" not in attr:
                setattr(Color, attr, "")

    # Authenticate using our provided falcon client_id and client_secret
    falcon_user = UserManagement(client_id=client_id,
                                 client_secret=client_secret,
                                 member_cid=child_cid
                                 )
    # Confirm we authenticated
    if falcon_user.token_fail_reason:
        # Report that authentication failed and stop processing
        raise SystemExit(f"Authorization failed: {falcon_user.token_fail_reason}")

    try:
        # Execute the command by calling the named function
        if command == "add":
            register_user(filename)
            update_users(filename)
        elif command == "remove":
            delete_users(filename)
        elif command == "update":
            update_users(filename)
        elif command == "list":
            list_users(tables, sort_column, sort_direction)
        elif command == "getroles":
            get_roles()
    except Exception as errored:  # pylint: disable=W0703  # Catching any variation
        # Handle any previously unhandled errors
        raise SystemExit(f"Command failed with error: {str(errored)}.") from errored
    # Discard our token on our way out
    falcon_user.auth_object.revoke(falcon_user.token)
