"""Type stubs for malquery."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class MalQuery(ServiceClass):

    def get_quotas(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def fuzzy_search(
        self,
        *,
        options: Optional[dict] = None,
        patterns: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_download(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_metadata(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_request(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_samples(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def samples_multidownload(
        self,
        *args: Union[str, List[str]],
        samples: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def exact_search(
        self,
        *,
        options: Optional[dict] = None,
        patterns: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def hunt(
        self,
        *,
        options: Optional[dict] = None,
        yara_rule: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetMalQueryQuotasV1 = get_quotas
    PostMalQueryFuzzySearchV1 = fuzzy_search
    GetMalQueryDownloadV1 = get_download
    GetMalQueryMetadataV1 = get_metadata
    GetMalQueryRequestV1 = get_request
    GetMalQueryEntitiesSamplesFetchV1 = get_samples
    PostMalQueryEntitiesSamplesMultidownloadV1 = samples_multidownload
    PostMalQueryExactSearchV1 = exact_search
    PostMalQueryHuntV1 = hunt
