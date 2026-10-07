# test_eval_dataset_entries.py
# This class tests the eval_dataset_entries service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import EvalDatasetEntries

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = EvalDatasetEntries(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestEvalDatasetEntries:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesEvalDatasetEntriesV1": falcon.get_eval_dataset_entries(ids=["string"], project_id="string"),
            "EntitiesEvalDatasetEntriesUpdateV1": falcon.update_eval_dataset_entry(created_at="string", data="string",
                                                                                   dataset_id="string", description="string",
                                                                                   id="string", is_deleted="string",
                                                                                   metadata="string", name="string",
                                                                                   owner="string", project_id="string",
                                                                                   tags="string", updated_at="string",
                                                                                   access_granted_at="string", cid="string",
                                                                                   factors="string", first_name="string",
                                                                                   last_login_at="string", last_name="string",
                                                                                   status="string", uid="string",
                                                                                   user_type="string", uuid="string",
                                                                                   api_client_id="string", email="string"),
            "EntitiesEvalDatasetEntriesCreateV1": falcon.create_eval_dataset_entry(created_at="string", data="string",
                                                                                   dataset_id="string", description="string",
                                                                                   id="string", is_deleted="string",
                                                                                   metadata="string", name="string",
                                                                                   owner="string", project_id="string",
                                                                                   tags="string", updated_at="string",
                                                                                   access_granted_at="string", cid="string",
                                                                                   factors="string", first_name="string",
                                                                                   last_login_at="string", last_name="string",
                                                                                   status="string", uid="string",
                                                                                   user_type="string", uuid="string",
                                                                                   api_client_id="string", email="string"),
            "EntitiesEvalDatasetEntriesDeleteV1": falcon.delete_eval_dataset_entry(id="string", project_id="string"),
            "QueriesEvalDatasetEntriesV1": falcon.query_eval_dataset_entries(offset=1, limit=1, sort="string",
                                                                             filter="string", project_id="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks

    def test_payload_coverage(self):
        """Exercise nested payload builder branches."""
        falcon.update_eval_dataset_entry(access_granted_at="string", cid="string", factors="string", first_name="string", last_login_at="string", last_name="string", status="string", uid="string", user_type="string", uuid="string", api_client_id="string", email="string")
        falcon.create_eval_dataset_entry(access_granted_at="string", cid="string", factors="string", first_name="string", last_login_at="string", last_name="string", status="string", uid="string", user_type="string", uuid="string", api_client_id="string", email="string")
        assert True
