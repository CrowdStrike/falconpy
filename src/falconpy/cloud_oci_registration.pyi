"""Type stubs for cloud_oci_registration."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudOCIRegistration(ServiceClass):

    def get_account(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        next_token: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def rotate_key(
        self,
        *,
        tenancy_ocid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def validate_tenancy(
        self,
        *,
        products: Optional[list] = None,
        tenancy_ocid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_account(
        self,
        *,
        group_name: Optional[str] = None,
        home_region: Optional[str] = None,
        policy_name: Optional[str] = None,
        products: Optional[list] = None,
        registration_description: Optional[str] = None,
        registration_name: Optional[str] = None,
        tenancy_ocid: Optional[str] = None,
        user_email: Optional[str] = None,
        user_name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_account(
        self,
        *,
        group_name: Optional[str] = None,
        home_region: Optional[str] = None,
        policy_name: Optional[str] = None,
        products: Optional[list] = None,
        registration_description: Optional[str] = None,
        registration_name: Optional[str] = None,
        stack_ocid: Optional[str] = None,
        tenancy_ocid: Optional[str] = None,
        user_email: Optional[str] = None,
        user_name: Optional[str] = None,
        user_ocid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_account(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def download_script(
        self,
        *,
        deployment_method: Optional[str] = None,
        is_download: Optional[bool] = None,
        tenancy_ocid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    cloud_security_registration_oci_get_account = get_account
    cloud_security_registration_oci_rotate_key = rotate_key
    cloud_security_registration_oci_validate_tenancy = validate_tenancy
    cloud_security_registration_oci_create_account = create_account
    cloud_security_registration_oci_update_account = update_account
    cloud_security_registration_oci_delete_account = delete_account
    cloud_security_registration_oci_download_script = download_script
