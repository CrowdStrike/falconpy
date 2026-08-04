"""CrowdStrike Falcon Detections API interface class.

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
from ._util import force_default, process_service_request
from ._payload import generic_payload_list, update_detects_payload
from ._payload import aggregate_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._detects import _detects_endpoints as Endpoints
#  _____                                     __            __
# |     \.-----.-----.----.-----.----.---.-.|  |_.-----.--|  |
# |  --  |  -__|  _  |   _|  -__|  __|  _  ||   _|  -__|  _  |
# |_____/|_____|   __|__| |_____|____|___._||____|_____|_____|
#              |__|
#
# This service collection is deprecated.
# Developers should leverage operations from the Alerts service collection.


class Detects(ServiceClass):
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
    def get_aggregate_detects(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get detect aggregates as specified via json in request body.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/GetAggregateDetects

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
            # Similar to 664: Detects aggregates expects a list
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAggregateDetects",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_detects_by_ids(self: object, *args, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Modify the state, assignee, and visibility of detections.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/UpdateDetectsByIdsV2

        Keyword arguments
        -----------------
        assigned_to_uuid : str
            A user ID to assign the detection to.
        body : dict
            full body payload, not required when using other keywords.
                {
                    "assigned_to_uuid": "string",
                    "comment": "string",
                    "ids": [
                        "string"
                    ],
                    "new_behaviors_processed": [
                        "string"
                    ],
                    "show_in_ui": true,
                    "status": "string"
                }
        comment : str
            Optional comment to add to the detection. Comments are displayed with
            the detection in Falcon and are usually used to provide context or
            notes for other Falcon users. A detection can have multiple comments
            over time.
        ids : str or list[str]
            ID(s) of the detection to update.
        new_behaviors_processed : str or list[str]
        show_in_ui : bool
            Boolean determining if this detection is displayed in the Falcon
            console.
        status : str
            Current status of the detection. Allowed values:
            ignored           new
            in_progress       true_positive
            false_positive

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
            body = update_detects_payload(current_payload=generic_payload_list(
                                                submitted_arguments=args,
                                                submitted_keywords=kwargs,
                                                payload_value="ids"
                                                ),
                                          passed_keywords=kwargs
                                          )
        if body.get("comment", None):
            if not body.get("show_in_ui", None) and not body.get("status", None):
                # Issue 563
                body["show_in_ui"] = True

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateDetectsByIdsV2",
            body=body,
            body_validator={
                    "assigned_to_uuid": str,
                    "comment": str,
                    "ids": list,
                    "show_in_ui": bool,
                    "status": str
                    } if self.validate_payloads else None,
            body_required=["ids"] if self.validate_payloads else None
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_detect_summaries(self: object, *args, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """View information about detections.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/GetDetectSummaries

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when ids keyword is provided.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            ID(s) of the detections to retrieve.

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
            body = generic_payload_list(submitted_arguments=args,
                                        submitted_keywords=kwargs,
                                        payload_value="ids"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDetectSummaries",
            body=body,
            body_validator={"ids": list} if self.validate_payloads else None,
            body_required=["ids"] if self.validate_payloads else None
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_detects(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for detection IDs that match a given query.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/QueryDetects

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
                      An asterisk wildcard '*' includes all results.
                      AVAILABLE FILTERS
                      General
                      ----------------------------------------------------
                      adversary_ids             max_confidence
                      assigned_to_name          max_severity
                      cid                       max_severity_displayname
                      date_updated              seconds_to_triaged
                      detection_id              seconds_to_resolved
                      first_behavior            status
                      last_behavior
                      Behavioral (behaviors.filter) Ex: behaviors.md5
                      ----------------------------------------------------
                      alleged_filetype          pattern_disposition
                      behavior_id               scenario
                      cmdline                   severity
                      confidence                sha256
                      control_graph_id          tactic
                      device_id                 technique
                      filename                  timestamp
                      ioc_source                triggering_process_id
                      ioc_type                  triggering_process_graph_id
                      ioc_value                 user_id
                      md5                       user_name
                      objective
                      parent_details.parent_cmdline
                      parent_details.parent_md5
                      parent_details.parent_process_id
                      parent_details.parent_process_graph_id
                      parent_details.parent_sha256
                      Devices (device.filter)  Ex: device.platform_name
                      ----------------------------------------------------
                      agent_load_flags          machine_domain
                      agent_local_time          major_version
                      agent_version             minor_version
                      bios_manufacturer         modified_timestamp
                      bios_version              os_version
                      cid                       ou
                      config_id_base            platform_id
                      config_id_build           platform_name
                      config_id_platform        product_type
                      cpu_signature             product_type_desc
                      device_id                 release_group
                      external_ip               reduced_functionality_mode
                      first_seen                serial_number
                      hostname                  site_name
                      last_seen                 status
                      local_ip                  system_product_name
                      mac_address               system_manufacturer
                      Misc
                      ----------------------------------------------------
                      hostinfo.domain
                      hostinfo.active_directory_dn_display
                      quarantined_files.id      quarantined_files.state
                      quarantined_files.paths   quarantined_files.sha256
            For more detail regarding filtering options, please review:
            https://falcon.crowdstrike.com/documentation/86/detections-monitoring-apis#find-detections
        limit : int
            The maximum number of detections to return in this response.
            [Integer, default: 100; max: 9999]
            Use with the offset parameter to manage pagination of results.
        offset : int
            The first detection to return, where 0 is the latest detection.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Search all detection metadata for the provided.
        sort : str
            The property to sort by. FQL syntax (e.g. last_behavior|asc).
            Available sort fields:
            adversary_id        last_behavior
            devices.hostname    max_confidence
            first_behavior      max_severity

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryDetects",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetAggregateDetects = get_aggregate_detects
    UpdateDetectsByIdsV2 = update_detects_by_ids
    GetDetectSummaries = get_detect_summaries
    QueryDetects = query_detects
