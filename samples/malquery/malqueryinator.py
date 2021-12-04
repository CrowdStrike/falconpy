"""
MalQueryinator - MalQuery sample download utility.

Searches MalQuery (fuzzy) for a particular string,
downloading a specified number of examples if found.

09.02.21 - jlangdev@CrowdStrike, jshcodes@CrowdStrike
"""
#  ___ ___       __ _______
# |   Y   .---.-|  |   _   .--.--.-----.----.--.--.
# |.      |  _  |  |.  |   |  |  |  -__|   _|  |  |
# |. \_/  |___._|__|.  |   |_____|_____|__| |___  |
# |:  |   |        |:  1   |                |_____|
# |::.|:. |        |::..   |
# `--- ---'        `----|:.|    FalconPy v0.7.0+
#                       `--'

import argparse
try:
    from falconpy import APIHarness
except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy


def malware_search(type_, value, limit):
    """
    Performs a fuzzy MalQuery search based
    upon the type and value provided.
    """
    stub = ""
    if int(limit) > 1:
        stub = "s"
    print(f"Searching for {limit} example{stub} of {type_}: {value}")
    malware = falcon.command(
        "PostMalQueryFuzzySearchV1",
        body={
            "options": {
                "limit": int(limit)
            },
            "patterns": [{
                "type": type_,                              # Ascii, Hex or Wide
                "value": value                              # Value to find
                }]
        }
    )["body"]["resources"]

    return malware


def id_search(malware):
    """
    Requests the download for the ID returned from
    the fuzzy malware_search. Displays the details
    for the malware sample that is to be retrieved.
    """
    id_to_retrieve = []
    for found in malware:
        print(
            f"Requesting download for {found['sha256']}\n"
            f"File size: {found.get('filesize', 'Unknown')} bytes\n"
            f"Family: {found.get('family', 'Unknown')} malware\n"
            f"First seen: {found.get('first_seen', 'Unknown')}\n"
            f"File type: {found.get('filetype', 'Unknown')}"
            )

        id_to_retrieve.append(found["sha256"])
    search_request_id = falcon.command(                     # Request the download
        "PostMalQueryEntitiesSamplesMultidownloadV1",
        body={
            "samples": id_to_retrieve
        }
    )["body"]["meta"]["reqid"]
    return search_request_id


def get_malquery_request(search_request_id):
    """
    Checks the status of our download request,
    waiting until the status is set to "done".
    """
    print("Getting malquery request")
    running = True
    while running:
        search_result = falcon.command(
            "GetMalQueryRequestV1",
            ids=search_request_id
        )
        status = search_result["body"]["meta"]["status"]    # Grab our status result
        if status == "done":                                # When it's done, continue
            running = False


def get_sample(search_request_id: str, save_file: str):
    """
    Retrieves the sample from MalQuery,
    downloading to the file specified.
    """
    print(
        f"Downloading samples {search_request_id} to ./{save_file}"
        )
    archive_result = falcon.command(                        # Request the download
        "GetMalQueryEntitiesSamplesFetchV1",
        ids=search_request_id
    )
    if isinstance(archive_result, dict):                    # Is it a dictionary?
        print(                                              # This probably means there was an error
            archive_result["body"]["errors"][0]["message"]  # Show the error message we got back
            )
    else:                                                   # No, it's a file
        with open(save_file, 'wb') as saving:
            saving.write(archive_result)


def connect_api(key: str, secret: str):
    """
    Connects and returns an instance of the Uber class.
    """
    return APIHarness(client_id=key, client_secret=secret)


def parse_command_line():
    """
    Parses the passed command line and
    returns the created args object.
    """
    parser = argparse.ArgumentParser(
        description="Malquerinator"
    )
    # Type defaults to "ascii" when not provided
    parser.add_argument(
        '-t', '--type',
        help="Type of pattern for the malware query: ascii, hex, or wide",
        required=False
    )

    parser.add_argument(
        '-v', '--value',
        help="Value for malware query of type determined by --t/--type arg",
        required=True
    )

    parser.add_argument(
        '-f', '--file',
        help="Name of file to write to",
        required=True
    )

    parser.add_argument(
        '-e', '--examples',
        help="Number of examples to download",
        required=False
    )

    parser.add_argument(
        '-k', '--key',
        help='Falcon API Client ID',
        required=True
    )
    parser.add_argument(
        '-s', '--secret',
        help='Falcon API Client secret',
        required=True
    )

    return parser.parse_args()


