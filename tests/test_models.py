# test_models.py
# This class tests the models service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import Models

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Models(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestModels:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesModelsV1": falcon.entities_models_v1(ids="12345678"),
            "QueriesModelsV1": falcon.queries_models_v1(offset=1, limit=1, filter="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
