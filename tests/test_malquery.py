# test_malquery.py
# This class tests the malquery service class
import os
import sys

# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.malquery import MalQuery as FalconMQ

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconMQ(creds={"client_id": auth.config["falcon_client_id"],
                         "client_secret": auth.config["falcon_client_secret"]
                         })
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestMalQuery:
    def serviceMQ_GetQuotas(self):
        returned = False
        if falcon.GetMalQueryQuotasV1()["status_code"] in AllowedResponses:
            returned = True

        return returned

    def serviceMQ_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["PostMalQueryFuzzySearchV1", "body={}"],
            ["GetMalQueryDownloadV1", "ids='12345678'"],
            ["GetMalQueryMetadataV1", "ids='12345678'"],
            ["GetMalQueryRequestV1", "ids='12345678'"],
            ["GetMalQueryEntitiesSamplesFetchV1", "ids='12345678'"],
            ["PostMalQueryEntitiesSamplesMultidownloadV1", "body={}"],
            ["PostMalQueryExactSearchV1", "body={}"],
            ["PostMalQueryHuntV1", "body={}"],

        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_GetQuotas(self):
        assert self.serviceMQ_GetQuotas() is True

    def test_Errors(self):
        assert self.serviceMQ_GenerateErrors() is True
