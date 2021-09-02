"""
 _______       __                   ___ ___  _______                __ __
|   _   .---.-|  .----.-----.-----.(   Y   )|   _   .---.-.-----.--|  |  |--.-----.--.--.
|.  1___|  _  |  |  __|  _  |     | \  1  / |   1___|  _  |     |  _  |  _  |  _  |_   _|
|.  __) |___._|__|____|_____|__|__| /  _  \ |____   |___._|__|__|_____|_____|_____|__.__|
|:  |                              /:  |   \|:  1   |
|::.|                             (::. |:.  |::.. . |           FalconPy v0.6.3
`---'                              `--- ---'`-------'

falconx_scan_example.py - Falcon X Sandbox - Upload / Scan example

- jshcodes@CrowdStrike 09.01.2021
"""
import os
import argparse
from falconpy.falconx_sandbox import FalconXSandbox
from falconpy.sample_uploads import SampleUploads
from falconpy.oauth2 import OAuth2


def check_scan_status(id: str) -> dict:
    """
    Retrieves the status of a submission and returns it
    """
    # Return our submission response by ID
    return sandbox.GetSubmissions(ids=id)


def upload_file(filename: str,
                upload_name: str,
                submit_comment: str,
                confidential: bool
                ) -> dict:
    """
    Uploads the specified file to CrowdStrike cloud
    applying any provided attributes. Returns the result.
    """
    # Read in our binary payload
    PAYLOAD = open(filename, 'rb').read()
    # Upload this file to the Sample Uploads API
    return samples.upload_sample(file_data=PAYLOAD,
                                 file_name=upload_name,
                                 comment=submit_comment,
                                 is_confidential=confidential
                                 )


def submit_for_analysis(sha_value: str) -> dict:
    """
    Submits an uploaded file that matches the provided
    SHA256 to Falcon X Sandbox for analysis
    """
    # Call the submit method and provide the SHA256
    # of our upload file. Select Windows 10 64-bit
    # as our analysis environment.
    return sandbox.submit(
        body={
            "sandbox": [{
                "sha256": sha_value,
                "environment_id": 160
            }]
        }
    )


def delete_file(id_value: str) -> dict:
    """
    Deletes a file from CrowdStrike cloud
    based upon the SHA256 provided.
    """
    # Call the delete_sample method using the SHA256
    return samples.delete_sample(ids=sha)["status_code"]


def get_indicator():
    """
    Tracks the current position of the progress indicator
    and returns it's value when requested.
    """
    # indicator_position and indicator_forward are global
    global indicator_position                                       
    global indicator_forward
    # If our counter exceeds the list length flip our direction
    if indicator_position >= len(indicator) - 1:
        indicator_forward = False
    if indicator_position <= 0:
        indicator_forward = True

    if indicator_forward:
        # Increment it by 1
        indicator_position += 1
    else:
        # Decrement it by 1
        indicator_position -= 1

    # Return our current indicator
    return f"[{indicator[indicator_position]}]"


def inform(msg: str):
    """
    Provides informational updates to
    the user as the program progresses.
    """
    # Dynamic user update messages
    print("  %-80s" % msg, end="\r", flush=True)


# Silly KITT progress indicator
indicator = [
    "........",
    "o.......",
    "Oo......",
    "oOo.....",
    ".oOo....",
    "..oOo...",
    "...oOo..",
    "....oOo.",
    ".....oOo",
    "......oO",
    ".......o",
    "........"
]
# Current indicator position
indicator_position = 0
# Current indicator direction
indicator_forward = True

# Argument parser for our command line
parser = argparse.ArgumentParser(
    description="Falcon X Sandbox example"
    )
# File to be analyzed
parser.add_argument(
    '-f', '--file',
    help='File to analyze',
    required=True
    )
# CrowdStrike API Client ID
parser.add_argument(
    '-k', '--key',
    help='Your CrowdStrike API key ID\n'
    '     Required Scopes\n'
    '     Sample Uploads:   WRITE\n'
    '     Sandbox:          WRITE\n', required=True
    )
# CrowdStrike API Client secret
parser.add_argument(
    '-s', '--secret',
    help='Your CrowdStrike API key secret', required=True
    )
args = parser.parse_args()

# Announce progress
inform("[  Init  ]")
# Create an instance of our authentication object
# and provide our API credentials for authorization
auth = OAuth2(client_id=args.key,
              client_secret=args.secret
              )
# Connect to Sample Uploads
samples = SampleUploads(auth_object=auth)
# Connect to Falcon X Sandbox
sandbox = FalconXSandbox(auth_object=auth)

# Announce progress
inform("[ Upload ]")
# Upload our test file
response = upload_file(args.file,
                       "example-file.jpg",
                       "Falcon X upload and scan example",
                       confidential=False
                       )

# Retrieve the SHA of our upload file
sha = response["body"]["resources"][0]["sha256"]

# Announce progress
inform("[ Submit ]")
# Submit the file for analysis to Falcon X Sandbox
submit_response = submit_for_analysis(sha)

# Track our running status
running = "running"
# Loop until success or error
while running == "running":
    # Submission ID
    submit_id = submit_response["body"]["resources"][0]["id"]
    # Check the scan status
    result = check_scan_status(submit_id)
    if result["body"]["resources"]:
        # Announce progress with our KITT indicator
        inform(f"{get_indicator()}")
        # Grab our latest status
        running = result["body"]["resources"][0]["state"]

# We've finished, retrieve the report
result = sandbox.get_reports(ids=submit_id)

inform("[ Delete ]")
# Remove our test file
delete_response = delete_file(sha)

# Display the results
print(result)

# Inform the user of our deletion failure
if delete_response != 200:
    print("Unable to remove test file from Falcon X Sandbox")