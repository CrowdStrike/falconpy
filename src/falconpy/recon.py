"""CrowdStrike Falcon X Recon API interface class

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
from ._util import process_service_request, force_default, handle_single_argument
from ._payload import recon_rules_payload, recon_notifications_payload
from ._payload import recon_action_payload, recon_action_update_payload
from ._payload import recon_rule_preview_payload, aggregate_payload
from ._service_class import ServiceClass
from ._endpoint._recon import _recon_endpoints as Endpoints


class Recon(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following:

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (OAuth2.token())
    """
    @force_default(defaults=["body"], default_types=["dict"])
    def aggregate_notifications(self: object, body: dict = None, **kwargs) -> dict:
        """Get notification aggregates as specified via JSON in request body.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                [
                    {
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
                    }
                ]
        date_ranges -- List of dictionaries.
        field -- String.
        filter -- FQL syntax. String.
        interval -- String.
        min_doc_count -- Minimum number of documents required to match. Integer.
        missing -- String.
        name -- Scan name. String.
        q -- FQL syntax. String.
        ranges -- List of dictionaries.
        size -- Integer.
        sort -- FQL syntax. String.
        sub_aggregates -- List of strings.
        time_zone -- String.
        type -- String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/AggregateNotificationsV1
        """
        if not body:
            body = aggregate_payload(submitted_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateNotificationsV1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def preview_rule(self: object, body: dict = None, **kwargs) -> dict:
        """Get notification aggregates as specified via JSON in request body.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "filter": "string",
                    "topic": "string"
                }
        filter -- Rule filter. String.
        topic -- Rule topic. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/PreviewRuleV1
        """
        if not body:
            body = recon_rule_preview_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PreviewRuleV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_actions(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get actions based on their IDs. IDs can be retrieved using the GET query_actions.

        Keyword arguments:
        ids -- List of action IDs to retrieve details for. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetActionsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetActionsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_actions(self: object, body: dict = None, **kwargs) -> dict:
        """Create actions for a monitoring rule.
        Accepts a list of actions that will be attached to the monitoring rule.

        Keyword arguments:
        actions -- List of actions to attach to the monitoring rule.
                   When provided, actions overrides other passed keywords excluding body.
                   List of dictionaries in the following format:
                   {
                       "frequency": "string",
                       "recipients": [
                           "string"
                       ],
                       "type": "string"
                   }
        body -- full body payload, not required when using other keywords.
                {
                    "actions": [
                        {
                            "frequency": "string",
                            "recipients": [
                                "string"
                            ],
                            "type": "string"
                        }
                    ],
                    "rule_id": "string"
                }
        frequency - Frequency of the action. String. Used when only one
                    action is being handled.
        recipients -- UUIDs of the recipients. List of strings. Used when
                      only one action is being handled.
        rule_id -- Rule ID to attach the action to. Always required.
        type -- Action type, used when only one action is being handled.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateActionV1
        """
        if not body:
            body = recon_action_payload(passed_keywords=kwargs)

        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/CreateActionsV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateActionsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_action(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Delete an action from a monitoring rule based on the action ID.

        Keyword arguments:
        ids -- List of action IDs to delete. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/DeleteActionV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteActionV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_action(self: object, body: dict = None, **kwargs) -> dict:
        """Update an action for a monitoring rule.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "frequency": "string",
                    "id": "string",
                    "recipients": [
                        "string"
                    ],
                    "status": "string"
                }
        frequency - Frequency of the action. String.
        id -- Action ID. String.
        recipients -- UUIDs of the recipients. List of strings.
        status -- Action status. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateActionV1
        """
        if not body:
            body = recon_action_update_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateActionV1",
            body=body,
            body_validator={
                    "frequency": str,
                    "id": str,
                    "recipients": list,
                    "status": str
                } if self.validate_payloads else None,
            body_required=["id"] if self.validate_payloads else None
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notifications_detailed_translated(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get detailed notifications based on their IDs.
        These include the raw intelligence content that generated the match.
        This endpoint will return translated notification content.
        The only target language available is English.
        A single notification can be translated per request

        Keyword arguments:
        ids -- List of notification IDs to retrieve details for. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsDetailedTranslatedV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetNotificationsDetailedTranslatedV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notifications_detailed(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get detailed notifications based on their IDs.
        These include the raw intelligence content that generated the match.

        Keyword arguments:
        ids -- List of notification IDs to retrieve details for. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsDetailedV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetNotificationsDetailedV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notifications_translated(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get notifications based on their IDs.
        IDs can be retrieved using query_notifications.
        This endpoint will return translated notification content.
        The only target language available is English.

        Keyword arguments:
        ids -- List of notification IDs to retrieve details for. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsTranslatedV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetNotificationsTranslatedV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notifications(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get notifications based on their IDs.
        IDs can be retrieved using get_notifications.

        Keyword arguments:
        ids -- List of notification IDs to retrieve details for. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetNotificationsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_notifications(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Delete notifications based on IDs.
        Notifications cannot be recovered after they are deleted.

        Keyword arguments:
        ids -- List of notification IDs to retrieve details for. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/DeleteNotificationsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteNotificationsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_notifications(self: object, body: dict = None, **kwargs) -> dict:
        """Update notification status or assignee. Accepts bulk requests

        Keyword arguments:
        assigned_to_uuid - UUID of the assigned user. String.
        body -- full body payload, not required when using other keywords.
                [
                    {
                        "assigned_to_uuid": "string",
                        "id": "string",
                        "status": "string"
                    }
                ]
        id -- Notification ID. String.
        status -- Notification status. String.

        This method only supports keywords for providing arguments.

        This method does not support body payload validation.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateNotificationsV1
        """
        if not body:
            body = recon_notifications_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateNotificationsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get monitoring rules rules by provided IDs.

        Keyword arguments:
        ids -- List of rule IDs to retrieve details for. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetRulesV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetRulesV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_rules(self: object, body: dict = None, **kwargs) -> dict:
        """Create monitoring rules.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                [
                    {
                        "filter": "string",
                        "name": "string",
                        "permissions": "string",
                        "priority": "string",
                        "topic": "string"
                    }
                ]
        filter -- Rule filter. String.
        name -- Rule name. String.
        permissions -- String. (private / public)
        priority -- String. (high / medium / low)
        topic -- Rule topic. String.

        This method only supports keywords for providing arguments.

        This method does not support body payload validation.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/CreateRulesV1
        """
        if not body:
            body = recon_rules_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateRulesV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rules(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Delete monitoring rules.

        Keyword arguments:
        ids -- List of rule IDs to delete. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/DeleteRulesV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteRulesV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_rules(self: object, body: dict = None, **kwargs) -> dict:
        """Update monitoring rules.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                [
                    {
                        "filter": "string",
                        "name": "string",
                        "permissions": "string",
                        "priority": "string",
                        "topic": "string"
                    }
                ]
        filter -- Rule filter. String.
        name -- Rule name. String.
        permissions -- String. (private / public)
        priority -- String. (high / medium / low)
        topic -- Rule topic. String.

        This method only supports keywords for providing arguments.

        This method does not support body payload validation.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateRulesV1
        """
        if not body:
            body = recon_rules_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateRulesV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_actions(self: object, parameters: dict = None, **kwargs) -> dict:
        """Query actions based on provided criteria.
        Use the IDs from this response to get the action entities with get_actions.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
                  Available filters
                  cid                   rule_id
                  created_timestamp     status
                  frequency             type
                  id                    updated_timestamp
                  recipients            user_uuid
        limit -- The maximum number of IDs to return. [integer, 1-500]
        offset -- The first item to return, where 0 is the latest item. (Integer)
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        q -- Free text search across all indexed fields.
        sort -- The property to sort by. FQL syntax.
                (e.g. created_timestamp|asc, updated_timestamp|desc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/QueryActionsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryActionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_notifications(self: object, parameters: dict = None, **kwargs) -> dict:
        """Query notifications based on provided criteria.
        Use the IDs from this response to get the notification
        entities with get_notifications or get_notifications detailed.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
                  Available filters
                  cid               rule_topic
                  created_date      rule_priority
                  id                status
                  item_type         type
                  rule_name         updated_date
                  rule_id           user_uuid
        limit -- The maximum number of IDs to return. [integer, 1-500]
        offset -- The first item to return, where 0 is the latest item. (Integer)
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        q -- Free text search across all indexed fields.
        sort -- The property to sort by. FQL syntax. (e.g. created_date|asc, updated_date|desc)

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/QueryNotificationsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryNotificationsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rules(self: object, parameters: dict = None, **kwargs) -> dict:
        """Query monitoring rules based on provided criteria.
        Use the IDs from this response to fetch the rules with get_rules.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
                  Available filters
                  cid                         priority
                  created_timestamp           permissions
                  filter                      status
                  id                          topic
                  last_updated_timestamp      user_uuid
        limit -- The maximum number of IDs to return. [integer, 1-500]
        offset -- The first item to return, where 0 is the latest item. (Integer)
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        q -- Free text search across all indexed fields.
        sort -- The property to sort by. FQL syntax.
                (e.g. created_timestamp|asc, last_updated_timestamp|desc)

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/QueryRulesV1
        """
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
