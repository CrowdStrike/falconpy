# test_knowledge_bases.py
# This class tests the knowledge_bases service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import KnowledgeBases

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = KnowledgeBases(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestKnowledgeBases:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "AggregatesKnowledgeBasesV1": falcon.aggregates_knowledge_bases_v1(include_deleted=True,
                                                                               date_ranges=[{"from": "string", "to": "string"}],
                                                                               field="string", filter="string",
                                                                               interval="string", min_doc_count=0,
                                                                               missing="string", name="string", q="string",
                                                                               ranges=[{"From": 0, "To": 0}], size=0,
                                                                               sort="string", sub_aggregates=["string"],
                                                                               time_zone="string", type="string"),
            "EntitiesKnowledgeBasesV1": falcon.entities_knowledge_bases_v1(ids=["string"], include_deleted=True),
            "EntitiesKnowledgeBasesCreateV1": falcon.entities_knowledge_bases_create_v1(created_at="string",
                                                                                        description="string",
                                                                                        embedding_model="string",
                                                                                        files_count="string", id="string",
                                                                                        is_deleted="string", name="string",
                                                                                        updated_at="string", cid="string",
                                                                                        factors="string", first_name="string",
                                                                                        last_login_at="string",
                                                                                        last_name="string", status="string",
                                                                                        uid="string", user_type="string",
                                                                                        uuid="string"),
            "EntitiesKnowledgeBasesUpdateV1": falcon.entities_knowledge_bases_update_v1(created_at="string",
                                                                                        description="string",
                                                                                        embedding_model="string",
                                                                                        files_count="string", id="string",
                                                                                        is_deleted="string", name="string",
                                                                                        updated_at="string", cid="string",
                                                                                        factors="string", first_name="string",
                                                                                        last_login_at="string",
                                                                                        last_name="string", status="string",
                                                                                        uid="string", user_type="string",
                                                                                        uuid="string"),
            "QueriesKnowledgeBasesV1": falcon.queries_knowledge_bases_v1(offset=1, limit=1, sort="string", filter="string",
                                                                         include_deleted=True),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
