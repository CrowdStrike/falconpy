"""Type stubs for federated_connections."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FederatedConnections(ServiceClass):

    def post_federated_connections_config(
        self,
        *,
        cluster_url: Optional[str] = None,
        connection_id: Optional[str] = None,
        view_token: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_federated_connections_config(
        self,
        *,
        connection_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def patch_federated_connections_config(
        self,
        *,
        connection_id: Optional[str] = None,
        cluster_url: Optional[str] = None,
        view_token: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    PostFederatedConnectionsConfig = post_federated_connections_config
    DeleteFederatedConnectionsConfig = delete_federated_connections_config
    PatchFederatedConnectionsConfig = patch_federated_connections_config
