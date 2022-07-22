#!/usr/bin/env python3
r"""Execute a single RTR command across multiple hosts within multiple child tenants.

 _______ __            ______                         __ _______ __         __ __
|_     _|  |--.-----. |      |.----.-----.--.--.--.--|  |     __|  |_.----.|__|  |--.-----.
  |   | |     |  -__| |   ---||   _|  _  |  |  |  |  _  |__     |   _|   _||  |    <|  -__|
  |___| |__|__|_____| |______||__| |_____|________|_____|_______|____|__|  |__|__|__|_____|

     ___ ___       __ __   __  _______ ___ ______
    |   Y   .--.--|  |  |_|__||   _   |   |   _  \
    |.      |  |  |  |   _|  ||.  1___|.  |.  |   \
    |. \_/  |_____|__|____|__||.  |___|.  |.  |    \
    |:  |   |                 |:  1   |:  |:  1    /
    |::.|:. |                 |::.. . |::.|::.. . /
    `--- ---'                 `-------`---`------'

 ______  _______ _______ _______ _     _
 |_____] |_____|    |    |       |_____|
 |_____] |     |    |    |_____  |     |

            _______  _____  _______ _______ _______ __   _ ______
            |       |     | |  |  | |  |  | |_____| | \  | |     \
            |_____  |_____| |  |  | |  |  | |     | |  \_| |_____/

                        _______ _     _ _______ _______ _     _ _______  _____   ______
                        |______  \___/  |______ |       |     |    |    |     | |_____/
                        |______ _/   \_ |______ |_____  |_____|    |    |_____| |    \_

                                                                    FalconPy v1.1.5
"""
import os
import json
import time
from argparse import ArgumentParser, RawTextHelpFormatter
import concurrent.futures
from falconpy import (
    FlightControl,
    Hosts,
    RealTimeResponseAdmin,
    RealTimeResponse
)


class Tracker:
    """Progress indicator class to track our progress."""

    def __init__(self):
        """Construct an instance of the progress indicator class."""
        self.cids = 0
        self.success = 0
        self.queued = 0
        self.missed = 0
        self.hosts = 0

    def tenant(self):
        """Increment the number of tenants processed."""
        self.cids += 1

    def complete(self):
        """Increment the number of successful command executions."""
        self.success += 1

    def queue(self):
        """Increment the number of queued command executions."""
        self.queued += 1

    def host(self):
        """Incremement the number of hosts returned by the lookup queries."""
        self.hosts += 1

    def no_match(self):
        """Increment the number of failed commands due to no host matches."""
        self.missed += 1

    def message(self):
        """Return the progress as a concatenated string."""
        return "".join([
            f"{self.hosts} hosts tested across {self.cids} children. ",
            f"{self.missed if self.missed > 0 else ''}",
            f"{' children returned no matches. ' if self.missed > 0 else ''}",
            f"{self.success} commands executed and {self.queued} queued."
            ])


def init_session(rtr_sdk: RealTimeResponse, aid: list or str):
    """Initialize a RTR session with the host matching the AID provided."""
    def do_init():
        """Perform a batch init sessions operation using the AID list provided."""
        return rtr_sdk.batch_init_sessions(host_ids=aid, queue_offline=True)

    # Simple rate limit example solution
    max_tries = 3
    tries = 0
    while True:
        session = do_init()
        if session["status_code"] == 201:
            batch_id = session["body"]["batch_id"]
            break
        if session["status_code"] == 429:
            tries += 1
            if tries > max_tries:
                # Max tries exceeded, stop trying
                batch_id = (429, "Rate limit exceeded")
                break
            print("Rate limit met, pausing")
            time.sleep(2*tries)  # Wait for 2 seconds, then 4 seconds, then finally 6 seconds.
        else:
            batch_id = (session["body"]["errors"][0]["code"],
                        session["body"]["errors"][0]["message"]
                        )
            break

    return batch_id


def delete_session(rtr_sdk: RealTimeResponse, ses_id: str):
    """Delete an RTR session as specified by session ID and return the status code."""
    return rtr_sdk.delete_session(session_id=ses_id)["status_code"]


