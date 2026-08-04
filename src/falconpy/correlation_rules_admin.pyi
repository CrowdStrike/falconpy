"""Type stubs for correlation_rules_admin."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CorrelationRulesAdmin(ServiceClass):

    def change_correlation_rule_owner(
        self,
        *,
        api_client_id: Optional[str] = None,
        id: Optional[str] = None,
        user_id: Optional[str] = None,
        user_uuid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_rules_ownership_put_v2(
        self,
        *,
        api_client_id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        user_id: Optional[str] = None,
        user_uuid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    entities_rules_ownership_put_v1 = change_correlation_rule_owner
