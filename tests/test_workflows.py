"""
test_workflows.py - This class tests the Workflows service class
"""
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Workflows

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Workflows(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]  # Temp allow 403


class TestWorkflows:
    def run_all_tests(self):
        error_checks = True
        tests = {
            "WorkflowExecute" : falcon.execute(body={}),
            "WorkflowExecutionsAction" : falcon.execution_action(action_name="resume", ids="12345678"),
            "WorkflowExecutionResults" : falcon.execution_results(ids="12345678"),
            "WorkflowSystemDefinitionsDeProvision" : falcon.deprovision(definition_id="12345", deprovision_all=True),
            "WorkflowSystemDefinitionsPromote" : falcon.promote(customer_definition_id="12345", activities={}),
            "WorkflowSystemDefinitionsProvision" : falcon.provision(name="FalconPyTesting", configuration=[{}]),

        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
            #     print(tests[key])

        return error_checks

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_functionality(self):
        assert self.run_all_tests() is True
