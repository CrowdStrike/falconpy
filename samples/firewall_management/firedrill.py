r"""FireDrill - Firewall Mangement service class walkthrough.

 ________  _____  _______     ________  ______   _______     _____  _____     _____
|_   __  ||_   _||_   __ \   |_   __  ||_   _ `.|_   __ \   |_   _||_   _|   |_   _|
  | |_ \_|  | |    | |__) |    | |_ \_|  | | `. \ | |__) |    | |    | |       | |
  |  _|     | |    |  __ /     |  _| _   | |  | | |  __ /     | |    | |   _   | |   _
 _| |_     _| |_  _| |  \ \_  _| |__/ | _| |_.' /_| |  \ \_  _| |_  _| |__/ | _| |__/ |
|_____|   |_____||____| |___||________||______.'|____| |___||_____||________||________|

Creates a new rule group, adds new rules, changes their order, modifies rule properties
deletes a rule, then deletes the rule group

02/27/24 - jlangdev@CrowdStrike
"""
import os
from random import SystemRandom
from argparse import ArgumentParser, RawTextHelpFormatter
try:
    from falconpy import FirewallManagement
except (ImportError, ModuleNotFoundError) as no_falconpy:
    raise SystemExit(
        "The crowdstrike-falconpy package must be installed to run this program."
        ) from no_falconpy

RULES = [
            {
                "action": "ALLOW",
                "address_family": "IP4",
                "description": "test rule 1",
                "direction": "IN",
                "enabled": True,
                "fields": [
                    {
                        "name": "image_name",
                        "value": "",
                        "type": "windows_path",
                        "values": []
                    }
                ],
                "fqdn": "",
                "fqdn_enabled": False,
                "icmp": {"icmp_code": "", "icmp_type": ""},
                "local_address": [{"address": "*", "netmask": 0}],
                "local_port": [{"end": 1000, "start": 1}],
                "log": False,
                "monitor": {"count": "1", "period_ms": "1000000"},
                "name": "rule1",
                "protocol": "6",
                "remote_address": [{"address": "10.0.77.101-104", "netmask": 0}],
                "remote_port": [{"end": 1000, "start": 1}],
                "temp_id": "1"
            },
            {
                "action": "ALLOW",
                "address_family": "IP4",
                "description": "test rule 2",
                "direction": "IN",
                "enabled": True,
                "fields": [
                    {
                        "name": "image_name",
                        "value": "",
                        "type": "windows_path",
                        "values": []
                    }
                ],
                "fqdn": "",
                "fqdn_enabled": False,
                "icmp": {"icmp_code": "", "icmp_type": ""},
                "local_address": [{"address": "*", "netmask": 0}],
                "local_port": [{"end": 2000, "start": 1001}],
                "log": False,
                "monitor": {"count": "1", "period_ms": "1000000"},
                "name": "rule2",
                "protocol": "6",
                "remote_address": [{"address": "10.0.76.101-104", "netmask": 0}],
                "remote_port": [{"end": 2000, "start": 1001}],
                "temp_id": "2",
            },
        ]

DIFFS = [
            {
                "value": RULES[0],
                "op": "add",
                "path": "/rules/0"
            },
            {
                "value": RULES[1],
                "op": "add",
                "path": "/rules/1"
            },
            {
                "value": "modified0",
                "op": "replace",
                "path": "/rules/0/name"
            },
            {
                "value": "modified1",
                "op": "replace",
                "path": "/rules/1/name"
            },
            {
                "op": "remove",
                "path": "/rules/1"
            }
        ]


def create_rule_group(random_string):
    """Create a new rule group and returns a rule group entity ID for following operations."""
    print("\n\t\tCREATING NEW RULE GROUP...")

    response = mgmt.create_rule_group(
        description="test rule group",
        enabled=True,
        name=f"fw-sample-test-group-{random_string}"
    )

    rule_group_id = response["body"]["resources"][0]

    print(f"API Responded: {response['status_code']}")
    print(response["body"])
    print("New Rule Group ID: "+rule_group_id)

    return rule_group_id


def get_rule_group_details(group_id):
    """Retrieve details of new rule group created at the start of execution.

    Returns tracking number required for modifications.
    """
    print("\n\t\tGETTING NEW RULE GROUP DETAILS...")

    response = mgmt.get_rule_groups(group_id)
    tracking_number = response["body"]["resources"][0]["tracking"]
    ids = response["body"]["resources"][0]["rule_ids"]

    print(f"API Responded: {response['status_code']}")
    print(response["body"])
    print(f"Tracking Number: {tracking_number}")

    return tracking_number, ids


