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
AllowedResponses = [200, 201, 400, 403, 404, 415, 500, 502]  # Allowing 415 due to workflow import

with open("tests/test.yml", "rb") as file_data:
    binary_example = file_data.read()

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
            "WorkflowActivitesCombined": falcon.search_activities(),
            "WorkflowTriggersCombined": falcon.search_triggers(),
            "WorkflowExecutionsCombined": falcon.search_executions(),
            "WorkflowDefinitionsExport": falcon.export_definition(),
            "WorkflowDefinitionsImport": falcon.import_definition(validate_only=True, data_file="this_will_415"),
            "WorkflowDefinitionsImport2": falcon.import_definition(validate_only=True, file_data="this_will_500"),
            "WorkflowDefinitionsImport3": falcon.import_definition(validate_only=True, data_file="not_here.yml"),
            "WorkflowDefinitionsImport4": falcon.import_definition(validate_only=True, data_file="tests/test.yml", name="workflow_name"),
            "WorkflowDefinitionsImport4": falcon.import_definition(validate_only=True, data_file=binary_example, name="workflow_name"),
            "WorkflowDefinitionsUpdate": falcon.update_definition(change_log="testing"),
            "WorkflowDefinitionsAction1": falcon.workflow_definition_action(ids="1234567", action_name="enable"),
            "WorkflowDefinitionsAction2": falcon.workflow_definition_action(ids="1234567", action_name="whatever"),
            "WorkflowGetHumanInputV1": falcon.get_human_input(ids="1234567"),
            "WorkflowUpdateHumanInputV1": falcon.update_human_input(input="whatever", note="whatever"),
            "WorkflowActivitiesContentCombined": falcon.search_activities_content(limit=1)
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
