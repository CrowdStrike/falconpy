"""Type stubs for cloud_snapshots."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudSnapshots(ServiceClass):

    def search_detections(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_scan_jobs(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scan_jobs(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def launch_scan_job(
        self,
        *,
        account_id: Optional[str] = None,
        asset_identifier: Optional[str] = None,
        cloud_provider: Optional[str] = None,
        region: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scan_reports(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_credentials(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_iac_credentials(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def register_account(
        self,
        *,
        aws_accounts: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    CombinedDetections = search_detections
    ReadDeploymentsCombined = search_scan_jobs
    ReadDeploymentsEntities = get_scan_jobs
    CreateDeploymentEntity = launch_scan_job
    GetScanReport = get_scan_reports
    GetCredentialsMixin0 = get_credentials
    GetCredentialsIAC = get_iac_credentials
    RegisterCspmSnapshotAccount = register_account
