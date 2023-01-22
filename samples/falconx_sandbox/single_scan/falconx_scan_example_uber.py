r"""Falcon X Sandbox - Upload / Scan example, Uber class version.

 _______       __
|   _   .---.-|  .----.-----.-----.
|.  1___|  _  |  |  __|  _  |     |
|.  __) |___._|__|____|_____|__|__|
|:  |
|::.|    ___       __         __ __ __
`---'   |   .-----|  |_.-----|  |  |__.-----.-----.-----.----.-----.
        |.  |     |   _|  -__|  |  |  |  _  |  -__|     |  __|  -__|
        |.  |__|__|____|_____|__|__|__|___  |_____|__|__|____|_____|
        |:  |                         |_____|
        |::.|            _______                 __ __
        `---'           |     __|.---.-.-----.--|  |  |--.-----.--.--.
                        |__     ||  _  |     |  _  |  _  |  _  |_   _|
                        |_______||___._|__|__|_____|_____|_____|__.__|

                                    CrowdStrike FalconPy  v0.8.6+

Supports scanning a single file only.

- jshcodes@CrowdStrike 09.01.2021
"""
import os
import time
import argparse
from enum import Enum
from datetime import timedelta
from argparse import RawTextHelpFormatter
try:
    from falconpy import APIHarness
except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy


class Environment(Enum):
    """Enum to hold our different environment specifiers."""
    WIN7 = 100
    WIN7_64 = 110
    WIN10 = 160
    DROID = 200
    LINUX = 300
    MACOS = 400


class Indicator():
    """Silly progress indicator styled after a classic Cylon."""
    def __init__(self, start_position: int = -1, start_direction: bool = True):
        self.position = start_position
        self.direction = start_direction
        self.indicator = self._setup()

    @staticmethod
    def _setup():
        cylons = []
        total = 7
        cylons.append(f"{'o' * (total+1)}")
        for cnt in range(total):
            cylons.append(f"{'o' * (cnt)}O{'o' * (total - cnt)}")
        cylons.append(f"{'o' * (cnt+1)}O")
        cylons.append(f"{'o' * (total+1)}")
        return cylons

    def step(self):
        """Calculate the position and direction of the indicator."""
        if self.position >= len(self.indicator) - 1:
            # Too long - out of bounds
            self.direction = False
        if self.position <= 0:
            # Too short - out of bounds
            self.direction = True

        if self.direction:
            # Increment position by 1
            self.position += 1
        else:
            # Decrement position by 1
            self.position -= 1

    def display(self) -> str:
        """Increment the indicator position and return its value."""
        # Step the indicator forward
        self.step()
        # Return the new indicator display
        return f"[ {self.indicator[self.position]} ]"


