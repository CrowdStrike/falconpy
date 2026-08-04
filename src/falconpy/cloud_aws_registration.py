"""CrowdStrike Falcon CloudAWSRegistration API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

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
from typing import Dict, Union
from ._util import force_default, process_service_request
from ._payload import cloud_aws_registration_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._cloud_aws_registration import _cloud_aws_registration_endpoints as Endpoints


class CloudAWSRegistration(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def trigger_health_check(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Trigger health check scan for AWS accounts.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-aws-registration/cloud-registration-aws-trigger-health-check

        Keyword arguments
        -----------------
        account_ids : str or list[str]
            AWS Account IDs.
        organization_ids : str or list[str]
            Organization IDs.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        kwargs["organization-ids"] = kwargs.get("organization_ids", None)
        kwargs["account-ids"] = kwargs.get("account_ids", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_aws_trigger_health_check",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_accounts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve existing AWS accounts by account IDs OR organization IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-aws-registration/cloud-registration-aws-get-accounts

        Keyword arguments
        -----------------
        ids : str or list[str]
            AWS account IDs to filter.
        organization_ids : str or list[str]
            AWS organization IDs to filter.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        kwargs["organization-ids"] = kwargs.get("organization_ids", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_aws_get_accounts",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new account.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-aws-registration/cloud-registration-aws-create-account

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                        "account_id": "string",
                        "account_type": "string",
                        "csp_events": true,
                        "is_master": true,
                        "organization_id": "string",
                        "products": [
                            {
                                "features": [
                                    "string"
                                ],
                                "product": "string"
                            }
                        ]
                        }
                    ]
                }
        account_id : str
            AWS account ID.
        account_type : str
            AWS account type.
        csp_events : bool
            Flag indicating if CSP events should be included.
        is_master : bool
            Flag indicating if this is a master account.
        organization_id : str
            AWS organization ID.
        products : list
            List of included products and features. List of dictionaries.
            [
                {
                    "features": [
                        "string"
                    ],
                    "product": "string"
                }
            ]

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_aws_registration_payload(kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_aws_create_account",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing account.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-aws-registration/cloud-registration-aws-update-account

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                        "account_id": "string",
                        "account_type": "string",
                        "csp_events": true,
                        "is_master": true,
                        "organization_id": "string",
                        "products": [
                            {
                                "features": [
                                    "string"
                                ],
                                "product": "string"
                            }
                        ]
                        }
                    ]
                }
        account_id : str
            AWS account ID.
        account_type : str
            AWS account type.
        csp_events : bool
            Flag indicating if CSP events should be included.
        is_master : bool
            Flag indicating if this is a master account.
        organization_id : str
            AWS organization ID.
        products : list
            List of included products and features. List of dictionaries.
            [
                {
                    "features": [
                        "string"
                    ],
                    "product": "string"
                }
            ]

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_aws_registration_payload(kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_aws_update_account",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_account(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an existing AWS account or organization.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-aws-registration/cloud-registration-aws-delete-account

        Keyword arguments
        -----------------
        ids : str or list[str]
            AWS account IDs to remove.
        organization_ids : str or list[str]
            AWS organization IDs to remove.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        kwargs["organization-ids"] = kwargs.get("organization_ids", None)
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_aws_delete_account",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def validate_accounts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Validate the AWS account registration status, and discover organization child accounts if organization is specified.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-aws-registration/cloud-registration-aws-validate-accounts

        Keyword arguments
        -----------------
        account_id : str
            AWS Account ID. organization-id shouldn't be specified if this is specified.
        iam_role_arn : str
            IAM Role ARN.
        organization_id : str
            AWS organization ID to validate master account.
            account_id shouldn't be specified if this is specified.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        kwargs["iam-role-arn"] = kwargs.get("iam_role_arn", None)
        kwargs["organization-id"] = kwargs.get("organization_id", None)
        kwargs["account-id"] = kwargs.get("account_id", None)
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_aws_validate_accounts",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_accounts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve existing AWS accounts by account IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-aws-registration/cloud-registration-aws-query-accounts

        Keyword arguments
        -----------------
        organization_ids : str or list[str]
            Organization IDs used to filter accounts.
        products : str or list[str] (required)
            Products registered for an account.
        features : str or list[str] (required)
            Features registered for an account.
        account_status : str
            Account status to filter results by.
        limit : int
            The maximum number of items to return. When not specified or 0, 100 is used.
            When larger than 500, 500 is used.
        offset : int
            The offset to start retrieving records from.
        group_by : str
            Field to group by.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        kwargs["organization-ids"] = kwargs.get("organization_ids", None)
        kwargs["account-status"] = kwargs.get("account_status", None)
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_aws_query_accounts",
            keywords=kwargs,
            params=parameters
            )

    cloud_registration_aws_trigger_health_check = trigger_health_check
    cloud_registration_aws_get_accounts = get_accounts
    cloud_registration_aws_create_account = create_account
    cloud_registration_aws_update_account = update_account
    cloud_registration_aws_delete_account = delete_account
    cloud_registration_aws_validate_accounts = validate_accounts
    cloud_registration_aws_query_accounts = query_accounts
