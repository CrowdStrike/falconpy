"""Type stubs for tailored_intelligence."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class TailoredIntelligence(ServiceClass):

    def get_event_body(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_event_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_events(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rules(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetEventsBody = get_event_body
    get_events_body = get_event_body
    GetEventsEntities = get_event_entities
    get_events_entities = get_event_entities
    QueryEvents = query_events
    GetRulesEntities = get_rule_entities
    get_rules_entities = get_rule_entities
    QueryRules = query_rules
