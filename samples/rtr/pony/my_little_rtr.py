"""
 _______             __  _______ __                 _______
|   _   .-----.---.-|  ||       |__.--------.-----.|   _   .-----.-----.-----.-----.-----.-----.-----.
|.  l   |  -__|  _  |  ||.|   | |  |        |  -__||.  l   |  -__|__ --|  _  |  _  |     |__ --|  -__|
|.  _   |_____|___._|__|`-|.  |-|__|__|__|__|_____||.  _   |_____|_____|   __|_____|__|__|_____|_____|
|:  |   |                 |:  |                    |:  |   |           |__|
|::.|:. |                 |::.|                    |::.|:. |                    FalconPy v0.8.6+
`--- ---'                 `---'                    `--- ---'

CrowdStrike FalconPy demonstration - Real Time Response, Service Class version / aka. The My Little RTR demo

Pull system information from a host using the CrowdStrike RTR API, an open source ASCII art project and BASH.

Yes, it really does generate My Little Ponies. Thank you Glax!  https://gitlab.com/mattia.basaglia/ASCII-Pony

Created 08.16.21 - jshcodes@CrowdStrike
"""
#                                         __         __----__
#                                        /  \__..--''    _-__''-_
#                                       ( /  \            `-.''''`
#                                       | |   `-..__  .,     `.
#                         ___           ( '.  \ ____`\ )`-_    `.
#                  ___   (   `.         '\   __/   __\' /-``-.._ \
#                 (   `-. `.   `.       .|\_  (   / .-| |W)|    ``'  User     : root
#                  `-.   `-.`.   `.     |' ( ,'\ ( (WW| \` j         Hostname : sample-host.us-west-1.compute.internal
#          ..---'''''-`.    `.\   _\   .|   ',  \_\_`/   ``-.        IP       :
#        ,'            _`-,   `  (  |  |'     `.        \__/         Distro   :
#       /   _         ( ```    __ \  \ |     ._:7,______.-'          Kernel   : 4.14.232-177.418.amzn2.x86_64 x86_64
#      | .-'/          `-._   (  `.\  '':     \    /                 Uptime   : 32 days, 13:36
#      '`  /          .-''>`-. `-. `   |       |  (                  Load     : 0.00, 0.00, 0.00
#         -          /   /    `_: `_:. `.    .  \  \                 Shell    : /bin/bash
#         |          |  |  o()(   (      \   )\  ;  |                Packages :
#        .'          `. |   Oo `---:.__-'') /  )/   |                RAM      : 133M / 1.9G
#        |            | |  ()o            |/   '    |                CPU      : Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
#       .'            |/ \  o     /             \__/                 Swap     : 0B / 0B
#       |  ,         .|   |      /-,_______\       \                 Disk     : 1.7G / 13G
#      /  / )        |' _/      /     |    |\       \
#    .:.-' .'         )/       /     |     | `--,    \
#         /       .  / |      |      |     |   /      )
#    .__.'    ,   :|/_/|      |      |      | (       |
#    `-.___.-`;  / '   |      |      |      |  \      |
#           .:_-'      |       \     |       \  `.___/
#                       \_______)     \_______)
#
import argparse
import time     # You can prolly remove the delays
from argparse import RawTextHelpFormatter
try:
    from falconpy import OAuth2, Hosts, RealTimeResponse, RealTimeResponseAdmin

except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy


def inform(msg: str):
    """
    Provides informational updates to the user as the program progresses
    """
    print("%-80s" % msg, end="\r", flush=True)  # pylint: disable=C0209


def execute_command(passed_payload: str, hdr: str, cmd: str):
    """
    Executes a RTR Admin command, waits for it to complete,
    and then returns the result
    """
    passed_payload["command_string"] = cmd
    req = falcon_rtra.execute_admin_command(                        # Call the command
        body=passed_payload                                         # Execute the command
        )
    if req["status_code"] != 201:                                   # Confirm execution success
        raise SystemExit(                                           # There is no retry, crash out
            "Unable to execute command. "
            "No ponies for you! ಥ_ಥ"
            )
    request_id = req["body"]["resources"][0]["cloud_request_id"]    # Retrieve the cloud_request_id
    completed = False                                               # Boolean to track our command status
    inform(f"  Waiting on {hdr} to finish executing")
    cnt = 1
    while not completed:                                            # Keep requesting status until the command is completed
        inform(
            f"  Waiting on {hdr} to finish executing{'.' * cnt}"
            )
        cnt += 1
        requested = falcon_rtra.check_admin_command_status(         # Retrieve the results command
            cloud_request_id=request_id,                            # Passing in the cloud_request_id
            sequence_id=0                                           # Results are chunked, but we just need the first result
            )                                                       # Starting in v1.0.5, this value defaults to '0'.
        completed = requested["body"]["resources"][0]["complete"]   # Check to see if our command has finished executing

    inform(
        f"  Waiting on {hdr} to finish executing{'.' * cnt}done!"
        )
    time.sleep(.1)
    return requested                                                # Return our result


