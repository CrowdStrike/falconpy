################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# cloud_connect_aws - Falcon X Discover API Interface Class                                                    #
################################################################################################################
# Copyright CrowdStrike 2020

# By accessing or using this script, sample code, application programming interface, tools, 
# and/or associated documentation (if any) (collectively, “Tools”), You (i) represent and 
# warrant that You are entering into this Agreement on behalf of a company, organization 
# or another legal entity (“Entity”) that is currently a customer or partner of 
# CrowdStrike, Inc. (“CrowdStrike”), and (ii) have the authority to bind such Entity and 
# such Entity agrees to be bound by this Agreement.

# CrowdStrike grants Entity a non-exclusive, non-transferable, non-sublicensable, royalty 
# free and limited license to access and use the Tools solely for Entity’s internal business 
# purposes and in accordance with its obligations under any agreement(s) it may have with 
# CrowdStrike. Entity acknowledges and agrees that CrowdStrike and its licensors retain all 
# right, title and interest in and to the Tools, and all intellectual property rights 
# embodied therein, and that Entity has no right, title or interest therein except for the 
# express licenses granted hereunder and that Entity will treat such Tools as CrowdStrike’s 
# confidential information.

# THE TOOLS ARE PROVIDED “AS-IS” WITHOUT WARRANTY OF ANY KIND, WHETHER EXPRESS, IMPLIED OR 
# STATUTORY OR OTHERWISE. CROWDSTRIKE SPECIFICALLY DISCLAIMS ALL SUPPORT OBLIGATIONS AND 
# ALL WARRANTIES, INCLUDING WITHOUT LIMITATION, ALL IMPLIED WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT. IN NO EVENT SHALL CROWDSTRIKE 
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THE TOOLS, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
