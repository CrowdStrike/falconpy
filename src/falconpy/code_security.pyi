"""Type stubs for code_security."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CodeSecurity(ServiceClass):

    def get_scm_repository_aggregates(
        self,
        *,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_branch_config(
        self,
        *,
        connection_id: Optional[str] = None,
        repository_ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_branch_config(
        self,
        *,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_branch_config(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_branch_config(
        self,
        *,
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_scm_connections(
        self,
        *,
        provider: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scm_connection(
        self,
        *,
        uuid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_scm_connection(
        self,
        *,
        uuid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def trigger_scm_sync(
        self,
        *,
        uuid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_scm_exclusion_rules(
        self,
        *,
        connection_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_scm_exclusion_rule(
        self,
        *,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_scm_exclusion_rule(
        self,
        *,
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_scm_repositories(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def exchange_github_app_code(
        self,
        *,
        code: Optional[str] = None,
        installation_id: Optional[str] = None,
        org: Optional[str] = None,
        state: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def register_scm_app(
        self,
        *,
        app_id: Optional[str] = None,
        installation_id: Optional[str] = None,
        org: Optional[str] = None,
        private_key: Optional[str] = None,
        webhook_secret: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetSCMRepositoryAggregates = get_scm_repository_aggregates
    GetBranchConfig = get_branch_config
    CreateBranchConfig = create_branch_config
    DeleteBranchConfig = delete_branch_config
    UpdateBranchConfig = update_branch_config
    ListSCMConnections = list_scm_connections
    GetSCMConnection = get_scm_connection
    DeleteSCMConnection = delete_scm_connection
    TriggerSCMSync = trigger_scm_sync
    ListExclusionRules = list_scm_exclusion_rules
    CreateExclusionRule = create_scm_exclusion_rule
    DeleteExclusionRule = delete_scm_exclusion_rule
    ListSCMRepositories = list_scm_repositories
    ExchangeGitHubAppCode = exchange_github_app_code
    RegisterSCMApp = register_scm_app
