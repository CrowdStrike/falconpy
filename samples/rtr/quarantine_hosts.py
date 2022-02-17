#  _   _           _
# | | | | ___  ___| |_ ___
# | |_| |/ _ \/ __| __/ __|
# |  _  | (_) \__ \ |_\__ \
# |_| |_|\___/|___/\__|___/
#
# This example demonstrates how to apply or lift containment on a host using its hostname.
# This solution makes use of Service Class legacy authentication.
#
import json
import argparse
# Import necessary FalconPy classes
from falconpy import oauth2 as FalconAuth
from falconpy import hosts as FalconHosts

# Setup our argument parser
parser = argparse.ArgumentParser("Script that leverages Falcon API to (un)contain hosts")
parser.add_argument('-c', '--creds_file', dest='creds_file', help='Path to creds json file', required=True)
parser.add_argument('-H', '--hostname', dest='hostname', help='Hostname to quarantine', required=True)
parser.add_argument('-l', '--lift', dest='lift_containment', action="store_true", help='Lift containment', default=False)
# Parse our ingested arguments
args = parser.parse_args()
# Hostname of the machine to contain / release
hostname = args.hostname
# Default action is to quarantine
if args.lift_containment:
    action = "lift_containment"
else:
    action = "contain"
# Use the credentials file provided
creds_file = args.creds_file
# Load the contents of the creds file into the creds dictionary
with open(creds_file) as f:
    creds = json.load(f)
# Create an instance of our OAuth2 authorization class using our ingested creds
authorization = FalconAuth.OAuth2(creds={
                "client_id": creds['falcon_client_id'],
                "client_secret": creds['falcon_client_secret']
    })
# Try to generate a token
try:
    token = authorization.token()['body']['access_token']
except Exception as e:
    # Exit out on authentication errors
    print("Failed to authenticate")
    print(e)
    exit(-1)
# If we have a token, proceed to the next step
if token:
    # Create an instance of the Hosts class
    falcon = FalconHosts.Hosts(access_token=token)
    # Create our parameter payload, using our ingested hostname as a filter
    PARAMS = {
        'offset': 0,
        'limit': 10,
        'filter': f"hostname:'{hostname}'"
    }
    # Query the Hosts API for hosts that match our filter pattern
    response = falcon.QueryDevicesByFilter(parameters=PARAMS)
    # Retrieve the list of IDs returned
    contain_ids = response['body']['resources']
    # Output the result
    print(json.dumps(response, indent=4))

    if not contain_ids:
        # No hosts were found, exit out
        print(f"[-] Could not find hostname: {hostname} - Please verify proper case")
        exit(-2)

    # Create our next payload based upon the action requested
    PARAMS = {
        'action_name': action
    }
    # Our body payload will contain our list of IDs
    BODY = {
        'ids': contain_ids
    }
    # Provide a status update to the terminal
    if action == "contain":
        print(f"\n[+] Containing: {hostname}\n")
    else:
        print(f"\n[+] Lifting Containment: {hostname}\n")

    # Perform the requested action
    response = falcon.PerformActionV2(parameters=PARAMS, body=BODY)
    # Output the result
    print(json.dumps(response, indent=4))
