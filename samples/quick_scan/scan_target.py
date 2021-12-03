"""Quick Scan a folder or a bucket"""
#   _______ ___ ___ ___ _______ ___ ___    _______ _______ _______ ______     _______ _______ ___
#  |   _   |   Y   |   |   _   |   Y   )  |   _   |   _   |   _   |   _  \   |   _   |   _   |   |
#  |.  |   |.  |   |.  |.  1___|.  1  /   |   1___|.  1___|.  1   |.  |   |  |.  1   |.  1   |.  |
#  |.  |   |.  |   |.  |.  |___|.  _  \   |____   |.  |___|.  _   |.  |   |  |.  _   |.  ____|.  |
#  |:  1   |:  1   |:  |:  1   |:  |   \  |:  1   |:  1   |:  |   |:  |   |  |:  |   |:  |   |:  |
#  |::..   |::.. . |::.|::.. . |::.| .  ) |::.. . |::.. . |::.|:. |::.|   |  |::.|:. |::.|   |::.|
#  `----|:.`-------`---`-------`--- ---'  `-------`-------`--- ---`--- ---'  `--- ---`---'   `---'
#       `--'                                                     Josh's Quick Scan experiment
#
# Scans either a folder or a S3 bucket using the CrowdStrike Falcon X Quick Scan and Sandbox APIs.
#
# Created // 04.12.21: jshcodes@CrowdStrike - In order to proceed, please insert 16oz of coffee.
#
# ===== NOTES REGARDING THIS SOLUTION ============================================================
#
# This is a proof of concept. Extensive performance testing has not been performed at this time.
#
# A VOLUME is a collection of files that are uploaded and then scanned as a singular batch.
#
# LOCAL DIRECTORY scanning: the folder is inventoried and then files are uploaded to the API in a
# linear fashion. This method is only impacted by data transfer speeds from the source file system
# location to CrowdStrike's cloud. Supports pattern matching to filter objects scanned using the
# "--pattern" or "-p" command line parameter.
#
# S3 BUCKET scanning: the bucket contents are inventoried, and then the contents are downloaded
# to local memory and uploaded to the Sandbox API in a linear fashion. This method does NOT store
# the files on the local file system. Due to the nature of this solution, the method is heavily
# impacted by data transfer speeds. Recommended deployment pattern involves running in AWS within
# a container, an EC2 instance or as a serverless lambda. Scans the entire bucket whether you like
# it or not. You must specify a target that includes the string "s3://" in order to scan a bucket.
#
# The log file rotates because cool kids don't leave messes on other people's file systems.
#
# This solution is dependant upon Amazon's boto3 library, and CrowdStrike FalconPy >= v0.8.7.
#     python3 -m pip install boto3 crowdstrike-falconpy
#
# Example config.json file:
#
#    {
#        "falcon_client_id": "API ID GOES HERE",
#        "falcon_client_secret": "API SECRET GOES HERE"
#    }
#
#
# This solution has been tested on Python 3.7 / 3.9 running under Amazon Linux 2 and MacOS 10.15.
#
# ================================================================================================
# pylint: disable=E0401, R0903
#
import io
import os
import json
import time
import argparse
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
# AWS Boto library
import boto3
# !!! Requires FalconPy v0.8.7+ !!!
# Authorization, Sample Uploads and QuickScan Service Classes
from falconpy import OAuth2, SampleUploads, QuickScan


class Analysis:
    """Class to hold our analysis and status."""
    def __init__(self):
        self.uploaded = []
        self.files = []
        self.scanning = True
        # Dynamically create our payload using the contents of our uploaded list
        self.payload = lambda: {"samples": self.uploaded}


class Configuration:
    """Class to hold our running configuration."""
    def __init__(self, args):
        self.config_file = "../config.json"
        if args.config_file:
            self.config_file = args.config_file
        self.log_level = logging.INFO
        if args.log_level:
            if args.log_level.upper() in "DEBUG,WARN,ERROR".split(","):
                if args.log_level.upper() == "DEBUG":
                    self.log_level = logging.DEBUG
                elif args.log_level.upper() == "WARN":
                    self.log_level = logging.WARN
                elif args.log_level.upper() == "ERROR":
                    self.log_level = logging.ERROR

        self.target_pattern = "**/*.*"
        if args.pattern:
            self.target_pattern = args.pattern
        self.scan_delay = 3
        if args.check_delay:
            try:
                self.scan_delay = int(args.check_delay)
            except ValueError:
                # They gave us garbage, ignore it
                pass
        # Will stop processing if you give us a bucket and no region
        self.region = None
        if args.region:
            self.region = args.region
        # Target directory or bucket to be scanned
        if "s3://" in args.target:
            self.target_dir = args.target.replace("s3://", "")
            self.bucket = True
        else:
            self.target_dir = args.target
            self.bucket = False


