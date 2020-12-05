################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# user_management - Falcon X User Management API Interface Class                                               #
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

class User_Management:
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

    def GetRoles(self, parameters):
        """ Get info about a role. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetRoles
        FULL_URL = self.base_url+'/user-roles/entities/user-roles/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GrantUserRoleIds(self, parameters, body):
        """ Assign one or more roles to a user. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GrantUserRoleIds
        FULL_URL = self.base_url+'/user-roles/entities/user-roles/v1'
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

    def RevokeUserRoleIds(self, parameters):
        """ Revoke one or more roles from a user. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RevokeUserRoleIds
        FULL_URL = self.base_url+'/user-roles/entities/user-roles/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetAvailableRoleIds(self):
        """ Show role IDs for all roles available in your customer account. 
            For more information on each role, provide the role ID to `/customer/entities/roles/v1`. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetAvailableRoleIds
        FULL_URL = self.base_url+'/user-roles/queries/user-role-ids-by-cid/v1'
        HEADERS = self.headers
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetUserRoleIds(self, parameters):
        """ Show role IDs of roles assigned to a user. For more information on each role, provide the role ID to `/customer/entities/roles/v1`. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetUserRoleIds
        FULL_URL = self.base_url+'/user-roles/queries/user-role-ids-by-user-uuid/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RetrieveUser(self, parameters):
        """ Get info about a user. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUser
        FULL_URL = self.base_url+'/users/entities/users/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def CreateUser(self, parameters, body):
        """ Create a new user. After creating a user, assign one or more roles with POST /user-roles/entities/user-roles/v1. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/CreateUser
        FULL_URL = self.base_url+'/users/entities/users/v1'
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

    def DeleteUser(self, parameters):
        """ Delete a user permanently. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/DeleteUser
        FULL_URL = self.base_url+'/users/entities/users/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def UpdateUser(self, parameters, body):
        """ Modify an existing user. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/UpdateUser
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

    def RetrieveEmailsByCID(self):
        """ List the usernames (usually an email address) for all users in your customer account. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveEmailsByCID
        FULL_URL = self.base_url+'/users/queries/emails-by-cid/v1'
        HEADERS = self.headers
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RetrieveUserUUIDsByCID(self):
        """ List user IDs for all users in your customer account. For more information on each user, provide the user ID to `/users/entities/user/v1`."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUserUUIDsByCID
        FULL_URL = self.base_url+'/users/queries/user-uuids-by-cid/v1'
        HEADERS = self.headers
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RetrieveUserUUID(self, parameters):
        """ Get a user's ID by providing a username (usually an email address). """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUserUUID
        FULL_URL = self.base_url+'/users/queries/user-uuids-by-email/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned
