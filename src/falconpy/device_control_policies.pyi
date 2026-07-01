"""Type stubs for device_control_policies."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class DeviceControlPolicies(ServiceClass):

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

    def get_default_policies(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_default_policies(
        self,
        *,
        custom_notifications: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def perform_action(
        self,
        *,
        action_name: Optional[str] = None,
        action_parameters: Optional[list] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_classes(
        self,
        *,
        policies: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_default_settings(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_default_settings(
        self,
        *,
        bluetooth_custom_notifications: Optional[dict] = None,
        usb_custom_notifications: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def set_precedence(
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
        clone_id: Optional[str] = None,
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

    def get_policies_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_policies_v2(
        self,
        *,
        policies: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policies_v2(
        self,
        *,
        policies: Optional[list] = None,
        body: Optional[dict] = None,
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

    queryCombinedDeviceControlPolicyMembers = query_combined_policy_members
    queryCombinedDeviceControlPolicies = query_combined_policies
    getDefaultDeviceControlPolicies = get_default_policies
    updateDefaultDeviceControlPolicies = update_default_policies
    performDeviceControlPoliciesAction = perform_action
    patchDeviceControlPoliciesClassesV1 = update_policy_classes
    getDefaultDeviceControlSettings = get_default_settings
    updateDefaultDeviceControlSettings = update_default_settings
    setDeviceControlPoliciesPrecedence = set_precedence
    getDeviceControlPolicies = get_policies
    createDeviceControlPolicies = create_policies
    deleteDeviceControlPolicies = delete_policies
    getDeviceControlPoliciesV2 = get_policies_v2
    postDeviceControlPoliciesV2 = create_policies_v2
    patchDeviceControlPoliciesV2 = update_policies_v2
    updateDeviceControlPolicies = update_policies
    queryDeviceControlPolicyMembers = query_policy_members
    queryDeviceControlPolicies = query_policies