def remove_scripts(scripts: list):
    """
    Deletes all scripts in the list provided
    """
    inform("  Removing pony scripts")
    cnt = 1
    for script in scripts:                                          # Delete every script in the list provided
        inform(f"  Removing pony scripts{'.' * cnt}")
        falcon_rtra.delete_scripts(ids=falcon_rtra.list_scripts(
            filter=f"name:'{script}'"
            )["body"]["resources"][0]
        )
        cnt += 1
    inform(f"  Removing pony scripts{'.' * cnt}done!")
    time.sleep(.1)


def upload_scripts(scripts: list):
    """
    Uploads all scripts in the list provided
    """
    inform("  Uploading pony scripts")
    cnt = 1
    for script in scripts:                                          # Loop thru the three scripts defined below
        if "~/ponies/systempony" in script:                         # and upload them to CrowdStrike Cloud
            name = "create-pony"
            desc_stub = "generator"
        elif "rm -fR ~/ponies" in script:
            name = "cleanup-pony"
            desc_stub = "removal"
        else:
            name = "install-pony"
            desc_stub = "installer"
        inform(f"  Uploading pony scripts{'.' * cnt}")
        cnt += 1
        upload = falcon_rtra.create_scripts(
                data={
                    "name": name,
                    "content": script,
                    "platform": "linux",                            # This example only works on Linux
                    "permission_type": "private",
                    "description": f"Pony {desc_stub}"
                }, files=[(name, (name, 'application/script'))]
            )
        if upload["status_code"] not in [200, 409]:
            raise SystemExit("Unable to upload demo scripts")
    inform(f"  Uploading pony scripts{'.' * cnt}done!")
    time.sleep(.1)


def get_host_aid(host: str):
    """
    Retrieves the AID for a given hostname
    """
    inform("  Retrieving AID for target host")
    result = falcon_hosts.query_devices_by_filter(                     # Retrieve our test instance's AID
        filter=f"hostname:'{host}*'"                                # Filter our request to the Hosts API by hostname
        )
    if result["status_code"] == 200:
        if len(result["body"]["resources"]) == 0:
            raise SystemExit(
                    "%50s" % f"{' ' * 50}\nUnable to retrieve "     # pylint: disable=C0209
                    "AID for target.  ¯\_(ツ)_/¯\n"                 # noqa=W605 pylint: disable=W1401
                    "Check target hostname value."
                )
        returned = result["body"]["resources"][0]
        inform(f"  Retrieving AID for target host ({returned})")
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
    if session["status_code"] == 201:
        sess_id = session["body"]["resources"][0]["session_id"]
        inform(
            f"  Connecting to target...connected ({sess_id})"
            )
        time.sleep(.3)
    else:
        raise SystemExit("Unable to establish session with host")

    return sess_id


def delete_session(ses_id: str):
    """
    Deletes the RTR session as specified by session ID
    """
    inform("  Deleting session")
    falcon_rtr.delete_session(session_id=ses_id)                    # Delete our current RTR session
    inform("Cleanup complete, Friendship is Magic!\n")


def main():
    """
    Main routine
    """
    target_aid = get_host_aid(hostname)                             # Retrieve our test instance's AID
    session_id = init_session(target_aid)                           # Open a new session and store the session ID
    payload["session_id"] = session_id                              # Add the session ID to our command payload
    upload_scripts([PONY_INSTALL, PONY_EXEC, PONY_CLEANUP])         # Upload our pony scripts to CrowdStrike cloud
    execute_command(payload, "install ponies", INSTALL_COMMAND)     # Install our pony generator with the install-pony command
    execute_command(payload, "generate pony", PONY_COMMAND)         # Generate our pony with our create-pony command
    pony = execute_command(                                         # Retrieve our resulting pony system information display
        payload,
        "retrieve pony",
        READ_COMMAND
        )["body"]["resources"][0]["stdout"]                         # Our pony lives in the "stdout" field
    execute_command(payload, "remove ponies", CLEANUP_COMMAND)      # Remove our system pony installation with cleanup-pony
    remove_scripts(MY_LITTLE_PONIES)                                # Remove our pony scripts from CrowdStrike cloud
    delete_session(session_id)                                      # Delete our current RTR session
    print(pony)                                                     # Print the results of our script... pretty colors!


