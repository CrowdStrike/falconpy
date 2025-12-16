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
AllowedResponses = [200, 201, 204, 207, 400, 403, 404, 406, 429, 500, 503]


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
            "GetIntegrationTasks": falcon.get_integration_tasks(category="something", order_by="whatever"),
            "GetIntegrationTasks2": falcon.get_integration_tasks(category="something", parameters={"order_by": "whatever"}),
            "GetIntegrationTasksAdmin": falcon.get_integration_tasks_admin(category="something", order_by="whatever"),
            "GetIntegrationTasksAdmin2": falcon.get_integration_tasks_admin(category="something", parameters={"order_by": "whatever"}),
            "CreateIntegrationTask": falcon.create_integration_task(integration_task={"something": "different"}),
            "UpdateIntegrationTask": falcon.update_integration_task(id=42, integration_task={"something": "else"}),
            "DeleteIntegrationTask": falcon.delete_integration_task(id=42),
            "RunIntegrationTask": falcon.run_integration_task(id=42, task_id=42),
            "RunIntegrationTaskV2": falcon.run_integration_task_v2(id=42, task_id=42),
            "RunIntegrationTaskAdmin": falcon.run_integration_task_admin(id=42, task_id=42),
            "UpdateIntegrationTaskFail": falcon.update_integration_task(),
            "DeleteIntegrationTaskFail": falcon.delete_integration_task(),
            "RunIntegrationTaskFail": falcon.run_integration_task(),
            "RunIntegrationTaskV2Fail": falcon.run_integration_task_v2(),
            "RunIntegrationTaskAdminFail": falcon.run_integration_task_admin(),
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
            "DeleteTags": falcon.delete_tags(is_sensitive=False, name="Bob_the_Tag", value="Priceless"),
            "ExecuteFunctionDataCount": falcon.execute_function_data_count(cloud_provider="aws", aws_lambda_arn="whatevers"),
            "ExecuteFunctionsCount": falcon.execute_functions_count(cloud_account_id="12345678", cloud_provider="aws"),
            "ExecuteFunctionDataQueryCount": falcon.execute_function_data_query_count(field="whatever"),
            "ExecuteFunctionsQueryCount": falcon.execute_functions_query_count(field="whatever"),
            "ExecuteFunctionData": falcon.execute_function_data(field="whatever"),
            "ExecuteFunctionsOvertime": falcon.execute_functions_over_time(field="whatever"),
            "ExecuteFunctions": falcon.execute_functions(field="whatever"),
            "ExecuteFunctionDataQuery": falcon.execute_function_data_query(field="whatever"),
            "ExecuteFunctionsQueryOvertime": falcon.execute_functions_query_over_time(field="whatever"),
            "ExecuteFunctionsQuery": falcon.execute_functions_query(field="whatever"),
            "getServiceArtifacts": falcon.get_service_artifacts(persistent_signature="whatever",
                                                                optional_time="12345",
                                                                revision_id="whatever",
                                                                order_by="name"
                                                                ),
            "getServiceArtifacts2": falcon.get_service_artifacts(parameters={
                                                                    "persistent_signature": "whatever",
                                                                    "optional_time": "12345",
                                                                    "revision_id": "whatever",
                                                                    "order_by": "name"
                                                                    }),
            "GetIntegrationTasksMetadata": falcon.get_integration_tasks_metadata(category="collection"),
            "GetIntegrationTasksV2": falcon.get_integration_tasks_v2(limit=1, order_by="whatever"),
            "GetIntegrationTasksV2num2": falcon.get_integration_tasks_v2(limit=1, parameters={"order_by": "whatever"}),
            "GetIntegrationsV2": falcon.get_integrations_v2(integration_type=1),
            "GetExecutorNodesMetadata": falcon.get_executor_nodes_metadata(executor_node_ids="whatever"),
            "RetrieveRelayInstances": falcon.retrieve_relay_instances(id="1234", current_aws_arn="whatever", order_by="state", use_jobs=False),
            "RetrieveRelayInstances2": falcon.retrieve_relay_instances(current_aws_arn="whatever", order_by="state", use_jobs=False),
            "GetCloudSecurityIntegrationState": falcon.get_cloud_security_integration_state(),
            "SetCloudSecurityIntegrationState": falcon.set_cloud_security_integration_state(is_enabled=False),
            "SetCloudSecurityIntegrationState2": falcon.set_cloud_security_integration_state(body={"is_enabled": False}),
        }
        for key in tests:
            if not isinstance(tests[key], bytes):
                if tests[key]["status_code"] not in AllowedResponses:
                    error_checks = False
                    # print(key)
                    # print(tests[key])
                
        assert error_checks
