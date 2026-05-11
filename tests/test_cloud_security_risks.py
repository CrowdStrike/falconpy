# test_cloud_security_risks.py
# This class tests the cloud_security_risks service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import CloudSecurityRisks

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudSecurityRisks(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestCloudSecurityRisks:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "cloud_security_timeline_risks_enriched": falcon.cloud_security_timeline_risks_enriched(id="12345678"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
