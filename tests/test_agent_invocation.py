# test_agent_invocation.py
# This class tests the agent_invocation service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import AgentInvocation

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = AgentInvocation(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestAgentInvocation:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "InvokePublishedAgentExternalV1": falcon.invoke_published_agent_external_v1(credit_cents_limit="string",
                                                                                        deadline_seconds="string",
                                                                                        id="string", messages="string"),
            "GetAgentInvocationV3": falcon.get_agent_invocation_v3(id="12345678"),
            "InvokeAgentVersionExternalV1": falcon.invoke_agent_version_external_v1(credit_cents_limit="string",
                                                                                    deadline_seconds="string", id="string",
                                                                                    messages="string", version_id="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
