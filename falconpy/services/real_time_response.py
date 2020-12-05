################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# real_time_response - Falcon X Real Time Response API Interface Class                                         #
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
