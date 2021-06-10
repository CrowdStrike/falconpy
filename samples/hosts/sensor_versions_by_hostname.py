"""
This sample demonstrates retrieving sensor versions by hostname
"""
# pylint: disable=C0103,W0621,E0401
import json
from falconpy.hosts import Hosts


def device_list(offset: int, limit: int):
    """
    I return a list of all devices for the CID, if I max out on the query limit, I can paginate
    """
    result = falcon.QueryDevicesByFilter(parameters={"limit": limit, "offset": offset})
    new_offset = result["body"]["meta"]["pagination"]["offset"]
    total = result["body"]["meta"]["pagination"]["total"]
    device_list = result["body"]["resources"]
    return new_offset, total, device_list


def device_detail(aids: list):
    """
    I return the device_id and agent_version for a list of AIDs I'm provided
    """
    result = falcon.GetDeviceDetails(ids=aids)
    devices = []
    # return just the aid and agent version
    for device in result["body"]["resources"]:
        res = {}
        res["hostname"] = device["hostname"]
        res["agent_version"] = device["agent_version"]
        devices.append(res)
    return devices


# Grab our config parameters from a local file.
with open('../config.json', 'r') as file_config:
    config = json.loads(file_config.read())

falcon = Hosts(creds={
        "client_id": config["falcon_client_id"],
        "client_secret": config["falcon_client_secret"]
    },
    # base_url = "https://YOUR_BASE_URL.crowdstrike.com"   # Enter your base URL here if it is not US-1
)

offset = 0      # Start at the beginning
displayed = 0   # This is just so we can show a running count
total = 1       # Assume there is at least one
limit = 500     # Quick limit to prove pagination
while offset < total:
    offset, total, devices = device_list(offset, limit)
    details = device_detail(devices)
    for detail in details:
        displayed += 1
        print(f"{displayed}: {detail['hostname']} is on version {detail['agent_version']}")
