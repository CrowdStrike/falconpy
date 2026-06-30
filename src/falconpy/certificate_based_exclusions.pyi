"""Type stubs for certificate_based_exclusions."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CertificateBasedExclusions(ServiceClass):

    def get_exclusions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_exclusions(
        self,
        *,
        exclusions: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_exclusions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_exclusions(
        self,
        *,
        exclusions: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_certificates(
        self,
        *,
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_certificates(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    cb_exclusions_get_v1 = get_exclusions
    cb_exclusions_create_v1 = create_exclusions
    cb_exclusions_delete_v1 = delete_exclusions
    cb_exclusions_update_v1 = update_exclusions
    certificates_get_v1 = get_certificates
    cb_exclusions_query_v1 = query_certificates
