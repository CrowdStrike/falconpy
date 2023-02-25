r"""Retrieve MITRE reports for adversaries.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |       FalconPy v1.2.10
`-------'                         `-------'

 _   _  _  ___  ___ ___      _  ___  ___ _    __  _  _
| \_/ || ||_ _|| o \ __|    / \|_ _||_ _(o)  / _|| |//
| \_/ || | | | |   / _|    | o || |  | |/oV7( (_ |  (
|_| |_||_| |_| |_|\\___|   |_n_||_|  |_|\_n\ \__||_|\\

____ ____ ___  ____ ____ ___   ___  ____ _ _ _ _  _ _    ____ ____ ___
|__/ |___ |__] |  | |__/  |    |  \ |  | | | | |\ | |    |  | |__| |  \
|  \ |___ |    |__| |  \  |    |__/ |__| |_|_| | \| |___ |__| |  | |__/

Download MITRE ATT&CK reports for specified (or all) adversaries.

This application requires:
    colorama
    crowdstrike-falconpy v1.2.10+

Created: 02.24.23 - jshcodes@CrowdStrike
"""
import os
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from random import randrange  # non-cryptographic usage
try:
    from colorama import Fore, Style
except ImportError as no_colorama:
    raise SystemExit(
        "This application requires the colorama package.\n"
        "Install: python3 -m pip install colorama"
        ) from no_colorama
try:
    from falconpy import Intel, _VERSION
except ImportError as no_falconpy:
    raise SystemExit(
        "This application requires the crowdstrike-falconpy (v1.2.10+) package.\n"
        "Install: python3 -m pip install crowdstrike-falconpy"
        ) from no_falconpy


def shiny(message: str):
    """Output fabulous terminal messages."""
    colors = [
        Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.LIGHTWHITE_EX, Fore.RED,
        Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.GREEN,
        Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.YELLOW
        ]
    fantastic = [f"{colors[randrange(0, len(colors) - 1)]}{c}" for c in message]  # nosec B311
    fantastic.append(Style.RESET_ALL)

    return "".join(fantastic).ljust(120, " ")


def version_check():
    """Confirm the version of FalconPy we're running supports the syntax we're using."""
    valid_version = False
    vers = _VERSION.split(".")
    major_minor = float(f"{vers[0]}.{vers[1]}")
    if major_minor >= 1.2 and int(vers[2]) >= 10:
        valid_version = True

    if not valid_version:
        raise SystemExit("This example requires crowdstrike-falconpy v1.2.10 or greater.")


def download_thread(actor_id: str, sdk: Intel, file_format: str, folder: str):
    """Download a MITRE report for the specified adversary."""
    download_successful = False
    actor_name = f"{actor_id.split('-')[0].title()} {actor_id.split('-')[1].title()}"
    detail_available = sdk.query_mitre_attacks(id=actor_id)["body"]["resources"]
    if detail_available:
        filename = f"{actor_id.replace('-', '_')}.{file_format}"
        print(f"  Retrieving {shiny(actor_name)}", end="\r", flush=True)
        filename = os.path.join(folder, filename)
        with open(filename, "wb") as save_file:
            save_file.write(sdk.get_mitre_report(actor_id=actor_id, format=file_format))
        download_successful = True

    return download_successful


def consume_arguments():
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    required = parser.add_argument_group("required arguments")
    required.add_argument("-k", "--falcon_client_id",
                          help="CrowdStrike Falcon API Client ID",
                          required=True
                          )
    required.add_argument("-s", "--falcon_client_secret",
                          help="CrowdStrike Falcon API Client Secret",
                          required=True
                          )
    parser.add_argument("-g", "--usgov",
                        help="US GovCloud customers",
                        default=False,
                        action="store_true"
                        )
    parser.add_argument("-f", "--format",
                        help="Report format (csv [default] or json)",
                        default="csv"
                        )
    parser.add_argument("-i", "--id_search",
                        help="Filter by actor slug (stemmed search, comma delimit)",
                        default=None
                        )

    return parser.parse_args()


def get_actor_slugs(sdk: Intel, id_string: str):
    """Retrieve a list of actor slugs for the specified (or all) adversaries."""
    filter_string = None
    if id_string:
        filters = []
        for act in id_string.split(","):
            filters.append(f"slug:*'*{act.lower()}*'")
        filter_string = ",".join(filters)
    actors = sdk.query_actor_entities(limit=5000, filter=filter_string, fields="slug")
    if actors["status_code"] != 200:
        error_detail = f"API Error: {actors['body']['errors'][0]['message']}"
        raise SystemExit(error_detail)
    return [a["slug"] for a in actors["body"]["resources"]]


def open_sdk(cmd: Namespace):
    """Return an authenticated instance of the Intel Service Class."""
    return Intel(client_id=cmdline.falcon_client_id,
                 client_secret=cmdline.falcon_client_secret,
                 base_url="usgov1" if cmd.usgov else "auto"
                 )


def download_reports(sdk: Intel, file_format: str, actors: list):
    """Asynchronously download all available reports for the adversary list."""
    subfolder = os.path.join(os.getcwd(), f"mitre_{datetime.utcnow().strftime('%m%d%YT%H%M%SZ')}")
    os.makedirs(subfolder, exist_ok=True)
    success = 0
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(download_thread, slug, sdk, file_format, subfolder) for slug in actors
        }
        for fut in futures:
            if fut.result():
                success += 1

    print(f"{success} MITRE ATT&CK reports downloaded.")


if __name__ == "__main__":
    # Confirm our running FalconPy version
    version_check()
    # Retrieve provided command line arguments
    cmdline = consume_arguments()
    # Create an instance of the Intel Service Class
    intel = open_sdk(cmdline)
    # Get a list of available adversary slugs filtering by the id_search argument
    slugs = get_actor_slugs(intel, cmdline.id_search)
    # Download all reports to a subfolder using the specified file format
    download_reports(intel, cmdline.format, slugs)