# pylint: disable=R0914
def execute_command(rtra_sdk: RealTimeResponseAdmin, cmd: str, bat_id: str):
    """Execute a RTR Admin command, wait for it to complete, and then return the result."""
    # Calculate base_command based upon the value of the command string
    base_cmd = cmd.split(" ")[0]
    command_str = cmd
    if SCRIPT:
        # If they've selected advanced script execution
        base_cmd = "runscript"
        command_str = f"runscript -Raw=```{cmd}```"
    # Execute the command against the batch of hosts
    req = rtra_sdk.batch_admin_command(command_string=command_str,
                                       base_command=base_cmd,
                                       batch_id=bat_id,
                                       timeout_duration=f"{TIMEOUT}s"
                                       )
    returned = {}
    if req["status_code"] != 201:  # pylint: disable=R1702
        # Command execution failed, return the error message
        try:
            returned[bat_id] = {
                "cloud_request_id": "Failed",
                "session_id": "Failed",
                "result": f"{req['body']['combined']['errors'][0]['message']} ({bat_id})"
                }
        except KeyError:
            # Malformed return payload
            returned[bat_id] = {
                "cloud_request_id": "Failed",
                "session_id": "Failed",
                "result": f"{req['body']['errors'][0]['message']} ({bat_id})"
                }
    else:
        for device_id, session in req["body"]["combined"]["resources"].items():
            try:
                request_id = session["task_id"]
                ses_id = session["session_id"]
                if session["offline_queued"]:
                    # Command was queued offline
                    returned[device_id] = {
                        "cloud_request_id": request_id,
                        "session_id": ses_id,
                        "result": None
                    }
                else:
                    # Command was executed
                    completed = False
                    while not completed:
                        # Check the status of the command execution
                        requested = rtra_sdk.check_admin_command_status(
                            cloud_request_id=request_id,
                            sequence_id=0
                            )
                        if "resources" in requested["body"]:
                            completed = requested["body"]["resources"][0]["complete"]
                        else:
                            # Invalid return payload
                            returned[device_id] = {
                                "cloud_request_id": request_id,
                                "session_id": ses_id,
                                "result": "Unable to complete command execution"
                            }

                    exec_result = []
                    results = requested["body"]["resources"]
                    for result in results:
                        # Retrieve the contents of stdout and stderr
                        exec_result.append(result["stdout"])
                        exec_result.append(result["stderr"])
                    # Command was executed, return the result
                    returned[device_id] = {
                        "cloud_request_id": request_id,
                        "session_id": ses_id,
                        "result": "\n".join(exec_result)
                    }
            except KeyError:
                # Unable to retrieve the cloud_request_id from the session
                # More than likely session could not be established
                returned[device_id] = {
                    "cloud_request_id": "Failed",
                    "session_id": "Failed",
                    "result": session["errors"][0]["message"]
                }


    return returned


def run_test(kid: str):  # pylint: disable=R0912,R0914,R0915
    """Execute the specified command on the batch of hosts retrieved using the provided filter."""
    def connect_to_hosts():
        """Return an authenticated Hosts Service Class object."""
        return Hosts(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     member_cid=kid
                     )
    # Increment the number of CIDs we have iterated through
    progress.tenant()
    # Dictionary to track our queued executions
    queued = {}
    # Create an instance of the Hosts Service Class,
    # using our child tenant ID for the member_cid value.
    # Add a rate limit check here to back us off if we're
    # hitting our maximum requests per minute
    max_attempts = 3
    attempt = 0
    while True:
        attempt += 1
        hosts = connect_to_hosts()
        if hosts.token_status == 201:
            break
        if hosts.token_status == 429:
            if attempt > max_attempts:
                break
            print("Rate limit met, pausing")
            time.sleep(2*attempt)
        else:
            # Break out on non-rate limit errors
            break

    # Retrieve a list of endpoint AIDs that match our provided search filter
    check = hosts.query_devices_by_filter(limit=LIMIT, filter=FILTER, sort=SORT)
    check_len = 0
    if "resources" in check["body"]:
        # Number of devices returned that match our filter
        check_len = len(check["body"]["resources"])

    # Add our CID-specific header for terminal output
    display = [f"Tenant:\033[1m {kid}\033[0m "
               f"[Token: {hosts.token_status}] ",
               f"[Query: {check['status_code']}] ",
               f"({check_len} device{'s' if check_len > 1 or check_len <= 0 else ''} found)\n"
               ]

    if check_len:
        # Create instances of the Real Time Response and Real Time Response
        # Service Classes using our prexisting auth_object from Hosts.
        rtr = RealTimeResponse(auth_object=hosts.auth_object)
        rtr_admin = RealTimeResponseAdmin(auth_object=hosts.auth_object)
        # Batch ID for the session batch
        batch = init_session(rtr, check["body"]["resources"])
        if not isinstance(batch, tuple):
            for device_id, rtr_output in execute_command(rtr_admin, COMMAND, batch).items():
                # Increment the number of hosts we have executed the command against
                progress.host()
                # We're done with this RTR session
                delete_session(rtr, rtr_output["session_id"])
                if not rtr_output["result"]:
                    # This host's execution was queued
                    rtr_msg = "".join([
                        f"RTR batch: {batch}) command queued ",
                        f"(device ID: {device_id}, request ID: {rtr_output['cloud_request_id']})"
                    ])
                    # Increment the queued count
                    progress.queue()
                    if kid not in queued:
                        queued[kid] = {}
                    queued[kid][device_id] = rtr_output["cloud_request_id"]
                else:
                    # This host's execution completed successfully
                    rtr_msg = rtr_output["result"]
                    # Increment the success count
                    progress.complete()
                    result_folder = os.path.join(FOLDER, kid)
                    if not os.path.isdir(result_folder):
                        # Our results folder doesn't exist, create it
                        os.makedirs(result_folder)
                    with open(os.path.join(result_folder, f"{device_id}_{batch}.txt"),
                              "w",
                              encoding="utf-8") as res:
                        # Write the result to the output save file
                        res.write(rtr_msg)
                if rtr_msg[0] == "\n":
                    # strip any leading CRs
                    rtr_msg = rtr_msg[1:]
                # Add this result to the terminal output
                display.append(f"\033[1m{device_id}\033[0m\n{rtr_msg}\n")
        else:
            # This CID returned no hosts for the filter we provided
            progress.no_match()
            # Add this result to the terminal output
            display.append(f"[{batch[0]}] {batch[1]}\n")

    if queued:
        # Dump the list of queued executions using the CID and batch ID for a filename
        with open(os.path.join(FOLDER, f"{kid}_{batch}.json"), "w", encoding="utf-8") as pending:
            json.dump(queued, pending, indent=4)

    # Return our concatenated output for display
    return "".join(display)


