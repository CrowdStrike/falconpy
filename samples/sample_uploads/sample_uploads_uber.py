r"""Sample Uploads Service Collection example, Uber Class version.

 ____                        _        _   _       _                 _
/ ___|  __ _ _ __ ___  _ __ | | ___  | | | |_ __ | | ___   __ _  __| |___
\___ \ / _` | '_ ` _ \| '_ \| |/ _ \ | | | | '_ \| |/ _ \ / _` |/ _` / __|
 ___) | (_| | | | | | | |_) | |  __/ | |_| | |_) | | (_) | (_| | (_| \__ \
|____/ \__,_|_| |_| |_| .__/|_|\___|  \___/| .__/|_|\___/ \__,_|\__,_|___/
                      |_|                  |_|

 _   _ _                  ____ _
| | | | |__   ___ _ __   / ___| | __ _ ___ ___
| | | | '_ \ / _ \ '__| | |   | |/ _` / __/ __|
| |_| | |_) |  __/ |    | |___| | (_| \__ \__ \
 \___/|_.__/ \___|_|     \____|_|\__,_|___/___/

The following demonstrates how to interact with the Sample Uploads API using the Uber Class.
This example uses Direct Authentication and supports token refresh / authentication free usage.

This sample requires FalconPy v0.8.6+
"""
import os
import json
from argparse import ArgumentParser, RawTextHelpFormatter
# Import the Uber Class
from falconpy import APIHarness
#     _       _
#    /  _ .__|_o _
#    \_(_)| || |(_|
#                _|
#
# Grab our config parameters from our config file or command line.
parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
parser.add_argument("-k", "--falcon_client_id", help="API Client ID (required if not using a configuration file).", required=False, default=None)
parser.add_argument("-s", "--falcon_client_secret", help="API Client Secret (required if not using a configuration file).", required=False, default=None)
parser.add_argument("-c", "--config_file", help="Credential configuration file (required if not using command line arguments).", required=False, default="../config.json")
parser.add_argument("-b", "--base_url", help="CrowdStrike Region (only required for GovCloud users).", required=False, default="auto")
args = parser.parse_args()

if not args.falcon_client_id or not args.falcon_client_secret:
    if not os.path.exists(args.config_file):
        raise SystemExit("Credentials not provided, unable to continue.")
    # Review this README here for more detail regarding the sample config file.
    # https://github.com/CrowdStrike/falconpy/tree/main/samples
    with open(args.config_file, 'r', encoding="utf-8") as file_config:
            config = json.loads(file_config.read())
else:
    config = {
        "falcon_client_id": args.falcon_client_id,
        "falcon_client_secret": args.falcon_client_secret
    }

# Provide our credentials to the Uber Class using Direct Authentication.
# Since we are using version 0.8.6+ we do not need to specify the base_url
# keyword unless we are on GovCloud.
falcon = APIHarness(client_id=config["falcon_client_id"],
                    client_secret=config["falcon_client_secret"],
                    base_url=args.base_url
                    )

# Define our upload and download file names
UP_FILENAME = "testfile.jpg"
DOWN_FILENAME = "uberclass.jpg"

# Remove our download file if it is present before we begin
if os.path.exists(DOWN_FILENAME):
    os.remove(DOWN_FILENAME)

#    | |._ | _  _. _|
#    |_||_)|(_)(_|(_|
#       |
#
# Open the file for binary read, this will be our payload
with open(UP_FILENAME, "rb") as upload:
    PAYLOAD = upload.read()

# Upload the file using the Sample Uploads API, name this file "newfile.jpg" in the sandbox
# Since we are using the Uber Class, we  need to specify the cntent type
response = falcon.command('UploadSampleV3',
                          file_name="newfile.jpg",
                          data=PAYLOAD,
                          content_type="application/octet-stream"
                          )

# Display the results of the upload operation based upon the value of status_code
if response["status_code"] == 200:
    # Grab the SHA256 unique identifier for the file we just uploaded from the response
    sha = response["body"]["resources"][0]["sha256"]
    print(f"File ({sha}) successfully uploaded to the sandbox.")
else:
    raise SystemExit("Unable to upload file to the sandbox.")

#    ,_
#    | \ _     ._ | _  _. _|
#    |_/(_)\/\/| ||(_)(_|(_|
#
# Download a copy of this file, use the SHA256 ID to retrieve it
response = falcon.command("GetSampleV3", ids=sha)

if not isinstance(response, dict):
    # This response contains a binary object, we need to save the result to a new file
    with open(DOWN_FILENAME, 'wb') as download:
        download.write(response)
else:
    # An error has occurred, we can't retrieve the file.
    raise SystemExit("Unable to retreive file from the sandbox.")

#    ,_
#    | \ _ | __|_ _
#    |_/(/_|(/_|_(/_
#
# Delete the file from the Sandbox API
response = falcon.command("DeleteSampleV3", ids=sha)

# Display the results of the delete operation based upon the value of status_code
if response["status_code"] == 200:
    print("File successfully deleted from sandbox.")
else:
    print("Unable to remove file from sandbox.")

# To see the raw response from the API use the following
# print(json.dumps(response, indent=4))


#     _________________
#    |# :           : #|
#    |  :           :  |
#    |  :  SAMPLES  :  |
#    |  :           :  |
#    |  :___________:  |
#    |     _________   |
#    |    | __      |  |
#    |    ||  |     |  |
#    \____||__|_____|__|
