"""Type stubs for delivery_settings."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class DeliverySettings(ServiceClass):

    def get_delivery_settings(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_delivery_settings(
        self,
        *,
        delivery_settings: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetDeliverySettings = get_delivery_settings
    PostDeliverySettings = create_delivery_settings
