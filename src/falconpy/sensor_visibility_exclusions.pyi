"""Type stubs for sensor_visibility_exclusions."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class SensorVisibilityExclusions(ServiceClass):

    def get_exclusions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_exclusions(
        self,
        *,
        comment: Optional[str] = None,
        groups: Optional[Union[str, List[str]]] = None,
        is_descendant_process: Optional[bool] = None,
        value: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_exclusions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_exclusions(
        self,
        *,
        comment: Optional[str] = None,
        groups: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        is_descendant_process: Optional[bool] = None,
        value: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_exclusions(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    getSensorVisibilityExclusionsV1 = get_exclusions
    createSVExclusionsV1 = create_exclusions
    deleteSensorVisibilityExclusionsV1 = delete_exclusions
    updateSensorVisibilityExclusionsV1 = update_exclusions
    querySensorVisibilityExclusionsV1 = query_exclusions
