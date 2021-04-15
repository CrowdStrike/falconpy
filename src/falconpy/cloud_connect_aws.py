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
from ._util import service_request, parse_id_list
from ._service_class import ServiceClass


class Cloud_Connect_AWS(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def QueryAWSAccounts(self: object, parameters: dict = None) -> dict:
        """ Search for provisioned AWS Accounts by providing an FQL filter and paging details.
            Returns a set of AWS accounts which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/QueryAWSAccounts
        FULL_URL = self.base_url+'/cloud-connect-aws/combined/accounts/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        VALIDATOR = {
            "limit": int,
            "offset": int,
            "sort": str,
            "filter": str
        }
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   verify=self.ssl_verify,
                                   params_validator=VALIDATOR
                                   )
        return returned

    def GetAWSSettings(self: object) -> dict:
        """ Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/GetAWSSettings
        FULL_URL = self.base_url+'/cloud-connect-aws/combined/settings/v1'
        HEADERS = self.headers
        returned = service_request(caller=self, method="GET", endpoint=FULL_URL, headers=HEADERS, verify=self.ssl_verify)

        return returned

    def GetAWSAccounts(self: object, ids) -> dict:
        """ Retrieve a set of AWS Accounts by specifying their IDs."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/GetAWSAccounts
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/accounts/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self, method="GET", endpoint=FULL_URL, headers=HEADERS, verify=self.ssl_verify)

        return returned

    def ProvisionAWSAccounts(self: object, body: dict, parameters: dict = None) -> dict:
        """ Provision AWS Accounts by specifying details about the accounts to provision. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/ProvisionAWSAccounts
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/accounts/v1'
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        BODY = body
        HEADERS = self.headers
        VALIDATOR = {"resources": list}
        REQUIRED = ["resources"]
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   body=BODY,
                                   body_validator=VALIDATOR,
                                   body_required=REQUIRED,
                                   verify=self.ssl_verify
                                   )
        return returned

    def DeleteAWSAccounts(self: object, ids) -> dict:
        """ Delete a set of AWS Accounts by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/DeleteAWSAccounts
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/accounts/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self, method="DELETE", endpoint=FULL_URL, headers=HEADERS, verify=self.ssl_verify)

        return returned

    def UpdateAWSAccounts(self: object, body: dict) -> dict:
        """ Update AWS Accounts by specifying the ID of the account and details to update. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/UpdateAWSAccounts
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/accounts/v1'
        BODY = body
        HEADERS = self.headers
        VALIDATOR = {"resources": list}
        REQUIRED = ["resources"]
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   body_validator=VALIDATOR,
                                   body_required=REQUIRED,
                                   verify=self.ssl_verify
                                   )
        return returned

    def CreateOrUpdateAWSSettings(self: object, body: dict) -> dict:
        """ Create or update Global Settings which are applicable to all provisioned AWS accounts. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/CreateOrUpdateAWSSettings
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/settings/v1'
        HEADERS = self.headers
        BODY = body
        VALIDATOR = {"resources": list}
        REQUIRED = ["resources"]
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   body_validator=VALIDATOR,
                                   body_required=REQUIRED,
                                   verify=self.ssl_verify
                                   )
        return returned

    def VerifyAWSAccountAccess(self: object, ids, body: dict = None) -> dict:
        """ Performs an Access Verification check on the specified AWS Account IDs. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/VerifyAWSAccountAccess
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/cloud-connect-aws/entities/verify-account-access/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        if body is None:
            body = {}
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def QueryAWSAccountsForIDs(self: object, parameters: dict = None) -> dict:
        """ Search for provisioned AWS Accounts by providing an FQL filter and paging details.
            Returns a set of AWS account IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws/QueryAWSAccountsForIDs
        FULL_URL = self.base_url+'/cloud-connect-aws/queries/accounts/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        VALIDATOR = {
            "limit": int,
            "offset": int,
            "sort": str,
            "filter": str
        }
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   params_validator=VALIDATOR,
                                   verify=self.ssl_verify
                                   )
        return returned
