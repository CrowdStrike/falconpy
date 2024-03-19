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
AllowedResponses = [200, 201, 400, 403, 404, 415, 500]  # Allowing 415 due to workflow import


class TestWorkflows:
    def run_all_tests(self):
        error_checks = True
        tests = {
            "WorkflowExecute" : falcon.execute(body={}),
            "WorkflowExecuteInternal" : falcon.execute_internal(body={}),
            "WorkflowMockExecute" : falcon.mock_execute(body={}, mocks="whatever"),
            "WorkflowExecutionsAction" : falcon.execution_action(action_name="resume", ids="12345678"),
            "WorkflowExecutionResults" : falcon.execution_results(ids="12345678"),
            "WorkflowSystemDefinitionsDeProvision" : falcon.deprovision(definition_id="12345", deprovision_all=True),
            "WorkflowSystemDefinitionsPromote" : falcon.promote(customer_definition_id="12345", activities={}),
            "WorkflowSystemDefinitionsProvision" : falcon.provision(name="FalconPyTesting", configuration=[{}]),
            "WorkflowDefinitionsCombined": falcon.search_definitions(),
            "WorkflowExecutionsCombined": falcon.search_executions(),
            "WorkflowDefinitionsExport": falcon.export_definition(),
            "WorkflowDefinitionsImport": falcon.import_definition(validate_only=True, data_file="this_will_415"),
            "WorkflowDefinitionsImport": falcon.import_definition(validate_only=True, file_data="this_will_500"),
            "WorkflowDefinitionsUpdate": falcon.update_definition(change_log="testing"),
            "WorkflowGetHumanInputV1": falcon.get_human_input(ids="1234567"),
            "WorkflowUpdateHumanInputV1": falcon.update_human_input(input="whatever", note="whatever"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])

        return error_checks

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_functionality(self):
        assert self.run_all_tests() is True
