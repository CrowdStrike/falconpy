################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# intel - Falcon X Threat Intelligence API Interface Class                                                     #
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

class Intel:
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

    def QueryIntelActorEntities(self, parameters):
        """ Get info about actors that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorEntities
        FULL_URL = self.base_url+'/intel/combined/actors/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def QueryIntelIndicatorEntities(self, parameters):
        """ Get info about indicators that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorEntities
        FULL_URL = self.base_url+'/intel/combined/indicators/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def QueryIntelReportEntities(self, parameters):
        """ Get info about reports that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportEntities
        FULL_URL = self.base_url+'/intel/combined/reports/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetIntelActorEntities(self, parameters):
        """ Retrieve specific actors using their actor IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelActorEntities
        FULL_URL = self.base_url+'/intel/entities/actors/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetIntelIndicatorEntities(self, body):
        """ Retrieve specific indicators using their indicator IDs. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelIndicatorEntities
        FULL_URL = self.base_url+'/intel/entities/indicators/GET/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetIntelReportPDF(self, parameters):#Probably need to not do result.json() here. Check the swagger
        """ Return a Report PDF attachment. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportPDF
        FULL_URL = self.base_url+'/intel/entities/report-files/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetIntelReportEntities(self, parameters):
        """ Retrieve specific reports using their report IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportEntities
        FULL_URL = self.base_url+'/intel/entities/reports/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetIntelRuleFile(self, parameters):#There is an optional header you can see Accept to choose the result format. See Swagger.
        """ Download earlier rule sets. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleFile
        FULL_URL = self.base_url+'/intel/entities/rules-files/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetLatestIntelRuleFile(self, parameters):#There is an optional header you can see Accept to choose the result format. See Swagger.
        """ Download the latest rule set. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetLatestIntelRuleFile
        FULL_URL = self.base_url+'/intel/entities/rules-latest-files/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def GetIntelRuleEntities(self, parameters):
        """ Retrieve details for rule sets for the specified ids. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleEntities
        FULL_URL = self.base_url+'/intel/entities/rules/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def QueryIntelActorIds(self, parameters):
        """ Get actor IDs that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorIds
        FULL_URL = self.base_url+'/intel/queries/actors/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def QueryIntelIndicatorIds(self, parameters):
        """ Get indicators IDs that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorIds
        FULL_URL = self.base_url+'/intel/queries/indicators/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def QueryIntelReportIds(self, parameters):
        """ Get report IDs that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds
        FULL_URL = self.base_url+'/intel/queries/reports/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned

    def QueryIntelRuleIds(self, parameters):
        """ Search for rule IDs that match provided filter criteria. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds
        FULL_URL = self.base_url+'/intel/queries/rules/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))
        
        return returned
