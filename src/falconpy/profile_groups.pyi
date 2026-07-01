"""Type stubs for profile_groups."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ProfileGroups(ServiceClass):

    def group_actions_v1_mixin0(
        self,
        *,
        action_name: Optional[str] = None,
        action_parameters: Optional[list] = None,
        filter: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def group_users_actions_v1_mixin0(
        self,
        *,
        action_name: Optional[str] = None,
        action_parameters: Optional[list] = None,
        filter: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_group_users_v1(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_groups_v1_mixin0(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_group_v1_mixin0(
        self,
        *,
        cid: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_groups_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_group_v1_mixin0(
        self,
        *,
        id: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_groups_v1(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_groups_v1_mixin0(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GroupActionsV1Mixin0 = group_actions_v1_mixin0
    GroupUsersActionsV1Mixin0 = group_users_actions_v1_mixin0
    GetGroupUsersV1 = get_group_users_v1
    GetGroupsV1Mixin0 = get_groups_v1_mixin0
    CreateGroupV1Mixin0 = create_group_v1_mixin0
    DeleteGroupsV1 = delete_groups_v1
    UpdateGroupV1Mixin0 = update_group_v1_mixin0
    GetUserGroupsV1 = get_user_groups_v1
    QueryGroupsV1Mixin0 = query_groups_v1_mixin0