def upload_samples():
    """Upload the samples identified within the target to the Sandbox API."""
    # Retrieve a list of all files and paths within the target
    paths = Path(Config.target_dir).glob(Config.target_pattern)
    # Inform the user as to what we're doing
    logger.info("Assembling %s volume for submission", Config.target_dir)
    # Loop through each identified file and upload it to the sandbox for analysis
    for path in paths:
        # Convert the path to a string
        filepath = str(path)
        # Grab the file name
        filename = os.path.basename(filepath)
        # Open the file for binary read, this will be our payload
        with open(filepath, 'rb') as upload_file:
            payload = upload_file.read()
        # Upload the file using the Sandbox
        response = Samples.upload_sample(file_name=filename, sample=payload)
        # Grab the SHA256 unique identifier for the file we just uploaded
        sha = response["body"]["resources"][0]["sha256"]
        # Add this SHA256 to the volume payload element
        Analyzer.uploaded.append(sha)
        # Track the upload so we can remove the file when we're done
        Analyzer.files.append([filename, filepath, sha])
        # Inform the user of our progress
        logger.debug("Uploaded %s to %s", filename, sha)


def upload_bucket_samples():
    """Retrieve keys from a bucket and then uploads them to the Sandbox API."""
    if not Config.region:
        logger.error("You must specify a region in order to scan a bucket target")
        raise SystemExit(
            "Target region not specified. Use -r or --region to specify the target region."
            )
    # Connect to S3 in our target region
    s_3 = boto3.resource("s3", region_name=Config.region)
    # Connect to our target bucket
    bucket = s_3.Bucket(Config.target_dir)
    # Retrieve a list of all objects in the bucket
    summaries = bucket.objects.all()
    # Inform the user as this may take a minute
    logger.info("Assembling volume from target bucket (%s) for submission", Config.target_dir)
    # Loop through our list of files, downloading each to memory then upload them to the Sandbox
    for item in summaries:
        # Grab the file name from the path
        filename = os.path.basename(item.key)
        # Teensy bit of witch-doctor magic to download the file
        # straight into the payload used for our upload to the Sandbox
        response = Samples.upload_sample(file_name=filename,
                                         file_data=io.BytesIO(
                                             bucket.Object(key=item.key).get()["Body"].read()
                                             )
                                         )
        # Retrieve our uploaded file SHA256 identifier
        sha = response["body"]["resources"][0]["sha256"]
        # Add this SHA256 to the upload payload element
        Analyzer.uploaded.append(sha)
        # Track the upload so we recognize the file when we're done
        Analyzer.files.append([filename, item.key, sha])
        # Inform the user of our progress
        logger.debug("Uploaded %s to %s", filename, sha)


def scan_uploaded_samples() -> dict:
    """Retrieve a scan using the ID of the scan provided by the scan submission."""
    while Analyzer.scanning:
        # Retrieve the scan results
        scan_results = Scanner.get_scans(ids=scan_id)
        try:
            if scan_results["body"]["resources"][0]["status"] == "done":
                # Scan is complete, retrieve our results
                results = scan_results["body"]["resources"][0]["samples"]
                # and break out of the loop
                Analyzer.scanning = False
            else:
                # Not done yet, sleep for a bit
                time.sleep(Config.scan_delay)
        except IndexError:
            # Results aren't populated yet, skip
            pass

    return results


def report_results(results: dict):
    """Retrieve the scan results for the submitted scan."""
    # Loop thru our results, compare to our upload and return the verdict
    for result in results:
        for item in Analyzer.files:
            if result["sha256"] == item[2]:
                if "no specific threat" in result["verdict"]:
                    # File is clean
                    logger.info("Verdict for %s: %s", item[1], result["verdict"])
                else:
                    # Mitigation would trigger from here
                    logger.warning("Verdict for %s: %s", item[1], result["verdict"])


def clean_up_artifacts():
    """Remove uploaded files from the Sandbox."""
    logger.info("Removing artifacts from Sandbox")
    for item in Analyzer.uploaded:
        # Perform the delete
        response = Samples.delete_sample(ids=item)
        if response["status_code"] > 201:
            # File was not removed, log the failure
            logger.warning("Failed to delete %s", item)
        else:
            logger.debug("Deleted %s", item)
    logger.info("Artifact cleanup complete")


