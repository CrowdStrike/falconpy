#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script is used in combination with the upload_response_script.py script to remove old response scripts from all CIDs listed in the auth file.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
f_name = "ResponseScript 1.0" #Name of the script to remove
###############################################

#Import API Harness and Auth File
from falconpy import APIHarness
from auth import *

#Do the needful for each CID in the auth file
for key, value in cids.items():
    print("\n"+value)
    falcon = APIHarness(client_id=clientid, client_secret=clientsec, member_cid=key)

    #Find Script ID
    id = falcon.command("RTR_ListScripts",filter="name:'"+f_name+"'")["body"]["resources"][0]
    print("Script ID: ",id)

    #Remove Script
    response = falcon.command("RTR_DeleteScripts", ids=id)
    print("Status Code: ",response["status_code"])
