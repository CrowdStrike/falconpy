# test_aidr.py
# This class tests the aidr service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import AIDR

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = AIDR(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestAIDR:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "aggregateAgentSessionsV1": falcon.aggregate_aidr_agent_sessions(limit=1, offset=1, time_range="string",
                                                                             product="string"),
            "aggregateAgentsV1": falcon.aggregate_aidr_agents(limit=1, offset=1, time_range="string"),
            "aggregateDetectionsV1": falcon.aggregate_aidr_detections(limit=1, offset=1, time_range="string",
                                                                      agent_id="string", product="string"),
            "aggregateSkillUsageV1": falcon.aggregate_aidr_skill_usage(limit=1, offset=1, time_range="string",
                                                                       session_id="string", aid="string"),
            "aggregateSkillsV1": falcon.aggregate_aidr_skills(limit=1, offset=1, time_range="string", name_filter="string"),
            "aggregateToolUsageV1": falcon.aggregate_aidr_tool_usage(limit=1, offset=1, time_range="string",
                                                                     session_id="string", aid="string"),
            "aggregateToolsV1": falcon.aggregate_aidr_tools(limit=1, offset=1, time_range="string", sensor_id="string"),
            "entitiesAgentInstallationsV1": falcon.get_aidr_agent_installations(ids="12345678"),
            "entitiesAgentOSUsersV1": falcon.get_aidr_agent_os_users(aid="string", username="string"),
            "entitiesAgentSessionsV1": falcon.get_aidr_agent_sessions(ids="12345678"),
            "entitiesAgentsV1": falcon.get_aidr_agents(ids="12345678"),
            "entitiesClassifiedFileAccessV1": falcon.get_aidr_classified_file_access(id="12345678"),
            "entitiesExecutionsV1": falcon.get_aidr_executions(id="string", context_process_id="string"),
            "entitiesFileEventsV1": falcon.get_aidr_file_events(id="12345678"),
            "entitiesModelNamesV1": falcon.get_aidr_model_names(ids="12345678"),
            "entitiesNetworkEventsV1": falcon.get_aidr_network_events(id="12345678"),
            "entitiesProcessTreeV1": falcon.get_aidr_process_tree(id="string", depth=1),
            "entitiesSessionActivityV1": falcon.get_aidr_session_activity(ids="12345678"),
            "entitiesSkillsV1": falcon.get_aidr_skills(ids="12345678"),
            "entitiesToolsV1": falcon.get_aidr_tools(ids="12345678"),
            "queryAgentInstallationsV1": falcon.query_aidr_agent_installations(limit=1, offset=1, time_range="string",
                                                                               sensor_id="string", product="string",
                                                                               hostname="string"),
            "queryAgentOSUsersV1": falcon.query_aidr_agent_os_users(limit=1, offset=1, time_range="string",
                                                                    object_sid="string", aid="string", username="string"),
            "queryAgentSessionsV1": falcon.query_aidr_agent_sessions(limit=1, offset=1, time_range="string", product="string"),
            "queryAgentsV1": falcon.query_aidr_agents(limit=1, offset=1, time_range="string", product="string",
                                                      hostname="string"),
            "queryDetectionsV1": falcon.query_aidr_detections(limit=1, offset=1, time_range="string", agent_id="string",
                                                              product="string"),
            "queryExecutionsV1": falcon.query_aidr_executions(limit=1, offset=1, time_range="string", session_id="string",
                                                              aid="string"),
            "queryMcpServerNamesV1": falcon.query_aidr_mcp_server_names(limit=1, offset=1, time_range="string"),
            "queryModelNamesV1": falcon.query_aidr_model_names(limit=1, offset=1, time_range="string"),
            "queryPromptsV1": falcon.query_aidr_prompts(limit=1, offset=1, time_range="string", session_id="string",
                                                        aid="string"),
            "querySkillUsageV1": falcon.query_aidr_skill_usage(limit=1, offset=1, time_range="string", name="string",
                                                               session_id="string", aid="string"),
            "querySkillsV1": falcon.query_aidr_skills(limit=1, offset=1, time_range="string", name_filter="string"),
            "queryToolUsageV1": falcon.query_aidr_tool_usage(limit=1, offset=1, time_range="string", tool_name="string",
                                                             session_id="string", aid="string"),
            "queryToolsV1": falcon.query_aidr_tools(limit=1, offset=1, time_range="string", sensor_id="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
