################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# oAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# firewall_management - Falcon X Firewall Management API Interface Class                                       #
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
