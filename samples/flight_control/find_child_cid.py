"""Identify CID for a child host.

 _______ __ __       __    __    _______             __              __
|   _   |  |__.-----|  |--|  |_ |   _   .-----.-----|  |_.----.-----|  |
|.  1___|  |  |  _  |     |   _||.  1___|  _  |     |   _|   _|  _  |  |
|.  __) |__|__|___  |__|__|____||.  |___|_____|__|__|____|__| |_____|__|
|:  |         |_____|           |:  1   |
|::.|                           |::.. . |
`---'                           `-------'


This solution leverages the Flight Control and Hosts APIs.
Recommended version: FalconPy v0.8.6+

Creation date: 01.07.2021 - jshcodes@CrowdStrike

You will need the following scopes on your API keys:
    Flight Control: READ
    Hosts: READ
"""
import argparse
from falconpy import Hosts, FlightControl, OAuth2


def parse_command_line() -> object:
    """Parse the command line for inbound configuration parameters."""
    parser = argparse.ArgumentParser(description="Falcon Flight Control child host CID lookup.")
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
        help='CrowdStrike API region (us1, us2, eu1, usgov1)'
        ' NOT required unless you are using `usgov1`',
        required=False,
        default="auto"
    )
    parser.add_argument(
        '-f',
        '--find_host',
        help='Hostname or Device ID to identify',
        required=True
    )
    return parser.parse_args()


args = parse_command_line()
BASE = args.base_url

HOSTNAME = args.find_host

mssp = FlightControl(client_id=args.client_id, client_secret=args.client_secret, base_url=BASE)

children = mssp.query_children()
if children["status_code"] == 200:
    if children["body"]["resources"]:
        CIDS = children["body"]["resources"]
        AUTH = []
        for cid in CIDS:
            AUTH.append(
                OAuth2(client_id=args.client_id,
                       client_secret=args.client_secret, base_url=BASE,
                       member_cid=cid
                       )
            )
        for auth in AUTH:
            hosts = Hosts(auth_object=auth)
            lookup = hosts.query_devices_by_filter(filter=f"hostname:'{HOSTNAME}',device_id:'{HOSTNAME}'")
            if lookup["body"]["resources"]:
                for host in lookup["body"]["resources"]:
                    detail = hosts.get_device_details(ids=host)
                    host_cid = detail["body"]["resources"][0]["cid"]
                    print(f"Host identified on CID: {host_cid}")
    else:
        print("No children identified.")
else:
    print("No children identified, check permissions.")
