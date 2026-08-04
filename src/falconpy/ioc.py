"""CrowdStrike Falcon Indicators of Compromise API interface class v2.

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
    aggregate_payload,
    indicator_payload,
    indicator_update_payload,
    indicator_report_payload,
    indicator_sdmf_query_v1_payload,
    )
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._ioc import _ioc_endpoints as Endpoints
from ._endpoint._iocs import _iocs_endpoints as LegacyEndpoints


class IOC(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def indicator_aggregate(self: object,
                            parameters: dict = None,
                            body: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get indicator aggregates as specified via json in request body.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.aggregate.v1

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
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
                    "field": "string",
                    "filter": "string",
                    "from": 0,
                    "include": "string",
                    "interval": "string",
                    "max_doc_count": 0,
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

        date_ranges : list[dict]
            If peforming a date range query specify the from and to date ranges.
            These can be in common date formats like 2019-07-18 or now.
        exclude : str
            Fields to exclude.
        field : str
            Term you want to aggregate on. If doing a date_range query,
            this is the date field you want to apply the date ranges to.
        filter : str
            Optional filter criteria in the form of an FQL query.
            For more information about FQL queries, see our FQL documentation in Falcon.
        from : int
        include : str
            Fields to include.
        interval : str
        max_doc_count : int
            Maximum number of documents.
        min_doc_count : int
            Minimum number of documents.
        missing : str
        name : str
            Scan name.
        q : str
            FQL syntax.
        ranges : list[dict]
        size : int
        sort : str
            FQL syntax.
        sub_aggregates : list[str]
        time_zone : str
        type : str

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            # IOC aggregate payload does NOT expect a list
            body = aggregate_payload(submitted_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_aggregate_v1",
            body=body,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_combined(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Combined for Indicators.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.combined.v1

        Keyword arguments
        -----------------
        after : str
            A pagination token used with the limit parameter to manage pagination of results.
            On your first request, don't provide an `after` token. On subsequent requests,
            provide the `after` token from the previous response to continue from that place
            in the results. To access more than 10k indicators, use the `after` parameter
            instead of `offset`.
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        from_parent : bool
            The filter for returning either only indicators for the request customer
            or its MSSP parents.
        limit : int
            The maximum records to return. [1-500]. Defaults to 100.
            Use with the offset parameter to manage pagination of results.
        offset : int
            The offset to start retrieving records from.
            Offset and After params are mutually exclusive.
            If none provided then scrolling will be used by default.
            To access more than 10K IOCs, use the `after` parameter instead of `offset`.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by (e.g. alias.desc or state.asc). FQL syntax.
            Available values
            action                          modified_by
            applied_globally                modified_on
            metadata.av_hits                metadata.original_filename.raw
            metadata.company_name.raw       metadata.product_name.raw
            created_by                      metadata.product_version
            created_on                      severity_number
            expiration                      source
            expired                         type
            metadata.filename.raw           value

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_combined_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def action_get(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Actions by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/action.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of Indicator ID(s) you wish to lookup.
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
            operation_id="action_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_indicators_report(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Launch an indicators report creation job.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/GetIndicatorsReport

        Keyword arguments
        -----------------
        body : dict
            full parameters payload, not required if using other keywords.
                {
                    "from_parent": true,
                    "report_format": "string",
                    "search": {
                        "filter": "string",
                        "query": "string",
                        "sort": "string"
                    }
                }
        filter : str
            FQL formatted string specifying the search filter.
            Overridden if 'search' keyword is provided.
        from_parent : bool
            Flag indicating if this indicator is defined in the parent.
        query : str
            FQL formatted string specifying the search query.
            Overridden if 'search' keyword is provided.
        report_format : str
            Format of the report.
        search : dict
            Search parameters. Strings are in FQL format. Dictionary.
            {
                "filter": "string",
                "query": "string",
                "sort": "string"
            }
        sort : str
            FQL formatted string specifying the search sort.
            Overridden if 'search' keyword is provided.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = indicator_report_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIndicatorsReport",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_get(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Indicators by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of Indicator ID(s) you wish to lookup.
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
            operation_id="indicator_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def indicator_create(self: object,
                         body: dict = None,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Indicators.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.create.v1

        Keyword arguments
        -----------------
        action : str
            Default action for the IOC.
        applied_globally : bool
            Is this IOC applied globally?
        body : dict
            full body payload, not required if keywords are used.
                {
                    "comment": "string",
                    "indicators": [
                        {
                        "action": "string",
                        "applied_globally": true,
                        "description": "string",
                        "expiration": "2021-10-22T10:40:39.372Z",
                        "host_groups": [
                            "string"
                        ],
                        "metadata": {
                            "filename": "string"
                        },
                        "mobile_action": "string",
                        "platforms": [
                            "string"
                        ],
                        "severity": "string",
                        "source": "string",
                        "tags": [
                            "string"
                        ],
                        "type": "string",
                        "value": "string"
                        }
                    ]
                }
        comment : str
            Audit log comment for the update.
        description : str
            Description for the IOC.
        expiration : str
            UTC formatted date.
        filename : str
            Filename to use in the metadata.
        host_groups : list[str]
            List of host groups to apply this IOC to.
        ignore_warnings : bool
            Set to true to ignore warnings and add all IOCs. Boolean. Default: False
        indicators : list[dict]
            List of indicators to create.
        metadata : str
            Dictionary containing the filename for the IOC.
            Not required if filename is used.
            {
                "filename": "string"
            }
        mobile_action : str
            Action to perform for mobile.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        platforms : str
            Platforms this IOC applies to.
        retrodetects : bool
            Whether to submit to retrodetects.
        severity : str
            Severity this IOC generates.
        source : str
            Source of the IOC.
        tags : list[str]
            List of Falcon Grouping Tags to apply this IOC to.
        type : str
            Type of indicator.
        value : str
            Value of the indicator.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = indicator_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_create_v1",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_delete(self: object,
                         *args,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete Indicators by IDs.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.delete.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of Indicator ID(s) you wish to delete.
        from_parent : bool
            Limit action to IOCs originating from the MSSP parent.
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
            operation_id="indicator_delete_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def indicator_update(self: object,
                         body: dict,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Indicators.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.update.v1

        Keyword arguments
        -----------------
        action : str
            Default action for the IOC.
        applied_globally : bool
            Is this IOC applied globally?
        body : dict
            full body payload, not required if keywords are used.
                {
                    "bulk_update": {
                        "action": "string",
                        "applied_globally": true,
                        "description": "string",
                        "expiration": "2021-10-22T11:03:16.123Z",
                        "filter": "string",
                        "from_parent": true,
                        "host_groups": [
                            "string"
                        ],
                        "mobile_action": "string",
                        "platforms": [
                            "string"
                        ],
                        "severity": "string",
                        "source": "string",
                        "tags": [
                            "string"
                        ]
                    },
                    "comment": "string",
                    "indicators": [
                        {
                            "action": "string",
                            "applied_globally": true,
                            "description": "string",
                            "expiration": "2021-10-22T11:03:16.123Z",
                            "host_groups": [
                                "string"
                            ],
                            "id": "string",
                            "metadata": {
                                "filename": "string"
                            },
                            "mobile_action": "string",
                            "platforms": [
                                "string"
                            ],
                            "severity": "string",
                            "source": "string",
                            "tags": [
                                "string"
                            ]
                        }
                    ]
                }
        bulk_update : dict
            Dictionary representing the indicator values to update in bulk.
        comment : str
            Audit log comment for the update.
        description : str
            Description for the IOC.
        expiration : str
            UTC formatted date.
        filename : str
            Filename to use in the metadata.
        from_parent : bool
            Flag indicating if this indicator originates from the parent.
        host_groups : list[str]
            List of host groups to apply this IOC to.
        id : str
            ID of the indicator to be updated. At least one ID must be specified using this
            keyword, or as part of the indicators list using the indicators keyword.
        indicators : list[dict]
            List of indicators to update.
        ignore_warnings : bool
            Set to true to ignore warnings and add all IOCs. Boolean. Default: False
        metadata : str
            Dictionary containing the filename for the IOC.
            Not required if filename is used.
            {
                "filename": "string"
            }
        mobile_action : str
            Action to perform for mobile.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        platforms : str
            Platforms this IOC applies to.
        retrodetects : bool
            Whether to submit to retrodetects.
        severity : str
            Severity this IOC generates.
        source : str
            Source of the IOC.
        tags : list[str]
            List of Falcon Grouping Tags to apply this IOC to.
        type : str
            Type of indicator.
        value : str
            Value of the indicator.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = indicator_update_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_update_v1",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def action_query(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query Actions.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/action.query.v1

        Keyword arguments
        -----------------
        limit : int
            Number of IDs to return.
        offset : str
            Starting index of overall result set from which to return IDs.
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
            operation_id="action_query_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_search(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for Indicators.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.search.v1

        Keyword arguments
        -----------------
        after : str
            A pagination token used with the limit parameter to manage pagination of results.
            On your first request, don't provide an `after` token. On subsequent requests,
            provide the `after` token from the previous response to continue from that place
            in the results. To access more than 10k indicators, use the `after` parameter
            instead of `offset`.
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        from_parent : bool
            The filter for returning either only indicators for the request customer
            or its MSSP parents.
        limit : int
            The maximum records to return. [1-500]. Defaults to 100.
            Use with the offset parameter to manage pagination of results.
        offset : int
            The offset to start retrieving records from.
            Offset and After params are mutually exclusive.
            If none provided then scrolling will be used by default.
            To access more than 10K IOCs, use the `after` parameter instead of `offset`.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by (e.g. alias.desc or state.asc). FQL syntax.
            Available values
            action                          modified_by
            applied_globally                modified_on
            metadata.av_hits                metadata.original_filename.raw
            metadata.company_name.raw       metadata.product_name.raw
            created_by                      metadata.product_version
            created_on                      severity_number
            expiration                      source
            expired                         type
            metadata.filename.raw           value

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_search_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def ioc_type_query(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query IOC types.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/ioc_type.query.v1

        Keyword arguments
        -----------------
        limit : int
            Number of IDs to return.
        offset : str
            Starting index of overall result set from which to return IDs.
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
            operation_id="ioc_type_query_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def platform_query(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query platforms.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/platform.query.v1

        Keyword arguments
        -----------------
        limit : int
            Number of IDs to return.
        offset : str
            Starting index of overall result set from which to return IDs.
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
            operation_id="platform_query_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def severity_query(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query severities.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/severity.query.v1

        Keyword arguments
        -----------------
        limit : int
            Number of IDs to return.
        offset : str
            Starting index of overall result set from which to return IDs.
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
            operation_id="severity_query_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def devices_count_legacy(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return the number of hosts in your customer account that have observed a given custom IOC.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesCount

        Keyword arguments
        -----------------
        type : str
            The type of indicator. String. Required.
            Valid types include:
            `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
            `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
            `domain`: A domain name. Length - min: 1, max: 200.
            `ipv4`: An IPv4 address. Must be a valid IP address.
            `ipv6`: An IPv6 address. Must be a valid IP address.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        value : str
            The string representation of the indicator.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=LegacyEndpoints,
            operation_id="DevicesCount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def devices_count(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return the number of hosts in your customer account that have observed a given custom IOC.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.get.device.count.v1

        Keyword arguments
        -----------------
        type : str
            The type of indicator. String. Required.
            Valid types include:
            `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
            `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
            `domain`: A domain name. Length - min: 1, max: 200.
            `ipv4`: An IPv4 address. Must be a valid IP address.
            `ipv6`: An IPv6 address. Must be a valid IP address.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        value : str
            The string representation of the indicator.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_get_device_count_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def devices_ran_on_legacy(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find hosts that have observed a given custom IOC.

        For details about those hosts, use the hosts API interface.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesRanOn

        Keyword arguments
        -----------------
        type : str
            The type of indicator. String. Required.
            Valid types include:
            `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
            `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
            `domain`: A domain name. Length - min: 1, max: 200.
            `ipv4`: An IPv4 address. Must be a valid IP address.
            `ipv6`: An IPv6 address. Must be a valid IP address.
        limit : str
            The first process to return, where 0 is the latest offset.
            Use with the offset parameter to manage pagination of results.
        offset : str
            The first process to return, where 0 is the latest offset.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        value : str
            The string representation of the indicator.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=LegacyEndpoints,
            operation_id="DevicesRanOn",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def devices_ran_on(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find hosts that have observed a given custom IOC.

        For details about those hosts, use the hosts API interface.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.get.devices.ran.on.v1

        Keyword arguments
        -----------------
        type : str
            The type of indicator. String. Required.
            Valid types include:
            `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
            `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
            `domain`: A domain name. Length - min: 1, max: 200.
            `ipv4`: An IPv4 address. Must be a valid IP address.
            `ipv6`: An IPv6 address. Must be a valid IP address.
        limit : str
            The first process to return, where 0 is the latest offset.
            Use with the offset parameter to manage pagination of results.
        offset : str
            The first process to return, where 0 is the latest offset.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        value : str
            The string representation of the indicator.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_get_devices_ran_on_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def processes_ran_on_legacy(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for processes associated with a custom IOC.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/ProcessesRanOn

        Keyword arguments
        -----------------
        type : str
            The type of indicator. String. Required.
            Valid types include:
            `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
            `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
            `domain`: A domain name. Length - min: 1, max: 200.
            `ipv4`: An IPv4 address. Must be a valid IP address.
            `ipv6`: An IPv6 address. Must be a valid IP address.
        limit : str
            The first process to return, where 0 is the latest offset.
            Use with the offset parameter to manage pagination of results.
        offset : str
            The first process to return, where 0 is the latest offset.
            Use with the limit parameter to manage pagination of results.
        device_id : str
            Specify a host's ID to return only processes from that host.
            Get a host's ID from get_device_details, the Falcon console,
            or the Streaming API.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        value : str
            The string representation of the indicator.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=LegacyEndpoints,
            operation_id="ProcessesRanOn",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def processes_ran_on(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for processes associated with a custom IOC.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.get.processes_ran_on.v1

        Keyword arguments
        -----------------
        type : str
            The type of indicator. String. Required.
            Valid types include:
            `sha256`: A hex-encoded sha256 hash string. Length - min: 64, max: 64.
            `md5`: A hex-encoded md5 hash string. Length - min 32, max: 32.
            `domain`: A domain name. Length - min: 1, max: 200.
            `ipv4`: An IPv4 address. Must be a valid IP address.
            `ipv6`: An IPv6 address. Must be a valid IP address.
        limit : str
            The first process to return, where 0 is the latest offset.
            Use with the offset parameter to manage pagination of results.
        offset : str
            The first process to return, where 0 is the latest offset.
            Use with the limit parameter to manage pagination of results.
        device_id : str
            Specify a host's ID to return only processes from that host. Get a host's ID from QueryDevicesByFilter,
            the Falcon console, or the Streaming API.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        value : str
            The string representation of the indicator.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_get_processes_ran_on_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def entities_processes(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """For the provided ProcessID retrieve the process details.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/entities.processes

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of Process ID(s) for the running process you want to lookup.
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
            endpoints=LegacyEndpoints,
            operation_id="entities_processes",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    # These names are acceptable and match the API operation IDs.
    # They are defined here for ease of use purposes.
    action_get_v1 = action_get
    action_query_v1 = action_query
    GetIndicatorsReport = get_indicators_report
    indicator_aggregate_v1 = indicator_aggregate
    indicator_combined_v1 = indicator_combined
    indicator_get_v1 = indicator_get
    indicator_create_v1 = indicator_create
    indicator_delete_v1 = indicator_delete
    indicator_update_v1 = indicator_update
    indicator_search_v1 = indicator_search
    ioc_type_query_v1 = ioc_type_query
    platform_query_v1 = platform_query
    severity_query_v1 = severity_query

    @force_default(defaults=["body"], default_types=["dict"])
    def indicator_sdmf_query_v1(self: object,
                                body: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute an SDMF data frame query against IOC indicators.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator_sdmf_query_v1

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
            body = indicator_sdmf_query_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_sdmf_query_v1",
            body=body
            )
    # Legacy operation IDs are ported from IOCS.py
    #                - jshcodes@CrowdStrike, see Discussion #319
    DevicesCount = devices_count_legacy
    indicator_get_device_count_v1 = devices_count
    DevicesRanOn = devices_ran_on_legacy
    indicator_get_devices_ran_on_v1 = devices_ran_on
    ProcessesRanOn = processes_ran_on_legacy
    indicator_get_processes_ran_on_v1 = processes_ran_on
