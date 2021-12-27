# test_iocs.py
# This class tests the iocs service class

import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Iocs

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Iocs(auth_object=config)
AllowedResponses = [200, 429, 500] # Half of the class is deprecated, allow 500

class TestIOCs:
    def serviceIOCs_QueryIOCs(self):
        if falcon.QueryIOCs()["status_code"] in AllowedResponses:
            return True
        else:
            return False

    
    def serviceIOCs_GetIOC(self):
        
        if falcon.GetIOC(parameters={"type":"ipv4", "value":falcon.QueryIOCs(parameters={"types":"ipv4"})["body"]["resources"][0]})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIOCs_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["DevicesCount","parameters={}"],
            ["GetIOC","parameters={}"],
            ["CreateIOC","body={}"],
            ["DeleteIOC","parameters={}"],
            ["UpdateIOC","body={}, parameters={}"],
            ["DevicesRanOn","parameters={}"],
            ["QueryIOCs",""],
            ["ProcessesRanOn","parameters={}"],
            ["entities_processes","ids='12345678'"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0],cmd[1])) != 500:
                errorChecks = False
        
        return errorChecks

    def test_QueryIOCs(self):
        assert self.serviceIOCs_QueryIOCs() == True

    # Current test environment doesn't have any custom IOCs configured atm
    #@pytest.mark.skipif(falcon.QueryIOCs(parameters={"types":"ipv4"})["status_code"] == 429, reason="API rate limit reached")
    # def test_GetIOC(self):
    #     assert self.serviceIOCs_GetIOC() == True


    def test_Errors(self):
        assert self.serviceIOCs_GenerateErrors() == True