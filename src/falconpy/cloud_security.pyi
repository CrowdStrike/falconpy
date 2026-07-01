"""Type stubs for cloud_security."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudSecurity(ServiceClass):

    def combined_cloud_risks(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_cloud_groups(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_cloud_groups_by_id(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_cloud_group(
        self,
        *,
        business_impact: Optional[str] = None,
        business_unit: Optional[str] = None,
        description: Optional[str] = None,
        environment: Optional[str] = None,
        name: Optional[str] = None,
        owners: Optional[Union[str, List[str]]] = None,
        selectors: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_cloud_group(
        self,
        *,
        business_impact: Optional[str] = None,
        business_unit: Optional[str] = None,
        description: Optional[str] = None,
        environment: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        owners: Optional[Union[str, List[str]]] = None,
        selectors: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_cloud_groups(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_group_ids(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ListCloudGroupsExternal = list_cloud_groups
    ListCloudGroupsByIDExternal = list_cloud_groups_by_id
    CreateCloudGroupExternal = create_cloud_group
    UpdateCloudGroupExternal = update_cloud_group
    DeleteCloudGroupsExternal = delete_cloud_groups
    ListCloudGroupIDsExternal = list_group_ids
