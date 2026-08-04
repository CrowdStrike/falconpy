# test_spans.py
# This class tests the spans service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import Spans

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Spans(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestSpans:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesSpansV1": falcon.entities_spans_v1(ids="12345678"),
            "QueriesSpansV1": falcon.queries_spans_v1(offset=1, limit=1, sort="string", filter="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
