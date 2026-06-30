"""Type stubs for event_streams."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class EventStreams(ServiceClass):

    def refresh_active_stream(
        self,
        *,
        action_name: Optional[str] = None,
        appId: Optional[str] = None,
        partition: Optional[int] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_available_streams(
        self,
        *,
        appId: Optional[str] = None,
        format: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    refreshActiveStreamSession = refresh_active_stream
    listAvailableStreamsOAuth2 = list_available_streams
