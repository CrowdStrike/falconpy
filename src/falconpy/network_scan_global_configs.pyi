"""Type stubs for network_scan_global_configs."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class NetworkScanGlobalConfigs(ServiceClass):

    def get_global_configs(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_global_configs(
        self,
        *,
        auto_confirm_ownership: Optional[dict] = None,
        max_concurrent_tasks: Optional[int] = None,
        network_scanning_enabled: Optional[bool] = None,
        scan_exclusion: Optional[dict] = None,
        scanners: Optional[list] = None,
        scanners_exclusion: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetGlobalConfigs = get_global_configs
    UpdateGlobalConfigs = update_global_configs
