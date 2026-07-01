"""Type stubs for sensor_update_policy."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class SensorUpdatePolicy(ServiceClass):

    def reveal_uninstall_token(
        self,
        *,
        audit_message: Optional[str] = None,
        device_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def increment_uninstall_token(
        self,
        *,
        audit_message: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_builds(
        self,
        *args: Union[str, List[str]],
        platform: Optional[str] = None,
        stage: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_kernels(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_policy_members(
        self,
        *,
        id: Optional[str] = None,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_policies(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_combined_policies_v2(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def perform_policies_action(
        self,
        *,
        action_name: Optional[str] = None,
        action_parameters: Optional[list] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def set_policies_precedence(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        platform_name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_policies(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_policies(
        self,
        *,
        description: Optional[str] = None,
        name: Optional[str] = None,
        platform_name: Optional[str] = None,
        settings: Optional[dict] = None,
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
        id: Optional[str] = None,
        name: Optional[str] = None,
        settings: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_policies_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_policies_v2(
        self,
        *,
        description: Optional[str] = None,
        name: Optional[str] = None,
        platform_name: Optional[str] = None,
        settings: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policies_v2(
        self,
        *,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        settings: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_kernels(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_policy_members(
        self,
        *,
        id: Optional[str] = None,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_policies(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    revealUninstallToken = reveal_uninstall_token
    incrementUninstallToken = increment_uninstall_token
    queryCombinedSensorUpdateBuilds = query_combined_builds
    queryCombinedSensorUpdateKernels = query_combined_kernels
    queryCombinedSensorUpdatePolicyMembers = query_combined_policy_members
    queryCombinedSensorUpdatePolicies = query_combined_policies
    queryCombinedSensorUpdatePoliciesV2 = query_combined_policies_v2
    performSensorUpdatePoliciesAction = perform_policies_action
    setSensorUpdatePoliciesPrecedence = set_policies_precedence
    getSensorUpdatePolicies = get_policies
    createSensorUpdatePolicies = create_policies
    deleteSensorUpdatePolicies = delete_policies
    updateSensorUpdatePolicies = update_policies
    getSensorUpdatePoliciesV2 = get_policies_v2
    createSensorUpdatePoliciesV2 = create_policies_v2
    updateSensorUpdatePoliciesV2 = update_policies_v2
    querySensorUpdateKernelsDistinct = query_kernels
    querySensorUpdatePolicyMembers = query_policy_members
    querySensorUpdatePolicies = query_policies
