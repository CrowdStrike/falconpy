# noqa: D209
r"""Identify usernames for specific hosts.

                                                                  88                                  88  88
                                                                  88               ,d                 ""  88
                                                                  88               88                     88
 ,adPPYba,  8b,dPPYba,   ,adPPYba,   8b      db      d8   ,adPPYb,88  ,adPPYba,  MM88MMM  8b,dPPYba,  88  88   ,d8   ,adPPYba,
a8"     ""  88P'   "Y8  a8"     "8a  `8b    d88b    d8'  a8"    `Y88  I8[    ""    88     88P'   "Y8  88  88 ,a8"   a8P_____88
8b          88          8b       d8   `8b  d8'`8b  d8'   8b       88   `"Y8ba,     88     88          88  8888[     8PP"""""""
"8a,   ,aa  88          "8a,   ,a8"    `8bd8'  `8bd8'    "8a,   ,d88  aa    ]8I    88,    88          88  88`"Yba,  "8b,   ,aa
 `"Ybbd8"'  88           `"YbbdP"'       YP      YP       `"8bbdP"Y8  `"YbbdP"'    "Y888  88          88  88   `Y8a  `"Ybbd8"'


Created: 05/08/2022, micgoetz@CrowdStrike
Updated: 05/24/2022, micgoetz@CrowdStrike

This script will grab ALL (max 5000) of your CrowdStrike-installed devices and auto-tag each one based upon the most common
username seen. Or, provide a csv file with hosts and usernames you want to tag each with.

Most common username is determined by looking at the last 10 logins.

Requires: crowdstrike-falconpy
    python3 -m pip install crowdstrike-falconpy

This program requires your:
    - API Client ID
    - API Secret ID

With permissions:
    Hosts: Read + Write
"""
import argparse
import csv
import getpass
try:
    from falconpy import Hosts
except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy


