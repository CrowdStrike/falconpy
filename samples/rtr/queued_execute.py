r"""CrowdStrike Bulk Command Execution example (w/ queueing) - Real Time Response Admin.

        ___           __  _______             ___
       / _ \___ ___ _/ / /_  __(_)_ _  ___   / _ \___ ___ ___  ___  ___  ___ ___
      / , _/ -_) _ `/ /   / / / /  ' \/ -_) / , _/ -_|_-</ _ \/ _ \/ _ \(_-</ -_)
     /_/|_|\__/\_,_/_/   /_/ /_/_/_/_/\__/ /_/|_|\__/___/ .__/\___/_//_/___/\__/
                                                       /_/
 _______                            __  _______                   __
|   _   .--.--.-----.--.--.-----.--|  ||   _   .-----.-----.-----|__.-----.-----.-----.
|.  |   |  |  |  -__|  |  |  -__|  _  ||   1___|  -__|__ --|__ --|  |  _  |     |__ --|
|.  |   |_____|_____|_____|_____|_____||____   |_____|_____|_____|__|_____|__|__|_____|
|:  1   |                              |:  1   |
|::..   |                              |::.. . |                FalconPy v1.0
`----|:.|                              `-------'         jshcodes@CrowdStrike, 02.25.22
     `--'


This simple example demonstrates performing batch administrative commands against
multiple hosts. The host list is calculated based upon a string match between the
hostname and a search string you provide at runtime. The command executed is also
provided at runtime, and passed to the target host in Raw format. (Default: `ls -al`)

Hosts that are offline when the session is inititalize will be queued for later execution.

Results are output to the screen broken out by host. You must provide your credentials
to the program at runtime, or have them pre-defined within your environment. These
environment variables are called FALCON_CLIENT_ID and FALCON_CLIENT_SECRET.

Requires: crowdstrike-falconpy v8.0+
API Scopes:
    Hosts       - READ
    RTR         - READ, WRITE
    RTR ADMIN   - READ, WRITE

Modified: 10.17.22, add AID consumption via a file - jshcodes@CrowdStrike
Allowed formats:
  JSON                  or
  [                     {
      "AID1",               "hosts": [
      "AID2",                   "AID1",
      "etc"                     "AID2",
  ]                             "etc"
                            ]
                        }

ASCII - List of AIDs only, commas will be ignored
AID1
AID2
AID3
etc.

JSON is attempted first, then we fall back to ASCII when it doesn't decode.

Duplicates are ignored.
"""
import os
import time
import json
from argparse import ArgumentParser, RawTextHelpFormatter
try:
    from falconpy import Hosts, RealTimeResponse, RealTimeResponseAdmin
except ImportError as no_falconpy:
    raise SystemExit(
        "This solution requires the crowdstrike-falconpy package to be installed."
        ) from no_falconpy


