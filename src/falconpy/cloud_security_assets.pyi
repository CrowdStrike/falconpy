"""Type stubs for cloud_security_assets."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudSecurityAssets(ServiceClass):

    def combined_application_findings(
        self,
        *,
        crn: Optional[str] = None,
        gcrn: Optional[str] = None,
        type: Optional[str] = None,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_combined_compliance_by_account(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        after: Optional[str] = None,
        include_failing_iom_severity_counts: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_assets(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_assets(
        self,
        *,
        after: Optional[str] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_security_assets_entities_post(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    cloud_security_assets_combined_application_findings = combined_application_findings
    cloud_security_assets_combined_compliance_by_account = get_combined_compliance_by_account
    cloud_security_assets_entities_get = get_assets
    cloud_security_assets_queries = query_assets