def add_new_rule(group_id, tracking_number, rule_id_buffer, i):
    """Add a new rule to the new rule group.

    This rule is stored in the RULES variable defined at start of script.
    """
    print(f"\n\t\tADDING NEW RULE TO GROUP {group_id}...")

    if len(rule_id_buffer) < 1:
        rule_ids = [str(i+1)]
    else:
        rule_ids = rule_id_buffer + [(str(i+1))]

    response = mgmt.update_rule_group(
        id=group_id,
        diff_type="application/json-patch+json",
        diff_operations=DIFFS[i],
        rule_ids=rule_ids,
        rule_versions=[1],
        comment="updating test rule group",
        tracking=tracking_number
    )

    print(f"API Responded: {response['status_code']}")
    print(response["body"])


def reorder_rules(group_id, tracking_number, rule_id_buffer):
    """Reverse rules in new rule group.

    Implemented to demonstrate rule-reordering via API.
    """
    print(f"\n\t\tREORDERING RULES IN GROUP {group_id}...")

    reversed_rules = rule_id_buffer[::-1]
    response = mgmt.update_rule_group(
        id=group_id,
        rule_ids=reversed_rules,
        tracking=tracking_number
    )

    print(f"API Responded: {response['status_code']}")
    print(response["body"])


def modify_rules(group_id, tracking_number, rule_id_buffer):
    """Modify existing rules in new rule group.

    The difference is defined in the DIFFS variable.
    """
    print(f"\n\t\tMODIFYING RULES IN GROUP {group_id}...")

    response = mgmt.update_rule_group(
        id=group_id,
        diff_type="application/json-patch+json",
        diff_operations=DIFFS[2:4],
        rule_ids=rule_id_buffer,
        rule_versions=[2, 2],
        comment="modifying test rule group",
        tracking=tracking_number
    )

    print(f"API Responded: {response['status_code']}")
    print(response["body"])


def remove_rule(group_id, tracking_number, rule_id_buffer):
    """Remove the first rule from the group."""
    print(f"\n\t\tREMOVING RULE[0] IN GROUP {group_id}...")

    trimmed_ids = rule_id_buffer[:1]

    response = mgmt.update_rule_group(
        id=group_id,
        diff_type="application/json-patch+json",
        diff_operations=DIFFS[4],
        rule_ids=trimmed_ids,
        rule_versions=[0, 2],
        comment="removing rule 1",
        tracking=tracking_number
    )

    print(f"API Responded: {response['status_code']}")
    print(response["body"])


def remove_rule_group(rule_group_id):
    """Remove the rule group first created in this script."""
    print(f"\n\t\tREMOVING RULE GROUP: {rule_group_id}...")

    response = mgmt.delete_rule_groups(ids=rule_group_id)

    print(f"API Responded: {response['status_code']}")
    print(response["body"])


def parse_command_line():
    """Parse the passed command line and returns the created Namespace object."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-k", "--key",
                        help="Falcon API Client ID",
                        default=os.getenv("FALCON_CLIENT_ID")
                        )
    parser.add_argument("-s", "--secret",
                        help="Falcon API Client secret",
                        default=os.getenv("FALCON_CLIENT_SECRET")
                        )

    parsed = parser.parse_args()
    if not parsed.key or not parsed.secret:
        parser.error(
            "You must provide valid API credentials ('-k' and '-s') in order to use this program."
            )

    return parsed


def main():
    """Execute all the methods defined in this script to demonstrate firewall management APIs."""
    random_string = SystemRandom().randrange(1, 10000)
    new_rule_group_id = create_rule_group(random_string)

    tracking_number, rule_id_buffer = get_rule_group_details(new_rule_group_id)
    add_new_rule(new_rule_group_id, tracking_number, rule_id_buffer, 0)

    tracking_number, rule_id_buffer = get_rule_group_details(new_rule_group_id)
    add_new_rule(new_rule_group_id, tracking_number, rule_id_buffer, 1)

    tracking_number, rule_id_buffer = get_rule_group_details(new_rule_group_id)
    reorder_rules(new_rule_group_id, tracking_number, rule_id_buffer)

    tracking_number, rule_id_buffer = get_rule_group_details(new_rule_group_id)
    modify_rules(new_rule_group_id, tracking_number, rule_id_buffer)

    tracking_number, rule_id_buffer = get_rule_group_details(new_rule_group_id)
    remove_rule(new_rule_group_id, tracking_number, rule_id_buffer)
    get_rule_group_details(new_rule_group_id)

    remove_rule_group(new_rule_group_id)


# Retrieve our provided command line arguments
args = parse_command_line()
client_id = args.key
client_secret = args.secret
mgmt = FirewallManagement(client_id=client_id, client_secret=client_secret)


if __name__ == "__main__":
    main()
