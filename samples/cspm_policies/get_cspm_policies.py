import argparse
import json
import csv
from falconpy import cspm_registration as FalconCSPM

parser = argparse.ArgumentParser(description="Gather API client_id and client_secret from arguments")
parser.add_argument("-f", "--falcon_client_id", help="Falcon Client ID", required=True)
parser.add_argument("-s", "--falcon_client_secret", help="Falcon Client Secret", required=True)
parser.add_argument("-o", "--output_file", help="Policy report output file", required=True)
parser.add_argument("-c", "--cloud", help="Cloud provider (aws, azure, gcp)", required=False)
args = parser.parse_args()

falcon_client_id = args.falcon_client_id
falcon_client_secret = args.falcon_client_secret
data_file = args.output_file
cloud = args.cloud

falcon = FalconCSPM.CSPM_Registration(
    creds={"client_id": falcon_client_id, 
            "client_secret": falcon_client_secret
})

if cloud:
    policies = falcon.GetCSPMPolicySettings("cloud-platform=" + cloud)['body']['resources']
else:
    policies = falcon.GetCSPMPolicySettings()['body']['resources']

length = 0
headers = []
for p in policies:
    if len(p.keys()) > length:
        length = len(p.keys())
        headers = [*p]
list_dict = []
for p in policies:
    policy = ""
    for h in headers:
        try:
            if h == headers[-1]:
                str_line = "\"{}\": \"{}\"".format(h,str(p[h]).strip("\n").replace('"',''))
            else:
                str_line = "\"{}\": \"{}\", ".format(h,str(p[h]).strip("\n").replace('"',''))
        except:
            if h == headers[-1]:
                str_line = "\"{}\": \"{}\"".format(h,"")
            else:
                str_line = "\"{}\": \"{}\", ".format(h,"")
        policy += str_line
    new_dict = "{{{}}}".format(policy)
    list_dict.append(json.loads(new_dict))

keys = list_dict[0].keys()
with open(data_file, 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list_dict)