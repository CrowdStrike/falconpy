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

        Keyword arguments:
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/get_template_configs
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

        Keyword arguments:
        ids -- IDs of templates to be retrieved (Min: 1, Max: 100). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/get_templates
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

        Keyword arguments:
        body -- Full body payload as a list of dictionaries in JSON format. Not required if using other keywords.
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
        active_check_level -- The active check level associated with the template.
                              Allowed values: active_check_safe_only, active_check_all. Required. String.
        additional_tcp_ports -- Additional TCP ports associated with the template. List of strings.
        additional_udp_ports -- Additional UDP ports associated with the template. List of strings.
        auto_include_new_detections -- Automatically include new detections in the template. Boolean.
        detections -- Detections associated with the template. List of strings.
        ignore_tcp_resets -- Ignore TCP resets associated with the template. Boolean.
        name -- The name given to the template. Required. String.
        ports_scan_level -- The port scan level associated with the template.
                            Allowed values: default, all_ports, custom. Required. String.
        scan_intensity -- The scan intensity at which scans will run from this template.
                          Allowed values: basic, standard, cautious, maximum. Required. String.
        type -- The type of the template. Allowed values: discovery, assessment. Required. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/create_templates
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

        Keyword arguments:
        body -- Full body payload as a list of dictionaries in JSON format. Not required if using other keywords.
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
        active_check_level -- The active check level associated with the template.
                              Allowed values: active_check_safe_only, active_check_all. String.
        additional_tcp_ports -- Additional TCP ports associated with the template. List of strings.
        additional_udp_ports -- Additional UDP ports associated with the template. List of strings.
        auto_include_new_detections -- Automatically include new detections in the template. Boolean.
        detections -- Detections associated with the template. List of strings.
        id -- The unique identifier of the template to update. Required. String.
        ignore_tcp_resets -- Ignore TCP resets associated with the template. Boolean.
        name -- The name given to the template. String.
        ports_scan_level -- The port scan level associated with the template.
                            Allowed values: default, all_ports, custom. String.
        scan_intensity -- The scan intensity at which scans will run from this template.
                          Allowed values: basic, standard, cautious, maximum. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/update_templates
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

        Keyword arguments:
        ids -- IDs of templates to be deleted (Min: 1, Max: 100). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/delete_templates
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

        Keyword arguments:
        offset -- An offset used with the limit parameter to manage pagination of results. On your first request, don’t provide
                  an offset. On subsequent requests, add previous offset with the previous limit to continue from that place in
                  the results Integer.
        limit -- The number of template IDs to return in this response
                 (Min: 1, Max: 100, Default: 100). Integer.
        sort -- Sort templates by their properties. A single sort field is allowed. String.
        filter -- Search for templates by providing an FQL filter. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-templates/query_templates
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
