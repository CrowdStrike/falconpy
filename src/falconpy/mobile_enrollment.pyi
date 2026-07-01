"""Type stubs for mobile_enrollment."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class MobileEnrollment(ServiceClass):

    def device_enroll(
        self,
        *,
        action_name: Optional[str] = None,
        filter: Optional[str] = None,
        email_addresses: Optional[Union[str, List[str]]] = None,
        expires_at: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def device_enroll_v4(
        self,
        *,
        action_name: Optional[str] = None,
        filter: Optional[str] = None,
        email_addresses: Optional[Union[str, List[str]]] = None,
        enrollment_type: Optional[str] = None,
        expires_at: Optional[str] = None,
        use_network_extension: Optional[bool] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    RequestDeviceEnrollmentV3 = device_enroll
    RequestDeviceEnrollmentV4 = device_enroll_v4
