#!/usr/bin/env python3
r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'
 __ __   ___    _____ ______  _____     ______   ____   ____   ____    ___  ____
|  T  T /   \  / ___/|      T/ ___/    |      T /    T /    T /    T  /  _]|    \
|  l  |Y     Y(   \_ |      (   \_     |      |Y  o  |Y   __jY   __j /  [_ |  D  )
|  _  ||  O  | \__  Tl_j  l_j\__  T    l_j  l_j|     ||  T  ||  T  |Y    _]|    /
|  |  ||     | /  \ |  |  |  /  \ |      |  |  |  _  ||  l_ ||  l_ ||   [_ |    \
|  |  |l     ! \    |  |  |  \    |      |  |  |  |  ||     ||     ||     T|  .  Y
l__j__j \___/   \___j  l__j   \___j      l__j  l__j__jl___,_jl___,_jl_____jl__j\_j

This script was developed by @Don-Swanson-Adobe to bulk assign or remove a Falcon
Grouping Tag against a list of hosts based on their serial number.

Developed by @Don-Swanson-Adobe
"""
import os
import logging
from falconpy import APIHarnessV2
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace


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
    parser.add_argument("-t", "--tag", help="String to use for the Falcon Tag", default="TEST_TAG")
    parser.add_argument("-r", "--remove",
                        help="Remove tag instead of applying it",
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
    parsed = parser.parse_args()
    if not parsed.client_id or not parsed.client_secret:
        parser.error("You must provide CrowdStrike API credentials using the '-k' and '-s' arguments.")

    return parsed


def get_host_serials(target_file: str):
    """Open CSV and import serials."""
    try:
        with open(target_file, newline='') as serial_file:
            print("Opening serial file")
            return serial_file.read().split("\n")

    except FileNotFoundError:
        raise SystemExit(
            "You must provide a valid serial file with the '-f' argument in order to run this program."
            )


def process_hosts(numbers: list):
    """Process the retrieved serial numbers and apply the tags."""
    # Get AID and assign tag for each serial
    print("Getting AID")
    max_query_terms = 20  # Maximum number of FQL query terms allowed
    host_batches = [numbers[i:i+max_query_terms] for i in range(0, len(numbers), max_query_terms)]
    for host_batch in host_batches:  # Loop through each batch of 1-20
        filter_string = ""
        for host in [h for h in host_batch if h]:  # And create a host filter that includes all hosts
            filter_string = f"{filter_string},serial_number:'{host}'"
        filter_string = filter_string[1:]

        response = falcon.command("QueryDevicesByFilterScroll", filter=filter_string)
        if len(response["body"]["resources"]):
            aids = response["body"]["resources"]
            action = "add" if not cmd_line.remove else "remove"
            BODY = {"action": action, "device_ids": aids, "tags": [grouping_tag]}
            response = falcon.command("UpdateDeviceTags", body=BODY)
            for result in response["body"]["resources"]:
                if result["updated"]:
                    act_stub = "added" if action == "add" else "removed"
                    print(
                        f"Successfully {act_stub} {result['device_id']} with {grouping_tag}."
                        )
                else:
                    print(f"Unable to apply Falcon Grouping Tag to {result['device_id']}.")
        else:
            print("No results found")

# Consume the command line
cmd_line = consume_arguments()
# Activate API debugging if requested
if cmd_line.debug:
    logging.basicConfig(level=logging.DEBUG)
# Retrieve the list of serial numbers to process
serials = get_host_serials(cmd_line.serial_file)
# Setup the Falcon Grouping Tag
grouping_tag = "FalconGroupingTags/" + cmd_line.tag
# Login to the CrowdStrike Falcon API
falcon = APIHarnessV2(client_id=cmd_line.client_id,
                      client_secret=cmd_line.client_secret,
                      debug=cmd_line.debug
                      )
# Apply the requested tagging changes
process_hosts(serials)
