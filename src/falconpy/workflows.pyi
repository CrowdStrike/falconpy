"""Type stubs for workflows."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Workflows(ServiceClass):

    def search_activities(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        skip_artifact_resolution: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_activities_content(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_definitions(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_executions(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_triggers(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def export_definition(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        sanitize: Optional[bool] = None,
        include_mocks: Optional[bool] = None,
        version: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def import_definition(
        self,
        *,
        name: Optional[str] = None,
        validate_only: Optional[bool] = None,
        include_activity_metadata: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_definition(
        self,
        *,
        validate_only: Optional[bool] = None,
        Definition: Optional[dict] = None,
        change_log: Optional[str] = None,
        enabled: Optional[bool] = None,
        flight_control: Optional[dict] = None,
        id: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute(
        self,
        *,
        execution_cid: Optional[Union[str, List[str]]] = None,
        definition_id: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        key: Optional[str] = None,
        depth: Optional[int] = None,
        source_event_url: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_internal(
        self,
        *,
        execution_cid: Optional[Union[str, List[str]]] = None,
        definition_id: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        key: Optional[str] = None,
        depth: Optional[int] = None,
        batch_size: Optional[int] = None,
        source_event_url: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def mock_execute(
        self,
        *,
        execution_cid: Optional[Union[str, List[str]]] = None,
        definition_id: Optional[str] = None,
        name: Optional[str] = None,
        key: Optional[str] = None,
        depth: Optional[int] = None,
        source_event_url: Optional[str] = None,
        validate_only: Optional[bool] = None,
        skip_validation: Optional[bool] = None,
        ignore_activity_mock_references: Optional[bool] = None,
        definition: Optional[dict] = None,
        mocks: Optional[str] = None,
        on_demand_trigger: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execution_action(
        self,
        *,
        action_name: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execution_results(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        skip_fields: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_human_input(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_human_input(
        self,
        *,
        id: Optional[str] = None,
        input: Optional[str] = None,
        note: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def deprovision(
        self,
        *,
        definition_id: Optional[str] = None,
        deprovision_all: Optional[bool] = None,
        template_id: Optional[str] = None,
        template_name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def promote(
        self,
        *,
        customer_definition_id: Optional[str] = None,
        name: Optional[str] = None,
        parameters: Optional[dict] = None,
        template_id: Optional[str] = None,
        template_name: Optional[str] = None,
        template_version: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def provision(
        self,
        *,
        name: Optional[str] = None,
        parameters: Optional[dict] = None,
        template_id: Optional[str] = None,
        template_name: Optional[str] = None,
        template_version: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def workflow_definition_action(
        self,
        *,
        action_name: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_single_activity_node(
        self,
        *,
        execution_cid: Optional[Union[str, List[str]]] = None,
        definition_id: Optional[str] = None,
        name: Optional[str] = None,
        key: Optional[str] = None,
        depth: Optional[int] = None,
        definition: Optional[dict] = None,
        mocks: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_child_executions(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def workflow_definitions_delete(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    WorkflowActivitiesCombined = search_activities
    WorkflowDefinitionsCombined = search_definitions
    WorkflowActivitiesContentCombined = search_activities_content
    WorkflowDefinitionsDelete = workflow_definitions_delete
    delete_definitions = workflow_definitions_delete
    WorkflowExecutionsCombined = search_executions
    WorkflowSystemDefinitionsDeProvision = deprovision
    WorkflowSystemDefinitionsPromote = promote
    WorkflowSystemDefinitionsProvision = provision
    WorkflowExecuteSingleNodeV1 = execute_single_activity_node
    v1_child_executions_query = query_child_executions
