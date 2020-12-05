################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# sensor_update_policy - Falcon X Sensor Policy Management API Interface Class                                 #
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

class Sensor_Update_Policy:
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

    def revealUninstallToken(self, parameters, body):
        """ Reveals an uninstall token for a specific device. To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device_id'. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/revealUninstallToken
        FULL_URL = self.base_url+'/policy/combined/reveal-uninstall-token/v1'
        HEADERS = self.headers
        DATA = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned



    def queryCombinedSensorUpdateBuilds(self, parameters):
        """ Retrieve available builds for use with Sensor Update Policies. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/queryCombinedSensorUpdateBuilds
        FULL_URL = self.base_url+'/policy/combined/sensor-update-builds/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def queryCombinedSensorUpdatePolicyMembers(self, parameters):
        """ Search for members of a Sensor Update Policy in your environment by providing an FQL 
            filter and paging details. Returns a set of host details which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/queryCombinedSensorUpdatePolicyMembers
        FULL_URL = self.base_url+'/policy/combined/sensor-update-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def queryCombinedSensorUpdatePolicies(self, parameters):
        """ Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. 
            Returns a set of Sensor Update Policies which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/queryCombinedSensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/combined/sensor-update/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def queryCombinedSensorUpdatePoliciesV2(self, parameters):
        """ Search for Sensor Update Policies with additional support for uninstall protection in your environment 
            by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/queryCombinedSensorUpdatePoliciesV2
        FULL_URL = self.base_url+'/policy/combined/sensor-update/v2'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def performSensorUpdatePoliciesAction(self, parameters, body):
        """ Perform the specified action on the Sensor Update Policies specified in the request. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/performSensorUpdatePoliciesAction
        FULL_URL = self.base_url+'/policy/entities/sensor-update-actions/v1'
        HEADERS = self.headers
        DATA = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def setSensorUpdatePoliciesPrecedence(self, parameters, body):
        """ Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request. 
            The first ID specified will have the highest precedence and the last ID specified will have the lowest. 
            You must specify all non-Default Policies for a platform when updating precedence. 
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/setSensorUpdatePoliciesPrecedence
        FULL_URL = self.base_url+'/policy/entities/sensor-update-precedence/v1'
        HEADERS = self.headers
        DATA = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def getSensorUpdatePolicies(self, parameters):
        """ Retrieve a set of Sensor Update Policies by specifying their IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/getSensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def createSensorUpdatePolicies(self, parameters, body):
        """ Create Sensor Update Policies by specifying details about the policy to create. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/createSensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v1'
        HEADERS = self.headers
        DATA = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def deleteSensorUpdatePolicies(self, parameters):
        """ Delete a set of Sensor Update Policies by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/deleteSensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def updateSensorUpdatePolicies(self, parameters, body):
        """ Update Sensor Update Policies by specifying the ID of the policy and details to update. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/updateSensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v1'
        HEADERS = self.headers
        DATA = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("PATCH", FULL_URL, params=PARAMS, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def getSensorUpdatePoliciesV2(self, parameters):
        """ Retrieve a set of Sensor Update Policies with additional support for uninstall protection by specifying their IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/getSensorUpdatePoliciesV2
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v2'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def createSensorUpdatePoliciesV2(self, parameters, body):
        """ Create Sensor Update Policies by specifying details about the policy to create with additional support for uninstall protection. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/createSensorUpdatePoliciesV2
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v2'
        HEADERS = self.headers
        DATA = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def updateSensorUpdatePoliciesV2(self, parameters, body):
        """ Update Sensor Update Policies by specifying the ID of the policy and details to update with additional support for uninstall protection. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/updateSensorUpdatePoliciesV2
        FULL_URL = self.base_url+'/users/entities/users/v1'
        HEADERS = self.headers
        DATA = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("PATCH", FULL_URL, params=PARAMS, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def querySensorUpdatePolicyMembers(self, parameters):
        """ Search for members of a Sensor Update Policy in your environment by providing an FQL 
            filter and paging details. Returns a set of Agent IDs which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/querySensorUpdatePolicyMembers
        FULL_URL = self.base_url+'/policy/queries/sensor-update-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def querySensorUpdatePolicies(self, parameters):
        """ Search for Sensor Update Policies in your environment by providing an FQL filter and 
            paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/querySensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/queries/sensor-update/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned
