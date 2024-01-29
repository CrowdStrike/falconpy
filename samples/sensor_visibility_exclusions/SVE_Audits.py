#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script is intended to output a list of SVEs in each Child CID listed in the auth file along with Created and Modified On/By details. Useful for regular audits of SVEs across multiple CIDs.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
outpath = "../SVE_Audits.txt" #Location of the output CSV
#Note: './' is 1 directory up from current, '../' is 2 directories up
###############################################

#Import API Harness and Auth File
from falconpy import APIHarness
from auth import *

#Establish the output file
file_object = open(outpath, 'a+')

#Do the needful for each CID in the auth file
for key, value in cids.items():
    print("\n\n\n\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n"+value+"\nCID: "+key+"\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
    file_object.write("\n\n\n\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n"+value+"\nCID: "+key+"\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
    #Auth
    falcon = APIHarness(client_id=clientid, client_secret=clientsec, member_cid=key)

    #Query for the list of SVEs in the CID, Pull out the SVE Value, who Created/Modified it and when, then store to the output file
    response = falcon.command("querySensorVisibilityExclusionsV1")
    if len(response["body"]["resources"]):
        sveresponse = falcon.command("getSensorVisibilityExclusionsV1", ids=response["body"]["resources"])
        for detail in sveresponse["body"]["resources"]:
            sve = (detail["value"])
            createdby = (detail["created_by"])
            createdon = (detail["created_on"])
            modifiedby = (detail["modified_by"])
            modifiedon = (detail["last_modified"])
            print("\nSVE: "+sve+"\nCreator: "+createdby+"\nCreated on: "+createdon+"\nLast Modified by: "+modifiedby+"\nLast Modified on: "+modifiedon+"\n")
            file_object.write("\nSVE: "+sve+"\nCreator: "+createdby+"\nCreated on: "+createdon+"\nLast Modified by: "+modifiedby+"\nLast Modified on: "+modifiedon+"\n")

#Close out the file write
file_object.close()