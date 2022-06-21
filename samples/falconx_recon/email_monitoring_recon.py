"""Add monitoring rules for email addresses provided in a csv file (1 email address per row)
 _____     _                  __  __  ____                      
|  ___|_ _| | ___ ___  _ __   \ \/ / |  _ \ ___  ___ ___  _ __  
| |_ / _` | |/ __/ _ \| '_ \   \  /  | |_) / _ \/ __/ _ \| '_ \ 
|  _| (_| | | (_| (_) | | | |  /  \  |  _ <  __/ (_| (_) | | | |
|_|  \__,_|_|\___\___/|_| |_| /_/\_\ |_| \_\___|\___\___/|_| |_|

Creation: 06.21.2022, wozboz@CrowdStrike
"""


from falconpy import Recon
from csv import reader
from argparse import ArgumentParser, RawTextHelpFormatter

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

parser.add_argument("-f", "--file",
                    help="File with email-addresses to use as input",
                    required=True,
                    )

args = parser.parse_args()


EMAIL_FILE = args.file

falcon = Recon(client_id=args.falcon_client_id,
               client_secret=args.falcon_client_secret,
               base_url=args.base_url
               )

query = "("
with open(EMAIL_FILE) as read_file:
    csv_reader = reader(read_file)
    n = 0
    for row in csv_reader:
        n += 1
        query += "email:'" + str(row[0]) + "',"
        if n%20 == 0:
            query = query[:-1]
            query += ")"
            response = falcon.create_rules(filter=f"{query}",
                                    name=f"Functional Email Addresses{int(n/20)}",
                                    priority="medium",
                                    topic="SA_EMAIL",
                                    permissions="public",
                                    )
            query = "("

query = query[:-1]
query += ")"
response = falcon.create_rules(filter=f"{query}",
                                    name=f"Functional Email Addresses{n}",
                                    priority="medium",
                                    topic="SA_EMAIL",
                                    permissions="public",
                                    )

print(f"Successfully created monitoring rules for {n} email addresses.")