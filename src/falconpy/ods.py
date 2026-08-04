"""CrowdStrike Falcon ODS API interface class.

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
from typing import Union, Dict
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import (
    generic_payload_list,
    aggregate_payload,
    scheduled_scan_payload,
    )
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._ods import _ods_endpoints as Endpoints


class ODS(ServiceClass):
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

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_scan_hosts(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get aggregates on ODS scan-hosts data.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/aggregate-query-scan-host-metadata

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
            operation_id="aggregate_query_scan_host_metadata",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_scans(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get aggregates on ODS scan data.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/aggregate-scans

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
            operation_id="aggregate_scans",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_scheduled_scans(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get aggregates on ODS scheduled-scan data.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/aggregate-scheduled-scans

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
            operation_id="aggregate_scheduled_scans",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_malicious_files(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve malicious files by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/get-malicious-files-by-ids

        Keyword arguments
        -----------------
        ids : str or list[str]
            The scan IDs to retrieve the scan entities.
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
            operation_id="get_malicious_files_by_ids",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def cancel_scans(self: object, *args, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Cancel ODS scans for the given scan IDs.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/cancel-scans

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if ids is provided as a keyword.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            ID(s) of the scans to cancel.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = generic_payload_list(
                submitted_keywords=handle_single_argument(args, kwargs, "ids"), payload_value="ids"
                )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cancel_scans",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scan_hosts(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get scan hosts by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/get-scan-host-metadata-by-ids

        Keyword arguments
        -----------------
        ids : str or list[str]
            The scan host IDs to retrieve.
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
            operation_id="get_scan_host_metadata_by_ids",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    # This operation is no longer available
    # @force_default(defaults=["body"], default_types=["dict"])
    # def scans_report(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
    #     """Launch a scans report creation job.

    #     Keyword arguments:
    #     body -- full body payload, not required if ids is provided as a keyword.
    #             {
    #                 "is_schedule": true,
    #                 "report_format": "string",
    #                 "search": {
    #                     "filter": "string",
    #                     "sort": "string"
    #                 }
    #             }
    #     is_schedule -- Flag indicating if this report is scheduled. Boolean.
    #     filter -- FQL filter to filter the report. String. Overrides the value within
    #               the search dictionary if provided. String.
    #     report_format -- Format for the report. String.
    #     search -- Filter the report results. Dictionary.
    #     sort -- FQL sort string to use within the report. Overrides the value within
    #             the search dictionary if provided. String.

    #     This method only supports keywords for providing arguments.

    #     Returns: dict object containing API response.

    #     HTTP Method: POST

    #     Swagger URL
    #     https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/scans-report
    #     """
    #     if not body:
    #         body = scans_report_payload(passed_keywords=kwargs)

    #     return process_service_request(
    #         calling_object=self,
    #         endpoints=Endpoints,
    #         operation_id="scans_report",
    #         keywords=kwargs,
    #         body=body
    #         )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scans_v1(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get scans by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/get-scans-by-scan-ids

        Keyword arguments
        -----------------
        ids : str or list[str]
            The scan IDs to retrieve.
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
            operation_id="get_scans_by_scan_ids",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scans(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get scans by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/get-scans-by-scan-ids-v2

        Keyword arguments
        -----------------
        ids : str or list[str]
            The scan IDs to retrieve.
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
            operation_id="get_scans_by_scan_ids_v2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_scan(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create ODS scan and start it.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/create-scan

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if ids is provided as a keyword.
                {
                    "cloud_ml_level_detection": 0,
                    "cloud_ml_level_prevention": 0,
                    "cpu_priority": 0,
                    "description": "string",
                    "endpoint_notification": true,
                    "file_paths": [
                        "string"
                    ],
                    "host_groups": [
                        "string"
                    ],
                    "hosts": [
                        "string"
                    ]
                    "initiated_from": "string",
                    "max_duration": 0,
                    "max_file_size": 0,
                    "pause_duration": 0,
                    "quarantine": true,
                    "scan_exclusions": [
                        "string"
                    ],
                    "sensor_ml_level_detection": 0,
                    "sensor_ml_level_prevention": 0
                }
        cloud_ml_level_detection : int
            ML detection level.
        cloud_ml_level_prevention : int
            ML prevention level.
        cpu_priority : int
            Scan host CPU priority.
        description : str
            Scan description.
        endpoint_notification : bool
            Flag indicating if the endpoint should be notified.
        file_paths : str or list[str]
            File paths to be scanned.
        host_groups : str or list[str]
            Host group IDs to scan.
        hosts : str or list[str]
            Host AIDs to scan.
        ignored_by_channelfile : dict
            Flag indicating if this scan is ignored by channelfiles. Boolean.
            Overrides the value specified in the schedule.
        initiated_from : str
            Endpoint the scan was initiated from.
        interval : dict
            Scan schedule interval in seconds. Integer. Overrides the value specified in
            the schedule.
        max_duration : int
            Maximum duration in seconds for the scan.
        max_file_size : int
            Maximum file size for files scanned.
        pause_duration : int
            Time in seconds to pause during the scan.
        quarantine : bool
            Quarantine malicious files identified by the scan.
        scan_exclusions : str or list[str]
            List of file path globs to exclude from the scan.
        start_timestamp : dict
            Starting timestamp for the scan. String. Overrides the value specified
            in the schedule.
        sensor_ml_level_detection : int
            Endpoint sensor ML detection level.
        sensor_ml_level_prevention : int
            Endpoint sensor ML prevention level.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = scheduled_scan_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_scan",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scheduled_scans(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get scheduled scans by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/get-scheduled-scans-by-scan-ids

        Keyword arguments
        -----------------
        ids : str or list[str]
            The scan IDs to retrieve.
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
            operation_id="get_scheduled_scans_by_scan_ids",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def schedule_scan(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create ODS scan and start or schedule scan for the given scan request.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/schedule-scan

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if ids is provided as a keyword.
                {
                    "cloud_ml_level_detection": 0,
                    "cloud_ml_level_prevention": 0,
                    "cpu_priority": 0,
                    "description": "string",
                    "endpoint_notification": true,
                    "file_paths": [
                        "string"
                    ],
                    "host_groups": [
                        "string"
                    ],
                    "initiated_from": "string",
                    "max_duration": 0,
                    "max_file_size": 0,
                    "pause_duration": 0,
                    "quarantine": true,
                    "scan_exclusions": [
                        "string"
                    ],
                    "scan_inclusions": [
                        "string"
                    ],
                    "schedule": {
                        "ignored_by_channelfile": true,
                        "interval": 0,
                        "start_timestamp": "string"
                    },
                    "sensor_ml_level_detection": 0,
                    "sensor_ml_level_prevention": 0
                }
        cloud_ml_level_detection : int
            ML detection level.
        cloud_ml_level_prevention : int
            ML prevention level.
        cpu_priority : int
            Scan host CPU priority.
        description : str
            Scan description.
        endpoint_notification : bool
            Flag indicating if the endpoint should be notified.
        file_paths : str or list[str]
            File paths to be scanned.
        host_groups : str or list[str]
            Host group IDs to scan.
        ignored_by_channelfile : dict
            Flag indicating if this scan is ignored by channelfiles. Boolean.
            Overrides the value specified in the schedule.
        initiated_from : str
            Endpoint the scan was initiated from.
        interval : dict
            Scan schedule interval in seconds. Integer. Overrides the value specified in
            the schedule.
        max_duration : int
            Maximum duration in seconds for the scan.
        max_file_size : int
            Maximum file size for files scanned.
        pause_duration : int
            Time in seconds to pause during the scan.
        quarantine : bool
            Quarantine malicious files identified by the scan.
        scan_exclusions : str or list[str]
            List of file path globs to exclude from the scan.
        scan_inclusions : str or list[str]
            List of file path globs to include the scan.
        schedule : dict
            Details related to the scan schedule. Dictionary.
            {
                "ignored_by_channelfile": true,
                "interval": 0,
                "start_timestamp": "string"
            }
        start_timestamp : dict
            Starting timestamp for the scan. String. Overrides the value specified
            in the schedule.
        sensor_ml_level_detection : int
            Endpoint sensor ML detection level.
        sensor_ml_level_prevention : int
            Endpoint sensor ML prevention level.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = scheduled_scan_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="schedule_scan",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_scheduled_scans(self: object,
                               *args,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete ODS scheduled scans for the given IDs.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/delete-scheduled-scans

        Keyword arguments
        -----------------
        filter : str
            A FQL compatible query.
        ids : str or list[str]
            List of scan IDs to delete.
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
            operation_id="delete_scheduled_scans",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_malicious_files(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for malicious files.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/query-malicious-files

        Keyword arguments
        -----------------
        filter : str
            A FQL compatible query string. String.
            Available filters:
            id                filename
            cid               hash
            scan_id           pattern_id
            host_id           severity
            host_scan_id      quarantined
            filepath          last_updated
        limit : int (1-500)
            The maximum number of records to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. id|desc or filename|asc).
            Available sort fields:
            id                  hash
            scan_id             pattern_id
            host_id             severity
            host_scan_id        last_updated
            filename

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_malicious_files",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_scan_hosts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for scan hosts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/query-scan-host-metadata

        Keyword arguments
        -----------------
        filter : str
            A FQL compatible query string. String.
            Available filters:
            id                    filecount.quarantined
            cid                   filecount.skipped
            profile_id            affected_hosts_count
            host_id               status
            scan_id               severity
            host_scan_id          completed_on
            filecount.scanned     started_on
            filecount.malicious   last_updated
        limit : int (1-500)
            The maximum number of records to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. id|desc or status|asc).
            Available sort fields:
            id                      filecount.skipped
            scan_id                 status
            host_id                 severity
            filecount.scanned       started_on
            filecount.malicious     completed_on
            filecount.quarantined   last_updated

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_scan_host_metadata",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_scans(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for scans.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/query-scans

        Keyword arguments
        -----------------
        filter : str
            A FQL compatible query string. String.
            Available filters:
            id                    filecount.quarantined
            cid                   filecount.skipped
            profile_id            created_by
            initiated_from        status
            affected_hosts_count  severity
            description.keyword   scan_completed_on
            filecount.scanned     scan_started_on
            filecount.malicious   created_on
            last_updated          description
            targeted_host_count   missing_host_count
            targeted_platforms    targeted_platforms.keyword
        limit : int (1-500)
            The maximum number of records to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. id|desc or status|asc).
            Available sort fields:
            id                      affected_hosts_count
            initiated_from          status
            description.keyword     severity
            filecount.scanned       scan_started_on
            filecount.malicious     scan_completed_on
            filecount.quarantined   created_on
            filecount.skipped       created_by
            last_updated            description

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_scans",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_scheduled_scans(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for scheduled scans.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ods/query-scheduled-scans

        Keyword arguments
        -----------------
        filter : str
            A FQL compatible query string. String.
            Available filters:
              channel_file_status         created_by
              created_on                  deleted
              description                 description.keyword
              id                          initiated_from
              last_updated                schedule.Interval
              schedule.start_timestamp    status
              targeted_platforms
        limit : int (1-500)
            The maximum number of records to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. id|desc or status|asc).
            Available sort fields:
            created_by|asc                   created_by|desc
            created_on|asc                   created_on|desc
            description.keyword|asc          description.keyword|desc
            description|asc                  description|desc
            id|asc                           id|desc
            last_updated|asc                 last_updated|desc
            schedule.interval|asc            schedule.interval|desc
            schedule.start_timestamp|asc     schedule.start_timestamp|desc
            status|asc                       status|desc
            targeted_host_count|asc          targeted_host_count|desc

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_scheduled_scans",
            keywords=kwargs,
            params=parameters
            )

    get_malicious_files_by_ids = get_malicious_files
    get_scan_host_metadata_by_ids = get_scan_hosts
    get_scans_by_scan_ids = get_scans
    get_scans_by_scan_ids_v1 = get_scans_v1
    get_scans_by_scan_ids_v2 = get_scans
    get_scheduled_scans_by_scan_ids = get_scheduled_scans
    query_scan_host_metadata = query_scan_hosts
    aggregate_query_scan_host_metadata = aggregate_scan_hosts
