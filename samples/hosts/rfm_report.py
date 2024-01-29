#!/usr/bin/env python3
r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

██████  ███████ ███    ███     ██████  ███████ ██████   ██████  ██████  ████████
██   ██ ██      ████  ████     ██   ██ ██      ██   ██ ██    ██ ██   ██    ██
██████  █████   ██ ████ ██     ██████  █████   ██████  ██    ██ ██████     ██
██   ██ ██      ██  ██  ██     ██   ██ ██      ██      ██    ██ ██   ██    ██
██   ██ ██      ██      ██     ██   ██ ███████ ██       ██████  ██   ██    ██

This script was developed by developed by @Don-Swanson-Adobe to determine the
number of hosts in RFM (Up for more than 24 hours and seen within the last 24
hours) in your tenant or every child tenant attached to your parent.

Developed by @Don-Swanson-Adobe
"""
import os
import logging
from datetime import datetime, timedelta
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import APIHarnessV2


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-m", "--mssp",
                        help="Return RFM details for child CIDs (MSSP parents only).",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-o", "--output_path",
                        help="Location to store CSV output",
                        default="RFM_Report.csv"
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
    parsed = parser.parse_args()
    if not parsed.client_id or not parsed.client_secret:
        parser.error("You must provide CrowdStrike API credentials using the '-k' and '-s' arguments.")

    return parsed


# Consume the command line
cmd_line = consume_arguments()
if cmd_line.debug:
    # Activate debugging if requested
    logging.basicConfig(level=logging.DEBUG)

# Establish 24 hours ago as the last seen time, setup the output file,
# and the variable to store which serial numbers we found
last = (datetime.now() - timedelta(hours = 24)).strftime('%Y-%m-%dT%H:%M:%SZ')
file_object = open(cmd_line.output_path, 'a+')
file_object.write("CID,Hostname,AID,Last Seen,RFM,OS,Kernel,Sensor Version,Tag1,Tag2,Tag3,Tag4\n")
filter_string = f"last_seen:>='{last}'+first_seen:<='{last}'+reduced_functionality_mode:'yes'"
rfm_total=0
if cmd_line.mssp:
    # Retrieve the list of child CIDs if we're in MSSP mode
    parent = APIHarnessV2(client_id=cmd_line.client_id,
                          client_secret=cmd_line.client_secret,
                          debug=cmd_line.debug
                          )
    cids = parent.command("queryChildren")["body"]["resources"]
else:
    # Just check my tenant
    cids = ["My tenant"]

# Do the needful for each CID in the list
for key in cids:
    auth = {
        "client_id": cmd_line.client_id,
        "client_secret": cmd_line.client_secret,
        "debug": cmd_line.debug
    }
    if key != "My tenant":
        auth["member_cid"] = key
    falcon = APIHarnessV2(**auth)
    response = falcon.command("QueryDevicesByFilter", filter=filter_string)
    if "resources" in response['body']:
        total = response["body"]["meta"]["pagination"]["total"]
        rfm_total += total
        off = 0
        while total > 0:
            response = falcon.command("QueryDevicesByFilter",
                        offset=off,
                        limit=500,
                        sort="device_id.asc",
                        filter=filter_string
                        )
            aids = response["body"]["resources"]
            hosts = falcon.command("GetDeviceDetails", ids=aids)["body"]["resources"]
            if hosts is not None:
                for info in hosts:
                    hostname = (info["hostname"])
                    aid = (info["device_id"])
                    last_seen = (info["last_seen"])
                    rfm = (info["reduced_functionality_mode"])
                    os_version = (info["os_version"])
                    kernel = (info["kernel_version"])
                    tags = (info["tags"])
                    agent_version = (info["agent_version"])
                    tag = ""   
                    for t in tags:
                        tag += t.replace('SensorGroupingTags/','')
                        tag += ","
                    file_object.write(key+","+hostname+","+aid+","+last_seen+","+rfm+","+os_version+","+kernel+","+agent_version+","+tag+"\n")
            total -= 500
            off += 500
                     
file_object.close()
print(f"Total hosts identified as in Reduced Functionality Mode: {rfm_total}")