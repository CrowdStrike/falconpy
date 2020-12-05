################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# device_control_policies - Falcon X Device Control Policies API Interface Class.                              #
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

class Device_Control_Policies:
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """

    def __init__(self, access_token, base_url='https://api.crowdstrike.com'):
        """ Instantiates the base class, ingests the authorization token, 
            and initializes the headers and base_url global variables. 
        """
        self.headers = { 'Authorization': 'Bearer {}'.format(access_token) }
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

    def queryCombinedDeviceControlPolicyMembers(self, parameters):
        """ Search for members of a Device Control Policy in your environment by providing an FQL filter 
            and paging details. Returns a set of host details which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/queryCombinedDeviceControlPolicyMembers
        FULL_URL = self.base_url+'/policy/combined/device-control-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def queryCombinedDeviceControlPolicies(self, parameters):
        """ Search for Device Control Policies in your environment by providing an FQL filter and 
            paging details. Returns a set of Device Control Policies which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/queryCombinedDeviceControlPolicies
        FULL_URL = self.base_url+'/policy/combined/device-control/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def performDeviceControlPoliciesAction(self, parameters, body):
        """ Search for Device Control Policies in your environment by providing an FQL filter 
            and paging details. Returns a set of Device Control Policies which match the filter criteria. 
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/performDeviceControlPoliciesAction
        FULL_URL = self.base_url+'/policy/combined/device-control/v1'
        HEADERS = self.headers
        BODY = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def setDeviceControlPoliciesPrecedence(self, body):
        """ Sets the precedence of Device Control Policies based on the order of IDs specified in the request. 
            The first ID specified will have the highest precedence and the last ID specified will have the lowest. 
            You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/performDeviceControlPoliciesAction
        FULL_URL = self.base_url+'/policy/entities/device-control-precedence/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def getDeviceControlPolicies(self, parameters):
        """ Retrieve a set of Device Control Policies by specifying their IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/getDeviceControlPolicies
        FULL_URL = self.base_url+'/policy/entities/device-control/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def createDeviceControlPolicies(self, body):
        """ Create Device Control Policies by specifying details about the policy to create. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/createDeviceControlPolicies
        FULL_URL = self.base_url+'/policy/entities/device-control/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def deleteDeviceControlPolicies(self, parameters):
        """ Delete a set of Device Control Policies by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/createDeviceControlPolicies
        FULL_URL = self.base_url+'/policy/entities/device-control/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def updateDeviceControlPolicies(self, body):
        """ Update Device Control Policies by specifying the ID of the policy and details to update. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/updateDeviceControlPolicies
        FULL_URL = self.base_url+'/policy/entities/device-control/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("PATCH", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def queryDeviceControlPolicyMembers(self, parameters):
        """ Search for members of a Device Control Policy in your environment by providing an FQL filter
            and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/queryDeviceControlPolicyMembers
        FULL_URL = self.base_url+'/policy/queries/device-control-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def queryDeviceControlPolicies(self, parameters):
        """ Search for Device Control Policies in your environment by providing an FQL filter and paging details. 
            Returns a set of Device Control Policy IDs which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies/queryDeviceControlPolicyMembers
        FULL_URL = self.base_url+'/policy/queries/device-control/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned
