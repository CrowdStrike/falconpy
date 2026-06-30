"""Type stubs for falcon_container."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FalconContainer(ServiceClass):

    def download_export_file(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_export_jobs(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def launch_export_job(
        self,
        *,
        expand_vulnerabilities: Optional[bool] = None,
        format: Optional[str] = None,
        fql: Optional[str] = None,
        resource: Optional[str] = None,
        sort: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_credentials(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_image_vulnerabilities(
        self,
        *,
        applicationPackages: Optional[list] = None,
        osversion: Optional[str] = None,
        packages: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_assessment(
        self,
        *,
        digest: Optional[str] = None,
        image_id: Optional[str] = None,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_image_details(
        self,
        *args: Union[str, List[str]],
        image_id: Optional[str] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def image_matches_policy(
        self,
        *,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_registry_entities(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_registry_entities_by_uuid(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_registry_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_export_jobs(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_registry_entities(
        self,
        *,
        credential: Optional[dict] = None,
        type: Optional[str] = None,
        url: Optional[str] = None,
        url_uniqueness_key: Optional[str] = None,
        user_defined_alias: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_registry_entities(
        self,
        *,
        id: Optional[str] = None,
        credential: Optional[dict] = None,
        state: Optional[str] = None,
        user_defined_alias: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def scan_inventory(
        self,
        *,
        agent_uuid: Optional[str] = None,
        agent_version: Optional[str] = None,
        agent_version_hash: Optional[str] = None,
        cluster_id: Optional[str] = None,
        cluster_name: Optional[str] = None,
        container_id: Optional[str] = None,
        ephemeral_scan: Optional[bool] = None,
        helm_version: Optional[str] = None,
        high_entropy_strings: Optional[list] = None,
        host_ip: Optional[str] = None,
        host_name: Optional[str] = None,
        inventory: Optional[dict] = None,
        original_image_name: Optional[str] = None,
        pod_id: Optional[str] = None,
        pod_name: Optional[str] = None,
        pod_namespace: Optional[str] = None,
        runmode: Optional[str] = None,
        runtime_type: Optional[str] = None,
        scan_request: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scan_headers(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def check_prevention_policies(
        self,
        *,
        registry: Optional[str] = None,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        architecture: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_report_by_reference(
        self,
        *,
        registry: Optional[str] = None,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        image_id: Optional[str] = None,
        digest: Optional[str] = None,
        architecture: Optional[str] = None,
        report_format: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_report_by_id(
        self,
        *,
        uuid: Optional[str] = None,
        report_format: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    DownloadExportFile = download_export_file
    ReadExportJobs = read_export_jobs
    LaunchExportJob = launch_export_job
    GetCredentials = get_credentials
    GetImageAssessmentReport = get_assessment
    DeleteImageDetails = delete_image_details
    ImageMatchesPolicy = image_matches_policy
    ReadImageVulnerabilities = read_image_vulnerabilities
    ReadRegistryEntities = read_registry_entities
    ReadRegistryEntitiesByUUID = read_registry_entities_by_uuid
    DeleteRegistryEntities = delete_registry_entities
    QueryExportJobs = query_export_jobs
    CreateRegistryEntities = create_registry_entities
    UpdateRegistryEntities = update_registry_entities
    PostImageScanInventory = scan_inventory
    HeadImageScanInventory = get_scan_headers
    PolicyChecks = check_prevention_policies
    GetReportByReference = get_report_by_reference
    GetReportByScanID = get_report_by_id
