# flake8: noqa=W605  pylint: disable=W1401
"""CrowdStrike Falcon Sensor Download utility.

            CrowdStrike Falcon
 _______                               ______                        __                __
|   _   .-----.-----.-----.-----.----.|   _  \ .-----.--.--.--.-----|  .-----.---.-.--|  |
|   1___|  -__|     |__ --|  _  |   _||.  |   \|  _  |  |  |  |     |  |  _  |  _  |  _  |
|____   |_____|__|__|_____|_____|__|  |.  |    |_____|________|__|__|__|_____|___._|_____|
|:  1   |                             |:  1    /
|::.. . |                             |::.. . /                 - jshcodes@CrowdStrike
`-------'                             `------'

This example requires the crowdstrike-falconpy (0.6.2+) and tabulate packages.

Required API Scope - Sensor Download: READ
"""
from argparse import ArgumentParser, RawTextHelpFormatter
from tabulate import tabulate
try:
    from falconpy import APIHarness
except ImportError as no_falconpy:
    raise SystemExit(
        "The CrowdStrike SDK must be installed in order to use this utility.\n"
        "Install this application with the command `python3 -m pip install crowdstrike-falconpy`."
    ) from no_falconpy

parser = ArgumentParser(
        description=__doc__,
        formatter_class=RawTextHelpFormatter
        )
parser.add_argument('-k', '--key', help="CrowdStrike API Key", required=True)
parser.add_argument('-s', '--secret', help="CrowdStrike API Secret", required=True)
parser.add_argument('-a', '--all', help='Show all columns / Download all versions', required=False, action="store_true")
parser.add_argument('-d', '--download', help="Shortcut for '--command download'", required=False, action="store_true")
parser.add_argument('-c', '--command', help='Command to perform. (list or download, defaults to list)', required=False)
parser.add_argument('-o', '--os', help='Sensor operating system', required=False)
parser.add_argument('-v', '--osver', help='Sensor operating system version', required=False)
parser.add_argument('-n', '--filename', help="Name to use for downloaded file", required=False)
parser.add_argument('-f',
                    '--format',
                    help='Table format to use for display.\n'
                    '(plain, simple, github, grid, fancy_grid, pipe, orgtbl, jira, presto, \n'
                    'pretty, psql, rst, mediawiki, moinmoin, youtrack, html, unsafehtml, \n'
                    'latext, latex_raw, latex_booktabs, latex_longtable, textile, tsv)',
                    required=False
                    )
args = parser.parse_args()
CMD = args.command
if CMD == "" or not CMD:
    CMD = "list"
if args.download:
    CMD = "download"
CLIENTID = args.key
CLIENTSECRET = args.secret
OS = ""
if args.os:
    check_os = args.os.lower()
    if check_os in ["rhel", "centos", "oracle", "rhel/centos/oracle"]:
        OS = "RHEL/CentOS/Oracle"
    if check_os in ["amzn", "az", "amazon", "amazon linux"]:
        OS = "Amazon Linux"
    if check_os in ["sles", "suse"]:
        OS = "SLES"
    if check_os in ["ubuntu", "kali", "deb", "debian"]:
        OS = "Debian"
    if check_os in ["win", "windows", "microsoft"]:
        OS = "Windows"
    if check_os in ["mac", "macos", "apple"]:
        OS = "macOS"
    if check_os in ["container", "docker", "kubernetes"]:
        OS = "Container"
    if check_os in ["idp", "identity", "identity protection"]:
        OS = "Identity*"
OS_FILTER = ""
if OS:
    OS_FILTER = f"os:'{str(OS)}'"

FILENAME = ""
if args.filename:
    FILENAME = args.filename

FORMAT = "fancy_grid"
if args.format:
    FORMAT = args.format

SHOW_ALL = False
if args.all:
    SHOW_ALL = True

OSVER = ""
if args.osver:
    OSVER = args.osver

# Login to the Falcon API and retrieve our list of sensors
falcon = APIHarness(client_id=CLIENTID, client_secret=CLIENTSECRET)
sensors = falcon.command(action="GetCombinedSensorInstallersByQuery", filter=OS_FILTER)
if CMD in "list":
    # List sensors
    data = []
    headers = {
            "name": "Name",
            "description": "Description",
            "platform": "Platform",
            "os": "OS",
            "os_version": "OS Version",
            "sha256": "File Hash",
            "release_date": "Release Date",
            "version": "Version",
            "file_size": "File Size",
            "file_type": "File Type"
        }
    if not SHOW_ALL:
        headers.pop("description")
        headers.pop("platform")
        headers.pop("sha256")
        headers.pop("file_size")
        headers.pop("file_type")
    for sensor in sensors["body"]["resources"]:
        if OSVER in [sensor["os_version"], ""]:
            if not SHOW_ALL:
                sensor.pop("description")
                sensor.pop("platform")
                sensor.pop("sha256")
                sensor.pop("file_size")
                sensor.pop("file_type")
            data.append(sensor)
    # Show results
    if len(data) == 0:
        print("No results, check your filter and try your query again.")
    else:
        print(tabulate(data, headers=headers, tablefmt=FORMAT))
elif CMD in "download":
    # Download sensors
    DO_DOWNLOAD = True
    for sensor in sensors["body"]["resources"]:
        if OSVER in [sensor["os_version"], ""]:
            if DO_DOWNLOAD:
                print(f"Downloading {sensor['description']} version {sensor['version']}")
                if not FILENAME:
                    filename = sensor["name"]
                    if sensor["os"] in ["Windows", "macOS"]:
                        filename = f"{filename[:-4]}_{sensor['version']}{filename[len(filename)-4:]}"
                else:
                    filename=FILENAME
                download = falcon.command(action="DownloadSensorInstallerById", id=sensor["sha256"])
                if isinstance(download, dict):
                    raise SystemExit("Unable to download requested sensor.")
                with open(filename, "wb") as save_file:
                    save_file.write(download)
                if not SHOW_ALL:
                    DO_DOWNLOAD = False
else:
    print("Stop mumbling!")
