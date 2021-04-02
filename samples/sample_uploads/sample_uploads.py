#  ____                        _        _   _       _                 _
# / ___|  __ _ _ __ ___  _ __ | | ___  | | | |_ __ | | ___   __ _  __| |___
# \___ \ / _` | '_ ` _ \| '_ \| |/ _ \ | | | | '_ \| |/ _ \ / _` |/ _` / __|
#  ___) | (_| | | | | | | |_) | |  __/ | |_| | |_) | | (_) | (_| | (_| \__ \
# |____/ \__,_|_| |_| |_| .__/|_|\___|  \___/| .__/|_|\___/ \__,_|\__,_|___/
#                       |_|                  |_|
#
#
# These examples show how to interact with the Sample Uploads API using
# both the Uber class, and the regular Service class.
#
import json

#  _   _ _                  ____ _
# | | | | |__   ___ _ __   / ___| | __ _ ___ ___
# | | | | '_ \ / _ \ '__| | |   | |/ _` / __/ __|
# | |_| | |_) |  __/ |    | |___| | (_| \__ \__ \
#  \___/|_.__/ \___|_|     \____|_|\__,_|___/___/
#
# This example shows how to interact with the 
# Sample Uploads API using the Uber class.

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


#  ____                  _             ____ _
# / ___|  ___ _ ____   _(_) ___ ___   / ___| | __ _ ___ ___
# \___ \ / _ \ '__\ \ / / |/ __/ _ \ | |   | |/ _` / __/ __|
#  ___) |  __/ |   \ V /| | (_|  __/ | |___| | (_| \__ \__ \
# |____/ \___|_|    \_/ |_|\___\___|  \____|_|\__,_|___/___/
#
# This example shows how to interact with the 
# Sample Uploads API using the Sample Uploads Service class.

from falconpy import sample_uploads as FalconUploads

# #Grab our config parameters
with open('config.json', 'r') as file_config:
    config = json.loads(file_config.read())

falcon = FalconUploads.Sample_Uploads(creds={
        "client_id": config["falcon_client_id"],
        "client_secret": config["falcon_client_secret"]
    }
)

# Define our file
FILENAME = "testfile.jpg"
# Open the file for binary read, this will be our payload
PAYLOAD = open(FILENAME, 'rb').read()
# Upload the file using the Sample Uploads API, name this file "newfile.jpg" in the API
# Since we are using the Service Class, we do not need to specify the content type
response = falcon.UploadSampleV3(file_name="newfile.jpg", file_data=PAYLOAD)
# Grab the SHA256 unique identifier for the file we just uploaded
sha = response["body"]["resources"][0]["sha256"]
# Download a copy of this file, use the SHA256 ID to retrieve it
response = falcon.GetSampleV3(ids=sha)
# Save the result to a new file
open('serviceclass.jpg', 'wb').write(response)
# Delete the file from the API
response = falcon.DeleteSampleV3(ids=sha)
# Print the results of our delete command
print(json.dumps(response, indent=4))
