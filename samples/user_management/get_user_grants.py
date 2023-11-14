r"""Threaded user grant lookup sample.

 ______                         __ _______ __         __ __
|      |.----.-----.--.--.--.--|  |     __|  |_.----.|__|  |--.-----.
|   ---||   _|  _  |  |  |  |  _  |__     |   _|   _||  |    <|  -__|
|______||__| |_____|________|_____|_______|____|__|  |__|__|__|_____|
      ___ ___                   ___ ___                                                    __
     |   Y   .-----.-----.----.|   Y   .---.-.-----.---.-.-----.-----.--------.-----.-----|  |_
     |.  |   |__ --|  -__|   _||.      |  _  |     |  _  |  _  |  -__|        |  -__|     |   _|
     |.  |   |_____|_____|__|  |. \_/  |___._|__|__|___._|___  |_____|__|__|__|_____|__|__|____|
     |:  1   |                 |:  |   |                 |_____|
     |::.. . |                 |::.|:. |                               with Flight Control!
     `-------'                 `--- ---'                                (FalconPy v1.3.0+)

Asynchronously retrieve all user grants for every user defined within the tenant and output
the results to a comma-delimited text file. When not specified, this file is named user_grants.csv.

Creation date: 11.13.2023 - jshcodes@CrowdStrike
"""
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from concurrent.futures import ThreadPoolExecutor
from csv import writer
from datetime import datetime
from logging import basicConfig, DEBUG
from os import getenv, path, mkdir
from typing import Tuple, List, Dict
try:
    from falconpy import APIError, FlightControl, UserManagement, version
except ImportError as no_falconpy:
    raise ImportError("In order to use this sample application, the CrowdStrike FalconPy "
                      "library (version 1.3.0 or greater) must be installed."
                      ) from no_falconpy


