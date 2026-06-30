"""Type stubs for sensor_usage."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class SensorUsage(ServiceClass):

    def get_weekly_usage(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_hourly_usage(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetSensorUsageWeekly = get_weekly_usage
    GetSensorUsageHourly = get_hourly_usage
