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
        tests = {
            "EntitiesKnowledgeBaseFilesDownloadV1": falcon.entities_knowledge_base_files_download_v1(knowledge_base_id="string",
                                                                                                     id="string"),
            "EntitiesKnowledgeBaseFilesV1": falcon.entities_knowledge_base_files_v1(knowledge_base_id="string",
                                                                                    ids=["string"], include_deleted=True),
            "EntitiesKnowledgeBaseFilesUpdateV1": falcon.entities_knowledge_base_files_update_v1(),
            "EntitiesKnowledgeBaseFilesCreateV1": falcon.entities_knowledge_base_files_create_v1(),
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
