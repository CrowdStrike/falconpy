"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

cloud_connect_aws - Falcon Discover for AWS API Interface Class

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
from ._util import force_default, process_service_request, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._cloud_connect_aws import _cloud_connect_aws_endpoints as Endpoints


class CloudConnectAWS(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aws_accounts(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for provisioned AWS Accounts by providing an FQL filter and paging details.
        Returns a set of AWS accounts which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/QueryAWSAccounts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryAWSAccounts",
            keywords=kwargs,
            params=parameters
            )

    def get_aws_settings(self: object) -> dict:
        """
        Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/GetAWSSettings
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAWSSettings"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of AWS Accounts by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/GetAWSAccounts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAWSAccounts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def provision_aws_accounts(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Provision AWS Accounts by specifying details about the accounts to provision.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/ProvisionAWSAccounts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ProvisionAWSAccounts",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a set of AWS Accounts by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/DeleteAWSAccounts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteAWSAccounts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def update_aws_accounts(self: object, body: dict) -> dict:
        """
        Update AWS Accounts by specifying the ID of the account and details to update.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/UpdateAWSAccounts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateAWSAccounts",
            body=body
            )

    def create_or_update_aws_settings(self: object, body: dict) -> dict:
        """
        Create or update Global Settings which are applicable to all provisioned AWS accounts.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/CreateOrUpdateAWSSettings
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateOrUpdateAWSSettings",
            body=body
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict"])
    def verify_aws_account_access(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Performs an Access Verification check on the specified AWS Account IDs.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/VerifyAWSAccountAccess
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="VerifyAWSAccountAccess",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aws_accounts_for_ids(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for provisioned AWS Accounts by providing an FQL filter and paging details.
        Returns a set of AWS account IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/QueryAWSAccountsForIDs
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryAWSAccountsForIDs",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    QueryAWSAccounts = query_aws_accounts
    GetAWSSettings = get_aws_settings
    GetAWSAccounts = get_aws_accounts
    ProvisionAWSAccounts = provision_aws_accounts
    DeleteAWSAccounts = delete_aws_accounts
    UpdateAWSAccounts = update_aws_accounts
    CreateOrUpdateAWSSettings = create_or_update_aws_settings
    VerifyAWSAccountAccess = verify_aws_account_access
    QueryAWSAccountsForIDs = query_aws_accounts_for_ids


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Cloud_Connect_AWS = CloudConnectAWS  # pylint: disable=C0103
