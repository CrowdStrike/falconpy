# test_intelligence_indicator_graph.py
# This class tests the intelligence_indicator_graph service class

# import json
import os
import sys
import pytest
from urllib.parse import urlparse
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import IntelligenceIndicatorGraph

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = IntelligenceIndicatorGraph(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 401, 403, 404, 429]


class TestIntelligenceIndicatorGraph:
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "SearchIndicators": falcon.search(filter="indicator:'malware.ru'", limit=1, sort="PublishDate|desc"),
            "LookupIndicators": falcon.lookup("whatever.com,1.2.3.4"),
            "LookupIndicators": falcon.lookup(body={"values": "whatever.com, 1.2.3.4"})
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
