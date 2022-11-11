r"""CrowdStrike API authentication leveraging GCP Secrets Manager for credential storage.

Using

  ____  ____ ____
 / ___|/ ___|  _ \
| |  _| |   | |_) |
| |_| | |___|  __/
 \____|\____|_|

   ____                     _         __  __
  / ___|  ___  ___ _ __ ___| |_ ___  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
  \___ \ / _ \/ __| '__/ _ \ __/ __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
   ___) |  __/ (__| | |  __/ |_\__ \ | |  | | (_| | | | | (_| | (_| |  __/ |
  |____/ \___|\___|_|  \___|\__|___/ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|
                                                               |___/

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

Creation date: 11.09.22 - ffalor@CrowdStrike

This application demonstrates storing CrowdStrike API credentials within the GCP Secrets Manager 
service, and retrieving them to access the CrowdStrike API.
"""
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
try:
    from falconpy import Hosts
except ImportError as no_falconpy:
    raise SystemExit(
        "The crowdstrike-falconpy library must be installed to use this program"
    ) from no_falconpy
try:
    from google.cloud import secretmanager
except ImportError as no_google:
    raise SystemExit(
        "The google-cloud-secretmanager library must be installed to use this program"
    ) from no_google


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)
    # Authenticating to GCP: https://googleapis.dev/python/google-api-core/latest/auth.html
    parser.add_argument("-p", "--project_id",
                        help="The GCP Project ID where the secret is stored",
                        dest="project_id"
                        )
    parser.add_argument("-v", "--secret_version",
                        help="The version of the secret to retrieve",
                        required=False,
                        default="latest",
                        dest="secret_version"
                        )
    parser.add_argument("-k", "--client_id_name",
                        help="The name of the GCP Secret Manager secret containing the Falcon API client ID",
                        required=False,
                        default="FALCON_CLIENT_ID",
                        dest="client_id_name"
                        )
    parser.add_argument("-s", "--client_secret_name",
                        help="The name of the GCP Secret Manager secret containing the Falcon API client secret",
                        required=False,
                        default="FALCON_CLIENT_SECRET",
                        dest="client_secret_name"
                        )

    return parser.parse_args()


def access_secret_version(sec_id, project_id, version_id):
    """Access the secret value."""
    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{project_id}/secrets/{sec_id}/versions/{version_id}"

    try:
        response = client.access_secret_version(request={"name": name})
    except Exception as eception:
        raise SystemExit(eception) from eception

    return response.payload.data.decode('UTF-8')


def perform_simple_demonstration(client_id: str, client_secret: str):
    """Perform a simple API demonstration using the credentials retrieved."""
    falcon = Hosts(client_id=client_id, client_secret=client_secret)
    # Retrieve 500 hosts and sort ascending by hostname
    aid_lookup = falcon.query_devices_by_filter_scroll(
        sort="hostname.asc", limit=500)
    if not aid_lookup["status_code"] == 200:
        raise SystemExit(aid_lookup["body"]["errors"][0]["message"])
    if not aid_lookup["body"]["resources"]:
        raise SystemExit("No hosts found.")
    device_details = falcon.get_device_details(
        ids=aid_lookup["body"]["resources"])
    if not device_details["status_code"] == 200:
        raise SystemExit(device_details["body"]["errors"][0]["message"])
    for host in device_details["body"]["resources"]:
        print(f"{host.get('hostname', 'Not found')} [{host['device_id']}]")

    print("Demonstration completed.")


if __name__ == "__main__":
    args = consume_arguments()
    falcon_client_id = access_secret_version(
        args.client_id_name, args.project_id, args.secret_version)
    falcon_client_secret = access_secret_version(
        args.client_secret_name, args.project_id, args.secret_version)
    print("Client API credentials successfully retrieved from GCP Secrets Manager.")
    perform_simple_demonstration(falcon_client_id, falcon_client_secret)
