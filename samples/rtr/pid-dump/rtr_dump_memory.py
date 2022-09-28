"""
 _______             __  _______ __                 _______
|   _   .-----.---.-|  ||       |__.--------.-----.|   _   .-----.-----.-----.-----.-----.-----.-----.
|.  l   |  -__|  _  |  ||.|   | |  |        |  -__||.  l   |  -__|__ --|  _  |  _  |     |__ --|  -__|
|.  _   |_____|___._|__|`-|.  |-|__|__|__|__|_____||.  _   |_____|_____|   __|_____|__|__|_____|_____|
|:  |   |                 |:  |                    |:  |   |           |__|
|::.|:. |                 |::.|                    |::.|:. |                    FalconPy v0.6.0+
`--- ---'                 `---'                    `--- ---'

CrowdStrike FalconPy demonstration - Real Time Response, Service Class version

Perform a memory dump for a specified PID using Real Time Response and CrowdStrike-FalconPy.

Created 08.19.21 - jshcodes@CrowdStrike
"""
import argparse                                                         # Argument parsing for the command line
import datetime                                                         # DateTime to calculate a Julian date
import time     # You can prolly remove the delays                      # Time handling - used for delays
import zipfile                                                          # Generic zip handling
import os                                                               # OS functions
import py7zr                                                            # 7zip handling
try:
    from falconpy.oauth2 import OAuth2                                      # CrowdStrike Authentication API
    from falconpy.hosts import Hosts                                        # CrowdStrike Hosts API
    from falconpy.real_time_response import RealTimeResponse                # CrowdStrike RTR API
    from falconpy.real_time_response_admin import RealTimeResponseAdmin     # CrowdStrike RTR Admin API
except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy


def get_dump_filename():
    """
    Creates a unique file name by calculating
    the Julian date based off of the current time.
    """
    fmt = '%Y-%m-%d %H:%M:%S'
    stddate = datetime.datetime.now().strftime(fmt)
    sdtdate = datetime.datetime.strptime(stddate, fmt)
    jdate = sdtdate.timetuple().tm_yday
    jdate = "{}{}".format(
        stddate.replace(
            "-",
            "").replace(
                ":",
                "").replace(
                    " ",
                    ""), jdate
                    )
    dump_fn = f"memdump-pid-{jdate}"                                # Format: memdump-pid-{SOME_NUMBER}
    return dump_fn


def get_indicator():
    """
    Tracks the current position of the progress indicator
    and returns it's value when requested.
    """
    global INDICATOR_POSITION                                       # pylint: disable=W0603  # indicator_position is global
    INDICATOR_POSITION += 1                                         # pylint: disable=E0602  # Increment it by 1
    if INDICATOR_POSITION >= len(indicator):                        # If our counter exceeds the list length
        INDICATOR_POSITION = 0                                      # Reset it back to zero

    return indicator[INDICATOR_POSITION]                            # Return our value


def inform(msg: str):
    """
    Provides informational updates to
    the user as the program progresses.
    """
    print("%-80s" % msg, end="\r", flush=True)                      # Dynamic user update messages


def execute_command(passed_payload: str, hdr: str, cmd: str):
    """
    Executes a RTR Admin command, waits for it to complete,
    and then returns the result
    """
    passed_payload["command_string"] = cmd
    req = falcon_rtra.execute_admin_command(                        # Call the command
        **passed_payload                                            # Execute the command
        )
    if req["status_code"] != 201:                                   # Confirm execution success
        raise SystemExit(                                           # There is no retry, crash out
            "%80s" % f"{' ' * 80}\nUnable to execute command: "
            f"[{req['body']['errors'][0]['code']}] "
            f"{req['body']['errors'][0]['message']}"
            )
    request_id = req["body"]["resources"][0]["cloud_request_id"]    # Retrieve the cloud_request_id
    completed = False                                               # Boolean to track our command status
    inform(f"  Waiting on {hdr} to finish executing")
    while not completed:                                            # Keep requesting status until the command is completed
        inform(
            f"  Waiting on {hdr} to finish executing...{get_indicator()}"
            )
        requested = falcon_rtra.check_admin_command_status(         # Retrieve the results command
            cloud_request_id=request_id,                            # Passing in the cloud_request_id
            sequence_id=0                                           # Results are chunked, but we just need the first result
            )
        completed = requested["body"]["resources"][0]["complete"]   # Check to see if our command has finished executing

    inform(
        f"  Waiting on {hdr} to finish executing...done!"           # Inform the user of success
        )
    time.sleep(.1)
    return requested                                                # Return our result


