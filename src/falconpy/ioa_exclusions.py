"""Falcon IOA Exclusions API Interface Class.

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
from ._util import force_default, handle_single_argument, process_service_request
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._ioa_exclusions import _ioa_exclusions_endpoints as Endpoints
from ._payload import (
    ioa_exclusion_payload,
    aggregate_payload,
    ioa_ss_exclusion_payload,
    ioa_ss_default_exclusion_payload
)


class IOAExclusions(ServiceClass):
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

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def get_ss_exclusion_aggregates(self: object,
                                    body: dict = None,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Self Service IOA Exclusion aggregates as specified via json in the request body.

        Keyword arguments:
        ifn_regex -- The `ifn_regex` expression to filter exclusion aggregations by. String.
        Used alongside filter expressions provided in the request body.
        cl_regex -- The `cl_regex` expression to filter exclusion aggregations by. String.
        Used alongside filter expressions provided in the request body.
        parent_ifn_regex -- The `parent_ifn_regex` expression to filter exclusion aggregations by. String.
        Used alongside filter expressions provided in the request body.
        parent_cl_regex -- The `parent_cl_regex` expression to filter exclusion aggregations by. String.
        Used alongside filter expressions provided in the request body.
        grandparent_ifn_regex -- The `grandparent_ifn_regex` expression to filter exclusion aggregations by. String.
        Used alongside filter expressions provided in the request body.
        grandparent_cl_regex -- The `grandparent_cl_regex` expression to filter exclusion aggregations by. String.
        Used alongside filter expressions provided in the request body.
        body -- full body payload, not required when ids keyword is provided.
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
        date_ranges -- Date range timeframe. List of dictionaries.
        exclude -- Fields to exclude from results. String.
        extended_bounds -- Extended bounds for histogram aggregations. Dictionary.
        field -- Field to aggregate on. String.
        filters_spec -- Additional filter specifications. Dictionary.
        from -- Starting index of overall result set. Integer.
        include -- Fields to include in results. String.
        max_doc_count -- Maximum number of documents per bucket. Integer.
        min_doc_count -- Minimum number of documents per bucket. Integer.
        missing -- Value to use for documents missing the field. String.
        name -- Name of the aggregation. String.
        percents -- Percentile values to calculate. List of integers.
        q -- Full text search query. String.
        ranges -- Range boundaries for range aggregations. List of dictionaries.
        size -- Maximum number of records to return. Integer.
        sort -- The field to sort on. String.
        sub_aggregates -- Nested aggregation definitions. List.
        time_zone -- Time zone for date histogram aggregations. String.
        type -- Type of aggregation to perform. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/ss-ioa-exclusions.aggregates.v2
        """
        if not body:
            body = aggregate_payload(submitted_keywords=kwargs)
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ss_ioa_exclusions_aggregates_v2",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_ss_exclusion_reports_v2(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a report of Self Service IOA Exclusions scoped by the given filters.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
                {
                    "report_format": "string",
                    "search": {
                        "filter": "string",
                        "sort": "string"
                    }
                }
        report_format -- Format of the report to generate. String.
        search -- Search criteria including filter and sort options. Dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/ss-ioa-exclusions.get-reports.v2
        """
        if not body:
            body = ioa_ss_exclusion_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ss_ioa_exclusions_get_reports_v2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ss_exclusion_rules_v2(self: object,
                                  *args,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the Self Service IOA Exclusions rules by id.

        Keyword arguments:
        ids -- The ids of the exclusions to retrieve. String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/ss-ioa-exclusions.get.v2
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ss_ioa_exclusions_get_v2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_ss_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create new Self Service IOA Exclusions.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
                {
                    "exclusions": [
                        {
                        "cl_regex": "string",
                        "comment": "string",
                        "description": "string",
                        "detection_json": "string",
                        "grandparent_cl_regex": "string",
                        "grandparent_ifn_regex": "string",
                        "host_groups": [
                            "string"
                        ],
                        "ifn_regex": "string",
                        "name": "string",
                        "parent_cl_regex": "string",
                        "parent_ifn_regex": "string",
                        "pattern_id": "string",
                        "pattern_name": "string"
                        }
                    ]
                }
        exclusions -- List of exclusion definitions to create. List of dictionaries.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/ss-ioa-exclusions.create.v2
        """
        if not body:
            if kwargs.get("exclusions", None):
                body = {
                    "exclusions": kwargs.get("exclusions", None)
                }

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ss_ioa_exclusions_create_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_ss_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the Self Service IOA Exclusions rule by id.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
                {
                    "exclusions": [
                        {
                        "cl_regex": "string",
                        "comment": "string",
                        "description": "string",
                        "detection_json": "string",
                        "grandparent_cl_regex": "string",
                        "grandparent_ifn_regex": "string",
                        "host_groups": [
                            "string"
                        ],
                        "id": "string",
                        "ifn_regex": "string",
                        "name": "string",
                        "parent_cl_regex": "string",
                        "parent_ifn_regex": "string",
                        "pattern_id": "string",
                        "pattern_name": "string"
                        }
                    ]
                }
        exclusions -- List of exclusion definitions to update. List of dictionaries.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/ss-ioa-exclusions.update.v2
        """
        if not body:
            if kwargs.get("exclusions", None):
                body = {
                    "exclusions": kwargs.get("exclusions", None)
                }

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ss_ioa_exclusions_update_v2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_ss_exclusions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete the Self Service IOA Exclusions rule by id.

        Keyword arguments:
        ids -- The ids of the exclusions to delete. String or list of strings.
        comment -- The comment why these ss ioa exclusions were deleted. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/ss-ioa-exclusions.delete.v2
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ss_ioa_exclusions_delete_v2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_ss_exclusion_matched_rules(self: object,
                                       body: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Self Service IOA Exclusions rules for matched IFN/CLI.

        For child, parent and grandparent.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
                {
                    "aid": "string",
                    "command_line": "string",
                    "grandparent_command_line": "string",
                    "grandparent_image_file_name": "string",
                    "image_file_name": "string",
                    "parent_command_line": "string",
                    "parent_image_file_name": "string",
                    "pattern_ids": [
                        "string"
                    ]
                }
        aid -- Agent ID to match exclusions against. String.
        command_line -- Command line of the child process. String.
        grandparent_command_line -- Command line of the grandparent process. String.
        grandparent_image_file_name -- Image file name of the grandparent process. String.
        image_file_name -- Image file name of the child process. String.
        parent_command_line -- Command line of the parent process. String.
        parent_image_file_name -- Image file name of the parent process. String.
        pattern_ids -- Pattern IDs to match exclusions against. List of strings.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/ss-ioa-exclusions.matched-rule.v2
        """
        if not body:
            body = ioa_ss_default_exclusion_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ss_ioa_exclusions_matched_rule_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_default_ss_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get defaults for Self Service IOA Exclusions based on provided IFN/CLI for child, parent and grandparent.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
                {
                    "aid": "string",
                    "command_line": "string",
                    "grandparent_command_line": "string",
                    "grandparent_image_file_name": "string",
                    "image_file_name": "string",
                    "parent_command_line": "string",
                    "parent_image_file_name": "string"
                }
        aid -- Agent ID to get default exclusions for. String.
        command_line -- Command line of the child process. String.
        grandparent_command_line -- Command line of the grandparent process. String.
        grandparent_image_file_name -- Image file name of the grandparent process. String.
        image_file_name -- Image file name of the child process. String.
        parent_command_line -- Command line of the parent process. String.
        parent_image_file_name -- Image file name of the parent process. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/ss-ioa-exclusions.new-rules.v2
        """
        if not body:
            body = ioa_ss_default_exclusion_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ss_ioa_exclusions_new_rules_v2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_ss_exclusions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for Self Service IOA Exclusions.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. String.
        Filtered queries involving regex fields should specify their expressions in the `ifn_regex` and `cl_regex` parameters.
        Regex parameters here are used alongside expressions specified in the filter query parameter.
        ifn_regex -- The `ifn_regex` expression to filter exclusions by. String.
        cl_regex -- The `cl_regex` expression to filter exclusions by. String.
        parent_ifn_regex -- The `parent_ifn_regex` expression to filter exclusions by. String.
        parent_cl_regex -- The `parent_cl_regex` expression to filter exclusions by. String.
        grandparent_ifn_regex -- The `grandparent_ifn_regex` expression to filter exclusions by. String.
        grandparent_cl_regex -- The `grandparent_cl_regex` expression to filter exclusions by. String.
        offset -- The offset to start retrieving records from. Integer.
        limit -- The maximum records to return. [1-500]. Integer.
        sort -- The sort expression that should be used to sort the results. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/ss-ioa-exclusions.search.v2
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ss_ioa_exclusions_search_v2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_exclusions(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a set of IOA Exclusions by specifying their IDs.

        Keyword arguments:
        ids -- List of exclusion IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/getIOAExclusionsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getIOAExclusionsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create the IOA exclusions.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
            {
                "cl_regex": "string",
                "comment": "string",
                "description": "string",
                "detection_json": "string",
                "groups": [
                    "string"
                ],
                "ifn_regex": "string",
                "name": "string",
                "pattern_id": "string",
                "pattern_name": "string"
            }
        cl_regex -- Command line regex value for the exclusion. String.
        comment -- Comment describing why the exclusion is entered. String.
        description -- Description of the exclusion. String.
        detection_json -- Detection JSON payload for the exclusion. String.
        groups -- Group IDs to exclude. List of strings.
        ifn_regex -- Image file name regex value for the exclusion. String.
        name -- Name of the exclusion. String.
        pattern_id -- Pattern ID associated with the exclusion. String.
        pattern_name -- Pattern name associated with the exclusion. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/createIOAExclusionsV1
        """
        if not body:
            body = ioa_exclusion_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createIOAExclusionsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_exclusions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete the IOA Exclusions by ID.

        Keyword arguments:
        comment -- Explains why this exclusions was deleted. String.
        ids -- List of exclusion IDs to delete. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/deleteIOAExclusionsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteIOAExclusionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the IOA Exclusions.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
            {
                "cl_regex": "string",
                "comment": "string",
                "description": "string",
                "detection_json": "string",
                "groups": [
                    "string"
                ],
                "id": "string",
                "ifn_regex": "string",
                "name": "string",
                "pattern_id": "string",
                "pattern_name": "string"
            }
        cl_regex -- Command line regex value for the exclusion. String.
        comment -- Comment describing why the exclusion is updated. String.
        description -- Description of the exclusion. String.
        detection_json -- Detection JSON payload for the exclusion. String.
        groups -- Group IDs to exclude. List of strings.
        id -- Identifier of the exclusion to update. String.
        ifn_regex -- Image file name regex value for the exclusion. String.
        name -- Name of the exclusion. String.
        pattern_id -- Pattern ID associated with the exclusion. String.
        pattern_name -- Pattern name associated with the exclusion. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/updateIOAExclusionsV1

        """
        if not body:
            body = ioa_exclusion_payload(passed_keywords=kwargs)
            if kwargs.get("id", None):
                body["id"] = kwargs.get("id", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateIOAExclusionsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_exclusions(self: object,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for IOA Exclusions.

        Keyword arguments:
        cl_regex -- The cl_regex expression to filter exclusions by, used alongside expressions
                    specified in the filter query parameter.
        filter -- The filter expression that should be used to limit the results. FQL syntax.
                  The filter expression that should be used to limit the results.
                  Filtered queries involving regex fields should specify their expressions in the
                  'ifn_regex' and 'cl_regex' parameters.
                  An asterisk wildcard '*' includes all results.
                  AVAILABLE FILTERS
                  applied_globally            last_modified
                  created_by                  modified_by
                  created_on                  value
                  name                        pattern
        ifn_regex -- The ifn_regex expression to filter exclusions by, used alongside expressions
                     specified in the filter query parameter. String.
        limit -- The maximum number of exclusions to return in this response.
                 [Integer, default: 100; max: 500]
                 Use with the offset parameter to manage pagination of results.
        offset -- The first exclusion to return, where 0 is the latest exclusion.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        sort -- The property to sort by. FQL syntax (e.g. last_behavior|asc).
                Available sort fields:
                applied_globally            last_modified
                created_by                  modified_by
                created_on                  value
                name                        pattern

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/queryIOAExclusionsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryIOAExclusionsV1",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    getIOAExclusionsV1 = get_exclusions
    createIOAExclusionsV1 = create_exclusions
    deleteIOAExclusionsV1 = delete_exclusions
    updateIOAExclusionsV1 = update_exclusions
    queryIOAExclusionsV1 = query_exclusions
    ss_ioa_exclusions_aggregates_v2 = get_ss_exclusion_aggregates
    ss_ioa_exclusions_get_reports_v2 = get_ss_exclusion_reports_v2
    ss_ioa_exclusions_get_v2 = get_ss_exclusion_rules_v2
    ss_ioa_exclusions_create_v2 = create_ss_exclusions
    ss_ioa_exclusions_update_v2 = update_ss_exclusions
    ss_ioa_exclusions_delete_v2 = delete_ss_exclusions
    ss_ioa_exclusions_matched_rule_v2 = get_ss_exclusion_matched_rules
    ss_ioa_exclusions_new_rules_v2 = get_default_ss_exclusions
    ss_ioa_exclusions_query_v2 = query_ss_exclusions


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
IOA_Exclusions = IOAExclusions  # pylint: disable=C0103
