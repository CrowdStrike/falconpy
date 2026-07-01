"""Type stubs for filevantage."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FileVantage(ServiceClass):

    def get_actions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def start_actions(
        self,
        *,
        change_ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        operation: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_contents(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_changes(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_host_groups(
        self,
        *,
        policy_id: Optional[str] = None,
        action: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_precedence(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_rule_groups(
        self,
        *,
        policy_id: Optional[str] = None,
        action: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

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
        platform: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_policies(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policies(
        self,
        *,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scheduled_exclusions(
        self,
        *,
        policy_id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_scheduled_exclusions(
        self,
        *,
        description: Optional[str] = None,
        name: Optional[str] = None,
        policy_id: Optional[str] = None,
        processes: Optional[str] = None,
        repeated: Optional[dict] = None,
        schedule_end: Optional[str] = None,
        schedule_start: Optional[str] = None,
        timezone: Optional[str] = None,
        users: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_scheduled_exclusions(
        self,
        *,
        policy_id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_scheduled_exclusions(
        self,
        *,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        policy_id: Optional[str] = None,
        processes: Optional[str] = None,
        repeated: Optional[dict] = None,
        schedule_end: Optional[str] = None,
        schedule_start: Optional[str] = None,
        timezone: Optional[str] = None,
        users: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule_group_precedence(
        self,
        *,
        rule_group_id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules(
        self,
        *,
        rule_group_id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule(
        self,
        *,
        content_files: Optional[Union[str, List[str]]] = None,
        content_registry_values: Optional[Union[str, List[str]]] = None,
        created_timestamp: Optional[str] = None,
        depth: Optional[str] = None,
        description: Optional[str] = None,
        enable_content_capture: Optional[bool] = None,
        enable_hash_capture: Optional[bool] = None,
        exclude: Optional[str] = None,
        exclude_processes: Optional[str] = None,
        exclude_users: Optional[str] = None,
        id: Optional[str] = None,
        include: Optional[str] = None,
        include_processes: Optional[str] = None,
        include_users: Optional[str] = None,
        modified_timestamp: Optional[str] = None,
        path: Optional[str] = None,
        precedence: Optional[int] = None,
        rule_group_id: Optional[str] = None,
        severity: Optional[str] = None,
        type: Optional[str] = None,
        watch_attributes_directory_changes: Optional[bool] = None,
        watch_attributes_file_changes: Optional[bool] = None,
        watch_create_directory_changes: Optional[bool] = None,
        watch_create_file_changes: Optional[bool] = None,
        watch_create_key_changes: Optional[bool] = None,
        watch_delete_directory_changes: Optional[bool] = None,
        watch_delete_file_changes: Optional[bool] = None,
        watch_delete_key_changes: Optional[bool] = None,
        watch_delete_value_changes: Optional[bool] = None,
        watch_permissions_directory_changes: Optional[bool] = None,
        watch_permissions_file_changes: Optional[bool] = None,
        watch_permissions_key_changes: Optional[bool] = None,
        watch_rename_directory_changes: Optional[bool] = None,
        watch_rename_file_changes: Optional[bool] = None,
        watch_rename_key_changes: Optional[bool] = None,
        watch_set_value_changes: Optional[bool] = None,
        watch_write_file_changes: Optional[bool] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rules(
        self,
        *,
        rule_group_id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule(
        self,
        *,
        content_files: Optional[Union[str, List[str]]] = None,
        content_registry_values: Optional[Union[str, List[str]]] = None,
        created_timestamp: Optional[str] = None,
        depth: Optional[str] = None,
        description: Optional[str] = None,
        enable_content_capture: Optional[bool] = None,
        enable_hash_capture: Optional[bool] = None,
        exclude: Optional[str] = None,
        exclude_processes: Optional[str] = None,
        exclude_users: Optional[str] = None,
        id: Optional[str] = None,
        include: Optional[str] = None,
        include_processes: Optional[str] = None,
        include_users: Optional[str] = None,
        modified_timestamp: Optional[str] = None,
        path: Optional[str] = None,
        precedence: Optional[int] = None,
        rule_group_id: Optional[str] = None,
        severity: Optional[str] = None,
        type: Optional[str] = None,
        watch_attributes_directory_changes: Optional[bool] = None,
        watch_attributes_file_changes: Optional[bool] = None,
        watch_create_directory_changes: Optional[bool] = None,
        watch_create_file_changes: Optional[bool] = None,
        watch_create_key_changes: Optional[bool] = None,
        watch_delete_directory_changes: Optional[bool] = None,
        watch_delete_file_changes: Optional[bool] = None,
        watch_delete_key_changes: Optional[bool] = None,
        watch_delete_value_changes: Optional[bool] = None,
        watch_permissions_directory_changes: Optional[bool] = None,
        watch_permissions_file_changes: Optional[bool] = None,
        watch_permissions_key_changes: Optional[bool] = None,
        watch_rename_directory_changes: Optional[bool] = None,
        watch_rename_file_changes: Optional[bool] = None,
        watch_rename_key_changes: Optional[bool] = None,
        watch_set_value_changes: Optional[bool] = None,
        watch_write_file_changes: Optional[bool] = None,
        body: Optional[dict] = None,
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
        description: Optional[str] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rule_groups(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule_group(
        self,
        *,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def signal_changes(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_actions(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_changes(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_changes_scroll(
        self,
        *,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_policies(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        type: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_scheduled_exclusions(
        self,
        *args: Union[str, List[str]],
        policy_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rule_groups(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        type: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    getActionsMixin0 = get_actions
    startActions = start_actions
    getContents = get_contents
    updatePolicyHostGroups = update_policy_host_groups
    updatePolicyPrecedence = update_policy_precedence
    updatePolicyRuleGroups = update_policy_rule_groups
    getPolicies = get_policies
    createPolicies = create_policy
    deletePolicies = delete_policies
    updatePolicies = update_policies
    getScheduledExclusions = get_scheduled_exclusions
    createScheduledExclusions = create_scheduled_exclusions
    deleteScheduledExclusions = delete_scheduled_exclusions
    updateScheduledExclusions = update_scheduled_exclusions
    updateRuleGroupPrecedence = update_rule_group_precedence
    getRules = get_rules
    createRules = create_rule
    deleteRules = delete_rules
    updateRules = update_rule
    getRuleGroups = get_rule_groups
    createRuleGroups = create_rule_group
    deleteRuleGroups = delete_rule_groups
    updateRuleGroups = update_rule_group
    getChanges = get_changes
    signalChangesExternal = signal_changes
    queryActionsMixin0 = query_actions
    queryChanges = query_changes
    highVolumeQueryChanges = query_changes_scroll
    queryRuleGroups = query_rule_groups
    queryScheduledExclusions = query_scheduled_exclusions
    queryPolicies = query_policies
