"""
 ___  _______  _______
|   ||   _   ||   _   |
|.  ||.  |   ||.  1___|
|.  ||.  |   ||.  |___
|:  ||:  1   ||:  1   |
|::.||::.. . ||::.. . |
`---'`-------'`-------'

Create IOC Example - @jshcodes 06.23.21

FalconPy v.0.8.6+

INDICATOR FILE FORMAT EXAMPLE (JSON)
{
    "source": "Test",
    "action": "detect",
    "expiration": "2023-01-22T15:00:00.000Z",
    "description": "Testing",
    "type": "ipv4",
    "value": "4.1.42.34",
    "platforms": ["linux"],
    "severity": "LOW",
    "applied_globally": true
}
"""
import logging
import json
import os
from argparse import ArgumentParser, RawTextHelpFormatter
from falconpy import APIHarness, IOC


def consume_command_line():
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-k", "--falcon_client_id", 
                        help="Falcon API Client ID", 
                        required=True)
    parser.add_argument("-s", "--falcon_client_secret", 
                        help="Falcon API Client Secret", 
                        required=True)
    parser.add_argument("-m", "--method", 
                        help="SDK method to use ('service' or 'uber').", 
                        required=False, 
                        default="service")
    parser.add_argument("-i", "--indicator", 
                        help="Path to the file representing the indicator (JSON format).", 
                        default="example_indicator.json", 
                        required=False)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    
    
    parsed = parser.parse_args()

    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)
    

    return parsed


def connect_api(class_type: str = "service", creds: dict = None):
    """Connect to the selected API service."""
    if class_type.lower() == "service":
        falcon_api = IOC(creds=creds)
    elif class_type.lower() == "uber":
        falcon_api = APIHarness(creds=creds)

    return falcon_api


args = consume_command_line()
credentials = {
    "client_id": args.falcon_client_id,
    "client_secret": args.falcon_client_secret
}
if args.method not in ["service", "uber"]:
    args.method = "service"

falcon = connect_api(args.method, credentials, args.debug)

if not os.path.exists(args.indicator):
    raise SystemExit("Unable to load indicator file.")

with open(args.indicator, "r", encoding="utf-8") as indicator:
    ind_json = json.loads(indicator.read())
    if args.method == "service":
        # Create an IOC using the IOC Service class
        # Since we are using a version greater than 0.7.3,
        # we are able to make use of Body Payload abstraction
        response = falcon.indicator_create(source=ind_json["source"],
                                           action=ind_json["action"],
                                           expiration=ind_json["expiration"],
                                           description=ind_json["description"],
                                           type=ind_json["type"],
                                           value=ind_json["value"],
                                           severity=ind_json["severity"],
                                           applied_globally=ind_json["applied_globally"],
                                           platforms=ind_json["platforms"]  # Can be a list or a comma-delimited string.
                                           )
        print(response)
    elif args.method == "uber":
        # Create an IOC using the Uber class
        # The Uber class does not support Body Payload abstraction.
        # We will send it a standard body payload instead.
        BODY = {
            "indicators": [ind_json]
        }
        response = falcon.command('indicator_create_v1', body=BODY)
        print(response)
