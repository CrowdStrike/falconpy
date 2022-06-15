"""CrowdStrike Falcon Firewall Management API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

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
# pylint: disable=C0302
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import aggregate_payload, firewall_container_payload
from ._payload import firewall_rule_group_payload, firewall_rule_group_update_payload
from ._service_class import ServiceClass
from ._endpoint._firewall_management import _firewall_management_endpoints as Endpoints


class FirewallManagement(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (OAuth2.token())
    """

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_events(self: object, body: list = None, **kwargs) -> dict:
        """Aggregate events for customer.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                List of dictionaries.
                [{
                    "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                    ],
                    "field": "string",
                    "filter": "string",
                    "interval": "string",
                    "min_doc_count": 0,
                    "missing": "string",
                    "name": "string",
                    "q": "string",
                    "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                    ],
                    "size": 0,
                    "sort": "string",
                    "sub_aggregates": [
                        null
                    ],
                    "time_zone": "string",
                    "type": "string"
                }]
        date_ranges -- If peforming a date range query specify the from and to date ranges.
                       These can be in common date formats like 2019-07-18 or now.
                       List of dictionaries.
        field -- Term you want to aggregate on. If doing a date_range query,
                 this is the date field you want to apply the date ranges to. String.
        filter -- Optional filter criteria in the form of an FQL query.
                  For more information about FQL queries, see our FQL documentation in Falcon.
                  String.
        interval -- String.
        min_doc_count -- Minimum number of documents required to match. Integer.
        missing -- String.
        name -- Name of the aggregation. String.
        q -- FQL syntax. String.
        ranges -- List of dictionaries.
        size -- Size limit to apply to the queries. Integer.
        sort -- FQL syntax. String.
        sub_aggregates -- List of strings.
        time_zone -- String.
        type -- String.

        This method only supports keywords for providing arguments.

        This method does not support body payload validation.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_events
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_events",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_policy_rules(self: object, body: list = None, **kwargs) -> dict:
        """Aggregate rules within a policy for customer.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                List of dictionaries.
                [{
                    "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                    ],
                    "field": "string",
                    "filter": "string",
                    "interval": "string",
                    "min_doc_count": 0,
                    "missing": "string",
                    "name": "string",
                    "q": "string",
                    "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                    ],
                    "size": 0,
                    "sort": "string",
                    "sub_aggregates": [
                        null
                    ],
                    "time_zone": "string",
                    "type": "string"
                }]
        date_ranges -- If peforming a date range query specify the from and to date ranges.
                       These can be in common date formats like 2019-07-18 or now.
                       List of dictionaries.
        field -- Term you want to aggregate on. If doing a date_range query,
                 this is the date field you want to apply the date ranges to. String.
        filter -- Optional filter criteria in the form of an FQL query.
                  For more information about FQL queries, see our FQL documentation in Falcon.
                  String.
        interval -- String.
        min_doc_count -- Minimum number of documents required to match. Integer.
        missing -- String.
        name -- Name of the aggregation. String.
        q -- FQL syntax. String.
        ranges -- List of dictionaries.
        size -- Size limit to apply to the queries. Integer.
        sort -- FQL syntax. String.
        sub_aggregates -- List of strings.
        time_zone -- String.
        type -- String.

        This method only supports keywords for providing arguments.

        This method does not support body payload validation.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_policy_rules
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_policy_rules",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_rule_groups(self: object, body: list = None, **kwargs) -> dict:
        """Aggregate rule groups for customer.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                List of dictionaries.
                [{
                    "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                    ],
                    "field": "string",
                    "filter": "string",
                    "interval": "string",
                    "min_doc_count": 0,
                    "missing": "string",
                    "name": "string",
                    "q": "string",
                    "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                    ],
                    "size": 0,
                    "sort": "string",
                    "sub_aggregates": [
                        null
                    ],
                    "time_zone": "string",
                    "type": "string"
                }]
        date_ranges -- If peforming a date range query specify the from and to date ranges.
                       These can be in common date formats like 2019-07-18 or now.
                       List of dictionaries.
        field -- Term you want to aggregate on. If doing a date_range query,
                 this is the date field you want to apply the date ranges to. String.
        filter -- Optional filter criteria in the form of an FQL query.
                  For more information about FQL queries, see our FQL documentation in Falcon.
                  String.
        interval -- String.
        min_doc_count -- Minimum number of documents required to match. Integer.
        missing -- String.
        name -- Name of the aggregation. String.
        q -- FQL syntax. String.
        ranges -- List of dictionaries.
        size -- Size limit to apply to the queries. Integer.
        sort -- FQL syntax. String.
        sub_aggregates -- List of strings.
        time_zone -- String.
        type -- String.

        This method only supports keywords for providing arguments.

        This method does not support body payload validation.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rule_groups
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_rule_groups",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_rules(self: object, body: list = None, **kwargs) -> dict:
        """Aggregate rules for customer.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                List of dictionaries.
                [{
                    "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                    ],
                    "field": "string",
                    "filter": "string",
                    "interval": "string",
                    "min_doc_count": 0,
                    "missing": "string",
                    "name": "string",
                    "q": "string",
                    "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                    ],
                    "size": 0,
                    "sort": "string",
                    "sub_aggregates": [
                        null
                    ],
                    "time_zone": "string",
                    "type": "string"
                }]
        date_ranges -- If peforming a date range query specify the from and to date ranges.
                       These can be in common date formats like 2019-07-18 or now.
                       List of dictionaries.
        field -- Term you want to aggregate on. If doing a date_range query,
                 this is the date field you want to apply the date ranges to. String.
        filter -- Optional filter criteria in the form of an FQL query.
                  For more information about FQL queries, see our FQL documentation in Falcon.
                  String.
        interval -- String.
        min_doc_count -- Minimum number of documents required to match. Integer.
        missing -- String.
        name -- Name of the aggregation. String.
        q -- FQL syntax. String.
        ranges -- List of dictionaries.
        size -- Size limit to apply to the queries. Integer.
        sort -- FQL syntax. String.
        sub_aggregates -- List of strings.
        time_zone -- String.
        type -- String.

        This method only supports keywords for providing arguments.

        This method does not support body payload validation.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rules
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_rules",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_events(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get events entities by ID and optionally version.

        Keyword arguments:
        ids -- The IDs of the events to retrieve. String or list of strings.
        parameters - full parameters payload, not required if `ids` keyword is provided.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_events
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_events",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_firewall_fields(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get the firewall field specifications by ID.

        Keyword arguments:
        ids -- The IDs of the rule types to retrieve. String or list of strings.
        parameters - full parameters payload, not required if `ids` keyword is provided.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_firewall_fields
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_firewall_fields",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_platforms(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get platforms by ID, e.g., windows or mac or droid.

        Keyword arguments:
        ids -- The IDs of the platforms to retrieve. String or list of strings.
        parameters - full parameters payload, not required if `ids` keyword is provided.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_platforms
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_platforms",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy_containers(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get policy container entities by policy ID.

        Keyword arguments:
        ids -- The IDs of the policy container(s) to retrieve. String or list of strings.
        parameters - full parameters payload, not required if `ids` keyword is provided.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_policy_containers
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_policy_containers",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_policy_container(self: object,
                                body: dict,
                                cs_username: str = None,  # pylint: disable=W0613  # deprecated
                                **kwargs
                                ) -> dict:
        """Update an identified policy container.

        Keyword arguments:
        body -- Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "default_inbound": "string",
                    "default_outbound": "string",
                    "enforce": true,
                    "is_default_policy": true,
                    "platform_id": "string",
                    "policy_id": "string",
                    "rule_group_ids": [
                        "string"
                    ],
                    "test_mode": true,
                    "tracking": "string"
                }
        default_inbound -- Default inbound. String.
        default_outbound -- Default outbound. String.
        enforce -- Flag indicating if the policy is enforced. Boolean.
        is_default_policy -- Flag indicating if the policy is the default. Boolean.
        platform_id -- Platform ID. (`windows`, `mac`, `linux`) String.
        policy_id -- ID of the policy to be updated. String.
        rule_group_ids -- Rule group IDs this policy applies to. String or list of strings.
        test_mode -- Flag indicating if this policy is in test mode. Boolean.
        tracking -- Tracking. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PUT

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update_policy_container
        """
        if not body:
            body = firewall_container_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_policy_container",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get rule group entities by ID.

        These groups do not contain their rule entites, just the rule IDs in precedence order.

        Keyword arguments:
        ids -- The IDs of the rule group(s) to retrieve. String or list of strings.
        parameters - full parameters payload, not required if `ids` keyword is provided.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rule_groups
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_rule_groups",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def create_rule_group(self: object,
                          body: dict = None,
                          cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                          parameters: dict = None,
                          **kwargs
                          ) -> dict:
        """Create new rule group on a platform for a customer with a name and description.

        Returns the ID.

        Keyword arguments:
        action -- Rule action to perform. String. Overridden if 'rules' keyword is provided.
        address_family -- Address type, String. Either 'IP4', 'IP6' or 'NONE'.
                          Overridden if 'rules' keyword is provided.
        body -- Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "description": "string",
                    "enabled": true,
                    "name": "string",
                    "rules": [
                        {
                            "action": "string",
                            "address_family": "string",
                            "description": "string",
                            "direction": "string",
                            "enabled": true,
                            "fields": [
                                {
                                    "final_value": "string",
                                    "label": "string",
                                    "name": "string",
                                    "type": "string",
                                    "value": "string",
                                    "values": [
                                        "string"
                                    ]
                                }
                            ],
                            "icmp": {
                                "icmp_code": "string",
                                "icmp_type": "string"
                            },
                            "local_address": [
                                {
                                    "address": "string",
                                    "netmask": 0
                                }
                            ],
                            "local_port": [
                                {
                                    "end": 0,
                                    "start": 0
                                }
                            ],
                            "log": true,
                            "monitor": {
                                "count": "string",
                                "period_ms": "string"
                            },
                            "name": "string",
                            "platform_ids": [
                                "string"
                            ],
                            "protocol": "string",
                            "remote_address": [
                                {
                                    "address": "string",
                                    "netmask": 0
                                }
                            ],
                            "remote_port": [
                                {
                                    "end": 0,
                                    "start": 0
                                }
                            ],
                            "temp_id": "string"
                        }
                    ]
                }
        clone_id -- A rule group ID from which to copy rules.
                    If this is provided the `rules` keyword is ignored.
        comment -- Audit log comment for this action. String.
        description -- Rule group description. String.
        direction -- Traffic direction for created rule. String. Either 'IN', 'OUT' or 'BOTH'.
                     Overridden if 'rules' keyword is provided.
        enabled -- Flag indicating if the rule group is enabled. Boolean.
        fields -- Fields to impact. Dictionary or list of dictionaries.
                  Overridden if 'rules' keyword is provided.
        icmp -- ICMP protocol options. Dictionary.  Overridden if 'rules' keyword is provided.
        library -- If this flag is set to true then the rules will be cloned from the
                   clone_id from the CrowdStrike Firewall Rule Groups Library. String.
        local_address -- Local address and netmask detail. Dictionary or list of dictionaries.
                         Overridden if 'rules' keyword is provided.
        local_port -- Local port range. Dictionary or list of dictionaries.
                      Overridden if 'rules' keyword is provided.
        log -- Log rule matches. Boolean. Overridden if 'rules' keyword is provided.
        name -- Rule group name. String.
        monitor -- Monitor count / period. Dictionary. Overridden if 'rules' keyword is provided.
        parameters - full parameters payload, not required if using other keywords.
        platform_ids -- OS platform(s) covered by rule. Comma-delimited string or list of strings.
                        Overridden if 'rules' keyword is provided.
        protocol -- Integer protocol specified. Integer. Overridden if 'rules' keyword is provided.
                    (TCP = 6, UDP = 17)
        remote_address -- Remote address and netmask detail. Dictionary or list of dictionaries.
                          Overridden if 'rules' keyword is provided.
        remote_port -- Remote port range. Dictionary or list of dictionaries.
                       Overridden if 'rules' keyword is provided.
        rule_description -- Description for created rule. String.
                            Overridden if 'rules' keyword is provided.
        rule_enabled -- Enablement status for new rule. Boolean.
                        Overridden if 'rules' keyword is provided.
        rule_name -- Name for the new rule. String.  Overridden if 'rules' keyword is provided.
        rules - Rule(s) in JSON format. Single dictionary or List of dictionaries.
                {
                    "action": "string",
                    "address_family": "string",
                    "description": "string",
                    "direction": "string",
                    "enabled": true,
                    "fields": [
                        {
                            "final_value": "string",
                            "label": "string",
                            "name": "string",
                            "type": "string",
                            "value": "string",
                            "values": [
                                "string"
                            ]
                        }
                    ],
                    "icmp": {
                        "icmp_code": "string",
                        "icmp_type": "string"
                    },
                    "local_address": [
                        {
                            "address": "string",
                            "netmask": 0
                        }
                    ],
                    "local_port": [
                        {
                            "end": 0,
                            "start": 0
                        }
                    ],
                    "log": true,
                    "monitor": {
                        "count": "string",
                        "period_ms": "string"
                    },
                    "name": "string",
                    "platform_ids": [
                        "string"
                    ],
                    "protocol": "string",
                    "remote_address": [
                        {
                            "address": "string",
                            "netmask": 0
                        }
                    ],
                    "remote_port": [
                        {
                            "end": 0,
                            "start": 0
                        }
                    ],
                    "temp_id": "string"
                }
        temp_id -- String to use for rule temporary ID. String.
                   Overridden if 'rules' keyword is provided.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/create_rule_group
        """
        if not body:
            body = firewall_rule_group_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_rule_group",
            body=body,
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule_groups(self: object,
                           *args,
                           cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                           parameters: dict = None,
                           **kwargs
                           ) -> dict:
        """Delete rule group entities by ID.

        Keyword arguments:
        ids -- The IDs of the rule group(s) to delete. String or list of strings.
        parameters - full parameters payload, not required if `ids` keyword is provided.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QueryReports
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="delete_rule_groups",
            params=handle_single_argument(args, parameters, "ids"),
            keywords=kwargs
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def update_rule_group(self: object,
                          body: dict = None,
                          cs_username: str = None,  # pylint: disable=W0613  # deprecated
                          parameters: dict = None,
                          **kwargs
                          ) -> dict:
        """Update name, description, or enabled status of a rule group and underlying rules.

        Can also create, edit, delete, or reorder rules.

        Keyword arguments:
        body -- Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "diff_operations": [
                        {
                            "from": "string",
                            "op": "string",
                            "path": "string"
                        }
                    ],
                    "diff_type": "string",
                    "id": "string",
                    "rule_ids": [
                        "string"
                    ],
                    "rule_versions": [
                        0
                    ],
                    "tracking": "string"
                }
        comment -- Audit log comment for this action. String.
        diff_from -- From value for diff. String. Overridden if 'diff_operations' is provided.
        diff_op -- Operation for diff. String. Overridden if 'diff_operations' is provided.
        diff_operations -- Diff operations to perform against the rule group.
                           Single dictionary or List of dictionaries.
        diff_path -- Path for diff. String. Overridden if 'diff_operations' is provided.
        diff_type -- Type of diff to apply. String.
        id -- ID of the rule group to update. String.
        parameters - full parameters payload, not required if using other keywords.
        rule_ids -- Rule ID(s). List of strings.
        rule_versions -- Rule version(s). List of integers.
        tracking -- Tracking. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update_rule_group
        """
        if not body:
            body = firewall_rule_group_update_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_rule_group",
            body=body,
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get rule entities by ID or Family ID.

        ID = 64-bit unsigned int as decimal string
        Family ID = 32-character hexadecimal string

        Keyword arguments:
        ids -- The IDs of the rule(s) to retrieve. String or list of strings.
        parameters - full parameters payload, not required if `ids` keyword is provided.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rules
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_rules",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_events(self: object, parameters: dict = None, **kwargs) -> dict:
        """Find all event IDs matching the query with filter.

        Keyword arguments:
        after -- A pagination token used with the limit parameter to manage pagination
                 of results. On your first request, don't provide an after token. On
                 subsequent requests, provide the after token from the previous response
                 to continue from that place in the results.
        filter -- FQL query specifying the filter parameters.
                  Filter term criteria:
                  enabled           name
                  platform          description

                  Filter range criteria:
                  created_on
                  modified_on

                  (use any common date format, such as '2010-05-15T14:55:21.892315096Z')
        limit -- The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset -- The integer offset to start retrieving records from. Defaults to 0.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. created_on|desc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_events
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_events",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_firewall_fields(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get the firewall field specification IDs for the provided platform.

        Keyword arguments:
        platform_id -- Get fields configuration for this platform. String.
        limit -- The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset -- The integer offset to start retrieving records from. Defaults to 0.
        parameters - full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_firewall_fields
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_firewall_fields",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_platforms(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get the list of platform names.

        Keyword arguments:
        limit -- The maximum number of rule IDs to return. [integer, 1-100]
        offset -- The integer offset to start retrieving records from. Defaults to 0.
        parameters - full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_platforms
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_platforms",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policy_rules(self: object, parameters: dict = None, **kwargs) -> dict:
        """Find all firewall rule IDs matching the query with filter.

        Results are returned in precedence order.

        Keyword arguments:
        after -- A pagination token used with the limit parameter to manage pagination
                 of results. On your first request, don't provide an after token. On
                 subsequent requests, provide the after token from the previous response
                 to continue from that place in the results.
        filter -- FQL query specifying the filter parameters.
                  Filter term criteria:
                  enabled           name
                  platform          description

                  Filter range criteria:
                  created_on
                  modified_on

                  (use any common date format, such as '2010-05-15T14:55:21.892315096Z')
        limit -- The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset -- The integer offset to start retrieving records from. Defaults to 0.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. created_on|desc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_policy_rules
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_policy_rules",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_groups(self: object, parameters: dict = None, **kwargs) -> dict:
        """Find all rule group IDs matching the query with filter.

        Keyword arguments:
        after -- A pagination token used with the limit parameter to manage pagination
                 of results. On your first request, don't provide an after token. On
                 subsequent requests, provide the after token from the previous response
                 to continue from that place in the results.
        filter -- FQL query specifying the filter parameters.
                  Filter term criteria:
                  enabled           name
                  platform          description

                  Filter range criteria:
                  created_on
                  modified_on

                  (use any common date format, such as '2010-05-15T14:55:21.892315096Z')
        limit -- The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset -- The integer offset to start retrieving records from. Defaults to 0.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. created_on|desc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rule_groups",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rules(self: object, parameters: dict = None, **kwargs) -> dict:
        """Find all rule IDs matching the query with filter.

        Keyword arguments:
        after -- A pagination token used with the limit parameter to manage pagination
                 of results. On your first request, don't provide an after token. On
                 subsequent requests, provide the after token from the previous response
                 to continue from that place in the results.
        filter -- FQL query specifying the filter parameters.
                  Filter term criteria:
                  enabled           name
                  platform          description

                  Filter range criteria:
                  created_on
                  modified_on

                  (use any common date format, such as '2010-05-15T14:55:21.892315096Z')
        limit -- The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset -- The integer offset to start retrieving records from. Defaults to 0.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. created_on|desc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rules",
            keywords=kwargs,
            params=parameters
            )


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Firewall_Management = FirewallManagement  # pylint: disable=C0103