def parse_command_line():
    """Calculate constants based upon provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-k", "--falcon_client_id",
                        help="CrowdStrike Falcon API Client ID",
                        required=False
                        )
    parser.add_argument("-s", "--falcon_client_secret",
                        help="CrowdStrike Falcon API Client Secret",
                        required=False
                        )
    parser.add_argument("-c", "--command",
                        help="Command to perform.",
                        required=False
                        )
    parser.add_argument("-f", "--find",
                        help="String to match against hostname to select hosts.",
                        required=False
                        )
    parser.add_argument("-l", "--load_file",
                        help="File containing the list of AIDs to target (JSON or ASCII list)",
                        required=False,
                        default=None
                        )


    parsed = parser.parse_args()
    if not parsed.find and not parsed.load_file:
        parser.error("You must specify a string to search (`-f`) "
                     "or a load file (`-l`) containing a list of AIDs."
                     )

    return parsed


# Constants used for display formatting
BOLD = "\033[1m"
NOCOLOR = "\033[0m"

# Parse our command line
args = parse_command_line()

# Constants provided at runtime / from the environment
CLIENT_ID = os.getenv("FALCON_CLIENT_ID")
if args.falcon_client_id:
    CLIENT_ID = args.falcon_client_id

CLIENT_SECRET = os.getenv("FALCON_CLIENT_SECRET")
if args.falcon_client_secret:
    CLIENT_SECRET = args.falcon_client_secret

COMMAND = "ls -al"
if args.command:
    COMMAND = args.command

HOST_MATCH = args.find

# Connect to the CrowdStrike API service collections
hosts = Hosts(client_id=CLIENT_ID,
              client_secret=CLIENT_SECRET
              )
rtr = RealTimeResponse(auth_object=hosts.auth_object)
rtr_admin = RealTimeResponseAdmin(auth_object=hosts.auth_object)

if args.load_file:
# Retrieve a list of host AIDs from our load file
    if not os.path.exists(args.load_file):
        raise SystemExit(f"The load file: {args.load_file} cannot be found.")
    # Mock up our expected host_ids dictionary
    host_ids = {}
    host_ids["body"] = {}
    try:
        # Simple tricks to identify file type.  Properly done this should use Python magic.
        with open(args.load_file, "r", encoding="utf-8") as loader:
            file_detail = json.load(loader)
        if "hosts" in file_detail:
            host_ids["body"]["resources"] = file_detail["hosts"]
        else:
            host_ids["body"]["resources"] = file_detail
    except json.JSONDecodeError as err:
        # Fall back to the flat file method
        with open(args.load_file, "r", encoding="utf-8") as loader:
            file_detail = loader.read()
        host_ids["body"]["resources"] = list(filter(None, file_detail.replace(",", "").split("\n")))
else:
    # Retrieve a list of host AIDs that match our search string
    host_ids = hosts.query_devices_by_filter(filter=f"hostname:*'*{HOST_MATCH}*'",
                                             sort="hostname.asc"
                                             )
    if host_ids["status_code"] != 200:
        raise SystemExit("Unable to communicate with the CrowdStrike API. Check permissions.")

if not host_ids["body"]["resources"]:
    raise SystemExit("Unable to find any hosts matching the specified search string.\n"
                     f"Searched for: {BOLD}{HOST_MATCH}{NOCOLOR}"
                     )

# Retrieve the details for these AIDs so we can lookup the hostnames
devices = hosts.get_device_details(ids=host_ids["body"]["resources"])["body"]["resources"]

# Create a mapping dictionary from AID to hostname
# We'll use this later to display hostnames for results
device_map = {}
for device in devices:
    hostname = device.get("hostname", "Not found")
    aid = device.get("device_id", "Not found")
    device_map[aid] = hostname

print("Starting sessions with target hosts.")
# Start a batch session with all the hosts we've identified.
# Note: I am not able to use Body Payload Abstraction for this call.
# This is due to issue 568 and is resolved in v1.0.5.
# More detail: https://github.com/CrowdStrike/falconpy/issues/568
body_payload = {
    "host_ids": host_ids["body"]["resources"],
    "queue_offline": True
}
session_init = rtr.batch_init_sessions(body=body_payload)
# Create a list to store all of our created session IDs
session_list = []
# Create a list to store AIDs of our queued sessions
queued_list = []
# Retrieve our batch ID
batch_id = session_init["body"]["batch_id"]
# Create a list of sessions returned
sessions = session_init["body"]["resources"]
# Output successful session connections
for session in sessions:
    # Grab the ID for this session
    session_id = sessions[session]['session_id']
    if session_id:
        if sessions[session]["offline_queued"]:
            queued_list.append(session_id)
            print(f"Session with {BOLD}{device_map[session]}{NOCOLOR} QUEUED.")
        else:
            # Append this ID to our session list
            session_list.append(session_id)
            print(f"Session with {BOLD}{device_map[session]}{NOCOLOR} started successfully.",
                  f"[{session_id}]"
                  )
    else:
        if sessions[session]["offline_queued"]:
            queued_list.append(device_map[session])
            print(f"Session with {BOLD}{device_map[session]}{NOCOLOR} QUEUED.")
        else:
            for err in sessions[session]["errors"]:
                ecode = err["code"]
                emsg = err["message"]
                print(f"Session with {BOLD}{device_map[session]}{NOCOLOR} FAILED.",
                      f"[{ecode}] {emsg}"
                      )

print(f"\nExecuting command (`{COMMAND}`) against target hosts.\n")
# Execute our command against the hosts in our batch session
cloud_request = rtr_admin.batch_admin_command(base_command="runscript",
                                              batch_id=batch_id,
                                              persist_all=True,
                                              command_string=f"runscript -Raw=```{COMMAND}```"
                                              )

print("Closing sessions with target hosts.")
# Close all of our open sessions with these hosts
for session_id in session_list:
    if rtr.delete_session(session_id=session_id)["status_code"] == 204:
        print(f"Session {BOLD}{session_id}{NOCOLOR} deleted successfully.")
    else:
        print(f"Unable to delete session {BOLD}{session_id}{NOCOLOR}.")

# Parse and output the results
if cloud_request["status_code"] == 201:
    results = cloud_request["body"]["combined"]["resources"]
    for result in results:
        out_data = results[result]
        if out_data["stdout"] or out_data["stderr"] or out_data["errors"]:
            print(f"{BOLD}\n{device_map[result]}{NOCOLOR}")
        if out_data["stdout"]:
            print(out_data["stdout"])
        if out_data["stderr"]:
            print(out_data["stderr"])
        if out_data["errors"]:
            for err in out_data["errors"]:
                ecode = err["code"]
                emsg = err["message"]
                print(f"[{ecode}] {emsg}")
else:
    # An error occurred
    for err in cloud_request["body"]["errors"]:
        ecode = err["code"]
        emsg = err["message"]
        print(f"[{ecode}] {emsg}")

# Wait for queued sessions
# This is probably not how you would want to handle this in a real world scenario.
# CrowdStrike will wait up to 7 DAYS for a machine to be restored to service so that
# it can execute your queued command.  This means running a loop and waiting is
# probably not the way you wanna go.  (A better scenario would be to track these
# session / cloud request IDs for later confirmation.) For our example scenario
# where we are turning instances off and back on to see the result, this is fine.
if queued_list:
    cloud_requests = {}
    for ses_id in queued_list:
        queued = rtr.list_queued_sessions(ids=ses_id)
        if queued["status_code"] == 200:
            for sess in queued["body"]["resources"]:
                if sess["status"] == "PENDING":
                    for cmd in sess["Commands"]:
                        if cmd["cloud_request_id"] not in cloud_requests:
                            print(f"Device offline ({device_map[sess['aid']]}).",
                                  f" Request is queued ({cmd['cloud_request_id']})."
                                  )
                            cloud_requests[device_map[sess["aid"]]] = cmd["cloud_request_id"]
                else:
                    # It completed while we were creating our list, check for each command
                    for key, val in cloud_requests.items():
                        print(f"{BOLD}\n{key}{NOCOLOR}")
                        # Retrieve the results (didn't bother to check for chunked responses here)
                        status = rtr_admin.check_admin_command_status(
                            cloud_request_id=val
                            )["body"]["resources"]
                        # Display the results
                        for result in status:
                            if result["stdout"]:
                                print(result["stdout"])
                            if result["stderr"]:
                                print(result["stderr"])

    # Boolean to track the status of our results retrieval
    ALL_DONE = False
    for ses_id in queued_list:
        while not ALL_DONE:
            # Retrieve our list of queued sessions
            queued = rtr.list_queued_sessions(ids=ses_id)
            if queued["status_code"] == 200:
                for sess in queued["body"]["resources"]:
                    if not sess["status"] == "PENDING":
                        # If it's not pending, we're interested in the result
                        # Regardless of status. For every queued command.
                        for key, val in cloud_requests.items():
                            print(f"{BOLD}\n{key}{NOCOLOR}")
                            # Retrieve the results (didn't bother to check for chunked responses)
                            status = rtr_admin.check_admin_command_status(
                                cloud_request_id=val
                                )["body"]["resources"]
                            # Display the results
                            for result in status:
                                if result["stdout"]:
                                    print(result["stdout"])
                                if result["stderr"]:
                                    print(result["stderr"])

                            # Break out of the loop. In a real world scenario
                            # we would have to track completion per cloud request.
                            # In this example, we'll run our loop until the first one
                            # completes, then iterate for the next one (which is also
                            # probably back online if you turned them both back on at
                            # the same time.)
                            ALL_DONE = True
                    else:
                        # Display our "still waiting..." message
                        current_time = time.strftime("%H:%M:%S", time.localtime())
                        print(
                            f"[ {current_time} ] Queued session not ready, sleeping for 20 seconds."
                            )
                        # Snooze for a bit
                        time.sleep(20)

            else:
                # Error occurred. Show the detail.
                for err in queued["body"]["errors"]:
                    ecode = err["code"]
                    emsg = err["message"]
                    print(f"[{ecode}] {emsg}")
