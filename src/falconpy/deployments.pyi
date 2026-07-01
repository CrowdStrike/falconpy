"""Type stubs for deployments."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Deployments(ServiceClass):

    def query_release_notes(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_deployments(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_releases(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_release_notes_v1(
        self,
        *,
        IDs: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_release_notes(
        self,
        *,
        IDs: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_release_note_ids(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    CombinedReleaseNotesV1 = query_release_notes
    GetDeploymentsExternalV1 = get_deployments
    CombinedReleasesV1Mixin0 = query_releases
    GetEntityIDsByQueryPOST = get_release_notes_v1
    GetEntityIDsByQueryPOSTV1 = get_release_notes_v1
    GetEntityIDsByQueryPOSTV2 = get_release_notes
    QueryReleaseNotesV1 = query_release_note_ids
