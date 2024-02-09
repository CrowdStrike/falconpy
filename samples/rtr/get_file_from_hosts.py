r"""Retrieve a file from multiple hosts.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |        FalconPy v1.3
`-------'                         `-------'
        ____             __   _______
       / __ \___  ____ _/ /  /_  __(_)___ ___  ___
      / /_/ / _ \/ __ `/ /    / / / / __ `__ \/ _ \
     / _, _/  __/ /_/ / /    / / / / / / / / /  __/
    /_/ |_|\___/\__,_/_/    /_/ /_/_/ /_/ /_/\___/
            ____
           / __ \___  _________  ____  ____  ________
          / /_/ / _ \/ ___/ __ \/ __ \/ __ \/ ___/ _ \
         / _, _/  __(__  ) /_/ / /_/ / / / (__  )  __/
        /_/ |_|\___/____/ .___/\____/_/ /_/____/\___/
                       /_/

This program will retrieve a single file of the same name
from multiple hosts. Files will be saved as 7zip archives
named after the host's AID.

Creation date: 11.30.23 - jshcodes@CrowdStrike
"""
import os
import multiprocessing
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from logging import basicConfig, DEBUG
from time import sleep
try:
    from falconpy import Hosts, RealTimeResponse
except ImportError as no_falconpy:
    raise SystemExit(
        "FalconPy v1.3 or greater must be installed to run this program."
        ) from no_falconpy


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true"
                        )
    parser.add_argument("-n", "--hostname",
                        help="Hostname to target (stemmed search)",
                        default=""
                        )
    parser.add_argument("-b", "--base_url", help="CrowdStrike API base URL", default="auto")
    auth = parser.add_argument_group("authentication arguments")
    auth.add_argument("-k", "--client-id",
                      dest="client_id",
                      help="Falcon API client ID",
                      default=os.getenv("FALCON_CLIENT_ID")
                      )
    auth.add_argument("-s", "--client-secret",
                      dest="client_secret",
                      help="Falcon API client ID",
                      default=os.getenv("FALCON_CLIENT_SECRET")
                      )
    req = parser.add_argument_group("required arguments")
    req.add_argument("-f", "--filepath",
                     help="Filename and path of the file to be downloaded",
                     required=True
                     )
    return parser.parse_args()


def wait_for_file(ses: dict, fname: str):
    """Asynchronously wait for a file to complete the get process.
    
    After processing completes, delete the session.
    """
    success = False
    waiting = True
    while waiting:
        file_list = rtr.list_files_v2(session_id=ses["session_id"])["body"]["resources"]
        for item in [f for f in file_list if f["cloud_request_id"] == ses["task_id"]]:
            if item["complete"]:
                waiting = False
            else:
                sleep(3)
    file_download = rtr.get_extracted_file_contents(session_id=ses["session_id"],
                                                    sha256=item["sha256"],
                                                    filename=fname,
                                                    )
    if isinstance(file_download, bytes):
        with open(f"{ses['aid']}.7z", "wb") as save_file:    # Save to a file named after the device ID
            save_file.write(file_download)
        print(f"Successfully downloaded {fname} from {ses['aid']} to {ses['aid']}.7z")
        success = True

    rtr.delete_session(ses["session_id"])  # Close this specific host session

    return {"session_id": ses["session_id"],
            "id": item["id"],
            "success": success
            }


start = datetime.now().timestamp()
successful = 0
cmdline = consume_arguments()
# Debug logging
if cmdline.debug:
    basicConfig(level=DEBUG)
# Handle any provided command line hostname filters
target_filter = ""
if cmdline.hostname:
    target_filter = f"hostname:*'*{cmdline.hostname}*'"
# Retrieve our target filename from the provided file path
_, target_file = os.path.split(cmdline.filepath)
# Construct instances of the Service Classes we are wanting to use.
hosts = Hosts(debug=cmdline.debug,
              client_id=cmdline.client_id,
              client_secret=cmdline.client_secret,
              base_url=cmdline.base_url
              )
rtr = RealTimeResponse(auth_object=hosts)
# Retrieve our target device AIDs.
target_devices = hosts.query_devices_by_filter_scroll(filter=target_filter)["body"]["resources"]
print(f"{len(target_devices)} matching hosts identified.")
# Initialize a session with the host batch.
session_init = rtr.batch_init_sessions(host_ids=target_devices)
batch_id = session_init["body"]["batch_id"]  # Grab the batch ID
# Issue a batch get command
result = rtr.batch_get_command(batch_id=batch_id, file_path=cmdline.filepath)
# Quickly loop thru the result to create our batch of successful session IDs
sessions = [d for d in result["body"]["combined"]["resources"].values() if d["stdout"]]
print(f"File successfully identified on {len(sessions)} hosts.")
# Grab the batch ID
batch_req_id = result["body"]["batch_get_cmd_req_id"]
# Asynchronously wait for the upload to complete, and then the file to download
# Afterwards, delete the session and the file from the cloud
with ThreadPoolExecutor(max_workers=min(multiprocessing.cpu_count() * 2, 20)) as executor:
    futures = {
        executor.submit(wait_for_file, sess, target_file) for sess in sessions
    }
    for fut in as_completed(futures):
        fresult = fut.result()
        # Delete the file now that it's been downloaded
        rtr.delete_file_v2(session_id=fresult["session_id"], ids=fresult["id"])
        if fresult["success"]:
            successful += 1
# Routine complete, display the total run time.
print(f"{successful} total files downloaded.")
print(f"Total run time: {datetime.now().timestamp() - start:.2f} seconds")
