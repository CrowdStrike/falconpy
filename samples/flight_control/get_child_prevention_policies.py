r"""Retrieve child prevention policies.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |         FalconPy v1.2
`-------'                         `-------'

___  ____ ____ _  _ ____ _  _ ___ _ ____ _  _    ___  ____ _    _ ____ _ ____ ____
|__] |__/ |___ |  | |___ |\ |  |  | |  | |\ |    |__] |  | |    | |    | |___ [__
|    |  \ |___  \/  |___ | \|  |  | |__| | \|    |    |__| |___ | |___ | |___ ___]

Retrieve the prevention policies for all (or a subset of) child tenants within the parent.

Creation: 02.19.23 - jshcodes@CrowdStrike
"""
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import FlightControl, PreventionPolicy


def consume_arguments():
    """Consume any command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    req = parser.add_argument_group("required arguments")
    req.add_argument("-k", "--falcon_client_id",
                     help="CrowdStrike Falcon API client ID",
                     required=True
                     )
    req.add_argument("-s", "--falcon_client_secret",
                     help="CrowdStrike Falcon API client Secret",
                     required=True
                     )
    parser.add_argument("-c", "--children",
                        help="List of children to retrieve (comma-delimit)",
                        default=None
                        )
    return parser.parse_args()


def open_sdk(cmd: Namespace):
    """Open the Flight Control service collection using the keys provided."""
    return FlightControl(client_id=cmd.falcon_client_id, client_secret=cmd.falcon_client_secret)


def retrieve_children(sdk: FlightControl, specified: str):
    """Retrieve all child tenants for this MSSP parent."""
    kids = []
    if specified:
        kids = specified.split(",")
    else:
        children_lookup = sdk.query_children()
        lookup_status = children_lookup["status_code"]
        if lookup_status == 200:
            kids = children_lookup["body"]["resources"]
        if not kids:
            fail_message = "No children found!"
            if lookup_status in [401, 403]:
                fail_message = "Unable to access Flight Control API using provided credentials."
            if lookup_status == 429:
                fail_message = "Rate limit met, please retry your request after a few seconds."
            raise SystemExit(fail_message)

    return kids


def list_prevent_policies(child_tenants: list, cmd: Namespace):
    """List all prevention policies for each child tenant."""
    for child_id in child_tenants:
        # Login to the Policy API for this child tenant
        policy_api = PreventionPolicy(client_id=cmd.falcon_client_id,
                                      client_secret=cmd.falcon_client_secret,
                                      member_cid=child_id
                                      )
        policy_lookup = policy_api.query_combined_policies()
        if policy_lookup["status_code"] == 200:
            policies = policy_lookup["body"]["resources"]
            if not policies:
                print(f"No policies found for {child_id}.")
            for policy in policies:
                result = f"[{child_id}] {policy['name']} ({policy['id']})"
                if policy["cid"] == child_id:
                    print(result)


if __name__ == "__main__":
    # Retrieve provided command line arguments
    cmd_line = consume_arguments()
    # Open the SDK, retrieve all children and list their policies
    list_prevent_policies(retrieve_children(open_sdk(cmd_line), cmd_line.children), cmd_line)
