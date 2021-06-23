"""
 ___  _______  _______
|   ||   _   ||   _   |
|.  ||.  |   ||.  1___|
|.  ||.  |   ||.  |___
|:  ||:  1   ||:  1   |
|::.||::.. . ||::.. . |
`---'`-------'`-------'

Create IOC Example - @jshcodes 06.23.21

FalconPy v.0.5.0+ only, uses the new IOC endpoint
"""
import json
from falconpy.api_complete import APIHarness as Uber
from falconpy.ioc import IOC as IOC


def connectAPI(class_type: str = "service"):
    with open("../config.json", "r") as cred_file:
        config = json.loads(cred_file.read())
    creds = {
        "client_id": config["falcon_client_id"],
        "client_secret": config["falcon_client_secret"]
    }
    if class_type.lower() == "service":
        falcon = IOC(creds=creds)
    elif class_type.lower() == "uber":
        falcon = Uber(creds=creds)
    else:
        falcon = None

    return falcon


def createIOCPayload(source: str, policy: str, expiration: int, desc: str, type: str, val: str, platforms: list):
    payload = {
        "indicators": [
            {
                "source": source,
                "policy": policy,
                "expiration_days": expiration,
                "description": desc,
                "type": type,
                "value": val,
                "platforms": platforms,
                "applied_globally": True
            }
        ]
    }
    return payload


# Create an IOC using the IOC Service class
falcon = connectAPI("service")
BODY = createIOCPayload("Test", "detect", 1, "Testing", "ipv4", "9.8.7.6", ["Linux"])
response = falcon.indicator_create_v1(body=BODY)
print(response)

# Create an IOC using the Uber class
falcon = connectAPI("uber")
BODY = createIOCPayload("Test", "detect", 1, "Testing", "ipv4", "8.7.6.5", ["Linux"])
response = falcon.command('indicator_create_v1', body=BODY)
print(response)
