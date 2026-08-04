"""Falcon Complete Dashboard API Interface Class.

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
from ._util import process_service_request, force_default
from ._payload import aggregate_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._falcon_complete_dashboard import _falcon_complete_dashboard_endpoints as Endpoints


class CompleteDashboard(ServiceClass):
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
    def aggregate_alerts(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate allowlist ticket values based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/AggregateAlerts

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
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
        date_ranges : list[dict]
            If peforming a date range query specify the from and to date ranges.
            These can be in common date formats like 2019-07-18 or now.
        field : str
            Term you want to aggregate on. If doing a date_range query,
            this is the date field you want to apply the date ranges to.
        filter : str
            Optional filter criteria in the form of an FQL query.
            For more information about FQL queries, see our FQL documentation in Falcon.
        interval : str
        min_doc_count : int
            Minimum number of documents required to match.
        missing : str
        name : str
            Name of the aggregation.
        q : str
            FQL syntax.
        ranges : list[dict]
        size : int
            Size limit to apply to the queries.
        sort : str
            FQL syntax.
        sub_aggregates : list[str]
        time_zone : str
        type : str
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateAlerts",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_allow_list(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate allowlist ticket values based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/AggregateAllowList

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
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
        date_ranges : list[dict]
            If peforming a date range query specify the from and to date ranges.
            These can be in common date formats like 2019-07-18 or now.
        field : str
            Term you want to aggregate on. If doing a date_range query,
            this is the date field you want to apply the date ranges to.
        filter : str
            Optional filter criteria in the form of an FQL query.
            For more information about FQL queries, see our FQL documentation in Falcon.
        interval : str
        min_doc_count : int
            Minimum number of documents required to match.
        missing : str
        name : str
            Name of the aggregation.
        q : str
            FQL syntax.
        ranges : list[dict]
        size : int
            Size limit to apply to the queries.
        sort : str
            FQL syntax.
        sub_aggregates : list[str]
        time_zone : str
        type : str
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateAllowList",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_block_list(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate blocklist ticket values based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/AggregateBlockList

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
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
                ]
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
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateBlockList",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_device_count_collection(self: object,
                                          body: list = None,
                                          **kwargs
                                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate host/devices count based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /Falcon%20Complete%20Dashboard/AggregateDeviceCountCollection

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
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
                ]
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
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            methods="POST",
            operation_id="AggregateDeviceCountCollection",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_escalations(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate escalation ticket values based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/AggregateEscalations

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
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
                ]
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
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateEscalations",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_fc_incidents(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate incident values based on the matched filter.

        DECOMMISSIONED: This operation has been decommissioned by CrowdStrike.
        Calls to this method will return a 410 status code.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/AggregateFCIncidents

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
            operation_id="AggregateFCIncidents",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_incident_ids_by_filter(self: object,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve incidents that match the provided filter criteria with scrolling enabled.

        DECOMMISSIONED: This operation has been decommissioned by CrowdStrike.
        Calls to this method will return a 410 status code.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/QueryIncidentIdsByFilter

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
            operation_id="QueryIncidentIdsByFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_prevention_policy(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate prevention policy values based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/AggregatePreventionPolicy

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
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
                ]
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
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregatePreventionPolicy",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_remediations(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate remediation ticket values based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/AggregateRemediations

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
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
                ]
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
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateRemediations",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_sensor_update_policy(self: object,
                                       body: list = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate sensor update policy values based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/AggregateSensorUpdatePolicy

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
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
                ]
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
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateSensorUpdatePolicy",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_support_issues(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate device count values based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/AggregateSupportIssues

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
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
                ]
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
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateSupportIssues",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_total_device_counts(self: object,
                                      body: list = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve aggregate device count values based on the matched filter.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /Falcon%20Complete%20Dashboard/AggregateTotalDeviceCounts

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
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
                ]
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
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateTotalDeviceCounts",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_alert_ids_by_filter_v1(self: object,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Alerts Ids for epp that match the provided FQL filter criteria with scrolling enabled.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/QueryAlertIdsByFilter

        Keyword arguments
        -----------------
        filter : str
            Optional filter and sort criteria in the form of an FQL query.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort on, followed by a dot `.`, followed by the sort direction.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryAlertIdsByFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_alert_ids_by_filter(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Alerts Ids for epp, idp and ngsiem that match the provided FQL filter criteria with scrolling enabled.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/QueryAlertIdsByFilterV2

        Keyword arguments
        -----------------
        filter : str
            Optional filter and sort criteria in the form of an FQL query.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort on, followed by a dot `.`, followed by the sort direction.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryAlertIdsByFilterV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_allow_list_filter(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve allowlist tickets that match the provided filter criteria with scrolling enabled.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/QueryAllowListFilter

        Keyword arguments
        -----------------
        filter : str
            Optional filter and sort criteria in the form of an FQL query.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort on, followed by a dot `.`, followed by the sort direction.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryAllowListFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_block_list_filter(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve block list tickets that match the provided filter criteria with scrolling enabled.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Falcon%20Complete%20Dashboard/QueryBlockListFilter

        Keyword arguments
        -----------------
        filter : str
            Optional filter and sort criteria in the form of an FQL query.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort on, followed by a dot `.`, followed by the sort direction.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryBlockListFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_device_count_collection_queries_by_filter(self: object,
                                                      parameters: dict = None,
                                                      **kwargs
                                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve device count collection Ids that match the provided FQL filter, criteria with scrolling enabled.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /Falcon%20Complete%20Dashboard/GetDeviceCountCollectionQueriesByFilter

        Keyword arguments
        -----------------
        filter : str
            Optional filter and sort criteria in the form of an FQL query.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort on, followed by a dot `.`, followed by the sort direction.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDeviceCountCollectionQueriesByFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_escalations_filter(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve escalation tickets that match the provided filter criteria with scrolling enabled.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /Falcon%20Complete%20Dashboard/QueryEscalationsFilter

        Keyword arguments
        -----------------
        filter : str
            Optional filter and sort criteria in the form of an FQL query.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort on, followed by a dot `.`, followed by the sort direction.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryEscalationsFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_remediations_filter(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve remediation tickets that match the provided filter criteria with scrolling enabled.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /Falcon%20Complete%20Dashboard/QueryRemediationsFilter

        Keyword arguments
        -----------------
        filter : str
            Optional filter and sort criteria in the form of an FQL query.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort on, followed by a dot `.`, followed by the sort direction.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryRemediationsFilter",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    AggregateAlerts = aggregate_alerts
    AggregateAllowList = aggregate_allow_list
    AggregateBlockList = aggregate_block_list
    AggregateDeviceCountCollection = aggregate_device_count_collection
    AggregateEscalations = aggregate_escalations
    AggregateFCIncidents = aggregate_fc_incidents
    AggregatePreventionPolicy = aggregate_prevention_policy
    AggregateRemediations = aggregate_remediations
    AggregateSensorUpdatePolicy = aggregate_sensor_update_policy
    AggregateSupportIssues = aggregate_support_issues
    AggregateTotalDeviceCounts = aggregate_total_device_counts
    QueryAlertIdsByFilterV1 = query_alert_ids_by_filter_v1
    QueryAlertIdsByFilter = query_alert_ids_by_filter_v1
    QueryAlertIdsByFilterV2 = query_alert_ids_by_filter
    QueryAllowListFilter = query_allow_list_filter
    QueryBlockListFilter = query_block_list_filter
    GetDeviceCountCollectionQueriesByFilter = get_device_count_collection_queries_by_filter
    QueryEscalationsFilter = query_escalations_filter
    QueryIncidentIdsByFilter = query_incident_ids_by_filter
    QueryRemediationsFilter = query_remediations_filter


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Complete_Dashboard = CompleteDashboard  # pylint: disable=C0103
