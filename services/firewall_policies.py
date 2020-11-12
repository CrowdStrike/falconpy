################################################################################################################
# CROWDSTRIKE FALCON COMPLETE                                                                                  #
# oAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# firewall_policies - Falcon X Firewall Policies API Interface Class.                                          #
################################################################################################################
import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class Firewall_Policies:
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

    def queryCombinedFirewallPolicyMembers(self, parameters):
        """ Search for members of a Firewall Policy in your environment by providing an FQL filter 
            and paging details. Returns a set of host details which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/queryCombinedFirewallPolicyMembers
        FULL_URL = self.base_url+'/policy/combined/firewall-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def queryCombinedFirewallPolicies(self, parameters):
        """ Search for Firewall Policies in your environment by providing an FQL filter and paging details. 
            Returns a set of Firewall Policies which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/queryCombinedFirewallPolicies
        FULL_URL = self.base_url+'/policy/combined/firewall/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def performFirewallPoliciesAction(self, parameters, body):
        """ Perform the specified action on the Firewall Policies specified in the request. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/performFirewallPoliciesAction
        FULL_URL = self.base_url+'/policy/entities/firewall-actions/v1'
        HEADERS = self.headers
        BODY = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def setFirewallPoliciesPrecedence(self, body):
        """ Sets the precedence of Firewall Policies based on the order of IDs specified in the request. 
            The first ID specified will have the highest precedence and the last ID specified will have the lowest. 
            You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/setFirewallPoliciesPrecedence
        FULL_URL = self.base_url+'/policy/entities/firewall-precedence/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def getFirewallPolicies(self, parameters):
        """ Retrieve a set of Firewall Policies by specifying their IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/getFirewallPolicies
        FULL_URL = self.base_url+'/policy/entities/firewall/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def createFirewallPolicies(self, parameters, body):
        """ Create Firewall Policies by specifying details about the policy to create. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/createFirewallPolicies
        FULL_URL = self.base_url+'/policy/entities/firewall/v1'
        HEADERS = self.headers
        PARAMS = parameters
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def deleteFirewallPolicies(self, parameters):
        """ Delete a set of Firewall Policies by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/deleteFirewallPolicies
        FULL_URL = self.base_url+'/policy/entities/firewall/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def updateFirewallPolicies(self, body):
        """ Update Firewall Policies by specifying the ID of the policy and details to update. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/updateFirewallPolicies
        FULL_URL = self.base_url+'/policy/entities/firewall/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("PATCH", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def queryFirewallPolicyMembers(self, parameters):
        """ Search for members of a Firewall Policy in your environment by providing an FQL filter and 
            paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/queryFirewallPolicyMembers
        FULL_URL = self.base_url+'/policy/queries/firewall-members/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def queryFirewallPolicies(self, parameters):
        """ Search for Firewall Policies in your environment by providing an FQL filter and paging details.
            Returns a set of Firewall Policy IDs which match the filter criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/queryFirewallPolicies
        FULL_URL = self.base_url+'/policy/queries/firewall/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned
