# test_cloud_security_registration_combined.py
# This class tests the cloud_security_registration_combined service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import CloudSecurityRegistrationCombined

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudSecurityRegistrationCombined(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestCloudSecurityRegistrationCombined:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "cloud_registration_cross_provider_get_account_aggregates": falcon.cloud_registration_cross_provider_get_account_aggregates(date_ranges=[{"from": "string", "to": "string"}],
                                                                                                                                        field="string",
                                                                                                                                        filter="string",
                                                                                                                                        interval="string",
                                                                                                                                        min_doc_count=0,
                                                                                                                                        missing="string",
                                                                                                                                        name="string",
                                                                                                                                        q="string",
                                                                                                                                        ranges=[{"From": 0, "To": 0}],
                                                                                                                                        size=0,
                                                                                                                                        sort="string",
                                                                                                                                        sub_aggregates=["string"],
                                                                                                                                        time_zone="string",
                                                                                                                                        type="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
