"""Falcon Machine Learning Exclusions API Interface Class.

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
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import (
    exclusion_payload,
    aggregate_payload,
    ml_exclusions_actions_payload,
    ml_exclusions_report_payload,
    ml_exclusions_update_payload
)
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._ml_exclusions import _ml_exclusions_endpoints as Endpoints


class MLExclusions(ServiceClass):
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
    @force_default(defaults=["body"], default_types=["dict"])
    def aggregate_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get exclusion aggregates as specified via json in request body.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "date_ranges": [
                        {
                        "from": "string",
                        "to": "string"
                        }
                    ],
                    "exclude": "string",
                    "extended_bounds": {
                        "max": "string",
                        "min": "string"
                    },
                    "field": "string",
                    "filter": "string",
                    "filters_spec": {
                        "filters": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                        },
                        "other_bucket": true,
                        "other_bucket_key": "string"
                    },
                    "from": 0,
                    "include": "string",
                    "interval": "string",
                    "max_doc_count": 0,
                    "min_doc_count": 0,
                    "missing": "string",
                    "name": "string",
                    "percents": [
                        0
                    ],
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

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.aggregates.v2
        """
        if not body:
            body = aggregate_payload(submitted_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_aggregates_v2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_all_exclusions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all exclusions.

        Keyword arguments:

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.get-all.v2
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_get_all_v2"
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def perform_actions(self: object,
                        body: dict = None,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Actions used to manipulate the content of exclusions, with ancestor fields.

        Keyword arguments:
        action_name -- The action to perform. String.
                       Available values:
                            add_item    remove_item     validate_filepath
        body -- full body payload, not required when using other keywords.
                {
                    "action_parameters": [
                        {
                        "name": "string",
                        "value": "string"
                        }
                    ],
                    "available": true,
                    "description": "string",
                    "group": "string",
                    "label": "string",
                    "name": "string"
                }
        action_parameters -- List of dictionary.
        available -- Boolean.
        description -- String.
        group -- String.
        label -- String.
        name -- String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.perform-action.v2
        """
        if not body:
            body = ml_exclusions_actions_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_perform_action_v2",
            body=body,
            params=parameters,
            kwargs=kwargs
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_reports(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a report of ML exclusions scoped by the given filters.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "report_format": "string",
                    "search": {
                        "filter": "string",
                        "sort": "string"
                    }
                }

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.get-reports.v2
        """
        if not body:
            body = ml_exclusions_report_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_get_reports_v2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_exclusions_by_id(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the exclusions by id, with ancestor fields.

        Keyword arguments:
        ids -- The ids of the exclusions to retrieve. String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.get.v2
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_get_v2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create the exclusions, with ancestor fields.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "exclusions": [
                        {
                        "comment": "string",
                        "excluded_from": [
                            "string"
                        ],
                        "grandparent_value": "string",
                        "groups": [
                            "string"
                        ],
                        "parent_value": "string",
                        "value": "string"
                        }
                    ]
                }
        exclusions -- List of dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.create.v2
        """
        if not body:
            if kwargs.get("exclusions", None):
                body = kwargs.get("exclusions", None)
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_create_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_exclusions_v2(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the exclusions by id, with ancestor fields.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "comment": "string",
                    "excluded_from": [
                        "string"
                    ],
                    "grandparent_value": "string",
                    "groups": [
                        "string"
                    ],
                    "id": "string",
                    "parent_value": "string",
                    "value": "string"
                }
        comment -- String.
        excluded_from -- String or list of strings.
        grandparent_value -- String.
        groups -- String or list of strings.
        id -- String.
        parent_value -- String.
        value -- String.
        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.update.v2
        """
        if not body:
            body = ml_exclusions_update_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_update_v2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_exclusions_v2(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete the exclusions by id, with ancestor fields.

        Keyword arguments:
        ids -- The ids of the exclusions to delete. String or list of strings.
        comment -- The comment why these exclusions were deleted. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.delete.v2
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_delete_v2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_exclusions_v2(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for exclusions, with ancestor fields.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. String.
        offset -- The offset to start retrieving records from. Integer.
        limit -- The maximum records to return. [1-500]. Integer
        sort -- The sort expression that should be used to sort the results. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.search.v2
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_search_v2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ml_exclusion_sets(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a set of ML Exclusions by specifying their IDs.

        Keyword arguments:
        ids -- The ids of the exclusions to retrieve. String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.
        
        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/getMLExclusionsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getMLExclusionsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_ml_exclusions_v2(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create the ML exclusions.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "comment": "string",
                    "excluded_from": [
                        "string"
                    ],
                    "groups": [
                        "string"
                    ],
                    "value": "string"
                }
        comment -- Comment describing why the exclusion is entered. String.
        excluded_from -- String or list of strings.
        groups -- Group IDs to exclude. List of strings.
        value -- Value to exclude. String

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/createMLExclusionsV1
        """
        if not body:
            body = exclusion_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createMLExclusionsV1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_ml_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the ML exclusions.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "comment": "string",
                    "groups": [
                        "string"
                    ],
                    "id": "string",
                    "is_descendant_process": true,
                    "value": "string"
                }
        comment -- Comment describing why the exclusion is entered. String.
        groups -- Group IDs to exclude. List of strings.
        id -- String.
        is_descendant_process -- Boolean.
        value -- Value to exclude. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/updateMLExclusionsV1
        """
        if not body:
            body = ml_exclusions_update_payload(passed_keywords=kwargs)
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateMLExclusionsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a set of ML Exclusions by specifying their IDs.

        Keyword arguments:
        ids -- List of exclusion IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/getMLExclusionsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getMLExclusionsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create the ML exclusions.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "comment": "string",
                    "excluded_from": [
                        "string"
                    ],
                    "groups": [
                        "string"
                    ],
                    "value": "string"
                }
        comment -- String comment describing why the exclusion is entered.
        excluded_from --
        groups -- Group IDs to exclude. List of strings.
        value -- Value to exclude. String

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/createMLExclusionsV1
        """
        if not body:
            body = exclusion_payload(passed_keywords=kwargs)
        # Issue 1233
        if not body.get("groups"):
            body["groups"] = ["all"]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createMLExclusionsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_exclusions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete the ML Exclusions by ID.

        Keyword arguments:
        comment -- Explains why this exclusions was deleted. String.
        ids -- List of exclusion IDs to delete. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/deleteMLExclusionsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteMLExclusionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the ML Exclusions.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "comment": "string",
                    "groups": [
                        "string"
                    ],
                    "id": "string",
                    "is_descendant_process": boolean,
                    "value": "string"
                }
        comment -- String comment describing why the exclusion is entered.
        groups -- Group IDs to exclude. List of strings.
        id -- Exclusion ID to update. String.
        is_descendant_process -- Flag indicating if this is a descendant process. Boolean.
        value -- Value to exclude. String

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/updateMLExclusionsV1
        """
        if not body:
            body = exclusion_payload(passed_keywords=kwargs)
        if kwargs.get("id", None):
            body["id"] = kwargs.get("id", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateMLExclusionsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_exclusions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for ML Exclusions.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
                  An asterisk wildcard '*' includes all results.
                  AVAILABLE FILTERS
                  applied_globally            last_modified
                  created_by                  modified_by
                  created_on                  value
        limit -- The maximum number of detections to return in this response.
                 [Integer, default: 100; max: 500]
                 Use with the offset parameter to manage pagination of results.
        offset -- The first detection to return, where 0 is the latest detection.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        sort -- The property to sort by. FQL syntax (e.g. last_behavior|asc).
                Available sort fields:
                applied_globally            last_modified
                created_by                  modified_by
                created_on                  value

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/queryMLExclusionsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryMLExclusionsV1",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    getMLExclusionsV1 = get_exclusions
    createMLExclusionsV1 = create_exclusions
    deleteMLExclusionsV1 = delete_exclusions
    updateMLExclusionsV1 = update_exclusions
    queryMLExclusionsV1 = query_exclusions


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
ML_Exclusions = MLExclusions  # pylint: disable=C0103
