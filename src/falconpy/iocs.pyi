"""Type stubs for iocs."""
from typing import Dict, List, Optional, Union
from typing_extensions import deprecated
from ._service_class import ServiceClass
from ._result import Result


class Iocs(ServiceClass):

    def devices_count(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This API endpoint is no longer available. Please use the new IOC.indicator_get method defined in the new IOC service class in order to perform this operation.")
    def get_ioc(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This API endpoint is no longer available. Please use the new IOC.indicator_create method defined in the new IOC service class in order to perform this operation.")
    def create_ioc(
        self,
        *,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This API endpoint is no longer available. Please use the new IOC.indicator_delete method defined in the new IOC service class in order to perform this operation.")
    def delete_ioc(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This API endpoint is no longer available. Please use the new IOC.indicator_update method defined in the new IOC service class in order to perform this operation.")
    def update_ioc(
        self,
        *,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def devices_ran_on(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This API endpoint is no longer available. Please use the new IOC.indicator_search method defined in the new IOC service class in order to perform this operation.")
    def query_iocs(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def processes_ran_on(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_processes(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    DevicesCount = devices_count
    GetIOC = get_ioc
    CreateIOC = create_ioc
    DeleteIOC = delete_ioc
    UpdateIOC = update_ioc
    DevicesRanOn = devices_ran_on
    QueryIOCs = query_iocs
    ProcessesRanOn = processes_ran_on
