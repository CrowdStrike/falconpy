"""Type stubs for firewall_policies."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FirewallPolicies(ServiceClass):

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

    def perform_action(
        self,
        *,
        action_name: Optional[str] = None,
        action_parameters: Optional[list] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def set_policies(
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
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
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

    queryCombinedFirewallPolicyMembers = query_combined_policy_members
    queryCombinedFirewallPolicies = query_combined_policies
    performFirewallPoliciesAction = perform_action
    perform_policies_action = perform_action
    setFirewallPoliciesPrecedence = set_policies
    set_policies_precedence = set_policies
    getFirewallPolicies = get_policies
    createFirewallPolicies = create_policies
    deleteFirewallPolicies = delete_policies
    updateFirewallPolicies = update_policies
    queryFirewallPolicyMembers = query_policy_members
    queryFirewallPolicies = query_policies
