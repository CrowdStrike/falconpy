"""CrowdStrike Falcon ScanningOrchestrator API interface class.

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
from ._payload import create_schedules_payload, trigger_scan_by_schedule_payload, update_schedules_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._scanning_orchestrator import _scanning_orchestrator_endpoints as Endpoints


class ScanningOrchestrator(ServiceClass):
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
    def get_combined_schedules(self: object,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get combined scanning schedules.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/scanning-orchestrator/get_combined_schedules

        Keyword arguments
        -----------------
        limit : int
            Number of results to return.
        offset : int
            Starting offset for pagination.
        sort : str
            Sort field and direction. Available fields: scan_product, provider_type, enabled, name, created_at. Example:
            name|asc.
        filter : str
            FQL filter expression. Available fields: scan_product, provider_type, enabled, name, created_at. Example:
            enabled:true.
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
            operation_id="get_combined_schedules",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def trigger_scan_by_schedule(self: object,
                                 body: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Trigger scan by schedule IDs.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/scanning-orchestrator/trigger_scan_by_schedule

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : list
            The ids value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = trigger_scan_by_schedule_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="trigger_scan_by_schedule",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_schedules(self: object,
                      *args,
                      parameters: dict = None,
                      **kwargs
                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get scanning schedules.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/scanning-orchestrator/get_schedules

        Keyword arguments
        -----------------
        ids : str or list[str]
            Schedule IDs to retrieve.
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
            operation_id="get_schedules",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_schedules(self: object,
                         body: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create scanning schedules.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/scanning-orchestrator/create_schedules

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "account_ids": [
                                "string"
                            ],
                            "all_accounts": true,
                            "all_regions": true,
                            "cadence": {
                                "unit": "string",
                                "value": 0
                            },
                            "cloud_group_ids": [
                                "string"
                            ],
                            "dspm_scanning_config": {
                                "classification_scan_mode": "string",
                                "scan_type": "string"
                            },
                            "enable": true,
                            "name": "string",
                            "provider_type": "string",
                            "scan_product": "string",
                            "selected_regions": [
                                "string"
                            ],
                            "service_names": [
                                "string"
                            ]
                        }
                    ]
                }
        resources : list
            The resources value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = create_schedules_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_schedules",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_schedules(self: object,
                         *args,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete scanning schedules.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/scanning-orchestrator/delete_schedules

        Keyword arguments
        -----------------
        ids : str or list[str]
            Schedule IDs to delete.
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
            operation_id="delete_schedules",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_schedules(self: object,
                         body: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update scanning schedules.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/scanning-orchestrator/update_schedules

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "asset_filter": {
                                "aws": {
                                    "account_ids": [
                                        "string"
                                    ],
                                    "all_accounts": true,
                                    "all_regions": true,
                                    "regions": [
                                        "string"
                                    ],
                                    "service_names": [
                                        "string"
                                    ]
                                },
                                "azure": {
                                    "all_locations": true,
                                    "all_subscriptions": true,
                                    "locations": [
                                        "string"
                                    ],
                                    "service_names": [
                                        "string"
                                    ],
                                    "subscription_ids": [
                                        "string"
                                    ]
                                },
                                "cloud_groups": {
                                    "cloud_group_ids": [
                                        "string"
                                    ],
                                    "provider_account_ids": [
                                        "string"
                                    ],
                                    "service_names": [
                                        "string"
                                    ]
                                },
                                "gcp": {
                                    "all_projects": true,
                                    "all_regions": true,
                                    "project_ids": [
                                        "string"
                                    ],
                                    "regions": [
                                        "string"
                                    ],
                                    "service_names": [
                                        "string"
                                    ]
                                },
                                "provider_type": "string",
                                "scan_product": "string"
                            },
                            "cadence": {
                                "unit": "string",
                                "value": 0
                            },
                            "enable": true,
                            "id": "string",
                            "name": "string",
                            "scan_config": {
                                "dspm_scanning_config": {
                                    "classification_scan_mode": "string",
                                    "scan_type": "string"
                                }
                            }
                        }
                    ]
                }
        resources : list
            The resources value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_schedules_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_schedules",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_service_types(self: object,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get allowed service types.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/scanning-orchestrator/get_service_types

        Keyword arguments
        -----------------
        scan_product : str
            Scan product filter. Available values: dspm_scanning, vulnerability_scanning.
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
            operation_id="get_service_types",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_schedules(self: object,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search scanning schedules.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/scanning-orchestrator/search_schedules

        Keyword arguments
        -----------------
        limit : int
            Number of results to return.
        offset : int
            Starting offset for pagination.
        sort : str
            Sort field and direction. Available fields: scan_product, provider_type, enabled, name, created_at. Example:
            name|asc.
        filter : str
            FQL filter expression. Available fields: scan_product, provider_type, enabled, name, created_at. Example:
            enabled:true.
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
            operation_id="search_schedules",
            keywords=kwargs,
            params=parameters
            )
