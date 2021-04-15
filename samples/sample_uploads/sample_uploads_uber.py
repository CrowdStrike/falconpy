#  ____                        _        _   _       _                 _
# / ___|  __ _ _ __ ___  _ __ | | ___  | | | |_ __ | | ___   __ _  __| |___
# \___ \ / _` | '_ ` _ \| '_ \| |/ _ \ | | | | '_ \| |/ _ \ / _` |/ _` / __|
#  ___) | (_| | | | | | | |_) | |  __/ | |_| | |_) | | (_) | (_| | (_| \__ \
# |____/ \__,_|_| |_| |_| .__/|_|\___|  \___/| .__/|_|\___/ \__,_|\__,_|___/
#                       |_|                  |_|
#
#
#  _   _ _                  ____ _
# | | | | |__   ___ _ __   / ___| | __ _ ___ ___
# | | | | '_ \ / _ \ '__| | |   | |/ _` / __/ __|
# | |_| | |_) |  __/ |    | |___| | (_| \__ \__ \
#  \___/|_.__/ \___|_|     \____|_|\__,_|___/___/
#
# These examples show how to interact with the Sample Uploads API using the Uber class.
#
import json
# Import the Uber Class
from falconpy import api_complete as FalconSDK

# Grab our config parameters
with open('../config.json', 'r') as file_config:
    config = json.loads(file_config.read())

# Create an instance of the Uber class
falcon = FalconSDK.APIHarness(creds={
        "client_id": config["falcon_client_id"],
        "client_secret": config["falcon_client_secret"]
    }
)

# Define our file
FILENAME = "testfile.jpg"
# Open the file for binary read, this will be our payload
PAYLOAD = open(FILENAME, 'rb').read()
# Upload the file using the Sample Uploads API, name this file "newfile.jpg" in the API
response = falcon.command('UploadSampleV3', file_name="newfile.jpg", data=PAYLOAD, content_type="application/octet-stream")
# Grab the SHA256 unique identifier for the file we just uploaded
sha = response["body"]["resources"][0]["sha256"]
# Download a copy of this file, use the SHA256 ID to retrieve it
response = falcon.command("GetSampleV3", ids=sha)
# Save the result to a new file
open('uberclass.jpg', 'wb').write(response)
# Delete the file from the API
response = falcon.command("DeleteSampleV3", ids=sha)
# Print the results of our delete command
print(json.dumps(response, indent=4))
