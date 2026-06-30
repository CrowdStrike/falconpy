"""Type stubs for container_vulnerabilities."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ContainerVulnerabilities(ServiceClass):

    def read_vulnerability_counts_by_active_exploited(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_vulnerability_counts_by_cps_rating(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_vulnerability_counts_by_cvss_score(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_vulnerability_counts_by_severity(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_vulnerability_count(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_vulnerabilities_by_count(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_vulnerabilities_by_pub_date(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_combined_vulnerability_detail(
        self,
        *,
        id: Optional[str] = None,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_combined_vulnerabilities_info(
        self,
        *,
        cve_id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_combined_vulnerabilities(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ReadCombinedVulnerabilities = read_combined_vulnerabilities
    ReadCombinedVulnerabilitiesInfo = read_combined_vulnerabilities_info
    ReadCombinedVulnerabilitiesDetails = read_combined_vulnerability_detail
    ReadVulnerabilitiesPublicationDate = read_vulnerabilities_by_pub_date
    ReadVulnerabilitiesByImageCount = read_vulnerabilities_by_count
    ReadVulnerabilityCount = read_vulnerability_count
    ReadVulnerabilityCountBySeverity = read_vulnerability_counts_by_severity
    ReadVulnerabilityCountByCPSRating = read_vulnerability_counts_by_cps_rating
    ReadVulnerabilityCountByCVSSScore = read_vulnerability_counts_by_cvss_score
    ReadVulnerabilityCountByActivelyExploited = read_vulnerability_counts_by_active_exploited
    read_vulnerability_counts_by_actively_exploited = read_vulnerability_counts_by_active_exploited
