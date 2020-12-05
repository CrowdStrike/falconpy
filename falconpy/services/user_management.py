################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# user_management - Falcon X User Management API Interface Class                                               #
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
