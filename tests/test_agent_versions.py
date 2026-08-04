# test_agent_versions.py
# This class tests the agent_versions service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import AgentVersions

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = AgentVersions(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestAgentVersions:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetAgentVersionsV1": falcon.get_agent_versions_v1(ids="12345678"),
            "QueryAgentVersionsV1": falcon.query_agent_versions_v1(offset=1, limit=1, sort="string", filter="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
