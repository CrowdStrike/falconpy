r"""Real Time Response API streaming download sample.

._____________._.______  ._______.______  ._____.___ .___ .______  ._____
|    ___/\__ _:|: __   \ : .____/:      \ :         |: __|:      \ :_ ___\
|___    \  |  :||  \____|| : _/\ |   .   ||   \  /  || : ||       ||   |___
|       /  |   ||   :  \ |   /  \|   :   ||   |\/   ||   ||   |   ||   /  |
|__:___/   |   ||   |___\|_.: __/|___|   ||___| |   ||   ||___|   ||. __  |
   :       |___||___|       :/       |___|      |___||___|    |___| :/ |. |
                                                                    :   :/
                                                                        :
.______  ._______           ___ .______  .___    ._______  .______  .______  .________
:_ _   \ : .___  \ .___    |   |:      \ |   |   : .___  \ :      \ :_ _   \ |    ___/
|   |   || :   |  |:   | /\|   ||       ||   |   | :   |  ||   .   ||   |   ||___    \
| . |   ||     :  ||   |/  :   ||   |   ||   |/\ |     :  ||   :   || . |   ||       /
|. ____/  \_. ___/ |   /       ||___|   ||   /  \ \_. ___/ |___|   ||. ____/ |__:___/
 :/         :/     |______/|___|    |___||______/   :/         |___| :/         :
 :          :              :                        :                :
                           :
                                                                FalconPy v1.5.0

            ╦ ╦┌┐ ┌─┐┬─┐  ╔═╗┬  ┌─┐┌─┐┌─┐  ╦  ╦┌─┐┬─┐┌─┐┬┌─┐┌┐┌
            ║ ║├┴┐├┤ ├┬┘  ║  │  ├─┤└─┐└─┐  ╚╗╔╝├┤ ├┬┘└─┐││ ││││
            ╚═╝└─┘└─┘┴└─  ╚═╝┴─┘┴ ┴└─┘└─┘   ╚╝ └─┘┴└─└─┘┴└─┘┘└┘

This sample demonstrates how to perform a streaming download from the
CrowdStrike Real Time Response API. Files are saved as 7-zip archives.

Requirements:
    crowdstrike-falconpy v1.5.0+

Creation: 04.23.2025 - jshcodes@CrowdStrike
"""
import logging
import os
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from typing import List
from requests.exceptions import HTTPError
from falconpy import APIError, APIHarnessV2, BaseURL


class Indicator:
    """Over-architected progress indicator 🤪."""

    _indicator = ["🕛", "🕐", "🕑", "🕒", "🕓", "🕔", "🕧", "🕖", "🕗", "🕘", "🕙", "🕚"]

    def __init__(self):
        """Initialize the class and set the starting position."""
        self._position = -1

    def __repr__(self) -> str:
        """Increment the position and display the current progress indicator value."""
        self.position += 1
        if self.position > len(self.indicator) - 1:
            self.position = 0
        return self.indicator[self.position]

    @property
    def indicator(self) -> List[str]:
        """Progress indicator graphical elements."""
        return self._indicator

    @property
    def position(self) -> int:
        """Progress indicator position."""
        return self._position

    @position.setter
    def position(self, value: int):
        """Set the indicator position."""
        self._position = value


class Arrow(Indicator):
    """Animated download emoji, I might have played with this sample for too long."""

    _indicator = []
    for index, element in enumerate(["💾  ⬅", "💾 ⬅ ", "💾⬅  ", "✅   "]):
        count = 500
        if index == 3:
            count = count * 3
        for i in range(count):
            _indicator.append(element)