def parse_command_line():
    """Parse and return inbound command line arguments."""
    # Argument parser for our command line
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=RawTextHelpFormatter
        )
    # File to be analyzed
    parser.add_argument(
        '-f', '--file',
        help='File to analyze',
        required=True
        )
    # Environment to use for analysis
    parser.add_argument(
        '-e', '--environment',
        help="Environment to use for analysis (win7, win7_64, win10, droid, linux, macos)",
        required=False
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
    return parser.parse_args()


def check_scan_status(check_id: str) -> dict:
    """Retrieve the status of a submission and return it."""
    # Return our submission response by ID
    return falcon.command("GetSubmissions", ids=check_id)


def upload_file(filename: str,
                upload_name: str,
                submit_comment: str,
                confidential: bool
                ) -> dict:
    """Upload file to CrowdStrike Cloud.

    Uploads the specified file to CrowdStrike cloud
    applying any provided attributes. Returns the result.
    """
    # Read in our binary payload
    with open(filename, 'rb') as payload:
        # Upload this file to the Sample Uploads API
        return falcon.command("UploadSampleV3",
                              data=payload.read(),
                              file_name=upload_name,
                              comment=submit_comment,
                              is_confidential=confidential,
                              content_type="application/octet-stream"
                              )


def submit_for_analysis(sha_value: str) -> dict:
    """Submit file for analysis.

    Submits an uploaded file that matches the provided SHA256
    to the specified Falcon Intelligence Sandbox environment
    for analysis. Returns the result.
    """
    # Call the submit method and provide the SHA256
    # of our upload file and our desired environment type.
    return falcon.command("Submit",
                          body={
                              "sandbox": [{
                                  "sha256": sha_value,
                                  "environment_id": Environment[SANDBOX_ENV].value
                              }]
                          }
                          )


def delete_file(id_value: str) -> int:
    """Delete file from sandbox.

    Deletes a file from CrowdStrike cloud based upon the
    SHA256 provided. Returns the operation status code.
    """
    # Call the delete_sample method using the SHA256
    return falcon.command("DeleteSampleV3", ids=id_value)["status_code"]


def inform(msg: str):
    """Provide informational updates to the user as the program progresses."""
    # Dynamic user update messages
    print("  %-80s" % msg, end="\r", flush=True)


def running_time(begin: time):
    """Calculate the current running time and return it."""
    return f"[ Time running: {str(timedelta(seconds=(time.time() - begin)))} ]"


# Start the clock
start_time = time.time()
# Parse our command line arguments
args = parse_command_line()
# Check for environment
if not args.environment:
    SANDBOX_ENV = "WIN10"
else:
    # Convert the submitted environment name to upper case
    SANDBOX_ENV = str(args.environment).upper()
    MATCHED = False
    # Loop thru our defined environment names
    for env in Environment:
        # User submitted name matches an accepted type
        if env.name == SANDBOX_ENV:
            MATCHED = True
    if not MATCHED:
        # We only accept the environments defined in our Enum above
        raise SystemExit("Invalid sandbox environment specified.")

if not os.path.isfile(args.file):
    # We were not provided a valid filename
    raise SystemExit("Invalid filename specified.")

# Announce progress
inform(f"[   Init   ] {running_time(start_time)}")
# Connect to the API and provide our credentials for authorization
falcon = APIHarness(client_id=args.key,
                    client_secret=args.secret
                    )
# Announce progress
inform(f"[  Upload  ] {running_time(start_time)}")

# Upload our test file
response = upload_file(args.file,
                       f"Falcon Intelligence File Analysis: {time.strftime('%V %r %Z')}",
                       "Falcon Intelligence upload and scan example",
                       confidential=False
                       )

# Retrieve the SHA of our upload file
sha = response["body"]["resources"][0]["sha256"]

# Announce progress
inform(f"[  Submit  ] {running_time(start_time)}")

# Submit the file for analysis to Falcon X Sandbox
submit_response = submit_for_analysis(sha)

# Track our running status
RUNNING = "running"

# Create a new progress indicator
indicator = Indicator()

# Loop until success or error
while RUNNING == "running":
    # Submission ID
    submit_id = submit_response["body"]["resources"][0]["id"]
    # Check the scan status
    result = check_scan_status(submit_id)
    if result["body"]["resources"]:
        # Announce progress with our KITT indicator
        inform(f"{indicator.display()} {running_time(start_time)}")
        # Grab our latest status
        RUNNING = result["body"]["resources"][0]["state"]

# We've finished, retrieve the report. There will only be one in this example.
analysis_result = falcon.command("GetReports", ids=submit_id)["body"]
if RUNNING == "error":
    if analysis_result["errors"]:
        raise SystemExit(analysis_result["errors"][0]["message"])
    else:
        raise SystemExit("\nAn error occurred while attempting this analysis")

try:
    analysis = analysis_result["resources"][0]["sandbox"][0]
except (TypeError, KeyError):
    raise SystemExit("\nUnable to retrieve analysis results")

# Announce progress
inform(f"[  Delete  ] {running_time(start_time)}")
# Remove our test file
delete_response = delete_file(sha)

# Display the analysis results
if "error_type" in analysis:
    # Error occurred, display the detail
    print(f"{analysis['error_type']}: {analysis['error_message']}")
else:
    # No error, display the full analysis
    print(f"Detonated on: {analysis['environment_description']}{' ' * 20}")
    print(f"File type: {analysis['file_type']}")
    try:
        if len(analysis['classification']):
            print("\nClassifications")
            for classification in analysis['classification']:
                print(classification)
    except KeyError:
        # No classification branch, skip
        pass
    try:
        if len(analysis['extracted_interesting_strings']):
            print("\nInteresting strings")
            for interesting in analysis['extracted_interesting_strings']:
                print(f"Source: {interesting['source']}   Type: {interesting['type']}")
                print(f"{interesting['value']}\n")
    except KeyError:
        # No extracted strings branch, skip
        pass

    print(f"\nVerdict: {analysis['verdict']}")

# Inform the user of our deletion failure
if delete_response != 200:
    print("Unable to remove test file from Falcon Intelligence Sandbox")

# Display our total execution time
COMPLETE_TIME = str(timedelta(seconds=(time.time() - start_time)))
print(f"Total running time: {COMPLETE_TIME}")
