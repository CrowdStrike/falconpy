r"""CrowdStrike Falcon Sensor Download utility.

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
import logging
from tabulate import tabulate
try:
    from falconpy import APIHarnessV2
except ImportError as no_falconpy:
    raise SystemExit(
        "The CrowdStrike SDK must be installed in order to use this utility.\n"
        "Install this application with the command `python3 -m pip install crowdstrike-falconpy`."
    ) from no_falconpy

def consume_arguments():
    """Consume any provided command line arguments."""
    parser = ArgumentParser(
            description=__doc__,
            formatter_class=RawTextHelpFormatter
            )
    parser.add_argument('-k', '--key', help="CrowdStrike API Key", required=True)
    parser.add_argument('-s', '--secret', help="CrowdStrike API Secret", required=True)
    parser.add_argument('-a', '--all', help='Show all columns / Download all versions',
                        required=False,
                        action="store_true",
                        default=False
                        )
    parser.add_argument('-d', '--download', help="Shortcut for '--command download'",
                        required=False,
                        default=False,
                        action="store_true"
                        )
    parser.add_argument('-n', '--nminus',
                        help='Download previous version (n-1, n-2, 0 = current, 2 = n-2)',
                        default=0,
                        required=False
                        )
    parser.add_argument('-c', '--command',
                        help='Command to perform. (list or download, defaults to list)',
                        required=False,
                        default="list"
                        )
    parser.add_argument('-o', '--os', help='Sensor operating system', required=False, default="")
    parser.add_argument('-v', '--osver',
                        help='Sensor operating system version',
                        required=False,
                        default=""
                        )
    parser.add_argument('-f', '--filename',
                        help="Name to use for downloaded file",
                        required=False,
                        default=""
                        )
    parser.add_argument('-t',
                        '--table_format',
                        help='Table format to use for display.\n'
                        '(plain, simple, github, grid, fancy_grid, pipe, orgtbl, jira, presto, \n'
                        'pretty, psql, rst, mediawiki, moinmoin, youtrack, html, unsafehtml, \n'
                        'latext, latex_raw, latex_booktabs, latex_longtable, textile, tsv)',
                        required=False, default="fancy_grid"
                        )
    parser.add_argument('-b', '--base_url',
                        help="CrowdStrike region (only required for usgov1)",
                        required=False,
                        default="auto"
                        )
    parser.add_argument('--debug',
                        help="Enable API debugging",
                        required=False,
                        default=False,
                        action="store_true"
                        )
    return parser.parse_args()

def get_version_map(sensor_versions: list):  # pylint: disable=R0914
    """Create a mapping of all available sensor versions."""
    version_map = {
        "windows": {},
        "mac": {},
        "linux": {}
    }

    for version in sensor_versions["body"]["resources"]:
        ver = version.get("version", None)
        plat = version.get("platform", None)
        os_name = version.get("os", None)
        os_ver = version.get("os_version", None)
        name = version.get("name", None)
        desc = version.get("description", None)
        sha = version.get("sha256", None)
        tracked = False
        current = False
        prev = False
        eldest = False
        if plat and os_name:
            for os_type, os_detail in version_map.get(plat, {}).items():
                if os_type == f"{os_name} {os_ver}".strip():
                    if not os_detail.get("current", {}):
                        os_detail["current"] = {}
                        os_detail["current"]["name"] = name
                        os_detail["current"]["version"] = ver
                        os_detail["current"]["description"] = desc
                        os_detail["current"]["sha256"] = sha
                        tracked = True
                    else:
                        current = True
                    if current and not os_detail.get("previous", {}):
                        os_detail["previous"] = {}
                        os_detail["previous"]["name"] = name
                        os_detail["previous"]["version"] = ver
                        os_detail["previous"]["description"] = desc
                        os_detail["previous"]["sha256"] = sha
                        tracked = True
                    elif current and os_detail.get("previous", {}):
                        prev = True
                    if current and prev and not os_detail.get("oldest", {}):
                        os_detail["oldest"] = {}
                        os_detail["oldest"]["name"] = name
                        os_detail["oldest"]["version"] = ver
                        os_detail["oldest"]["description"] = desc
                        os_detail["oldest"]["sha256"] = sha
                        tracked = True
                    elif current and prev and os_detail.get("oldest", {}):
                        eldest = True

            if not tracked and not current and not prev and not eldest:
                version_map[plat][f"{os_name} {os_ver}".strip()] = {}
                version_map[plat][f"{os_name} {os_ver}".strip()]["current"] = {
                    "name": name,
                    "version": ver,
                    "description": desc,
                    "sha256": sha
                }

    return version_map

def create_constants():
    """Create constants from the provided command-line arguments."""
    args = consume_arguments()
    cmd = args.command
    if args.download:
        cmd = "download"

    os_name = ""
    if args.os:
        check_os = args.os.lower()
        if check_os in ["rhel", "centos", "oracle", "rhel/centos/oracle"]:
            os_name = "RHEL/CentOS/Oracle"
        if check_os in ["amzn", "az", "amazon", "amazon linux"]:
            os_name = "Amazon Linux"
        if check_os in ["sles", "suse"]:
            os_name = "SLES"
        if check_os in ["ubuntu", "kali", "deb", "debian"]:
            os_name = "Debian"
        if check_os in ["win", "windows", "microsoft"]:
            os_name = "Windows"
        if check_os in ["mac", "macos", "apple"]:
            os_name = "macOS"
        if check_os in ["container", "docker", "kubernetes"]:
            os_name = "Container"
        if check_os in ["idp", "identity", "identity protection"]:
            os_name = "Identity*"

    os_filter = ""
    if os_name:
        os_filter = f"os:'{str(os_name)}'"
    else:
        if args.os:
            allowed = ["rhel", "centos", "oracle", "rhel/centos/oracle", "mac", "macos", "apple",
                       "amzn", "az", "amazon", "amazon linux", "ubuntu", "kali", "deb", "debian",
                       "sles", "suse", "win", "windows", "microsoft", "container", "docker",
                       "kubernetes", "idp", "identity", "identity protection"
                       ]
            raise SystemExit(f"Invalid operating system specified.\nAllowed values: {', '.join(allowed)}")
    return cmd, args.key, args.secret, os_filter, args.filename, args.table_format, args.all, \
        args.osver, args.nminus, args.debug, args.base_url


CMD, CLIENTID, CLIENTSECRET, OS_FILTER, FILENAME, FORMAT, SHOW_ALL, \
    OSVER, NMINUS, ENABLE_DEBUG, BASE_URL = create_constants()

if ENABLE_DEBUG:
    # Activate debugging if requested
    logging.basicConfig(level=logging.DEBUG)

# Login to the Falcon API and retrieve our list of sensors
falcon = APIHarnessV2(client_id=CLIENTID,
                      client_secret=CLIENTSECRET,
                      debug=ENABLE_DEBUG,
                      base_url=BASE_URL
                      )
sensors = falcon.command(action="GetCombinedSensorInstallersByQuery",
                         filter=OS_FILTER,
                         sort="version.desc"                         
                         )

if sensors["status_code"] == 401:
    raise SystemExit("Authentication failure (STATUS CODE {})".format(sensors["status_code"]))


elif CMD in "list":
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
    NMVER = "current"
    # Get a complete mapping of sensor versions, including n-1 and n-2
    version_detail = get_version_map(sensors)
    if NMINUS:
        if int(NMINUS) == 1:
            NMVER = "previous"
        elif int(NMINUS) == 2:
            NMVER = "oldest"
    dl_complete = []
    # Download sensors
    DO_DOWNLOAD = True
    for sensor in sensors["body"]["resources"]:
        full_name = f"{sensor['os']} {sensor['os_version']}".strip()
        if OSVER in [sensor["os_version"], ""]:
            if DO_DOWNLOAD and full_name not in dl_complete:
                plat_spec = sensor["platform"]
                if plat_spec:
                    sha_to_retrieve = version_detail[plat_spec][full_name][NMVER]["sha256"]
                    dl_desc = version_detail[plat_spec][full_name][NMVER]['description']
                    dl_ver = version_detail[plat_spec][full_name][NMVER]['version']
                    if not FILENAME:
                        fname = version_detail[plat_spec][full_name][NMVER]["name"]
                        if sensor["os"] in ["Windows", "macOS"]:
                            fname = f"{fname[:-4]}_{dl_ver}{fname[len(fname)-4:]}"
                    else:
                        fname=FILENAME
                    print(f"Downloading {dl_desc} version {dl_ver}")
                    download = falcon.command(
                        action="DownloadSensorInstallerById",
                        id=sha_to_retrieve
                        )
                    if isinstance(download, dict):
                        raise SystemExit("Unable to download requested sensor.")
                    with open(fname, "wb") as save_file:
                        save_file.write(download)
                    dl_complete.append(full_name)
                    if not SHOW_ALL:
                        DO_DOWNLOAD = False
else:
    print("Stop mumbling!")
