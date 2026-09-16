"""CrowdStrike Falcon Audit API interface class.

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
from ._payload import create_audit_query_job_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._audit import _audit_endpoints as Endpoints


class Audit(ServiceClass):
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

    @force_default(defaults=["parameters"], default_types=["dict"])
    def export_audit_query_results(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Export the results of a completed query job in CSV or JSON format.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/audit/ExportQueryResults

        Keyword arguments
        -----------------
        id : str
            Job ID from a previously created query job.
        format : str
            Export format: csv or json.
        include_descriptions : bool
            When true, includes descriptions for category and action fields (default: false)
        include_extension_metadata : bool
            When true, filters extension keys based on audit definition YAML and includes
            descriptions for extension keys (default: false)
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
            operation_id="ExportQueryResults",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_audit_query_results(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve the results of a completed query job with pagination.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/audit/GetQueryResults

        Keyword arguments
        -----------------
        id : str
            Job ID from a previously created query job.
        offset : int
            Starting position for pagination (default: 0)
        limit : int
            Maximum number of records to return (default: 100)
        include_descriptions : bool
            When true, includes descriptions for category and action fields (default: false)
        include_extension_metadata : bool
            When true, filters extension keys based on audit definition YAML and includes
            descriptions for extension keys (default: false)
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
            operation_id="GetQueryResults",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def poll_audit_query_status(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Check the status of a previously created query job.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/audit/PollQueryJobStatus

        Keyword arguments
        -----------------
        id : str or list[str]
            Job ID from a previously created query job.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PollQueryJobStatus",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_audit_query_job(self: object,
                               body: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create an asynchronous query job to retrieve audit log entries based on specified filters.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/audit/CreateQueryJob

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "action": [
                        "string"
                    ],
                    "action_description": [
                        "string"
                    ],
                    "actor_id": [
                        "string"
                    ],
                    "actor_ip": [
                        "string"
                    ],
                    "actor_type": [
                        "string"
                    ],
                    "category": [
                        "string"
                    ],
                    "category_description": [
                        "string"
                    ],
                    "cid": [
                        "string"
                    ],
                    "end_time": "string",
                    "event_id": [
                        "string"
                    ],
                    "event_version": [
                        "string"
                    ],
                    "extensions": "string",
                    "geo_city": [
                        "string"
                    ],
                    "geo_country": [
                        "string"
                    ],
                    "sort": "string",
                    "start_time": "string",
                    "target_display_name": [
                        "string"
                    ],
                    "target_id": [
                        "string"
                    ],
                    "target_type": [
                        "string"
                    ],
                    "user_agent": [
                        "string"
                    ]
                }
        action : list
            The action value.
        action_description : list
            The action_description value.
        actor_id : list
            The actor_id value.
        actor_ip : list
            The actor_ip value.
        actor_type : list
            The actor_type value.
        category : list
            The category value.
        category_description : list
            The category_description value.
        cid : list
            The cid value.
        end_time : str
            The end_time value.
        event_id : list
            The event_id value.
        event_version : list
            The event_version value.
        extensions : dict
            The extensions value.
        geo_city : list
            The geo_city value.
        geo_country : list
            The geo_country value.
        sort : str
            The sort value.
        start_time : str
            The start_time value.
        target_display_name : list
            The target_display_name value.
        target_id : list
            The target_id value.
        target_type : list
            The target_type value.
        user_agent : list
            The user_agent value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = create_audit_query_job_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateQueryJob",
            body=body
            )
    ExportQueryResults = export_audit_query_results
    GetQueryResults = get_audit_query_results
    PollQueryJobStatus = poll_audit_query_status
    CreateQueryJob = create_audit_query_job
