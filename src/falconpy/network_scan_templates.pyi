"""Type stubs for network_scan_templates."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class NetworkScanTemplates(ServiceClass):

    def get_template_configs(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_templates(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_templates(
        self,
        *,
        active_check_level: Optional[str] = None,
        additional_tcp_ports: Optional[Union[str, List[str]]] = None,
        additional_udp_ports: Optional[Union[str, List[str]]] = None,
        auto_include_new_detections: Optional[bool] = None,
        detections: Optional[Union[str, List[str]]] = None,
        excluded_tcp_ports: Optional[Union[str, List[str]]] = None,
        excluded_udp_ports: Optional[Union[str, List[str]]] = None,
        ignore_tcp_resets: Optional[bool] = None,
        name: Optional[str] = None,
        ports_scan_level: Optional[str] = None,
        scan_flags: Optional[dict] = None,
        scan_intensity: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_templates(
        self,
        *,
        active_check_level: Optional[str] = None,
        additional_tcp_ports: Optional[Union[str, List[str]]] = None,
        additional_udp_ports: Optional[Union[str, List[str]]] = None,
        auto_include_new_detections: Optional[bool] = None,
        detections: Optional[Union[str, List[str]]] = None,
        excluded_tcp_ports: Optional[Union[str, List[str]]] = None,
        excluded_udp_ports: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        ignore_tcp_resets: Optional[bool] = None,
        name: Optional[str] = None,
        ports_scan_level: Optional[str] = None,
        scan_flags: Optional[dict] = None,
        scan_intensity: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_templates(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_templates(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetTemplateConfigs = get_template_configs
    GetTemplates = get_templates
    CreateTemplates = create_templates
    UpdateTemplates = update_templates
    DeleteTemplates = delete_templates
    QueryTemplates = query_templates
