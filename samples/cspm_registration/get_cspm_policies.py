"""CrowdStrike Horizon - Retrieve CSPM Policies

This example uses the CSPM Registration Class to output Horizon policies to CSV.

This sample requires FalconPy v0.7.4+.

Input parameters:

  --falcon_client_id or -f (client id of the API credentials with Horizon read capabilities)
  --falcon_client_secret or -s (secret associated with the client_id)
  --output_file or -o (the output file name and path (.csv extentions recommended))
  --cloud or -c (optional: the target cloud platform policies)

Examples:
Using client_id and client_secret as environment variables and will output all of the policies.

 python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET \
             -o ~/Documents/policies.csv

Using client_id and client_secret as environment variables and will output only the azure policies.

 python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET \
             -c azure -o ~/Documents/azure-policies.csv

The script can also be ran using the config.json example credential file.

 python3 get_cspm_policies.py -c azure -o ~/Documents/azure-policies.csv

"""
#     ___  ____  ____     ___  ____  ____  _  _    ____   __   __    __  ___  __  ____  ____
#    / __)(  __)(_  _)   / __)/ ___)(  _ \( \/ )  (  _ \ /  \ (  )  (  )/ __)(  )(  __)/ ___)
#   ( (_ \ ) _)   )(    ( (__ \___ \ ) __// \/ \   ) __/(  O )/ (_/\ )(( (__  )(  ) _) \___ \
#    \___/(____) (__)    \___)(____/(__)  \_)(_/  (__)   \__/ \____/(__)\___)(__)(____)(____/
#
# pylint: disable=C0209
#
import argparse
import json
import csv
from json.decoder import JSONDecodeError
import os
import sys
import logging
from falconpy import CSPMRegistration

# Capture command line arguments
parser = argparse.ArgumentParser(
    description="Gather API client_id and client_secret from arguments")
parser.add_argument("-f", "--falcon_client_id",
                    help="Falcon Client ID", default=None, required=False)
parser.add_argument("-s", "--falcon_client_secret",
                    help="Falcon Client Secret", default=None, required=False)
parser.add_argument("-o", "--output_file",
                    help="Policy report output file", required=False)
parser.add_argument(
    "-c", "--cloud", help="Cloud provider (aws, azure, gcp)", required=False)
args = parser.parse_args()

# Grab our client_id and client_secret or exit
CONFIG_FILE = '../config.json'
if os.path.isfile(CONFIG_FILE):
    with open(CONFIG_FILE, 'r', encoding="utf-8") as file_config:
        config = json.loads(file_config.read())
        falcon_client_id = config['falcon_client_id']
        falcon_client_secret = config['falcon_client_secret']
elif args.falcon_client_id is not None and args.falcon_client_secret is not None:
    falcon_client_id = args.falcon_client_id
    falcon_client_secret = args.falcon_client_secret
else:
    logging.error(
        " Please specify Falcon API Credentials with config.json or script arguments")
    sys.exit()

data_file = args.output_file
cloud = args.cloud

# Instantiate CSPM_Registration service class
falcon = CSPMRegistration(client_id=falcon_client_id,
                          client_secret=falcon_client_secret
                          )


def format_json_data(json_data):
    """Format API results for CSV.

    Format api json data to accommodate for missing keys
    The goal of this function is to bring uniformity to the api
    returned data so it can be reported in csv format.
    """
    length = 0
    headers = []
    for pol in json_data:
        if len(pol.keys()) > length:
            length = len(pol.keys())
            headers = [*pol]
    list_dict = []
    for pol in json_data:
        policy = ""
        for head in headers:
            if head in pol.keys():
                if head == headers[-1]:
                    str_line = "\"{}\": \"{}\"".format(
                        head, str(pol[head]).strip("\n").replace('"', ''))
                else:
                    str_line = "\"{}\": \"{}\", ".format(
                        head, str(pol[head]).strip("\n").replace('"', ''))
            else:
                if head == headers[-1]:
                    str_line = "\"{}\": \"{}\"".format(head, "")
                else:
                    str_line = "\"{}\": \"{}\", ".format(head, "")
            policy += str_line
        new_dict = "{{{}}}".format(policy)
        try:
            list_dict.append(json.loads(new_dict))
        except JSONDecodeError:
            # Throw out any decode errors
            pass
    return list_dict


# Retrieve our list of policy settings
policies = falcon.get_policy_settings(cloud_platform=cloud)['body']['resources']
# Call format function on the returned api data
return_data = format_json_data(policies)

# Determine if an output file is specified and write out or print
if data_file:
    keys = return_data[0].keys()
    with open(data_file, 'w', newline='', encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(return_data)
else:
    print(return_data)
