"""Type stubs for installation_tokens."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class InstallationTokens(ServiceClass):

    def audit_events_read(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def customer_settings_read(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def tokens_read(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def tokens_create(
        self,
        *,
        expires_timestamp: Optional[str] = None,
        label: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def tokens_delete(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def tokens_update(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        expires_timestamp: Optional[str] = None,
        label: Optional[str] = None,
        revoked: Optional[bool] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def audit_events_query(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def tokens_query(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def customer_settings_update(
        self,
        *,
        max_active_tokens: Optional[int] = None,
        tokens_required: Optional[bool] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...
