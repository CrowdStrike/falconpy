# test_eval_cases.py
# This class tests the eval_cases service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import EvalCases

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = EvalCases(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestEvalCases:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesEvalCasesV1": falcon.get_eval_cases(ids=["string"], project_id="string"),
            "QueriesEvalCasesV1": falcon.query_eval_cases(offset=1, limit=1, sort="string", filter="string",
                                                          project_id="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
