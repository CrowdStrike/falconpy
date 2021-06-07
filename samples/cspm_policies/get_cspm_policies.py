#  ___  ____  ____     ___  ____  ____  _  _    ____   __   __    __  ___  __  ____  ____
# / __)(  __)(_  _)   / __)/ ___)(  _ \( \/ )  (  _ \ /  \ (  )  (  )/ __)(  )(  __)/ ___)
# ( (_ \ ) _)   )(    ( (__ \___ \ ) __// \/ \   ) __/(  O )/ (_/\ )(( (__  )(  ) _) \___ \
# \___/(____) (__)    \___)(____/(__)  \_)(_/  (__)   \__/ \____/(__)\___)(__)(____)(____/
#
# The below example uses the CSPM Registration Class to output Horizon policies to csv
#
# Input parameters:
#
# --falcon_client_id or -f (client id of the API credentials with Horizon read capabilities)
# --falcon_client_secret or -s (secret associated with the client_id)
# --output_file or -o (the output file name and path (.csv extentions recommended))
# --cloud or -c (optional: the target cloud platform policies)
#
# Example: below using client_id and client_secret as environment 
# variables and will output all of the policies
#
#  python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET \
#              -o ~/Documents/policies.csv
#
# Example: Below using client_id and client_secret as environment variables and 
#          will output only the azure policies
#
#  python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET \
#              -c azure -o ~/Documents/azure-policies.csv
#
### The script can also be ran with the config.json file
#
#  python3 get_cspm_policies.py -c azure -o ~/Documents/azure-policies.csv
#
###

import argparse
import json
import csv
import os
import sys
import logging
from falconpy import cspm_registration as FalconCSPM

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
config_file = '../config.json'
if os.path.isfile(config_file):
    with open(config_file, 'r') as file_config:
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
falcon = FalconCSPM.CSPM_Registration(
    creds={"client_id": falcon_client_id,
           "client_secret": falcon_client_secret
           })

# Format api json data to accommodate for missing keys
# The goal of this function is to bring uniformtity to the api
# returned data so it can be reported in csv format
def format_json_data(json_data):
    length = 0
    headers = []
    for p in json_data:
        if len(p.keys()) > length:
            length = len(p.keys())
            headers = [*p]
    list_dict = []
    for p in json_data:
        policy = ""
        for h in headers:
            if h in p.keys():
                if h == headers[-1]:
                    str_line = "\"{}\": \"{}\"".format(
                        h, str(p[h]).strip("\n").replace('"', ''))
                else:
                    str_line = "\"{}\": \"{}\", ".format(
                        h, str(p[h]).strip("\n").replace('"', ''))
            else:
                if h == headers[-1]:
                    str_line = "\"{}\": \"{}\"".format(h, "")
                else:
                    str_line = "\"{}\": \"{}\", ".format(h, "")
            policy += str_line
        new_dict = "{{{}}}".format(policy)
        list_dict.append(json.loads(new_dict))
    return list_dict


# determine if we are reporting on a single cloud-platform
if cloud:
    policies = falcon.GetCSPMPolicySettings(
        "cloud-platform=" + cloud)['body']['resources']
else:
    policies = falcon.GetCSPMPolicySettings()['body']['resources']

# Call format function on the returned api data
return_data = format_json_data(policies)

# Determine if an output file is specified and write out or print
if data_file:
    keys = return_data[0].keys()
    with open(data_file, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(return_data)
else:
    print(return_data)
