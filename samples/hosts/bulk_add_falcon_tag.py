#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script was developed to bulk assign a Falcon Grouping Tag to a list of hosts based on their serial number
#Developed by Don-Swanson-Adobe

##### REPLACE THE FOLLOWING VALUES#####
inpath = './serials.txt' #Note, serials should be separated by a new line in the text source file#
falcon_tag = "TEST_TAG"  #The Falcon Grouping Tag to add
#Note: './' is 1 directory up from current, '../' is 2 directories up
#######################################

#Import FalconPy and auth file
from falconpy import APIHarness
from auth import *
import csv

#Open CSV and import serials
print("Opening CSV\n")
serials = []
with open(inpath, newline='') as f:
    for row in csv.reader(f):
        serials.append(row[0])

#Setup the Falcon Grouping Tag and login
fgt = "FalconGroupingTags/" + falcon_tag
falcon = APIHarness(client_id=clientid, client_secret=clientsec)

#Get AID and assign tag for each serial
print("Getting AID\n")
for i in serials:
    print("\nSerial: " + i)
    response = falcon.command("QueryDevicesByFilter",filter="serial_number:'"+i+"'")
    if len(response["body"]["resources"]):
        aid = response["body"]["resources"][0] 
        BODY = {"action": "add","device_ids": aid,"tags": [fgt]}
        response = falcon.command("UpdateDeviceTags", body=BODY)
        print(response)
    else:
        print("SERIAL NOT FOUND")
