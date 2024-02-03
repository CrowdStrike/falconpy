#!/usr/bin/env python3
r"""Sensor restart utility.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

  )\.--.   )\.---.   )\  )\    )\.--.     .-./(     /`-.
 (   ._.' (   ,-._( (  \, /   (   ._.'  ,'     )  ,' _  \
  `-.`.    \  '-,    ) \ (     `-.`.   (  .-, (  (  '-' (
 ,_ (  \    ) ,-`   ( ( \ \   ,_ (  \   ) '._\ )  ) ,_ .'
(  '.)  )  (  ``-.   `.)/  ) (  '.)  ) (  ,   (  (  ' ) \
 '._,_.'    )..-.(      '.(   '._,_.'   )/ ._.'   )/   )/

   /`-.   )\.---.    )\.--.  .-,.-.,-.    /`-.      /`-.  .-,.-.,-.
 ,' _  \ (   ,-._(  (   ._.' ) ,, ,. (  ,' _  \   ,' _  \ ) ,, ,. (
(  '-' (  \  '-,     `-.`.   \( |(  )/ (  '-' (  (  '-' ( \( |(  )/
 ) ,_ .'   ) ,-`    ,_ (  \     ) \     )   _  )  ) ,_ .'    ) \
(  ' ) \  (  ``-.  (  '.)  )    \ (    (  ,' ) \ (  ' ) \    \ (
 )/   )/   )..-.(   '._,_.'      )/     )/    )/  )/   )/     )/

This program creates a RTR Session, drops a script on the host, runs
the script, and then finally retrieves the output. The script will start
TCPdump and perform a capture while the Falcon Sensor is restarted.

Developed by @Don-Swanson-Adobe, modified by jshcodes@CrowdStrike

Requirements:
    crowdstrike-falconpy >= 1.3.0
    py7zr
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from enum import Enum
from time import sleep
import py7zr
from falconpy import APIHarnessV2, APIError, Result


class WHAT_IS_THE(Enum):
    """Dodge bandit's silliness."""
    MAGIC_WORD = "infected"


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    req = parser.add_argument_group("Required arguments")
    req.add_argument("-k", "--client_id",
                     help="CrowdStrike Falcon API key",
                     default=os.getenv("FALCON_CLIENT_ID")
                     )
    req.add_argument("-s", "--client_secret",
                     help="CrowdStrike Falcon API secret",
                     default=os.getenv("FALCON_CLIENT_SECRET")
                     )
    hid = req.add_mutually_exclusive_group(required=True)
    hid.add_argument("-a", "--aid",
                     help="Endpoint AID",
                     default=None
                     )
    hid.add_argument("-n", "--hostname",
                     help="Endpoint Hostname",
                     default=None
                     )

    parsed = parser.parse_args()
    if not parsed.client_id or not parsed.client_secret:
        parser.error("You must provide CrowdStrike API credentials using the '-k' and '-s' arguments.")

    return parsed


def do_command(base_command: str, command_string: str, session_id: str) -> Result:
    """Craft the command body payload, execute the API operation, and return the result object."""
    body_payload = {
        "base_command": base_command,
        "command_string": command_string,
        "persist": True,
        "session_id": session_id
    }
    try:
        return falcon.command("RTR_ExecuteAdminCommand", body=body_payload)
    except APIError as api_error:
        raise SystemExit(api_error)


DUMP_SCRIPT = """#!/bin/bash
hostname=$(hostname)
echo "Starting capture"
tcpdump -G 60 -W 1 -w tcpdump-$hostname.pcap &
sleep 10
systemctl stop falcon-sensor
sleep 5
systemctl start falcon-sensor
sleep 45
echo "Capture Complete!"
"""


# Consume any command line arguments
cmd_line = consume_arguments()

# Activate debugging if requested
if cmd_line.debug:
    logging.basicConfig(level=logging.DEBUG)

# Create our base authentication dictionary
auth = {
    "client_id": cmd_line.client_id,
    "client_secret": cmd_line.client_secret,
    "debug": cmd_line.debug,
    "pythonic": True
}

endpoint_aid = ""
endpoint_cid = ""
endpoint_hostname = ""
this_cid = ""
script = "remote_tcp_dump.sh"
falcon = APIHarnessV2(**auth)
try:
    this_cid = falcon.command("GetSensorInstallersCCIDByQuery").data[0][:-3].lower()
except APIError as api_error:
    # They do not have access to the sensor downloads service collection with this key
    raise SystemExit("The Sensor Download scope required to run this program.")

if cmd_line.hostname:
    endpoint_hostname = cmd_line.hostname
    endpoint_aid = falcon.command("QueryDevicesByFilterScroll",
                                    filter=f"hostname:'{endpoint_hostname}'"
                                    ).data[0]
    if not endpoint_aid:
        raise SystemExit("The hostname was not found.")
