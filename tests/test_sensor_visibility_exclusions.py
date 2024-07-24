# test_sensor_visibility_exclusions.py
# This class tests the sensor_visibility_exclusions service class
import os
import sys
import pytest
# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import SensorVisibilityExclusions

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = SensorVisibilityExclusions(auth_object=config)
AllowedResponses = [200, 400, 401, 404, 429]


class TestSVExclusions:
    def sve_list_exclusions(self):
        returned = False
        exclusions = falcon.querySensorVisibilityExclusionsV1(limit=1, offset=2, pizza="IsDelicious")
        if exclusions["status_code"] in AllowedResponses:
            returned = True
        elif exclusions["status_code"] == 500:
            pytest.skip("API communication failure")
        return returned

    def sve_test_all_paths(self):
        error_checks = True
        tests = {
            "get_sv_exclusions": falcon.get_exclusions(ids="12345678"),
            "create_exclusion": falcon.create_exclusions(body={}),
           "create_exclusion_too": falcon.create_exclusions(comment="Unit Testing",
                                                            groups=["1234578"],
                                                            value="Charlie"
                                                            ),
           "update_exclusion": falcon.update_exclusions(body={"id": "12345678"}),
           "update_exclusion_also": falcon.update_exclusions(comment="Unit Testing",
                                                             groups=["12345678"],
                                                             id="12345678",
                                                             value="Bananas"
                                                             ),
           "delete_exclusion": falcon.delete_exclusions(ids="12345678"),
        }
        for key in tests:
            if tests[key]["status_code"] == 500:
                error_checks = False

        return error_checks

    def test_find(self):
        assert self.sve_list_exclusions() is True

    def test_all_functionality(self):
        assert self.sve_test_all_paths() is True
