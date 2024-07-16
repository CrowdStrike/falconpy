r"""CrowdStrike API authentication leveraging AWS Parameter Store for credential storage.

Using

     ___   ____    __    ____   _______.
    /   \  \   \  /  \  /   /  /       |
   /  ^  \  \   \/    \/   /  |   (----`
  /  /_\  \  \            /    \   \
 /  _____  \  \    /\    / .----)   |
/__/     \__\  \__/  \__/  |_______/

        ____                                  __               _____ __
       / __ \____ __________ _____ ___  ___  / /____  _____   / ___// /_____  ________
      / /_/ / __ `/ ___/ __ `/ __ `__ \/ _ \/ __/ _ \/ ___/   \__ \/ __/ __ \/ ___/ _ \
     / ____/ /_/ / /  / /_/ / / / / / /  __/ /_/  __/ /      ___/ / /_/ /_/ / /  /  __/
    /_/    \__,_/_/   \__,_/_/ /_/ /_/\___/\__/\___/_/      /____/\__/\____/_/   \___/

to retrieve

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |
`-------'                         `-------'

                ____ ___  _    ____ ____ ____ ___  ____ _  _ ___ _ ____ _    ____
                |__| |__] |    |    |__/ |___ |  \ |___ |\ |  |  | |__| |    [__
                |  | |    |    |___ |  \ |___ |__/ |___ | \|  |  | |  | |___ ___]

Creation date: 11.01.22 - jshcodes@CrowdStrike

This application demonstrates storing CrowdStrike API credentials within the
AWS Parameter Store service, and retrieving them to access the CrowdStrike API.
"""
import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
try:
    import boto3
except ImportError as no_boto:
    raise SystemExit("The boto3 library must be installed to use this program.") from no_boto
try:
    from falconpy import Hosts
except ImportError as no_falconpy:
    raise SystemExit(
        "The crowdstrike-falconpy library must be installed to use this program"
        ) from no_falconpy


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    # If you do not provide these values, they will default to
    # "FALCON_CLIENT_ID" and "FALCON_CLIENT_SECRET".
    parser.add_argument("-k", "--client_id_parameter",
                        help="Name of the Parameter Store parameter storing your API client ID",
                        required=False,
                        default="FALCON_CLIENT_ID",
                        dest="client_id_parameter"
                        )
    parser.add_argument("-s", "--client_secret_parameter",
                        help="Name of the Parameter Store parameter storing your API client secret",
                        required=False,
                        default="FALCON_CLIENT_SECRET",
                        dest="client_secret_parameter"
                        )
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )

    parsed = parser.parse_args()
    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)
    

    return parsed



def get_parameter_store_params(cmd_line: Namespace):
    """Use the provided parameter names to retrieve and return the CrowdStrike API credentials."""
    # Parameters provided to us by the command line
    param_names = [cmd_line.client_id_parameter, cmd_line.client_secret_parameter]
    # Create a SSM client
    ssm_client = boto3.client("ssm")
    # Retrieve client ID and secret
    ssm_response = ssm_client.get_parameters(Names=param_names, WithDecryption=True)
    returned_client_id = None
    returned_client_secret = None
    for returned in ssm_response["Parameters"]:
        if returned["Name"] == cmd_line.client_id_parameter:
            returned_client_id = returned["Value"]
        if returned["Name"] == cmd_line.client_secret_parameter:
            returned_client_secret = returned["Value"]
    # No client ID was found
    if not returned_client_id:
        raise SystemExit(
            f"The parameter '{cmd_line.client_id_parameter}' was not found within "
            "AWS Parameter Store. Check AWS region / parameter name."
            )
    # No client secret was found
    if not returned_client_secret:
        raise SystemExit(
            f"The parameter '{cmd_line.client_secret_parameter}' was not found within "
            "AWS Parameter Store. Check AWS region / parameter name."
            )
    print("Client API credentials successfully retrieved from AWS Parameter Store.")

    # Retrieve and return values
    return returned_client_id, returned_client_secret


def perform_simple_demonstration(client_id: str, client_secret: str, debug: bool):
    """Perform a simple API demonstration using the credentials retrieved."""
    falcon = Hosts(client_id=client_id, client_secret=client_secret, debug=debug)
    # Retrieve 500 hosts and sort ascending by hostname
    aid_lookup = falcon.query_devices_by_filter_scroll(sort="hostname.asc", limit=500)
    if not aid_lookup["status_code"] == 200:
        raise SystemExit(aid_lookup["body"]["errors"][0]["message"])
    if not aid_lookup["body"]["resources"]:
        raise SystemExit("No hosts found.")
    device_details = falcon.get_device_details(ids=aid_lookup["body"]["resources"])
    if not device_details["status_code"] == 200:
        raise SystemExit(device_details["body"]["errors"][0]["message"])
    for host in device_details["body"]["resources"]:
        print(f"{host.get('hostname', 'Not found')} [{host['device_id']}]")

    print("Demonstration completed.")


if __name__ == "__main__":
    # Consume our command line arguments 
    args = consume_arguments()
    # retrieve our credentials from AWS parameter store
    client_id, client_secret = get_parameter_store_params(args)
    # and then execute a simple API demonstration to prove functionality.
    perform_simple_demonstration(client_id, client_secret)
