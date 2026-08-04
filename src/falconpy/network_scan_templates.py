"""CrowdStrike Falcon NetworkScanTemplates API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |        FalconPy
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
from ._payload import network_scan_template_create_payload, network_scan_template_update_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._network_scan_templates import _network_scan_templates_endpoints as Endpoints


class NetworkScanTemplates(ServiceClass):
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
    def get_template_configs(self: object,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get details on the network scan template configurations.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/get_template_configs

        Keyword arguments
        -----------------
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
            operation_id="get_template_configs",
            keywords=kwargs,
            params=parameters
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_templates(self: object,
                      *args,
                      parameters: dict = None,
                      **kwargs
                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get templates by their IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/get_templates

        Keyword arguments
        -----------------
        ids : str or list[str]
            IDs of templates to be retrieved (Min: 1, Max: 100)
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
            operation_id="get_templates",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
        )

    @force_default(defaults=["body"], default_types=["list"])
    def create_templates(self: object,
                         body: list = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create templates using provided specifications.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/create_templates

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a list of dictionaries in JSON format. Not required if using other keywords.
                [
                    {
                        "active_check_level": "string",
                        "additional_tcp_ports": [
                            "string"
                        ],
                        "additional_udp_ports": [
                            "string"
                        ],
                        "auto_include_new_detections": boolean,
                        "detections": [
                            "string"
                        ],
                        "ignore_tcp_resets": boolean,
                        "name": "string",
                        "ports_scan_level": "string",
                        "scan_intensity": "string",
                        "type": "string"
                    }
                ]
        active_check_level : str (required)
            The active check level associated with the template.
            Allowed values: active_check_safe_only, active_check_all.
        additional_tcp_ports : str or list[str]
            Additional TCP ports associated with the template.
        additional_udp_ports : str or list[str]
            Additional UDP ports associated with the template.
        auto_include_new_detections : bool
            Automatically include new detections in the template.
        detections : str or list[str]
            Detections associated with the template.
        ignore_tcp_resets : bool
            Ignore TCP resets associated with the template.
        name : str (required)
            The name given to the template.
        ports_scan_level : str (required)
            The port scan level associated with the template.
            Allowed values: default, all_ports, custom.
        scan_intensity : str (required)
            The scan intensity at which scans will run from this template.
            Allowed values: basic, standard, cautious, maximum.
        type : str (required)
            The type of the template. Allowed values: discovery, assessment.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = network_scan_template_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_templates",
            body=body
        )

    @force_default(defaults=["body"], default_types=["list"])
    def update_templates(self: object,
                         body: list = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update templates using provided specifications.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/update_templates

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a list of dictionaries in JSON format. Not required if using other keywords.
                [
                    {
                        "active_check_level": "string",
                        "additional_tcp_ports": [
                            "string"
                        ],
                        "additional_udp_ports": [
                            "string"
                        ],
                        "auto_include_new_detections": boolean,
                        "detections": [
                            "string"
                        ],
                        "id": "string",
                        "ignore_tcp_resets": boolean,
                        "name": "string",
                        "ports_scan_level": "string",
                        "scan_intensity": "string"
                    }
                ]
        active_check_level : str
            The active check level associated with the template.
            Allowed values: active_check_safe_only, active_check_all.
        additional_tcp_ports : str or list[str]
            Additional TCP ports associated with the template.
        additional_udp_ports : str or list[str]
            Additional UDP ports associated with the template.
        auto_include_new_detections : bool
            Automatically include new detections in the template.
        detections : str or list[str]
            Detections associated with the template.
        id : str (required)
            The unique identifier of the template to update.
        ignore_tcp_resets : bool
            Ignore TCP resets associated with the template.
        name : str
            The name given to the template.
        ports_scan_level : str
            The port scan level associated with the template.
            Allowed values: default, all_ports, custom.
        scan_intensity : str
            The scan intensity at which scans will run from this template.
            Allowed values: basic, standard, cautious, maximum.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = network_scan_template_update_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_templates",
            body=body
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_templates(self: object,
                         *args,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete templates by their IDs.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/delete_templates

        Keyword arguments
        -----------------
        ids : str or list[str]
            IDs of templates to be deleted (Min: 1, Max: 100)
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
            operation_id="delete_templates",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_templates(self: object,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get template IDs by filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/query_templates

        Keyword arguments
        -----------------
        offset : int
            An offset used with the limit parameter to manage pagination of results. On your first request, don’t provide
            an offset. On subsequent requests, add previous offset with the previous limit to continue from that place in
            the results.
        limit : int
            The number of template IDs to return in this response
            (Min: 1, Max: 100, Default: 100)
        sort : str
            Sort templates by their properties. A single sort field is allowed.
        filter : str
            Search for templates by providing an FQL filter.
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
            operation_id="query_templates",
            keywords=kwargs,
            params=parameters
        )

    # Backward compatibility aliases
    GetTemplateConfigs = get_template_configs
    GetTemplates = get_templates
    CreateTemplates = create_templates
    UpdateTemplates = update_templates
    DeleteTemplates = delete_templates
    QueryTemplates = query_templates
