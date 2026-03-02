# test_spotlight_vulnerabilities.py
# This class tests the spotlight_vulnerabilities service class

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Classes to test - manually imported from sibling folder
from falconpy import SpotlightVulnerabilities
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))


auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = SpotlightVulnerabilities(auth_object=config)
AllowedResponses = [200, 400, 403, 429]


class TestSpotlight:
    def spotlight_queryVulnerabilities(self):
        result = falcon.queryVulnerabilities(parameters={"limit": 1,
                                                         "filter": "created_timestamp:>'2021-01-01T00:00:01Z'"
                                                         },
                                             pythonic=True
                                             )
        if result.status_code in AllowedResponses:
            _ = result.after
            return True
        else:
            return False

    def spotlight_query_vulnerabilities_combined(self):
        if falcon.query_vulnerabilities_combined(limit=1,
                                                 filter="created_timestamp:>'2021-01-01T00:00:01Z'"
                                                 )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def spotlight_getVulnerabilities(self):
        try:
            id_lookup = falcon.queryVulnerabilities(limit=1,
                                                    filter="created_timestamp:>'2021-01-01T00:00:01Z'"
                                                    )
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"]
            else:
                id_list = "1234567890"
            if falcon.getVulnerabilities(ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            pytest.skip("Workflow-related error, skipping")
            return True

    def spotlight_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        if falcon.combinedQueryVulnerabilities()["status_code"] != 500:
            errorChecks = False
        if falcon.queryVulnerabilities(parameters={})["status_code"] != 500:
            errorChecks = False
        if falcon.getVulnerabilities(ids="12345678")["status_code"] != 500:
            errorChecks = False
        if falcon.getRemediations(ids="12345678")["status_code"] != 500:
            errorChecks = False
        if falcon.getRemediationsV2(ids="12345678")["status_code"] != 500:
            errorChecks = False
        return errorChecks

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_queryVulnerabilities(self):
        assert self.spotlight_queryVulnerabilities() is True

    def test_queryVulnerabilities_combined(self):
        assert self.spotlight_query_vulnerabilities_combined() is True

    @pytest.mark.skipif(falcon.queryVulnerabilities(
                                                    parameters={"limit": 1,
                                                                "filter": "created_timestamp:>'2021-01-01T00:00:01Z'"
                                                                }
                                                    )["status_code"] == 429, reason="API rate limit reached")
    def test_getVulnerabilities(self):
        assert self.spotlight_getVulnerabilities() is True

    def test_Errors(self):
        assert self.spotlight_GenerateErrors() is True
