"""Type stubs for correlation_rules."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CorrelationRules(ServiceClass):

    def aggregate_rule_versions(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules_combined(
        self,
        *,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules_combined_v2(
        self,
        *,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_latest_rule_versions(
        self,
        *args: Union[str, List[str]],
        rule_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def export_rule(
        self,
        *,
        get_latest: Optional[bool] = None,
        report_format: Optional[str] = None,
        search: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def import_rule(
        self,
        *,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def publish_rule_version(
        self,
        *,
        id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rule_versions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule(
        self,
        *,
        anomaly: Optional[dict] = None,
        comment: Optional[str] = None,
        customer_id: Optional[str] = None,
        description: Optional[str] = None,
        guardrail_notifications: Optional[list] = None,
        mitre_attack: Optional[list] = None,
        name: Optional[str] = None,
        notifications: Optional[list] = None,
        operation: Optional[dict] = None,
        search: Optional[dict] = None,
        severity: Optional[int] = None,
        status: Optional[str] = None,
        tactic: Optional[str] = None,
        technique: Optional[str] = None,
        template_id: Optional[str] = None,
        trigger_on_create: Optional[bool] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule(
        self,
        *,
        anomaly: Optional[dict] = None,
        comment: Optional[str] = None,
        description: Optional[str] = None,
        guardrail_notifications: Optional[list] = None,
        id: Optional[str] = None,
        mitre_attack: Optional[list] = None,
        name: Optional[str] = None,
        notifications: Optional[list] = None,
        operation: Optional[dict] = None,
        search: Optional[dict] = None,
        severity: Optional[int] = None,
        state: Optional[str] = None,
        status: Optional[str] = None,
        tactic: Optional[str] = None,
        technique: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rules(
        self,
        *,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rules_v2(
        self,
        *,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_rule_template_ids(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule_from_template(
        self,
        *,
        customer_id: Optional[str] = None,
        templates: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule_templates_by_id(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    aggregates_rule_versions_post_v1 = aggregate_rule_versions
    combined_rules_get_v1 = get_rules_combined
    combined_rules_get_v2 = get_rules_combined_v2
    entities_latest_rules_get_v1 = get_latest_rule_versions
    entities_rule_versions_export_post_v1 = export_rule
    entities_rule_versions_import_post_v1 = import_rule
    entities_rule_versions_publish_patch_v1 = publish_rule_version
    entities_rule_versions_delete_v1 = delete_rule_versions
    entities_rules_get_v1 = get_rules
    entities_rules_get_v2 = get_rules_v2
    entities_rules_post_v1 = create_rule
    entities_rules_delete_v1 = delete_rules
    entities_rules_patch_v1 = update_rule
    queries_rules_get_v1 = query_rules
    queries_rules_get_v2 = query_rules_v2
    queries_templates_get_v1Mixin0 = search_rule_template_ids
    entities_templates_rules_post_v1 = create_rule_from_template
    entities_templates_get_v1Mixin0 = get_rule_templates_by_id
