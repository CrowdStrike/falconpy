################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# real_time_response_admin - Falcon X Real Time Response Administration API Interface Class                    #
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
