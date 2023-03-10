r"""Get Quick Scan quota.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |      FalconPy v1.2.12
`-------'                         `-------'

   ___                  .                  ___  _                    \
 .'   `.  ,   .   __.  _/_     ___       .'   \ /        ___    ___  |   ,
 |     |  |   | .'   \  |     /   `      |      |,---. .'   ` .'   ` |  /
 |  ,_ |  |   | |    |  |    |    |      |      |'   ` |----' |      |-<
  `._.`-. `._/|  `._.'  \__/ `.__/|       `.__, /    | `.___,  `._.' /  \_

Checks your current Quick Scan quota and returns the results.

You must provide your API credentials to this application via the
command line or by setting the following two environment variables:
    FALCON_CLIENT_ID
    FALCON_CLIENT_SECRET

Creation date: 03.10.23 - jshcodes@CrowdStrike
"""
import os
from argparse import ArgumentParser, RawTextHelpFormatter
try:
    from falconpy import QuickScan
except ImportError as no_falconpy:
    raise SystemExit("This application requires the crowdstrike-falconpy library.\n"
                     "Installation: python3 -m pip install crowdstrike-falconpy"
                     ) from no_falconpy


def initialize():
    """Check for API credentials and return an authenticated Quick Scan Service Class instance."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-k", "--falcon_client_id",
                        help="CrowdStrike Falcon API Client ID",
                        required=False
                        )
    parser.add_argument("-s", "--falcon_client_secret",
                        help="CrowdStrike Falcon API Client secret",
                        required=False
                        )
    parsed = parser.parse_args()
    # Command line arguments override detected environment variables
    client_id = parsed.falcon_client_id if parsed.falcon_client_id else os.getenv("FALCON_CLIENT_ID")
    client_secret = parsed.falcon_client_secret if parsed.falcon_client_id else os.getenv("FALCON_CLIENT_SECRET")
    if not client_id:
        parser.error("CrowdStrike Falcon API key must be provided as an argument\n"
                     "or exist within the environment as a variable named FALCON_CLIENT_ID."
                     )
    if not client_secret:
        parser.error("CrowdStrike Falcon API secret must be provided as an argument\n"
                     "or exist within the environment as a variable named FALCON_CLIENT_SECRET."
                     )

    return QuickScan(client_id=client_id, client_secret=client_secret)


def get_quota(interface: QuickScan):
    """Retrieve the current quota details from the API and display the result."""
    quota_lookup = interface.get_scans()
    if not quota_lookup["status_code"] == 200:
        raise SystemExit("Unable to retrieve quota details from the API.")
    total = quota_lookup["body"]["meta"]["quota"]["total"]
    used = quota_lookup["body"]["meta"]["quota"]["used"]
    in_progress = quota_lookup["body"]["meta"]["quota"]["in_progress"]
    print(f"You have used {used:,} out of {total:,} scans available. "
          f"Currently {in_progress:,} scans are running."
          )


if __name__ == "__main__":
    get_quota(initialize())
