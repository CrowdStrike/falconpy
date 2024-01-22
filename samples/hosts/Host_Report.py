#!/usr/bin/env python3
#Please establish an "auth.py" file in the same directory as this script with the "clientid" and "clientsec" variables defined.
#This script was intended to replace the manual daily export of hosts from the Falcon Console that was required to audit host compliance. It was developed to be run as a recurring job and will output a CSV with all hosts in the CID along with other required info that can than be imported into a compliance dashboard or tool.
#Developed by Don-Swanson-Adobe

####REPLACE THE FOLLOWING EXAMPLE VARIABLES####
outpath = './Hosts_output.csv'
#Note: './' is 1 directory up from current, '../' is 2 directories up
###############################################

#Import FalconPy and capture start time
from falconpy import APIHarness
from datetime import datetime
from auth import *
startTime = datetime.now()

#Setup Outfile
file_object = open(outpath, 'a+')
file_object.write("Hostname,Last Seen,First Seen,Platform,OS Version,OS Build,OS Product Name,Kernel Version,Model,Manufacturer,Type,Chassis,Last Reboot,Prevention Policy,Response Policy,Sensor Update Policy,USB Device Policy,Host ID,MAC Address,Connection MAC Address,Status,CPUID,Serial Number,Sensor Version,Sensor Tags\n")

#Function to get detail from the detail_response
def get_detail(detail, filter):
    if filter in detail:
        return detail[filter]
    else:
        return "Not Found"

#Login and run this puppy!
############################################################################################################################################################
falcon = APIHarness(client_id=clientid, client_secret=clientsec)
offset = ''
response = falcon.command("QueryDevicesByFilterScroll")
total = response["body"]["meta"]["pagination"]["total"]

while total > 0:
    response = falcon.command("QueryDevicesByFilterScroll", offset=offset, limit=5000)
    print("Total Remaining: ",total)
    total = total - 5000
    offset = response["body"]["meta"]["pagination"]["offset"]
    detail_response = falcon.command("GetDeviceDetails", ids=response["body"]["resources"])
    for detail in detail_response["body"]["resources"]:
        hostname = get_detail(detail, "hostname")
        last_seen = get_detail(detail, "last_seen")
        first_seen = get_detail(detail, "first_seen")
        platform = get_detail(detail, "platform_name")
        os_version = get_detail(detail, "os_version")
        os_build = get_detail(detail, "os_build")
        os_product_name = get_detail(detail, "os_product_name")
        kernel_version = get_detail(detail, "kernel_version")
        model = get_detail(detail, "system_product_name").replace(",", " ")
        manufacturer = get_detail(detail, "system_manufacturer").replace(",", " ")
        type = get_detail(detail, "product_type_desc")
        chassis = get_detail(detail, "chassis_type_desc")
        last_reboot = get_detail(detail, "last_reboot")
        if "device_policies" in detail:
            prevention_policy = detail['device_policies']['prevention']['policy_id']
            response_policy = detail['device_policies']['remote_response']['policy_id']
            sensor_update_policy = detail['device_policies']['sensor_update']['policy_id']
            if "usb_storage_control" in detail['device_policies']:
                usb_device_policy = detail['device_policies']['usb_storage_control']['policy_id']
            else:
                usb_device_policy = "Not Found"
        else:
            prevention_policy = "Not Found"
            response_policy = "Not Found"
            sensor_update_policy = "Not Found"
            usb_device_policy = "Not Found"
        host_id = get_detail(detail, "device_id")
        mac_address = get_detail(detail, "mac_address")
        connection_mac_address = get_detail(detail, "connection_mac_address")
        status = get_detail(detail, "status")
        cpuid = get_detail(detail, "cpu_signature")
        serial_number = get_detail(detail, "serial_number")
        sensor_version = get_detail(detail, "agent_version")
        sensor_tags = (str(get_detail(detail, "tags")).replace(",", ";"))

        file_object.write(hostname+","+last_seen+","+first_seen+","+platform+","+os_version+","+os_build+","+os_product_name+","+kernel_version+","+model+","+manufacturer+","+type+","+chassis+","+last_reboot+","+prevention_policy+","+response_policy+","+sensor_update_policy+","+usb_device_policy+","+host_id+","+mac_address+","+connection_mac_address+","+status+","+cpuid+","+serial_number+","+sensor_version+","+sensor_tags+"\n")

file_object.close()
print("Done")
print("Time to complete: ",datetime.now() - startTime)