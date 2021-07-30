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
# pylint: disable=C0103  # Aligning method names to API operation IDs
from ._util import service_request, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._cloud_connect_aws import _cloud_connect_aws_endpoints as Endpoints


class Cloud_Connect_AWS(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryAWSAccounts(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for provisioned AWS Accounts by providing an FQL filter and paging details.
        Returns a set of AWS accounts which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/QueryAWSAccounts
        operation_id = "QueryAWSAccounts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )

        return returned

    def GetAWSSettings(self: object) -> dict:
        """
        Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/GetAWSSettings
        operation_id = "GetAWSSettings"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetAWSAccounts(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of AWS Accounts by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/GetAWSAccounts
        operation_id = "GetAWSAccounts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def ProvisionAWSAccounts(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Provision AWS Accounts by specifying details about the accounts to provision.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/ProvisionAWSAccounts
        operation_id = "ProvisionAWSAccounts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def DeleteAWSAccounts(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a set of AWS Accounts by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/DeleteAWSAccounts
        operation_id = "DeleteAWSAccounts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )

        return returned

    def UpdateAWSAccounts(self: object, body: dict) -> dict:
        """
        Update AWS Accounts by specifying the ID of the account and details to update.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/UpdateAWSAccounts
        operation_id = "UpdateAWSAccounts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def CreateOrUpdateAWSSettings(self: object, body: dict) -> dict:
        """
        Create or update Global Settings which are applicable to all provisioned AWS accounts.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/CreateOrUpdateAWSSettings
        operation_id = "CreateOrUpdateAWSSettings"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters", "body"], default_types=["dict"])
    def VerifyAWSAccountAccess(self: object, parameters: dict = None, body: dict = None, **kwargs) -> dict:
        """
        Performs an Access Verification check on the specified AWS Account IDs.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/VerifyAWSAccountAccess
        operation_id = "VerifyAWSAccountAccess"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        body_payload = body
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryAWSAccountsForIDs(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for provisioned AWS Accounts by providing an FQL filter and paging details.
        Returns a set of AWS account IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/QueryAWSAccountsForIDs
        operation_id = "QueryAWSAccountsForIDs"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )

        return returned
