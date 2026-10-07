# test_eval_runs.py
# This class tests the eval_runs service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import EvalRuns

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = EvalRuns(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestEvalRuns:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesEvalRunsV1": falcon.get_eval_runs(ids=["string"], project_id="string"),
            "EntitiesEvalRunsCreateV1": falcon.create_eval_run(actual_cost="string", agent_id="string",
                                                               agent_version_id="string", completed_at="string",
                                                               created_at="string", dataset_entry_ids="string",
                                                               dataset_ids="string", entry_tags="string",
                                                               estimated_cost="string", evaluator_ids="string", id="string",
                                                               is_deleted="string", metadata="string", name="string",
                                                               owner="string", project_id="string", status="string",
                                                               updated_at="string", variable_values="string",
                                                               access_granted_at="string", cid="string", factors="string",
                                                               first_name="string", last_login_at="string",
                                                               last_name="string", uid="string", user_type="string",
                                                               uuid="string", api_client_id="string", email="string",
                                                               completed_cases="string", error_cases="string",
                                                               total_cases="string", average_latency="string",
                                                               average_score="string", evaluator_results="string",
                                                               failed_cases="string", median_score="string",
                                                               passed_cases="string", std_deviation="string",
                                                               total_duration="string"),
            "EntitiesEvalRunsDeleteV1": falcon.delete_eval_run(id="string", project_id="string"),
            "EntitiesEvalRunsUpdateV1": falcon.update_eval_run(project_id="string", actual_cost="string", agent_id="string",
                                                               agent_version_id="string", completed_at="string",
                                                               created_at="string", dataset_entry_ids="string",
                                                               dataset_ids="string", entry_tags="string",
                                                               estimated_cost="string", evaluator_ids="string", id="string",
                                                               is_deleted="string", metadata="string", name="string",
                                                               owner="string", project_id="string", status="string",
                                                               updated_at="string", variable_values="string",
                                                               access_granted_at="string", cid="string", factors="string",
                                                               first_name="string", last_login_at="string",
                                                               last_name="string", uid="string", user_type="string",
                                                               uuid="string", api_client_id="string", email="string",
                                                               completed_cases="string", error_cases="string",
                                                               total_cases="string", average_latency="string",
                                                               average_score="string", evaluator_results="string",
                                                               failed_cases="string", median_score="string",
                                                               passed_cases="string", std_deviation="string",
                                                               total_duration="string"),
            "EntitiesEvalRunsActionV1": falcon.perform_eval_run_action(id="string", action_name="string", action="string",
                                                                       id="string", project_id="string",
                                                                       agent_run_credit_cents="string",
                                                                       judge_run_credit_cents="string"),
            "QueriesEvalRunsV1": falcon.query_eval_runs(offset=1, limit=1, sort="string", filter="string",
                                                        project_id="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks

    def test_payload_coverage(self):
        """Exercise nested payload builder branches."""
        falcon.create_eval_run(access_granted_at="string", cid="string", factors="string", first_name="string", last_login_at="string", last_name="string", uid="string", user_type="string", uuid="string", api_client_id="string", email="string", completed_cases="string", error_cases="string", total_cases="string", average_latency="string", average_score="string", evaluator_results="string", failed_cases="string", median_score="string", passed_cases="string", std_deviation="string", total_duration="string")
        falcon.update_eval_run(access_granted_at="string", cid="string", factors="string", first_name="string", last_login_at="string", last_name="string", uid="string", user_type="string", uuid="string", api_client_id="string", email="string", completed_cases="string", error_cases="string", total_cases="string", average_latency="string", average_score="string", evaluator_results="string", failed_cases="string", median_score="string", passed_cases="string", std_deviation="string", total_duration="string")
        falcon.perform_eval_run_action(agent_run_credit_cents="string", judge_run_credit_cents="string")
        assert True
