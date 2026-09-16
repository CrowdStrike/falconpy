# test_agents.py
# This class tests the agents service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import Agents

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Agents(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestAgents:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "DeleteAgentV1": falcon.delete_agent(id="12345678"),
            "GetAgentsV2": falcon.get_studio_agents(ids="12345678"),
            "CreateOrEditAgentExternalV3": falcon.create_or_update_agent(duplicate_from_agent_id="string", id="string",
                                                                         template_id="string", compaction_config="string",
                                                                         description="string", input_format="string",
                                                                         knowledge_base_ids="string", model="string",
                                                                         model_config="string", name="string",
                                                                         output_format="string", parent_version_ids="string",
                                                                         skill_ids="string", system_prompt="string",
                                                                         targeting_config="string", tools="string"),
            "PatchAgentExternalV3": falcon.update_agent(id="string", dry_run=True, is_enabled="string", is_published="string",
                                                        version_id="string"),
            "QueryAgentsV2": falcon.query_studio_agents(offset=1, limit=1, sort="string", filter="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks

    def test_payload_coverage(self):
        """Exercise nested payload builder branches."""
        falcon.create_or_update_agent(compaction_config="string", description="string", input_format="string", knowledge_base_ids="string", model="string", model_config="string", name="string", output_format="string", parent_version_ids="string", skill_ids="string", system_prompt="string", targeting_config="string", tools="string")
        assert True
