#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script was developed to clone the prevention policies from one CID to another. It was developed to be run once and will create the policies and populate them with the appropriate settings.
#Developed by Don-Swanson-Adobe

#Import API Harness and Auth Filefrom auth import *
from falconpy import APIHarness
from auth import *
falcon_source = APIHarness(client_id=clientid, client_secret=clientsec) #Source CID API Harness with all the policies you wish to clone
falcon_dest = APIHarness(client_id=clientid_2, client_secret=clientsec_2) #Destination CID API Harness with no policies

policydetails = falcon_source.command("queryCombinedPreventionPolicies")["body"]["resources"]
print(policydetails)

for policy in policydetails:
    config = []    
    for prev_settings in policy["prevention_settings"]:
        for settings in prev_settings["settings"]:
            setting_dict = {"id": settings["id"], "value": settings["value"]}
            config.append(setting_dict)
    BODY = {"resources": [{"description": policy["description"],"name": policy["name"],"platform_name": policy["platform_name"],"settings": config}]}
    print(BODY)
    response = falcon_dest.command("createPreventionPolicies", body=BODY)
    print(response)
    print("wait")