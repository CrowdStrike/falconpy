"""Type stubs for sensor_download."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class SensorDownload(ServiceClass):

    def get_combined_sensor_installers_by_query(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_combined_sensor_installers_by_query_v2(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def download_sensor_installer(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def download_sensor_installer_v2(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sensor_installer_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sensor_installer_entities_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sensor_installer_ccid(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sensor_installers_by_query(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sensor_installers_by_query_v2(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_combined_sensor_installers_by_query_v3(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def download_sensor_installer_v3(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sensor_installer_entities_v3(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sensor_installers_by_query_v3(
        self,
        *args: Union[str, List[str]],
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetCombinedSensorInstallersByQuery = get_combined_sensor_installers_by_query
    GetCombinedSensorInstallersByQueryV2 = get_combined_sensor_installers_by_query_v2
    DownloadSensorInstallerById = download_sensor_installer
    DownloadSensorInstallerByIdV2 = download_sensor_installer_v2
    GetSensorInstallersEntities = get_sensor_installer_entities
    GetSensorInstallersEntitiesV2 = get_sensor_installer_entities_v2
    GetSensorInstallersCCIDByQuery = get_sensor_installer_ccid
    GetSensorInstallersByQuery = get_sensor_installers_by_query
    GetSensorInstallersByQueryV2 = get_sensor_installers_by_query_v2
    GetCombinedSensorInstallersByQueryV3 = get_combined_sensor_installers_by_query_v3
    DownloadSensorInstallerByIdV3 = download_sensor_installer_v3
    GetSensorInstallersEntitiesV3 = get_sensor_installer_entities_v3
    GetSensorInstallersByQueryV3 = get_sensor_installers_by_query_v3
