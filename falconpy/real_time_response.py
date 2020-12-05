################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# real_time_response - Falcon X Real Time Response API Interface Class                                         #
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

class Real_Time_Response:
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

    def RTR_AggregateSessions(self, body):
        """ Get aggregates on session data. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_AggregateSessions
        FULL_URL = self.base_url+'/real-time-response/aggregates/sessions/GET/v1'
        HEADERS = self.headers
        DATA = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def BatchActiveResponderCmd(self, parameters, body):
        """ Batch executes a RTR active-responder command across the hosts mapped to the given batch ID. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        FULL_URL = self.base_url+'/real-time-response/combined/batch-active-responder-command/v1'
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

    def BatchCmd(self, parameters, body):
        """ Batch executes a RTR read-only command across the hosts mapped to the given batch ID. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        FULL_URL = self.base_url+'/real-time-response/combined/batch-command/v1'
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

    def BatchGetCmdStatus(self, parameters):
        """ Retrieves the status of the specified batch get command. Will return successful files when they are finished processing. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchGetCmdStatus
        FULL_URL = self.base_url+'/real-time-response/combined/batch-get-command/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def BatchGetCmd(self, parameters, body):
        """ Batch executes `get` command across hosts to retrieve files. 
            After this call is made `/real-time-response/combined/get-command-status/v1` is used to query for the results.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        FULL_URL = self.base_url+'/real-time-response/combined/batch-get-command/v1'
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

    def BatchInitSessions(self, parameters, body):
        """ Batch initialize a RTR session on multiple hosts. Before any RTR commands can be used, an active session is needed on the host. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchInitSessions
        FULL_URL = self.base_url+'/real-time-response/combined/batch-init-session/v1'
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

    def BatchRefreshSessions(self, parameters, body):
        """ Batch refresh a RTR session on multiple hosts. RTR sessions will expire after 10 minutes unless refreshed. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchRefreshSessions
        FULL_URL = self.base_url+'/real-time-response/combined/batch-refresh-session/v1'
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

    def RTR_CheckActiveResponderCommandStatus(self, parameters):
        """ Get status of an executed active-responder command on a single host. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_CheckActiveResponderCommandStatus
        FULL_URL = self.base_url+'/real-time-response/entities/active-responder-command/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_ExecuteActiveResponderCommand(self, body):
        """ Execute an active responder command on a single host. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchRefreshSessions
        FULL_URL = self.base_url+'/real-time-response/entities/active-responder-command/v1'
        HEADERS = self.headers
        DATA = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_CheckCommandStatus(self, parameters):
        """ Get status of an executed command on a single host. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_CheckCommandStatus
        FULL_URL = self.base_url+'/real-time-response/entities/command/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_ExecuteCommand(self, body):
        """ Execute a command on a single host. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ExecuteCommand
        FULL_URL = self.base_url+'/real-time-response/entities/command/v1'
        HEADERS = self.headers
        DATA = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_GetExtractedFileContents(self, parameters):
        """ Get RTR extracted file contents for specified session and sha256. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_GetExtractedFileContents
        FULL_URL = self.base_url+'/real-time-response/entities/extracted-file-contents/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_ListFiles(self, parameters):
        """ Get a list of files for the specified RTR session. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListFiles
        FULL_URL = self.base_url+'/real-time-response/entities/file/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_DeleteFile(self, parameters):
        """ Delete a RTR session file. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteFile
        FULL_URL = self.base_url+'/real-time-response/entities/file/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_PulseSession(self, body):
        """ Refresh a session timeout on a single host. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_PulseSession
        FULL_URL = self.base_url+'/real-time-response/entities/refresh-session/v1'
        HEADERS = self.headers
        DATA = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_ListSessions(self, body):
        """ Get session metadata by session id. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListSessions
        FULL_URL = self.base_url+'/real-time-response/entities/sessions/GET/v1'
        HEADERS = self.headers
        DATA = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def InitSessionMixin0(self, body):
        """ Initialize a new session with the RTR cloud. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/InitSessionMixin0
        FULL_URL = self.base_url+'/real-time-response/entities/sessions/v1'
        HEADERS = self.headers
        DATA = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_DeleteSession(self, parameters):
        """ Delete a session. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteSession
        FULL_URL = self.base_url+'/real-time-response/entities/sessions/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def RTR_ListAllSessions(self, parameters):
        """ Get a list of session_ids. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListAllSessions
        FULL_URL = self.base_url+'/real-time-response/queries/sessions/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned
