# test_cloud_oci_registration.py
# This class tests the cloud_oci_registration service class

# import json
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CloudOCIRegistration

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudOCIRegistration(auth_object=config)
AllowedResponses = [200, 201, 204, 207, 400, 403, 429]


class TestCloudOCIRegistration:
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "cloud_security_registration_oci_get_account": falcon.get_account(limit=1),
            "cloud_security_registration_oci_rotate_key": falcon.rotate_key(tenancy_ocid="12345678"),
            "cloud_security_registration_oci_validate_tenancy": falcon.validate_tenancy(tenancy_ocid="12345678"),
            "cloud_security_registration_oci_validate_tenancy2": falcon.validate_tenancy(products={"features": "bananas"}),
            "cloud_security_registration_oci_create_account": falcon.create_account(tenancy_ocid="12345678", user_name="bob"),
            "cloud_security_registration_oci_create_account": falcon.create_account(tenancy_ocid="12345678", user_name="bob", products={"features": "apples"}),
            "cloud_security_registration_oci_update_account": falcon.update_account(tenancy_ocid="12345678", user_name="larry"),
            "cloud_security_registration_oci_delete_account": falcon.delete_account(tenancy_ocid="12345678"),
            "cloud_security_registration_oci_download_script": falcon.download_script(tenancy_ocid="12345678"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
