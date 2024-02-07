#!/usr/bin/env python3
r"""Sensor Update Policy cloner.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

╔═╗┌─┐┌┐┌┌─┐┌─┐┬─┐  ╦ ╦┌─┐┌┬┐┌─┐┌┬┐┌─┐  ╔═╗┌─┐┬  ┬┌─┐┬ ┬
╚═╗├┤ │││└─┐│ │├┬┘  ║ ║├─┘ ││├─┤ │ ├┤   ╠═╝│ ││  ││  └┬┘
╚═╝└─┘┘└┘└─┘└─┘┴└─  ╚═╝┴  ─┴┘┴ ┴ ┴ └─┘  ╩  └─┘┴─┘┴└─┘ ┴

       _..._             .-'''-.
    .-'_..._''. .---.   '   _    \
  .' .'      '.\|   | /   /` '.   \    _..._         __.....__
 / .'           |   |.   |     \  '  .'     '.   .-''         '.
. '             |   ||   '      |  '.   .-.   . /     .-''"'-.  `. .-,.--.
| |             |   |\    \     / / |  '   '  |/     /________\   \|  .-. |
| |             |   | `.   ` ..' /  |  |   |  ||                  || |  | |
. '             |   |    '-...-'`   |  |   |  |\    .-------------'| |  | |
 \ '.          .|   |               |  |   |  | \    '-.____...---.| |  '-
  '. `._____.-'/|   |               |  |   |  |  `.             .' | |
    `-.______ / '---'               |  |   |  |    `''-...... -'   | |
             `                      |  |   |  |                    |_|
                                    '--'   '--'

This script will clone one or all sensor update policies from one CID to another.

Developed by @Don-Swanson-Adobe
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import APIHarnessV2, APIError


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-n", "--policy_name", help="Limit cloning to a specific policy")
    req = parser.add_argument_group("Required arguments")
    req.add_argument("--source_id",
                     help="CrowdStrike Falcon API key (Source CID)",
                     default=os.getenv("FALCON_CLIENT_ID")
                     )
    req.add_argument("--source_secret",
                     help="CrowdStrike Falcon API secret (Source CID)",
                     default=os.getenv("FALCON_CLIENT_SECRET")
                     )
    req.add_argument("--dest_id",
                     help="CrowdStrike Falcon API key (Destination CID)",
                     required=True
                     )
    req.add_argument("--dest_secret",
                     help="CrowdStrike Falcon API secret (Destination CID)",
                     required=True
                     )
    parsed = parser.parse_args()
    if not parsed.source_id or not parsed.source_secret:
        parser.error("You must provide CrowdStrike API credentials for the source CID.")

    return parsed


# Consume any command line arguments
cmd_line = consume_arguments()

# Activate debugging if requested
if cmd_line.debug:
    logging.basicConfig(level=logging.DEBUG)

# Source CID API Harness with the policies you wish to clone
with APIHarnessV2(client_id=cmd_line.source_id,
                  client_secret=cmd_line.source_secret,
                  debug=cmd_line.debug,
                  pythonic=True
                  ) as source:
    # Destination CID API Harness where policies will be cloned to
    with APIHarnessV2(client_id=cmd_line.dest_id,
                      client_secret=cmd_line.dest_secret,
                      debug=cmd_line.debug,
                      pythonic=True
                      ) as destination:
        filter_string = None
        if cmd_line.policy_name:
            filter_string = f"name:*'{cmd_line.policy_name}'"
        try:
            policies = source.command("queryCombinedSensorUpdatePoliciesV2",
                                      filter=filter_string
                                      ).data
        except APIError as api_error:
            raise SystemExit(api_error.message)
        for policy in policies:
            if policy["platform_name"] == "Linux":
                settings = {"build": str(policy["settings"]["build"])}
            else:
                settings = {
                    "build": str(policy["settings"]["build"]),
                    "uninstall_protection": policy["settings"]["uninstall_protection"]
                    }
            body_payload = {
                "resources": [{
                        "description": policy["description"],
                        "name": policy["name"],
                        "platform_name": policy["platform_name"],
                        "settings": settings
                        }]
                    }
            try:
                response = destination.command("createSensorUpdatePoliciesV2", body=body_payload)
                if response.status_code == 201:
                    print(f"Created {policy['name']} policy successfully.")
            except APIError as api_error:
                print(f"Unable to create {policy['name']} policy on destination tenant.")