def parse_command_line() -> Namespace:
    """Ingest the provided command line parameters and handle any input errors."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    behave = parser.add_argument_group("behavior", "Download and API behavior arguments.")
    behave.add_argument("-c", "--chunk_size",
                        help="Streaming download chunk size",
                        default=8192
                        )
    behave.add_argument("-o", "--overwrite",
                        help="Force overwritting of a pre-existing save file",
                        action="store_true",
                        default=False
                        )
    behave.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    file_group = parser.add_argument_group("filename",
                                           "You must specify a filename to download.\nIf you do "
                                           "not specify a save filename, it will be saved as "
                                           "\"result.7z\"."
                                           )
    file_group.add_argument("-f", "--filename",
                            help="Target filename",
                            required=True
                            )
    file_group.add_argument("-sf", "--save_file",
                            help="Name of the saved file",
                            default="result.7z"
                            )
    mut_group = parser.add_argument_group("host",
                                          "One of the two following arguments must be specified."
                                          )
    mutual = mut_group.add_mutually_exclusive_group(required=True)
    mutual.add_argument("-n", "--hostname",
                        help="Target hostname (use instead of AID)"
                        )
    mutual.add_argument("-a", "--aid",
                        help="Target host AID (use instead of hostname)"
                        )
    auth = parser.add_argument_group("authentication",
                                     "If these arguments are not specified, "
                                     "Environment Authentication will be attempted.\n"
                                     "Environment Authentication: https://falconpy.io/Usage/"
                                     "Authenticating-to-the-API.html#environment-authentication"
                                     )
    auth.add_argument("-k", "--falcon_client_id",
                      help="CrowdStrike Falcon API Client ID",
                      default=None
                      )
    auth.add_argument("-s", "--falcon_client_secret",
                      help="CrowdStrike Falcon API Client Secret",
                      default=None
                      )

    parsed = parser.parse_args()
    if not isinstance(parsed.chunk_size, int):
        parsed.chunk_size = 8192

    return parsed


def open_sdk(debug: bool,
             client_id: str,
             client_secret: str
             ) -> APIHarnessV2:
    """Create an instance of Uber Class from the FalconPy SDK."""
    uber_class = APIHarnessV2(debug=debug,
                              client_id=client_id,
                              client_secret=client_secret,
                              pythonic=True
                              )
    region_name = ""
    for region in BaseURL:
        if region.value == uber_class.base_url.replace("https://", ""):
            region_name = f" {region.name}"

    print(f"  🌐 Connection to CrowdStrike API{region_name} established", end="\r")

    return uber_class


def get_host_aid(hostname: str, sdk: APIHarnessV2) -> str:
    """Retrieve the host AID."""
    try:
        returned = sdk.command("CombinedDevicesByFilter", filter=f"hostname:'{hostname}'").data
        if not returned:
            raise SystemExit("No hosts using this hostname were identified.")
    except APIError as api_error:
        raise SystemExit(api_error) from api_error

    print("  🔎 Host AID identified", end=f"{' '*30}\r")

    return returned[0]["device_id"]


def create_rtr_session(host_aid: str, sdk: APIHarnessV2) -> str:
    """Initialize an RTR session with the target host."""
    try:
        body_payload = {"device_id": host_aid}
        session = sdk.command("RTR_InitSession", body=body_payload)
    except APIError as api_error:
        raise SystemExit(api_error) from api_error

    print("  🔗 Real Time Response connection established", end=f"{' '*20}\r")

    return session.data[0]["session_id"]


def close_rtr_session(session: str, sdk: APIHarnessV2) -> None:
    """Close the RTR session with the target host."""
    try:
        sdk.command("RTR_DeleteSession", session_id=session)
    except APIError as api_error:
        raise SystemExit(api_error) from api_error

    print("  ⛓️‍💥 Real Time Response connection disconnected", end=f"{' '*20}\r")


def get_target_file(filename: str, session: str, sdk: APIHarnessV2) -> str:
    """Execute a get command for the target file and upload it to the CrowdStrike cloud."""
    try:
        body_payload = {
            "base_command": "get",
            "session_id": session,
            "command_string": f"get {filename}"
        }
        get_request = sdk.command("RTR_ExecuteActiveResponderCommand", body=body_payload).data
    except APIError as api_error:
        raise SystemExit(api_error) from api_error

    print("  🤖 Get file command sent", end=f"{' '*30}\r")

    return get_request[0]["cloud_request_id"]


def wait_for_upload(cloud_request_id: str, sdk: APIHarnessV2) -> None:
    """Wait for the upload to complete and return the file SHA256 identifier."""
    status = False
    while not status:
        try:
            result = sdk.command("RTR_CheckActiveResponderCommandStatus",
                                 cloud_request_id=cloud_request_id,
                                 sequence_id=0
                                 )
            status = result.data[0]["complete"]
            print("  ⏳ Waiting for get command to process", end=f"{' '*30}\r")
        except APIError as api_error:
            raise SystemExit(api_error) from api_error
    if result.data[0]["stderr"]:
        print(f"{' '*80}")
        raise SystemExit(f"ERROR: {result.data[0]['stderr']}")


def get_uploaded_file_id(filename: str, session: str, sdk: APIHarnessV2) -> str:
    """Retrieve the SHA256 ID for the upload file."""
    sha = None
    fileid = None
    while not sha:
        try:
            result = sdk.command("RTR_ListFilesV2", session_id=session).data
            for item in result:
                if item["name"] == filename and item["sha256"]:
                    sha = item["sha256"]
                    fileid = item["id"]
        except APIError as api_error:
            raise SystemExit(api_error) from api_error

    print("  🆔 File unique ID retrieved", end=f"{' '*30}\r")

    return sha, fileid


def wait_indicator(value: int = -1) -> int:
    """Create a simple progress indicator."""
    indicator = ["|", "/", "—", "\\"]
    value += 1
    if value > 3:
        value = 0

    return value, indicator[value]


def stream_download_file(sha256: str,
                         session: str,
                         chunk_size: int,
                         save_filename: str,
                         sdk: APIHarnessV2
                         ) -> None:
    """Perform a streaming download of the target file from the CrowdStrike cloud."""
    try:
        progress = Indicator()
        arrow = Arrow()
        not_ready = True
        while not_ready:
            try:
                with sdk.command("RTR_GetExtractedFileContents",
                                 sha256=sha256,
                                 session_id=session,
                                 filename=save_filename,
                                 stream=True
                                 ) as request:
                    request.raise_for_status()
                    print(f"{' '*58}", end="\r")
                    with open(save_filename, "wb") as save_file:
                        chk = 0
                        for chunk in request.iter_content(chunk_size=chunk_size):
                            chk += len(chunk)
                            save_file.write(chunk)
                            print(f"  {arrow} {chk:.0f} bytes downloaded", end=f"{' '*36}\r")
                    not_ready = False
            except HTTPError:
                print(f"  ➡️ Waiting for file to be moved to the CrowdStrike cloud {progress}",
                      end="\r"
                      )
    except APIError as api_error:
        raise SystemExit(api_error) from api_error

    print(f"💯 Download complete, {chk} bytes downloaded "
          f"to the 7-zip archive \"{save_filename}\" "
          )


def delete_file_from_cloud(sha256: str, session: str, sdk: APIHarnessV2) -> None:
    """Remove the get file from the CrowdStrike cloud."""
    try:
        sdk.command("RTR_DeleteFileV2", ids=sha256, session_id=session)
        print("  🗑️ File removed from the CrowdStrike cloud", end="\r")
    except APIError as api_error:
        # Don't end the process so that we can still close out our RTR session.
        print(f"NON-FATAL {api_error}")


def check_for_existing_file(filename: str, overwrite: bool) -> None:
    """Check for the existence of our save file and inform the user it will be overwritten."""
    if not overwrite:
        if os.path.exists(filename):
            keep_going = False
            answer = input(f"The save file {filename} already exists and will be overwritten. "
                           "Continue (Y/N)? "
                           )
            if answer in ["Y", "y", "yes", "Yes", "YES"]:
                keep_going = True
            if not keep_going:
                raise SystemExit("File download procedure cancelled by user")


def main_routine(cmdline: Namespace) -> None:
    """Execute the process based upon specified command line arguments."""
    # Check for the save file and inform the user it will be overwritten.
    check_for_existing_file(cmdline.save_file, cmdline.overwrite)
    # Enable debugging if it has been specified on the command line.
    if cmdline.debug:
        logging.basicConfig(level=logging.DEBUG)
    # Create instances of our three necessary FalconPy Service Classes.
    uber = open_sdk(cmdline.debug, cmdline.falcon_client_id, cmdline.falcon_client_secret)
    # Retrieve our host's AID.
    device_id = cmdline.aid
    if not device_id:
        device_id = get_host_aid(cmdline.hostname, uber)
    # Initialize a Real Time Response session with the host.
    session_id = create_rtr_session(device_id, uber)
    # Execute a get command for our target file.
    task_id = get_target_file(cmdline.filename, session_id, uber)
    # Wait for the file to upload to the CrowdStrike cloud.
    wait_for_upload(task_id, uber)
    # Retrieve the SHA256 file identifier.
    file_sha, file_id = get_uploaded_file_id(cmdline.filename, session_id, uber)
    # Perform a streaming download of the target file.
    stream_download_file(file_sha, session_id, cmdline.chunk_size, cmdline.save_file, uber)
    # Delete the file from the CrowdStrike cloud.
    delete_file_from_cloud(file_id, session_id, uber)
    # Close the Real Time Response session.
    close_rtr_session(session_id, uber)


if __name__ == "__main__":
    # Parse any provided command line arguments and execute the main routine
    main_routine(parse_command_line())
