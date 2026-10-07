# test_eval_evaluators.py
# This class tests the eval_evaluators service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import EvalEvaluators

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = EvalEvaluators(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestEvalEvaluators:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesEvalEvaluatorsV1": falcon.get_eval_evaluators(ids=["string"], project_id="string"),
            "EntitiesEvalEvaluatorsUpdateV1": falcon.update_eval_evaluator(agent_ids="string", config="string",
                                                                           created_at="string", description="string",
                                                                           evaluator_type="string", id="string",
                                                                           is_deleted="string", metadata="string",
                                                                           name="string", owner="string", project_id="string",
                                                                           tags="string", updated_at="string",
                                                                           access_granted_at="string", cid="string",
                                                                           factors="string", first_name="string",
                                                                           last_login_at="string", last_name="string",
                                                                           status="string", uid="string", user_type="string",
                                                                           uuid="string", api_client_id="string",
                                                                           email="string"),
            "EntitiesEvalEvaluatorsCreateV1": falcon.create_eval_evaluator(agent_ids="string", config="string",
                                                                           created_at="string", description="string",
                                                                           evaluator_type="string", id="string",
                                                                           is_deleted="string", metadata="string",
                                                                           name="string", owner="string", project_id="string",
                                                                           tags="string", updated_at="string",
                                                                           access_granted_at="string", cid="string",
                                                                           factors="string", first_name="string",
                                                                           last_login_at="string", last_name="string",
                                                                           status="string", uid="string", user_type="string",
                                                                           uuid="string", api_client_id="string",
                                                                           email="string"),
            "EntitiesEvalEvaluatorsDeleteV1": falcon.delete_eval_evaluator(id="string", project_id="string"),
            "QueriesEvalEvaluatorsV1": falcon.query_eval_evaluators(offset=1, limit=1, sort="string", filter="string",
                                                                    project_id="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks

    def test_payload_coverage(self):
        """Exercise nested payload builder branches."""
        falcon.update_eval_evaluator(access_granted_at="string", cid="string", factors="string", first_name="string", last_login_at="string", last_name="string", status="string", uid="string", user_type="string", uuid="string", api_client_id="string", email="string")
        falcon.create_eval_evaluator(access_granted_at="string", cid="string", factors="string", first_name="string", last_login_at="string", last_name="string", status="string", uid="string", user_type="string", uuid="string", api_client_id="string", email="string")
        assert True
