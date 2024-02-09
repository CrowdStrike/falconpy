"""MalQueryinator - MalQuery sample download utility.

 ___ ___       __ _______
|   Y   .---.-|  |   _   .--.--.-----.----.--.--.
|.      |  _  |  |.  |   |  |  |  -__|   _|  |  |
|. \_/  |___._|__|.  |   |_____|_____|__| |___  |
|:  |   |        |:  1   |                |_____|
|::.|:. |        |::..   |
`--- ---'        `----|:.|    FalconPy v1.3.0+
                      `--'

Searches MalQuery (fuzzy) for a particular string,
downloading a specified number of examples if found.

09.02.21 - jlangdev@CrowdStrike, jshcodes@CrowdStrike
02.09.23 - jshcodes@Crowdstrike
"""
import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
try:
    from falconpy import APIHarnessV2, version
except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy 1.3 or greater must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy


def malware_search(type_, value, limit):
    """Perform a fuzzy MalQuery search based upon the type and value provided."""
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
    """Request the download for the ID returned from the fuzzy malware_search.
    
    Displays the details for the malware sample that is to be retrieved.
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
    """Check the status of our download request, waiting until the status is set to "done"."""
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
    """Retrieve the sample from MalQuery, downloading to the file specified."""
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


def connect_api(key: str, secret: str, debug: bool):
    """Connects and returns an instance of the Uber class."""
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    return APIHarnessV2(client_id=key, client_secret=secret, debug=debug)


def parse_command_line():
    """Parses the passed command line and returns the created args object."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    # Type defaults to "ascii" when not provided
    parser.add_argument("-t", "--type",
                        help="Type of pattern for the malware query: ascii, hex, or wide"
                        )
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-v", "--value",
                        help="Value for malware query of type determined by --t/--type arg",
                        required=True
                        )
    parser.add_argument("-f", "--file", help="Name of file to write to", required=True)
    parser.add_argument("-e", "--examples", help="Number of examples to download")

    parser.add_argument("-k", "--key",
                        help="Falcon API Client ID",
                        default=os.getenv("FALCON_CLIENT_ID")
                        )
    parser.add_argument("-s", "--secret",
                        help="Falcon API Client secret",
                        default=os.getenv("FALCON_CLIENT_SECRET")
                        )

    parsed = parser.parse_args()
    if not parsed.key or not parsed.secret:
        parser.error(
            "You must provide valid API credentials ('-k' and '-s') in order to use this program."
            )

    return parsed


def main():
    """Execute main routine."""
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
falcon = connect_api(key=args.key, secret=args.secret, debug=args.debug)

if __name__ == "__main__":
    main()
