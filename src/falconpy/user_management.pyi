"""Type stubs for user_management."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class UserManagement(ServiceClass):

    def aggregate_users(
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
        body: Optional[list] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_grants_v1(
        self,
        *args: Union[str, List[str]],
        user_uuid: Optional[str] = None,
        cid: Optional[str] = None,
        direct_only: Optional[bool] = None,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_grants(
        self,
        *args: Union[str, List[str]],
        user_uuid: Optional[str] = None,
        cid: Optional[str] = None,
        direct_only: Optional[bool] = None,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_roles_mssp(
        self,
        *args: Union[str, List[str]],
        cid: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_roles_mssp_v1(
        self,
        *args: Union[str, List[str]],
        cid: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def user_action(
        self,
        *,
        action: Optional[dict] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def user_roles_action(
        self,
        *,
        action: Optional[str] = None,
        cid: Optional[str] = None,
        expires_at: Optional[str] = None,
        role_ids: Optional[Union[str, List[str]]] = None,
        uuid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def retrieve_users(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_user_mssp(
        self,
        *,
        validate_only: Optional[bool] = None,
        cid: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        password: Optional[str] = None,
        uid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_user_mssp(
        self,
        *args: Union[str, List[str]],
        user_uuid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_user_mssp(
        self,
        *,
        user_uuid: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_roles(
        self,
        *args: Union[str, List[str]],
        cid: Optional[str] = None,
        user_uuid: Optional[str] = None,
        action: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_users(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_roles(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def grant_user_role_ids(
        self,
        *,
        user_uuid: Optional[str] = None,
        roleIds: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def revoke_user_role_ids(
        self,
        *,
        user_uuid: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_available_role_ids(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_role_ids(
        self,
        *args: Union[str, List[str]],
        user_uuid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def retrieve_user(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_user(
        self,
        *,
        firstName: Optional[str] = None,
        lastName: Optional[str] = None,
        password: Optional[str] = None,
        uid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_user(
        self,
        *args: Union[str, List[str]],
        user_uuid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_user(
        self,
        *,
        user_uuid: Optional[str] = None,
        firstName: Optional[str] = None,
        lastName: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def retrieve_emails_by_cid(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def retrieve_user_uuids_by_cid(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def retrieve_user_uuid(
        self,
        *args: Union[str, List[str]],
        uid: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    aggregateUsersV1 = aggregate_users
    combinedUserRolesV1 = get_user_grants_v1
    CombinedUserRolesV2 = get_user_grants
    get_user_roles = get_user_grants
    get_user_roles_combined = get_user_grants
    entitiesRolesGETV2 = get_roles_mssp
    entitiesRolesV1 = get_roles_mssp_v1
    userActionV1 = user_action
    userRolesActionV1 = user_roles_action
    retrieveUsersGETV1 = retrieve_users
    createUserV1 = create_user_mssp
    deleteUserV1 = delete_user_mssp
    updateUserV1 = update_user_mssp
    queryRolesV1 = query_roles
    queriesRolesV1 = query_roles
    queryUserV1 = query_users
    GetRoles = get_roles
    GrantUserRoleIds = grant_user_role_ids
    RevokeUserRoleIds = revoke_user_role_ids
    GetAvailableRoleIds = get_available_role_ids
    GetUserRoleIds = get_user_role_ids
    RetrieveUser = retrieve_user
    retrieveUser = retrieve_user
    CreateUser = create_user
    DeleteUser = delete_user
    UpdateUser = update_user
    RetrieveEmailsByCID = retrieve_emails_by_cid
    RetrieveUserUUIDsByCID = retrieve_user_uuids_by_cid
    RetrieveUserUUID = retrieve_user_uuid
