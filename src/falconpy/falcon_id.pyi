"""Type stubs for falcon_id."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FalconId(ServiceClass):

    def get_third_party_passkey_registry(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_third_party_passkey_registry(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_third_party_passkey_registry(
        self,
        *,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_third_party_passkey_registry(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetThirdPartyPasskeyRegistry = get_third_party_passkey_registry
    DeleteThirdPartyPasskeyRegistry = delete_third_party_passkey_registry
    UpdateThirdPartyPasskeyRegistry = update_third_party_passkey_registry
    QueryThirdPartyPasskeyRegistry = query_third_party_passkey_registry
