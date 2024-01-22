#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#Born out of need to provide the support team a PCAP WHILE restarting the sensor, This script is designed to setup an RTR Session, put a script on the host (That also happens to stop and start the sensor), run that script, then finally retrieve the output.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
cid = "EXAMPLE_CID" #If you are not using a multi-tenant environment, this and the "member_cid" variable on line 19 can be removed 
aid = "EXAMPLE_AID"
script = "./remote_tcp_dump.sh"
#Note: './' is 1 directory up from current, '../' is 2 directories up
###############################################

#Import API Harness and Auth File and some additional modules
from auth import *
from time import sleep
from falconpy import APIHarness

#Setup the API Harness
falcon = APIHarness(client_id=clientid,client_secret=clientsec, member_cid=cid) #Member CID should not be used in non-multi-tenant environments

#Initiate the Session
BODY = {"device_id": aid, "queue_offline": True}
session = falcon.command("RTR_InitSession", body=BODY)["body"]["resources"][0]["session_id"]
print("Session ID: "+session)

#"PUT" the File
BODY = {"base_command": "put", "command_string": "put "+script, "persist": True,  "session_id": session}
response = falcon.command("RTR_ExecuteAdminCommand", body=BODY)
if response["status_code"] != 201:
    print("Error: File not uploaded")
    exit()
sleep(5)

#Chmod the File
BODY = {"base_command": "runscript", "command_string": "runscript -Raw=```chmod +x ./"+script+"```", "persist": True,  "session_id": session}
response = falcon.command("RTR_ExecuteAdminCommand", body=BODY)
if response["status_code"] != 201:
    print("Error: Not Chomd'd")
    exit()

#Run the File (We use systemd-run to ensure the script continues to run after the sensor is stopped)
BODY = {"base_command": "runscript", "command_string": "runscript -Raw=```systemd-run ./"+script+"```", "persist": True,  "session_id": session}
response = falcon.command("RTR_ExecuteAdminCommand", body=BODY)
if response["status_code"] != 201:
    print("Error: Execution Failed")
    exit()

#Wait for finish
sleep(90)

#Get the output File
BODY = {"base_command": "get", "command_string": "get tcpdump.pcap", "persist": True,  "session_id": session}
response = falcon.command("RTR_ExecuteAdminCommand", body=BODY)
if response["status_code"] != 201:
    print("Error: Get Failed")
    exit()


#######################################
#Example of the remote_tcp_dump.sh script
##!/bin/bash
##This script can be re-purposed to run any command on the endpoint via RTR while restarting the sensor. 
##create a variable with the hostname
#hostname=$(hostname)
#
##run tcpdump for 60 seconds and save the file with the hostname
#echo "Starting capture"
#tcpdump -G 60 -W 1 -w tcpdump-$hostname.pcap &
#sleep 10
#
## Stopping the Falcon Sensor
#systemctl stop falcon-sensor
#sleep 5
#
## Starting the Falcon Sensor
#systemctl start falcon-sensor
#sleep 45
#
##print that the script is done
#echo "Capture Complete!"