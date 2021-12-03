"""This sample demonstrates retrieving sensor versions by hostname.

This example requires FalconPy v0.8.6+
"""
import argparse
from falconpy import Hosts


def parse_command_line() -> object:
    """Parses command-line arguments and returns them back as an object."""
    parser = argparse.ArgumentParser(description="List sensors versions by hostname")
    parser.add_argument(
        '-k',
        '--client_id',
        help='CrowdStrike Falcon API key ID',
        required=True
        )
    parser.add_argument(
        '-s',
        '--client_secret',
        help='CrowdStrike Falcon API key secret',
        required=True
        )
    parser.add_argument(
        '-b',
        '--base_url',
        help='CrowdStrike API region (us1, us2, eu1, usgov1).'
        ' NOT required unless you are on usgov1.',
        required=False
    )
    parser.add_argument(
        '-r',
        '--reverse',
        help='Reverse sort (defaults to ASC)',
        required=False,
        action="store_true"
        )

    return parser.parse_args()


def device_list(off: int, limit: int, sort: str):
    """Return a list of all devices for the CID, paginating when necessary."""
    result = falcon.query_devices_by_filter(limit=limit, offset=off, sort=sort)
    new_offset = result["body"]["meta"]["pagination"]["offset"]
    total = result["body"]["meta"]["pagination"]["total"]
    returned_device_list = result["body"]["resources"]
    return new_offset, total, returned_device_list


def device_detail(aids: list):
    """Return the device_id and agent_version for a list of AIDs provided."""
    result = falcon.get_device_details(ids=aids)
    device_details = []
    # return just the aid and agent version
    for device in result["body"]["resources"]:
        res = {}
        res["hostname"] = device.get("hostname", None)
        res["agent_version"] = device.get("agent_version", None)
        device_details.append(res)
    return device_details


args = parse_command_line()

if args.base_url:
    BASE = args.base_url
else:
    BASE = "us1"

if args.reverse:
    SORT = "hostname.desc"
else:
    SORT = "hostname.asc"

falcon = Hosts(client_id=args.client_id,
               client_secret=args.client_secret,
               base_url=BASE
               )

OFFSET = 0      # Start at the beginning
DISPLAYED = 0   # This is just so we can show a running count
TOTAL = 1       # Assume there is at least one
LIMIT = 500     # Quick limit to prove pagination
while OFFSET < TOTAL:
    OFFSET, TOTAL, devices = device_list(OFFSET, LIMIT, SORT)
    details = device_detail(devices)
    for detail in details:
        DISPLAYED += 1
        print(f"{DISPLAYED}: {detail['hostname']} is on version {detail['agent_version']}")
