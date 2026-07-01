"""Type stubs for image_assessment_policies."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ImageAssessmentPolicies(ServiceClass):

    def read_policies(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_policies(
        self,
        *,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policies(
        self,
        *,
        id: Optional[str] = None,
        description: Optional[str] = None,
        is_enabled: Optional[bool] = None,
        name: Optional[str] = None,
        policy_data: Optional[dict] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_policy(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_policy_exclusions(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_exclusions(
        self,
        *,
        conditions: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_policy_groups(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_policy_groups(
        self,
        *,
        description: Optional[str] = None,
        name: Optional[str] = None,
        policy_group_data: Optional[dict] = None,
        policy_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_groups(
        self,
        *,
        id: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        policy_group_data: Optional[dict] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_policy_group(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_precedence(
        self,
        *,
        precedence: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ReadPolicies = read_policies
    CreatePolicies = create_policies
    UpdatePolicies = update_policies
    DeletePolicy = delete_policy
    ReadPolicyExclusions = read_policy_exclusions
    UpdatePolicyExclusions = update_policy_exclusions
    ReadPolicyGroups = read_policy_groups
    CreatePolicyGroups = create_policy_groups
    UpdatePolicyGroups = update_policy_groups
    DeletePolicyGroup = delete_policy_group
    UpdatePolicyPrecedence = update_policy_precedence
