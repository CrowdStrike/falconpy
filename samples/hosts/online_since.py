#!/usr/bin/env python3
r"""List the number of hosts within a tenant broken out by online duration.

  ______   .__   __.  __       __  .__   __.  _______         _______. __  .__   __.   ______  _______
 /  __  \  |  \ |  | |  |     |  | |  \ |  | |   ____|       /       ||  | |  \ |  |  /      ||   ____|
|  |  |  | |   \|  | |  |     |  | |   \|  | |  |__         |   (----`|  | |   \|  | |  ,----'|  |__
|  |  |  | |  . `  | |  |     |  | |  . `  | |   __|         \   \    |  | |  . `  | |  |     |   __|
|  `--'  | |  |\   | |  `----.|  | |  |\   | |  |____    .----)   |   |  | |  |\   | |  `----.|  |____
 \______/  |__| \__| |_______||__| |__| \__| |_______|   |_______/    |__| |__| \__|  \______||_______|

This script is a modified version of a similar script developed by
Trueblood506@CrowdStrike and is located here: https://github.com/Trueblood506/HostOnline
"""
import sys
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
import pandas as pd
from falconpy import Hosts


def retrieve_api_data(logger: logging.Logger, config: ArgumentParser):
    """Retrieve hostname, first_seen and last_seen for every host in our tenant."""
    logger.info("Connecting to API")
    hosts = Hosts(client_id=config.falcon_client_id,
                  client_secret=config.falcon_client_secret,
                  base_url=config.base_url
                  )
    host_details = {}
    offset = ""
    total = 1
    retrieved = 0
    logger.info("Retrieving details for all available hosts")
    while retrieved < total:
        logger.debug("Querying API for hosts")
        result = hosts.query_devices_by_filter_scroll(limit=5000, offset=offset, sort="hostname|asc")
        page = result["body"]["meta"].get("pagination", {"total": 0})
        total = page["total"]
        if not total:
            log.error("No hosts found")
            raise SystemExit("\nProcess exited as no hosts were returned.")
        offset = page["offset"]
        total_returned = len(result["body"]["resources"])
        retrieved += total_returned
        logger.debug("Retrieved %i IDs (%i / %i)", total_returned, retrieved, total)
        if result["body"]["resources"]:
            detail = hosts.get_device_details(
                        result["body"]["resources"]
                        )["body"]["resources"]
            for host in detail:
                if host.get("first_seen", None) and host.get("last_seen", None):
                    host_details[host["device_id"]] = {
                        "hostname": host.get("hostname", "Unknown"),
                        "last_seen": host.get("last_seen"),
                        "first_seen": host.get("first_seen")
                    }
        logger.debug("Retrieved hostname, first_seen and last_seen for this %i hosts", total_returned)

    logger.info("Retrieved details for a total of %i hosts", len(host_details))

    return host_details


def process_data(dataset: pd.DataFrame, logger: logging.Logger):
    """Use pandas to quickly process our returned dataset."""
    logger.info("Processing dataset")
    dframe = pd.DataFrame().from_dict(dataset, orient="index")
    logger.debug("Calculating differences")
    difference = pd.to_datetime(dframe["last_seen"].values) - pd.to_datetime(dframe["first_seen"].values)
    difference = difference.astype("timedelta64[h]")
    difference = difference.values.tolist()
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    logger.debug("Processing difference results")
    for i in difference:
        if i < 1:
            count8 += 1
        elif i >= 720:
            count7 += 1
        elif i >= 168:
            count6 += 1
        elif i >= 24:
            count5 += 1
        elif i >= 8:
            count4 += 1
        elif i >= 4:
            count3 += 1
        elif i >= 2:
            count2 += 1
        elif i >= 1:
            count += 1
    return count8, count, count2, count3, count4, count5, count6, count7


def logger_setup(config: ArgumentParser):
    """Create a log utility to show results."""
    logging.basicConfig(stream=sys.stdout, format='%(levelname)-8s%(message)s')
    log_device = logging.getLogger("online_since")
    log_level = logging.INFO
    if str(config.log_level).upper() == "DEBUG" or str(config.log_level).upper().startswith("D"):
        log_level = logging.DEBUG
    log_device.setLevel(log_level)
    return log_device


def show_result(data_to_process: dict, log_utility: logging.Logger):
    """Use the log utility to show the results of our processed data."""
    results = process_data(data_to_process, log_utility)
    log_utility.info("There are %i devices that have been online for less than 1 hour.", results[0])
    log_utility.info("There are %i devices that have been online for more than 1 hour.", results[1])
    log_utility.info("There are %i devices that have been online for more than 2 hours.", results[2])
    log_utility.info("There are %i devices that have been online for more than 4 hours.", results[3])
    log_utility.info("There are %i devices that have been online for more than 8 hours.", results[4])
    log_utility.info("There are %i devices that have been online for more than 24 hours.", results[5])
    log_utility.info("There are %i devices that have been online for at least a week.", results[6])
    log_utility.info("There are %i devices that have been online for at least a month.", results[7])


def consume_arguments():
    """Consume and return any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-k", "--falcon_client_id", help="CrowdStrike API Client ID", required=True)
    parser.add_argument("-s", "--falcon_client_secret", help="CrowdStrike API Client Secret", required=True)
    parser.add_argument("-b", "--base_url",
                        help="CrowdStrike Falcon Base URL (only required for GovCloud)",
                        default="auto",
                        required=False
                        )
    parser.add_argument("-l", "--log_level", help="Logging level (debug, info)", default="info", required=False)

    return parser.parse_args()


if __name__ == "__main__":
    args = consume_arguments()
    log = logger_setup(args)
    api_data = retrieve_api_data(log, args)
    show_result(api_data, log)
