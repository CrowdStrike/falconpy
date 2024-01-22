#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script is intended to determine the number of hosts in RFM (Up for more than 24 hours and seen within the last 24 hours) in each Child CID listed in the auth file.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
outpath = './RFM_Report.csv' #Location of the output CSV
#Note: './' is 1 directory up from current, '../' is 2 directories up
###############################################

#Import API Harness and Auth File
from falconpy import APIHarness
from auth import *
from datetime import datetime, timedelta

#Establish 24 hours ago as the last seen time, setup the output file, and the variable to store which serial numbers we found
lastseen = (datetime.now() - timedelta(hours = 24)).strftime('%Y-%m-%dT%H:%M:%SZ')
file_object = open(outpath, 'a+')
file_object.write("CID,Hostname,AID,Last Seen,RFM,OS,Kernel,Sensor Version,Tag1,Tag2,Tag3,Tag4\n")
filter = "last_seen:>='"+lastseen+"'+first_seen:<='"+lastseen+"'+reduced_functionality_mode:'yes'"
rfm_total=0

#Do the needful for each CID in the auth file
for key, value in cids.items():
    print(value)
    falcon = APIHarness(client_id=clientid, client_secret=clientsec,member_cid=key)
    response = falcon.command("QueryDevicesByFilter",filter=filter)
    if response['body']['resources'] is not None:
        total = response["body"]["meta"]["pagination"]["total"]
        print(total)
        rfm_total += total
        off = 0
        while total >0:
            response = falcon.command("QueryDevicesByFilter",
                        offset=off,
                        limit=500,
                        sort="device_id.asc",
                        filter=filter
                        )
            aids = response["body"]["resources"]
            hosts = falcon.command("GetDeviceDetails", ids=aids)["body"]["resources"]
            if hosts is not None:
                for info in hosts:
                    hostname = (info["hostname"])
                    aid = (info["device_id"])
                    last_seen = (info["last_seen"])
                    rfm = (info["reduced_functionality_mode"])
                    os_version = (info["os_version"])
                    kernel = (info["kernel_version"])
                    tags = (info["tags"])
                    agent_version = (info["agent_version"])
                    tag = ""   
                    for t in tags:
                        tag += t.replace('SensorGroupingTags/','')
                        tag += ","
                    file_object.write(key+","+hostname+","+aid+","+last_seen+","+rfm+","+os_version+","+kernel+","+agent_version+","+tag+"\n")
            total -= 500
            off += 500
                     
file_object.close()
print("Total host count in RFM: ",rfm_total)