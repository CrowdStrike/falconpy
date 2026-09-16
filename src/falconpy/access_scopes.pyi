"""Type stubs for access_scopes."""
from typing import Dict, List, Optional, Union
from typing_extensions import deprecated
from ._service_class import ServiceClass
from ._result import Result


class AccessScopes(ServiceClass):

    def list_access_scopes_external(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This operation is no longer available in CrowdStrike's API. Calling this method will result in an error from the API.")
    def query_access_scopes_external(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ListAccessScopesExternal = list_access_scopes_external
    QueryAccessScopesExternal = query_access_scopes_external