def remove_scripts(scripts: list):
    """
    Deletes all scripts in the list provided
    """
    inform("  Removing helper scripts")                             # Provide a status update to show progress
    cnt = 1
    for script in scripts:                                          # Delete every script in the list provided
        inform(f"  Removing helper scripts{'.' * cnt}")             # Provide a status update to show progress
        falcon_rtra.delete_scripts(ids=falcon_rtra.list_scripts(    # Delete the script by ID using a nested
            filter=f"name:'{script}'"                               # call to list_scripts using the script name
            )["body"]["resources"][0]                               # as a filter
        )
        cnt += 1                                                    # Counter to show progress
    inform(f"  Removing helper scripts{'.' * cnt}done!")            # Inform the user of success
    time.sleep(.1)


def upload_scripts(scripts: list):
    """
    Uploads all scripts in the list provided
    """
    inform("  Uploading helper scripts")
    cnt = 1
    for script in scripts:                                          # Loop thru the scripts defined below
        if "yum install gdb -y" in script:                          # and upload them to CrowdStrike Cloud
            name = "pid-memdump"                                    # Use the script contents to determine
            desc_stub = "PID memory dump"                           # the names / descriptions to use
        else:
            name = "pid-memdump-cleanup"
            desc_stub = "PID dump cleanup"
        inform(f"  Uploading helper scripts{'.' * cnt}")            # Inform the user of our progress
        cnt += 1
        upload = falcon_rtra.create_scripts(
                data={
                    "name": name,
                    "content": script,
                    "platform": "linux",                            # This example only works on Linux
                    "permission_type": "private",                   # This example only works for your API key
                    "description": f"Helper {desc_stub}"
                }, files=[(name, (name, 'application/script'))]
            )
        if upload["status_code"] not in [200, 409]:                 # Helper scripts don't force an overwrite
            raise SystemExit("Unable to upload helper scripts")
    inform(f"  Uploading helper scripts{'.' * cnt}done!")           # Inform the user of success
    time.sleep(.1)


def get_host_aid(host: str):
    """
    Retrieves the AID for a given hostname
    """
    inform("  Retrieving AID for target host")
    result = falcon_hosts.QueryDevicesByFilter(                     # Retrieve our test instance's AID
        filter=f"hostname:'{host}*'"                                # Filter our request to the Hosts API by hostname
        )
    if result["status_code"] == 200:
        if len(result["body"]["resources"]) == 0:                   # We got no results back from the API for this hostname
            raise SystemExit(
                    "%80s" % f"{' ' * 80}\nUnable to retrieve "
                    "AID for target.  ¯\_(ツ)_/¯\n"                 # noqa=W605 pylint: disable=W1401  # Linters hate my art
                    "Check target hostname value."
                )
        returned = result["body"]["resources"][0]
        inform(f"  Retrieving AID for target host ({returned})")    # Provide a status update so they know we found it
    else:
        returned = False

    return returned


