"""Type stubs for custom_ioa."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CustomIOA(ServiceClass):

    def get_patterns(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_platforms(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule_groups(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule_group(
        self,
        *,
        comment: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        platform: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rule_groups(
        self,
        *args: Union[str, List[str]],
        comment: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule_group(
        self,
        *,
        comment: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        rulegroup_version: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule_types(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules_get(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule(
        self,
        *,
        comment: Optional[str] = None,
        description: Optional[str] = None,
        disposition_id: Optional[int] = None,
        field_values: Optional[list] = None,
        name: Optional[str] = None,
        pattern_severity: Optional[str] = None,
        rulegroup_id: Optional[str] = None,
        ruletype_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rules(
        self,
        *,
        rule_group_id: Optional[str] = None,
        comment: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rules(
        self,
        *,
        comment: Optional[str] = None,
        rule_updates: Optional[list] = None,
        rulegroup_id: Optional[str] = None,
        rulegroup_version: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rules_v2(
        self,
        *,
        comment: Optional[str] = None,
        rule_updates: Optional[list] = None,
        rulegroup_id: Optional[str] = None,
        rulegroup_version: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def validate(
        self,
        *,
        fields: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_patterns(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_platforms(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rule_groups_full(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rule_groups(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rule_types(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rules(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    get_platformsMixin0 = get_platforms
    get_rule_groupsMixin0 = get_rule_groups
    create_rule_groupMixin0 = create_rule_group
    delete_rule_groupMixin0 = delete_rule_groups
    delete_rule_groupsMixin0 = delete_rule_groups
    update_rule_groupMixin0 = update_rule_group
    get_rulesMixin0 = get_rules
    query_platformsMixin0 = query_platforms
    query_rule_groupsMixin0 = query_rule_groups
    query_rulesMixin0 = query_rules
