#!/usr/bin/env python3
r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

8¯¯¯¯8                               8¯¯¯¯8
8      eeee eeeee  e  eeeee e        8      eeee eeeee eeeee  eeee e   e
8eeeee 8    8   8  8  8   8 8        8eeeee 8    8   8 8   8  8  8 8   8
    88 8eee 8eee8e 8e 8eee8 8e           88 8eee 8eee8 8eee8e 8e   8eee8
e   88 88   88   8 88 88  8 88       e   88 88   88  8 88   8 88   88  8
8eee88 88ee 88   8 88 88  8 88eee    8eee88 88ee 88  8 88   8 88e8 88  8

This script takes a file listing Serial Numbers and outputs a CSV with the 
Serial Number, Hostname, CID, RFM, Last Seen, Local IP, and Tags for each 
host in the list. This list can be used to compare a list of serial numbers
to the list of hosts in the Falcon Console to determine which serial numbers
are not currently reporting to the console.

Developed by @Don-Swanson-Adobe
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from datetime import datetime, timedelta
from falconpy import Hosts


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-f", "--serial_file",
                        help="Text file contain serial numbers of hosts to tag",
                        default="serials.txt"
                        )
    parser.add_argument("-o", "--output_path",
                        help="Location to store CSV output",
                        default="output.csv"
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


def get_host_serials(target_file: str):
    """Open CSV and import serials."""
    try:
        with open(target_file, newline='') as serial_file:
            print("Opening serial file")
            return serial_file.read().splitlines()

    except FileNotFoundError:
        raise SystemExit(
            "You must provide a valid serial file with the '-f' argument in order to run this program."
            )


def diff_compare(source, found):
    """Function to determine which serial numbers couldn't be found."""
    s = set(found)
    li_dif = [x for x in source if x not in s]
    return li_dif


cmd_line = consume_arguments()
if cmd_line.debug:
    logging.basicConfig(level=logging.DEBUG)

# Setup the current last seen time as the last 72 hours
lastseen = (datetime.utcnow() - timedelta(hours = 72)).strftime('%Y-%m-%dT%H:%M:%SZ')

# Retrieve the list of serial numbers to process
serials = get_host_serials(cmd_line.serial_file)

# Chunk the list of serials into a usable size
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

# Setup the output file, and the variable to store which serial numbers we found
SORT = "hostname.asc"
file_object = open(cmd_line.output_path, 'a+')
file_object.write("Serial,Hostname,CID,RFM,Last Seen,Local IP,Tag1,Tag2,Tag3,Tag4\n")
found = []

# Setup the API Harness
falcon = Hosts(client_id=cmd_line.client_id,
               client_secret=cmd_line.client_secret,
               debug=cmd_line.debug
               )

# Chunk the Serial numbers into groups of 250
for group in chunker(serials, 250):    
    # Get AIDs for matching hosts
    host_ids = falcon.query_devices_by_filter(filter=f"serial_number:{group}")
    
    # Get and write details for those hosts. 
    devices = falcon.get_device_details(ids=host_ids["body"]["resources"])["body"]["resources"] 
    if devices is not None:
        for device in devices:
            if len(device):
                if device["last_seen"] >= lastseen:
                    hostname = device["hostname"]
                    last_seen = device["last_seen"]
                    rfm = device["reduced_functionality_mode"]
                    cid = device["cid"]
                    serial = device["serial_number"]
                    if "local_ip" in device:
                        local_ip = device["local_ip"]
                    else:
                        local_ip = "Unavailable"
                    tags = device["tags"]
                    tag = ""
                    for i in tags:
                        tag += i.replace('SensorGroupingTags/','')
                        tag += ","
                    file_object.write(serial+","+hostname+","+cid+","+rfm+","+last_seen+","+local_ip+","+tag+"\n")
                    found.append(serial)

# Compare to original list to determine which couldn't be found
print("Determining Hosts Not Found")
not_found = diff_compare(serials,found)
for host in not_found:
    file_object.write(host+",Serial NOT FOUND\n")

file_object.close()
