"""Sample Uploads Service Collection example, Service Class version.

The following demonstrates how to interact with the Sample Uploads API using the Service Class.
This example uses Direct Authentication and supports token refresh / authentication free usage.

This sample requires FalconPy v0.8.6+
"""
#  ____                        _        _   _       _                 _
# / ___|  __ _ _ __ ___  _ __ | | ___  | | | |_ __ | | ___   __ _  __| |___
# \___ \ / _` | '_ ` _ \| '_ \| |/ _ \ | | | | '_ \| |/ _ \ / _` |/ _` / __|
#  ___) | (_| | | | | | | |_) | |  __/ | |_| | |_) | | (_) | (_| | (_| \__ \
# |____/ \__,_|_| |_| |_| .__/|_|\___|  \___/| .__/|_|\___/ \__,_|\__,_|___/
#                       |_|                  |_|
#
#  ____                  _             ____ _
# / ___|  ___ _ ____   _(_) ___ ___   / ___| | __ _ ___ ___
# \___ \ / _ \ '__\ \ / / |/ __/ _ \ | |   | |/ _` / __/ __|
#  ___) |  __/ |   \ V /| | (_|  __/ | |___| | (_| \__ \__ \
# |____/ \___|_|    \_/ |_|\___\___|  \____|_|\__,_|___/___/
#
import os
import json
# Import the Sample Uploads Service Class
from falconpy import SampleUploads
#     _       _
#    /  _ .__|_o _
#    \_(_)| || |(_|
#                _|
#
# Grab our config parameters from our config file.
# Review this README here for more detail regarding the sample config file.
# https://github.com/CrowdStrike/falconpy/tree/main/samples
with open('../config.json', 'r', encoding="utf-8") as file_config:
    config = json.loads(file_config.read())

# Provide our credentials to the SampleUploads Service Class using
# Direct Authentication. Since we are using version 0.8.6+ we do not
# need to specify the base_url keyword unless we are on GovCloud.
falcon = SampleUploads(client_id=config["falcon_client_id"],
                       client_secret=config["falcon_client_secret"]
                       # ,base_url="usgov1"     # GovCloud users only
                       )

# Define our upload and download file names
UP_FILENAME = "testfile.jpg"
DOWN_FILENAME = "serviceclass.jpg"

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
# Since we are using the Service Class, we do not need to specify the content type
response = falcon.upload_sample(file_name="newfile.jpg", file_data=PAYLOAD)
# You can also use Operation ID syntax for this step if you prefer
# response = falcon.UploadSampleV3(file_name="newfile.jpg", file_data=PAYLOAD)

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
response = falcon.get_sample(ids=sha)
# You can also use Operation ID syntax for this step if you prefer
# response = falcon.GetSampleV3(ids=sha)
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
response = falcon.delete_sample(ids=sha)
# You can also use Operation ID syntax for this step if you prefer
# response = falcon.DeleteSampleV3(ids=sha)

# Display the results of the delete operation based upon the value of status_code
if response["status_code"] == 200:
    print("File successfully deleted from sandbox.")
else:
    print("Unable to remove file from sandbox.")

# To see the raw response from the API use the following
# print(json.dumps(response, indent=4))


#     _________________
#    |# :           : #|
#    |  :  MALWARE  :  |
#    |  :  SAMPLES  :  |
#    |  :           :  |
#    |  :___________:  |
#    |     _________   |
#    |    | __      |  |
#    |    ||  |     |  |
#    \____||__|_____|__|
