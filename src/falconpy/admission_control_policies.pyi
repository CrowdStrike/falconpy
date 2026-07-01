"""Type stubs for admission_control_policies."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class AdmissionControlPolicies(ServiceClass):

    def get_policies(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_policy(
        self,
        *,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy(
        self,
        *,
        ids: Optional[str] = None,
        description: Optional[str] = None,
        is_enabled: Optional[bool] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_policies(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_host_groups(
        self,
        *,
        host_groups: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def remove_host_groups(
        self,
        *,
        policy_id: Optional[str] = None,
        host_group_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_precedence(
        self,
        *,
        id: Optional[str] = None,
        precedence: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_custom_rules(
        self,
        *,
        id: Optional[str] = None,
        rule_groups: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_custom_rules(
        self,
        *,
        policy_id: Optional[str] = None,
        custom_rule_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def set_rule_group_precedence(
        self,
        *,
        id: Optional[str] = None,
        rule_groups: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def replace_rule_group_selectors(
        self,
        *,
        id: Optional[str] = None,
        rule_groups: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule_groups(
        self,
        *,
        id: Optional[str] = None,
        rule_groups: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule_groups(
        self,
        *,
        id: Optional[str] = None,
        rule_groups: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rule_groups(
        self,
        *,
        policy_id: Optional[str] = None,
        rule_group_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_policies(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    admission_control_get_policies = get_policies
    admission_control_create_policy = create_policy
    admission_control_update_policy = update_policy
    admission_control_delete_policies = delete_policies
    admission_control_add_host_groups = add_host_groups
    admission_control_remove_host_groups = remove_host_groups
    admission_control_update_policy_precedence = update_policy_precedence
    admission_control_add_rule_group_custom_rule = add_custom_rules
    admission_control_remove_rule_group_custom_rule = delete_custom_rules
    admission_control_set_rule_group_precedence = set_rule_group_precedence
    admission_control_replace_rule_group_selectors = replace_rule_group_selectors
    admission_control_create_rule_groups = create_rule_groups
    admission_control_update_rule_groups = update_rule_groups
    admission_control_delete_rule_groups = delete_rule_groups
    admission_control_query_policies = query_policies
