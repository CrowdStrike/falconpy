"""Falcon Container API Interface Class.

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
from ._util import process_service_request, force_default
from ._payload import image_payload
from ._service_class import ServiceClass
from ._endpoint._falcon_container import _falcon_container_endpoints as Endpoints


class FalconContainer(ServiceClass):
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

    def get_credentials(self: object) -> dict:
        """Retrieve the registry credentials.

        HTTP Method: GET

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container/GetCredentials

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
            operation_id="GetCredentials"
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def read_image_vulnerabilities(self: object, body: dict = None, **kwargs) -> dict:
        """Retrieve an assessment report for an image by specifying repository and tag.

        HTTP Method: POST

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container-cli/ReadImageVulnerabilities

        Keyword arguments
        ----
        body : str
            Full body payload in JSON format, not required when using other keywords.
            {
                "osversion": "string",
                "packages": [
                    {
                        "LayerHash": "string",
                        "LayerIndex": 0,
                        "MajorVersion": "string",
                        "PackageHash": "string",
                        "PackageProvider": "string",
                        "PackageSource": "string",
                        "Product": "string",
                        "SoftwareArchitecture": "string",
                        "Status": "string",
                        "Vendor": "string"
                    }
                ]
            }
        packages : list[dict]
            List of images to retrieve vulnerabilities for.
        osversion : str
            Operating system version for the image to be checked.

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = image_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadImageVulnerabilities",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_assessment(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve an assessment report for an image by specifying repository and tag.

        HTTP Method: GET

        Swagger URL
        ----
        This operation does not exist in swagger.

        Keyword arguments
        ----
        repository : str (required)
            Repository where the image resides.
        parameters : str (JSON)
            Full parameters payload in JSON string format. Not required if using keywords.
        tag : str (required)
            Tag used for the image assessed.

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetImageAssessmentReport",
            keywords=kwargs,
            params=parameters
            )

    def delete_image_details(self: object, *args, image_id: str = None) -> dict:
        """Delete image details from the CrowdStrike registry.

        HTTP Method: DELETE

        Swagger URL
        ----
        This operation does not exist in swagger.

        Keyword arguments
        ----
        image_id : str (required)
            ID of the image to delete details for.

        Arguments
        ----
        When not specified, the first argument to this method is assumed
        to be 'image_id'. All others are ignored.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        if args:
            image_id = args[0]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteImageDetails",
            image_id=image_id
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def image_matches_policy(self: object, parameters: dict = None, **kwargs) -> dict:
        """Check if an image matches a policy by specifying repository and tag.

        HTTP Method: GET

        Swagger URL
        ----
        This operation does not exist in swagger.

        Keyword arguments
        ----
        repository : str (required)
            Repository where the image resides.
        parameters : str (JSON)
            Full parameters payload in JSON string format. Not required if using keywords.
        tag : str (required)
            Tag used for the image assessed.

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        parameters["policy_type"] = "image-prevention-policy"
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ImageMatchesPolicy",
            keywords=kwargs,
            params=parameters
            )

    # This method name aligns to the operation ID in the API but
    # does not conform to snake_case / PEP8 and is defined here for
    # backwards compatibility / ease of use purposes
    GetCredentials = get_credentials
    GetImageAssessmentReport = get_assessment
    DeleteImageDetails = delete_image_details
    ImageMatchesPolicy = image_matches_policy
