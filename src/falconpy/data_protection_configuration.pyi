"""Type stubs for data_protection_configuration."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class DataProtectionConfiguration(ServiceClass):

    def get_classification(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_classification(
        self,
        *,
        classification_properties: Optional[dict] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_classifications(
        self,
        *,
        classification_properties: Optional[dict] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_classification(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cloud_application(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_cloud_application(
        self,
        *,
        description: Optional[str] = None,
        name: Optional[str] = None,
        urls: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_cloud_application(
        self,
        *,
        id: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        urls: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_cloud_application(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_content_pattern(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_content_pattern(
        self,
        *,
        category: Optional[str] = None,
        description: Optional[str] = None,
        example: Optional[str] = None,
        min_match_threshold: Optional[int] = None,
        name: Optional[str] = None,
        regexes: Optional[Union[str, List[str]]] = None,
        region: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_content_pattern(
        self,
        *,
        id: Optional[str] = None,
        description: Optional[str] = None,
        example: Optional[str] = None,
        min_match_threshold: Optional[int] = None,
        name: Optional[str] = None,
        regexes: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_content_pattern(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_precedence(
        self,
        *,
        platform: Optional[str] = None,
        precedence: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_enterprise_account(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_enterprise_account(
        self,
        *,
        application_group_id: Optional[str] = None,
        domains: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        plugin_config_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_enterprise_account(
        self,
        *,
        id: Optional[str] = None,
        domains: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_enterprise_account(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_file_type(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sensitivity_label(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_sensitivity_label(
        self,
        *,
        co_authoring: Optional[bool] = None,
        display_name: Optional[str] = None,
        external_id: Optional[str] = None,
        label_provider: Optional[str] = None,
        name: Optional[str] = None,
        plugins_configuration_id: Optional[str] = None,
        synced: Optional[bool] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_sensitivity_label(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_local_application_group(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_local_application_group(
        self,
        *,
        description: Optional[str] = None,
        local_application_ids: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_local_application_group(
        self,
        *,
        id: Optional[str] = None,
        description: Optional[str] = None,
        local_application_ids: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_local_application_group(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_local_application(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_local_application(
        self,
        *,
        apply_rules_for_children_processes: Optional[bool] = None,
        emit_rule_matched_events_only: Optional[bool] = None,
        enable_rename_detection: Optional[bool] = None,
        executable_name: Optional[str] = None,
        group_ids: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_local_application(
        self,
        *,
        id: Optional[str] = None,
        apply_rules_for_children_processes: Optional[bool] = None,
        emit_rule_matched_events_only: Optional[bool] = None,
        enable_rename_detection: Optional[bool] = None,
        executable_name: Optional[str] = None,
        group_ids: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_local_application(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
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
        platform_name: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        policy_properties: Optional[dict] = None,
        precedence: Optional[int] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policies(
        self,
        *,
        platform_name: Optional[str] = None,
        description: Optional[str] = None,
        host_groups: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        is_enabled: Optional[bool] = None,
        name: Optional[str] = None,
        policy_properties: Optional[dict] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_policies(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        platform_name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_web_location(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_web_location(
        self,
        *,
        web_locations: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_web_location(
        self,
        *,
        id: Optional[str] = None,
        application_id: Optional[str] = None,
        deleted: Optional[bool] = None,
        enterprise_account_id: Optional[str] = None,
        location_type: Optional[str] = None,
        name: Optional[str] = None,
        provider_location_id: Optional[str] = None,
        provider_location_name: Optional[str] = None,
        type: Optional[str] = None,
        web_location_group_ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_web_location(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_classifications(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_cloud_applications(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_content_patterns(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_enterprise_accounts(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_file_type(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_sensitivity_label(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_local_application_groups(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_local_applications(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_policies(
        self,
        *,
        platform_name: Optional[str] = None,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_web_locations(
        self,
        *,
        filter: Optional[str] = None,
        type: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    entities_classification_get_v2 = get_classification
    entities_classification_post_v2 = create_classification
    entities_classification_patch_v2 = update_classifications
    entities_classification_delete_v2 = delete_classification
    entities_cloud_application_get = get_cloud_application
    entities_cloud_application_create = create_cloud_application
    entities_cloud_application_patch = update_cloud_application
    entities_cloud_application_delete = delete_cloud_application
    entities_content_pattern_get = get_content_pattern
    entities_content_pattern_create = create_content_pattern
    entities_content_pattern_patch = update_content_pattern
    entities_content_pattern_delete = delete_content_pattern
    entities_policy_precedence_post_v1 = update_policy_precedence
    entities_enterprise_account_get = get_enterprise_account
    entities_enterprise_account_create = create_enterprise_account
    entities_enterprise_account_patch = update_enterprise_account
    entities_enterprise_account_delete = delete_enterprise_account
    entities_file_type_get = get_file_type
    entities_sensitivity_label_get_v2 = get_sensitivity_label
    entities_sensitivity_label_create_v2 = create_sensitivity_label
    entities_sensitivity_label_delete_v2 = delete_sensitivity_label
    entities_local_application_group_get = get_local_application_group
    entities_local_application_group_create = create_local_application_group
    entities_local_application_group_patch = update_local_application_group
    entities_local_application_group_delete = delete_local_application_group
    entities_local_application_get = get_local_application
    entities_local_application_create = create_local_application
    entities_local_application_patch = update_local_application
    entities_local_application_delete = delete_local_application
    entities_policy_get_v2 = get_policies
    entities_policy_post_v2 = create_policy
    entities_policy_patch_v2 = update_policies
    entities_policy_delete_v2 = delete_policies
    entities_web_location_get_v2 = get_web_location
    entities_web_location_create_v2 = create_web_location
    entities_web_location_patch_v2 = update_web_location
    entities_web_location_delete_v2 = delete_web_location
    queries_classification_get_v2 = query_classifications
    queries_cloud_application_get_v2 = query_cloud_applications
    queries_content_pattern_get_v2 = query_content_patterns
    queries_enterprise_account_get_v2 = query_enterprise_accounts
    queries_file_type_get_v2 = query_file_type
    queries_sensitivity_label_get_v2 = query_sensitivity_label
    queries_local_application_group_get = query_local_application_groups
    queries_local_application_get = query_local_applications
    queries_policy_get_v2 = query_policies
    queries_web_location_get_v2 = query_web_locations
