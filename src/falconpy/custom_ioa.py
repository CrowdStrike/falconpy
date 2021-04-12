"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

custom_ioa - Falcon Custom Indicators of Attack API Interface Class

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
from ._util import service_request, parse_id_list
from ._service_class import ServiceClass


class Custom_IOA(ServiceClass):
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def get_patterns(self: object, ids) -> dict:
        """Get pattern severities by ID"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-patterns
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+"/ioarules/entities/pattern-severities/v1?ids={}".format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_platformsMixin0(self: object, ids) -> dict:
        """Get platforms by ID"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-platformsMixin0
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+"/ioarules/entities/platforms/v1?ids={}".format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_rule_groupsMixin0(self: object, ids) -> dict:
        """Get rule groups by ID"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rule-groupsMixin0
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+"/ioarules/entities/rule-groups/v1?ids={}".format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def create_rule_groupMixin0(self: object, body: dict, cs_username: str) -> dict:
        """Create a rule group for a platform with a name and an optional description. Returns the rule group."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/create-rule-groupMixin0
        FULL_URL = self.base_url+'/ioarules/entities/rule-groups/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def delete_rule_groupMixin0(self: object, ids, cs_username: str, parameters: dict = None) -> dict:
        """Delete rule groups by ID."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/delete-rule-groupsMixin0
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/ioarules/entities/rule-groups/v1?ids={}'.format(ID_LIST)
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

    def update_rule_groupMixin0(self: object, body: dict, cs_username: str) -> dict:
        """Update a rule group. The following properties can be modified: name, description, enabled."""
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/update-rule-groupMixin0
        FULL_URL = self.base_url+'/ioarules/entities/rule-groups/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_rule_types(self: object, ids) -> dict:
        """Get rule types by ID"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rule-types
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+"/ioarules/entities/rule-types/v1?ids={}".format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_rules_get(self: object, ids) -> dict:
        """Get rules by ID and optionally version in the following format: ID[:version]"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rules-get
        FULL_URL = self.base_url+"/ioarules/entities/rules/GET/v1"
        HEADERS = self.headers
        BODY = {}
        BODY["ids"] = parse_id_list(ids).split(",")     # We need a list in this scenario
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_rulesMixin0(self: object, ids) -> dict:
        """Get rules by ID and optionally version in the following format: ID[:version].
           The max number of IDs is constrained by URL size.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rulesMixin0
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+"/ioarules/entities/rules/v1?ids={}".format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def create_rule(self: object, body: dict, cs_username: str) -> dict:
        """Create a rule within a rule group. Returns the rule."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/create-rule
        FULL_URL = self.base_url+'/ioarules/entities/rules/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def delete_rules(self: object, ids, cs_username: str, parameters: dict = None) -> dict:
        """Delete rules from a rule group by ID."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/delete-rules
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/ioarules/entities/rules/v1?ids={}'.format(ID_LIST)
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

    def update_rules(self: object, body: dict, cs_username: str) -> dict:
        """Update rules within a rule group. Return the updated rules."""
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/update-rules
        FULL_URL = self.base_url+'/ioarules/entities/rules/v1'
        HEADERS = self.headers
        HEADERS['X-CS-USERNAME'] = cs_username
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def validate(self: object, body: dict) -> dict:
        """Validates field values and checks for matches if a test string is provided."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/validate
        FULL_URL = self.base_url+'/ioarules/entities/rules/validate/v1'
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

    def query_patterns(self: object, parameters: dict = None) -> dict:
        """Get all pattern severity IDs"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-patterns
        FULL_URL = self.base_url+"/ioarules/queries/pattern-severities/v1"
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_platformsMixin0(self: object, parameters: dict = None) -> dict:
        """Get all platform IDs."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-platformsMixin0
        FULL_URL = self.base_url+"/ioarules/queries/platforms/v1"
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_rule_groups_full(self: object, parameters: dict = None) -> dict:
        """Find all rule groups matching the query with optional filter."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-groups-full
        FULL_URL = self.base_url+"/ioarules/queries/rule-groups-full/v1"
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_rule_groupsMixin0(self: object, parameters: dict = None) -> dict:
        """Finds all rule group IDs matching the query with optional filter."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-groupsMixin0
        FULL_URL = self.base_url+"/ioarules/queries/rule-groups/v1"
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_rule_types(self: object, parameters: dict = None) -> dict:
        """Get all rule type IDs."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-types
        FULL_URL = self.base_url+"/ioarules/queries/rule-types/v1"
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def query_rulesMixin0(self: object, parameters: dict = None) -> dict:
        """Finds all rule IDs matching the query with optional filter."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rulesMixin0
        FULL_URL = self.base_url+"/ioarules/queries/rules/v1"
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   verify=self.ssl_verify
                                   )
        return returned
