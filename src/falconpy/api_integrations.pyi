"""Type stubs for api_integrations."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class APIIntegrations(ServiceClass):

    def get_plugin_configs(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_command_proxy(
        self,
        *,
        config: Optional[dict] = None,
        config_auth_type: Optional[str] = None,
        config_id: Optional[str] = None,
        definition_id: Optional[str] = None,
        id: Optional[str] = None,
        operation_id: Optional[str] = None,
        request: Optional[dict] = None,
        version: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_command(
        self,
        *,
        config: Optional[dict] = None,
        config_auth_type: Optional[str] = None,
        config_id: Optional[str] = None,
        definition_id: Optional[str] = None,
        id: Optional[str] = None,
        operation_id: Optional[str] = None,
        request: Optional[dict] = None,
        version: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetCombinedPluginConfigs = get_plugin_configs
    ExecuteCommandProxy = execute_command_proxy
    ExecuteCommand = execute_command
