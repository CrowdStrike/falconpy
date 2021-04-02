import json
import argparse
from pprint import pprint
from falconpy import oauth2 as FalconAuth
from falconpy import hosts as FalconHosts

parser = argparse.ArgumentParser(
    "Script that leverages Falcon API to (un)contain hosts")
parser.add_argument('-c', '--creds_file', dest='creds_file',
                    help='Path to creds json file', required=True)
parser.add_argument('-H', '--hostname', dest='hostname',
                    help='Hostname to quarantine', required=True)
parser.add_argument('-l', '--lift', dest='lift_containment',
                    action="store_true", help='Lift containment',
                    default=False)

args = parser.parse_args()

hostname = args.hostname
if args.lift_containment:
    action = "lift_containment"
else:
    action = "contain"

creds_file = args.creds_file
with open(creds_file) as f:
    creds = json.load(f)

authorization = FalconAuth.OAuth2(creds={
                "client_id": creds['falcon_client_id'],
                "client_secret": creds['falcon_client_secret']
    })

try:
    token = authorization.token()['body']['access_token']
except Exception as e:
    print("Failed to authenticate")
    print(e)
    exit(-1)

if token:
    falcon = FalconHosts.Hosts(access_token=token)

    PARAMS = {
        'offset': 0,
        'limit': 10,
        'filter': f"hostname:'{hostname}'"
    }

    response = falcon.QueryDevicesByFilter(parameters=PARAMS)

    contain_ids = response['body']['resources']
    print()
    pprint(response)
    if not contain_ids:
        print(f"[-] Could not find hostname: {hostname} - Please verify \
                proper case")
        exit(-2)

    PARAMS = {
        'action_name': action
    }

    BODY = {
        'ids': contain_ids
    }

    if action == "contain":
        print(f"[+] Containing: {hostname}")
    else:
        print(f"[+] Lifting Containment: {hostname}")

    print()

    # TODO: Get rid of action_name="contain" once bug is resolved
    # BUG: https://github.com/CrowdStrike/falconpy/issues/114
    response = falcon.PerformActionV2(parameters=PARAMS, body=BODY,
                                      action_name="contain")
    pprint(response)
