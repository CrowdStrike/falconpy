"""Type stubs for response_policies."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ResponsePolicies(ServiceClass):

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
        clone_id: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        platform_name: Optional[str] = None,
        settings: Optional[list] = None,
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
        settings: Optional[list] = None,
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

    queryCombinedRTResponsePolicyMembers = query_combined_policy_members
    queryCombinedRTResponsePolicies = query_combined_policies
    performRTResponsePoliciesAction = perform_policies_action
    setRTResponsePoliciesPrecedence = set_policies_precedence
    getRTResponsePolicies = get_policies
    createRTResponsePolicies = create_policies
    deleteRTResponsePolicies = delete_policies
    updateRTResponsePolicies = update_policies
    queryRTResponsePolicyMembers = query_policy_members
    queryRTResponsePolicies = query_policies
