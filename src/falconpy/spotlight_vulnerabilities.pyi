"""Type stubs for spotlight_vulnerabilities."""
from typing import Dict, List, Optional, Union
from typing_extensions import deprecated
from ._service_class import ServiceClass
from ._result import Result


class SpotlightVulnerabilities(ServiceClass):

    def query_vulnerabilities_combined(
        self,
        *,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        facet: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This operation is no longer available in CrowdStrike's API. Calling this method will result in an error from the API.")
    def query_installed_patches_combined(
        self,
        *,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_vulnerabilities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_vulnerabilities(
        self,
        *,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_remediations(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_remediations_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    getVulnerabilities = get_vulnerabilities
    queryVulnerabilities = query_vulnerabilities
    combinedQueryVulnerabilities = query_vulnerabilities_combined
    combinedQueryInstalledPatches = query_installed_patches_combined
    getRemediations = get_remediations
    getRemediationsV2 = get_remediations_v2
