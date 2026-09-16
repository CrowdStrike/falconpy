"""Type stubs for skills."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Skills(ServiceClass):

    def download_studio_skill(
        self,
        *,
        id: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_studio_skills(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_studio_skill(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_studio_skill(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_studio_skill(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_studio_skills(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesSkillsDownloadV2 = download_studio_skill
    EntitiesSkillsV1 = get_studio_skills
    EntitiesSkillsUpdateV1 = update_studio_skill
    EntitiesSkillsCreateV1 = create_studio_skill
    EntitiesSkillsDeleteV1 = delete_studio_skill
    QueriesSkillsV1 = query_studio_skills