def init_session(aid: str):
    """
    Initializes a RTR session with
    the host matching the AID provided
    """
    inform("  Connecting to target")
    session = falcon_rtr.init_session(body={                        # Open a new session and store the session ID
        "device_id": aid                                            # Pass in the AID we looked up previously
        })
    if session["status_code"] == 201:                               # Successfully connected
        sess_id = session["body"]["resources"][0]["session_id"]     # Retrieve our session_id
        inform(                                                     # Inform the user that we're connected
            f"  Connecting to target...connected ({sess_id})"
            )
        time.sleep(.3)
    else:
        raise SystemExit("Unable to establish session with host")   # Cannot create a session, crash out

    return sess_id


def delete_session(ses_id: str):
    """
    Deletes the RTR session as specified by session ID
    """
    inform("  Deleting session")
    falcon_rtr.delete_session(session_id=ses_id)                    # Delete our current RTR session
    inform("Cleanup complete    \n")                                # Inform the user, we're done


def upload_helper(helper: str):
    """
    Uploads the dynamically generated utility helper
    to CrowdStrike cloud for execution.
    """
    helper_payload = {
        "Description": "Memory Dump helper script",
        "platform": ["linux"],
        "permission_type": "private",
        "Name": helper
    }
    with open(helper, "rb") as helper_script:
        file = [('file',                                            # Payload containing our dynamically generated script file
                (helper,
                 helper_script.read(),
                 'application/octet-stream'
                 )
                 )]
    res = falcon_rtra.create_put_files(                             # Upload our dynamically generated script file
        data=helper_payload,
        files=file
        )
    if res["status_code"] == 409:                                   # This helper already exists and may be stale
        remove_helper(helper)                                       # Remove it
        res = falcon_rtra.create_put_files(                         # ... and upload it again
            data=payload,
            files=file
            )
    elif res["status_code"] not in [200, 201]:                      # Upload failure
        raise SystemExit(                                           # Crash out, we need this helper to continue
            "%80s" % f"{' ' * 80}\nUnable to upload memory dump helper"
            )
    inform(f"  Helper {helper} uploaded")                           # Inform the user of successful upload


def remove_helper(helper: str):
    """
    Removes the dynamically generated utility helper
    from CrowdStrike cloud.
    """
    helper_lookup = falcon_rtra.list_put_files(                     # Retrieve our helper ID by looking for it's name
        filter=f"name:'{helper}'"
        )
    if helper_lookup["status_code"] == 200:                         # Found it
        helper_id = helper_lookup["body"]["resources"][0]           # Grab the ID
        delete_result = falcon_rtra.delete_put_files(               # Delete it using the ID we just looked up
            ids=helper_id
            )
        if delete_result["status_code"] != 200:                     # Delete failed
            inform("  Unable to remove helper file")                # Inform the user and continue
        else:
            inform(f"  Helper {helper} removed")                    # Inform the user of success


