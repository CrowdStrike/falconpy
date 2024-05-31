#!/usr/bin/env python3
r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

 _   _           _       _____                     _
| | | |         | |     /  ___|                   | |
| |_| | ___  ___| |_    \ `--.  ___  __ _ _ __ ___| |__
|  _  |/ _ \/ __| __|    `--. \/ _ \/ _` | '__/ __| '_ \
| | | | (_) \__ \ |_    /\__/ /  __/ (_| | | | (__| | | |
\_| |_/\___/|___/\__|   \____/ \___|\__,_|_|  \___|_| |_|

This script will take a file listing of hostnames (one host per line) or
a single hostname provided at runtime to produce a CSV containing the 
details for hosts that are found. This solution can be used to compare a
list of hostnames to the list of hosts in the Falcon Console to determine
which hostnames are not currently reporting in to the console.

Developed by @Don-Swanson-Adobe
Modification: 05.28.24 - David M. Berry - Updated get_hostnames function to ignore comments.
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import Hosts


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-f", "--hostname_file",
                        help="Text file containing hostnames to search for",
                        default="hostnames.txt"
                        )
    parser.add_argument("-n", "--hostname",
                        help="Hostname to search for",
                        default=None
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


def get_hostnames(target_file: str):
    """Open file and import hostnames, ignoring comments."""
    try:
        with open(target_file, 'r') as host_file:
            print("Opening hostname file")
            hostnames = []
            for line in host_file:
                line = line.split('#')[0].strip()  # Remove comments and strip whitespace
                if line:  # Ignore empty lines
                    hostnames.append(line)
            return hostnames
    except FileNotFoundError:
        raise SystemExit(
            "You must provide a valid hostname file with the '-f' argument, "
            "or a host with the '-n' argument in order to run this program."
            )


cmd_line = consume_arguments()

# Activate debugging if requested
if cmd_line.debug:
    logging.basicConfig(level=logging.DEBUG)

# Create our list of hostnames to search for
hostnames = []
if not cmd_line.hostname:
    # They didn't give us a hostname, look for a hostname file
    hostnames.extend(get_hostnames(cmd_line.hostname_file))
else:
    hostnames.append(cmd_line.hostname)

# Setup constants and successfully identified hostname list
BATCH_SIZE = 250
found = []

# Connect to the API using a context handler for automatic logout and enable pythonic responses
with Hosts(client_id=cmd_line.client_id,
               client_secret=cmd_line.client_secret,
               debug=cmd_line.debug,
               pythonic=True
               ) as falcon:
    # Use a context handler to open our file so closing it later happens automagically
    with open(cmd_line.output_path, 'a+') as file_object:
        file_object.write("Hostname,CID,RFM,Last Seen,Landscape,Tag1,Tag2,Tag3,Tag4\n")
        for batch in [hostnames[i:i+BATCH_SIZE] for i in range(0, len(hostnames), BATCH_SIZE)]:
            # Get AIDs for matching hostnames. Exact matches only.
            host_ids = falcon.query_devices_by_filter(filter=f"hostname:{batch}")
            if host_ids:
                # Get and write details for those hosts (use the data parameter iterable)
                for device in falcon.get_device_details(ids=host_ids.data):
                    hostname = device["hostname"]
                    last_seen = device["last_seen"]
                    rfm = device["reduced_functionality_mode"]
                    cid = device["cid"]
                    tags = device["tags"]
                    tag = ""
                    for tag_string in tags:
                        tag += tag_string.replace('SensorGroupingTags/','')
                        tag += ","
                    file_object.write(hostname+","+cid+","+rfm+","+last_seen+","+tag+"\n")
                    found.append(hostname)
        # Compare to the original list
        not_found = [x for x in hostnames if x not in set(found)]
        for host in not_found:
            file_object.write(host+",HOST NOT FOUND\n")

print(f"Search complete, results have been written to {cmd_line.output_path}")
