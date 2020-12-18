# A valid CrowdStrike Falcon API key is required to run these tests. 
# API client ID & secret should be stored in tests/test.config in JSON format.
# {
#    "falcon_client_id": "CLIENT_ID_GOES_HERE",
#    "falcon_client_secret": "CLIENT_SECRET_GOES_HERE"
# }
import json
import os
import sys
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('./src'))
# Classes to test - manually imported from our sibling folder
import falconpy.api_complete as FalconSDK
import falconpy.oauth2 as FalconAuth
import falconpy.cloud_connect_aws as FalconAWS

# The TestAuthorization class tests authentication and deauthentication
# for both the Uber and Service classes.
class TestAuthorization():
    def getConfig(self):
        #Grab our config parameters
        try:
            self.config = {}
            self.config["falcon_client_id"] = os.getenv("DEBUG_API_ID")
            self.config["falcon_client_secret"] = os.getenv("DEBUG_API_SECRET")
        except:
            with open('%s/test.config' % os.path.dirname(os.path.abspath(__file__)), 'r') as file_config:
                self.config = json.loads(file_config.read())

    def uberAuth(self):
        self.getConfig()       
        self.falcon = FalconSDK.APIHarness(creds={
                "client_id": self.config["falcon_client_id"],
                "client_secret": self.config["falcon_client_secret"]
            }
        )
        self.falcon.authenticate()
        if self.falcon.authenticated:
            return True
        else:
            return False

    def uberRevoke(self):
        return self.falcon.deauthenticate()

    def serviceAuth(self):
        self.getConfig()
        self.authorization = FalconAuth.OAuth2(creds={
            'client_id': self.config["falcon_client_id"],
            'client_secret': self.config["falcon_client_secret"]
        })

        try:
            self.token = self.authorization.token()['body']['access_token']
            
        except:
            self.token = False
        
        if self.token:
            return True
        else:
            return False

    def serviceRevoke(self):
        try:
            result = self.authorization.revoke(token=self.token)["status_code"]
            if result > 0:
                return True
            else:
                return False
        except:
            return False
        
    def test_uberAuth(self):
        assert self.uberAuth() == True
        self.uberRevoke()
    
    def test_uberRevoke(self):
        self.uberAuth()
        assert self.uberRevoke() == True

    def test_serviceAuth(self):
        assert self.serviceAuth() == True
        self.serviceRevoke()

    def test_serviceRevoke(self):
        self.serviceAuth()
        assert self.serviceRevoke() == True



