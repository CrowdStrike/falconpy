"""Type stubs for api_clients."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class APIClients(ServiceClass):

    def get_accessible_scopes(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def reset_api_client_secret(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        action_name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_api_clients(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_api_client(
        self,
        *,
        description: Optional[str] = None,
        name: Optional[str] = None,
        scopes: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_api_clients(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_api_client(
        self,
        *,
        ids: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        scopes: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_all_api_client_ids_for_customer(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetAccessibleScopes = get_accessible_scopes
    ResetAPIClientSecret = reset_api_client_secret
    GetAPIClients = get_api_clients
    CreateAPIClient = create_api_client
    DeleteAPIClients = delete_api_clients
    UpdateAPIClient = update_api_client
    GetAllAPIClientIdsForCustomer = get_all_api_client_ids_for_customer