def main():
    """
    Main routine
    """
    target_aid = get_host_aid(hostname)                             # Retrieve our test instance's AID
    session_id = init_session(target_aid)                           # Open a new session and store the session ID
    payload["session_id"] = session_id                              # Add the session ID to our command payload
    if command.lower() == "ps":                                     # They've requested a list of running processes
        procs = execute_command(                                    # Execute the 'ps' command
            payload,
            "get processes",
            PS_COMMAND
            )["body"]["resources"][0]["stdout"]
        print(procs)                                                # And print out the results

    else:                                                           # They've requested a dump
        if not process_id:                                          # ... but did not provided us a process ID
            raise SystemExit(                                       # Can't dump a process without an ID, crash out
                "%80s" % f"{' ' * 80}"
                "\nProcess ID (--pid) is required to dump memory"
                )
        with open(MEMDUMP_HELPER, "w") as helper_file:              # Dynamically create our dump helper script
            helper_file.write(MEMDUMP_HELPER_CONTENT)

        upload_helper(MEMDUMP_HELPER)                               # Upload this file to CrowdStrike cloud
        payload["base_command"] = "put"                             # Change our base_command to 'put'
        execute_command(payload, "put memdump utility", PUT_COMMAND)
        upload_scripts([PID_MEMDUMP, PID_MEMDUMP_CLEAN])
        payload["base_command"] = "runscript"                       # Change our base_command to 'runscript'
        execute_command(payload, "get PID memory", DUMP_COMMAND)    # Execute the dump of the PID's memory
        # print(dump_result["body"]["resources"][0]['stdout'])
        payload["base_command"] = "get"                             # Swap our base_command to 'get'
        # print(DUMP_FILENAME)
        # print(GET_COMMAND)
        get_result = execute_command(                               # Retrieve the dump zip file and upload it
            payload,                                                # to CrowdStrike cloud
            "get dump",
            GET_COMMAND
            )
        # print(get_result)
        req_id = get_result["body"]["resources"][0]["task_id"]      # Retrieve our task_id
        # print(cloud_request_id)
        status = False
        while not status:
            status = falcon_rtra.check_admin_command_status(        # Use the task_id to check our get file status
                cloud_request_id=req_id,
                sequence_id=0
                )["body"]["resources"][0]["complete"]
        # print(session_id)
        file_check = falcon_rtr.list_files(session_id=session_id)   # File is ready, call for a list of files for this session
        # print(file_check)
        if len(file_check["body"]["resources"]) > 0:                # At least one file was returned
            file_id = file_check["body"]["resources"][0]["sha256"]  # We only want the first one, there should only be one
            # print(file_id)
            download = falcon_rtr.get_extracted_file_contents(      # Retrieve the file as a CrowdStrike secured zip file
                sha256=file_id,                                     # Password will be "infected" even though this archive
                session_id=session_id,                              # DOES NOT contain malware, just a simple memory dump.
                filename=f"{DUMP_FILENAME}.zip"
                )

            if isinstance(download, dict):                          # Our download failed for some reason
                print(download)                                     # Print the API response to stdout
            else:
                with open(                                          # We received a valid file download
                        f"{DUMP_FILENAME}.zip",
                        "wb") as save_file:
                    save_file.write(download)                       # Save this file in our current folder as DUMP_FILENAME
            inform("  Extracting save file contents")
            archive = py7zr.SevenZipFile(                           # nosec - Open our downloaded archive file using the
                f"{DUMP_FILENAME}.zip",                             # password of "infected". Bandit will consider this
                mode="r",                                           # hard-coded password a low threat and cry about it.
                password="infected"
                )
            archive.extractall(path="./extracted")                  # Extract this archive into the "extracted" folder
            archive.close()                                         # Close the archive
            inform(" Extracting staging archive contents")
            with zipfile.ZipFile(                                   # Our extracted file will be a regular zip we
                    f"./extracted/{DUMP_FILENAME}.zip",             # created with our uploaded BASH script. Open
                    "r"                                             # this using regular unzip, no password required.
                    ) as zip_ref:
                zip_ref.extractall("./")                            # Extract our dump files to our local folder

            inform("  Removing temporary archive")
            os.remove(f"./extracted/{DUMP_FILENAME}.zip")           # Remove our initial zip download
            inform("  Removing temporary folder")
            os.removedirs("./extracted")                            # Remove our temporary working folder
            inform("  Removing staging archive")
            os.remove(f"{DUMP_FILENAME}.zip")                       # Remove our regular zip of dump files

        execute_command(                                            # Remove all artifacts from the file system
            payload,
            "remove artifacts",
            CLEANUP_COMMAND
            )
        remove_scripts(HELPER_SCRIPTS)                              # Remove our work scripts from CrowdStrike cloud
        remove_helper(MEMDUMP_HELPER)                               # Remove our memory dump helper script
        delete_session(session_id)                                  # Delete our current RTR session
        os.remove(MEMDUMP_HELPER)                                   # Remove our memory dump temporary file


parser = argparse.ArgumentParser(                                   # Argument parser for our command line
    description="FalconPy RTR demo"
    )
parser.add_argument(                                                # Hostname to target
    '-t', '--target',
    help='Hostname of your target.\nMust be part of your CID.',
    required=True
    )
