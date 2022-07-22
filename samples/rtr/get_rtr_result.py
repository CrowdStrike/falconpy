r"""Retrieve the results of a command executed via Real Time Response.

 _______             __  _______ __
|   _   .-----.---.-|  ||       |__.--------.-----.
|.  l   |  -__|  _  |  ||.|   | |  |        |  -__|
|.  _   |_____|___._|__|`-|.  |-|__|__|__|__|_____|
|:  |   |                 |:  |
|::.|:. |                 |::.|
`--- ---'                 `---'
             _______
            |   _   .-----.-----.-----.-----.-----.-----.-----.
            |.  l   |  -__|__ --|  _  |  _  |     |__ --|  -__|
            |.  _   |_____|_____|   __|_____|__|__|_____|_____|
            |:  |   |           |__|
            |::.|:. |                       FalconPy v1.1
            `--- ---'
"""
import os
import glob
import json
from argparse import ArgumentParser, RawTextHelpFormatter
from falconpy import RealTimeResponseAdmin, __version__ as FPVERSION


def show_banner():
    """Display the banner."""
    top = __doc__.split("\n")
    top.pop(0)
    top.pop(0)
    top.insert(0, "\033[31m")
    top = "\n".join(top).replace("FalconPy v1.1", f"\033[34m FalconPy v{FPVERSION} \033[31m")
    mag = "\033[95m"
    endm = "\033[0m"
    print(rf"""{top} {mag}
____ _  _ ____ ____ _  _ ___ _ ____ _  _    ____ ____ ____ _  _ _    ___ ____
|___  \/  |___ |    |  |  |  | |  | |\ |    |__/ |___ [__  |  | |     |  [__
|___ _/\_ |___ |___ |__|  |  | |__| | \|    |  \ |___ ___] |__| |___  |  ___]
{'=' * 78}{endm}""")


def parse_command_line():
    """Retrieve provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-k", "--falcon_client_id",
                        help="CrowdStrike Falcon API Client ID",
                        required=True
                        )
    parser.add_argument("-s", "--falcon_client_secret",
                        help="CrowdStrike Falcon API Client Secret",
                        required=True
                        )
    parser.add_argument("-m", "--member_cid",
                        help="Child CID for MSSP scenarios",
                        required=False,
                        default=None
                        )
    parser.add_argument("-b", "--base_url",
                        help="CrowdStrike Base URL (Only required for GovCloud: usgov1)",
                        required=False,
                        default="auto"
                        )
    parser.add_argument("-c", "--cloud_request_id",
                        help="Cloud Request ID to retrieve, accepts comma-delimited lists",
                        required=False,
                        default=None
                        )
    parser.add_argument("-q", "--sequence",
                        help="Command result sequence ID, defaults to 0",
                        required=False,
                        default=0
                        )
    parser.add_argument("-f", "--queue_file_folder",
                        help="Load a directory of save files or a single save file for processing",
                        required=False,
                        default=None
                        )
    return parser.parse_args()


def perform_lookup(clid, csec, mid, base, cr_id, seq):  # pylint: disable=R0913
    """Perform the lookup for the cloud request ID."""
    # Show the banner
    show_banner()

    # Connect to the API using the Real Time Response Admin Service Class
    rtr = RealTimeResponseAdmin(client_id=clid,
                                client_secret=csec,
                                member_cid=mid,
                                base_url=base
                                )

    # Loop through each Cloud Request ID provided and check it's status
    for request_id in cr_id.split(","):
        result = rtr.check_admin_command_status(cloud_request_id=request_id,
                                                sequence=seq
                                                )

        # Display the Cloud Request ID
        print(f"Cloud Request ID:\033[1m {request_id}\033[0m")

        # Display the API error result
        if result["status_code"] != 200:
            for err in result["body"]["errors"]:
                print(f"[{err['code']}] {err['message']}\n")

        # Display the contents of `stdout` and `stderr` for the returned result
        for execution in result["body"]["resources"]:
            for std in ["stdout", "stderr"]:
                if std in execution:
                    if execution[std]:
                        print(f"{execution[std]}\n")


# Parse the command line
args = parse_command_line()
# If we were provided an execution directory
if args.queue_file_folder:
    # And that directory exists
    if os.path.exists(args.queue_file_folder):
        # Check to see if we're dealing with a file or folder
        if os.path.isfile(args.queue_file_folder):
            # We're only handling one file
            queue_files = [args.queue_file_folder]
        else:
            # Retrieve a list of all queue files within this directory
            queue_files = glob.glob(os.path.join(args.queue_file_folder,"*.json"), recursive=True)
        for queue_file in queue_files:
            # Loop through each queue file in the folder and
            # perform a lookup for each cloud request ID within
            with open(queue_file, "r", encoding="utf-8") as queues:
                queued = json.load(queues)
            cloud_request_id = []
            for mcid, details in queued.items():
                mem_cid = mcid
                for aid, crid in details.items():
                    cloud_request_id.append(crid)
                CLOUD_REQUEST_ID = ",".join(cloud_request_id)
            # Perform a lookup based upon the contents of the queue file
            perform_lookup(args.falcon_client_id,
                           args.falcon_client_secret,
                           mem_cid,
                           args.base_url,
                           CLOUD_REQUEST_ID,
                           args.sequence
                           )
else:
    # Perform a singular lookup based upon the cloud request ID provided
    perform_lookup(args.falcon_client_id,
                   args.falcon_client_secret,
                   args.member_cid,
                   args.base_url,
                   args.cloud_request_id,
                   args.sequence
                   )
