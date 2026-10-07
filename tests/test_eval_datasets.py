# test_eval_datasets.py
# This class tests the eval_datasets service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import EvalDatasets

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = EvalDatasets(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestEvalDatasets:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesEvalDatasetsDownloadV1": falcon.download_eval_dataset(id="string", project_id="string"),
            "EntitiesEvalDatasetsV1": falcon.get_eval_datasets(ids=["string"], project_id="string"),
            "EntitiesEvalDatasetsUpdateV1": falcon.update_eval_dataset(agent_ids="string", created_at="string",
                                                                       default_prompt_template="string", description="string",
                                                                       entryschema="string", id="string", is_deleted="string",
                                                                       metadata="string", name="string", owner="string",
                                                                       project_id="string", tags="string",
                                                                       updated_at="string", access_granted_at="string",
                                                                       cid="string", factors="string", first_name="string",
                                                                       last_login_at="string", last_name="string",
                                                                       status="string", uid="string", user_type="string",
                                                                       uuid="string", api_client_id="string", email="string"),
            "EntitiesEvalDatasetsCreateV1": falcon.create_eval_dataset(agent_ids="string", description="string", id="string",
                                                                       metadata="string", name="string", project_id="string",
                                                                       tags="string"),
            "EntitiesEvalDatasetsDeleteV1": falcon.delete_eval_dataset(id="string", project_id="string"),
            "QueriesEvalDatasetsV1": falcon.query_eval_datasets(offset=1, limit=1, sort="string", filter="string",
                                                                project_id="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks

    def test_payload_coverage(self):
        """Exercise nested payload builder branches."""
        falcon.update_eval_dataset(access_granted_at="string", cid="string", factors="string", first_name="string", last_login_at="string", last_name="string", status="string", uid="string", user_type="string", uuid="string", api_client_id="string", email="string")
        assert True
