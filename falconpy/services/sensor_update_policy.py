################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# oAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# sensor_update_policy - Falcon X Sensor Policy Management API Interface Class                                 #
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
