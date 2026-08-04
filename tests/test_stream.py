# test_stream.py
# This class tests the stream service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import Stream

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Stream(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestStream:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "StreamInvocationResponseV1": falcon.stream_invocation_response_v1(id="12345678"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
