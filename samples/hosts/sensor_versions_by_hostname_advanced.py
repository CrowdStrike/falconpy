r"""Advanced sensor versions by hostname lookups.

    /   /                                                      /   /
    | O |- - - - - - - - - - - - - - - - - - - - - - - - - - - | O |
    |   |  ____ ____ ____ _  _ ___  ____ ___ ____ _ _  _ ____  |   |
    | O |  |___ |--< [__] |/\| |__> ====  |  |--< | |-:_ |===  | O |
    |   |                                                      |   |
    | O |           ENDPOINT SENSOR VERSION REPORT             | O |
    |   |                                                      |   |
    | O |  1   ~~~~~~~~~~~~~                    6.44.3232.0    | O |
    |   |  2   ~~~~~~~~~~~~~~~                  6.44.3232.0    |   |
    | O |  3   ~~~~~~~~~~~                      6.42.5750.1    | O |
    |   |  4   ~~~~~~~~~~~                      6.46.2001.0    |   |
    | O |  5   ~~~~~~~~~~~~~                    6.44.3232.0    | O |
    |   |  6   ~~~~~~~~~~~~~~~                  6.44.3232.0    |   |
    | O |  7   ~~~~~~~~~                        6.44.6955.0    | O |
    |   |  8   ~~~~~~~~~~~~~~             /\    6.42.1136.1    |   |
    | O |    /\__                        /  \  __      /\      | O |
    |...|\/\/    \/\/\  /\/\  /\    /\/\/    \/  \  /\/  \/\/\_|...|
                      \/    \/  \  /              \/
                                 \/  FalconPy SDK

This sample discusses threaded interactions with the QueryDevicesByFilterScroll
and GetDeviceDetails (PostDeviceDetailsV2) operations.

Creation date: 10.28.22 - jshcodes@CrowdStrike

REQUIRES
    crowdstrike-falconpy v1.2.0+
    tabulate
"""
# pylint: disable=R0913, W0603
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from os import cpu_count
from threading import Lock
from tabulate import tabulate
from falconpy import Hosts, _VERSION as FPVERSION


