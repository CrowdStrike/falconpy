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
from typing import Dict, Union
from ._util import process_service_request, force_default, handle_single_argument
from ._payload import image_payload, registry_payload
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

    def get_credentials(self: object) -> Dict[str, Union[int, dict]]:
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
    def read_image_vulnerabilities(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Retrieve an assessment report for an image by specifying repository and tag.

        HTTP Method: POST

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container-cli/ReadImageVulnerabilities

        Keyword arguments
        ----
        applicationPackages : list[dict]
            List of application packages.
        body : dict
            Full body payload, not required when using other keywords.
            {
                "applicationPackages": [
                    {
                        "libraries": [
                            {
                                "Hash": "string",
                                "LayerHash": "string",
                                "LayerIndex": 0,
                                "License": "string",
                                "Name": "string",
                                "Path": "string",
                                "Version": "string"
                            }
                        ],
                        "type": "string"
                    }
                ],
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
    def get_assessment(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Retrieve an assessment report for an image by specifying repository and tag.

        If you specify both sets of parameters, the scan report is searched using the image ID
        and digest first. If that fails, the repository and tag are then searched.

        HTTP Method: GET

        Swagger URL
        ----
        This operation does not exist in swagger.

        Keyword arguments
        ----
        digest: str (must be paired with image_id)
            Hash digest for the image.
        image_id: str (must be paired with digest)
            Image ID for the image.
        repository : str (must be paired with tag)
            Repository where the image resides.
        parameters : dict
            Full parameters payload. Not required if using keywords.
        tag : str (must be paired with repository)
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

    def delete_image_details(self: object, *args, image_id: str = None) -> Dict[str, Union[int, dict]]:
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
    def image_matches_policy(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Check if an image matches a policy by specifying repository and tag.

        HTTP Method: GET

        Swagger URL
        ----
        This operation does not exist in swagger.

        Keyword arguments
        ----
        repository : str (required)
            Repository where the image resides.
        parameters : dict
            Full parameters payload. Not required if using keywords.
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

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_registry_entities(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve registry entities identified by the customer ID.

        HTTP Method: GET

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container-image/ReadRegistryEntities

        Keyword arguments
        ----
        limit : int
            The maximum number of records to return in this response. [1-500]
            Use with the offset parameter to manage pagination of results.
        offset : int
            The offset to start retrieving records from.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. Ex: id.asc, id.desc

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadRegistryEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_registry_entities_by_uuid(self: object,
                                       *args,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> dict:
        """Retrieve registry entities identified by the customer UUID.

        HTTP Method: GET

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container-image/ReadRegistryEntitiesByUUID

        Keyword arguments
        ----
        ids : str
            Registry entity UUID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ----
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadRegistryEntitiesByUUID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_registry_entities(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Delete the registry entity identified by the entity UUID.

        HTTP Method: DELETE

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container-image/DeleteRegistryEntities

        Keyword arguments
        ----
        ids : str
            List of Prevention Policy IDs to delete.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ----
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteRegistryEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_registry_entities(self: object, body: dict = None, **kwargs) -> dict:
        """Create a registry entity using the provided details.

        HTTP Method: POST

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container-image/CreateRegistryEntities

        Keyword arguments
        ----
        body : dict
            Full body payload, not required if keywords are used.
                {
                    "credential": {
                        "details": {}
                    },
                    "type": "string",
                    "url": "string",
                    "url_uniqueness_key": "string",
                    "user_defined_alias": "string"
                }

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = registry_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateRegistryEntities",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_registry_entities(self: object, body: dict = None, **kwargs) -> dict:
        """Update the registry entity, as identified by the entity UUID, using the provided details.

        HTTP Method: PATCH

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-container-image/UpdateRegistryEntities

        Keyword arguments
        ----
        body : dict
            Full body payload, not required if keywords are used.
                {
                    Payload here
                }

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = registry_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateRegistryEntities",
            body=body
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetCredentials = get_credentials
    GetImageAssessmentReport = get_assessment
    DeleteImageDetails = delete_image_details
    ImageMatchesPolicy = image_matches_policy
    ReadImageVulnerabilities = read_image_vulnerabilities
    ReadRegistryEntities = read_registry_entities
    ReadRegistryEntitiesByUUID = read_registry_entities_by_uuid
    DeleteRegistryEntities = delete_registry_entities
    CreateRegistryEntities = create_registry_entities
    UpdateRegistryEntities = update_registry_entities
