# A valid CrowdStrike Falcon API key is required to run these tests. 
# API client ID & secret should be stored in tests/test.config in JSON format.
# {
#    "falcon_client_id": "CLIENT_ID_GOES_HERE",
#    "falcon_client_secret": "CLIENT_SECRET_GOES_HERE"
# }
import json
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

#Import our sibling src folder into the path
sys.path.append(os.path.abspath('../src'))
# Classes to test - manually imported from sibling folder
from falconpy import cloud_connect_aws as FalconAWS


# The TestCloudConnectAWS class tests the cloud_connect_aws service class
class TestCloudConnectAWS:
    def serviceCCAWS_GetAWSSettings(self):
        auth = Authorization.TestAuthorization()
        auth.serviceAuth()
        falcon = FalconAWS.Cloud_Connect_AWS(access_token=auth.token)
        if falcon.GetAWSSettings()["status_code"] > 0:
            auth.serviceRevoke()
            return True
        else:
            auth.serviceRevoke()
            return False      

    def test_GetAWSSettings(self):
        assert self.serviceCCAWS_GetAWSSettings() == True
