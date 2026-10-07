"""Type stubs for it_automation."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ITAutomation(ServiceClass):

    def get_associated_tasks(
        self,
        *,
        id: Optional[str] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def scheduled_task_details(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_executions_by_query(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_task_groups_by_query(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_tasks_by_query(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_group(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_user_group(
        self,
        *,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_user_group(
        self,
        *,
        id: Optional[str] = None,
        add_user_ids: Optional[Union[str, List[str]]] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        remove_user_ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_user_groups(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def run_live_query(
        self,
        *,
        composite_query: Optional[dict] = None,
        discover_new_hosts: Optional[bool] = None,
        discover_offline_hosts: Optional[bool] = None,
        distribute: Optional[bool] = None,
        expiration_interval: Optional[str] = None,
        guardrails: Optional[dict] = None,
        osquery: Optional[str] = None,
        output_parser_config: Optional[dict] = None,
        queries: Optional[dict] = None,
        rows_parser_config: Optional[dict] = None,
        target: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_host_groups(
        self,
        *,
        action: Optional[str] = None,
        host_group_ids: Optional[Union[str, List[str]]] = None,
        policy_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policies_precedence(
        self,
        *,
        platform: Optional[str] = None,
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
        config: Optional[dict] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        platform: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy(
        self,
        *,
        config: Optional[dict] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        is_enabled: Optional[bool] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_policy(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scheduled_task(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_scheduled_task(
        self,
        *,
        discover_new_hosts: Optional[bool] = None,
        discover_offline_hosts: Optional[bool] = None,
        distribute: Optional[bool] = None,
        execution_args: Optional[dict] = None,
        expiration_interval: Optional[str] = None,
        guardrails: Optional[dict] = None,
        is_active: Optional[bool] = None,
        schedule: Optional[dict] = None,
        schedule_name: Optional[str] = None,
        target: Optional[str] = None,
        task_id: Optional[str] = None,
        trigger_condition: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_scheduled_task(
        self,
        *,
        id: Optional[str] = None,
        discover_new_hosts: Optional[bool] = None,
        discover_offline_hosts: Optional[bool] = None,
        distribute: Optional[bool] = None,
        execution_args: Optional[dict] = None,
        expiration_interval: Optional[str] = None,
        guardrails: Optional[dict] = None,
        is_active: Optional[bool] = None,
        schedule: Optional[dict] = None,
        schedule_name: Optional[str] = None,
        target: Optional[str] = None,
        task_id: Optional[str] = None,
        trigger_condition: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_scheduled_task(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cancel_execution(
        self,
        *args: Union[str, List[str]],
        task_execution_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_execution_host_status(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def rerun_execution(
        self,
        *,
        run_type: Optional[str] = None,
        run_types: Optional[Union[str, List[str]]] = None,
        task_execution_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_execution_results_search_status(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execution_results_search(
        self,
        *,
        filter_expressions: Optional[Union[str, List[str]]] = None,
        group_by_fields: Optional[Union[str, List[str]]] = None,
        search_end: Optional[str] = None,
        search_start: Optional[str] = None,
        task_execution_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_execution_results(
        self,
        *,
        id: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_execution(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def start_execution(
        self,
        *,
        discover_new_hosts: Optional[bool] = None,
        discover_offline_hosts: Optional[bool] = None,
        distribute: Optional[bool] = None,
        execution_args: Optional[dict] = None,
        expiration_interval: Optional[str] = None,
        guardrails: Optional[dict] = None,
        scheduled_task_id: Optional[str] = None,
        target: Optional[str] = None,
        task_id: Optional[str] = None,
        trigger_condition: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_task_group(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_task_group(
        self,
        *,
        access_type: Optional[str] = None,
        assigned_user_group_ids: Optional[Union[str, List[str]]] = None,
        assigned_user_ids: Optional[Union[str, List[str]]] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        task_ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_task_group(
        self,
        *,
        id: Optional[str] = None,
        access_type: Optional[str] = None,
        add_assigned_user_group_ids: Optional[Union[str, List[str]]] = None,
        add_assigned_user_ids: Optional[Union[str, List[str]]] = None,
        add_task_ids: Optional[Union[str, List[str]]] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        remove_assigned_user_group_ids: Optional[Union[str, List[str]]] = None,
        remove_assigned_user_ids: Optional[Union[str, List[str]]] = None,
        remove_task_ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_task_groups(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_tasks(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_task(
        self,
        *,
        access_type: Optional[str] = None,
        assigned_user_group_ids: Optional[Union[str, List[str]]] = None,
        assigned_user_ids: Optional[Union[str, List[str]]] = None,
        composite_query: Optional[dict] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        os_query: Optional[str] = None,
        output_parser_config: Optional[dict] = None,
        queries: Optional[dict] = None,
        remediations: Optional[dict] = None,
        rows_parser_config: Optional[dict] = None,
        target: Optional[str] = None,
        task_group_id: Optional[str] = None,
        task_parameters: Optional[list] = None,
        task_type: Optional[str] = None,
        trigger_condition: Optional[list] = None,
        verification_condition: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_task(
        self,
        *,
        id: Optional[str] = None,
        access_type: Optional[str] = None,
        add_assigned_user_group_ids: Optional[Union[str, List[str]]] = None,
        add_assigned_user_ids: Optional[Union[str, List[str]]] = None,
        composite_query: Optional[dict] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        os_query: Optional[str] = None,
        output_parser_config: Optional[dict] = None,
        queries: Optional[dict] = None,
        remediations: Optional[dict] = None,
        remove_assigned_user_group_ids: Optional[Union[str, List[str]]] = None,
        remove_assigned_user_ids: Optional[Union[str, List[str]]] = None,
        rows_parser_config: Optional[dict] = None,
        target: Optional[str] = None,
        task_group_id: Optional[str] = None,
        task_parameters: Optional[list] = None,
        task_type: Optional[str] = None,
        trigger_condition: Optional[list] = None,
        verification_condition: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_task(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_user_groups(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_policies(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        platform: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_scheduled_tasks(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_task_executions(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_task_groups(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_tasks(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_patch_deployment_configs(
        self,
        *,
        date_ranges: Optional[list] = None,
        exclude: Optional[str] = None,
        extended_bounds: Optional[dict] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        filters_spec: Optional[dict] = None,
        include: Optional[str] = None,
        interval: Optional[str] = None,
        max_doc_count: Optional[int] = None,
        min_doc_count: Optional[int] = None,
        missing: Optional[str] = None,
        name: Optional[str] = None,
        percents: Optional[list] = None,
        q: Optional[str] = None,
        ranges: Optional[list] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        sub_aggregates: Optional[list] = None,
        time_zone: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_patch_deployment_executions(
        self,
        *,
        date_ranges: Optional[list] = None,
        exclude: Optional[str] = None,
        extended_bounds: Optional[dict] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        filters_spec: Optional[dict] = None,
        include: Optional[str] = None,
        interval: Optional[str] = None,
        max_doc_count: Optional[int] = None,
        min_doc_count: Optional[int] = None,
        missing: Optional[str] = None,
        name: Optional[str] = None,
        percents: Optional[list] = None,
        q: Optional[str] = None,
        ranges: Optional[list] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        sub_aggregates: Optional[list] = None,
        time_zone: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_patch_host_deployments(
        self,
        *,
        date_ranges: Optional[list] = None,
        exclude: Optional[str] = None,
        extended_bounds: Optional[dict] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        filters_spec: Optional[dict] = None,
        include: Optional[str] = None,
        interval: Optional[str] = None,
        max_doc_count: Optional[int] = None,
        min_doc_count: Optional[int] = None,
        missing: Optional[str] = None,
        name: Optional[str] = None,
        percents: Optional[list] = None,
        q: Optional[str] = None,
        ranges: Optional[list] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        sub_aggregates: Optional[list] = None,
        time_zone: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cancel_patch_deployment_executions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_os_assessment_scan(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        after: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_os_assessments(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        after: Optional[str] = None,
        facets: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_patch_deployment_config(
        self,
        *,
        block_filter_group_ids: Optional[Union[str, List[str]]] = None,
        disabled: Optional[bool] = None,
        name: Optional[str] = None,
        patch_filter_group_ids: Optional[Union[str, List[str]]] = None,
        platform: Optional[str] = None,
        post_patch_script_options: Optional[dict] = None,
        pre_patch_script_options: Optional[dict] = None,
        prestage: Optional[bool] = None,
        reboot_options: Optional[dict] = None,
        recurring: Optional[bool] = None,
        run_now_no_schedule: Optional[bool] = None,
        schedule: Optional[dict] = None,
        target_hosts: Optional[str] = None,
        target_patches: Optional[str] = None,
        user_notification_options: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_patch_deployment_configs(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_patch_deployment_configs(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_patch_deployment_executions(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_host_deployment_patches(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_host_deployments(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_patch_deployment_config(
        self,
        *,
        block_filter_group_ids: Optional[Union[str, List[str]]] = None,
        disabled: Optional[bool] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        patch_filter_group_ids: Optional[Union[str, List[str]]] = None,
        platform: Optional[str] = None,
        post_patch_script_options: Optional[dict] = None,
        pre_patch_script_options: Optional[dict] = None,
        prestage: Optional[bool] = None,
        reboot_options: Optional[dict] = None,
        recurring: Optional[bool] = None,
        run_now_no_schedule: Optional[bool] = None,
        schedule: Optional[dict] = None,
        target_hosts: Optional[str] = None,
        target_patches: Optional[str] = None,
        user_notification_options: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    AggregateDeploymentConfigsV1 = aggregate_patch_deployment_configs
    AggregateDeploymentExecutionsV1 = aggregate_patch_deployment_executions
    AggregateHostDeploymentsV1 = aggregate_patch_host_deployments
    CancelDeploymentExecutionsV1 = cancel_patch_deployment_executions
    CombinedOSAssessments = query_combined_os_assessments
    CombinedOSAssessmentScan = query_combined_os_assessment_scan
    CreateDeploymentConfig = create_patch_deployment_config
    DeleteDeploymentConfigs = delete_patch_deployment_configs
    GetDeploymentConfigsByQueryV1 = query_combined_patch_deployment_configs
    GetDeploymentExecutionsByQueryV1 = query_combined_patch_deployment_executions
    GetHostDeploymentPatchesByQueryV1 = query_combined_host_deployment_patches
    GetHostDeploymentsByQueryV1 = query_combined_host_deployments
    ITAutomationGetAssociatedTasks = get_associated_tasks
    ITAutomationCombinedScheduledTasks = scheduled_task_details
    ITAutomationGetTaskExecutionsByQuery = get_executions_by_query
    ITAutomationGetTaskGroupsByQuery = get_task_groups_by_query
    ITAutomationGetTasksByQuery = get_tasks_by_query
    ITAutomationGetUserGroup = get_user_group
    ITAutomationCreateUserGroup = create_user_group
    ITAutomationUpdateUserGroup = update_user_group
    ITAutomationDeleteUserGroup = delete_user_groups
    ITAutomationRunLiveQuery = run_live_query
    ITAutomationUpdatePolicyHostGroups = update_policy_host_groups
    ITAutomationUpdatePoliciesPrecedence = update_policies_precedence
    ITAutomationGetPolicies = get_policies
    ITAutomationCreatePolicy = create_policy
    ITAutomationUpdatePolicies = update_policy
    ITAutomationDeletePolicy = delete_policy
    ITAutomationGetScheduledTasks = get_scheduled_task
    ITAutomationCreateScheduledTask = create_scheduled_task
    ITAutomationUpdateScheduledTask = update_scheduled_task
    ITAutomationDeleteScheduledTasks = delete_scheduled_task
    ITAutomationCancelTaskExecution = cancel_execution
    ITAutomationGetTaskExecutionHostStatus = get_execution_host_status
    ITAutomationRerunTaskExecution = rerun_execution
    ITAutomationGetExecutionResultsSearchStatus = get_execution_results_search_status
    ITAutomationStartExecutionResultsSearch = execution_results_search
    ITAutomationGetExecutionResults = get_execution_results
    ITAutomationGetTaskExecution = get_execution
    ITAutomationStartTaskExecution = start_execution
    ITAutomationGetTaskGroups = get_task_group
    ITAutomationCreateTaskGroup = create_task_group
    ITAutomationUpdateTaskGroup = update_task_group
    ITAutomationDeleteTaskGroups = delete_task_groups
    ITAutomationGetTasks = get_tasks
    ITAutomationCreateTask = create_task
    ITAutomationUpdateTask = update_task
    ITAutomationDeleteTask = delete_task
    ITAutomationSearchUserGroup = search_user_groups
    ITAutomationQueryPolicies = query_policies
    ITAutomationSearchScheduledTasks = search_scheduled_tasks
    ITAutomationSearchTaskExecutions = search_task_executions
    ITAutomationSearchTaskGroups = search_task_groups
    ITAutomationSearchTasks = search_tasks
    UpdateDeploymentConfig = update_patch_deployment_config
