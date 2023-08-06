"""Falcon Spotlight Data Grabber.

Usage:
python3 get_spotlight_vulnerabilites.py --client_id <your client id> --verbose
"""
from pprint import pprint
import pandas as pd
from argparse import ArgumentParser, RawTextHelpFormatter
from getpass import getpass
from datetime import datetime
from falconpy import SpotlightVulnerabilities

# Spotlight Vulnerabilities Grabber  
# This tool grabs all spotlight vulnerabilities on an account given a
# filter derived from FQL: https://falconpy.io/Service-Collections/Spotlight-Vulnerabilities.html

SEARCH_FILTER_EVERYTHING = "created_timestamp:>'2019-11-25T22:36:12Z'"
SEARCH_FILTER_TEST = "status:!'closed'+last_seen_within:'3'+cve.exprt_rating:['CRITICAL']"

def get_all_vulnerabilites_from_account(client_id, secret, filter, verbose=False):
    print('[+] Grabbing Spotlight Vulnerabilities, this may take some time for larger environments...')
    time_start = datetime.now()
    spotlight = SpotlightVulnerabilities(client_id=client_id,
              client_secret=secret
              )

    iterations = 0
    facet = {"cve", "host_info", "remediation", "evaluation_logic"}
    spotlight_results = spotlight.query_vulnerabilities_combined(filter=filter, facet=facet, limit=400)
    after = 'blah'
    rows_dict_list = []
    while after != None:
        # Retrieve a list of vulns
        # Confirm we received a success response back from the CrowdStrike API
        if spotlight_results["status_code"] == 200:
            spotlight_list = spotlight_results["body"]["resources"]
            for resource in spotlight_list:
                rows_dict_list.append(resource)
        else:
            # Retrieve the details of the error response
            error_detail = spotlight_results["body"]["errors"]
            for error in error_detail:
                #error structure may be different and not include a code if the lib
                #didn't actually make an HTTP request, so let's just print the whole error for now
                raise SystemExit(error)

        # Stop as we've received less results than we requested
        if len(spotlight_results["body"]["resources"]) < 400:
            break

        after = None
        if 'after' in spotlight_results['body']['meta']['pagination']:
            after = spotlight_results['body']['meta']['pagination']['after']
        
        iterations += 1
        if iterations % 20 == 0 and verbose:
            elapsed_time = datetime.now() - time_start 
            elapsed_minutes = elapsed_time.seconds / 60
            elapsed_seconds = elapsed_time.seconds % 60
            print("[+] Total API Calls: %d" % iterations)
            print("[+] Total Records Pulled: %d" % len(rows_dict_list))
            print("[+] Elapsed Time (seconds): %d minutes %d seconds" % (elapsed_minutes, elapsed_seconds))
            
        spotlight_results = spotlight.query_vulnerabilities_combined(filter=filter,
                                                                     limit=400,
                                                                     after=after,
                                                                     facet=facet
                                                                     )

    return pd.json_normalize(rows_dict_list)

def main():
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument('-k', '--client_id',
                        type=str,
                        required=True,
                        help="The Client ID of your Falcon API Key"
                        )
    parser.add_argument('-s', '--client_secret',
                        type=str,
                        required=True,
                        help="The Client secret of your Falcon API Key"
                        )
    parser.add_argument('-o', '--output_file',
                        type=str,
                        required=False,
                        help="The output file for the associated vulnerabilities",
                        default="spotlight_vulnerabilities.txt"
                        )
    parser.add_argument('-f', '--filter',
                        type=str,
                        required=False,
                        help="Filter for Vulnerabilities created via FQL: https://falconpy.io/Service-Collections/Spotlight-Vulnerabilities.html",
                        default="status:!'closed'+last_seen_within:'3'+cve.exprt_rating:['CRITICAL']"
                        )
    parser.add_argument('-p', '--prune',
                        help="Comma delimited list of columns to prune",
                        required=False,
                        default=None
                        )
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        required=False,
                        help="Give Verbose Information On Data Pull",
                        default=False
                        )
    args = parser.parse_args()
    spotlight_data = get_all_vulnerabilites_from_account(args.client_id,
                                                         args.client_secret,
                                                         args.filter,
                                                         args.verbose
                                                         )
    if args.prune:
        # Remove any columns they asked us to prune
        for pruned in args.prune.split(","):
            spotlight_data.pop(pruned)
    # Output the result to CSV
    spotlight_data.to_csv(args.output_file)

if __name__ == "__main__":
    main()
