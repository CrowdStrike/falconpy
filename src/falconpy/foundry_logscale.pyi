"""Type stubs for foundry_logscale."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FoundryLogScale(ServiceClass):

    def list_repos(
        self,
        *args: Union[str, List[str]],
        check_test_data: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def ingest_data(
        self,
        *,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def ingest_data_async(
        self,
        *,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_file(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_file(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_dynamic(
        self,
        *,
        app_id: Optional[str] = None,
        include_schema_generation: Optional[bool] = None,
        include_test_data: Optional[bool] = None,
        infer_json_types: Optional[bool] = None,
        match_response_schema: Optional[bool] = None,
        metadata: Optional[bool] = None,
        mode: Optional[str] = None,
        end: Optional[str] = None,
        repo_or_view: Optional[str] = None,
        search_query: Optional[str] = None,
        search_query_args: Optional[dict] = None,
        start: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_search_results(
        self,
        *,
        job_id: Optional[str] = None,
        app_id: Optional[str] = None,
        infer_json_types: Optional[bool] = None,
        job_status_only: Optional[bool] = None,
        limit: Optional[str] = None,
        match_response_schema: Optional[bool] = None,
        metadata: Optional[bool] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute(
        self,
        *,
        app_id: Optional[str] = None,
        detailed: Optional[bool] = None,
        include_test_data: Optional[bool] = None,
        infer_json_types: Optional[bool] = None,
        match_response_schema: Optional[bool] = None,
        metadata: Optional[bool] = None,
        end: Optional[str] = None,
        id: Optional[str] = None,
        mode: Optional[str] = None,
        name: Optional[str] = None,
        parameters: Optional[dict] = None,
        start: Optional[str] = None,
        version: Optional[str] = None,
        with_in: Optional[dict] = None,
        with_limit: Optional[dict] = None,
        with_renames: Optional[list] = None,
        with_sort: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def populate(
        self,
        *args: Union[str, List[str]],
        app_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def download_results(
        self,
        *,
        job_id: Optional[str] = None,
        infer_json_types: Optional[bool] = None,
        result_format: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_views(
        self,
        *args: Union[str, List[str]],
        check_test_data: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ListReposV1 = list_repos
    ListViewV1 = list_views
    IngestDataV1 = ingest_data
    IngestDataAsyncV1 = ingest_data_async
    CreateFileV1 = create_file
    UpdateFileV1 = update_file
    CreateSavedSearchesDynamicExecuteV1 = execute_dynamic
    GetSavedSearchesExecuteV1 = get_search_results
    CreateSavedSearchesExecuteV1 = execute
    CreateSavedSearchesIngestV1 = populate
    GetSavedSearchesJobResultsDownloadV1 = download_results
