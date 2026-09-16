# test_audit.py
# This class tests the audit service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import Audit

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Audit(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestAudit:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "ExportQueryResults": falcon.export_audit_query_results(id="string", format="string", include_descriptions=True,
                                                                    include_extension_metadata=True),
            "GetQueryResults": falcon.get_audit_query_results(id="string", offset=1, limit=1, include_descriptions=True,
                                                              include_extension_metadata=True),
            "PollQueryJobStatus": falcon.poll_audit_query_status(id="12345678"),
            "CreateQueryJob": falcon.create_audit_query_job(action="string", action_description="string", actor_id="string",
                                                            actor_ip="string", actor_type="string", category="string",
                                                            category_description="string", cid="string", end_time="string",
                                                            event_id="string", event_version="string", extensions="string",
                                                            geo_city="string", geo_country="string", sort="string",
                                                            start_time="string", target_display_name="string",
                                                            target_id="string", target_type="string", user_agent="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
