"""Discover Registration Utility - Service Class version

This is a modified version of the script falcon_discover_accounts, a troubleshooting script
posted to our Cloud-AWS repository at https://github.com/CrowdStrike/Cloud-AWS.

This solution demonstrates accepting user input to query the CrowdStrike Falcon Discover API
to register, update and delete AWS accounts.  An additional check function loops through all
accounts registered, and returns configuration detail to assist with troubleshooting setup.

This example leverages the Cloud Connect AWS Service Class and direct authentication.

This example requires FalconPy v0.8.6+.
"""
#   ____ _                 _    ____                            _        ___        ______
#  / ___| | ___  _   _  __| |  / ___|___  _ __  _ __   ___  ___| |_     / \ \      / / ___|
# | |   | |/ _ \| | | |/ _` | | |   / _ \| '_ \| '_ \ / _ \/ __| __|   / _ \ \ /\ / /\___ \
# | |___| | (_) | |_| | (_| | | |__| (_) | | | | | | |  __/ (__| |_   / ___ \ V  V /  ___) |
#  \____|_|\___/ \__,_|\__,_|  \____\___/|_| |_|_| |_|\___|\___|\__| /_/   \_\_/\_/  |____/
#

#
# pylint: disable=C0209,W0703
#
import argparse
import json
# Falcon SDK - Cloud_Connect_AWS and OAuth2 API service classes
from falconpy import CloudConnectAWS, OAuth2


# =============== FORMAT API PAYLOAD
def format_api_payload(rate_limit_reqs=0, rate_limit_time=0):
    """Generate a properly formatted JSON payload for POST and PATCH requests."""
    data = {
        "resources": [
            {
                "cloudtrail_bucket_owner_id": cloudtrail_bucket_owner_id,
                "cloudtrail_bucket_region": cloudtrail_bucket_region,
                "external_id": external_id,
                "iam_role_arn": iam_role_arn,
                "id": local_account,
                "rate_limit_reqs": rate_limit_reqs,
                "rate_limit_time": rate_limit_time
            }
        ]
    }
    return data


# =============== ACCOUNT VALUE
def account_value(provided_id, val, accts):
    """Return the specified value for a specific account id within account_list."""
    returned = False
    for item in accts:
        if item["id"] == provided_id:
            returned = item[val]
    return returned


# =============== CHECK ACCOUNTS
def check_account():
    """Check the accounts attached to this CID."""
    # Retrieve the account list
    account_list = falcon_discover.query_aws_accounts(limit=int(QUERY_LIMIT))["body"]["resources"]
    # Log the results of the account query to a file if logging is enabled
    if log_enabled:
        with open('falcon-discover-accounts.json', 'w+', encoding="utf-8") as file_handle:
            json.dump(account_list, file_handle)
    # Create a list of our account IDs out of account_list
    id_items = []
    for acct_id in account_list:
        id_items.append(acct_id["id"])
    q_max = 1    # VerifyAWSAccountAccess has a ID max count of 1 now?
    for index in range(0, len(id_items), q_max):
        sub_acct_list = id_items[index:index + q_max]
        temp_list = ",".join(list(sub_acct_list))
        access_response = falcon_discover.verify_aws_account_access(ids=temp_list)
        if access_response['status_code'] == 200:
            # Loop through each ID we verified
            for result in access_response["body"]["resources"]:
                if result["successful"]:
                    # This account is correctly configured
                    print(f'Account {result["id"]} is ok!')
                else:
                    # This account is incorrectly configured.  We'll use our account_value function to
                    # retrieve configuration values from the account list we've already ingested.
                    account_values_to_check = {
                        'id': result["id"],
                        'iam_role_arn': account_value(result["id"], "iam_role_arn", account_list),
                        'external_id': account_value(result["id"], "external_id", account_list),
                        'cloudtrail_bucket_owner_id': account_value(result["id"], "cloudtrail_bucket_owner_id", account_list),
                        'cloudtrail_bucket_region': account_value(result["id"], "cloudtrail_bucket_region", account_list),
                    }
                    # Use the account_value function to retrieve the access_health branch,
                    # which contains our api failure reason.
                    try:
                        print('Account {} has a problem: {}'.format(result["id"],
                                                                    account_value(result["id"],
                                                                                  "access_health",
                                                                                  account_list
                                                                                  )["api"]["reason"]
                                                                    ))
                    except Exception:
                        # The above call will produce an error if we're running
                        # check immediately after registering an account as
                        # the access_health branch hasn't been populated yet.
                        # Requery the API for the account_list when this happens.
                        account_list = falcon_discover.query_aws_accounts(limit=f"{str(QUERY_LIMIT)}")["body"]["resources"]
                        print('Account {} has a problem: {}'.format(result["id"],
                                                                    account_value(result["id"],
                                                                                  "access_health",
                                                                                  account_list
                                                                                  )["api"]["reason"]
                                                                    ))
                    # Output the account details to the user to assist with troubleshooting the account
                    print(f'Current settings {json.dumps(account_values_to_check, indent=4)}\n')
        else:
            try:
                # An error has occurred
                print("Got response error code {} message {} ({})".format(access_response["status_code"],
                                                                     access_response["body"]["errors"][0]["message"],
                                                                     access_response["body"]["errors"][0]["id"]
                                                                     ))
            except Exception:
                # Handle any egregious errors that break our return error payload
                print("Got response error code {} message {}".format(access_response['status_code'],
                                                                     access_response['body']["errors"][0]["message"])
                                                                     )


