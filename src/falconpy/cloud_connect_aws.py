################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# cloud_connect_aws - Falcon X Discover API Interface Class                                                    #
################################################################################################################
# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>

import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class Cloud_Connect_AWS:
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """

    def __init__(self, access_token, base_url="https://api.crowdstrike.com"):
        """ Instantiates the base class, ingests the authorization token, 
            and initializes the headers and base_url global variables. 
        """
        self.headers = {'Authorization': 'Bearer {}'.format(access_token)}
        self.base_url = base_url

    class Result:
        """ Subclass to handle parsing of result client output. """
        def __init__(self):
            """ Instantiates the subclass and initializes the result object. """
            self.result_obj = {}
            
        def __call__(self, status_code, headers, body):
            """ Formats values into a properly formatted result object. """
            self.result_obj['status_code'] = status_code
            self.result_obj['headers'] = dict(headers)
            self.result_obj['body'] = body
            
            return self.result_obj

    def QueryAWSAccounts(self, parameters):
        """ Search for provisioned AWS Accounts by providing an FQL filter and paging details. 
            Returns a set of AWS accounts which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/QueryAWSAccounts 
        FULL_URL = self.base_url+'/cloud-connect-aws/combined/accounts/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetAWSSettings(self):
        """ Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/GetAWSSettings
        FULL_URL = self.base_url+'/cloud-connect-aws/combined/settings/v1'
        HEADERS = self.headers
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
            
        return returned

    def GetAWSAccounts(self, parameters, ids):
        """ Retrieve a set of AWS Accounts by specifying their IDs."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/GetAWSAccounts
        ID_LIST = str(ids).replace(",","&ids=")
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/accounts/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned
        
    def ProvisionAWSAccounts(self, parameters, body):
        """ Provision AWS Accounts by specifying details about the accounts to provision. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/ProvisionAWSAccounts
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/accounts/v1'
        PARAMS=parameters
        BODY=body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=BODY, headers=self.headers, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned
        
    def DeleteAWSAccounts(self, parameters, ids):
        """ Delete a set of AWS Accounts by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/DeleteAWSAccounts
        ID_LIST = str(ids).replace(",","&ids=")
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/accounts/v1?ids={}'.format(ID_LIST)
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=self.headers, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def UpdateAWSAccounts(self, body):
        """ Update AWS Accounts by specifying the ID of the account and details to update. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/UpdateAWSAccounts
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/accounts/v1'
        BODY=body
        result = self.Result()
        try:
            response = requests.request("PATCH", FULL_URL, json=BODY, headers=self.headers, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def CreateOrUpdateAWSSettings(self, body):
        """ Create or update Global Settings which are applicable to all provisioned AWS accounts. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/CreateOrUpdateAWSSettings
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/settings/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
            
        return returned

    def VerifyAWSAccountAccess(self, parameters, body, ids):
        """ Performs an Access Verification check on the specified AWS Account IDs. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/VerifyAWSAccountAccess
        ID_LIST = str(ids).replace(",","&ids=")
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/verify-account-access/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        PARAMS = parameters
        BODY = body  #payload does not appear to be required
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def QueryAWSAccountsForIDs(self, parameters):
        """ Search for provisioned AWS Accounts by providing an FQL filter and paging details. 
            Returns a set of AWS account IDs which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/QueryAWSAccountsForIDs
        FULL_URL = self.base_url+'/cloud-connect-aws/queries/accounts/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
            
        return returned
