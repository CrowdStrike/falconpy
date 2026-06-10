# test_knowledge_base_files.py
# This class tests the knowledge_base_files service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import KnowledgeBaseFiles

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = KnowledgeBaseFiles(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestKnowledgeBaseFiles:
    def test_all_code_paths(self):
        error_checks = True
        payload = open("tests/testfile.png", "rb").read()
        create = falcon.entities_knowledge_base_files_create_v1
        update = falcon.entities_knowledge_base_files_update_v1
        tests = {
            "EntitiesKnowledgeBaseFilesDownloadV1": falcon.entities_knowledge_base_files_download_v1(knowledge_base_id="str",
                                                                                                     id="string"),
            "EntitiesKnowledgeBaseFilesV1": falcon.entities_knowledge_base_files_v1(knowledge_base_id="string",
                                                                                    ids=["string"], include_deleted=True),
            "EntitiesKnowledgeBaseFilesUpdateV1": update(id="string", file=payload,
                                                         file_name="testfile.csv", file_description="unit test"),
            "EntitiesKnowledgeBaseFilesUpdateV1_fail": update(),
            "EntitiesKnowledgeBaseFilesCreateV1": create(knowledge_base_id="string", file=payload,
                                                         file_name="testfile.csv", file_description="unit test"),
            "EntitiesKnowledgeBaseFilesCreateV1_fail": create(),
            "EntitiesKnowledgeBaseFilesCreateV1_params": create(file_name="testfile.csv",
                                                                parameters={"knowledge_base_id": "string",
                                                                            "file": payload}),
            "EntitiesKnowledgeBaseFilesDeleteV1": falcon.entities_knowledge_base_files_delete_v1(knowledge_base_id="string",
                                                                                                 id="string"),
            "QueriesKnowledgeBaseFilesV1": falcon.queries_knowledge_base_files_v1(knowledge_base_id="string", offset=1,
                                                                                  limit=1, filter="string",
                                                                                  include_deleted=True),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
