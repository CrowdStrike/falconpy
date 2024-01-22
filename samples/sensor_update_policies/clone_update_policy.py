#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script was developed to clone the sensor update policies from one CID to another. It was developed to be run once and will create the policies and populate them with the appropriate settings.
#Developed by Don-Swanson-Adobe

#Import API Harness and Auth File
from auth import *
from falconpy import APIHarness
falcon_source = APIHarness(client_id=clientid, client_secret=clientsec) #Source CID API Harness with all the policies you wish to clone
falcon_dest = APIHarness(client_id=clientid_2, client_secret=clientsec_2) #Destination CID API Harness with no policies

policydetails = falcon_source.command("queryCombinedSensorUpdatePoliciesV2")["body"]["resources"]

for policy in policydetails:
    if policy["platform_name"] == "Linux":
        settings = {"build": str(policy["settings"]["build"])}
    else:
        settings = {"build": str(policy["settings"]["build"]), "uninstall_protection": policy["settings"]["uninstall_protection"]}
    BODY = {"resources": [{"description": policy["description"],"name": policy["name"],"platform_name": policy["platform_name"],"settings": settings}]}
    print(BODY)
    response = falcon_dest.command("createSensorUpdatePoliciesV2", body=BODY)
    print(response)
