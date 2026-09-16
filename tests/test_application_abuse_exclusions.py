# test_application_abuse_exclusions.py
# This class tests the application_abuse_exclusions service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import ApplicationAbuseExclusions

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ApplicationAbuseExclusions(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestApplicationAbuseExclusions:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "app_abuse_exclusions_aggregates_v1": falcon.aggregate_app_abuse_exclusions(date_ranges=[{"from": "string", "to": "string"}],
                                                                                        field="string", filter="string",
                                                                                        interval="string", min_doc_count=0,
                                                                                        missing="string", name="string",
                                                                                        q="string",
                                                                                        ranges=[{"From": 0, "To": 0}], size=0,
                                                                                        sort="string",
                                                                                        sub_aggregates=["string"],
                                                                                        time_zone="string", type="string"),
            "app_abuse_exclusions_report_v1": falcon.create_app_abuse_report(report_format="string", filter="string",
                                                                             sort="string"),
            "app_abuse_exclusions_get_v1": falcon.get_app_abuse_exclusions(ids="12345678"),
            "app_abuse_exclusions_create_v1": falcon.create_app_abuse_exclusion(exclusions="string"),
            "app_abuse_exclusions_delete_v1": falcon.delete_app_abuse_exclusions(ids=["string"], comment="string"),
            "app_abuse_exclusions_update_v1": falcon.update_app_abuse_exclusions(exclusions="string"),
            "app_abuse_exclusions_get_apps_by_category_v1": falcon.get_app_abuse_apps_by_category(category="string",
                                                                                                  show_available_only=True),
            "app_abuse_exclusions_get_categories_v1": falcon.get_app_abuse_categories(),
            "app_abuse_exclusions_query_v1": falcon.query_app_abuse_exclusions(filter="string", offset=1, limit=1,
                                                                               sort="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks

    def test_payload_coverage(self):
        """Exercise nested payload builder branches."""
        falcon.create_app_abuse_report(filter="string", sort="string")
        assert True
