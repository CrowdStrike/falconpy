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


def connect_api(class_type: str = "service"):
    """Connect to the selected API service."""
    with open("../config.json", "r", encoding="utf-8") as cred_file:
        config = json.loads(cred_file.read())

    if class_type.lower() == "service":
        falcon_api = IOC(client_id=config["falcon_client_id"],
                         client_secret=config["falcon_client_secret"]
                         )
    elif class_type.lower() == "uber":
        falcon_api = APIHarness(client_id=config["falcon_client_id"],
                                client_secret=config["falcon_client_secret"]
                                )
    else:
        falcon_api = None

    return falcon_api


# Create an IOC using the IOC Service class
falcon = connect_api("service")
# Since we are using a version greater than 0.7.3,
# we are able to make use of Body Payload abstraction
response = falcon.indicator_create(source="Test",
                                   action="detect",
                                   expiration="2021-12-05T05:00:00.000Z",
                                   description="Testing",
                                   type="ipv4",
                                   value="8.7.6.53",
                                   severity="LOW",
                                   applied_globally=True,
                                   platforms="linux"  # Can be a list or a comma-delimited string.
                                   )
print(response)

# Create an IOC using the Uber class
falcon = connect_api("uber")
# The Uber class does not support Body Payload abstraction.
# We will send it a standard body payload instead.
BODY = {
    "indicators": [
        {
            "source": "Test",
            "action": "detect",
            "expiration": "2021-12-05T05:00:00.000Z",
            "description": "Testing",
            "type": "ipv4",
            "value": "4.1.2.33",
            "platforms": ["linux"],
            "severity": "LOW",
            "applied_globally": True
        }
    ]
}
response = falcon.command('indicator_create_v1', body=BODY)
print(response)
