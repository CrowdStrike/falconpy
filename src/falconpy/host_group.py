################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# host_groups - Falcon X Host Groups API Interface Class                                                       #
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

class Host_Group:
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

    def queryCombinedGroupMembers(self, parameters):
        """ Search for members of a Host Group in your environment by providing an FQL filter 
            and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryCombinedGroupMembers
        FULL_URL = self.base_url+'/devices/combined/host-group-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def queryCombinedHostGroups(self, parameters):
        """ Search for Host Groups in your environment by providing an FQL filter and 
            paging details. Returns a set of Host Groups which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryCombinedHostGroups
        FULL_URL = self.base_url+'/devices/combined/host-groups/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def performGroupAction(self, parameters, body):
        """ Perform the specified action on the Host Groups specified in the request. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/performGroupAction
        FULL_URL = self.base_url+'/devices/entities/host-group-actions/v1'
        HEADERS = self.headers
        PARAMS = parameters
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def getHostGroups(self, parameters):
        """ Retrieve a set of Host Groups by specifying their IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/getHostGroups
        FULL_URL = self.base_url+'/devices/entities/host-groups/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def createHostGroups(self, body):
        """ Create Host Groups by specifying details about the group to create. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/createHostGroups
        FULL_URL = self.base_url+'/devices/entities/host-groups/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
            
        return returned
        
    def deleteHostGroups(self, parameters):
        """ Delete a set of Host Groups by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/deleteHostGroups
        FULL_URL = self.base_url+'/devices/entities/host-groups/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        return returned
        
    def updateHostGroups(self, body):
        """ Update Host Groups by specifying the ID of the group and details to update. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/updateHostGroups
        FULL_URL = self.base_url+'/devices/entities/host-groups/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("PATCH", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
            
        return returned
        
    def queryGroupMembers(self, parameters):
        """ Search for members of a Host Group in your environment by providing an FQL filter 
            and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryGroupMembers
        FULL_URL = self.base_url+'/devices/queries/host-group-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
            
        return returned
        
    def queryHostGroups(self, parameters):
        """ Search for Host Groups in your environment by providing an FQL filter and 
            paging details. Returns a set of Host Group IDs which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryHostGroups
        FULL_URL = self.base_url+'/devices/queries/host-groups/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
            
        return returned