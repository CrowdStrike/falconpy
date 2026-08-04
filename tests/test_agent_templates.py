# test_agent_templates.py
# This class tests the agent_templates service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import AgentTemplates

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = AgentTemplates(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestAgentTemplates:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesAgentTemplatesV1": falcon.entities_agent_templates_v1(ids="12345678"),
            "QueriesAgentTemplatesV1": falcon.queries_agent_templates_v1(offset=1, limit=1, filter="string", sort="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
