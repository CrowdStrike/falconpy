#!/usr/bin/env python3
r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

 _    _   ______   ______  _______  ______
| |  | | / |  | \ / |        | |   / |
| |--| | | |  | | '------.   | |   '------.
|_|  |_| \_|__|_/  ____|_/   |_|    ____|_/

 ______   ______  ______   ______   ______  _______
| |  | \ | |     | |  | \ / |  | \ | |  | \   | |
| |__| | | |---- | |__|_/ | |  | | | |__| |   | |
|_|  \_\ |_|____ |_|      \_|__|_/ |_|  \_\   |_|

This script was developed by @Don-Swanson-Adobe and is intended to
replace the manual daily export of hosts from the Falcon Console that
was required to audit host compliance. It was developed to be run as
a recurring job and will output a CSV with all hosts in the CID along
with other required info that can then be imported into a compliance
dashboard or tool.

Developed by @Don-Swanson-Adobe
"""
import os
import logging
from datetime import datetime
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from falconpy import APIHarnessV2

#Function to get detail from the detail_response
def get_detail(detail, filter):
    if filter in detail:
        return detail[filter]
    else:
        return "Not Found"


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-o", "--output_path",
                        help="Location to store CSV output",
                        default="Hosts_output.csv"
                        )
    req = parser.add_argument_group("Required arguments")
    req.add_argument("-k", "--client_id",
                     help="CrowdStrike Falcon API key",
                     default=os.getenv("FALCON_CLIENT_ID")
                     )
    req.add_argument("-s", "--client_secret",
                     help="CrowdStrike Falcon API secret",
                     default=os.getenv("FALCON_CLIENT_SECRET")
                     )
    parsed = parser.parse_args()
    if not parsed.client_id or not parsed.client_secret:
        parser.error("You must provide CrowdStrike API credentials using the '-k' and '-s' arguments.")

    return parsed


#Login and run this puppy!
startTime = datetime.now()
cmd_line = consume_arguments()
if cmd_line.debug:
    logging.basicConfig(level=logging.DEBUG)
falcon = APIHarnessV2(client_id=cmd_line.client_id,
                      client_secret=cmd_line.client_secret,
                      debug=cmd_line.debug
                      )
#Setup Outfile
file_object = open(cmd_line.output_path, 'a+')
file_object.write("Hostname,Last Seen,First Seen,Platform,OS Version,OS Build,OS Product Name,Kernel Version,Model,Manufacturer,Type,Chassis,Last Reboot,Prevention Policy,Response Policy,Sensor Update Policy,USB Device Policy,Host ID,MAC Address,Connection MAC Address,Status,CPUID,Serial Number,Sensor Version,Sensor Tags\n")
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