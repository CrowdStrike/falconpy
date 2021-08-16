"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

recon - CrowdStrike Falcon X Recon API interface class

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
from ._util import process_service_request, force_default, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._recon import _recon_endpoints as Endpoints


class Recon(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    def aggregate_notifications(self: object, body: dict) -> dict:
        """
        Get notification aggregates as specified via JSON in request body.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/AggregateNotificationsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateNotificationsV1",
            body=body
            )

    def preview_rule(self: object, body: dict) -> dict:
        """
        Get notification aggregates as specified via JSON in request body.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/PreviewRuleV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PreviewRuleV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_actions(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get actions based on their IDs. IDs can be retrieved using the GET /queries/actions/v1 endpoint.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetActionsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetActionsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def create_actions(self: object, body: dict) -> dict:
        """
        Create actions for a monitoring rule. Accepts a list of actions that will be attached to the monitoring rule
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/CreateActionsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateActionsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_action(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete an action from a monitoring rule based on the action ID.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/DeleteActionV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteActionV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def update_action(self: object, body: dict) -> dict:
        """
        Update an action for a monitoring rule.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateActionV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateActionV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notifications_detailed_translated(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get detailed notifications based on their IDs. These include the raw intelligence content that generated the match.
        This endpoint will return translated notification content.
        The only target language available is English. A single notification can be translated per request
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsDetailedTranslatedV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetNotificationsDetailedTranslatedV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notifications_detailed(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get detailed notifications based on their IDs.
        These include the raw intelligence content that generated the match.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsDetailedV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetNotificationsDetailedV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notifications_translated(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get notifications based on their IDs. IDs can be retrieved using the GET /queries/notifications/v1 endpoint.
        This endpoint will return translated notification content. The only target language available is English.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsTranslatedV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetNotificationsTranslatedV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notifications(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get notifications based on their IDs. IDs can be retrieved using the GET /queries/notifications/v1 endpoint.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetNotificationsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_notifications(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete notifications based on IDs. Notifications cannot be recovered after they are deleted.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/DeleteNotificationsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteNotificationsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def update_notifications(self: object, body: dict) -> dict:
        """
        Update notification status or assignee. Accepts bulk requests
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateNotificationsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateNotificationsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get monitoring rules rules by provided IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetRulesV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetRulesV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def create_rules(self: object, body: dict) -> dict:
        """
        Create monitoring rules.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/CreateRulesV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateRulesV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rules(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete monitoring rules.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/DeleteRulesV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteRulesV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def update_rules(self: object, body: dict) -> dict:
        """
        Update monitoring rules.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateRulesV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateRulesV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_actions(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query actions based on provided criteria.
        Use the IDs from this response to get the action entities on GET /entities/actions/v1.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/QueryActionsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryActionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_notifications(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query notifications based on provided criteria.
        Use the IDs from this response to get the notification entities on GET /entities/notifications/v1
        or GET /entities/notifications-detailed/v1.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/QueryNotificationsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryNotificationsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rules(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query monitoring rules based on provided criteria.
        Use the IDs from this response to fetch the rules on /entities/rules/v1.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/QueryRulesV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryRulesV1",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    AggregateNotificationsV1 = aggregate_notifications
    PreviewRuleV1 = preview_rule
    GetActionsV1 = get_actions
    CreateActionsV1 = create_actions
    DeleteActionV1 = delete_action
    UpdateActionV1 = update_action
    GetNotificationsDetailedTranslatedV1 = get_notifications_detailed_translated
    GetNotificationsDetailedV1 = get_notifications_detailed
    GetNotificationsTranslatedV1 = get_notifications_translated
    GetNotificationsV1 = get_notifications
    DeleteNotificationsV1 = delete_notifications
    UpdateNotificationsV1 = update_notifications
    GetRulesV1 = get_rules
    CreateRulesV1 = create_rules
    DeleteRulesV1 = delete_rules
    UpdateRulesV1 = update_rules
    QueryActionsV1 = query_actions
    QueryNotificationsV1 = query_notifications
    QueryRulesV1 = query_rules