def parse_command_line() -> Namespace:
    """Parse command-line arguments and return them back as a Namespace."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    table_formats = [
        "plain", "simple", "github", "grid", "simple_grid", "rounded_grid", "heavy_grid",
        "fancy_grid", "fancy_outline", "pipe", "orgtbl", "asciidoc", "jira", "presto", "pretty",
        "psql", "rst", "mediawiki", "moinmoin", "youtrack", "html", "unsafehtml", "latex",
        "latex_raw", "latex_booktabs", "latex_longtable", "textile"
        ]
    requir = parser.add_argument_group("required arguments")
    requir.add_argument('-k', '--client_id',
                        help='CrowdStrike Falcon API key ID',
                        required=True
                        )
    requir.add_argument('-s', '--client_secret',
                        help='CrowdStrike Falcon API key secret',
                        required=True
                        )
    parser.add_argument('-m', '--mssp',
                        help='Child CID to access (MSSP only)',
                        required=False,
                        default=None
                        )
    parser.add_argument('-b', '--base_url',
                        help='CrowdStrike API region (us1, us2, eu1, usgov1).'
                        ' NOT required unless you are using `usgov1`.',
                        required=False,
                        default="auto"
                        )
    parser.add_argument('-r', '--reverse',
                        help='Reverse sort (defaults to ASC)',
                        required=False,
                        default=False,
                        action="store_true"
                        )
    parser.add_argument('-t', '-table_format',
                        help='Format of the results table',
                        dest="table_format",
                        required=False,
                        default="simple",
                        choices=table_formats
                        )
    parser.add_argument('-l', '-limit',
                        help='Query batch limit (Max: 5000, Default: 500)',
                        dest="limit",
                        required=False,
                        default=500,
                        type=int
                        )
    parser.add_argument('-x', '-ludicrous_speed',
                        help='Ludicrous speed, go!',
                        dest="ludicrous_speed",
                        action='store_true',
                        required=False,
                        default=False
                        )
    parser.add_argument('-z', '-max_threads',
                        help='Maximum number of threads to use for detail lookups',
                        default=min(32, (cpu_count() or 1) * 4),
                        required=False,
                        type=int,
                        dest="max_threads"
                        )

    return parser.parse_args()


def make_api_request(method, lock: Lock = None, **kwargs):
    """Increment our API request tracker then perform the request to the API."""
    global API_REQUESTS
    if lock:
        # If there is a thread lock present
        with lock:
            # Use it to safely increment our request counter  # pylint: disable=E0602
            API_REQUESTS += 1
    else:
        # This isn't a threaded call, so we can just increment it
        API_REQUESTS += 1

    return method(**kwargs)


def device_list(off: int, limit: int, sort: str, sdk: Hosts):
    """Return a list of all devices for the CID, paginating when necessary."""
    # Send our API request thru the make_api_request method so we can track our counts
    result = make_api_request(
        sdk.query_devices_by_filter_scroll, limit=limit, offset=off, sort=sort
        )
    new_offset = None           # Offset
    total = 0                   # Total
    returned_device_list = []   # Device ID list
    if result["status_code"] == 200:
        # Grab our new offset
        new_offset = result["body"]["meta"]["pagination"]["offset"]
        # Get the total count available
        total = result["body"]["meta"]["pagination"]["total"]
        # Retrieve our list of devices
        returned_device_list = result["body"]["resources"]

    return new_offset, total, returned_device_list


def device_detail(aids: list, sdk: Hosts, t_lock: Lock = None):
    """Return the device_id and agent_version for a list of AIDs provided."""
    # Pass the method, our thread lock and AID list to the api request method.
    result = make_api_request(sdk.get_device_details, t_lock, ids=aids)
    device_details = []  # This examples assumes you can connect to the API
    if result["status_code"] == 200:
        # return just the aid and agent version
        device_details = [
            {"hostname": device.get("hostname", device["device_id"]),
             "agent_version": device.get("agent_version", None)
             }
            for device in result["body"]["resources"]
            ]

    return device_details


def threaded_details(batch_to_process: list, hosts_api: Hosts, locking: Lock):
    """Perform a threaded device detail lookup.

    This is the method used by ludicrous threads.

    Um... Someone should probably trademark that.
    """
    # Pass this batch and the hosts SDK to the device detail method for our list
    devs = device_detail(batch_to_process, hosts_api, locking)
    # Quickly build our device map based off of our results
    device_map = [
        {"hostname": dev["hostname"], "agent_version": dev["agent_version"]} for dev in devs
        ]

    return device_map


# pylint: disable=R0914
def ludicrous_example(total: int,
                      offset: str,
                      limit: int,
                      sort: str,
                      api: Hosts,
                      rev: bool,
                      threads: int
                      ):
    r"""Execute the ludicrous example.

    This example demonstrates how to thread the lookup of device details after
    the retrieval of the AIDs has been completed. Depending on the number of
    records in question, this can result in an impressive performance increase.
         _________
      ,''         ``.
     /               \
    |   ,---------.   |
    |  /--.\ | /,--\  |   Ludicrous speed, go!
    | /`-._\\|//_,-'\ | /
    |/._ _ _____ _ _.\|
    /   \ |=/#\=| /   \
    (_`-._\|=\#/=|/_,-'_)
    /  ._'-.___,-'_,  \
   / /   `-.\_/.-'   \ \
    """
    all_devices = []        # All devices retrieved (list of dictionaries)
    device_maps = []        # List of devices we return (list)
    offset_pos = 0          # Running count of retrieved records
    thread_lock = Lock()    # We need this to stay thread safe when updating API_REQUESTS
    while offset_pos < total:
        # Retrieve a batch of device IDs sized by the value of our limit
        offset, total, devices = device_list(offset, limit, sort, api)
        offset_pos += len(devices)   # Update our position with the total number returned
        print(f"  📥 Retrieved {offset_pos:,} device IDs.    ", end="\r", flush=True)
        all_devices.append(devices)  # Append these results to our list
    # Now that we have a list of all of our IDs we need to cut them into individual
    # batches that can be fed to the GetDeviceDetails operation for extended detail.
    # Starting in FalconPy v1.2.0+ you can submit up to 5000 IDs to this operation.
    # Developers using a version lower than 1.2.0 would be limited to 500 IDs.
    batches = [all_devices[i:i+5000] for i in range(0, len(all_devices), 5000)][0]
    # Quick and easy method for sending these enrichment lookups to individual threads.
    # You can control the number of threads used by adjusting the max_threads argument.
    with ThreadPoolExecutor(max_workers=threads, thread_name_prefix="thread") as executor:
        futures = {
            executor.submit(threaded_details, batch, api, thread_lock) for batch in batches
        }
        for fut in futures:
            # Loop thru each threads return and add it's results to our device map
            device_maps.extend(fut.result())

    # Re-sort since our dictionaries come back in an unordered list
    device_maps.sort(key=lambda item: item["hostname"], reverse=rev)

    return device_maps


def standard_example(total: int, offset: str, limit: int, sort: str, api: Hosts, rev: bool):
    """Execute the standard example.

    Leverages a while loop to populate a list dynamically as it receives new records
    from the API. Device detail lookups are performed at the time the list is updated.
    """
    offset_pos = 0      # Running count of retrieved records
    details = []        # List of devices we return
    while offset_pos < total:
        # Retrieve a batch of device IDs sized by the value of our limit
        offset, total, devices = device_list(offset, limit, sort, api)
        offset_pos += len(devices)   # Update our position with the total number returned
        print(f"  📥 Retrieved {offset_pos:,} device IDs.    ", end="\r", flush=True)
        # Enrich and append these results to our list, since we're using FalconPy v1.2+
        # we can pass our list directly from the QueryDevicesByFilterScroll operation
        # to the GetDeviceDetails operation as they both have the same ID maximums.
        details.extend(device_detail(devices, api))

    # Re-sort since our dictionaries come back in an unordered list
    details.sort(key=lambda item: item["hostname"], reverse=rev)

    return details


def check_version():
    """Confirm the running version of FalconPy supports the new GetDeviceDetails operation."""
    vers = FPVERSION.split(".")  # major.minor.patch
    if float(f"{vers[0]}.{vers[1]}") < 1.2:
        raise SystemExit("  ⛔ This sample requires FalconPy v1.2 or greater.\n"
                         "  🔗 https://github.com/CrowdStrike/falconpy/releases/tag/v1.2.0")


if __name__ == "__main__":
    # Make sure our environment is sane
    check_version()
    # Get our start time timestamp
    startup_time = datetime.now().timestamp()
    # Retrieve any provided command line arguments
    args = parse_command_line()
    # Connect to the CrowdStrike API
    falcon = Hosts(client_id=args.client_id,
                   client_secret=args.client_secret,
                   base_url=args.base_url,
                   member_cid=args.mssp
                   )
    # Set constants
    SORT = "hostname.asc"       # Default to ascending
    if args.reverse:            # Calculate our sort method
        SORT = "hostname.desc"  # Reverse means descending
    LIMIT = args.limit          # Limit provided from the command line
    OFFSET = None               # First time the token is null
    TOTAL = 1                   # Assume there is at least one
    API_REQUESTS = 0            # Track how many API calls we make
    results = []                # List to hold our results
    # Headers for our tabular display
    HEADERS = {"hostname": "Hostname", "agent_version": "Agent Version"}
    if args.ludicrous_speed:
        # Run the ludicrous example and demonstrate this process asynchronously.
        results = ludicrous_example(
            TOTAL, OFFSET, LIMIT, SORT, falcon, args.reverse, args.max_threads
            )
    else:
        # Run the standard example and *yawn* demonstrate this process synchronously.
        results = standard_example(TOTAL, OFFSET, LIMIT, SORT, falcon, args.reverse)

    if results:
        # Print our results to a table. You could also loop thru the list or output to CSV here.
        print(tabulate(results,
                       headers=HEADERS,
                       tablefmt=args.table_format,
                       showindex=[f"{x:,}" for x in range(1, len(results)+1)]
                       ))
        print(f"\n  👨‍💻  {len(results):,} total endpoints returned")
    else:
        #       i\
        #   /[  ;>`;
        #  ij Y" "<        ,_________
        #   >  (dd)- ;   /"          ".
        #   j  . (   )i  |  RUT ROW!  |
        #   |  `. "-i f  `._  _______.'
        #   ] . [._.;-      |/
        #   |.`.`._|`;   ---'
        #    j  \  -'i
        #     \  `--'\
        #     |"-.___t'\
        #     ;;-.____./
        print(f"{' ' * 30}\n  🤷🏽  No results returned. Check your credentials.")

    print(f"  ⏱️   {datetime.now().timestamp() - startup_time:.2f} seconds total execution time\n"
          f"  📈  {API_REQUESTS:,} total API requests\n"
          )