parser.add_argument(                                                # Command to perform
    '-c', '--command',
    help="Command to perform against the host (ps or dump)",
    required=True
)
parser.add_argument(                                                # Command to perform
    '-p', '--pid',
    help="Process ID to dump",
    required=False
)
parser.add_argument(                                                # CrowdStrike API Client ID
    '-k', '--key',
    help='Your CrowdStrike API key ID\n'
    '     Required Scopes\n'
    '     Hosts:     READ\n'
    '     RTR:       WRITE\n'
    '     RTR Admin: WRITE', required=True
    )
parser.add_argument(                                                # CrowdStrike API Client secret
    '-s', '--secret',
    help='Your CrowdStrike API key secret', required=True
    )
args = parser.parse_args()                                          # Retrieve our provided command line arguments
hostname = args.target                                              # Grab the hostname of our target from the user
command = args.command
process_id = args.pid
falcon_auth = OAuth2(                                               # Create an instance of our authentication class
    client_id=args.key,                                             # and authenticate to the API
    client_secret=args.secret,
    )
falcon_hosts = Hosts(auth_object=falcon_auth)                       # Connect to the Hosts API using our auth object
falcon_rtr = RealTimeResponse(auth_object=falcon_auth)              # Connect to the RTR API using our auth object
falcon_rtra = RealTimeResponseAdmin(auth_object=falcon_auth)        # Connect to the RTR Admin API using our auth object


DUMP_FILENAME = get_dump_filename()                                 # The name of our dump file (Julian)
MEMDUMP_HELPER = "dump-pid-memory.sh"                               # The name of our dump helper script
# Installs gdb, moves the helper and executes
# the memory dump. Afterwards is zips the
# results into a file named after our DUMP_FILENAME
PID_MEMDUMP = f"""
#!/bin/bash
yum install gdb -y
cd /root
mv /{MEMDUMP_HELPER} /root
chmod +x /root/{MEMDUMP_HELPER}
./{MEMDUMP_HELPER} {process_id}
zip {DUMP_FILENAME} *.dump
rm *.dump
"""
# Removes the zip archive of dump results
# and the dump-pid-memory.sh helper script
PID_MEMDUMP_CLEAN = f"""
#!/bin/bash
rm /root/{DUMP_FILENAME}.zip
rm /root/{MEMDUMP_HELPER}
"""
# Content of the dump-pid-memory.sh helper script
MEMDUMP_HELPER_CONTENT = """#!/bin/bash

grep rw-p /proc/$1/maps \\
| sed -n 's/^\\([0-9a-f]*\\)-\\([0-9a-f]*\\) .*$/\\1 \\2/p' \\
| while read start stop; do \\
    gdb --batch --pid $1 -ex \\
        "dump memory $1-$start-$stop.dump 0x$start 0x$stop"; \\
done
"""
HELPER_SCRIPTS = ["pid-memdump", "pid-memdump-cleanup"]                             # The names of our uploaded scripts
BASE_COMMAND = "runscript"                                                          # We're using runscript for our calls
DUMP_COMMAND = f"runscript -CloudFile='pid-memdump' -CommandLine='{process_id}'"    # Command to perform the memory dump
PUT_COMMAND = f"put '{MEMDUMP_HELPER}'"                                             # Command to put the dump helper
GET_COMMAND = f"get /root/{DUMP_FILENAME}.zip"                                      # Command to retrieve the dump results
PS_COMMAND = "ps"                                                                   # Command to list processes
CLEANUP_COMMAND = "runscript -CloudFile='pid-memdump-cleanup'"                      # Command to remove all artifacts
payload = {"base_command": BASE_COMMAND}                                            # Initial payload with base_command loaded
INDICATOR_POSITION = 0                                                              # Position of our progress indicator
indicator = ["|", "/", "-", "\\"]

if __name__ == "__main__":
    main()
