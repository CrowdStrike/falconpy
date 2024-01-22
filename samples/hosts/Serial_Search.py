#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script is intended to take a file listing Serial Numbers and output a CSV with the Serial Number, Hostname, CID, RFM, Last Seen, Local IP, and Tags for each serial number. It was developed with the intention to be used to compare a list of serial numbers to the list of hosts in the Falcon Console to determine which serial numbers are not currently reporting to the console.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
inpath = './serials.txt' #Note, serials should be separated by a new line#
outpath = './output.csv' #Location of the output CSV
#Note: './' is 1 directory up from current, '../' is 2 directories up
###############################################

#Import Auth File and some additional modules
from auth import *
from falconpy import Hosts
import csv
from datetime import datetime, timedelta

#Function to determine which serial numbers couldn't be found
def Diff(source,found):
    s = set(found)
    li_dif = [x for x in source if x not in s]
    return li_dif

#Setup the current last seen time as the last 72 hours
lastseen = (datetime.utcnow() - timedelta(hours = 72)).strftime('%Y-%m-%dT%H:%M:%SZ')

#Read in the serial numbers from the sourcefile and append to the "serials" list
print("Opening "+inpath)
serials = []
with open(inpath, newline='') as f:
    for row in csv.reader(f):
        serials.append(row[0])

#Chunk the list of serials into a usable size
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


#Setup the output file, and the variable to store which serial numbers we found
SORT = "hostname.asc"
file_object = open(outpath, 'a+')
file_object.write("Serial,Hostname,CID,RFM,Last Seen,Local IP,Tag1,Tag2,Tag3,Tag4\n")
found = []

#Setup the API Harness
falcon = Hosts(client_id=clientid,client_secret=clientsec)

#Chunk the Serial numbers into groups of 250 to avoid making the API Choke
for group in chunker(serials, 250):    
    #Get AIDs for matching hosts
    host_ids = falcon.query_devices_by_filter(filter=f"serial_number:{group}")
    
    #Get and write details for those hosts. 
    devices = falcon.get_device_details(ids=host_ids["body"]["resources"])["body"]["resources"] 
    if devices is not None:
        for device in devices:
            if len(device):
                if (device["last_seen"]) >= lastseen:
                    hostname = (device["hostname"])
                    last_seen = (device["last_seen"])
                    rfm = (device["reduced_functionality_mode"])
                    cid = (device["cid"])
                    serial = (device["serial_number"])
                    if "local_ip" in device:
                        local_ip = (device["local_ip"])
                    else:
                        local_ip = "Unavailable"
                    tags = (device["tags"])
                    tag = ""
                    for i in tags:
                        tag += i.replace('SensorGroupingTags/','')
                        tag += ","
                    file_object.write(serial+","+hostname+","+cid+","+rfm+","+last_seen+","+local_ip+","+tag+"\n")
                    found.append(hostname)

#Compare to original list to determine which couldn't be found
print("Determining Hosts Not Found")
not_found = (Diff(serials,found))
for host in not_found:
    #print(host+",HOST NOT FOUND\n")
    file_object.write(host+",Serial NOT FOUND\n")

file_object.close()