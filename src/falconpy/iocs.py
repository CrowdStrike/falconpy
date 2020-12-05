################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# iocs - Falcon X Indicators of Compromise API Interface Class                                                 #
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

class Iocs:
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

    def DevicesCount(self, parameters):
        """ Number of hosts in your customer account that have observed a given custom IOC. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesCount
        FULL_URL = self.base_url+'/indicators/aggregates/devices-count/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetIOC(self, parameters):
        """ Get an IOC by providing a type and value. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/GetIOC
        FULL_URL = self.base_url+'/indicators/entities/iocs/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def CreateIOC(self, body):
        """ Create a new IOC. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/CreateIOC
        FULL_URL = self.base_url+'/indicators/entities/iocs/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def DeleteIOC(self, parameters):
        """ Delete an IOC by providing a type and value. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DeleteIOC
        FULL_URL = self.base_url+'/indicators/entities/iocs/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def UpdateIOC(self, parameters, body):
        """ Update an IOC by providing a type and value. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/UpdateIOC
        FULL_URL = self.base_url+'/indicators/entities/iocs/v1'
        HEADERS = self.headers
        PARAMS = parameters
        BODY = body
        result = self.Result()
        try:
            response = requests.request("PATCH", FULL_URL, params=PARAMS, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def DevicesRanOn(self, parameters):
        """ Find hosts that have observed a given custom IOC. For details about those hosts, use the hosts API interface. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesRanOn
        FULL_URL = self.base_url+'/indicators/queries/devices/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def QueryIOCs(self, parameters):
        """ Search the custom IOCs in your customer account. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/QueryIOCs
        FULL_URL = self.base_url+'/indicators/queries/iocs/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def ProcessesRanOn(self, parameters):
        """ Search for processes associated with a custom IOC. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/QueryIOCs
        FULL_URL = self.base_url+'/indicators/queries/processes/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def entities_processes(self, parameters):
        """ For the provided ProcessID retrieve the process details. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/entities_processes
        FULL_URL = self.base_url+'/processes/entities/processes/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned
