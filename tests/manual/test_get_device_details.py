"""test_get_device_details.py

This class tests the different operations available for retrieve device details.
"""
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Hosts, APIHarness

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Hosts(auth_object=config)
uber = APIHarness(client_id=falcon.auth_object.creds["client_id"],
                  client_secret=falcon.auth_object.creds["client_secret"],
                  base_url=falcon.auth_object.base_url
                  )
AllowedResponses = [200, 201, 429]

DEVICE_ID = "Not set"

class TestGetDeviceDetails:
    def get_a_device_id(self):
        global DEVICE_ID
        device_id = bool(DEVICE_ID != "Not set")
        if not device_id:
            device_id_query = falcon.query_devices(limit=1)
            if device_id_query["status_code"] == 200:
                if "resources" in device_id_query["body"]:
                    if device_id_query["body"]["resources"]:
                        DEVICE_ID = device_id_query["body"]["resources"][0]
                        device_id = True
        return device_id

    def valid_status_code(self, result):
        return bool(result["status_code"] in AllowedResponses)

    def legacy_opid_syntax(self):
        """Test the legacy GetDeviceDetails operation using the new Operation ID alias."""
        returned = False
        if self.get_a_device_id():
            if self.valid_status_code(falcon.GetDeviceDetailsV1(ids=DEVICE_ID)):
                returned = True
        return returned

    def new_opid_syntax(self):
        """Test the new GetDeviceDetailsV2 operation using the Operation ID alias."""
        returned = False
        if self.get_a_device_id():
            if self.valid_status_code(falcon.GetDeviceDetailsV2(ids=DEVICE_ID)):
                returned = True
        return returned

    def legacy_pep_syntax(self):
        """Test the legacy GetDeviceDetails operation using PEP 8 syntax."""
        returned = False
        if self.get_a_device_id():
            if self.valid_status_code(falcon.get_device_details_v1(DEVICE_ID)):
                returned = True
        return returned

    def new_pep_syntax(self):
        """Test the new GetDeviceDetailsV2 operation using PEP 8 syntax."""
        returned = False
        if self.get_a_device_id():
            if self.valid_status_code(falcon.get_device_details_v2(ids=DEVICE_ID)):
                returned = True
        return returned

    def alias_pep_syntax(self):
        """Test the new PostDeviceDetailsV2 operation using PEP 8 syntax."""
        returned = False
        if self.get_a_device_id():
            if self.valid_status_code(falcon.post_device_details_v2(ids=DEVICE_ID)):
                returned = True
        return returned

    def redirected_pep_syntax(self):
        """Tests PEP 8 syntax variations using the newly redirected method."""
        returned = self.get_a_device_id()
        if returned:
            if not self.valid_status_code(falcon.get_device_details(DEVICE_ID)):
                returned = False
            if not self.valid_status_code(falcon.get_device_details(ids=DEVICE_ID)):
                returned = False
            if not self.valid_status_code(falcon.get_device_details(parameters={"ids": [DEVICE_ID]})):
                returned = False
            if not self.valid_status_code(falcon.get_device_details(body={"ids": [DEVICE_ID]})):
                returned = False
        return returned

    def redirected_opid_syntax(self):
        """Tests Operation ID syntax variations using the newly redirected method."""
        returned = self.get_a_device_id()
        if returned:
            if not self.valid_status_code(falcon.GetDeviceDetails(DEVICE_ID)):
                returned = False
            if not self.valid_status_code(falcon.GetDeviceDetails(ids=DEVICE_ID)):
                returned = False
            if not self.valid_status_code(falcon.GetDeviceDetails(parameters={"ids": [DEVICE_ID]})):
                returned = False
            if not self.valid_status_code(falcon.GetDeviceDetails(body={"ids": [DEVICE_ID]})):
                returned = False
        return returned

    def uber_syntax(self):
        """Tests legacy Uber class syntax to redirected operation ID."""
        returned = self.get_a_device_id()
        if returned:
            if not self.valid_status_code(uber.command("GetDeviceDetails", ids=DEVICE_ID)):
                returned = False
            if not self.valid_status_code(uber.command("GetDeviceDetails", body={"ids": [DEVICE_ID]})):
                returned = False
            if not self.valid_status_code(uber.command("GetDeviceDetails", body={"ids": DEVICE_ID})):
                returned = False
            if not self.valid_status_code(uber.command("GetDeviceDetails", parameters={"ids": DEVICE_ID})):
                returned = False
            if not self.valid_status_code(uber.command("GetDeviceDetailsV1", ids=DEVICE_ID)):
                returned = False
            if not self.valid_status_code(uber.command("GetDeviceDetailsV2", ids=DEVICE_ID)):
                returned = False
            if not self.valid_status_code(uber.command("PostDeviceDetailsV2", body={"ids": [DEVICE_ID]})):
                returned = False
            if not self.valid_status_code(uber.command("PostDeviceDetailsV2", parameters={"ids": [DEVICE_ID]})):
                returned = False
            if not self.valid_status_code(uber.command("PostDeviceDetailsV2", ids=DEVICE_ID)):
                returned = False
            if not self.valid_status_code(uber.command("PostDeviceDetailsV2", ids=[DEVICE_ID])):
                returned = False

        return returned

    def test_legacy_opid_syntax(self):
        """Pytest harness hook."""
        assert self.legacy_opid_syntax() is True

    def test_new_opid_syntax(self):
        """Pytest harness hook."""
        assert self.new_opid_syntax() is True

    def test_legacy_pep_syntax(self):
        """Pytest harness hook."""
        assert self.legacy_pep_syntax() is True

    def test_new_pep_syntax(self):
        """Pytest harness hook."""
        assert self.new_pep_syntax() is True

    def test_alias_pep_syntax(self):
        """Pytest harness hook."""
        assert self.alias_pep_syntax() is True

    def test_redirected_opid_syntax(self):
        """Pytest harness hook."""
        assert self.redirected_opid_syntax() is True

    def test_redirected_pep_syntax(self):
        """Pytest harness hook."""
        assert self.redirected_pep_syntax() is True

    def test_uber_syntax(self):
        """Pytest harness hook."""
        assert self.uber_syntax() is True
