# test_serverless_vulnerabilities.py
# This class tests the serverless_vulnerabilities service class

# import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ServerlessVulnerabilities

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ServerlessVulnerabilities(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 429]


class TestServerlessVulnerabilities:
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetCombinedVulnerabilitiesSARIF": falcon.get_vulnerabilities(limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
