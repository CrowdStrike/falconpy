################################################################################################################
# CROWDSTRIKE FALCON COMPLETE                                                                                  #
# oAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# spotlight_vulnerabilities - Falcon X Spotlight Vulnerabilities API Interface Class                           #
################################################################################################################
import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class Spotlight_Vulnerabilities:
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

    def getVulnerabilities(self, parameters):
        """ Get details on vulnerabilities by providing one or more IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/spotlight-vulnerabilities/getVulnerabilities
        FULL_URL = self.base_url+'/spotlight/entities/vulnerabilities/v2'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def queryVulnerabilities(self, parameters):
        """ Search for Vulnerabilities in your environment by providing an FQL filter 
            and paging details. Returns a set of Vulnerability IDs which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/spotlight-vulnerabilities/queryVulnerabilities
        FULL_URL = self.base_url+'/spotlight/queries/vulnerabilities/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned
