r"""Pull samples from CrowdStrike Falcon Quarantine.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |         FalconPy v1.2
`-------'                         `-------'

____ _  _ ____ ____ ____ _  _ ___ _ _  _ ____ ___     ____ _ _    ____ ____
|  | |  | |__| |__/ |__| |\ |  |  | |\ | |___ |  \    |___ | |    |___ [__
|_\| |__| |  | |  \ |  | | \|  |  | | \| |___ |__/    |    | |___ |___ ___]

Leverages the FalconPy Uber Class to retrieves all quarantined files from
Falcon Quarantine and saves them to a subfolder within the current working
directory. Quarantined files can be downloaded as archives with a password
or as regular executables.

Requires: crowdstrike-falconpy
Optional: click

Created: 02.21.23 - tsullivan06@CrowdStrike
"""
import os
import json
from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime
try:
    from click import echo_via_pager
except ImportError:
    # If click is installed, show a paginated debug output
    # If it's not, just use print
    echo_via_pager = print
try:
    from falconpy import APIHarness
except ImportError as no_falconpy:
    raise SystemExit("The falconpy library must be installed. Install it with the command:\n"
                     "python3 -m pip install crowdstrike-falconpy"
                     ) from no_falconpy


# Retrieve our command line arguments
parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
required = parser.add_argument_group("required arguments")
required.add_argument("-k", "--key", help="Falcon Client API ID", required=True)
required.add_argument("-s", "--secret", help="Falcon Client API secret", required=True)
parser.add_argument("-p", "--protect", help="Password protect", action="store_true", default=False)
parser.add_argument("-b", "--base", help="Falcon API base url", default="auto")
parser.add_argument("-x", "--proxy", help="Proxy for API requests", default=None)
parser.add_argument("-d", "--debug", action="store_true", default=False,
                    help="Display API response for quarantine file request"
                    )
cmdline = parser.parse_args()
print("\n ✅ Starting retrieval of all quarantined files, please wait...")

# Configure the authentication mechanism
if cmdline.proxy:
    cmdline.proxy = json.loads(cmdline.proxy.replace("'", '"'))  # Clean up any weird quotes
falcon = APIHarness(client_id=cmdline.key,
                    client_secret=cmdline.secret,
                    base_url=cmdline.base,
                    proxy=cmdline.proxy
                    )

# API Query 1: collect the quarantine IDs available
q_id_response = falcon.command("QueryQuarantineFiles")
if not q_id_response["body"]["resources"]:
    raise SystemExit("No quarantined files found.")

# API Query 2: configure the ids list to collect the quarantine file details
details = falcon.command("GetQuarantineFiles",
                         body={"ids": list(set(q_id_response["body"]["resources"]))}
                         )["body"]["resources"]
if cmdline.debug:
    # Review the API response within the console if debug is enabled
    echo_via_pager(json.dumps(details, indent=4))  # Paginates if click is installed
    if echo_via_pager.__name__ != "echo_via_pager":
        print("")  # Don't need the extra line break when using pagination

# Leverage the details query response to create a dictionary of hash values to file names
filenames = {d["sha256"]: d["paths"][0]["filename"] for d in details}  # best naming option

# Create a subfolder named samples with the UTC time appended
subfolder = os.path.join(os.getcwd(), f"samples_{datetime.utcnow().strftime('%m%d%YT%H%M%SZ')}")
os.makedirs(subfolder, exist_ok=True)

# API Query 3: using the sha256 hash list, query the get sample endpoint to download the file to
# the local directory - name the download using the file name associated to the hash in the
# dictionary of hash values to file names
for item_hash, file_name in filenames.items():
    response = falcon.command("GetSampleV3", password_protected=cmdline.protect, ids=item_hash)
    if isinstance(response, dict):  # Error received from the API
        for err in response["body"]["errors"]:
            print(f" ⛔ Failed to download {file_name} [{err['code']}] {err['message']}")
    else:
        print(f" ⬇️  Downloaded {file_name} to {subfolder}.")
        file_path = os.path.join(subfolder, f"{file_name}{'.zip' if cmdline.protect else ''}")
        with open(file_path, 'wb') as output_file:
            output_file.write(response)

# Inform the user that we're done and where the files are stored
print(f"\n 🏁 Quarantine file download to {subfolder} completed.\n")
