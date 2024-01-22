#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script is intended to find users listed in Child CIDs. It was developed to help identify users that may need to be removed from the console, or don't belong, as most users belong in the Parent CID.
#Developed by Don-Swanson-Adobe

#Import API Harness and Auth File
from falconpy import APIHarness
from auth import *

#Do the needful for each CID in the auth file
for key, value in cids.items():
    print("\n"+value)
    falcon = APIHarness(client_id=clientid, client_secret=clientsec, member_cid=key)
    response = falcon.command("RetrieveUserUUIDsByCID")
    print(response["body"]["resources"])