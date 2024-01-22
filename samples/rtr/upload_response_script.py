#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script is intended to be used to upload a response script to all child CIDs listed in the auth file.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
f_filepath = "./ResponseScript.ps1" #Note: './' is 1 directory up from current, '../' is 2 directories up
f_name = "ResponseScript 2.0"
f_description = "SOC ResponseScript - Current As Of 01/01/2001"
f_platform = "windows" #windows, mac, linux
f_comment = "Updated to version 2.0" #Comment for Audit Log
f_permission = "public" #private: usable by only the user who uploaded it
                        #group: usable by all RTR Admins
                        #public: usable by all active-responders and RTR admins

###############################################

#Import API Harness and Auth File
from falconpy import APIHarness
from auth import *

#Setup the payload with the variables from above
PAYLOAD = {
    "description": f_description,
    "name": f_name,
    "comments_for_audit_log": f_comment,
    "permission_type": f_permission,
    "platform": [f_platform]
}
#Load File to be uploaded
file_upload = {'file': open(f_filepath, 'rb')}

#Upload the response script to each of the Child CIDs listed in the auth file
for key, value in cids.items():
    print("\n"+value)
    falcon = APIHarness(client_id=clientid, client_secret=clientsec, member_cid=key)

    response = falcon.command("RTR_CreateScripts", data=PAYLOAD, files=file_upload)
    print("Status Code: ",response["status_code"])
