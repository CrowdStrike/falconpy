# test_aspm.py
# This class tests the drift indicators service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ASPM

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ASPM(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429, 500, 503]


class TestASPM:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "UpsertBusinessApplications": falcon.update_business_applications(name="something", persistent_signatures=["sig"]),
            "GetExecutorNodes": falcon.get_executor_nodes(node_type="green"),
            "UpdateExecutorNode": falcon.update_executor_node(additional_header="thing"),
            "CreateExecutorNode": falcon.create_executor_node(additional_header="thing", use_jobs=False),
            "DeleteExecutorNode": falcon.delete_node(id=42),
            "DeleteExecutorNodeFail": falcon.delete_node(),
            "GetIntegrationTasks": falcon.get_integration_tasks(category="something"),
            "CreateIntegrationTask": falcon.create_integration_task(integration_task={"something": "different"}),
            "UpdateIntegrationTask": falcon.update_integration_task(id=42, integration_task={"something": "else"}),
            "DeleteIntegrationTask": falcon.delete_integration_task(id=42),
            "RunIntegrationTask": falcon.run_integration_task(id=42, task_id=42),
            "UpdateIntegrationTaskFail": falcon.update_integration_task(),
            "DeleteIntegrationTaskFail": falcon.delete_integration_task(),
            "RunIntegrationTaskFail": falcon.run_integration_task(),
            "GetIntegrations": falcon.get_integrations(integration_type="something"),
            "GetIntegrationTypes": falcon.get_integration_types(),
            "CreateIntegration": falcon.create_integration(integration={"thing": "something"}),
            "UpdateIntegration": falcon.update_integration(id=12345, integration={"data": "something"}, overwrite_fields=["banana"]),
            "DeleteIntegration": falcon.delete_integration(id=12345),
            "UpdateIntegrationFail": falcon.update_integration(),
            "DeleteIntegrationFail": falcon.delete_integration(),
            "ExecuteQuery": falcon.execute_query(query="something_interesting", select_fields={"fields":["whatever"]}),
            "ServiceNowGetDeployments": falcon.get_servicenow_deployments(ql_filters="query_search"),
            "ServiceNowGetServices": falcon.get_servicenow_services(ql_filters="query_search", order_by="green"),
            "GetServicesCount": falcon.get_services_count(only_count=True),
            "GetServiceViolationTypes": falcon.get_service_violation_types(filter="search", optional_time=3),
            "GetTags": falcon.get_tags(limit=1, tag_name="chartreuse"),
            "UpsertTags": falcon.update_tags(is_sensitive=False, entries=[{"name": "thing"}]),
            "UpsertTags2": falcon.update_tags(is_sensitive=False),
            "DeleteTags": falcon.delete_tags(is_sensitive=False, name="Bob_the_Tag", value="Priceless")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
