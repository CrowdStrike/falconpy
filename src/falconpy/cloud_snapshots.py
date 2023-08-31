"""CrowdStrike Cloud Snapshots API Interface Class.

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
from ._util import process_service_request, force_default
from ._payload import snapshot_registration_payload, snapshot_inventory_payload
from ._service_class import ServiceClass
from ._endpoint._cloud_snapshots import _cloud_snapshot_endpoints as Endpoints


class CloudSnapshots(ServiceClass):
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

    def get_credentials(self: object) -> Dict[str, Union[int, dict]]:
        """Retrieve the registry credentials.

        HTTP Method: GET

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-snapshots/GetCredentialsMixin0

        Keyword arguments
        ----
        This method does not accept keyword arguments.

        Arguments
        ----
        This method does not accept arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCredentialsMixin0"
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_inventory(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Create inventory from data received from a snapshot.

        Keyword arguments:
        body - full body payload in JSON format, not required if using other keywords.
               {
                   "job_metadata": {
                       "cloud_provider": "string",
                       "instance_id": "string",
                       "job_end_time": "2023-08-31T02:45:34.131Z",
                       "job_id": "string",
                       "job_start_time": "2023-08-31T02:45:34.131Z",
                       "message": "string",
                       "scanner_version": "string",
                       "status": "string"
                   },
                   "results": {
                       "applications": [
                           {
                               "major_version": "string",
                               "package_hash": "string",
                               "package_provider": "string",
                               "package_source": "string",
                               "path": "string",
                               "product": "string",
                               "software_architecture": "string",
                               "type": "string",
                               "vendor": "string"
                           }
                       ],
                       "os_version": "string"
                   }
               }
        cloud_provider -- Name of the cloud provider. String.
        instance_id -- ID of the instance. String.
        job_end_time -- Completion time for the job. UTC date string.
        job_id -- ID of the job. String.
        job_start_time -- Start time for the job. UTC date string.
        message -- Message received upon job completion. String.
        scanner_version -- Version identifier for the scanner used. String.
        status -- Job completion status. String.
        results -- Full results payload. Dictionary. Overrides values below.
        os_version -- Operating system version. String.
        applications -- Complete application list. List of dictionaries. Overrides values below.
        major_version -- Application major version. String.
        package_hash -- Hash for the package. String.
        package_provider -- Package provider. String.
        path -- File path for the application. String.
        product - Product name for the application. String.
        software_architecture -- Running architecture for the application. String.
        type -- Type of application. String.
        vendor -- Application vendor. String.
        job_metadata -- Complete job metadata. Dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-snapshots/CreateInventory
        """
        if not body:
            body = snapshot_inventory_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateInventory",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def register_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Create inventory from data received from a snapshot.

        Keyword arguments:
        body - full body payload in JSON format, not required if using other keywords.
               {
                   "aws_accounts": [
                       {
                           "account_number": "string",
                           "batch_regions": [
                               {
                                   "job_definition_name": "string",
                                   "job_queue": "string",
                                   "region": "string"
                               }
                           ],
                           "iam_external_id": "string",
                           "iam_role_arn": "string",
                           "kms_alias": "string",
                           "processing_account": "string"
                       }
                   ]
               }
        aws_accounts -- Complete list of AWS accounts to register. List of dictionaries.
                        Overrides any values specified below.
        account_number -- AWS account number. String
        batch_regions -- Region the batch is executed. List of dictionaries.
        iam_external_id -- The external ID of the IAM account used. String.
        iam_role_arn -- The AWS ARN for the IAM account used. String.
        kms_alias -- The KMS alias for the IAM account used. String.
        processing_account -- The name of the processing account. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-snapshots/RegisterCspmSnapshotAccount
        """
        if not body:
            body = snapshot_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RegisterCspmSnapshotAccount",
            keywords=kwargs,
            body=body
            )

    # This method name aligns to the operation ID in the API but
    # does not conform to snake_case / PEP8 and is defined here
    # for backwards compatibility / ease of use purposes
    GetCredentialsMixin0 = get_credentials
    CreateInventory = create_inventory
    RegisterCspmSnapshotAccount = register_account
