#!/usr/bin/env python3
r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

  _   _           _     ____                      _      
 | | | | ___  ___| |_  / ___|  ___  __ _ _ __ ___| |__   
 | |_| |/ _ \/ __| __| \___ \ / _ \/ _` | '__/ __| '_ \  
 |  _  | (_) \__ \ |_   ___) |  __/ (_| | | | (__| | | | 
 |_| |_|\___/|___/\__| |____/ \___|\__,_|_|  \___|_| |_| 
     _       _                               _           
    / \   __| |_   ____ _ _ __   ___ ___  __| |          
   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` |          
  / ___ \ (_| |\ V / (_| | | | | (_|  __/ (_| |          
 /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_|          
                                                         

This script will take a file listing of hostnames (one host per line) or
a single hostname provided at runtime to produce a CSV containing the 
details for hosts that are found. This solution can be used to compare a
list of hostnames to the list of hosts in the Falcon Console to determine
which hostnames are not currently reporting in to the console, or to discover hosts based on a partial match of the hostname. Comments in input files are also ommitted from lookup, thus keeping the output.csv clean, and allowing you to work with more useful host name files/inventory.

Developed by @Don-Swanson-Adobe, additional functionality by @David-M-Berry
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
    parser.add_argument("-n", "--hostname",
                        help="Hostname to search for",
                        required=False  # Make this argument optional
                        )
    parser.add_argument("-i", "--input_file",  # Add a new argument for input file
                        help="Text file containing hostnames to search for"
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


def process_hostnames(hostnames):
    with open(cmd_line.output_path, 'w') as file_object:  # Open in 'write' mode to clear previous content
        with Hosts(client_id=cmd_line.client_id,
                   client_secret=cmd_line.client_secret,
                   debug=cmd_line.debug,
                   pythonic=True
                   ) as falcon:
            for hostname in hostnames:
                host_ids = falcon.query_devices_by_filter(filter=f"hostname:*'*{hostname}*'")
                if host_ids:
                    for device in falcon.get_device_details(ids=host_ids.data):
                        device_hostname = device["hostname"]
                        last_seen = device["last_seen"]
                        rfm = device["reduced_functionality_mode"]
                        cid = device["cid"]
                        tags = device["tags"]
                        tag = ",".join(tag_string.replace('SensorGroupingTags/', '') for tag_string in tags)
                        file_object.write(f"{device_hostname},{cid},{rfm},{last_seen},{tag}\n")
                else:
                    file_object.write(f"{hostname},HOST NOT FOUND\n")
    
    # Deduplicate the output file
    deduplicate_output(cmd_line.output_path)
    print(f"Search complete, results have been written to {cmd_line.output_path}")


def deduplicate_output(output_path):
    """Remove duplicate entries from the output file."""
    with open(output_path, 'r') as file:
        lines = file.readlines()
    unique_lines = set(lines)
    with open(output_path, 'w') as file:
        file.writelines(unique_lines)


def prepend_header(output_path):
    """Prepend the header line to the output file."""
    with open(output_path, 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        file.write("Hostname,CID,RFM,Last Seen,Landscape,Tag1,Tag2,Tag3,Tag4\n" + content)


cmd_line = consume_arguments()

if cmd_line.hostname:
    hostnames = [cmd_line.hostname]
elif cmd_line.input_file:
    with open(cmd_line.input_file, 'r') as file:
        hostnames = []
        for line in file:
            line = line.split('#')[0].strip()  # Remove comments and strip whitespace
            if line:  # Ignore empty lines
                hostnames.append(line)
else:
    print("You must provide either a hostname or an input file.")
    exit(1)


if cmd_line.debug:
    logging.basicConfig(level=logging.DEBUG)

process_hostnames(hostnames)
prepend_header(cmd_line.output_path)
