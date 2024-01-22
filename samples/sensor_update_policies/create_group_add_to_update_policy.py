#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script was developed to create a new dynamic group based on a specific assignment rule and then add that group to a list of update policies. This is expecially useful when you want to create a dynamic group based on specific and/or criteria that you cannot do via the UI. NOTE: If you do use custom and/or criteria here, editing the group in the UI will remove the custom and/or and destroy the group function.
#You will need to create the Update Policy first and grab it's Policy ID (The last random string in the URL)
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
policies=["098765432109876543210987654321",] #Replace with Update Policies you wish the group to join
group_name=  "MacOS Ventura" #Replace with desired group name
group_description = "MacOS Ventura Hosts" #Replace with groups description
group_type = "dynamic" #Replace with group type
assignment_rule = "os_version:'Ventura (13)'" #Replace with the desired assignment rule
###############################################
#Dynamic Host group examples with custom and/or criteria
#AND Example:
#Product is Windows AND Type is Server
#       "platform_name:'Windows'+product_type_desc:'Server'"
#
#OR Examples:
#OS is Win Server 2008 R2 OR OS is Windows 7
#       "os_version:'Windows Server 2008 R2',os_version:'Windows 7'"
#OS is Win Server 2008 R2 OR OS is Windows 7
#       "(os_version:'Windows Server 2008 R2',os_version:'Windows 7')"
#
#Mixed Use
#Must Have a DEV Sensor Tag and a Team1 or Team2 Sensor Tag
#       "(tags:'SensorGroupingTags/DEV'+tags:'SensorGroupingTags/Team1),(tags:'SensorGroupingTags/DEV'+tags:'SensorGroupingTags/Team2')"
#       "tags:'SensorGroupingTags/DEV'+(tags:'SensorGroupingTags/Team1',tags:'SensorGroupingTags/Team2')"

#Import API Harness and Auth File
from falconpy import APIHarness
from auth import *

#Do the needful for each CID in the auth file
for key, value in cids.items():
    print("\n"+value)
    #Auth
    falcon = APIHarness(client_id=clientid, client_secret=clientsec, member_cid=key)

    #Create Host Group
    BODY = {
        "resources": [{
                "assignment_rule": assignment_rule,
                "description": group_description,
                "group_type": group_type,
                "name": group_name}]}

    response = falcon.command("createHostGroups", body=BODY)
    print("New Group ID: "+response["body"]["resources"][0]["id"])
    group_id = response["body"]["resources"][0]["id"]

    #Attach new group to policy
    for i in policies:
        BODY = {"action_parameters": [{"name": "group_id","value": group_id}],"ids": [i]}
        response = falcon.command("performSensorUpdatePoliciesAction", action_name="add-host-group", body=BODY)
        print("Response Code: " + str(response["status_code"]))
        print("Errors: " + str(response["body"]["errors"]))
