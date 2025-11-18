# test_it_automation.py
# This class tests the IT Automation service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ITAutomation

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ITAutomation(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestITAutomation:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "ITAutomationGetAssociatedTasks": falcon.get_associated_tasks(),
            "ITAutomationCombinedScheduledTasks": falcon.scheduled_task_details(),
            "ITAutomationGetTaskExecutionsByQuery": falcon.get_executions_by_query(),
            "ITAutomationGetTaskGroupsByQuery": falcon.get_task_groups_by_query(),
            "ITAutomationGetTasksByQuery": falcon.get_tasks_by_query(),
            "ITAutomationRunLiveQuery": falcon.run_live_query(discover_new_hosts=True),
            "ITAutomationUpdatePolicyHostGroups": falcon.update_policy_host_groups(host_group_ids="123456"),
            "ITAutomationUpdatePoliciesPrecedence": falcon.update_policies_precedence(),
            "ITAutomationGetPolicies": falcon.get_policies(),
            "ITAutomationCreatePolicy": falcon.create_policy(enable_os_query=True, is_enabled=False),
            "ITAutomationUpdatePolicies": falcon.update_policy(),
            "ITAutomationDeletePolicy": falcon.delete_policy(),
            "ITAutomationGetScheduledTasks": falcon.get_scheduled_task(),
            "ITAutomationCreateScheduledTask": falcon.create_scheduled_task(discover_new_hosts=True),
            "ITAutomationUpdateScheduledTask": falcon.update_scheduled_task(),
            "ITAutomationDeleteScheduledTasks": falcon.delete_scheduled_task(),
            "ITAutomationCancelTaskExecution": falcon.cancel_execution(),
            "ITAutomationGetTaskExecutionHostStatus": falcon.get_execution_host_status(),
            "ITAutomationRerunTaskExecution": falcon.rerun_execution(task_execution_id="123456"),
            "ITAutomationGetExecutionResultsSearchStatus": falcon.get_execution_results_search_status(),
            "ITAutomationStartExecutionResultsSearch": falcon.execution_results_search(group_by_fields="name"),
            "ITAutomationGetExecutionResults": falcon.get_execution_results(),
            "ITAutomationGetTaskExecution": falcon.get_execution(),
            "ITAutomationStartTaskExecution": falcon.start_execution(discover_new_hosts=True),
            "ITAutomationGetTaskGroups": falcon.get_task_group(),
            "ITAutomationCreateTaskGroup": falcon.create_task_group(),
            "ITAutomationUpdateTaskGroup": falcon.update_task_group(),
            "ITAutomationDeleteTaskGroups": falcon.delete_task_groups(),
            "ITAutomationGetTasks": falcon.get_tasks(),
            "ITAutomationCreateTask": falcon.create_task(task_parameters={"label": "bob"}, add_assigned_user_ids="123456"),
            "ITAutomationUpdateTask": falcon.update_task(),
            "ITAutomationDeleteTask": falcon.delete_task(),
            "ITAutomationQueryPolicies": falcon.query_policies(),
            "ITAutomationSearchScheduledTasks": falcon.search_scheduled_tasks(),
            "ITAutomationSearchTaskExecutions": falcon.search_task_executions(),
            "ITAutomationSearchTaskGroups": falcon.search_task_groups(),
            "ITAutomationSearchTasks": falcon.search_tasks(),
            "ITAutomationGetUserGroup": falcon.get_user_group(ids="12345678"),
            "ITAutomationCreateUserGroup": falcon.create_user_group(name="whatever"),
            "ITAutomationUpdateUserGroup": falcon.update_user_group(id="12345678"),
            "ITAutomationDeleteUserGroup": falcon.delete_user_groups(ids="12345678"),
            "ITAutomationSearchUserGroups": falcon.search_user_groups(limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