def consume_arguments() -> Tuple[Namespace, ArgumentParser]:
    """Retrieve any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug", help="Enable debug.", default=False, action="store_true")
    parser.add_argument("-o", "--output", help="CSV output filename.", default="user_grants.csv")
    auth = parser.add_argument_group("authentication arguments "
                                     "(not required if using environment authentication)")
    auth.add_argument("-k", "--client_id",
                      help="Falcon API client ID",
                      default=getenv("FALCON_CLIENT_ID")
                      )
    auth.add_argument("-s", "--client_secret",
                      help="Falcon API client secret",
                      default=getenv("FALCON_CLIENT_SECRET")
                      )

    return parser.parse_args(), parser


def get_grants(interface: UserManagement, uuid: str) -> List[Dict[str, str]]:
    """Retrieve all grants for the user UUID in question."""
    print(f"  Retrieving grant detail for {uuid}{' ' * 30}", end="\r")
    grant_detail = interface.get_user_grants(uuid).data

    return grant_detail


def get_grant_data(sdk: UserManagement) -> Tuple[List[str], List[Dict[str, str]]]:
    """Retrieve all user UUIDs within the tenant and then retrieve the grants for each."""
    running = True
    user_ids = []     # List of User IDs identified
    user_grants = []  # List of grants retrieved
    offset = None
    # Query users endpoint has a limit of 500 results, so we will paginate through all
    # results returned and append each iteration's results to our user_grants list
    while running:
        user_lookup = sdk.query_users(limit=500, offset=offset)
        user_ids.extend(user_lookup.data)
        total = user_lookup.total
        offset = len(user_ids)
        with ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(get_grants, sdk, user_id) for user_id in user_lookup.data
            }
            for fut in futures:
                user_grants.extend(fut.result())
        if len(user_ids) >= total:
            running = False

    return user_ids, user_grants


def get_extended_user_data(sdk: UserManagement,
                           user_uuids: list,
                           grants: list
                           ) -> List[Dict[str, str]]:
    """Retrieve extended user information and merge the results with the existing grants data."""
    user_info = {}  # Temporary dictionary to populate with user information detail
    # Retrieve users endpoint can only handle 500 IDs at a time, request results in batches
    batches = [user_uuids[i:i+500] for i in range(0, len(user_uuids), 500)]
    for batch in batches:
        lookup_result = sdk.retrieve_users(batch)
        for detail in lookup_result.data:
            # Create a "clean" dictionary that leverages UUID as the key,
            # we can use this to lookup the details when we merge dictioaries
            cleaned = {
                detail["uuid"]: {
                    "uid": detail["uid"],
                    "first_name": detail["first_name"],
                    "last_name": detail["last_name"],
                    "user_created_at": detail["created_at"]
                }
            }
            # Add our cleaned dictionary to our master user information dictionary
            user_info.update(cleaned)
    # Loop through each grant and add in our extended user detail
    for grant in grants:
        grant["uid"] = user_info[grant["uuid"]]["uid"]
        grant["first_name"] = user_info[grant["uuid"]]["first_name"]
        grant["last_name"] = user_info[grant["uuid"]]["last_name"]
        grant["user_created_at"] = user_info[grant["uuid"]]["user_created_at"]

    return grants


def write_grant_results(user_grants: list, output_file: str):
    """Write grant details to the specified CSV file."""
    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = writer(csv_file)
        if user_grants:
            csv_writer.writerow(user_grants[0].keys())  # Header row
            for grants in user_grants:
                csv_writer.writerow(grants.values())  # Data rows


def process_tenant(cmdline: Namespace, child: str = None):
    """Process the users identified within the current tenant."""
    # Create an instance of the UserManagement Service Class
    # and authenticate to the child tenant if necessary.
    users = UserManagement(client_id=cmdline.client_id,
                           client_secret=cmdline.client_secret,
                           member_cid=child,
                           debug=cmdline.debug,
                           pythonic=True
                           )
    # Retrieve a list of user UUIDs and grants
    id_list, grant_list = get_grant_data(users)
    # Enrich the grant list with extended user detail
    grant_list = get_extended_user_data(users, id_list, grant_list)
    print(" " * 80)  # Clear the last status update line
    # Calculate our destination CSV file name
    write_to = cmdline.output
    dir_name = path.dirname(cmdline.output)
    if child:
        print(f"Child tenant: {child}")
        write_to = path.join(dir_name, f"{child}.csv")
    # Create our destination path if it is missing
    if dir_name and not path.exists(dir_name):
        mkdir(dir_name)
    # They only provided us an output directory
    if path.isdir(write_to):
        write_to = path.join(write_to, "user_grants.csv")
    # Write the results to our output CSV file
    write_grant_results(grant_list, f"{write_to}")
    # Inform the user of the overall execution results
    print(f"{len(id_list):,} total users identified.")
    print(f"{len(grant_list):,} total grants retrieved.")
    print(f"Results saved to: {write_to}")


# _  _ ____ _ _  _    ____ ____ _  _ ___ _ _  _ ____
# |\/| |__| | |\ |    |__/ |  | |  |  |  | |\ | |___
# |  | |  | | | \|    |  \ |__| |__|  |  | | \| |___
if __name__ == "__main__":
    # Start the timer
    begin = datetime.now().timestamp()
    # Retrieve command line arguments and the argument parser
    parsed, handler = consume_arguments()
    # There are no credentials in the environment or command line, show help and quit
    if not parsed.client_id or not parsed.client_secret:
        handler.print_help()
        raise SystemExit(
                "\nYou must provide API credentials via the environment variables\n"
                "FALCON_CLIENT_ID and FALCON_CLIENT_SECRET or you must provide\n"
                "these values using the '-k' and '-s' command line arguments."
                )
    # Credentials are present, inform the user we are starting
    print(f"Process start ({datetime.utcfromtimestamp(begin)}, "
          f"FalconPy v{version(agent_string=False)})"
          )
    # Enable debug logging to the console if requested
    if parsed.debug:
        basicConfig(level=DEBUG)
    # Construct an instance of the FlightControl Service Class
    mssp = FlightControl(client_id=parsed.client_id,
                         client_secret=parsed.client_secret,
                         debug=parsed.debug,
                         pythonic=True
                         )
    try:
        # Attempt to query for any available children
        children = mssp.query_children().data
    except APIError:
        # No Flight Control scope
        children = []
    # Process the current tenant
    process_tenant(parsed)
    # For each child identified
    for child in children:
        # Process the child tenant
        process_tenant(parsed, child)
    # This party is over folks
    print(f"\nTotal processing time: {datetime.now().timestamp() - begin:.2f} seconds.")
