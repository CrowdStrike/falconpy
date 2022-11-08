r"""CrowdStrike API authentication leveraging Azure Key Vault for credential storage.
   _____
  /  _  \ __________ _________   ____
 /  /_\  \\___   /  |  \_  __ \_/ __ \
/    |    \/    /|  |  /|  | \/\  ___/
\____|__  /_____ \____/ |__|    \___  >
        \/      \/                  \/
     ____  __.             ____   ____            .__   __
    |    |/ _|____ ___.__. \   \ /   /____   __ __|  |_/  |_
    |      <_/ __ <   |  |  \   Y   /\__  \ |  |  \  |\   __\
    |    |  \  ___/\___  |   \     /  / __ \|  |  /  |_|  |
    |____|__ \___  > ____|    \___/  (____  /____/|____/__|

This application demonstrates storing CrowdStrike API credentials within the
Azure Key Vault service, and retrieving them to access the CrowdStrike API.
"""
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
try:
    from azure.identity import DefaultAzureCredential
except ImportError as no_identity:
    raise SystemExit("The azure-identity library must be installed to use this program.") from no_identity
try:
    from azure.keyvault.secrets import SecretClient
except ImportError as no_kv_secrets:
    raise SystemExit(
        "The azure-keyvault-secrets library must be installed to use this program"
        ) from no_kv_secrets
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
    # "falcon-client-id" and "falcon-client-secret".
    parser.add_argument("-k", "--client_id_parameter",
                        help="Name of the Key Vault Secrets parameter storing your API client ID",
                        required=False,
                        default="falcon-client-id",
                        dest="client_id_parameter"
                        )
    parser.add_argument("-s", "--client_secret_parameter",
                        help="Name of the Key Vault Secrets parameter storing your API client secret",
                        required=False,
                        default="falcon-client-secret",
                        dest="client_secret_parameter"
                        )
    parser.add_argument("-u", "--vault_uri",
                        help="URI of the Azure Key Vault containing the API credentials",
                        required=True,
                        dest="vault_uri"
                        )

    return parser.parse_args()


def get_parameter_store_params(cmd_line: Namespace):
    """Use the provided parameter names to retrieve and return the CrowdStrike API credentials."""
    # Parameters provided to us by the command line
    param_names = [cmd_line.client_id_parameter, cmd_line.client_secret_parameter]
    # Create a KV client
    kv_client = SecretClient(vault_url=cmd_line.vault_uri, credential=DefaultAzureCredential())
    # Retrieve client ID and secret
    returned_client_id = None
    returned_client_secret = None
    for secret in param_names:
        retrieved_secret = kv_client.get_secret(secret)
        if retrieved_secret.name == cmd_line.client_id_parameter:
            returned_client_id = retrieved_secret.value
        if retrieved_secret.name == cmd_line.client_secret_parameter:
            returned_client_secret = retrieved_secret.value

    # No client ID was found
    if not returned_client_id:
        raise SystemExit(
            f"The parameter '{cmd_line.client_id_parameter}' was not found within "
            "Azure Key Vault. Check Vault URI / parameter name."
            )
    # No client secret was found
    if not returned_client_secret:
        raise SystemExit(
            f"The parameter '{cmd_line.client_secret_parameter}' was not found within "
            "Azure Key Vault. Check Vault URI / parameter name."
            )
    print("Client API credentials successfully retrieved from Azure Key Vault.")

    # Retrieve and return values
    return returned_client_id, returned_client_secret


def perform_simple_demonstration(client_id: str, client_secret: str):
    """Perform a simple API demonstration using the credentials retrieved."""
    falcon = Hosts(client_id=client_id, client_secret=client_secret)
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
    # Consume our command line, retrieve our credentials from Azure Key Vault
    # and then execute a simple API demonstration to prove functionality.
    perform_simple_demonstration(*get_parameter_store_params(consume_arguments()))
