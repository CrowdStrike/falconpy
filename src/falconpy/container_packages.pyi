"""Type stubs for container_packages."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ContainerPackages(ServiceClass):

    def read_packages_by_image_count(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_zero_day_counts(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_fixable_vuln_count(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_vuln_count(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_combined_export(
        self,
        *,
        filter: Optional[str] = None,
        only_zero_day_affected: Optional[bool] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_combined(
        self,
        *,
        filter: Optional[str] = None,
        only_zero_day_affected: Optional[bool] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_packages(
        self,
        *,
        filter: Optional[str] = None,
        only_zero_day_affected: Optional[bool] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ReadPackagesByImageCount = read_packages_by_image_count
    ReadPackagesCountByZeroDay = read_zero_day_counts
    ReadPackagesByFixableVulnCount = read_fixable_vuln_count
    ReadPackagesByVulnCount = read_vuln_count
    ReadPackagesCombinedExport = read_combined_export
    ReadPackagesCombined = read_combined
    ReadPackagesCombinedV2 = read_packages
