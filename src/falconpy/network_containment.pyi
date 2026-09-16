"""Type stubs for network_containment."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class NetworkContainment(ServiceClass):

    def get_allowlist_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_allowlist_rules(
        self,
        *,
        rules: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_allowlist_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_allowlist_rules(
        self,
        *,
        rules: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_allowlist_rules(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetContainmentAllowlistRules = get_allowlist_rules
    CreateContainmentAllowlistRules = create_allowlist_rules
    DeleteContainmentAllowlistRules = delete_allowlist_rules
    UpdateContainmentAllowlistRules = update_allowlist_rules
    QueryContainmentAllowlistRules = query_allowlist_rules