def parse_command_line():
    """Parse any inbound command line arguments and set defaults."""
    parser = argparse.ArgumentParser("Falcon Quick Scan")
    parser.add_argument("-f", "--config",
                        dest="config_file",
                        help="Path to the configuration file",
                        required=False
                        )
    parser.add_argument("-l", "--log-level",
                        dest="log_level",
                        help="Default log level (DEBUG, WARN, INFO, ERROR)",
                        required=False
                        )
    parser.add_argument("-d", "--check-delay",
                        dest="check_delay",
                        help="Delay between checks for scan results",
                        required=False
                        )
    parser.add_argument("-p", "--pattern",
                        dest="pattern",
                        help="Target file patterns to scan (defaults to *.*)",
                        required=False
                        )
    parser.add_argument("-r", "--region",
                        dest="region",
                        help="Region the target bucket resides in",
                        required=False
                        )
    parser.add_argument("-t", "--target",
                        dest="target",
                        help="Target folder or bucket to scan. Bucket must have 's3://' prefix.",
                        required=True
                        )

    return parser.parse_args()


def load_api_config():
    """Grab our config parameters from our provided config file (JSON format)."""
    with open(Config.config_file, 'r', encoding="utf-8") as file_config:
        conf = json.loads(file_config.read())

    return OAuth2(client_id=conf["falcon_client_id"],
                  client_secret=conf["falcon_client_secret"]
                  )


def enable_logging():
    """Configure logging."""
    logging.basicConfig(level=Config.log_level,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s"
                        )
    # Create our logger
    log = logging.getLogger("Quick Scan")
    # Rotate log file handler
    rfh = RotatingFileHandler("falcon_quick_scan.log", maxBytes=20971520, backupCount=5)
    # Log file output format
    f_format = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    # Set the log file output level to INFO
    rfh.setLevel(Config.log_level)
    # Add our log file formatter to the log file handler
    rfh.setFormatter(f_format)
    # Add our log file handler to our logger
    log.addHandler(rfh)

    return log


if __name__ == '__main__':
    # Parse the inbound command line parameters and setup our running Config object
    Config = Configuration(parse_command_line())
    # Activate logging
    logger = enable_logging()
    # Grab our authentication object
    auth = load_api_config()
    # Connect to the Samples Sandbox API
    Samples = SampleUploads(auth_object=auth)
    # Connect to the Quick Scan API
    Scanner = QuickScan(auth_object=auth)
    # Create our analysis object
    Analyzer = Analysis()
    # Log that startup is done
    logger.info("Process startup complete, preparing to run scan")
    # Upload our samples to the Sandbox
    if Config.bucket:
        # S3 bucket
        upload_bucket_samples()
    else:
        # Local folder
        upload_samples()
    # Submit our volume for analysis and grab the id of our scan submission
    scan_id = Scanner.scan_samples(body=Analyzer.payload())["body"]["resources"][0]
    # Inform the user of our progress
    logger.info("Scan %s submitted for analysis", scan_id)
    # Retrieve our scan results from the API and report them
    report_results(scan_uploaded_samples())
    # Clean up our uploaded files from out of the API
    clean_up_artifacts()
    # We're done, let everyone know
    logger.info("Scan completed")

