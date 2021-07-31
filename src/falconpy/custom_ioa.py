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
# pylint: disable=C0103  # Aligning method names to API operation IDs
from ._util import service_request, parse_id_list, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._custom_ioa import _custom_ioa_endpoints as Endpoints


class Custom_IOA(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_patterns(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get pattern severities by ID
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-patterns
        operation_id = "get_patterns"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_platformsMixin0(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get platforms by ID
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-platformsMixin0
        operation_id = "get_platformsMixin0"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_groupsMixin0(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get rule groups by ID
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rule-groupsMixin0
        operation_id = "get_rule_groupsMixin0"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def create_rule_groupMixin0(self: object, body: dict, cs_username: str) -> dict:
        """
        Create a rule group for a platform with a name and an optional description. Returns the rule group.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/create-rule-groupMixin0
        operation_id = "create_rule_groupMixin0"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        header_payload["X-CS-USERNAME"] = cs_username
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule_groupMixin0(self: object, *args, **kwargs) -> dict:
        """
        Delete rule groups by ID. (Redirects to actual method. Typo fix.)
        """
        returned = self.delete_rule_groupsMixin0(*args, **kwargs)
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule_groupsMixin0(self: object, cs_username: str, parameters: dict = None, **kwargs) -> dict:
        """
        Delete rule groups by ID.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/delete-rule-groupsMixin0
        operation_id = "delete_rule_groupsMixin0"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        header_payload["X-CS-USERNAME"] = cs_username
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def update_rule_groupMixin0(self: object, body: dict, cs_username: str) -> dict:
        """
        Update a rule group. The following properties can be modified: name, description, enabled.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/update-rule-groupMixin0
        operation_id = "update_rule_groupMixin0"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        header_payload["X-CS-USERNAME"] = cs_username
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_types(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get rule types by ID
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rule-types
        operation_id = "get_rule_types"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def get_rules_get(self: object, ids) -> dict:
        """
        Get rules by ID and optionally version in the following format: ID[:version]
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rules-get
        operation_id = "get_rules_get"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = {}
        body_payload["ids"] = parse_id_list(ids).split(",")
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rulesMixin0(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get rules by ID and optionally version in the following format: ID[:version].
        The max number of IDs is constrained by URL size.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rulesMixin0
        operation_id = "get_rulesMixin0"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def create_rule(self: object, body: dict, cs_username: str) -> dict:
        """
        Create a rule within a rule group. Returns the rule.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/create-rule
        operation_id = "create_rule"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        header_payload["X-CS-USERNAME"] = cs_username
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rules(self: object, cs_username: str, parameters: dict = None, **kwargs) -> dict:
        """
        Delete rules from a rule group by ID.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/delete-rules
        operation_id = "delete_rules"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        header_payload["X-CS-USERNAME"] = cs_username
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def update_rules(self: object, body: dict, cs_username: str) -> dict:
        """
        Update rules within a rule group. Return the updated rules.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/update-rules
        operation_id = "update_rules"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        header_payload["X-CS-USERNAME"] = cs_username
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def validate(self: object, body: dict) -> dict:
        """
        Validates field values and checks for matches if a test string is provided.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/validate
        operation_id = "validate"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_patterns(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get all pattern severity IDs
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-patterns
        operation_id = "query_patterns"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_platformsMixin0(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get all platform IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-platformsMixin0
        operation_id = "query_platformsMixin0"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_groups_full(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find all rule groups matching the query with optional filter.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-groups-full
        operation_id = "query_rule_groups_full"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_groupsMixin0(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Finds all rule group IDs matching the query with optional filter.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-groupsMixin0
        operation_id = "query_rule_groupsMixin0"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_types(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get all rule type IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-types
        operation_id = "query_rule_types"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rulesMixin0(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Finds all rule IDs matching the query with optional filter.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rulesMixin0
        operation_id = "query_rulesMixin0"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
