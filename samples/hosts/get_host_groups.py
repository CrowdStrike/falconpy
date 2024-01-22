#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script is intended to output a list of all Host Groups in each Child CID listed in the auth file.
#Developed by Don-Swanson-Adobe

#Import API Harness and Auth File
from falconpy import APIHarness
from auth import *

#Do the needful for each CID in the auth file
for key, value in cids.items():
    print("\n"+value)
    falcon = APIHarness(client_id=clientid, client_secret=clientsec, member_cid=key)
    response = falcon.command("queryCombinedHostGroups")
    for group in response["body"]["resources"]:
        print("ID: ",group["id"])
        print("Name: ",group["name"])
        print("Description: ",group["description"])
        print("\n")