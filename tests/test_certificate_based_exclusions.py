# test_certificate_based_exclusions.py
# This class tests the CertificateBasedExclusions service class

# import json
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Classes to test - manually imported from sibling folder
from falconpy import CertificateBasedExclusions
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CertificateBasedExclusions(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 404, 429, 500]


class TestCertificateBasedExclusions:
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "get_exclusions": falcon.get_exclusions(ids="1234567"),
            "create_exclusions": falcon.create_exclusions(body={}),
            "create_exclusions": falcon.create_exclusions(certificate="something", subject="science_fiction"),
            "create_exclusions": falcon.create_exclusions(comment="something", host_groups="12345678,87654321"),
            "delete_exclusions": falcon.delete_exclusions(ids="1234567"),
            "update_exclusions": falcon.update_exclusions(body={}),
            "get_certificates": falcon.get_certificates(ids="1234567"),
            "query_certificates": falcon.query_certificates()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
            #   print(key)
            #   print(tests[key])
        assert error_checks
