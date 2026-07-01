"""Type stubs for hosts."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Hosts(ServiceClass):

    def query_hidden_devices_combined(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        fields: Optional[str] = None,
        parameters: Optional[dict] = None,
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

    def perform_group_action(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        action_name: Optional[str] = None,
        disable_hostname_check: Optional[bool] = None,
        action_parameters: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_device_tags(
        self,
        *,
        action: Optional[str] = None,
        device_ids: Optional[Union[str, List[str]]] = None,
        tags: Optional[Union[str, List[str]]] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_device_details_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_device_details_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_device_details(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_online_state(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_hidden_devices(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_devices_by_filter_scroll(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_devices_by_filter(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_devices_by_filter_combined(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        fields: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_device_login_history_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_device_login_history_v2(
        self,
        *args: Union[str, List[str]],
        limit: Optional[int] = None,
        to: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_network_address_history(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def devices_actions_delete_v1(
        self,
        *,
        action_parameters: Optional[list] = None,
        filter: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    CombinedHiddenDevicesByFilter = query_hidden_devices_combined
    DevicesActionsDeleteV1 = devices_actions_delete_v1
    PerformActionV2 = perform_action
    entities_perform_action = perform_group_action
    PerformGroupAction = perform_group_action
    UpdateDeviceTags = update_device_tags
    GetDeviceDetails = get_device_details
    GetDeviceDetailsV1 = get_device_details_v1
    GetDeviceDetailsV2 = get_device_details_v2
    PostDeviceDetailsV2 = get_device_details
    post_device_details_v2 = get_device_details
    QueryHiddenDevices = query_hidden_devices
    GetOnlineState_V1 = get_online_state
    get_online_state_v1 = get_online_state
    QueryDevicesByFilterScroll = query_devices_by_filter_scroll
    QueryDevicesByFilter = query_devices_by_filter
    QueryDevices = query_devices_by_filter_scroll
    query_devices = query_devices_by_filter_scroll
    QueryDeviceLoginHistory = query_device_login_history_v1
    CombinedDevicesByFilter = query_devices_by_filter_combined
    query_device_login_history = query_device_login_history_v1
    QueryDeviceLoginHistoryV2 = query_device_login_history_v2
    QueryGetNetworkAddressHistoryV1 = query_network_address_history
