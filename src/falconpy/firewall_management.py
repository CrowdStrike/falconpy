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
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._firewall_management import _firewall_management_endpoints as Endpoints


class FirewallManagement(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    def aggregate_events(self: object, body: dict) -> dict:
        """
        Aggregate events for customer.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_events
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_events",
            body=body
            )

    def aggregate_policy_rules(self: object, body: dict) -> dict:
        """
        Aggregate rules within a policy for customer.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_policy_rules
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_policy_rules",
            body=body
            )

    def aggregate_rule_groups(self: object, body: dict) -> dict:
        """
        Aggregate rule groups for customer.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rule_groups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_rule_groups",
            body=body
            )

    def aggregate_rules(self: object, body: dict) -> dict:
        """
        Aggregate rules for customer.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rules
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_rules",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_events(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get events entities by ID and optionally version.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_events
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_events",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_firewall_fields(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get the firewall field specifications by ID.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_firewall_fields
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_firewall_fields",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_platforms(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get platforms by ID, e.g., windows or mac or droid.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_platforms
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_platforms",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy_containers(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get policy container entities by policy ID.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_policy_containers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_policy_containers",
            keywords=kwargs,
            params=parameters
            )

    def update_policy_container(self: object,
                                body: dict,
                                cs_username: str = None  # pylint: disable=W0613  # cs_username is deprecated
                                ) -> dict:
        """
        Update an identified policy container.
        """
        # [PUT] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update_policy_container
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_policy_container",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_groups(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get rule group entities by ID.
        These groups do not contain their rule entites, just the rule IDs in precedence order.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rule_groups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_rule_groups",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def create_rule_group(self: object,
                          body: dict,
                          cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                          parameters: dict = None,
                          **kwargs
                          ) -> dict:
        """
        Create new rule group on a platform for a customer with a name and description, and return the ID.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/create_rule_group
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
                           cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                           parameters: dict = None,
                           **kwargs
                           ) -> dict:
        """
        Delete rule group entities by ID.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QueryReports
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="delete_rule_groups",
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_rule_group(self: object,
                          body: dict,
                          cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                          parameters: dict = None,
                          **kwargs
                          ) -> dict:
        """
        Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update_rule_group
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_rule_group",
            body=body,
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rules(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get rule entities by ID (64-bit unsigned int as decimal string) or Family ID (32-character hexadecimal string).
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rules
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_rules",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_events(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find all event IDs matching the query with filter.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_events
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_events",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_firewall_fields(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get the firewall field specification IDs for the provided platform.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_firewall_fields
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_firewall_fields",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_platforms(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get the list of platform names.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_platforms
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_platforms",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policy_rules(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find all firewall rule IDs matching the query with filter, and return them in precedence order.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_policy_rules
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_policy_rules",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_groups(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find all rule group IDs matching the query with filter.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rule_groups",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rules(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find all rule IDs matching the query with filter.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups
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
