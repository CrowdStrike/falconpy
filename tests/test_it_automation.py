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
            "ITAutomationGetAssociatedTasks": falcon.get_associated_tasks(id="file123",
                                                                          filter="name:'test'",
                                                                          sort="name|asc",
                                                                          offset=0,
                                                                          limit=50
                                                                          ),
            "ITAutomationCombinedScheduledTasks": falcon.scheduled_task_details(filter="task_name:'test'",
                                                                                sort="created_time|desc",
                                                                                offset=0,
                                                                                limit=50
                                                                                ),
            "ITAutomationGetTaskExecutionsByQuery": falcon.get_executions_by_query(filter="status:'completed'",
                                                                                    sort="start_time|desc",
                                                                                    offset=0,
                                                                                    limit=50
                                                                                    ),
            "ITAutomationGetTaskGroupsByQuery": falcon.get_task_groups_by_query(filter="name:'test'",
                                                                                sort="created_time|desc",
                                                                                offset=0,
                                                                                limit=50
                                                                                ),
            "ITAutomationGetTasksByQuery": falcon.get_tasks_by_query(filter="name:'test'",
                                                                     sort="created_time|desc",
                                                                     offset=0,
                                                                     limit=50
                                                                     ),
            "ITAutomationRunLiveQuery": falcon.run_live_query(discover_new_hosts=True,
                                                              discover_offline_hosts=True,
                                                              distribute=True,
                                                              expiration_interval="1h",
                                                              guardrails={"run_time_limit_millis": 5000},
                                                              osquery="SELECT * FROM processes",
                                                              target="host123"
                                                              ),
            "ITAutomationUpdatePolicyHostGroups": falcon.update_policy_host_groups(action="add",
                                                                                   host_group_ids="123456",
                                                                                   policy_id="policy123"
                                                                                   ),
            "ITAutomationUpdatePoliciesPrecedence": falcon.update_policies_precedence(ids="policy1,policy2",
                                                                                      platform="Windows"
                                                                                      ),
            "ITAutomationGetPolicies": falcon.get_policies(ids="policy123"),
            "ITAutomationCreatePolicy": falcon.create_policy(name="test-policy",
                                                             description="Test automation policy",
                                                             platform="Windows",
                                                             enable_os_query=True,
                                                             enable_script_execution=True,
                                                             enable_python_execution=False,
                                                             execution_timeout=30,
                                                             execution_timeout_unit="Minutes",
                                                             cpu_throttle=50,
                                                             concurrent_host_limit=10
                                                             ),
            "ITAutomationUpdatePolicies": falcon.update_policy(id="policy123",
                                                               name="updated-policy",
                                                               description="Updated policy",
                                                               is_enabled=True,
                                                               enable_os_query=True,
                                                               execution_timeout=60,
                                                               execution_timeout_unit="Minutes"
                                                               ),
            "ITAutomationDeletePolicy": falcon.delete_policy(ids="policy123"),
            "ITAutomationGetScheduledTasks": falcon.get_scheduled_task(ids="sched123"),
            "ITAutomationCreateScheduledTask": falcon.create_scheduled_task(discover_new_hosts=True,
                                                                            discover_offline_hosts=True,
                                                                            distribute=True,
                                                                            is_active=True,
                                                                            task_id="task123",
                                                                            target="host123",
                                                                            schedule={"frequency": "Daily",
                                                                                     "time": "09:00",
                                                                                     "timezone": "UTC"}
                                                                            ),
            "ITAutomationUpdateScheduledTask": falcon.update_scheduled_task(id="sched123",
                                                                            is_active=False,
                                                                            task_id="task456",
                                                                            target="host456"
                                                                            ),
            "ITAutomationDeleteScheduledTasks": falcon.delete_scheduled_task(ids="sched123"),
            "ITAutomationCancelTaskExecution": falcon.cancel_execution("exec123"),
            "ITAutomationGetTaskExecutionHostStatus": falcon.get_execution_host_status(ids="exec123",
                                                                                       filter="status:'completed'",
                                                                                       sort="start_time|desc",
                                                                                       offset=0,
                                                                                       limit=50
                                                                                       ),
            "ITAutomationRerunTaskExecution": falcon.rerun_execution(task_execution_id="exec123", run_type="hosts"),
            "ITAutomationGetExecutionResultsSearchStatus": falcon.get_execution_results_search_status(id="search123"),
            "ITAutomationStartExecutionResultsSearch": falcon.execution_results_search(task_execution_id="exec123",
                                                                                       group_by_fields="hostname",
                                                                                       filter_expressions="status:'success'",
                                                                                       start="2024-01-01",
                                                                                       end="2024-12-31"
                                                                                       ),
            "ITAutomationGetExecutionResults": falcon.get_execution_results(id="search123",
                                                                            offset=0,
                                                                            limit=50,
                                                                            sort="hostname.asc"
                                                                            ),
            "ITAutomationGetTaskExecution": falcon.get_execution(ids="exec123"),
            "ITAutomationStartTaskExecution": falcon.start_execution(discover_new_hosts=True,
                                                                     discover_offline_hosts=True,
                                                                     distribute=True,
                                                                     task_id="task123",
                                                                     target="host123",
                                                                     expiration_interval="2h",
                                                                     guardrails={"run_time_limit_millis": 10000}
                                                                     ),
            "ITAutomationGetTaskGroups": falcon.get_task_group(ids="group123"),
            "ITAutomationCreateTaskGroup": falcon.create_task_group(name="test-group",
                                                                    description="Test task group",
                                                                    access_type="Public",
                                                                    assigned_user_ids=["user1"],
                                                                    task_ids=["task1", "task2"]
                                                                    ),
            "ITAutomationUpdateTaskGroup": falcon.update_task_group(id="group123",
                                                                    name="updated-group",
                                                                    description="Updated group",
                                                                    add_task_ids=["task3"],
                                                                    remove_task_ids=["task1"]
                                                                    ),
            "ITAutomationDeleteTaskGroups": falcon.delete_task_groups(ids="group123"),
            "ITAutomationGetTasks": falcon.get_tasks(ids="task123"),
            "ITAutomationCreateTask": falcon.create_task(name="test-task",
                                                         description="Test automation task",
                                                         task_type="query",
                                                         access_type="Public",
                                                         task_parameters=[{"label": "param1",
                                                                          "key": "key1",
                                                                          "input_type": "text"}],
                                                         add_assigned_user_ids="user123",
                                                         target="host123"
                                                         ),
            "ITAutomationUpdateTask": falcon.update_task(id="task123",
                                                         name="updated-task",
                                                         description="Updated task",
                                                         add_assigned_user_ids=["user456"]
                                                         ),
            "ITAutomationDeleteTask": falcon.delete_task(ids="task123"),
            "ITAutomationQueryPolicies": falcon.query_policies(offset=0,
                                                               limit=50,
                                                               sort="precedence|asc",
                                                               platform="Windows"
                                                               ),
            "ITAutomationSearchScheduledTasks": falcon.search_scheduled_tasks(filter="task_name:'test'",
                                                                              sort="created_time|desc",
                                                                              offset=0,
                                                                              limit=50
                                                                              ),
            "ITAutomationSearchTaskExecutions": falcon.search_task_executions(filter="status:'completed'",
                                                                              sort="start_time|desc",
                                                                              offset=0,
                                                                              limit=50
                                                                              ),
            "ITAutomationSearchTaskGroups": falcon.search_task_groups(filter="name:'test'",
                                                                      sort="created_time|desc",
                                                                      offset=0,
                                                                      limit=50
                                                                      ),
            "ITAutomationSearchTasks": falcon.search_tasks(filter="name:'test'",
                                                           sort="created_time|desc",
                                                           offset=0,
                                                           limit=50
                                                           ),
            "ITAutomationGetUserGroup": falcon.get_user_group(ids="12345678"),
            "ITAutomationCreateUserGroup": falcon.create_user_group(name="test-group", description="Test user group"),
            "ITAutomationUpdateUserGroup": falcon.update_user_group(id="12345678",
                                                                    name="updated-group",
                                                                    description="Updated user group",
                                                                    add_user_ids="user1"
                                                                    ),
            "ITAutomationDeleteUserGroup": falcon.delete_user_groups(ids="12345678"),
            "ITAutomationSearchUserGroups": falcon.search_user_groups(filter="name:'test'",
                                                                      sort="name|asc",
                                                                      offset=0,
                                                                      limit=50
                                                                      )
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
