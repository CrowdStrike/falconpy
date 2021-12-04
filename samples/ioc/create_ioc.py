"""
 ___  _______  _______
|   ||   _   ||   _   |
|.  ||.  |   ||.  1___|
|.  ||.  |   ||.  |___
|:  ||:  1   ||:  1   |
|::.||::.. . ||::.. . |
`---'`-------'`-------'

Create IOC Example - @jshcodes 06.23.21

FalconPy v.0.8.6+
"""
import json
from falconpy import APIHarness, IOC


def connectAPI(class_type: str = "service"):
    """Connect to the selected API service."""
    with open("../config.json", "r", encoding="utf-8") as cred_file:
        config = json.loads(cred_file.read())

    if class_type.lower() == "service":
        falcon = IOC(client_id=config["falcon_client_id"],
                     client_secret=config["falcon_client_secret"]
                     )
    elif class_type.lower() == "uber":
        falcon = APIHarness(client_id=config["falcon_client_id"],
                            client_secret=config["falcon_client_secret"]
                            )
    else:
        falcon = None

    return falcon


def createIOCPayload(source: str,
                     action: str,
                     expiration: str,
                     desc: str,
                     type: str,
                     val: str,
                     platforms: list,
                     severity: str
                     ) -> dict:
    payload = {
        "indicators": [
            {
                "source": source,
                "action": action,
                "expiration": expiration,
                "description": desc,
                "type": type,
                "value": val,
                "platforms": platforms,
                "severity": severity,
                "applied_globally": True
            }
        ]
    }
    return payload


# Create an IOC using the IOC Service class
falcon = connectAPI("service")
# Since we are using a version greater than 0.7.3, we are able to make use of Body Payload abstraction
response = falcon.indicator_create(source="Test",
                                   action="detect",
                                   expiration="2021-12-05T05:00:00.000Z",
                                   description="Testing",
                                   type="ipv4",
                                   value="8.7.6.5",
                                   severity="LOW",
                                   applied_globally=True,
                                   platforms="linux"    # Can be a list or a comma-delimited string. This is a list of 1.
                                   )
print(response)

# Create an IOC using the Uber class
falcon = connectAPI("uber")
# The Uber class does not support Body Payload abstraction. We will send it a standard body payload instead.
BODY = createIOCPayload("Test", "detect", "2021-12-05T05:00:00.000Z", "Testing", "ipv4", "3.4.5.6", ["linux"], "LOW")
response = falcon.command('indicator_create_v1', body=BODY)
print(response)
