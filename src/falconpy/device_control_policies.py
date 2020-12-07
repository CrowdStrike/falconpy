################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# device_control_policies - Falcon X Device Control Policies API Interface Class.                              #
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