def parse_command_line():  # pylint: disable=R0914
    """Ingest the provided command line parameters and handle any input errors."""
    # Configure argument parsing
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-k", "--falcon_client_id",
                        help="CrowdStrike Falcon API Client ID",
                        required=False
                        )
    parser.add_argument("-s", "--falcon_client_secret",
                        help="CrowdStrike Falcon API Client Secret",
                        required=False
                        )
    parser.add_argument("-m", "--multithread",
                        help="Leverage multiprocessing when executing the demonstration",
                        required=False,
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-d", "--output_folder",
                        help="Folder to output saved results",
                        required=False,
                        default="executions"
                        )
    parser.add_argument("-f", "--filter",
                        help="FQL string to use to limit target hosts. "
                        "(Defaults to all Windows hosts.)",
                        required=False,
                        default="platform_name:'Windows'"
                        )
    parser.add_argument("-o", "--sort",
                        help="FQL string to use to sort returned host results.",
                        required=False,
                        default="last_seen|desc"
                        )
    parser.add_argument("-l", "--limit",
                        help="Number of hosts to return per CID. (Maximum: 5000)",
                        required=False,
                        default=3
                        )
    parser.add_argument("-c", "--command",
                        help="Command to execute across all targeted hosts. "
                        "(Defaults to return environment details.)",
                        required=False,
                        default="ls"
                        )
    parser.add_argument("-t", "--timeout",
                        help="Batch execution timeout in seconds. (Defaults to 120.)",
                        required=False,
                        default=120
                        )
    parser.add_argument("-n", "--number_of_threads",
                        help="Number of threads to spawn, ignored when not multithreaded. "
                        "Not required.",
                        required=False,
                        default=min(32, (os.cpu_count() or 1) * 4)
                        )
    parser.add_argument("-x", "--script_execution",
                        help="Executes the command in raw format using runscript."
                        "(Defaults to regular execution.)",
                        required=False,
                        default=False,
                        action="store_true"
                        )

    args = parser.parse_args()
    # Fall back to environment variables (if present) when they do not provide us keys
    if not args.falcon_client_id:
        args.falcon_client_id = os.getenv("FALCON_CLIENT_ID")
    if not args.falcon_client_secret:
        args.falcon_client_secret = os.getenv("FALCON_CLIENT_SECRET")

    # Return all command line arguments back to be used for constants
    return args.falcon_client_id, args.falcon_client_secret, args.multithread, \
        args.output_folder, args.filter, args.sort, args.limit, args.command, \
        args.script_execution, args.timeout, min(100, int(args.number_of_threads))


def retrieve_children():
    """Connect to the Flight Control API and retrieve a list of child tenants."""
    mssp = FlightControl(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    print("Retrieving list of available child CIDs")
    all_children = mssp.query_children()
    if all_children["status_code"] != 200:
        # No children returned, stop processing.
        raise SystemExit("Unable to retrieve children.")

    return all_children["body"]["resources"]


# Retrieve our command line arguments
CLIENT_ID, CLIENT_SECRET, MULTITHREAD, FOLDER, FILTER, \
    SORT, LIMIT, COMMAND, SCRIPT, TIMEOUT, THREADS = parse_command_line()

# Retrieve a list of children for the credentials provided
kids = retrieve_children()

# Tracker to log our progress for final output
progress = Tracker()

if not os.path.isdir(FOLDER):
    # If our output folder does not exist, create it
    os.makedirs(FOLDER)

if not MULTITHREAD:
    # This example demonstrates linear execution in a single threaded process.
    # For most scenarios, you should not hit the rate limit using this method,
    # but overall execution time will be longer.
    #
    for child in kids:
        print(run_test(child))
else:
    # This is an example of how we can accomplish this task using multithreading.
    # Depending on how many CIDs we have to go through, we will probably hit the
    # rate limit using this method. Typically, you will receive results faster
    # using this solution.
    #
    with concurrent.futures.ThreadPoolExecutor(THREADS) as executor:
        futures = {
            executor.submit(run_test, child) for child in kids
        }
        for fut in concurrent.futures.as_completed(futures):
            print(fut.result())

# Output the final results for all tenants and hosts tested
print(progress.message())
