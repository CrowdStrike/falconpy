"""Type stubs for mssp."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FlightControl(ServiceClass):

    def get_children(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_children_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cid_group_members_by_v1(
        self,
        *args: Union[str, List[str]],
        cid_group_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cid_group_members_by(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_cid_group_members(
        self,
        *,
        cid_group_id: Optional[str] = None,
        cids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_cid_group_members_v1(
        self,
        *,
        cid_group_id: Optional[str] = None,
        cids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_cid_group_members(
        self,
        *,
        cid_group_id: Optional[str] = None,
        cids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cid_group_by_id_v1(
        self,
        *args: Union[str, List[str]],
        cid_group_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cid_group_by_id(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_cid_groups(
        self,
        *,
        cid: Optional[str] = None,
        cid_group_id: Optional[str] = None,
        description: Optional[str] = None,
        is_default: Optional[bool] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_cid_groups(
        self,
        *args: Union[str, List[str]],
        cid_group_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_cid_groups(
        self,
        *,
        cid: Optional[str] = None,
        cid_group_id: Optional[str] = None,
        description: Optional[str] = None,
        is_default: Optional[bool] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_roles_by_id(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_role(
        self,
        *,
        cid_group_id: Optional[str] = None,
        id: Optional[str] = None,
        role_ids: Optional[Union[str, List[str]]] = None,
        user_group_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_roles(
        self,
        *,
        cid_group_id: Optional[str] = None,
        id: Optional[str] = None,
        role_ids: Optional[Union[str, List[str]]] = None,
        user_group_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_group_members_by_id_v1(
        self,
        *args: Union[str, List[str]],
        user_group_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_group_members_by_id(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_user_group_members(
        self,
        *,
        user_group_id: Optional[str] = None,
        user_uuids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_user_group_members(
        self,
        *,
        user_group_id: Optional[str] = None,
        user_uuids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_groups_by_id_v1(
        self,
        *args: Union[str, List[str]],
        user_group_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_groups_by_id(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_user_groups(
        self,
        *,
        cid: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        user_group_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_user_groups(
        self,
        *args: Union[str, List[str]],
        user_group_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_user_groups(
        self,
        *,
        cid: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        user_group_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_children(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_cid_group_members(
        self,
        *,
        cid: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_cid_groups(
        self,
        *,
        name: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_roles(
        self,
        *,
        user_group_id: Optional[str] = None,
        cid_group_id: Optional[str] = None,
        role_id: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_user_group_members(
        self,
        *,
        user_uuid: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_user_groups(
        self,
        *,
        name: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    getChildren = get_children
    getCIDGroupMembersBy = get_cid_group_members_by
    getCIDGroupMembersByV1 = get_cid_group_members_by_v1
    getCIDGroupMembersByV2 = get_cid_group_members_by
    addCIDGroupMembers = add_cid_group_members
    deleteCIDGroupMembers = delete_cid_group_members
    deleteCIDGroupMembersV1 = delete_cid_group_members_v1
    deleteCIDGroupMembersV2 = delete_cid_group_members
    getCIDGroupById = get_cid_group_by_id
    getCIDGroupByIdV1 = get_cid_group_by_id_v1
    getCIDGroupByIdV2 = get_cid_group_by_id
    createCIDGroups = create_cid_groups
    deleteCIDGroups = delete_cid_groups
    updateCIDGroups = update_cid_groups
    getRolesByID = get_roles_by_id
    addRole = add_role
    deletedRoles = delete_roles
    deleteRoles = delete_roles
    getUserGroupMembersByID = get_user_group_members_by_id
    getUserGroupMembersByIDV1 = get_user_group_members_by_id_v1
    getUserGroupMembersByIDV2 = get_user_group_members_by_id
    addUserGroupMembers = add_user_group_members
    deleteUserGroupMembers = delete_user_group_members
    getUserGroupsByID = get_user_groups_by_id
    getUserGroupsByIDV1 = get_user_groups_by_id_v1
    getUserGroupsByIDV2 = get_user_groups_by_id
    createUserGroup = create_user_groups
    createUserGroups = create_user_groups
    deleteUserGroups = delete_user_groups
    updateUserGroups = update_user_groups
    queryChildren = query_children
    queryCIDGroupMembers = query_cid_group_members
    queryCIDGroups = query_cid_groups
    queryRoles = query_roles
    queryUserGroupMembers = query_user_group_members
    queryUserGroups = query_user_groups
