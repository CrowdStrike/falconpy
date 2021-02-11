################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# falconx_sandbox - Falcon X Sandbox API Interface Class                                                       #
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

class FalconX_Sandbox:
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """

    def __init__(self, access_token, base_url='https://api.crowdstrike.com', ssl_verify=True):
        """ Instantiates the base class, ingests the authorization token, 
            and initializes the headers and base_url global variables. 
        """
        self.headers = { 'Authorization': 'Bearer {}'.format(access_token) }
        self.base_url = base_url
        self.ssl_verify = ssl_verify

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

    def GetArtifacts(self, parameters): 
        """ Download IOC packs, PCAP files, and other analysis artifacts. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetArtifacts
        FULL_URL = self.base_url+'/falconx/entities/artifacts/v1'
        HEADERS = self.headers
        HEADERS['Accept-Encoding'] = 'gzip' #Force gzip compression
        PARAMS = parameters
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=self.ssl_verify)
            if response.headers.get('content-type') == "application/json":
                returned = self.Result()(response.status_code, response.headers, response.json())
            else:
                returned = response.content
        except Exception as e:
            returned = self.Result()(500, {}, str(e))

        return returned

    def GetSummaryReports(self, ids):
        """ Get a short summary version of a sandbox report. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSummaryReports
        ID_LIST = str(ids).replace(",","&ids=")
        FULL_URL = self.base_url+'/falconx/entities/report-summaries/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        try:
            response = requests.request("GET", FULL_URL, headers=HEADERS, verify=self.ssl_verify)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))

        return returned

    def GetSubmissions(self, ids):
        """ Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSubmissions
        ID_LIST = str(ids).replace(",","&ids=")
        FULL_URL = self.base_url+'/falconx/entities/submissions/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        try:
            response = requests.request("GET", FULL_URL, headers=HEADERS, verify=self.ssl_verify)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))

        return returned

    def Submit(self, body):
        """ Submit an uploaded file or a URL for sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/Submit
        FULL_URL = self.base_url+'/falconx/entities/submissions/v1'
        HEADERS = self.headers
        BODY = body
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=self.ssl_verify)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))

        return returned

    def QueryReports(self, parameters={}):
        """ Find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs that match your criteria. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QueryReports
        FULL_URL = self.base_url+'/falconx/queries/reports/v1'
        HEADERS = self.headers
        PARAMS = parameters
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=self.ssl_verify)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))

        return returned

    def QuerySubmissions(self, parameters={}):
        """ Find submission IDs for uploaded files by providing an FQL filter and paging details. 
            Returns a set of submission IDs that match your criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QuerySubmissions
        FULL_URL = self.base_url+'/falconx/queries/submissions/v1'
        HEADERS = self.headers
        PARAMS = parameters
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=self.ssl_verify)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))

        return returned

    def UploadSampleV2(self, parameters, body):
        """ Upload a file for sandbox analysis. After uploading, use `/falconx/entities/submissions/v1` to start analyzing the file. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/UploadSampleV2
        FULL_URL = self.base_url+'/samples/entities/samples/v2'
        HEADERS = self.headers
        HEADERS['Content-Type'] = 'application/octet-stream'
        BODY = body
        PARAMS = parameters
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, data=BODY, headers=HEADERS, verify=self.ssl_verify)
            returned = self.Result()(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = self.Result()(500, {}, str(e))

        return returned


# TODO: Missing methods - GetReports, DeleteReport, GetSampleV2, DeleteSampleV2, QuerySampleV1