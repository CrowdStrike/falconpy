"""CrowdStrike Falcon Alerts API interface class.

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
from typing import Dict, Union, Optional, List
from ._util import force_default, process_service_request
from ._payload import (
    aggregate_payload, generic_payload_list, update_alerts_payload
    )
from ._service_class import ServiceClass
from ._endpoint._alerts import _alerts_endpoints as Endpoints


class Alerts(ServiceClass):
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
    def get_aggregate_alerts(self, body: list = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Retrieve aggregates for Alerts across all CIDs.

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
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Alerts/PostAggregatesAlertsV1
        """
        if not body:
            # Similar to 664: Alerts aggregates expects a list
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PostAggregatesAlertsV1",
            body=body
            )

    # PatchEntitiesAlertsV1 has been **DECOMISSIONED**

    # @force_default(defaults=["body"], default_types=["dict"])
    # def update_alerts(self, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
    #     """Perform actions on alerts identified by detection ID(s) in request.

    #     Keyword arguments:
    #     action_parameters -- List of dictionaries containing action specific parameter settings.
    #     add_tag -- add a tag to 1 or more alert(s). String. Overridden by action_parameters.
    #     append_comment -- appends new comment to existing comments. String.
    #                       Overridden by action_parameters.
    #     assign_to_name -- assign 1 or more alert(s) to a user identified by user name. String.
    #                       Overridden by action_parameters.
    #     assign_to_user_id -- assign 1 or more alert(s) to a user identified by user id
    #                          (eg: user1@example.com). String. Overridden by action_parameters.
    #     assign_to_uuid -- assign 1 or more alert(s) to a user identified by UUID. String.
    #                       Overridden by action_parameters.
    #     body -- full body payload, not required when using other keywords.
    #             {
    #                 "ids": [
    #                     "string"
    #                 ],
    #                 "request": {
    #                     "action_parameters": [
    #                         {
    #                             "name": "string",
    #                             "value": "string"
    #                         }
    #                     ]
    #                 }
    #             }
    #     ids -- ID(s) of the alert to update. String or list of strings.
    #     new_behavior_processed -- adds a newly processed behavior to 1 or more alert(s). String.
    #                               Overridden by action_parameters.
    #     remove_tag -- remove a tag from 1 or more alert(s). String.
    #                   Overridden by action_parameters.
    #     remove_tags_by_prefix -- remove tags with given prefix from 1 or more alert(s). String.
    #                              Overridden by action_parameters.
    #     show_in_ui -- shows 1 or more alert(s) on UI if set to true, hides otherwise.
    #                   An empty/nil value is also valid. Overridden by action_parameters.
    #     unassign -- unassign an previously assigned user from 1 or more alert(s).
    #                 The value passed to this action is ignored. Overridden by action_parameters.
    #     update_status -- update status for 1 or more alert(s). String.
    #                      Overridden by action_parameters.

    #     Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
    #                All others are ignored.

    #     Returns: dict object containing API response.

    #     HTTP Method: PATCH

    #     Swagger URL
    #     https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Alerts/PatchEntitiesAlertsV1
    #     """
    #     if not body:
    #         body = update_alerts_payload(
    #             current_payload=generic_payload_list(submitted_arguments=args,
    #                                                  submitted_keywords=kwargs,
    #                                                  payload_value="ids"
    #                                                  ),
    #             passed_keywords=kwargs
    #             )

    #     # Solve for the unusual ingest payload, passing action_parameters overrides other keywords
    #     if kwargs.get("action_parameters", None):
    #         body["request"]["action_parameters"] = kwargs.get("action_parameters", None)

    #     return process_service_request(
    #         calling_object=self,
    #         endpoints=Endpoints,
    #         operation_id="PatchEntitiesAlertsV1",
    #         body=body
    #         )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_alerts(self,
                      *args,
                      body: Optional[Dict[str, List[Union[str, Dict[str, str]]]]] = None,
                      **kwargs
                      ) -> Dict[str, Union[int, dict]]:
        """Perform actions on alerts identified by detection ID(s) in request.

        Keyword arguments:
        action_parameters -- List of dictionaries containing action specific parameter settings.
        add_tag -- add a tag to 1 or more alert(s). String. Overridden by action_parameters.
        append_comment -- appends new comment to existing comments. String.
                          Overridden by action_parameters.
        assign_to_name -- assign 1 or more alert(s) to a user identified by user name. String.
                          Overridden by action_parameters.
        assign_to_user_id -- assign 1 or more alert(s) to a user identified by user id
                             (eg: user1@example.com). String. Overridden by action_parameters.
        assign_to_uuid -- assign 1 or more alert(s) to a user identified by UUID. String.
                          Overridden by action_parameters.
        body -- full body payload, not required when using other keywords.
                {
                    "ids": [
                        "string"
                    ],
                    "action_parameters": [
                        {
                            "name": "string",
                            "value": "string"
                        }
                    ]
                }
        ids -- ID(s) of the alert to update. String or list of strings.
        new_behavior_processed -- adds a newly processed behavior to 1 or more alert(s). String.
                                  Overridden by action_parameters.
        remove_tag -- remove a tag from 1 or more alert(s). String.
                      Overridden by action_parameters.
        remove_tags_by_prefix -- remove tags with given prefix from 1 or more alert(s). String.
                                 Overridden by action_parameters.
        show_in_ui -- shows 1 or more alert(s) on UI if set to true, hides otherwise.
                      An empty/nil value is also valid. Overridden by action_parameters.
        unassign -- unassign an previously assigned user from 1 or more alert(s).
                    The value passed to this action is ignored. Overridden by action_parameters.
        update_status -- update status for 1 or more alert(s). String.
                         Overridden by action_parameters.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Alerts/PatchEntitiesAlertsV2
        """
        if not body:
            body = update_alerts_payload(
                current_payload=generic_payload_list(submitted_arguments=args,
                                                     submitted_keywords=kwargs,
                                                     payload_value="ids"
                                                     ),
                passed_keywords=kwargs
                )

        # Passing action_parameters overrides other keywords
        _action_params: Optional[List[Union[str, Dict[str, str]]]] = kwargs.get("action_parameters", None)
        if _action_params:
            body["action_parameters"] = _action_params
        # Getting this from mypy:
        # src/falconpy/alerts.py:269: error:
        # Unsupported target for indexed assignment ("Optional[Dict[str, List[Union[str, Dict[str, str]]]]]")
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PatchEntitiesAlertsV2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_alerts(self, *args, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Retrieve all Alerts given their IDs.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids -- ID(s) of the detections to retrieve. String or list of strings.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Alerts/PostEntitiesAlertsV1
        """
        if not body:
            body = generic_payload_list(submitted_arguments=args,
                                        submitted_keywords=kwargs,
                                        payload_value="ids"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PostEntitiesAlertsV1",
            body=body,
            body_validator={"ids": list} if self.validate_payloads else None,
            body_required=["ids"] if self.validate_payloads else None
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_alerts(self, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Search for detection IDs that match a given query.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.

        For more detail regarding filtering options, please review:
        https://falcon.crowdstrike.com/documentation/86/detections-monitoring-apis#find-detections

        limit -- The maximum number of detections to return in this response.
                 [Integer, default: 10000; max: 10000]
                 Use with the offset parameter to manage pagination of results.
        offset -- The first detection to return, where 0 is the latest detection.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        q -- Search all detection metadata for the provided string.
        sort -- The property to sort by. FQL syntax (e.g. status|asc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Alerts/GetQueriesAlertsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetQueriesAlertsV1",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    PostAggregatesAlertsV1 = get_aggregate_alerts
    PatchEntitiesAlertsV2 = update_alerts
    PostEntitiesAlertsV1 = get_alerts
    GetQueriesAlertsV1 = query_alerts
    # PatchEntitiesAlertsV1 has been decommissioned.  Redirect requests
    # to the newly defined PatchEntitiesAlertsV2 operation.
    update_alerts_v2 = update_alerts
    PatchEntitiesAlertsV1 = update_alerts
