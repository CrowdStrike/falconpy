#!/usr/bin/env python3
r"""Duplicate host groups from a parent down to the children.

 _   _           _      ____                         ____              _ _           _
| | | | ___  ___| |_   / ___|_ __ ___  _   _ _ __   |  _ \ _   _ _ __ | (_) ___ __ _| |_ ___  _ __
| |_| |/ _ \/ __| __| | |  _| '__/ _ \| | | | '_ \  | | | | | | | '_ \| | |/ __/ _` | __/ _ \| '__|
|  _  | (_) \__ \ |_  | |_| | | | (_) | |_| | |_) | | |_| | |_| | |_) | | | (_| (_| | || (_) | |
|_| |_|\___/|___/\__|  \____|_|  \___/ \__,_| .__/  |____/ \__,_| .__/|_|_|\___\__,_|\__\___/|_|
                                            |_|                 |_|


"""
from argparse import ArgumentParser, RawTextHelpFormatter
from falconpy import HostGroup, FlightControl


def create_host_group(sdk: HostGroup, gdesc: str, gtype: str, gname: str, arule: str):
    """Create a host group within the tenant based upon provided keyword arguments."""
    returned_id = None
    create_response = sdk.create_host_groups(description=gdesc,
                                             group_type=gtype,
                                             name=gname,
                                             assignment_rule=arule
                                             )
    if create_response["status_code"] == 409:
        # Group already exists
        print(f"Group {gname} already exists within this tenant.")

    elif create_response["status_code"] != 201:
        print(f"Unable to create group {gname} within this tenant.")
    else:
        returned_id = create_response["body"]["resources"][0]["id"]

    return returned_id


def consume_arguments():
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-k", "--falcon_client_id",
                        help="CrowdStrike Falcon API Client ID",
                        required=True
                        )
    parser.add_argument("-s", "--falcon_client_secret",
                        help="CrowdStrike Falcon API Client secret",
                        required=True
                        )
    parser.add_argument("-r", "--region",
                        help="CrowdStrike Region (us1, us2, eu1, usgov1). Required for usgov1.",
                        required=False,
                        default="auto"
                        )
    parser.add_argument("-f", "--hostgroup_filter",
                        help="String to use to search for host groups within the parent.",
                        required=True
                        )

    return parser.parse_args()


def get_host_group_matches(sdk: HostGroup, filter_string: str):
    """Retrieve our parent groups to duplicate using our provided filter."""
    result = sdk.query_combined_host_groups(filter=f"name:*'*{filter_string}*'")
    if result["status_code"] != 200:
        raise SystemExit("Unable to retrieve host group details from parent.")
    if not result["body"]["resources"]:
        raise SystemExit(
            "No host groups identified within parent that match the provided search term."
            )
    return result["body"]["resources"]


# MAIN ROUTINE
args = consume_arguments()
creds = {
    "client_id": args.falcon_client_id,
    "client_secret": args.falcon_client_secret
}
mssp = FlightControl(creds=creds, base_url=args.region)
parent_groups = HostGroup(auth_object=mssp.auth_object)
# Retrieve a list of children
children = mssp.query_children()["body"]["resources"]
if not children:
    # No children found, crash out
    raise SystemExit("No children found, are you using the correct API credentials?")

# Get our list of groups to migrate
host_groups_to_migrate = get_host_group_matches(parent_groups, args.hostgroup_filter)

# Loop through all identified children
for child in children:
    creds["member_cid"] = child  # Set member_cid in the credentials dictionary
    print(f"Tenant ID: {child}")
    groups = HostGroup(creds=creds, base_url=args.region)
    # Loop through all groups returned that match our filter
    for group in host_groups_to_migrate:
        # Create the group
        group_id = create_host_group(sdk=groups,
                                     gdesc=group["description"],
                                     gtype=group["group_type"],
                                     gname=group["name"],
                                     arule=group["assignment_rule"]
                                     )
        if group_id:
            print(f"Group {group_id} created.")
    print(f"{'=' * 80}\n")
