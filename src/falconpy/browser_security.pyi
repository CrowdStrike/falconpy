"""Type stubs for browser_security."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class BrowserSecurity(ServiceClass):

    def query_combined_seraphic_agents(
        self,
        *,
        filter: Optional[dict] = None,
        limit: Optional[int] = None,
        search: Optional[str] = None,
        skip: Optional[int] = None,
        sort: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def classify_domains(
        self,
        *,
        domains: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def activate_agents(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def deactivate_agents(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def apply_agent_tasks(
        self,
        *,
        agent_id: Optional[str] = None,
        actions: Optional[list] = None,
        ttl: Optional[int] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_seraphic_agents(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_seraphic_audit_logs(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_destination_groups(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_destination_group(
        self,
        *,
        classification: Optional[Union[str, List[str]]] = None,
        countries: Optional[Union[str, List[str]]] = None,
        description: Optional[str] = None,
        domains: Optional[Union[str, List[str]]] = None,
        ipsRange: Optional[list] = None,
        match_ips: Optional[bool] = None,
        name: Optional[str] = None,
        singleIps: Optional[Union[str, List[str]]] = None,
        top_level_domains: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_destination_group(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_destination_group(
        self,
        *,
        id: Optional[str] = None,
        classification: Optional[Union[str, List[str]]] = None,
        countries: Optional[Union[str, List[str]]] = None,
        description: Optional[str] = None,
        domains: Optional[Union[str, List[str]]] = None,
        ipsRange: Optional[list] = None,
        match_ips: Optional[bool] = None,
        name: Optional[str] = None,
        singleIps: Optional[Union[str, List[str]]] = None,
        top_level_domains: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_extension_analysis(
        self,
        *,
        store: Optional[str] = None,
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_seraphic_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_seraphic_rule(
        self,
        *,
        id: Optional[str] = None,
        addExtensionIds: Optional[Union[str, List[str]]] = None,
        addExtensionNames: Optional[Union[str, List[str]]] = None,
        destinations: Optional[dict] = None,
        removeExtensionIds: Optional[Union[str, List[str]]] = None,
        removeExtensionNames: Optional[Union[str, List[str]]] = None,
        status: Optional[dict] = None,
        targets: Optional[dict] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_tenant_settings(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_url_domain_lists(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_url_domain_list(
        self,
        *,
        integrationId: Optional[str] = None,
        urls: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_url_domain_list(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        integrationId: Optional[str] = None,
        urls: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_seraphic_agents(
        self,
        *,
        filter: Optional[dict] = None,
        limit: Optional[int] = None,
        search: Optional[str] = None,
        skip: Optional[int] = None,
        sort: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_destination_groups(
        self,
        *,
        exclude: Optional[Union[str, List[str]]] = None,
        filter: Optional[dict] = None,
        limit: Optional[int] = None,
        search: Optional[str] = None,
        skip: Optional[int] = None,
        sort: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_seraphic_rules(
        self,
        *,
        category: Optional[str] = None,
        advanced_filter: Optional[dict] = None,
        exclude: Optional[list] = None,
        filter: Optional[dict] = None,
        limit: Optional[int] = None,
        rule_ids: Optional[list] = None,
        search: Optional[str] = None,
        skip: Optional[int] = None,
        sort: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    CombinedQueryAgents = query_combined_seraphic_agents
    ClassifyDomains = classify_domains
    ActivateAgents = activate_agents
    DeactivateAgents = deactivate_agents
    ApplyAgentTasks = apply_agent_tasks
    GetAgents = get_seraphic_agents
    GetAuditLogsMixin0 = get_seraphic_audit_logs
    GetDestinationGroups = get_destination_groups
    CreateDestinationGroup = create_destination_group
    DeleteDestinationGroup = delete_destination_group
    UpdateDestinationGroup = update_destination_group
    GetExtensionAnalysis = get_extension_analysis
    GetRules = get_seraphic_rules
    UpdateRuleMixin0 = update_seraphic_rule
    GetTenantSettings = get_tenant_settings
    GetUrlDomainLists = get_url_domain_lists
    AddUrlDomainList = add_url_domain_list
    DeleteUrlDomainList = delete_url_domain_list
    QueryAgents = query_seraphic_agents
    QueryDestinationGroups = query_destination_groups
    QueryRulesMixin0 = query_seraphic_rules
