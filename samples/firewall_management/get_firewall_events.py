r"""Dump CrowdStrike Firewall events to a file.

 _______ __                           __ __
|   _   |__.----.-----.--.--.--.---.-|  |  |
|.  1___|  |   _|  -__|  |  |  |  _  |  |  |
|.  __) |__|__| |_____|________|___._|__|__|
|:  |
|::.|        ___ ___                                                    __
`---'       |   Y   .---.-.-----.---.-.-----.-----.--------.-----.-----|  |_
            |.      |  _  |     |  _  |  _  |  -__|        |  -__|     |   _|
            |. \_/  |___._|__|__|___._|___  |_____|__|__|__|_____|__|__|____|
            |:  |   |                 |_____|
            |::.|:. |                               FalconPy v1.0
            `--- ---'

Creation: 05.13.2022, wozboz@CrowdStrike
"""


import json
from argparse import ArgumentParser, RawTextHelpFormatter
from falconpy import FirewallManagement


parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
req = parser.add_argument_group("required arguments")
req.add_argument("-k", "--falcon_client_id",
                 help="CrowdStrike Falcon API Client ID",
                 required=True
                 )
req.add_argument("-s", "--falcon_client_secret",
                 help="CrowdStrike Falcon API Client Secret",
                 required=True
                 )
parser.add_argument("-b", "--base_url",
                    help="CrowdStrike base URL (only required for GovCloud, pass usgov1)",
                    required=False,
                    default="auto"
                    )

parser.add_argument("-l", "--limit",
                    help="FQL filter to use to filter detections",
                    required=False,
                    default="10000"
                    )

args = parser.parse_args()


TOTAL_LIMIT = args.limit

falcon = FirewallManagement(client_id=args.falcon_client_id,
                            client_secret=args.falcon_client_secret,
                            base_url=args.base_url
                            )


def main():
    """Start main routine."""
    results = []
    response = falcon.query_events(limit=500)
    if response["status_code"] != 200:
        err = response["body"]["errors"][0]
        emsg = err["message"]
        ecode = err["ecode"]
        raise SystemExit(f"[{ecode}] {emsg}")
    if not response["body"]["resources"]:
        raise SystemExit("No firewall events found!")
    first_event_response = falcon.get_events(ids=response["body"]["resources"])
    results.extend(first_event_response["body"]["resources"])
    response_after = response["body"]["meta"]["pagination"]["after"]
    while response_after:
        print("Querying... " + "Queried " + str(len(results)) + " events until now.")
        next_response = falcon.query_events(filter="",
                                            limit=500,
                                            after=response_after
                                            )
        next_event_response = falcon.get_events(ids=next_response["body"]["resources"])
        results.extend(next_event_response["body"]["resources"])
        if len(results) >= int(TOTAL_LIMIT):
            break
        response_after = next_response["body"]["meta"]["pagination"]["after"]

    print("Queried " + str(len(results)) + " events in total.")
    with open('CS_Firewall_Events.json', 'w', encoding="utf-8") as outfile:
        json.dump(results, outfile)


if __name__ == "__main__":
    main()
