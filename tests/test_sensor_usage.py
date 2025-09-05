# test_sensor_usage.py
# This class tests the sensor usage service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import SensorUsage

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = SensorUsage(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 404, 429]


class TestSensorUsage:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetWeeklySensorUsage": falcon.get_weekly_usage(),
            "GetHourlySensorUsage": falcon.get_hourly_usage()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
