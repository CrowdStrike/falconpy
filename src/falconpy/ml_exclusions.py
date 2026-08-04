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
# pylint: disable=C0302
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import (
    exclusion_payload,
    aggregate_payload,
    ml_exclusions_actions_payload,
    ml_exclusions_report_payload,
    ml_exclusions_update_payload,
    exclusions_sdmf_query_v1_payload,
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

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.aggregates.v2

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
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
        date_ranges : list[dict]
            Date range timeframe.
        exclude : str
            Fields to exclude from results.
        extended_bounds : dict
            Extended bounds for histogram aggregations.
        field : str
            Field to aggregate on.
        filter : str
            Filter criteria in the form of an FQL query.
        filters_spec : dict
            Additional filter specifications.
        from : int
            Starting index of overall result set.
        include : str
            Fields to include in results.
        interval : str
            Time interval for date histogram aggregations.
        max_doc_count : int
            Maximum number of documents per bucket.
        min_doc_count : int
            Minimum number of documents per bucket.
        missing : str
            Value to use for documents missing the field.
        name : str
            Name of the aggregation.
        percents : list
            Percentile values to calculate. List of floats.
        q : str
            Full text search query.
        ranges : list[dict]
            Range boundaries for range aggregations.
        size : int
            Maximum number of records to return.
        sort : str
            The field to sort on.
        sub_aggregates : list[dict]
            Nested aggregation definitions.
        time_zone : str
            Time zone for date histogram aggregations.
        type : str
            Type of aggregation to perform.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
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

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.get-all.v2

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_get_all_v2",
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def perform_actions(self: object,
                        body: dict = None,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Actions used to manipulate the content of exclusions, with ancestor fields.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.perform-action.v2

        Keyword arguments
        -----------------
        action_name : str
            The action to perform. String.
            Available values:
                 add_item    remove_item     validate_filepath
        body : dict
            full body payload, not required when using other keywords.
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
        action_parameters : list[dict]
            Action-specific parameters.
        available : bool
            Flag indicating if the action is available.
        description : str
            Description of the exclusion action.
        group : str
            Group associated with the action.
        label : str
            Display label for the action.
        name : str
            Name of the action.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ml_exclusions_actions_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_perform_action_v2",
            body=body,
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_reports(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a report of ML exclusions scoped by the given filters.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.get-reports.v2

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "report_format": "string",
                    "search": {
                        "filter": "string",
                        "sort": "string"
                    }
                }



        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
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
    def get_exclusions_by_id(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the exclusions by id, with ancestor fields.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.get.v2

        Keyword arguments
        -----------------
        ids : str or list[str]
            The ids of the exclusions to retrieve.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_get_v2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_exclusions_v2(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create the exclusions, with ancestor fields.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.create.v2

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
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
        exclusions : list[dict]

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = {}
            if kwargs.get("exclusions", None):
                body["exclusions"] = kwargs.get("exclusions", None)
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_create_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_exclusions_v2(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the exclusions by id, with ancestor fields.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.update.v2

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
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
        comment : str
            Comment describing why the exclusion is updated.
        excluded_from : str or list[str]
            Exclusion sources.
        grandparent_value : str
            Grandparent process value for the exclusion.
        groups : str or list[str]
            Group IDs to associate with the exclusion.
        id : str
            Identifier of the exclusion to update.
        parent_value : str
            Parent process value for the exclusion.
        value : str
            Value to exclude.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
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

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.delete.v2

        Keyword arguments
        -----------------
        ids : str or list[str]
            The ids of the exclusions to delete.
        comment : str
            The comment why these exclusions were deleted.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
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

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions.search.v2

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results.
        offset : int
            The offset to start retrieving records from.
        limit : int
            The maximum records to return. [1-500]
        sort : str
            The sort expression that should be used to sort the results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_search_v2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ml_exclusion_sets(self: object,
                              *args,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a set of ML Exclusions by specifying their IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/getMLExclusionsV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            The ids of the exclusions to retrieve.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getMLExclusionsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_ml_exclusions_v2(self: object,
                                body: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create the ML exclusions.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/createMLExclusionsV1

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
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
        comment : str
            Comment describing why the exclusion is entered.
        excluded_from : str or list[str]
        groups : str or list[str]
            Group IDs to exclude.
        value : str
            Value to exclude.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
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
    def update_ml_exclusions(self: object,
                             body: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the ML exclusions.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/updateMLExclusionsV1

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "comment": "string",
                    "groups": [
                        "string"
                    ],
                    "id": "string",
                    "is_descendant_process": true,
                    "value": "string"
                }
        comment : str
            Comment describing why the exclusion is entered.
        groups : str or list[str]
            Group IDs to exclude.
        id : str
            Identifier of the exclusion to update.
        is_descendant_process : bool
            Flag indicating if the exclusion applies to descendant processes.
        value : str
            Value to exclude.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
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

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/getMLExclusionsV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of exclusion IDs to retrieve.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
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

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/createMLExclusionsV1

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
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
        comment : str
            String comment describing why the exclusion is entered.
        excluded_from : str or list[str]
            Exclusion sources to apply.
        groups : str or list[str]
            Group IDs to exclude.
        value : str
            Value to exclude.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
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

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/deleteMLExclusionsV1

        Keyword arguments
        -----------------
        comment : str
            Explains why this exclusions was deleted.
        ids : str or list[str]
            List of exclusion IDs to delete.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
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

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/updateMLExclusionsV1

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "comment": "string",
                    "groups": [
                        "string"
                    ],
                    "id": "string",
                    "is_descendant_process": boolean,
                    "value": "string"
                }
        comment : str
            String comment describing why the exclusion is entered.
        groups : str or list[str]
            Group IDs to exclude.
        id : str
            Exclusion ID to update.
        is_descendant_process : bool
            Flag indicating if this is a descendant process.
        value : str
            Value to exclude.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
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

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/queryMLExclusionsV1

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            An asterisk wildcard '*' includes all results.
            AVAILABLE FILTERS
            applied_globally            last_modified
            created_by                  modified_by
            created_on                  value
        limit : int
            The maximum number of detections to return in this response.
            [Integer, default: 100; max: 500]
            Use with the offset parameter to manage pagination of results.
        offset : int
            The first detection to return, where 0 is the latest detection.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. last_behavior|asc).
            Available sort fields:
            applied_globally            last_modified
            created_by                  modified_by
            created_on                  value

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryMLExclusionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def exclusions_sdmf_query_v1(self: object,
                                 body: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute an SDMF data frame query against exclusion entities.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions/exclusions_sdmf_query_v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "control_info": {
                        "deadline": "string",
                        "duration": "string",
                        "execution_context": {
                            "catalog_version": "string",
                            "execution_options": "string",
                            "extensions": "string",
                            "queried_cids": [
                                "string"
                            ]
                        },
                        "execution_details": {
                            "driver_calls": "string"
                        },
                        "is_export_request": true,
                        "pagination_info": {
                            "limit": 0,
                            "offset": "string"
                        },
                        "partial_results": true,
                        "query_stats": {
                            "execution_stats": {
                                "visited_entities": 0,
                                "visited_relationships": 0
                            },
                            "total_hits": {
                                "relation": "string",
                                "total": 0
                            }
                        },
                        "store_headers": "string"
                    },
                    "id": "string",
                    "nodes": [
                        {
                            "alias": "string",
                            "id": "string",
                            "operator": "string",
                            "res_id": "string",
                            "schema": {
                                "base": [
                                    "string"
                                ],
                                "facets": [
                                    "string"
                                ],
                                "fields": [
                                    {
                                        "facets": [
                                            "string"
                                        ],
                                        "is_relationship": true,
                                        "is_required": true,
                                        "multiplicity": "string",
                                        "name": "string",
                                        "scope": "string",
                                        "type": "string"
                                    }
                                ],
                                "res_id": "string"
                            }
                        }
                    ],
                    "res_id": "string"
                }
        control_info : dict
            The control_info value.
        id : str
            The id value.
        nodes : list
            The nodes value.
        res_id : str
            The res_id value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = exclusions_sdmf_query_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="exclusions_sdmf_query_v1",
            body=body
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    getMLExclusionsV1 = get_exclusions
    createMLExclusionsV1 = create_exclusions
    deleteMLExclusionsV1 = delete_exclusions
    updateMLExclusionsV1 = update_exclusions
    queryMLExclusionsV1 = query_exclusions
    exclusions_aggregates_v2 = aggregate_exclusions
    exclusions_get_all_v2 = get_all_exclusions
    exclusions_perform_action_v2 = perform_actions
    exclusions_get_reports_v2 = get_reports
    exclusions_get_v2 = get_exclusions_by_id
    exclusions_create_v2 = create_exclusions_v2
    exclusions_update_v2 = update_exclusions_v2
    exclusions_delete_v2 = delete_exclusions_v2
    exclusions_search_v2 = search_exclusions_v2


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
ML_Exclusions = MLExclusions  # pylint: disable=C0103
