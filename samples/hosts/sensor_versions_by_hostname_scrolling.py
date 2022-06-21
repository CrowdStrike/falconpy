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
        '-m',
        '--mssp',
        help='Child CID to access (MSSP only)',
        required=False
        )
    parser.add_argument(
        '-b',
        '--base_url',
        help='CrowdStrike API region (us1, us2, eu1, usgov1).'
        ' NOT required unless you are using `usgov1`.',
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
    result = falcon.query_devices_by_filter_scroll(limit=limit, offset=off, sort=sort)
    new_offset = 0
    total = 0
    returned_device_list = []
    if result["status_code"] == 200:
        new_offset = result["body"]["meta"]["pagination"]["offset"]
        total = result["body"]["meta"]["pagination"]["total"]
        returned_device_list = result["body"]["resources"]

    return new_offset, total, returned_device_list

def device_detail(aids: list):
    """Return the device_id and agent_version for a list of AIDs provided."""
    result = falcon.get_device_details(ids=aids)
    device_details = []
    if result["status_code"] == 200:
        # return just the aid and agent version
        for device in result["body"]["resources"]:
            res = {}
            res["hostname"] = device.get("hostname", None)
            res["agent_version"] = device.get("agent_version", None)
            device_details.append(res)
    return device_details


args = parse_command_line()

BASE = "auto"
if args.base_url:
    BASE = args.base_url

SORT = "hostname.asc"
if args.reverse:
    SORT = "hostname.desc"

CHILD = None
if args.mssp:
    CHILD = args.mssp

falcon = Hosts(client_id=args.client_id,
               client_secret=args.client_secret,
               base_url=BASE,
               member_cid=CHILD
               )

OFFSET = None   # First time the token is null
DISPLAYED = 0   # Running count
TOTAL = 1       # Assume there is at least one
LIMIT = 500     # Quick limit to prove pagination
offset_pos = 0  # Start at the beginning
while offset_pos < TOTAL:
    OFFSET, TOTAL, devices = device_list(OFFSET, LIMIT, SORT)
    offset_pos += LIMIT
    details = device_detail(devices)
    for detail in details:
        DISPLAYED += 1
        print(f"{DISPLAYED}: {detail['hostname']} is on version {detail['agent_version']}")

if not DISPLAYED:
    print("No results returned.")