# =============== REGISTER ACCOUNT
def register_account():
    """Register the account with the Discover service."""
    # Call the API to update the requested account.
    register_response = falcon_discover.provision_aws_accounts(parameters={}, body=format_api_payload())
    if register_response["status_code"] == 201:
        print("Successfully registered account.")
    else:
        print("Registration failed with response: {} {}".format(register_response["status_code"],
                                                                register_response["body"]["errors"][0]["message"]
                                                                ))


# =============== UPDATE ACCOUNT
def update_account():
    """Update the account details within the Discover service."""
    # Call the API to update the requested account.
    update_response = falcon_discover.update_aws_accounts(body=format_api_payload())
    if update_response["status_code"] == 200:
        print("Successfully updated account.")
    else:
        print("Update failed with response: {} {}".format(update_response["status_code"],
                                                          update_response["body"]["errors"][0]["message"]
                                                          ))


# =============== DELETE ACCOUNT
def delete_account():
    """Delete the account from the Discover service."""
    # Call the API to delete the requested account, multiple IDs can be deleted by passing in a comma-delimited list
    delete_response = falcon_discover.delete_aws_accounts(ids=local_account)
    if delete_response["status_code"] == 200:
        print("Successfully deleted account.")
    else:
        print("Delete failed with response: {} {}".format(delete_response["status_code"],
                                                          delete_response["body"]["errors"][0]["message"]
                                                          ))


# =============== MAIN

# Configure argument parsing
parser = argparse.ArgumentParser(description="Get Params to send notification to CRWD topic")
# Fully optional
parser.add_argument('-q', '--query_limit', help='The query limit used for check account commands', required=False)
parser.add_argument('-l', '--log_enabled', help='Save results to a file?', required=False, action="store_true")
# Optionally required
parser.add_argument('-r', '--cloudtrail_bucket_region', help='AWS Region where the S3 bucket is hosted',
                    required=False)
parser.add_argument('-o', '--cloudtrail_bucket_owner_id', help='Account where the S3 bucket is hosted',
                    required=False)
parser.add_argument('-a', '--local_account', help='This AWS Account', required=False)
parser.add_argument('-e', '--external_id', help='External ID used to assume role in account', required=False)
parser.add_argument('-i', '--iam_role_arn',
                    help='IAM AWS IAM Role ARN that grants access to resources for Crowdstrike', required=False)
# Always required
parser.add_argument('-c', '--command', help='Troubleshooting action to perform', required=True)
parser.add_argument("-f", "--falcon_client_id", help="Falcon Client ID", required=True)
parser.add_argument("-s", "--falcon_client_secret", help="Falcon Client Secret", required=True)
args = parser.parse_args()

# =============== SET GLOBALS
command = args.command
# Only execute our defined commands
if command.lower() in "check,update,register,delete":
    if command.lower() in "update,register":
        # All fields required for update and register
        if (args.cloudtrail_bucket_owner_id is None or
                args.cloudtrail_bucket_region is None or
                args.local_account is None or
                args.external_id is None or
                args.iam_role_arn is None):
            parser.error(f"The {command} command requires the -r, -o, -a, -e, -i arguments to also be specified.")
        else:
            cloudtrail_bucket_region = args.cloudtrail_bucket_region
            cloudtrail_bucket_owner_id = args.cloudtrail_bucket_owner_id
            local_account = args.local_account
            external_id = args.external_id
            iam_role_arn = args.iam_role_arn
    elif command.lower() in "delete":
        # Delete only requires the local account ID
        if args.local_account is None:
            parser.error(f"The {command} command requires the -l argument to also be specified.")
        else:
            local_account = args.local_account
else:
    parser.error(f"The {command} command is not recognized.")
# These globals exist for all requests
falcon_client_id = args.falcon_client_id
falcon_client_secret = args.falcon_client_secret
log_enabled = args.log_enabled
if args.query_limit is None:
    QUERY_LIMIT = 100
else:
    QUERY_LIMIT = args.query_limit

# =============== MAIN ROUTINE
# Authenticate using our provided falcon client_id and client_secret

auth = OAuth2(client_id=falcon_client_id, client_secret=falcon_client_secret)

# Connect using our token and return an instance of the API gateway object
falcon_discover = CloudConnectAWS(auth_object=auth)
try:
    # Execute the requested command
    if command.lower() == "delete":
        delete_account()
    elif command.lower() == "register":
        register_account()
    elif command.lower() == "update":
        update_account()
    else:
        check_account()
except Exception as e:
    # Handle any previously unhandled errors
    print("Command failed with error: {}.".format(str(e)))
