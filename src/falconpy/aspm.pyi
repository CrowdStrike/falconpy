"""Type stubs for aspm."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ASPM(ServiceClass):

    def execute_function_data_count(
        self,
        *,
        query_name: Optional[str] = None,
        cloud_provider: Optional[str] = None,
        aws_lambda_arn: Optional[str] = None,
        gcp_cloud_function_url: Optional[str] = None,
        azure_site_subscription_id: Optional[str] = None,
        azure_site_resource_group: Optional[str] = None,
        azure_function_app_name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_functions_count(
        self,
        *,
        query_name: Optional[str] = None,
        cloud_provider: Optional[Union[str, List[str]]] = None,
        cloud_account_id: Optional[Union[str, List[str]]] = None,
        region: Optional[Union[str, List[str]]] = None,
        cid: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_function_data_query_count(
        self,
        *,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_functions_query_count(
        self,
        *,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_function_data(
        self,
        *,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_functions_over_time(
        self,
        *,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_functions(
        self,
        *,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_function_data_query(
        self,
        *,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_functions_query_over_time(
        self,
        *,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_functions_query(
        self,
        *,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_service_artifacts(
        self,
        *,
        persistentSignature: Optional[str] = None,
        optionalTime: Optional[int] = None,
        revisionId: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orderBy: Optional[Union[str, List[str]]] = None,
        direction: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_business_applications(
        self,
        *,
        name: Optional[str] = None,
        persistentSignatures: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cloud_security_integration_state(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def set_cloud_security_integration_state(
        self,
        *,
        isEnabled: Optional[bool] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_executor_nodes(
        self,
        *,
        node_type: Optional[str] = None,
        integration_type: Optional[int] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        order_by: Optional[str] = None,
        direction: Optional[str] = None,
        executor_node_ids: Optional[Union[str, List[str]]] = None,
        executor_node_names: Optional[Union[str, List[str]]] = None,
        executor_node_states: Optional[Union[str, List[str]]] = None,
        executor_node_types: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_executor_node(
        self,
        *,
        additional_header: Optional[str] = None,
        current_aws_arn: Optional[str] = None,
        dashboard_url: Optional[str] = None,
        id: Optional[str] = None,
        last_health_check: Optional[int] = None,
        name: Optional[str] = None,
        node_type: Optional[str] = None,
        password: Optional[str] = None,
        pod_settings: Optional[dict] = None,
        proxy_address: Optional[str] = None,
        status: Optional[dict] = None,
        type: Optional[str] = None,
        useJobs: Optional[bool] = None,
        username: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_executor_node(
        self,
        *,
        additional_header: Optional[str] = None,
        current_aws_arn: Optional[str] = None,
        dashboard_url: Optional[str] = None,
        id: Optional[str] = None,
        last_health_check: Optional[int] = None,
        name: Optional[str] = None,
        node_type: Optional[str] = None,
        password: Optional[str] = None,
        pod_settings: Optional[dict] = None,
        proxy_address: Optional[str] = None,
        status: Optional[dict] = None,
        type: Optional[str] = None,
        useJobs: Optional[bool] = None,
        username: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_executor_nodes_metadata(
        self,
        *,
        executor_node_ids: Optional[Union[str, List[str]]] = None,
        executor_node_names: Optional[Union[str, List[str]]] = None,
        executor_node_states: Optional[Union[str, List[str]]] = None,
        executor_node_types: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_node(
        self,
        *,
        ID: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def retrieve_relay_instances(
        self,
        *,
        ID: Optional[int] = None,
        additional_header: Optional[str] = None,
        current_aws_arn: Optional[str] = None,
        dashboard_url: Optional[str] = None,
        id: Optional[str] = None,
        last_health_check: Optional[int] = None,
        name: Optional[str] = None,
        node_type: Optional[str] = None,
        password: Optional[str] = None,
        pod_settings: Optional[dict] = None,
        proxy_address: Optional[str] = None,
        status: Optional[dict] = None,
        type: Optional[str] = None,
        useJobs: Optional[bool] = None,
        username: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_integration_tasks(
        self,
        *,
        integration_task_type: Optional[int] = None,
        category: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        orderBy: Optional[str] = None,
        direction: Optional[str] = None,
        integration_task_types: Optional[int] = None,
        ids: Optional[int] = None,
        names: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_integration_task(
        self,
        *,
        integration_task: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_integration_tasks_admin(
        self,
        *,
        integration_task_type: Optional[int] = None,
        category: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        orderBy: Optional[str] = None,
        direction: Optional[str] = None,
        integration_task_types: Optional[int] = None,
        ids: Optional[int] = None,
        names: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_integration_tasks_metadata(
        self,
        *,
        category: Optional[str] = None,
        integration_task_types: Optional[int] = None,
        ids: Optional[int] = None,
        names: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_integration_tasks_v2(
        self,
        *,
        integration_task_type: Optional[int] = None,
        category: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        orderBy: Optional[str] = None,
        direction: Optional[str] = None,
        integration_task_types: Optional[int] = None,
        ids: Optional[int] = None,
        names: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_integration_task(
        self,
        *,
        ID: Optional[int] = None,
        integration_task: Optional[dict] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_integration_task(
        self,
        *,
        ID: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def run_integration_task(
        self,
        *,
        ID: Optional[int] = None,
        category: Optional[str] = None,
        access_token: Optional[str] = None,
        data: Optional[str] = None,
        override: Optional[bool] = None,
        scheduled: Optional[bool] = None,
        task_id: Optional[int] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def run_integration_task_admin(
        self,
        *,
        ID: Optional[int] = None,
        category: Optional[str] = None,
        access_token: Optional[str] = None,
        data: Optional[str] = None,
        override: Optional[bool] = None,
        scheduled: Optional[bool] = None,
        task_id: Optional[int] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def run_integration_task_v2(
        self,
        *,
        ID: Optional[int] = None,
        category: Optional[str] = None,
        access_token: Optional[str] = None,
        data: Optional[str] = None,
        override: Optional[bool] = None,
        scheduled: Optional[bool] = None,
        task_id: Optional[int] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_integration_types(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_integrations(
        self,
        *,
        integration_type: Optional[int] = None,
        category: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_integration(
        self,
        *,
        integration: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_integrations_v2(
        self,
        *,
        integration_type: Optional[int] = None,
        category: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_integration(
        self,
        *,
        ID: Optional[int] = None,
        integration: Optional[dict] = None,
        overwriteFields: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_integration(
        self,
        *,
        ID: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_query(
        self,
        *,
        paginate: Optional[dict] = None,
        query: Optional[str] = None,
        revisionId: Optional[int] = None,
        selectFields: Optional[dict] = None,
        timestamp: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_servicenow_deployments(
        self,
        *,
        ql_filters: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orderBy: Optional[str] = None,
        direction: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_servicenow_services(
        self,
        *,
        ql_filters: Optional[str] = None,
        exclude_artifacts: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        orderBy: Optional[str] = None,
        direction: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_services_count(
        self,
        *,
        cids: Optional[Union[str, List[str]]] = None,
        deploymentTupleFilters: Optional[list] = None,
        nestingLevel: Optional[int] = None,
        onlyCount: Optional[bool] = None,
        optionalTime: Optional[int] = None,
        pagination: Optional[dict] = None,
        persistentSignatures: Optional[Union[str, List[str]]] = None,
        qlFilters: Optional[str] = None,
        relatedEntities: Optional[list] = None,
        revisionId: Optional[int] = None,
        rolesSignature: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_service_violation_types(
        self,
        *,
        filter: Optional[dict] = None,
        optionalTime: Optional[int] = None,
        revisionId: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_tags(
        self,
        *,
        isUnique: Optional[bool] = None,
        tagName: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        name: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_tags(
        self,
        *,
        entries: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_tags(
        self,
        *,
        entries: Optional[list] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_users_v2(
        self,
        *,
        pagination: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def post_group_v2(
        self,
        *,
        children: Optional[list] = None,
        description: Optional[str] = None,
        groupType: Optional[str] = None,
        isDefault: Optional[bool] = None,
        name: Optional[str] = None,
        parentId: Optional[int] = None,
        scope: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_group(
        self,
        *,
        ID: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_default_group(
        self,
        *,
        ID: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_group_v2(
        self,
        *,
        ID: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_group(
        self,
        *,
        ID: Optional[int] = None,
        children: Optional[list] = None,
        description: Optional[str] = None,
        groupId: Optional[int] = None,
        groupType: Optional[str] = None,
        isDefault: Optional[bool] = None,
        name: Optional[str] = None,
        parentId: Optional[int] = None,
        scope: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_group_hierarchy(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_groups_v2(
        self,
        *,
        type: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ExecuteFunctionDataCount = execute_function_data_count
    ExecuteFunctionsCount = execute_functions_count
    ExecuteFunctionDataQueryCount = execute_function_data_query_count
    ExecuteFunctionsQueryCount = execute_functions_query_count
    ExecuteFunctionData = execute_function_data
    ExecuteFunctionsOvertime = execute_functions_over_time
    ExecuteFunctions = execute_functions
    ExecuteFunctionDataQuery = execute_function_data_query
    ExecuteFunctionsQueryOvertime = execute_functions_query_over_time
    ExecuteFunctionsQuery = execute_functions_query
    getServiceArtifacts = get_service_artifacts
    UpsertBusinessApplications = update_business_applications
    GetCloudSecurityIntegrationState = get_cloud_security_integration_state
    SetCloudSecurityIntegrationState = set_cloud_security_integration_state
    GetExecutorNodes = get_executor_nodes
    UpdateExecutorNode = update_executor_node
    CreateExecutorNode = create_executor_node
    GetExecutorNodesMetadata = get_executor_nodes_metadata
    RetrieveRelayInstances = retrieve_relay_instances
    DeleteExecutorNode = delete_node
    GetIntegrationTasks = get_integration_tasks
    CreateIntegrationTask = create_integration_task
    GetIntegrationTasksAdmin = get_integration_tasks_admin
    GetIntegrationTasksMetadata = get_integration_tasks_metadata
    GetIntegrationTasksV2 = get_integration_tasks_v2
    UpdateIntegrationTask = update_integration_task
    DeleteIntegrationTask = delete_integration_task
    RunIntegrationTask = run_integration_task
    RunIntegrationTaskV2 = run_integration_task_v2
    RunIntegrationTaskAdmin = run_integration_task_admin
    GetIntegrationTypes = get_integration_types
    GetIntegrations = get_integrations
    CreateIntegration = create_integration
    GetIntegrationsV2 = get_integrations_v2
    UpdateIntegration = update_integration
    DeleteIntegration = delete_integration
    ExecuteQuery = execute_query
    ServiceNowGetDeployments = get_servicenow_deployments
    ServiceNowGetServices = get_servicenow_services
    GetServicesCount = get_services_count
    GetServiceViolationTypes = get_service_violation_types
    GetTags = get_tags
    UpsertTags = update_tags
    DeleteTags = delete_tags
    GetUsersV2 = get_users_v2
    PostGroupV2 = post_group_v2
    DeleteGroup = delete_group
    UpdateDefaultGroup = update_default_group
    GetGroupV2 = get_group_v2
    UpdateGroup = update_group
    GetGroupHierarchy = get_group_hierarchy
    GetGroupsV2 = get_groups_v2
