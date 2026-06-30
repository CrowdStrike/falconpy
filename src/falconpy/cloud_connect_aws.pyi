"""Type stubs for cloud_connect_aws."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudConnectAWS(ServiceClass):

    def query_aws_accounts(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aws_settings(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aws_accounts(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def provision_aws_accounts(
        self,
        *,
        mode: Optional[str] = None,
        cloudtrail_bucket_owner_id: Optional[str] = None,
        cloudtrail_bucket_region: Optional[str] = None,
        external_id: Optional[str] = None,
        iam_role_arn: Optional[str] = None,
        id: Optional[str] = None,
        rate_limit_reqs: Optional[int] = None,
        rate_limit_time: Optional[int] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_aws_accounts(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_aws_accounts(
        self,
        *,
        cloudtrail_bucket_owner_id: Optional[str] = None,
        cloudtrail_bucket_region: Optional[str] = None,
        external_id: Optional[str] = None,
        iam_role_arn: Optional[str] = None,
        id: Optional[str] = None,
        rate_limit_reqs: Optional[int] = None,
        rate_limit_time: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_or_update_aws_settings(
        self,
        *,
        cloudtrail_bucket_owner_id: Optional[str] = None,
        static_external_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def verify_aws_account_access(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aws_accounts_for_ids(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    QueryAWSAccounts = query_aws_accounts
    GetAWSSettings = get_aws_settings
    GetAWSAccounts = get_aws_accounts
    ProvisionAWSAccounts = provision_aws_accounts
    DeleteAWSAccounts = delete_aws_accounts
    UpdateAWSAccounts = update_aws_accounts
    CreateOrUpdateAWSSettings = create_or_update_aws_settings
    VerifyAWSAccountAccess = verify_aws_account_access
    QueryAWSAccountsForIDs = query_aws_accounts_for_ids
