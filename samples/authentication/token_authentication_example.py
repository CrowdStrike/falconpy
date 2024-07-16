"""CrowdStrike FalconPy Token (Legacy) Authentication Example.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |         FalconPy SDK
`-------'                         `-------'

    _______         __
   |_     _|.-----.|  |--.-----.-----.
     |   |  |  _  ||    <|  -__|     |
     |___|  |_____||__|__|_____|__|__|

         _______         __   __                 __   __              __   __
        |   _   |.--.--.|  |_|  |--.-----.-----.|  |_|__|.----.---.-.|  |_|__|.-----.-----.
        |       ||  |  ||   _|     |  -__|     ||   _|  ||  __|  _  ||   _|  ||  _  |     |
        |___|___||_____||____|__|__|_____|__|__||____|__||____|___._||____|__||_____|__|__|

Token authentication is the process of authenticating to a FalconPy Service Class by providing
a previously assigned bearer token directly to the `auth_token` keyword when instantiating
the Service Class. This is the original method of authentication provided by Service Classes,
and while it is frequently eschewed in preference to Direct and Object Authentication, there
are multiple scenarios where it is still the best option for the situation.

Token Authentication support will always be maintained within Falconpy.

Please note: Token Authentication creates an instance of a FalconPy Service Class that
             cannot reauthenticate itself as it does not have awareness of your API
             credentials. You will have to regenerate your bearer token before it expires
             and update the creds dictionary within the Service Class if you are implementing
             a long running process.

This sample should run using any version of FalconPy and requires the colorama and click libraries.
"""
import logging
import os
import click
import colorama
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace 
from falconpy import (
    CloudConnectAWS,
    Detects,
    Hosts,
    IOC,
    Incidents,
    Intel,
    OAuth2
)


RED = colorama.Fore.LIGHTRED_EX
GREEN = colorama.Fore.LIGHTGREEN_EX
YELLOW = colorama.Fore.LIGHTYELLOW_EX
BOLD = colorama.Style.BRIGHT
ENDMARK = colorama.Style.RESET_ALL

def consume_arguments() -> Namespace:
    parser = ArgumentParser(description=__doc__, fromatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-b", "--base-url",
                        dest="base_url",
                        help="CrowdStrike cloud region. (auto or usgov1, Default: auto)",
                        required=False,
                        default="usgov1"
                        )
    parsed = parser.parse_args()
    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)
    

    return parsed
# ### BEGIN token simulation
def get_token(debug=False):
    """
    Generate a token to use for authentication.

              ███████████
          ████          █████
        ██    ░░░░░░  ░░░░  ██
        ██  ░░░░░░  ░░░░    ███
      ██  ░░░░░░  ░░░░    ░░░░█▓
      ██  ░░░░  ░░FREE  ░░░░░░██
      ██  ░░  ░░░░TOKEN░░░░░░░██
      ██    ░░░░    ░░░░░░░░░░██
      ██  ░░░░    ░░░░░░░░░░░░█▓
        ██      ░░░░░░░░░░░░███
        ██    ░░░░░░░░░░░░░░██
          ████░░░░░░░░░░████
              ███████████

    NOTE: To run this test locally on your machine, you will need to set these
          values in your machine's environment, or provide your credentials when
          they are discovered not to be present.

          GovCloud Users:
          You will need to provide the base_url keyword to the OAuth2 Service
          Class when you create it. This value should be "usgov1".

    """
    falcon_client_id = os.getenv("FALCON_CLIENT_ID")
    falcon_client_secret = os.getenv("FALCON_CLIENT_SECRET")
    if not falcon_client_id:
        falcon_client_id = click.prompt("Please provide your Falcon Client API Key",
                                        hide_input=True
                                        )
    if not falcon_client_secret:
        falcon_client_secret = click.prompt("Please provide your Falcon Client API Secret",
                                            hide_input=True
                                            )
    auth = OAuth2(
        client_id=falcon_client_id,
        client_secret=falcon_client_secret,
        debug=debug 
        )
    # Generate a token
    auth.token()
    if auth.token_status != 201:
        raise SystemExit(f"{BOLD}{YELLOW}Unable to authenticate{ENDMARK}.")
    return auth.token_value
# ### END token simulation


def run_test(class_list: list, token_val: str):  # pylint: disable=R0912
    """Execute the test series and display the results."""
    # Loop thru and confirm we are authenticated to each class.
    for service_class in class_list:
        # Show the class name
        print(f" {service_class.__name__}...", end="\r", flush=True)
        # Create an instance of this class, authenticate using our pre-existing token.
        # NOTE: This authentication method will NOT re-authenticate to the API.
        #       This method does not support token refresh.
        test_instance = service_class(access_token=token_val)
        # Confirm our test classes by calling an easy operation
        # and checking the status_code returned.
        # Note: You can have a valid API key and still not
        # have access to the particular scope in question.
        if isinstance(test_instance, CloudConnectAWS):
            # Cloud Connect AWS service collection
            # https://falconpy.io/Service-Collections/Cloud-Connect-AWS.html
            if test_instance.query_aws_accounts(limit=1)["status_code"] == 200:
                passed(service_class.__name__)
            else:
                failed(service_class.__name__)
        if isinstance(test_instance, Detects):
            # Detects service collection
            # https://falconpy.io/Service-Collections/Detects.html
            if test_instance.query_detects()["status_code"] == 200:
                passed(service_class.__name__)
            else:
                failed(service_class.__name__)
        if isinstance(test_instance, Hosts):
            # Hosts service collection
            # https://falconpy.io/Service-Collections/Hosts.html
            if test_instance.query_devices()["status_code"] == 200:
                passed(service_class.__name__)
            else:
                failed(service_class.__name__)
        if isinstance(test_instance, Incidents):
            # Incidents service collection
            # https://falconpy.io/Service-Collections/Incidents.html
            if test_instance.query_incidents(limit=1)["status_code"] == 200:
                passed(service_class.__name__)
            else:
                failed(service_class.__name__)
        if isinstance(test_instance, Intel):
            # Intel service collection
            # https://falconpy.io/Service-Collections/Intel.html
            if test_instance.query_actor_entities(limit=1)["status_code"] == 200:
                passed(service_class.__name__)
            else:
                failed(service_class.__name__)
        if isinstance(test_instance, IOC):
            # IOC service collection
            # https://falconpy.io/Service-Collections/IOC.html
            if test_instance.indicator_combined_v1(limit=1)["status_code"] == 200:
                passed(service_class.__name__)
            else:
                failed(service_class.__name__)

    print("\nTest series completed")


def failed(svc_class: str):
    """Show the failure message."""
    print(f" {svc_class:<20} [{BOLD}{RED}FAILED{ENDMARK}]")


def passed(svc_class: str):
    """Show the success message."""
    print(f" {svc_class:<20} [{BOLD}{GREEN}PASSED{ENDMARK}]")


if __name__ == "__main__":
    # Parse command-line arguments and retrieve debug mode setting
    args = consume_arguments()
    # Authenticate using Falcon API OAuth2 with debug mode enabled if specified
    get_token(debug=args.debug)
    # Test each of these classes to confirm cross collection authentication for Service Classes
    classes_to_test = [CloudConnectAWS, Detects, Hosts, IOC, Incidents, Intel]
    # Grab a simulated token and execute the test series
    run_test(classes_to_test, get_token())
