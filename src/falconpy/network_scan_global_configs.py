"""CrowdStrike Falcon NetworkScanGlobalConfigs API interface class.

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
from ._payload import network_scan_global_configs_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._network_scan_global_configs import _network_scan_global_configs_endpoints as Endpoints


class NetworkScanGlobalConfigs(ServiceClass):
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

    def get_global_configs(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get global configuration settings for network scanning for the CID.

        Keyword arguments: This method does not accept keyword arguments.

        Arguments: This method does not accept arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-global-configs/get_global_configs
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_global_configs"
        )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_global_configs(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update global configuration settings for network scanning using provided specifications.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "auto_confirm_ownership": {
                        "min_managed_assets": integer
                    },
                    "max_concurrent_tasks": integer,
                    "network_scanning_enabled": boolean,
                    "scan_exclusion": {
                        "exclude_all_managed_hosts": boolean,
                        "host_groups": [
                            "string"
                        ],
                        "hosts": [
                            "string"
                        ],
                        "zone_level_scan_exclusions": [
                            {
                                "cidrs": [ "string" ],
                                "host_groups": [ "string" ],
                                "hosts": [ "string" ],
                                "scan_zone_id": "string"
                            }
                        ]
                    },
                    "scanners": [
                        {
                            "enabled": boolean,
                            "id": "string",
                            "type": "string"
                        }
                    ],
                    "scanners_exclusion": [
                        {
                            "enabled": boolean,
                            "id": "string",
                            "type": "string"
                        }
                    ]
                }
        auto_confirm_ownership -- Conditions for auto confirmation of network ownership. Dictionary.
        max_concurrent_tasks -- Maximum number of scan tasks to run in parallel. Integer.
        network_scanning_enabled -- Flag to enable or disable network scanning.
                                    Setting to False attempts to stop ongoing scans
                                    and prevents further scans from executing. Boolean.
        scan_exclusion -- Scan target exclusions including common as well as zone-level exclusions
                          (individual IPs, IP ranges, CIDRs). Required. Dictionary.
        scanners -- List of assets that will act as eligible scanners. List of dictionaries.
        scanners_exclusion -- List of assets that will always be excluded from being selected
                              as scanners. List of dictionaries.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-global-configs/update_global_configs
        """
        if not body:
            body = network_scan_global_configs_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_global_configs",
            body=body
        )

    # Backward compatibility aliases
    GetGlobalConfigs = get_global_configs
    UpdateGlobalConfigs = update_global_configs