#     __  ____    ___   __    __  ___    _____ ______  ____   ____  __  _    ___
#    /  ]|    \  /   \ |  T__T  T|   \  / ___/|      T|    \ l    j|  l/ ]  /  _]
#   /  / |  D  )Y     Y|  |  |  ||    \(   \_ |      ||  D  ) |  T |  ' /  /  [_
#  /  /  |    / |  O  ||  |  |  ||  D  Y\__  Tl_j  l_j|    /  |  | |    \ Y    _]
# /   \_ |    \ |     |l  `  '  !|     |/  \ |  |  |  |    \  |  | |     Y|   [_
# \     ||  .  Yl     ! \      / |     |\    |  |  |  |  .  Y j  l |  .  ||     T
#  \____jl__j\_j \___/   \_/\_/  l_____j \___j  l__j  l__j\_j|____jl__j\_jl_____j
#
#                                                                         ████
#                                                           ████░░    ████▒▒████
#                                                         ██▒▒▒▒████████▒▒▒▒▒▒████
#                                                       ██▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒██
#                                                     ██▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒██
#                                                   ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒██████
#                                                   ██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒████
#                                                 ░░  ████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒██▒▒
#                                               ████    ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██▒▒▒▒██
#                                               ████▒▒████████████▒▒▒▒▒▒▒▒▒▒▓▓██░░██▓▓██         Yup! That's a file...
#                                             ██░░▒▒██████  ░░████████▒▒▒▒▒▒▒▒██░░░░██
#                                           ▒▒██░░░░██▓▓  ██░░██████████▒▒▒▒▒▒▒▒██░░██
#                                           ██▒▒░░░░██▒▒░░    ████░░  ████▒▒▒▒▒▒██▒▒██
#                                         ████░░░░░░░░████▒▒░░██░░░░██░░░░██▒▒▒▒▒▒████
#                                         ██▒▒░░░░░░░░██▒▒░░░░██░░▒▒██████  ████▒▒▒▒██
#                                         ██░░░░░░░░░░▓▓██░░░░██░░  ██    ██▒▒██▓▓▒▒██
#                                     ████████▒▒░░░░░░░░██░░░░░░░░░░██      ████▒▒██▒▒██
#                               ░░████▒▒░░░░▓▓██▓▓░░░░░░▓▓░░░░░░░░░░  ██  ░░░░██    ██▓▓▓▓
#                             ▒▒████░░░░░░░░░░████░░░░░░░░▒▒░░░░░░░░░░░░████████▒▒    ████            ██████
#                           ▒▒██░░░░░░░░░░░░░░░░████░░░░░░██░░░░░░░░░░░░░░  ░░░░██░░    ▒▒        ████▒▒██████
#                         ████░░░░░░░░░░░░░░░░░░░░██░░░░░░██░░░░░░████████░░░░░░░░██            ██░░████████  ██
#                   ████████░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██  ░░██████████░░░░░░░░░░██        ██▒▒████░░░░    ██
#                 ██░░████░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░██░░  ████████░░░░░░░░░░██      ██████░░  ░░██    ██
#               ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓░░░░██░░░░░░████████░░░░░░  ██  ░░██░░██░░    ██    ██
#   ████████    ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░██▒▒██████▒▒████████░░██  ▒▒██░░░░░░    ██      ██
#   ████░░░░░░████▒▒░░████░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░▓▓██████        ██      ░░    ██  ░░██  ░░████░░░░██
#   ░░██░░░░░░░░░░██░░░░████░░░░░░░░░░░░░░██░░░░░░░░░░░░░░████                      ██    ██░░  ▒▒▒▒░░░░░░██
#     ██████▒▒░░░░████░░██░░░░░░██░░░░░░░░██░░░░░░░░░░░░░░░░██                      ██  ██▒▒  ░░████░░░░██
#       ████▒▒░░░░░░██████░░░░██░░░░░░████████░░░░░░░░░░░░░░░░██                  ██  ████░░░░██████████
#     ████░░░░░░░░░░░░██░░░░██████░░░░░░░░░░████░░░░░░░░░░░░░░░░████              ██  ██░░░░██  ▒▒████
#       ██░░░░░░░░░░░░░░░░██░░░░░░████░░░░░░░░██▒▒░░░░░░░░░░░░░░▒▒████          ▒▒████████████░░████
#       ▒▒██░░░░░░░░░░░░░░██▓▓░░░░░░░░████████████░░░░░░░░░░░░░░░░██████    ▓▓▒▒██████  ▒▒██████
#         ████░░░░░░░░░░░░░░██▒▒░░░░░░████░░████▒▒██░░░░░░░░░░░░▓▓██░░██████▒▒██  ▒▒██████████
#           ████░░░░░░░░░░████████▒▒██░░░░▒▒██  ██▒▒██░░░░░░░░░░██░░  ██░░░░░░██████████████
#             ▒▒██░░░░░░░░░░░░░░██████░░░░██▒▒▒▒▒▒░░██░░░░░░░░██░░  ██░░░░░░▒▒████████
#               ▒▒████░░░░░░░░░░░░░░████████  ▒▒▒▒  ████░░░░██  ░░██░░░░▒▒████████
#                 ████████▒▒░░░░░░░░░░░░▒▒████████████████████  ██▒▒░░░░░░████████
#                   ██████████████████▒▒░░░░░░░░██      ████████░░░░░░░░░░░░░░██████
#                     ████████████████████████▒▒██      ▒▒  ██▒▒▓▓░░░░░░░░  ░░░░████
#                     ████████████████████████████              ██░░░░░░░░██▒▒  ██
#                     ████████  ████████████████▒▒              ██  ░░░░░░░░██████
#           ██████████████████      ██████████████              ████░░░░██░░░░██
#           ██████████████████          ████████████            ██████░░░░██████
#           ██████████████████          ████████████            ████████████
#       ▓▓██████████████████▒▒      ░░████████████                ▓▓
#       ████████████████▒▒          ████████████▓▓
#   ░░░░████████████▒▒░░░░░░    ▒▒██████████████
# ░░░░░░░░░░██████░░░░░░░░░░░░░░██████████████
# ░░░░░░░░░░████████████░░░░░░░░██████████████
# ░░░░░░░░░░████████████░░░░░░░░████████████████████
# ░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░████████████████████████