# parsing the args
def parse_command_line() -> object:
    """Consume command-line arguments. ClientID & SecretID are required."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "-c",
        "--client_id",
        help="CrowdStrike Falcon API key ID",
        required=True
    )
    parser.add_argument(
        "-s",
        "--client_secret",
        help="CrowdStrike Falcon API key secret",
        required=False
    )
    parser.add_argument(
        "-b",
        "--base_url",
        help="CrowdStrike API region (us1, us2, eu1, usgov1). "
        "NOT required unless you are using `usgov1`.",
        required=False
    )
    parser.add_argument(
        "-m",
        "--mssp",
        help="Child CID to access (MSSP only)",
        required=False
    )
    parser.add_argument(
        "-i",
        "--input_file",
        help="The path to a csv with only hostnames & usernames. "
        "Expected format: 'hostname, username'",
        required=False,
        type=argparse.FileType("r")
    )
    parser.add_argument(
        "-t",
        "--test",
        help="run the program and output the results that would take place but take no action",
        required=False,
        action='store_true'  # per argparse, this means default=False
    )
    parser.add_argument(
        "-r",
        "--remove",
        help="remove falcon grouping tags, undoing whatever was originally done by this script",
        required=False,
        action='store_true'  # per argparse, this means default=False
    )
    return parser.parse_args()


def device_list():
    """Grab all available AIDs."""
    result = falcon.query_devices_by_filter(limit=5000, offset=0, sort="hostname.asc")
    returned_device_list = result["body"]["resources"]
    # returns list of device IDs:  ['aid1', 'aid2', 'aid3', ...]
    return returned_device_list


def most_common_name(list_of_names):
    """Grab the most common name in a list."""
    return max(set(list_of_names), key=list_of_names.count)


def parse_csv(file_contents: object):
    """Use the csv file to grab appropriate hosts & device IDs.

    Sends the information to upload_csv.
    """
    # need to grab the AIDs first as a list
    devices = device_list()

    # Retrieves a list containing device infomration based upon the ID list provided.
    device_details = falcon.get_device_details(ids=devices)["body"]["resources"]

    # grabbing the hostnames retrieved from the above query
    # and putting them in a list for future reference
    device_hostnames = []
    for i in device_details:
        device_hostnames.append(i["hostname"])

    # we can take this list of hostnames & AIDs and combine them into a tuple,
    # and have a bunch of tuples in a list for easier comparison against the CSV
    # [(aid1, hostname1),(aid2, hostname2), (aid3,)]
    host_list = list(zip(devices, device_hostnames))

    # use the hostnames that we grabbed from the cloud (above),
    # match against those used in the CSV,
    # and upload usernames as Falcon Grouping Tags
    upload_csv(file_contents, host_list)


def upload_csv(file_contents: object, host_list: list):
    """Read the CSV and generating a list of hostnames & usernames.

    For every hostname that we can match with an AID, just grab that corresponding username.
    """
    reader = csv.reader(file_contents)
    print("...reading file...")

    for row in reader:  # pylint: disable=R1702
        # check that there's only two columns in each row. It's about data quality, people!
        if len(row) == 2:

            # in each row, find matching hostname entries in the host list
            for device in host_list:
                # matches! this will send up the same tag for
                # multiple devices with the same hostname.
                if row[0] in device:

                    if len(row[1]) <= 237:

                        # the API & csv files with whitespace do not mix.
                        # jumping the gun and replacing usernames with whitespace characters
                        # with underscore characters
                        uname = row[1].replace(" ", "_")

                        if args.test is True:
                            print("Hostname: " + row[0])
                            print("   AID: " + device[0])
                            print("   Username: " + uname)

                        elif args.remove is True:
                            response = falcon.update_device_tags(action_name="remove",
                                                                 ids=device[0], tags=uname)
                            if response["body"]["errors"]:
                                print("Something went wrong. Error:")
                                print(str(response["body"]["errors"]))
                        else:
                            response = falcon.update_device_tags(action_name="add",
                                                                 ids=device[0], tags=uname)
                            if response["body"]["errors"]:
                                print("Something went wrong. Error:")
                                print(str(response["body"]["errors"]))
                    # username is too long, must be less than or equal to 237 characters
                    else:
                        print("username found longer than 237 characters, this will be ignored...")

        # more than 2 columns in the csv
        else:
            print("There's more than 2 columns! Expected format for csv: hostname, username")
            raise SystemExit


# grabbing the most common username from each host
def upload_device_logins(aids: list):
    """Process device logins.
    
    - Grab the most common username from each host
    - Match against 'bad' usernames
    - Upload them as grouping tags
    """
    # Chunk the incoming list of AIDS to our 500 id maximum
    aid_list = [aids[i:i + 500] for i in range(0, len(aids), 500)]
    for aid_batch in aid_list:  # pylint: disable=R1702
        result = falcon.query_device_login_history(ids=aid_batch)
        total_logins = result["body"]["resources"]
        for i in total_logins:
            recent_logins = (i["recent_logins"])
            devices_to_be_updated = []
            # do we have device logins? if yes keep going
            if bool(recent_logins):
                # get rid of any logins that match the list of "bad names"
                # and generate a list of possible names to find the most common from
                list_of_possible_names = []
                user_name_to_be_updated = []
                for item in range(len(recent_logins)):  # pylint: disable=C0200
                    if "user_name" in recent_logins[item]:
                        if not any(bad_word in recent_logins[item]["user_name"]
                                   for bad_word in bad_user_names):
                            # we can find valid user login names!!
                            # print(recent_logins[item]["user_name"])
                            list_of_possible_names.append(
                                recent_logins[item]["user_name"].split("@", 1)[0]
                                )

                # is the list of not-bad usernames empty?
                # get rid of it, we only want lists with values
                if list_of_possible_names:
                    devices_to_be_updated.append(i["device_id"])

                    # grab the most common username from the list of eligible logins
                    common_name = most_common_name(list_of_possible_names)
                    user_name_to_be_updated.append(common_name)

                    if args.test is True:
                        # query_device_login_history doesn't give hostname
                        # or the structure varies per OS platform), so have to pair hostnames
                        # Retrieves a list containing device infomration
                        # based upon the ID list provided.
                        device_details = falcon.get_device_details(
                                                    ids=i["device_id"])["body"]["resources"]

                        # grabbing the hostnames retrieved from the above query
                        # and putting them in a list for future reference
                        print("Hostname: " + str(device_details[0]["hostname"]))
                        print("   AID: " + i["device_id"])
                        print("   Username: " + str(common_name))

                    elif args.remove is True:
                        response = falcon.update_device_tags(action_name="remove",
                                                             ids=devices_to_be_updated,
                                                             tags=user_name_to_be_updated
                                                             )
                        if response["body"]["errors"]:
                            print("Something went wrong. Error:")
                            print(str(response["body"]["errors"]))
                    else:
                        # JUST GONNA SEND IT
                        response = falcon.update_device_tags(action_name="add",
                                                             ids=devices_to_be_updated,
                                                             tags=user_name_to_be_updated
                                                             )
                        if response["body"]["errors"]:
                            print("Something went wrong. Error:")
                            print(str(response["body"]["errors"]))


# #########################
# ######## MAIN ###########
# #########################
if __name__ == "__main__":

    # A list of words we want to exclude from the user_name list we retrieve.
    # If a user_name includes one of these names, it will not be tagged
    # Used only when a CSV file is not supplied
    bad_user_names = [
        'Font Driver Host', '\\demo', 'Window Manager\\', 'WORKGROUP\\',
        'NT AUTHORITY\\', '_spotlight@', 'root'
        ]

    args = parse_command_line()

    if args.client_secret is None:
        args.client_secret = getpass.getpass("ClientSecret: ") 

    BASE = "auto"
    if args.base_url:
        BASE = args.base_url

    CHILD = None
    if args.mssp:
        CHILD = args.mssp

    falcon = Hosts(client_id=args.client_id,
                   client_secret=args.client_secret,
                   base_url=BASE,
                   member_cid=CHILD
                   )
    # csv_upload
    if args.input_file:
        # import the csv & upload the usernames
        parse_csv(args.input_file)
    else:
        print("No csv found - using most common username from last 10 recorded logins...")
        my_device_list = device_list()
        upload_device_logins(my_device_list)

    print("\n\nDone!")
