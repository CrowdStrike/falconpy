r"""CrowdStrike Bulk Command Execution example - Real Time Response Admin.

   ___           __  _______             ___
  / _ \___ ___ _/ / /_  __(_)_ _  ___   / _ \___ ___ ___  ___  ___  ___ ___
 / , _/ -_) _ `/ /   / / / /  ' \/ -_) / , _/ -_|_-</ _ \/ _ \/ _ \(_-</ -_)
/_/|_|\__/\_,_/_/   /_/ /_/_/_/_/\__/ /_/|_|\__/___/ .__/\___/_//_/___/\__/
                                                  /_/
                                                        FalconPy v1.0
                                                        jshcodes@CrowdStrike, 02.22.22

This simple example demonstrates performing batch administrative commands against
multiple hosts. The host list is calculated based upon a string match between the
hostname and a search string you provide at runtime. The command executed is also
provided at runtime, and passed to the target host in Raw format. (Default: `ls -al`)
Results are output to the screen broken out by host. You must provide your credentials
to the program at runtime, or have them pre-defined within your environment. These
environment variables are called FALCON_CLIENT_ID and FALCON_CLIENT_SECRET.

Requires: crowdstrike-falconpy v8.0+
API Scopes:
    Hosts       - READ
    RTR         - READ, WRITE
    RTR ADMIN   - READ, WRITE
"""
import os
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
                        required=True
                        )
    parser.add_argument("-t", "--timeout",
                        help="Timeout duration for command execution in seconds. (Max: 600)",
                        default="30",
                        required=False
                        )

    return parser.parse_args()


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

try:
    TIMEOUT = min(max(int(args.timeout), 30), 600)
except ValueError:
    raise SystemExit("You must specify an integer between 30 and 600 for timeout.")

HOST_MATCH = args.find

# Connect to the CrowdStrike API service collections
hosts = Hosts(client_id=CLIENT_ID,
              client_secret=CLIENT_SECRET
              )
rtr = RealTimeResponse(auth_object=hosts.auth_object)
rtr_admin = RealTimeResponseAdmin(auth_object=hosts.auth_object)

# Retrieve a list of host AIDs that match our search string
host_ids = hosts.query_devices_by_filter(filter=f"hostname:*'*{HOST_MATCH}*'")
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
# Start a batch session with all the hosts we've identified
session_init = rtr.batch_init_sessions(host_ids=host_ids["body"]["resources"])
# Create a list to store all of our created session IDs
session_list = []
# Retrieve our batch ID
batch_id = session_init["body"]["batch_id"]
# Create a list of sessions returned
sessions = session_init["body"]["resources"]
# Output successful session connections
for session in sessions:
    # Grab the ID for this session
    session_id = sessions[session]['session_id']
    # Append this ID to our session list
    session_list.append(session_id)
    print(f"Session with {BOLD}{device_map[session]}{NOCOLOR} started successfully.",
          f"[{session_id}]"
          )

print(f"\nExecuting command (`{COMMAND}`) against target hosts.\n")
# Execute our command against the hosts in our batch session
cloud_request = rtr_admin.batch_admin_command(base_command="runscript",
                                              batch_id=batch_id,
                                              timeout_duration=f"{TIMEOUT}s",
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
        print(f"{BOLD}\n{device_map[result]}{NOCOLOR}")
        out_data = results[result]
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