def main():
    """
    Main routine
    """
    malware = malware_search(QUERY_TYPE, query_value, EXAMPLES)
    search_request_id = id_search(malware)
    get_malquery_request(search_request_id)
    get_sample(search_request_id, file)
    print("Done")


# Retrieve our provided command line arguments
args = parse_command_line()
if not args.type:
    QUERY_TYPE = "ascii"
else:
    if args.type.lower() not in ["ascii", "hex", "wide"]:
        QUERY_TYPE = "ascii"
    else:
        QUERY_TYPE = args.type.lower()
if not args.examples:
    EXAMPLES = 1
else:
    EXAMPLES = args.examples

query_value = args.value
file = args.file
falcon = connect_api(key=args.key, secret=args.secret)

if __name__ == "__main__":
    main()


#
#                                   WNNW
#                                 WKdcclx0XN
#                                  N0xl,',;cxX
#                                     W0l,..'cON
#                               WWW     Nx:,..,dX
#                         NKOxdolllodk0NWNXd,..,xW
#                      NOoc;''.......',:lxkd;..'lX
#                     WOc:;;;;;;,,''......'''...:kOkkkkk0N
#                      WNNNXXKOxoc;'............'''',:okKW
#                          NOl;,'..................',:clo0W
#                         Xo,',;:lodddollllc;'....'''...'dW
#                        W0dxOKXNWWWNK000000d,....'cdl,.,xW
#                         WW      WX0OkdodkOkc'....,xXOc;k
#                     W0xd0N    WN00Oo:,...,do'.....:KWX0X
#                    WOlcclkN  WK0000OOOkoc,;ol;;;;,;OW
#                    WNNNNXXNWX000000O00000Odk0O0XXKKN
#                   WNKkOXNXXKOxddOKXKK0O0000000X              This Inator has been Doof-approved!
#                  W0c:lkNWWWXd'';dXWNWNXOkO000KN
#                  N0xxOXWWWNKkl:oKNWWWWWX0OO00XW               /
#                  WXXWWWWWWNKKNNNWWWWWWWNX0O00N
#                   WNNNWWWNXOOXWWWWWWWWWKOO00KN
#                    WXOkkkOOOO0XNWWWWNX0kkO00KWWNNXXXNW
#           WWNNNNNXXXKkxxkO000OOOOOOOxxxO000O0K00O0000X
#       WNXKK00000000000000000000OkxxxkO00000OO00OO0000X
#    WNKK000000000000000000000000000000000000000OOO000XW
#  WXK000000000KKKK0OO000000000000000000000000KKKKXXNW
# NKO000KKXXXNWWWWK00000000000000000000000000KW
# WXXNNWW     WWNKO00000000000000000000000000N
#            NK00OOOOOOOOOOOOOOOOO0000000000KN
#            WK00000000000OO0000000000000000KN
#            NK000000000000000000000000000000XW
#           NK00000000000000000000000000000000XNW WXKNW
#          NK00000000000000000000000000000000000KKx;.'dXNWW
#         WK00000000000000000000000000000000000000k:  ,0WNNNW
#         X000000000000000000000000000000000000000Oc  .lXWWNXNWW
#        WX000000000000000KKKKXXNNNNNNNNNNNNNXX0d:,.   .lX WWNXNNW
#         NK0000000KKXXNNWWW                  WXl.      .xW WWWNNNNW
#          WNXXXNNWW                          NNKc       ;KWW  WNNNNWW
#                                            WNNWx.      .oN W WWNNNWWW
#                                            NNW 0'       'OW  W WNNWWWNW
#                                           WNN  X:        cXW WWNNWW WWNW
#                                           WNW  No        .OWNNNWWWW  WWNNW
#                                           WXNNWWk.       .oXXNWWWW WWW WNNW
#                                            NXXNW0,        :KWNNNNNW WWWWWNNW
#                                           WXXNW X:        ,0  WWWNNWW  W WNN