else:
    endpoint_aid = cmd_line.aid
try:
    endpoint = falcon.command("GetDeviceDetails", ids=endpoint_aid).data[0]
    endpoint_cid = endpoint["cid"]
    endpoint_hostname = endpoint["hostname"]
except APIError as api_error:
    raise SystemExit(api_error.message)


if endpoint_cid != this_cid:
    auth["member_cid"] = endpoint_cid

falcon = APIHarnessV2(**auth)
# Initiate the session
init_payload = {"device_id": endpoint_aid, "queue_offline": True}
try:
    session = falcon.command("RTR_InitSession", body=init_payload).data[0]["session_id"]
except APIError as api_error:
    raise SystemExit(api_error.message)
except (IndexError, KeyError):
    raise SystemExit("Unable to initiate session with endpoint.")
print("Session initialized")
# Check for the existence of the TCP dump script
script_id = falcon.command("RTR_ListScripts", filter=f"name:'{script}'").data
if not script_id:
    # The script doesn't exist, create it
    script_data = {
        "name": script,
        "content": DUMP_SCRIPT,
        "platform": "linux",
        "permission_type": "private",
        "description": f"Run a TCP dump while restarting the sensor"
    }
    falcon.command("RTR_CreateScripts",
                   data=script_data,
                   files=[(script, (script, 'application/script'))]
                   )
    # Grab the script's ID so we can remove it later
    script_id = falcon.command("RTR_ListScripts", filter=f"name:'{script}'").data

print("Uploading script to endpoint")
# "PUT" the script onto the endpoint
response = do_command("put", f"put {script}", session)
if response.status_code != 201:
    raise SystemExit("ERROR: Unable to drop script on target endpoint")
sleep(5)

# Set script execution permissions
response = do_command("runscript", f"runscript -Raw=```chmod +x ./{script}```", session)
if response.status_code != 201:
    raise SystemExit("ERROR: Unable to set script file permissions")

# Execute the script using systemd-run to ensure the script continues to run after the sensor is stopped
response = do_command("runscript", "runscript -Raw=```systemd-run ./"+script+"```", session)
if response.status_code != 201:
    raise SystemExit("ERROR: Script execution failed")

print("Script execution takes approximately 90 seconds, please wait...")
for counter in range(1, 91):
    print(f" {counter} second{'s' if counter > 1 else ''}", end="\r")
    sleep(.9)

print("Retrieving results")
# Get the output File
response = do_command("get", f"get tcpdump-{endpoint_hostname}.pcap", session)
if response.status_code != 201:
    raise SystemExit("ERROR: Unable to retrieve TCP dump")
cloud_request_id = response.data[0]["cloud_request_id"]
upload_complete = False
while not upload_complete:
    upload_complete = falcon.command("RTR_CheckAdminCommandStatus",
                                     cloud_request_id=cloud_request_id,
                                     sequence_id=0
                                     ).data[0]["complete"]
    print(" Waiting on upload to complete", end="\r")
try:
    file_id = falcon.command("RTR_ListFiles", session_id=session)[0]["sha256"]
except IndexError:
    raise SystemExit("Unable to retrieve TCP dump results")
try:
    with open(f"tcpdump-{endpoint_hostname}.7z", "wb") as dump_file:
        dump_file.write(falcon.command("RTR_GetExtractedFileContents",
                                       sha256=file_id,
                                       session_id=session,
                                       filename=f"tcpdump-{endpoint_hostname}.pcap"
                                       ).full_return)
except APIError as api_error:
    raise SystemExit(api_error.message)

print(f"Extracting results{' ' * 12}")
# Open our downloaded archive
archive = py7zr.SevenZipFile(f"tcpdump-{endpoint_hostname}.7z",
                             mode="r",
                             password=WHAT_IS_THE["MAGIC_WORD"].value
                             )
archive.extractall()
archive.close()

# Remove the 7zip archive
os.remove(f"tcpdump-{endpoint_hostname}.7z")

print("Cleaning up")
# Remove the dump file from the endpoint
response = do_command("rm", f"rm tcpdump-{endpoint_hostname}.pcap", session)
if response.status_code != 201:
    print("ERROR: Unable to remove TCP dump from endpoint")

# Remove the dump script from the endpoint
response = do_command("rm", f"rm {script}", session)
if response.status_code != 201:
    print("ERROR: Unable to remove dump script from endpoint")

# Delete the uploaded dump script
try:
    falcon.command("RTR_DeleteScripts", ids=script_id)
except APIError as api_error:
    print("Unable to remove TCP dump script from CrowdStrike cloud")

# Delete the RTR session
falcon.command("RTR_DeleteSession", session_id=session)

print(f"Procedure complete, TCP dump results saved to tcpdump-{endpoint_hostname}.pcap")
