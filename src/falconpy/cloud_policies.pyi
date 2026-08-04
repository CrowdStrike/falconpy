"""Type stubs for cloud_policies."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudPolicies(ServiceClass):

    def get_rule_input_schema(
        self,
        *,
        domain: Optional[str] = None,
        subdomain: Optional[str] = None,
        cloud_provider: Optional[str] = None,
        resource_type: Optional[str] = None,
        enriched: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def replace_control_rules(
        self,
        *,
        ids: Optional[str] = None,
        rule_ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_compliance_controls(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_compliance_control(
        self,
        *,
        description: Optional[str] = None,
        framework_id: Optional[str] = None,
        name: Optional[str] = None,
        section_name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_compliance_control(
        self,
        *,
        ids: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_compliance_control(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def rename_section_compliance_framework(
        self,
        *,
        ids: Optional[str] = None,
        sectionName: Optional[str] = None,
        section_name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_compliance_frameworks(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_compliance_framework(
        self,
        *,
        active: Optional[bool] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_compliance_framework(
        self,
        *,
        ids: Optional[str] = None,
        active: Optional[bool] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_compliance_framework(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_enriched_asset(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        domain: Optional[str] = None,
        subdomain: Optional[str] = None,
        resource_type: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_evaluation_result(
        self,
        *,
        cloud_provider: Optional[str] = None,
        resource_type: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        domain: Optional[str] = None,
        input: Optional[dict] = None,
        logic: Optional[str] = None,
        subdomain: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule_override(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule_override(
        self,
        *,
        overrides: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule_override(
        self,
        *,
        overrides: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rule_override(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule(
        self,
        *,
        alert_info: Optional[str] = None,
        attack_types: Optional[str] = None,
        category: Optional[str] = None,
        controls: Optional[list] = None,
        description: Optional[str] = None,
        domain: Optional[str] = None,
        labels: Optional[Union[str, List[str]]] = None,
        logic: Optional[str] = None,
        name: Optional[str] = None,
        parent_rule_id: Optional[str] = None,
        platform: Optional[str] = None,
        provider: Optional[str] = None,
        remediation_info: Optional[str] = None,
        remediation_url: Optional[str] = None,
        resource_type: Optional[str] = None,
        severity: Optional[int] = None,
        subdomain: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule(
        self,
        *,
        alert_info: Optional[str] = None,
        attack_types: Optional[Union[str, List[str]]] = None,
        category: Optional[str] = None,
        controls: Optional[list] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        rule_logic_list: Optional[list] = None,
        severity: Optional[int] = None,
        uuid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rule(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_compliance_controls(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_compliance_frameworks(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rule(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_suppression_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_suppression_rule(
        self,
        *,
        description: Optional[str] = None,
        domain: Optional[str] = None,
        name: Optional[str] = None,
        rule_selection_filter: Optional[dict] = None,
        rule_selection_type: Optional[str] = None,
        scope_asset_filter: Optional[dict] = None,
        scope_type: Optional[str] = None,
        subdomain: Optional[str] = None,
        suppression_comment: Optional[str] = None,
        suppression_expiration_date: Optional[str] = None,
        suppression_reason: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_suppression_rule(
        self,
        *,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        rule_selection_filter: Optional[dict] = None,
        rule_selection_type: Optional[str] = None,
        scope_asset_filter: Optional[dict] = None,
        scope_type: Optional[str] = None,
        suppression_comment: Optional[str] = None,
        suppression_expiration_date: Optional[str] = None,
        suppression_reason: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_suppression_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_suppression_rules(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def clone_compliance_framework(
        self,
        *,
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    CloneComplianceFramework = clone_compliance_framework
    ReplaceControlRules = replace_control_rules
    GetComplianceControls = get_compliance_controls
    CreateComplianceControl = create_compliance_control
    UpdateComplianceControl = update_compliance_control
    DeleteComplianceControl = delete_compliance_control
    RenameSectionComplianceFramework = rename_section_compliance_framework
    GetComplianceFrameworks = get_compliance_frameworks
    CreateComplianceFramework = create_compliance_framework
    UpdateComplianceFramework = update_compliance_framework
    DeleteComplianceFramework = delete_compliance_framework
    GetEvaluationResult = get_evaluation_result
    GetRuleOverride = get_rule_override
    CreateRuleOverride = create_rule_override
    UpdateRuleOverride = update_rule_override
    DeleteRuleOverride = delete_rule_override
    GetRule = get_rule
    CreateRuleMixin0 = create_rule
    UpdateRule = update_rule
    DeleteRuleMixin0 = delete_rule
    QueryComplianceControls = query_compliance_controls
    QueryComplianceFrameworks = query_compliance_frameworks
    QueryRule = query_rule
    GetRuleInputSchema = get_rule_input_schema
    GetEnrichedAsset = get_enriched_asset
    QuerySuppressionRules = query_suppression_rules
    DeleteSuppressionRules = delete_suppression_rules
    UpdateSuppressionRule = update_suppression_rule
    CreateSuppressionRule = create_suppression_rule
    GetSuppressionRules = get_suppression_rules
