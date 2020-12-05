################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# real_time_response_admin - Falcon X Real Time Response Administration API Interface Class                    #
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

class Real_Time_Response_Admin:
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

    def BatchAdminCmd(self, parameters, body):
        """ Batch executes a RTR administrator command across the hosts mapped to the given batch ID. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/BatchAdminCmd
        FULL_URL = self.base_url+'/real-time-response/combined/batch-admin-command/v1'
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

    def RTR_CheckAdminCommandStatus(self, parameters):
        """ Get status of an executed RTR administrator command on a single host. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_CheckAdminCommandStatus
        FULL_URL = self.base_url+'/real-time-response/entities/admin-command/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_ExecuteAdminCommand(self, body):
        """ Execute a RTR administrator command on a single host. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_ExecuteAdminCommand
        FULL_URL = self.base_url+'/real-time-response/entities/admin-command/v1'
        HEADERS = self.headers
        DATA = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_GetPut_Files(self, parameters):
        """ Get put-files based on the ID's given. These are used for the RTR `put` command. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_GetPut_Files
        FULL_URL = self.base_url+'/real-time-response/entities/put-files/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_CreatePut_Files(self, data, files):
        """ Upload a new put-file to use for the RTR `put` command. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_CreatePut_Files
        FULL_URL = self.base_url+'/real-time-response/entities/put-files/v1'
        HEADERS = self.headers
        DATA = data
        FILES = files
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, data=DATA, files=FILES, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_DeletePut_Files(self, parameters):
        """ Delete a put-file based on the ID given. Can only delete one file at a time. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_DeletePut_Files
        FULL_URL = self.base_url+'/real-time-response/entities/put-files/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_GetScripts(self, parameters):
        """ Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_GetScripts
        FULL_URL = self.base_url+'/real-time-response/entities/scripts/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_CreateScripts(self, data, files):
        """ Upload a new custom-script to use for the RTR `runscript` command. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_CreateScripts
        FULL_URL = self.base_url+'/real-time-response/entities/scripts/v1'
        HEADERS = self.headers
        DATA = data
        FILES = files
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, data=DATA, files=FILES, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_DeleteScripts(self, parameters):
        """ Delete a custom-script based on the ID given. Can only delete one script at a time. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_DeleteScripts
        FULL_URL = self.base_url+'/real-time-response/entities/scripts/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_UpdateScripts(self, data, files):
        """ Upload a new scripts to replace an existing one. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_UpdateScripts
        FULL_URL = self.base_url+'/real-time-response/entities/scripts/v1'
        HEADERS = self.headers
        DATA = data
        FILES = files
        result = self.Result()
        try:
            response = requests.request("PATCH", FULL_URL, data=DATA, files=FILES, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_ListPut_Files(self, parameters):
        """ Get a list of put-file ID's that are available to the user for the `put` command. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_ListPut_Files
        FULL_URL = self.base_url+'/real-time-response/queries/put-files/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_ListScripts(self, parameters):
        """ Get a list of custom-script ID's that are available to the user for the `runscript` command. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_ListScripts
        FULL_URL = self.base_url+'/real-time-response/queries/scripts/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned
