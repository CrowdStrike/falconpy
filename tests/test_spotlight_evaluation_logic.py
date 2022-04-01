# test_spotlight_evaluation_logic.py
# This class tests the spotlight_evaluation_logic service class

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Classes to test - manually imported from sibling folder
from falconpy import SpotlightEvaluationLogic
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))


auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = SpotlightEvaluationLogic(auth_object=config)
AllowedResponses = [200, 400, 403, 404, 429]


class TestSpotlightEval:
    def spotlight_queryEvaluationLogic(self):
        if falcon.queryEvaluationLogic(parameters={"limit": 1,
                                                   "filter": "created_timestamp:>'2021-01-01T00:00:01Z'"
                                                   }
                                       )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def spotlight_query_evaluation_logic_combined(self):
        if falcon.query_evaluation_logic_combined(limit=1,
                                                 filter="created_timestamp:>'2021-01-01T00:00:01Z'"
                                                 )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def spotlight_getEvalLogic(self):
        try:
            id_lookup = falcon.queryEvaluationLogic(limit=1,
                                                    filter="created_timestamp:>'2021-01-01T00:00:01Z'"
                                                    )
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"]
            else:
                id_list = "1234567890"
            if falcon.getEvaluationLogic(ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            pytest.skip("Workflow-related error, skipping")
            return True

    def spotlight_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        if falcon.combinedQueryEvaluationLogic()["status_code"] != 500:
            errorChecks = False
        if falcon.queryEvaluationLogic(parameters={})["status_code"] != 500:
            errorChecks = False
        if falcon.getEvaluationLogic(ids="12345678")["status_code"] != 500:
            errorChecks = False
        return errorChecks

    def test_queryEvaluationLogic(self):
        assert self.spotlight_queryEvaluationLogic() is True

    def test_queryEvaluationLogic_combined(self):
        assert self.spotlight_query_evaluation_logic_combined() is True

    def test_getEvaluationLogic(self):
        assert self.spotlight_getEvalLogic() is True

    def test_Errors(self):
        assert self.spotlight_GenerateErrors() is True
