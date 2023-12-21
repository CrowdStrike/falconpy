"""Retrieve uptime using CrowdStrike Falcon Real Time Response.

 ___ ___ _______ __   __
|   Y   |   _   |  |_|__.--------.-----.
|.  |   |.  1   |   _|  |        |  -__|
|.  |   |.  ____|____|__|__|__|__|_____|
|:  1   |:  |
|::.. . |::.|  CrowdStrike FalconPy v1.2
`-------`---'

01.23.23 - Creation date, jshcodes@CrowdStrike
"""
from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime, timedelta
from falconpy import Hosts, RealTimeResponse, RealTimeResponseAdmin

def consume_arguments():
    """Consume provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-n", "--hostname",
                        help="Hostname to target.\nWill handled multiple matches.",
                        required=False
                        )
    parser.add_argument("-b", "--base_url",
                        help="CrowdStrike region.\nOnly required for GovCloud users.",
                        required=False,
                        default="auto"
                        )
    parser.add_argument("-l", "--last_seen",
                        help="Amount of time (in minutes) since the host was last seen.",
                        required=False,
                        default=30,
                        type=int
                        )
    req = parser.add_argument_group("required arguments")
    req.add_argument("-k", "--falcon_client_id",
                     help="CrowdStrike Falcon API client ID.",
                     required=True
                     )
    req.add_argument("-s", "--falcon_client_secret",
                     help="CrowdStrike Falcon API client secret.",
                     required=True
                     )

    return parser.parse_args()


def open_sdks(client_id: str, client_secret: str, base_url: str):
    """Return authenticated Service Class objects using the provided API credentials."""
    hosts_sdk = Hosts(client_id=client_id, client_secret=client_secret, base_url=base_url)
    rtr_sdk = RealTimeResponse(auth_object=hosts_sdk)
    rtr_admin_sdk = RealTimeResponseAdmin(auth_object=hosts_sdk)

    return hosts_sdk, rtr_sdk, rtr_admin_sdk


def retrieve_uptimes(detail: dict, sdk: RealTimeResponse, sdk_admin: RealTimeResponseAdmin):
    """Loop through our list of hosts and leverage RTR to retrieve the current uptime."""
    def check_rtr_result(rtr_result: dict, host_id: str, dev_id: str):
        """Check the returned RTR result for a result or an error message."""
        request_id = rtr_result["body"]["resources"][0]["cloud_request_id"]
        keyname = f"{host_id} [{dev_id}]"
        completed = False
        while not completed:
            # stdout will be small, so we can go with the default sequence_id of 0
            result = sdk_admin.check_admin_command_status(cloud_request_id=request_id)
            stdout = result["body"]["resources"][0]["stdout"]
            stderr = result["body"]["resources"][0]["stderr"]
            if stdout or stderr:
                completed = True
        sdk.delete_session(session_id=session_id)
        results[keyname] = stdout
        if stderr:
            results[keyname] = stderr
        print(f"RTR runscript command for uptime has been executed on {host_id} [{dev_id}].")

    results = {}
    # This example is not demonstrating Batch RTR session init, which depending on
    # the size of the list of hosts, may be a better solution here.
    for host in detail:
        hostname = host.get('hostname')
        device_id = host.get('device_id')
        platform = host.get('platform_name')
        session_init = sdk.init_session(device_id=device_id, queue_offline=False)
        if session_init["status_code"] != 201:
            # RTR session connection failure.
            print(f"Unable to open RTR session with {hostname} [{device_id}]")
        else:
            session_id = session_init["body"]["resources"][0]["session_id"]
            # Craft a command string based upon the platform we are targeting.
            if platform.lower() in ['mac', 'linux']:
                command_string = f"runscript -Raw=```{UPTIME_BASH}```"
            else:
                command_string = f"runscript -Raw=```{UPTIME_WIN}```"

            check_result = sdk_admin.execute_admin_command(device_id=device_id,
                                                           session_id=session_id,
                                                           base_command="runscript",
                                                           command_string=command_string
                                                           )
            if check_result["status_code"] != 201:
                # RTR command execution failure.
                print(f"Unable to execute RTR command on {hostname} [{device_id}].")
            else:
                check_rtr_result(check_result, hostname, device_id)

    return results


def retrieve_hosts(hostname_filter: str, sdk: Hosts, last_seen: int):
    """Retrieve the host details for hosts matching the host filter."""
    search_time = datetime.now() - timedelta(minutes=last_seen)
    search_time = search_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    host_filter = f"last_seen:>='{search_time}'"
    if hostname_filter:
        host_filter = f"{host_filter}+hostname:*'*{hostname_filter}*'"

    hosts_to_check = sdk.query_devices_by_filter_scroll(filter=host_filter)
    # Unsuccessful API result
    if hosts_to_check["status_code"] != 200:
        raise SystemExit("Unable to retrieve host list. Check credentials.")

    # No hosts returned
    if not hosts_to_check["body"]["resources"]:
        raise SystemExit("Unable to retrieve host detail. Check provided hostname filter.")

    hosts_detail = sdk.get_device_details(ids=hosts_to_check["body"]["resources"])

    if hosts_detail["status_code"] != 200:
        raise SystemExit("Unable to retrieve host detail. Check permissions / hostname.")

    return hosts_detail["body"]["resources"]


def find_nth(haystack: str, needle: str, nth: int):
    """Find the Nth instance of a substring within a string."""
    start = haystack.find(needle)
    while start >= 0 and nth > 1:
        start = haystack.find(needle, start+len(needle))
        nth -= 1
    return start


def convert_windows_time(incoming: str):
    """Convert Windows time stamps to human readable format."""
    cur_time = datetime.now()
    incoming = datetime.strptime(incoming[:incoming.find("+")][:incoming.find(".")], "%Y%m%d%H%M%S")
    delta: timedelta = cur_time - incoming
    hour_min = ':'.join(str(timedelta(seconds=delta.seconds)).split(':')[0:2])
    return f"up {delta.days} days, {hour_min}"


def display_results(result_list: dict):
    """Parse the returned result dictionary and display the results."""
    for host_id, output in result_list.items():
        article = "has been"
        if "LastBootUpTime" in output:
            output = convert_windows_time(output.replace("LastBootUpTime", "").strip())
        else:
            output = " ".join(output.split(" ")[2:-1])
            output = output[:find_nth(output, ",", 2)]
        col = output.find(":")
        comma = output.find(",")
        inc = 1 if output[col-2:col-1] == " " else 2
        if col > 0:
            output = f"{output[:comma+1]} {output[col-inc:col]} hours and {output[col+1:]} minutes"
        if "disabled" in output:
            output = "runscript commands disabled"
            article = "has"
        print(f"{host_id} {article} {output}")


# Store our uptime commands in constants for later use, adjust as desired.
UPTIME_BASH = """
#!/bin/bash
uptime
"""

UPTIME_WIN = """
wmic path Win32_OperatingSystem get LastBootUpTime
"""

if __name__ == "__main__":
    # Retrieve command line arguments.
    cmd_line = consume_arguments()
    # Open the necessary SDK Service Classes.
    hosts, rtr, rtr_admin = open_sdks(cmd_line.falcon_client_id,
                                      cmd_line.falcon_client_secret,
                                      cmd_line.base_url
                                      )
    # Retrieve a list of hosts that match the provided hostname (or all hosts),
    # retrieve the uptime from each host, and then print out the returned results.
    display_results(retrieve_uptimes(retrieve_hosts(cmd_line.hostname, hosts, cmd_line.last_seen),
                                     rtr,
                                     rtr_admin
                                     ))
