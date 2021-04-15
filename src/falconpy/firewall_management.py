"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

firewall_management - CrowdStrike Falcon Firewall Management API interface class

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
from ._util import parse_id_list, service_request
from ._service_class import ServiceClass


class Firewall_Management(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def aggregate_events(self: object, body: dict) -> dict:
        """ Aggregate events for customer. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_events
        FULL_URL = self.base_url+'/fwmgr/aggregates/events/GET/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def aggregate_policy_rules(self: object, body: dict) -> dict:
        """ Aggregate rules within a policy for customer. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_policy_rules
        FULL_URL = self.base_url+'/fwmgr/aggregates/policy-rules/GET/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def aggregate_rule_groups(self: object, body: dict) -> dict:
        """ Aggregate rule groups for customer. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rule_groups
        FULL_URL = self.base_url+'/fwmgr/aggregates/rule-groups/GET/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def aggregate_rules(self: object, body: dict) -> dict:
        """ Aggregate rules for customer. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rules
        FULL_URL = self.base_url+'/fwmgr/aggregates/rules/GET/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_events(self: object, ids) -> dict:
        """ Get events entities by ID and optionally version. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_events
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/fwmgr/entities/events/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_firewall_fields(self: object, ids) -> dict:
        """ Get the firewall field specifications by ID. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_firewall_fields
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/fwmgr/entities/firewall-fields/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_platforms(self: object, ids) -> dict:
        """ Get platforms by ID, e.g., windows or mac or droid. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_platforms
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/fwmgr/entities/platforms/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_policy_containers(self: object, ids) -> dict:
        """ Get policy container entities by policy ID. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_policy_containers
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/fwmgr/entities/policies/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    # TODO: Update dynamic documentation to handle the cs_username parameter
    def update_policy_container(self: object, body: dict, cs_username: str) -> dict:
        """ Update an identified policy container. """
        # [PUT] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update_policy_container
        FULL_URL = self.base_url+'/fwmgr/entities/policies/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        BODY = body
        returned = service_request(caller=self,
                                   method="PUT",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_rule_groups(self: object, ids) -> dict:
        """ Get rule group entities by ID. These groups do not contain their rule entites,
            just the rule IDs in precedence order.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rule_groups
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/fwmgr/entities/rule-groups/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def create_rule_group(self: object, body: dict, cs_username: str, parameters: dict = None) -> dict:
        """ Create new rule group on a platform for a customer with a name and description, and return the ID. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/create_rule_group
        FULL_URL = self.base_url+'/fwmgr/entities/rule-groups/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def delete_rule_groups(self: object, ids, cs_username: str, parameters: dict = None) -> dict:
        """ Delete rule group entities by ID. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QueryReports
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/fwmgr/entities/rule-groups/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def update_rule_group(self: object, body: dict, cs_username: str, parameters: dict = None) -> dict:
        """ Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update_rule_group
        FULL_URL = self.base_url+'/fwmgr/entities/rule-groups/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_rules(self: object, ids) -> dict:
        """ Get rule entities by ID (64-bit unsigned int as decimal string) or Family ID (32-character hexadecimal string). """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rules
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/fwmgr/entities/rules/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_events(self: object, parameters: dict = None) -> dict:
        """ Find all event IDs matching the query with filter. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_events
        FULL_URL = self.base_url+'/fwmgr/queries/events/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_firewall_fields(self: object, parameters: dict = None) -> dict:
        """ Get the firewall field specification IDs for the provided platform. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_firewall_fields
        FULL_URL = self.base_url+'/fwmgr/queries/firewall-fields/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_platforms(self: object, parameters: dict = None) -> dict:
        """ Get the list of platform names. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_platforms
        FULL_URL = self.base_url+'/fwmgr/queries/platforms/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_policy_rules(self: object, parameters: dict = None) -> dict:
        """ Find all firewall rule IDs matching the query with filter, and return them in precedence order. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_policy_rules
        FULL_URL = self.base_url+'/fwmgr/queries/policy-rules/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_rule_groups(self: object, parameters: dict = None) -> dict:
        """ Find all rule group IDs matching the query with filter. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups
        FULL_URL = self.base_url+'/fwmgr/queries/rule-groups/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_rules(self: object, parameters: dict = None) -> dict:
        """ Find all rule IDs matching the query with filter. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups
        FULL_URL = self.base_url+'/fwmgr/queries/rules/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned
