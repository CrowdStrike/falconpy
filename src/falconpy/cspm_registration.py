"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

cspm_registration - Falcon Horizon for AWS API Interface Class

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


class CSPM_Registration(ServiceClass):
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def GetCSPMAwsAccount(self: object, ids, org_ids=None, parameters: dict = None) -> dict:
        """Returns information about the current status of an AWS account. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsAccount
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+"/cloud-connect-cspm-aws/entities/account/v1?ids={}".format(ID_LIST)
        if org_ids:
            ORG_ID_LIST = str(parse_id_list(org_ids)).replace(",", "&organization-ids=")
            FULL_URL = FULL_URL + "&organization-id={}".format(ORG_ID_LIST)
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )

        return returned

    def CreateCSPMAwsAccount(self: object, body: dict) -> dict:
        """Creates a new account in our system for a customer and generates a script
           to run in their AWS cloud environment to grant CrowdStrike Horizon access.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMAwsAccount
        FULL_URL = self.base_url+"/cloud-connect-cspm-aws/entities/account/v1"
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

    def DeleteCSPMAwsAccount(self: object, ids=None, org_ids=None) -> dict:
        """Delete an existing AWS Account or Organization by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMAwsAccount
        ep_base = "/cloud-connect-cspm-aws/entities/account/v1"
        if ids:
            ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
            FULL_URL = self.base_url+'{}?ids={}'.format(ep_base, ID_LIST)
        else:
            FULL_URL = self.base_url+ep_base
        if org_ids:
            ORG_ID_LIST = str(parse_id_list(org_ids)).replace(",", "&organization-ids=")
            if "?" in FULL_URL:
                stem = "&organization-ids="
            else:
                stem = "?organization-ids="
            FULL_URL = FULL_URL + stem + '{}'.format(ORG_ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self, method="DELETE", endpoint=FULL_URL, headers=HEADERS, verify=self.ssl_verify)

        return returned

    def GetCSPMAwsConsoleSetupURLs(self: object) -> dict:
        """Returns a URL for customers to visit in their cloud environment to grant access to CrowdStrike"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsConsoleSetupURLs
        FULL_URL = self.base_url+"/cloud-connect-cspm-aws/entities/console-setup-urls/v1"
        HEADERS = self.headers
        returned = service_request(caller=self, method="GET", endpoint=FULL_URL, headers=HEADERS, verify=self.ssl_verify)

        return returned

    def GetCSPMAwsAccountScriptsAttachment(self: object) -> bytes:
        """Return a script for customers to run in their cloud environment
           to grant access to CrowdStrike for their AWS environment.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /cspm-registration/GetCSPMAwsAccountScriptsAttachment
        FULL_URL = self.base_url+"/cloud-connect-cspm-aws/entities/user-scripts-download/v1"
        HEADERS = self.headers
        returned = service_request(caller=self, method="GET", endpoint=FULL_URL, headers=HEADERS, verify=self.ssl_verify)

        return returned

    def GetCSPMAzureAccount(self: object, ids, parameters: dict = None) -> dict:
        """Return information about Azure account registration."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAzureAccount2
        # This shows up as GetCSPMAzureAccount2 in the Uber class.
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+"/cloud-connect-cspm-azure/entities/account/v1?ids={}".format(ID_LIST)
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )

        return returned

    def CreateCSPMAzureAccount(self: object, body: dict) -> dict:
        """Creates a new account in our system for a customer and generates a script
           to run in their cloud environment to grant CrowdStrike Horizon access.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMAzureAccount2
        # This shows up as CreateCSPMAzureAccount2 in the Uber class
        FULL_URL = self.base_url+"/cloud-connect-cspm-azure/entities/account/v1"
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

    def DeleteCSPMAzureAccount(self: object, ids) -> dict:
        """Delete an existing Azure Subscription by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMAzureAccount
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+"/cloud-connect-cspm-azure/entities/account/v1?ids={}".format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self, method="DELETE", endpoint=FULL_URL, headers=HEADERS, verify=self.ssl_verify)

        return returned

    # TODO: Confirm payload formats for IDs not passed via an array
    def UpdateCSPMAzureAccountClientID(self: object, body: dict = None, parameters: dict = None) -> dict:
        """Update an Azure service account in our system with the
           user-created client_id created with the public key we've provided.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /cspm-registration/UpdateCSPMAzureAccountClientID2
        # This shows up as UpdateCSPMAzureAccountClientID2 in the Uber class
        FULL_URL = self.base_url+'/cloud-connect-cspm-azure/entities/client-id/v1'
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        HEADERS = self.headers
        if body is None:
            body = {}
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetCSPMAzureUserScriptsAttachment(self: object, parameters: dict = None) -> bytes:
        """Return a script for customers to run in their cloud environment
           to grant access to CrowdStrike for their Azure environment.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /cspm-registration/GetCSPMAzureUserScriptsAttachment2
        FULL_URL = self.base_url+"/cloud-connect-cspm-azure/entities/user-scripts-download/v1"
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )

        return returned

    def GetCSPMPolicy(self: object, ids) -> dict:
        """Given a policy ID, returns detailed policy information."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMPolicy
        FULL_URL = self.base_url+"/settings/entities/policy-details/v1"
        if ids:
            ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
            FULL_URL = FULL_URL + "&ids={}".format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )

        return returned

    def GetCSPMPolicySettings(self: object, parameters: dict = None) -> dict:
        """Returns information about current policy settings."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMPolicySettings
        FULL_URL = self.base_url+"/settings/entities/policy/v1"
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )

        return returned

    def UpdateCSPMPolicySettings(self: object, body: dict) -> dict:
        """Updates a policy setting - can be used to override policy severity or to disable a policy entirely."""
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /cspm-registration/UpdateCSPMPolicySettings
        FULL_URL = self.base_url+'/settings/entities/policy/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetCSPMScanSchedule(self: object, parameters: dict = None) -> dict:
        """Returns scan schedule configuration for one or more cloud platforms."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMScanSchedule
        FULL_URL = self.base_url+"/settings/scan-schedule/v1"
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )

        return returned

    def UpdateCSPMScanSchedule(self: object, body: dict) -> dict:
        """Updates scan schedule configuration for one or more cloud platforms."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMScanSchedule
        FULL_URL = self.base_url+"/settings/scan-schedule/v1"
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
