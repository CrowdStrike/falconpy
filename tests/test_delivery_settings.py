# test_delivery settings.py
# This class tests the delivery settings service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import DeliverySettings

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = DeliverySettings(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 429]

class TestDeliverySettings:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetDeliverySettings": falcon.get_delivery_settings(),
            "PostDeliverySettings": falcon.create_delivery_settings(delivery_cadence="general_availability", delivery_type="sensor_operations")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