# Installs git and clones the ASCII-Pony GitLab project
PONY_INSTALL = """
#!/bin/bash
yum install git -y
git clone https://gitlab.com/mattia.basaglia/ASCII-Pony.git ~/ponies
"""
# Executes the systempony command,
# saving the output to a file
PONY_EXEC = """
#!/bin/bash
~/ponies/systempony > ~/pony.txt
"""
# Removes our systempony output file,
# and removes the ASCII-Pony project
PONY_CLEANUP = """
#!/bin/bash
rm ~/pony.txt
rm -fR ~/ponies
"""
# Command line help display banner
PONY_BANNER = """
 ⠴⢮⠭⠍⠉⠉⠒⠤⣀
⢀⢊　　　　　　 ⢱⠊⠑⡀
⠋⡎  ⣀⡠⠤⠠⠖⠋⢉⠉  ⡄⢸
⣘⡠⠊⣩⡅  ⣴⡟⣯⠙⣊  ⢁⠜   The My Little RTR demo
　　 ⣿⡇⢸⣿⣷⡿⢀⠇⢀⢎          FalconPy v0.6.0+
　 ⠰⡉  ⠈⠛⠛⠋⠁⢀⠜ ⢂
　 　 ⠈⠒⠒⡲⠂⣠⣔⠁   ⡇  ⢀⡴⣾⣛⡛⠻⣦
　　　　⢠⠃  ⢠⠞    ⡸⠉⠲⣿⠿⢿⣿⣿⣷⡌⢷
   ⢀⠔⠂⢼    ⡎⡔⡄⠰⠃      ⢣  ⢻⣿⣿⣿⠘⣷
 ⡐⠁    ⠸⡀  ⠏  ⠈⠃      ⢸　 ⣿⣿⣿⡇⣿⡇
 ⡇    ⡎⠉⠉⢳    ⡤⠤⡤⠲⡀   ⢇   ⣿⣿⣿⣇⣿⣷
 ⡇  ⡠⠃    ⡸    ⡇ ⡇ ⢱⡀ ⢣   ⠙⣿⣿⣿⣿⣿⡄
 ⠑⠊ 　 　⢰　   ⠇⢸  ⡇⡇ ⡇    ⢳⣿⣿⣿⣿⡇
　　　　⢠⠃    ⡸⡎  ⡜⡇  ⡇     ⠻⡏⠻⣿⣿⣄
　　　 ⣔⣁⣀⣀⡠⠁ ⠈⠉⠉⠁⣎⣀⣀⡸

   CrowdStrike - We STOP Breaches
"""
MY_LITTLE_PONIES = ["install-pony", "create-pony", "cleanup-pony"]  # The names of our uploaded pony scripts
BASE_COMMAND = "runscript"                                          # We're using runscript for our calls
INSTALL_COMMAND = "runscript -CloudFile='install-pony'"             # This command installs our system pony solution
PONY_COMMAND = "runscript -CloudFile='create-pony'"                 # This command generates our "Pony status display" file
READ_COMMAND = "cat ~/pony.txt"                                     # This command displays the contents of the pony file
CLEANUP_COMMAND = "runscript -CloudFile='cleanup-pony'"             # This command removes the system pony solution
payload = {"base_command": BASE_COMMAND}                            # Our initial payload, with our base command loaded
parser = argparse.ArgumentParser(                                   # Argument parser for our command line
    description=PONY_BANNER, formatter_class=RawTextHelpFormatter
    )
parser.add_argument(                                                # Hostname to target
    '-t', '--target',
    help='Hostname of your target.\nMust be part of your CID.',
    required=True
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
falcon_auth = OAuth2(                                               # Create an instance of our authentication class
    client_id=args.key,                                             # and authenticate to the API
    client_secret=args.secret,
    )
falcon_hosts = Hosts(auth_object=falcon_auth)                       # Connect to the Hosts API using our auth object
falcon_rtr = RealTimeResponse(auth_object=falcon_auth)              # Connect to the RTR API using our auth object
falcon_rtra = RealTimeResponseAdmin(auth_object=falcon_auth)        # Connect to the RTR Admin API using our auth object

if __name__ == "__main__":
    main()
