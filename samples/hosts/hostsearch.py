#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script is intended to take a file listing hostnames and output a CSV with the with host details if found. It was developed with the intention to be used to compare a list of hostnames to the list of hosts in the Falcon Console to determine which hostnames are not currently reporting to the console.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
inpath = '../hostnames.txt' #Note, hostnames should be separated by a new line#
outpath = '../output.csv'
#Note: './' is 1 directory up from current, '../' is 2 directories up
###############################################

#Import API Harness and Auth File
from auth import *
from falconpy import Hosts
import csv

#Function to compare lists
def Diff(source,found):
    s = set(found)
    li_dif = [x for x in source if x not in s]
    return li_dif

#Pull info for report
print("Opening "+inpath)
hostnames = []
with open(inpath, newline='') as f:
    for row in csv.reader(f):
        hostnames.append(row[0])

#Setup variables and output file
SORT = "hostname.asc"
file_object = open(outpath, 'a+')
file_object.write("Hostname,CID,RFM,Last Seen,Landscape,Tag1,Tag2,Tag3,Tag4\n")
found = []

#Setup API Harness
falcon = Hosts(client_id=clientid,client_secret=clientsec)

for i in hostnames:     
    # Get AID for matching hosts
    host_ids = falcon.query_devices_by_filter(filter=f"hostname:'{i}'")
    
    # Get and write details for those hosts. 
    devices = falcon.get_device_details(ids=host_ids["body"]["resources"])["body"]["resources"]
    if devices is not None: 
        for device in devices:
            if len(device):
                hostname = (device["hostname"])
                last_seen = (device["last_seen"])
                rfm = (device["reduced_functionality_mode"])
                cid = (device["cid"])
                tags = (device["tags"])
                tag = ""
                for i in tags:
                    tag += i.replace('SensorGroupingTags/','')
                    tag += ","
                file_object.write(hostname+","+cid+","+rfm+","+last_seen+","+tag+"\n")
                found.append(hostname)

#Compare to original list
print("Determining Hosts Not Found")
not_found = (Diff(hostnames,found))
for host in not_found:
    #print(host+",HOST NOT FOUND\n")
    file_object.write(host+",HOST NOT FOUND\n")

file_object.close()