################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# firewall_management - Falcon X Firewall Management API Interface Class                                       #
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

class Firewall_Management:
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

    def aggregate_events(self, body):
        """ Aggregate events for customer. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_events
        FULL_URL = self.base_url+'/fwmgr/aggregates/events/GET/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def aggregate_policy_rules(self, body):
        """ Aggregate rules within a policy for customer. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_policy_rules
        FULL_URL = self.base_url+'/fwmgr/aggregates/policy-rules/GET/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def aggregate_rule_groups(self, body):
        """ Aggregate rule groups for customer. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rule_groups
        FULL_URL = self.base_url+'/fwmgr/aggregates/rule-groups/GET/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def aggregate_rules(self, body):
        """ Aggregate rules for customer. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rules
        FULL_URL = self.base_url+'/fwmgr/aggregates/rules/GET/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def get_events(self, parameters):
        """ Get events entities by ID and optionally version. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_events
        FULL_URL = self.base_url+'/fwmgr/entities/events/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def get_firewall_fields(self, parameters):
        """ Get the firewall field specifications by ID. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_firewall_fields
        FULL_URL = self.base_url+'/fwmgr/entities/firewall-fields/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def get_platforms(self, parameters):
        """ Get platforms by ID, e.g., windows or mac or droid. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_platforms
        FULL_URL = self.base_url+'/fwmgr/entities/platforms/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def get_policy_containers(self, parameters):
        """ Get policy container entities by policy ID. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_policy_containers
        FULL_URL = self.base_url+'/fwmgr/entities/policies/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def update_policy_container(self, body, cs_username):
        """ Update an identified policy container. """
        # [PUT] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update_policy_container
        FULL_URL = self.base_url+'/fwmgr/entities/policies/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        BODY = body
        result = self.Result()
        try:
            response = requests.request("PUT", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def get_rule_groups(self, parameters):
        """ Get rule group entities by ID. These groups do not contain their rule entites, just the rule IDs in precedence order. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rule_groups
        FULL_URL = self.base_url+'/fwmgr/entities/rule-groups/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def create_rule_group(self, parameters, body, cs_username):
        """ Create new rule group on a platform for a customer with a name and description, and return the ID. """ 
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/create_rule_group
        FULL_URL = self.base_url+'/fwmgr/entities/rule-groups/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        PARAMS = parameters
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def delete_rule_groups(self, parameters, cs_username):
        """ Delete rule group entities by ID. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QueryReports
        FULL_URL = self.base_url+'/fwmgr/entities/rule-groups/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("DELETE", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def update_rule_group(self, parameters, cs_username):
        """ Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update_rule_group
        FULL_URL = self.base_url+'/fwmgr/entities/rule-groups/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("PTACH", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def get_rules(self, parameters):
        """ Get rule entities by ID (64-bit unsigned int as decimal string) or Family ID (32-character hexadecimal string). """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rules
        FULL_URL = self.base_url+'/fwmgr/entities/rules/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def query_events(self, parameters):
        """ Find all event IDs matching the query with filter. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_events
        FULL_URL = self.base_url+'/fwmgr/queries/events/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def query_firewall_fields(self, parameters):
        """ Get the firewall field specification IDs for the provided platform. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_firewall_fields
        FULL_URL = self.base_url+'/fwmgr/queries/firewall-fields/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def query_platforms(self, parameters):
        """ Get the list of platform names. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_platforms
        FULL_URL = self.base_url+'/fwmgr/queries/platforms/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def query_policy_rules(self, parameters):
        """ Find all firewall rule IDs matching the query with filter, and return them in precedence order. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_policy_rules
        FULL_URL = self.base_url+'/fwmgr/queries/policy-rules/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def query_rule_groups(self, parameters):
        """ Find all rule group IDs matching the query with filter. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups
        FULL_URL = self.base_url+'/fwmgr/queries/rule-groups/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def query_rules(self, parameters):
        """ Find all rule IDs matching the query with filter. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups
        FULL_URL = self.base_url+'/fwmgr/queries/rules/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned
