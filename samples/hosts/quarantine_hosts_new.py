#  _   _           _
# | | | | ___  ___| |_ ___
# | |_| |/ _ \/ __| __/ __|
# |  _  | (_) \__ \ |_\__ \
# |_| |_|\___/|___/\__|___/
#
# 
# This is an updated example of the solution demonstrating host containment
# here: https://github.com/CrowdStrike/falconpy/blob/main/samples/rtr/quarantine_hosts.py
#
# This version requires FalconPy v0.8.0 or greater
#
# 02.22.22 - jshcodes@CrowdStrike, soggysec@CrowdStrike
import json
import argparse
from falconpy import Hosts

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
with open(creds_file) as file_creds:
    creds = json.load(file_creds)
# Create an instance of our OAuth2 authorization class using our ingested creds
falcon = Hosts(client_id=creds["falcon_client_id"], client_secret=creds["falcon_client_secret"])
# Query the Hosts API for hosts that match our filter pattern
response = falcon.query_devices_by_filter(filter=f"hostname:'{hostname}'", limit=10)
if response["status_code"] != 200:
    raise SystemExit("Unable to retrieve list of devices that match the hostname specified.")

# Retrieve the list of IDs returned
contain_ids = response["body"]["resources"]

if not contain_ids:
    # No hosts were found, exit out
    raise SystemExit(f"[-] Could not find hostname: {hostname} - Please verify proper case")

# Provide a status update to the terminal
if action == "contain":
    print(f"\n[+] Containing: {hostname}\n")
    blurb = "contained"
else:
    print(f"\n[+] Lifting Containment: {hostname}\n")
    blurb = "released"

# Perform the requested action
response = falcon.perform_action(ids=contain_ids, action_name=action)
if response["status_code"] == 202:
    for contained in response["body"]["resources"]:
        print(f"{hostname} [{contained['id']}] has been {blurb}.")
else:
    error_list = response["body"]["errors"]
    for err in error_list:
        ecode = err["code"]
        emsg = err["message"]
        print(f"[{ecode}] {emsg}")

