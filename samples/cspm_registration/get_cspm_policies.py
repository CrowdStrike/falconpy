r"""CrowdStrike Horizon - Retrieve CSPM Policies

  ___  ____  ____     ___  ____  ____  _  _    ____   __   __    __  ___  __  ____  ____
 / __)(  __)(_  _)   / __)/ ___)(  _ \( \/ )  (  _ \ /  \ (  )  (  )/ __)(  )(  __)/ ___)
( (_ \ ) _)   )(    ( (__ \___ \ ) __// \/ \   ) __/(  O )/ (_/\ )(( (__  )(  ) _) \___ \
 \___/(____) (__)    \___)(____/(__)  \_)(_/  (__)   \__/ \____/(__)\___)(__)(____)(____/

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
# pylint: disable=C0209
#
import json
import csv
import os
import sys
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from tabulate import tabulate
try:
    from falconpy import CSPMRegistration
except ImportError as no_falconpy:
    raise SystemExit(
        "The crowdstrike-falconpy package must be installed to run this program."
        ) from no_falconpy


def consume_arguments() -> Namespace:
# Capture command line arguments
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-f", "--falcon_client_id",
                        help="Falcon Client ID", 
                        default=None,
                        required=False)
    parser.add_argument("-s", "--falcon_client_secret",
                        help="Falcon Client Secret",
                        default=None, 
                        required=False)
    parser.add_argument("-o", "--output_file",
                        help="Policy report output file (CSV format)", 
                        required=False)
    parser.add_argument("-c", "--cloud", 
                        help="Cloud provider (aws, azure, gcp)", 
                        required=False)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )

    parsed = parser.parse_args()
    return parsed


cmd_line = consume_arguments()

# Activate debugging if requested
if cmd_line.debug:
    logging.basicConfig(level=logging.DEBUG)



# pylint: disable=E0606

# Grab our client_id and client_secret or exit
CONFIG_FILE = '../config.json'
if os.path.isfile(CONFIG_FILE):
    with open(CONFIG_FILE, 'r', encoding="utf-8") as file_config:
        config = json.loads(file_config.read())
        falcon_client_id = config['falcon_client_id']
        falcon_client_secret = config['falcon_client_secret']
elif cmd_line.falcon_client_id is not None and cmd_line.falcon_client_secret is not None:
    falcon_client_id = cmd_line.falcon_client_id
    falcon_client_secret = cmd_line.falcon_client_secret
    debug = cmd_line.debug if cmd_line.debug else False  # Set debug mode based on argument
else:
    logging.error(
        " Please specify Falcon API Credentials with config.json or script arguments")
    sys.exit()

data_file = cmd_line.output_file
cloud = cmd_line.cloud

# Instantiate CSPM_Registration service class
falcon = CSPMRegistration(client_id=falcon_client_id,
                          client_secret=falcon_client_secret,
                          debug=debug
                          )


def format_json_data(json_data):
    """Format API results for CSV.

    Format api json data to accommodate for missing keys
    The goal of this function is to bring uniformity to the api
    returned data so it can be reported in csv format.
    """
    list_dict = []
    checks = ["cloud_service", "cloud_asset_type_id", "cloud_asset_type", "nist_benchmark",
              "cis_benchmark", "fql_policy", "policy_settings", "pci_benchmark",
              "soc2_benchmark", "cloud_service_subtype"]
    for data_row in json_data:
        for check in checks:
            if check not in data_row:
                data_row[check] = ""
        list_dict.append(data_row)

    return list_dict


def chunk_long_description(desc, col_width) -> str:
    """Chunks a long string by delimiting with CR based upon column length."""

    desc_chunks = []
    chunk = ""
    for word in desc.split():
        new_chunk = f"{chunk} {word.strip()}"
        if len(new_chunk) >= col_width:
            desc_chunks.append(new_chunk)
            chunk = ""
        else:
            chunk = new_chunk

    delim = "\n"
    if chunk.strip():
        desc_chunks.append(chunk.strip())

    return delim.join(desc_chunks)


# Retrieve our list of policy settings
policies = falcon.get_policy_settings(cloud_platform=cloud)['body']['resources']
# Call format function on the returned api data
return_data = format_json_data(policies)
# Determine if an output file is specified and write out or print
if data_file:
    keys = []
    for row in return_data:
        for key in row.keys():
            if key not in keys:
                keys.append(key)
    with open(data_file, 'w', newline='', encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(return_data)
    print(f"CSPM policies exported to '{data_file}'.")
else:
    results = []
    for row in return_data:
        row.pop("cloud_service", None)
        row.pop("cloud_asset_type_id", None)
        row.pop("cloud_asset_type", None)
        row.pop("fql_policy", None)
        row.pop("is_remediable", None)
        row.pop("created_at", None)
        row.pop("updated_at", None)
        name_val = f"[{row['policy_id']}] {chunk_long_description(row['name'], 80).strip()}"
        name_val = f"{name_val}\n{row['policy_type']}"
        if row["cloud_service_subtype"]:
            name_val = f"{name_val} // {row['cloud_service_subtype']}"
        name_val = f"{name_val}\n{row['default_severity'].title()} severity"
        name_val = f"{name_val}\nCloud provider: {row['cloud_provider'].upper()}"
        row["name"] = name_val
        row.pop("policy_settings", None)
        row.pop("policy_id", None)
        row.pop("policy_type", None)
        row.pop("cloud_provider", None)
        row.pop("default_severity", None)
        row.pop("policy_timestamp", None)
        row.pop("cloud_service_subtype", None)
        row.pop("cloud_friendly_service", None)
        benchmarks = ["cis", "pci", "nist", "soc2"]
        benchmark_list = []
        for benchmark_name in benchmarks:
            for benchmark in row[f"{benchmark_name}_benchmark"]:
                bench_value = [f"[{benchmark['id']}]",
                               f"{benchmark['benchmark_short']}",
                               f"({benchmark['recommendation_number']})"
                               ]
                benchmark_list.append(" ".join(bench_value))
            row[f"{benchmark_name}_benchmark"] = "\n".join(benchmark_list)
        row.pop("remediation_summary", None)
        results.append(row)

    headers = {
        "name": "Name",
        "cis_benchmark": "CIS",
        "pci_benchmark": "PCI",
        "nist_benchmark": "NIST",
        "soc2_benchmark": "SOC2"
    }
    print(tabulate(tabular_data=results, tablefmt="fancy_grid", headers=headers))
