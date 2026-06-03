"""CrowdStrike Falcon Threatgraph API interface class.

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
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._threatgraph import _threatgraph_endpoints as Endpoints


class ThreatGraph(ServiceClass):
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
    def get_edges(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve edges for a given vertex id.  One edge type must be specified.

        Keyword arguments:
        direction -- The direction of edges that you would like to retrieve.
        edge_type -- The type of edges that you would like to retrieve. String.
                     Available values:
                     accessed_ad_computer                             accessed_adfs_application
                     accessed_azure_application                       accessed_by_kerberos_ticket
                     accessed_by_process                              accessed_by_session
                     accessed_okta_application                        accessed_ping_fed_application
                     accessed_service_account                         accessed_web
                     agent_process                                    agent_to_self_diagnostic
                     ai_agent_used_by                                 ai_runs_on
                     allowed_by_process                               allowed_firewall_rule
                     app_uninstalled_from_host                        assigned_ipv4_address
                     assigned_ipv6_address                            assigned_to_sensor
                     associated_by_ad_computer                        associated_by_ad_group
                     associated_by_ad_user                            associated_by_aggregate_indicator
                     associated_by_app                                associated_by_azure_ad_user
                     associated_by_azure_app                          associated_by_certificate
                     associated_by_control_graph                      associated_by_domain
                     associated_by_host                               associated_by_host_name
                     associated_by_idp_session                        associated_by_incident
                     associated_by_indicator                          associated_by_ip
                     associated_by_ip4                                associated_by_ip6
                     associated_by_okta_user                          associated_by_service_ticket
                     associated_control_graph                         associated_firewall_rule
                     associated_idp_indicator                         associated_incident
                     associated_indicator                             associated_k8s_cluster
                     associated_k8s_sensor                            associated_mobile_forensics_report
                     associated_mobile_indicator                      associated_module
                     associated_primary_module                        associated_quarantined_file
                     associated_quarantined_module                    associated_root_process
                     associated_to_ad_computer                        associated_to_sensor
                     associated_user_session                          associated_vmware_cluster
                     associated_vmware_sensor                         associated_with_process
                     associated_with_sensor                           attributed_by_process
                     attributed_from_domain                           attributed_from_module
                     attributed_on                                    attributed_on_domain
                     attributed_on_module                             attributed_to
                     attributed_to_actor                              authenticated_from_incident
                     authenticated_host                               blocked_by_app
                     blocked_by_process                               blocked_by_sensor
                     blocked_dns                                      blocked_ip4
                     blocked_ip6                                      blocked_module
                     bundled_in_app                                   bundles_module
                     cert_is_presented_by                             cert_presented
                     child_process                                    child_session
                     closed_ip4_socket                                closed_ip6_socket
                     command_line_parent_process                      connected_from_app
                     connected_from_host                              connected_from_process
                     connected_ip4                                    connected_ip6
                     connected_mcp                                    connected_on_customer
                     connected_on_sensor                              connected_to_accessory
                     connected_to_wifi_ap                             connection_killed_by_app
                     connection_killed_by_process                     containerized_app
                     containerized_by_sensor                          control_graph
                     created_by_incident                              created_by_process
                     created_by_user                                  created_quarantined_file
                     created_service                                  customer_agent_has_user
                     customer_has_sensor                              customer_ioc
                     customer_sensor_to_sensor                        customer_user_to_sensor_user
                     deleted_by_process                               deleted_rule
                     denied_by_firewall_rule                          denied_by_process
                     denied_firewall_rule                             detected_module
                     detection                                        device
                     disconnect_from_wifi_ap                          disconnected_from_accessory
                     disconnected_from_host                           dns
                     dns_request                                      duplicated_by_app
                     duplicates_app                                   established_on_ad_computer
                     established_on_host_name                         established_on_ip4
                     established_on_ip6                               established_on_sensor
                     established_session                              established_user_session
                     executed_app                                     executed_by_process
                     executed_macro_script                            executed_script
                     extracted_file                                   failed_to_authenticate_ad_user
                     failed_to_authenticate_to_ad_computer            failed_to_authenticate_to_adfs_app
                     failed_to_authenticate_to_azure_app              failed_to_authenticate_to_okta_app
                     failed_to_authenticate_to_ping_app               failed_to_authenticate_to_service_account
                     generated_by_renewing                            generated_by_session
                     generated_dce_rpc_epm_request_against_dc         generated_dce_rpc_request_against_dc
                     generated_failed_authentication_to_ad_computer   generated_failed_authentication_to_adfs_app
                     generated_failed_authentication_to_azure_app     generated_failed_authentication_to_okta_app
                     generated_failed_authentication_to_ping_app      generated_failed_authentication_to_service_account
                     generated_ldap_search_against_dc                 generated_service_ticket
                     had_code_injected_by_process                     has_app_installed
                     has_attributed_process                           has_attribution
                     has_firmware                                     implicated_by_incident
                     implicated_sensor                                indexed
                     initiated_by_ad_computer                         initiated_by_azure_ad_user
                     initiated_by_okta_user                           initiated_by_user
                     initiated_session                                injected_code_into_process
                     injected_thread                                  injected_thread_from_process
                     installed_app                                    installed_by_app
                     installed_on_host                                invalid_firewall_rule
                     invalid_from_process                             invalidated_by_process
                     invalidated_firewall_rule                        invokes_model
                     involved_ad_computer                             involved_service_account
                     ip4_socket_closed_by_app                         ip4_socket_closed_by_process
                     ip4_socket_opened_by_process                     ip6_socket_closed_by_app
                     ip6_socket_closed_by_process                     ip6_socket_opened_by_process
                     ipv4                                             ipv4_close
                     ipv4_listen                                      ipv6
                     ipv6_close                                       ipv6_listen
                     killed_ip4_connection                            killed_ip6_connection
                     known_by_md5                                     known_by_sha256
                     linking_event                                    loaded_by_process
                     loaded_module                                    loaded_skill
                     macro_executed_by_process                        mcp_tool_call
                     member_of_full_command_line                      module
                     module_written                                   mounted_on_host
                     mounted_to_host                                  network_close_ip4
                     network_close_ip6                                network_connect_ip4
                     network_connect_ip6                              network_listen_ip4
                     network_listen_ip6                               opened_ip4_socket
                     opened_ip6_socket                                parent_of_command_line
                     parent_process                                   parented_by_process
                     participating_process                            performed_psexec_against_dc
                     presented_by_cloud                               primary_module
                     primary_module_of_process                        process_ai_agent
                     protected_by_shield                              quarantined_file
                     queried_by_process                               queried_by_sensor
                     queried_dns                                      queried_on_customer
                     queried_on_sensor                                received_from_cloud
                     registered_by_incident                           registered_scheduledtask
                     renewed_to_generate                              reports_aggregate_indicator
                     resolved_from_domain                             resolved_to_ip4
                     resolved_to_ip6                                  rooted_control_graph
                     rule_set_by_process                              script
                     self_diagnostic_to_agent                         session_on_sensor
                     session_process                                  set_by_process
                     set_firewall_rule                                set_rule
                     shell_io_redirect                                shield_activated_on_host
                     submitted_prompt                                 tool_spawned_process
                     trigger_process                                  triggered_by_control_graph
                     triggered_by_process                             triggered_control_graph
                     triggered_custom_ioa                             triggered_detection
                     triggered_indicator                              triggered_mobile_indicator
                     triggered_xdr                                    triggering_domain
                     triggering_network                               uncontainerized_app
                     uncontainerized_by_sensor                        uninstalled_app
                     unmounted_from_host                              unmounted_on_host
                     used_tool                                        user
                     user_session                                     uses_ai_agent
                     witnessed_by_sensor                              witnessed_process
                     wmicreated_by_incident                           wmicreated_process
                     written_by_process                               wrote_module
        ids -- Vertex ID to get details for.  Only one value is supported. String.
        limit -- How many edges to return in a single request [1-100]. Integer.
        nano -- Return nano-precision entity timestamps. Boolean.
        offset -- The offset to use to retrieve the next page of results. Integer.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.
        scope -- Scope of the request. String.
                 Available values: cspm, customer, cwpp, device, global

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/threatgraph/combined_edges_get
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="combined_edges_get",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ran_on(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Look up instances of indicators.

        (Such as hashes, domain names, and ip addresses that have been seen on devices in your environment.)

        Keyword arguments:
        limit -- How many edges to return in a single request [1-100]. Integer.
        nano -- Return nano-precision entity timestamps. Boolean.
        offset -- The offset to use to retrieve the next page of results. Integer.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.
        type -- The type of indicator that you would like to retrieve. String.
                Available values: domain, ipv4, ipv6, md5, sha1, sha256
        value -- The value of the indicator to search by. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/threatgraph/combined_ran_on_get
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="combined_ran_on_get",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_summary(self: object,
                    parameters: dict = None,
                    vertex_type: str = "any-vertex",
                    **kwargs
                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve summary for a given vertex ID.

        Keyword arguments:
        ids -- Vertex ID to get details for.  String or list of strings.
        scope -- Scope of the request. String.
                 Available values: cspm, customer, cwpp, device, global
        nano -- Return nano-precision entity timestamps. Boolean.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.
        vertex_type -- Type of vertex to get properties for. String.
                       Allowed values:
                       accessories                    accessory
                       actor                          ad-computers
                       ad-groups                      ad_computer
                       ad_group                       adfs-applications
                       adfs_application               aggregate-indicators
                       aggregate_indicator            ai-agents
                       ai-models                      ai-prompts
                       ai-sessions                    ai-skills
                       ai-tools                       ai_agent
                       ai_model                       ai_prompt
                       ai_session                     ai_skill
                       ai_tool                        any-vertex
                       azure-ad-users                 azure-applications
                       azure_ad_user                  azure_application
                       certificate                    certificates
                       command-lines                  command_line
                       containerized-apps             containerized_app
                       control-graphs                 control_graph
                       custom_ioa                     custom_ioas
                       detection                      detection-indices
                       detection_index                detections
                       devices                        domain
                       domains                        extracted-files
                       extracted_file                 firewall
                       firewall_rule_match            firewall_rule_matches
                       firewalls                      firmware
                       firmwares                      host-names
                       host_name                      idp-indicators
                       idp-sessions                   idp_indicator
                       idp_session                    incident
                       incidents                      indicator
                       indicators                     ipv4
                       ipv6                           k8s_cluster
                       k8s_clusters                   kerberos-tickets
                       kerberos_ticket                legacy-detections
                       legacy_detection               macro_script
                       macro_scripts                  mcp-servers
                       mcp_server                     mobile-apps
                       mobile-fs-volumes              mobile-indicators
                       mobile_app                     mobile_fs_volume
                       mobile_indicator               mobile_os_forensics_report
                       mobile_os_forensics_reports    module
                       modules                        okta-applications
                       okta-users                     okta_application
                       okta_user                      ping-fed-applications
                       ping_fed_application           process
                       processes                      quarantined-files
                       quarantined_file               script
                       scripts                        sensor
                       sensor-self-diagnostics        sensor_self_diagnostic
                       shield                         shields
                       user-sessions                  user_id
                       user_session                   users
                       vmware_cluster                 vmware_clusters
                       web_access                     wifi-access-points
                       wifi_access_point              xdr
                       ad-computers             indicator
                       ad-groups                indicators
                       ad_computer              ipv4
                       ad_group                 ipv6
                       adfs-applications        k8s_cluster
                       adfs_application         k8s_clusters
                       aggregate-indicators     kerberos-tickets
                       aggregate_indicator      kerberos_ticket
                       any-vertex               legacy-detections
                       azure-ad-users           legacy_detection
                       azure-applications       macro_script
                       azure_ad_user            macro_scripts
                       azure_application        mobile-apps
                       certificate              mobile-fs-volumes
                       certificates             mobile-indicators
                       command-lines            mobile_app
                       command_line             mobile_fs_volume
                       containerized-apps       mobile_indicator
                       containerized_app        mobile_os_forensics_report
                       control-graphs           mobile_os_forensics_reports
                       control_graph            module
                       customer                 modules
                       customers                okta-applications
                       detection                okta-users
                       detection-indices        okta_application
                       detection_index          okta_user
                       detections               ping-fed-applications
                       devices                  ping_fed_application
                       direct                   process
                       directs                  processes
                       domain                   quarantined-files
                       domains                  quarantined_file
                       extracted-files          script
                       extracted_file           scripts
                       firewall                 sensor
                       firewall_rule_match      sensor-self-diagnostics
                       firewall_rule_matches    sensor_self_diagnostic
                       firewalls                tag
                       firmware                 tags
                       firmwares                user-sessions
                       host-names               user_id
                       host_name                user_session
                       hunting-leads            users
                       hunting_lead             wifi-access-points
                       idp-indicators           wifi_access_point
                       idp-sessions             xdr
                       idp_indicator            shield
                       shields                  custom_ioa
                       custom_ioas

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/threatgraph/combined_summary_get
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="combined_summary_get",
            keywords=kwargs,
            params=parameters,
            vertex_type=vertex_type
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_vertices_v1(self: object,
                        parameters: dict = None,
                        vertex_type: str = "any-vertex",
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve metadata for a given vertex ID.

        Note: This is a legacy operation used by CrowdStrike Store partners prior
        to release of the ThreatGraph OAuth 2.0 APIs. If you’re not currently using
        this endpoint, use the get_vertices method instead.

        Keyword arguments:
        ids -- Vertex ID to get details for.  String or list of strings.
        scope -- Scope of the request. String.
                 Available values: cspm, customer, cwpp, device, global
        nano -- Return nano-precision entity timestamps. Boolean.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.
        vertex_type -- Type of vertex to get properties for. String.
                       Allowed values:
                       accessories                    accessory
                       actor                          ad-computers
                       ad-groups                      ad_computer
                       ad_group                       adfs-applications
                       adfs_application               aggregate-indicators
                       aggregate_indicator            ai-agents
                       ai-models                      ai-prompts
                       ai-sessions                    ai-skills
                       ai-tools                       ai_agent
                       ai_model                       ai_prompt
                       ai_session                     ai_skill
                       ai_tool                        any-vertex
                       azure-ad-users                 azure-applications
                       azure_ad_user                  azure_application
                       certificate                    certificates
                       command-lines                  command_line
                       containerized-apps             containerized_app
                       control-graphs                 control_graph
                       custom_ioa                     custom_ioas
                       detection                      detection-indices
                       detection_index                detections
                       devices                        domain
                       domains                        extracted-files
                       extracted_file                 firewall
                       firewall_rule_match            firewall_rule_matches
                       firewalls                      firmware
                       firmwares                      host-names
                       host_name                      idp-indicators
                       idp-sessions                   idp_indicator
                       idp_session                    incident
                       incidents                      indicator
                       indicators                     ipv4
                       ipv6                           k8s_cluster
                       k8s_clusters                   kerberos-tickets
                       kerberos_ticket                legacy-detections
                       legacy_detection               macro_script
                       macro_scripts                  mcp-servers
                       mcp_server                     mobile-apps
                       mobile-fs-volumes              mobile-indicators
                       mobile_app                     mobile_fs_volume
                       mobile_indicator               mobile_os_forensics_report
                       mobile_os_forensics_reports    module
                       modules                        okta-applications
                       okta-users                     okta_application
                       okta_user                      ping-fed-applications
                       ping_fed_application           process
                       processes                      quarantined-files
                       quarantined_file               script
                       scripts                        sensor
                       sensor-self-diagnostics        sensor_self_diagnostic
                       shield                         shields
                       user-sessions                  user_id
                       user_session                   users
                       vmware_cluster                 vmware_clusters
                       web_access                     wifi-access-points
                       wifi_access_point              xdr
                       ad-computers             indicator
                       ad-groups                indicators
                       ad_computer              ipv4
                       ad_group                 ipv6
                       adfs-applications        k8s_cluster
                       adfs_application         k8s_clusters
                       aggregate-indicators     kerberos-tickets
                       aggregate_indicator      kerberos_ticket
                       any-vertex               legacy-detections
                       azure-ad-users           legacy_detection
                       azure-applications       macro_script
                       azure_ad_user            macro_scripts
                       azure_application        mobile-apps
                       certificate              mobile-fs-volumes
                       certificates             mobile-indicators
                       command-lines            mobile_app
                       command_line             mobile_fs_volume
                       containerized-apps       mobile_indicator
                       containerized_app        mobile_os_forensics_report
                       control-graphs           mobile_os_forensics_reports
                       control_graph            module
                       customer                 modules
                       customers                okta-applications
                       detection                okta-users
                       detection-indices        okta_application
                       detection_index          okta_user
                       detections               ping-fed-applications
                       devices                  ping_fed_application
                       direct                   process
                       directs                  processes
                       domain                   quarantined-files
                       domains                  quarantined_file
                       extracted-files          script
                       extracted_file           scripts
                       firewall                 sensor
                       firewall_rule_match      sensor-self-diagnostics
                       firewall_rule_matches    sensor_self_diagnostic
                       firewalls                tag
                       firmware                 tags
                       firmwares                user-sessions
                       host-names               user_id
                       host_name                user_session
                       hunting-leads            users
                       hunting_lead             wifi-access-points
                       idp-indicators           wifi_access_point
                       idp-sessions             xdr
                       idp_indicator            shield
                       shields                  custom_ioa
                       custom_ioas

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/threatgraph/entities_vertices_get
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_vertices_get",
            keywords=kwargs,
            params=parameters,
            vertex_type=vertex_type
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_vertices(self: object,
                     parameters: dict = None,
                     vertex_type: str = "any-vertex",
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve metadata for a given vertex ID.

        Keyword arguments:
        ids -- Vertex ID to get details for. String or list of strings.
        scope -- Scope of the request.  String.
                 Available values: cspm, customer, cwpp, device, global
        nano -- Return nano-precision entity timestamps. Boolean.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.
        vertex_type -- Type of vertex to get properties for. String.
                       Allowed values:
                       accessories                    accessory
                       actor                          ad-computers
                       ad-groups                      ad_computer
                       ad_group                       adfs-applications
                       adfs_application               aggregate-indicators
                       aggregate_indicator            ai-agents
                       ai-models                      ai-prompts
                       ai-sessions                    ai-skills
                       ai-tools                       ai_agent
                       ai_model                       ai_prompt
                       ai_session                     ai_skill
                       ai_tool                        any-vertex
                       azure-ad-users                 azure-applications
                       azure_ad_user                  azure_application
                       certificate                    certificates
                       command-lines                  command_line
                       containerized-apps             containerized_app
                       control-graphs                 control_graph
                       custom_ioa                     custom_ioas
                       detection                      detection-indices
                       detection_index                detections
                       devices                        domain
                       domains                        extracted-files
                       extracted_file                 firewall
                       firewall_rule_match            firewall_rule_matches
                       firewalls                      firmware
                       firmwares                      host-names
                       host_name                      idp-indicators
                       idp-sessions                   idp_indicator
                       idp_session                    incident
                       incidents                      indicator
                       indicators                     ipv4
                       ipv6                           k8s_cluster
                       k8s_clusters                   kerberos-tickets
                       kerberos_ticket                legacy-detections
                       legacy_detection               macro_script
                       macro_scripts                  mcp-servers
                       mcp_server                     mobile-apps
                       mobile-fs-volumes              mobile-indicators
                       mobile_app                     mobile_fs_volume
                       mobile_indicator               mobile_os_forensics_report
                       mobile_os_forensics_reports    module
                       modules                        okta-applications
                       okta-users                     okta_application
                       okta_user                      ping-fed-applications
                       ping_fed_application           process
                       processes                      quarantined-files
                       quarantined_file               script
                       scripts                        sensor
                       sensor-self-diagnostics        sensor_self_diagnostic
                       shield                         shields
                       user-sessions                  user_id
                       user_session                   users
                       vmware_cluster                 vmware_clusters
                       web_access                     wifi-access-points
                       wifi_access_point              xdr
                       ad-computers             indicator
                       ad-groups                indicators
                       ad_computer              ipv4
                       ad_group                 ipv6
                       adfs-applications        k8s_cluster
                       adfs_application         k8s_clusters
                       aggregate-indicators     kerberos-tickets
                       aggregate_indicator      kerberos_ticket
                       any-vertex               legacy-detections
                       azure-ad-users           legacy_detection
                       azure-applications       macro_script
                       azure_ad_user            macro_scripts
                       azure_application        mobile-apps
                       certificate              mobile-fs-volumes
                       certificates             mobile-indicators
                       command-lines            mobile_app
                       command_line             mobile_fs_volume
                       containerized-apps       mobile_indicator
                       containerized_app        mobile_os_forensics_report
                       control-graphs           mobile_os_forensics_reports
                       control_graph            module
                       customer                 modules
                       customers                okta-applications
                       detection                okta-users
                       detection-indices        okta_application
                       detection_index          okta_user
                       detections               ping-fed-applications
                       devices                  ping_fed_application
                       direct                   process
                       directs                  processes
                       domain                   quarantined-files
                       domains                  quarantined_file
                       extracted-files          script
                       extracted_file           scripts
                       firewall                 sensor
                       firewall_rule_match      sensor-self-diagnostics
                       firewall_rule_matches    sensor_self_diagnostic
                       firewalls                tag
                       firmware                 tags
                       firmwares                user-sessions
                       host-names               user_id
                       host_name                user_session
                       hunting-leads            users
                       hunting_lead             wifi-access-points
                       idp-indicators           wifi_access_point
                       idp-sessions             xdr
                       idp_indicator            shield
                       shields                  custom_ioa
                       custom_ioas

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/threatgraph/entities_vertices_getv2
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_vertices_getv2",
            keywords=kwargs,
            params=parameters,
            vertex_type=vertex_type
            )

    def get_edge_types(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Show all available edge types.

        This method does not accept arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/threatgraph/queries_edgetypes_get
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queries_edgetypes_get"
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes.
    combined_edges_get = get_edges
    combined_ran_on_get = get_ran_on
    combined_summary_get = get_summary
    entities_vertices_get = get_vertices_v1
    entities_vertices_getv2 = get_vertices
    get_vertices_v2 = get_vertices
    queries_edgetypes_get = get_edge_types
