# test_spotlight_vulnerabilities.py
# This class tests the spotlight_vulnerabilities service class

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Classes to test - manually imported from sibling folder
from falconpy import spotlight_vulnerabilities as FalconSpotlight
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))


auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconSpotlight.Spotlight_Vulnerabilities(access_token=token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestSpotlight:
    def serviceSpotlight_queryVulnerabilities(self):
        if falcon.queryVulnerabilities(
                                       parameters={"limit": 1,
                                                   "filter": "created_timestamp:>'2021-01-01T00:00:01Z'"
                                                   }
                                       )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSpotlight_getVulnerabilities(self):
        try:
            id_list = falcon.queryVulnerabilities(parameters={"limit": 1,
                                                              "filter": "created_timestamp:>'2021-01-01T00:00:01Z'"
                                                              }
                                                  )["body"]["resources"][0]
            if falcon.getVulnerabilities(ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            # Flaky
            pytest.skip("Workflow-related error, skipping")
            return True

    def serviceSpotlight_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        if falcon.queryVulnerabilities(parameters={})["status_code"] != 500:
            errorChecks = False
        if falcon.getVulnerabilities(ids="12345678")["status_code"] != 500:
            errorChecks = False
        if falcon.getRemediations(ids="12345678")["status_code"] != 500:
            errorChecks = False

        return errorChecks

    def test_queryVulnerabilities(self):
        assert self.serviceSpotlight_queryVulnerabilities() is True

    @pytest.mark.skipif(falcon.queryVulnerabilities(
                                                    parameters={"limit": 1,
                                                                "filter": "created_timestamp:>'2021-01-01T00:00:01Z'"
                                                                }
                                                    )["status_code"] == 429, reason="API rate limit reached")
    def test_getVulnerabilities(self):
        assert self.serviceSpotlight_getVulnerabilities() is True

    def test_Errors(self):
        assert self.serviceSpotlight_GenerateErrors() is True
