#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script was developed to setup the default groups in a new CID. It was developed to be run once and will create the groups and populate them with the appropriate assignment rules.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
groups = {"Sensor Uninstall Group": "staticByID", "Phase 0": "none", "Phase 1": "hostname:*'*'","Active Policy": "none", "Windows Servers": "platform_name:'Windows'+product_type_desc:'Server'", "DEV Updates": "tags:'SensorGroupingTags/DEV'", "Golden Images": "tags:'FalconGroupingTags/GoldenImage'", "Windows 7 and Server 2008 R2 Hosts": "(os_version:'Windows Server 2008 R2',os_version:'Windows 7')"}
#Groups are defined as "Group Name": "Assignment Rule"
###############################################


#Import API Harness and Auth File
from falconpy import APIHarness
from auth import *

#Function to add groups
def add_group(name,rule):
    if rule == "staticByID":
        BODY = {"resources": [{
            "group_type": "staticByID",
            "name": name
        }]}
    elif rule == "none":
        BODY = {"resources": [{
            "group_type": "dynamic",
            "name": name
        }]}
    else:
        BODY = {"resources": [{
            "group_type": "dynamic",
            "name": name,
            "assignment_rule": rule
        }]}
    response = falcon.command("createHostGroups", body=BODY)
    print(response)

#Do the needful for each CID in the auth file
for key, value in cids.items():
    print("\n"+value)
    falcon = APIHarness(client_id=clientid, client_secret=clientsec, member_cid=key)

    #Add groups with variable names dependent on CID Name(Useful for at a glance reporting of All Hosts and RFM Hosts):
    groups.update({value + " - All":"hostname:*'*'", value + " - RFM": "reduced_functionality_mode:'yes'"})

    #Add Groups
    for name,rule in groups.items():
        add_group(name,rule)