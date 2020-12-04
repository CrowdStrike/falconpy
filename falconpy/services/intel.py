################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# oAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# intel - Falcon X Threat Intelligence API Interface Class                                                     #
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
