#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this scrip with the "clientid" and "clientsec" variables defined.
#This script is intended to check if a specific host group is properly assigned to specific Prevention Policies. It was developed after we discovered that the API tended to not be able to merge/rectify when multiple API calls were made in a short period of time.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
group_name = "Active Policy" #Name of the group to check for
proactive_policy_ids =["123456789012345678901234567890", "098765432109876543210987654321"] #List of policy IDs to check against
#Policy IDs can be found by looking at the end of the URL when viewing the policy in the UI
###############################################

#Import API Harness and Auth File
from falconpy import APIHarness
from auth import *

#Do the needful for each CID in the auth file
for key, value in cids.items():
    print("\n"+value)
    print("CID: "+key)
    #Auth
    falcon = APIHarness(client_id=clientid, client_secret=clientsec, member_cid=key)

    #Find Group ID for the group name
    response = falcon.command("queryCombinedHostGroups")
    out = response["body"]["resources"]
    for groups in out:
        if groups["name"] == group_name:
            Group_ID = (groups["id"])

    #Get the policy details and check if host group exists
    response = falcon.command("getPreventionPolicies", ids=proactive_policy_ids)
    for i in response['body']['resources']:
        print(i["platform_name"])
        print("Policy ID: ",i["id"])
        for g in i['groups']:
            if g["id"] == Group_ID:
                print(group_name+" Assigned")