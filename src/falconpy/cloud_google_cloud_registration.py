"""CrowdStrike Falcon CloudGoogleCloudRegistration API interface class.

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
from ._util import force_default, process_service_request, handle_single_argument
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._cloud_google_cloud_registration import _cloud_google_cloud_registration_endpoints as Endpoints
from ._payload import cloud_google_registration_create_payload, cloud_registration_gcp_post_terraform_script_payload


class CloudGoogleCloudRegistration(ServiceClass):
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
    def get_entities(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve all GCP entities (organizations, folders, projects) grouped by type.

        Supports FQL filtering, sorting, and pagination.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-google-cloud-registration/cloud-registration-gcp-get-entities

        Keyword arguments
        -----------------
        ids : str or list[str]
            Google Cloud Registration IDs to filter by.
        filter : str
            FQL (Falcon Query Language) string for filtering results. String.
            Allowed filters:
              entity_type           entity_id             entity_name
              registration_id       registration_name     registration_scope
              parent_id             ioa_status            iom_status
              created               updated
        sort : str
            Field and direction for sorting results (e.g., 'created|desc'). String.
            Sorting applies across all entity types before grouping.
        limit : int
            Maximum number of records to return (default: 100, max: 500). Integer.
            Limit applies across all entity types.
        offset : int
            Starting index of result.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_gcp_get_entities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def trigger_health_check(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Trigger health check scan for GCP registrations.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-google-cloud-registration/cloud-registration-gcp-trigger-health-check

        Keyword arguments
        -----------------
        ids : str or list[str]
            GCP Registration IDs.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_gcp_trigger_health_check",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_registration(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a Google Cloud Registration.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-google-cloud-registration/cloud-registration-gcp-get-registration

        Keyword arguments
        -----------------
        ids : str
            Google Cloud Registration ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_gcp_get_registration",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_registration(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new Google Cloud Registration if one doesnt exist or update the existing Google Cloud Registration.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-google-cloud-registration/cloud-registration-gcp-put-registration

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "deployment_method": "string",
                            "entity_id": [
                                "string"
                            ],
                            "excluded_project_patterns": [
                                "string"
                            ],
                            "falcon_client_key_id": "string",
                            "falcon_client_key_type": "string",
                            "infra_manager_region": "string",
                            "infra_project_id": "string",
                            "labels": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            },
                            "products": [
                                {
                                "features": [
                                    "string"
                                ],
                                "product": "string"
                                }
                            ],
                            "registration_name": "string",
                            "registration_scope": "string",
                            "resource_name_prefix": "string",
                            "resource_name_suffix": "string",
                            "tags": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            },
                            "wif_project_id": "string"
                        }
                    ]
                }
        deployment_method : str
            The method of deployment.
        entity_id : str or list[str]
            The ID of the entity.
        excluded_project_patterns : str or list[str]
            Project patterns that should be excluded.
        falcon_client_key_id : str
            API client key ID.
        falcon_client_key_type : str
            API client key type.
        infra_project_id : str
            Infrastructure project ID.
        labels : dict
            Prop labels.
        products : list[dict]
            Products.
        registration_name : str
            Registration name.
        registration_scope : str
            Registration scope.
        resource_name_prefix : str
            Resource name prefix.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_google_registration_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_gcp_put_registration",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_registration(self: object,
                            body: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:  # noqa: E501, pylint: disable=C0301
        """Create a Google Cloud Registration.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-google-cloud-registration/cloud-registration-gcp-create-registration

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "deployment_method": "string",
                            "entity_id": [
                                "string"
                            ],
                            "excluded_project_patterns": [
                                "string"
                            ],
                            "falcon_client_key_id": "string",
                            "falcon_client_key_type": "string",
                            "infra_manager_region": "string",
                            "infra_project_id": "string",
                            "labels": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            },
                            "products": [
                                {
                                "features": [
                                    "string"
                                ],
                                "product": "string"
                                }
                            ],
                            "registration_name": "string",
                            "registration_scope": "string",
                            "resource_name_prefix": "string",
                            "resource_name_suffix": "string",
                            "tags": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            },
                            "wif_project_id": "string"
                        }
                    ]
                }
        deployment_method : str
            The method of deployment.
        entity_id : str or list[str]
            The ID of the entity.
        excluded_project_patterns : str or list[str]
            Project patterns that should be excluded.
        falcon_client_key_id : str
            API client key ID.
        falcon_client_key_type : str
            API client key type.
        infra_project_id : str
            Infrastructure project ID.
        labels : dict
            Prop labels.
        products : list[dict]
            Products.
        registration_name : str
            Registration name.
        registration_scope : str
            Registration scope.
        resource_name_prefix : str
            Resource name prefix.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_google_registration_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_gcp_create_registration",
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def cloud_registration_gcp_update_registration(self: object,
                                                   body: dict = None,
                                                   parameters: dict = None,
                                                   **kwargs
                                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a Google Cloud Registration.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-google-cloud-registration/cloud-registration-gcp-update-registration

        Keyword arguments
        -----------------
        ids : str
            Google Cloud Registration ID.
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "deployment_method": "string",
                            "entity_id": [
                                "string"
                            ],
                            "excluded_project_patterns": [
                                "string"
                            ],
                            "falcon_client_key_id": "string",
                            "falcon_client_key_type": "string",
                            "infra_manager_region": "string",
                            "infra_project_id": "string",
                            "labels": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            },
                            "products": [
                                {
                                "features": [
                                    "string"
                                ],
                                "product": "string"
                                }
                            ],
                            "registration_name": "string",
                            "registration_scope": "string",
                            "resource_name_prefix": "string",
                            "resource_name_suffix": "string",
                            "tags": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            },
                            "wif_project_id": "string"
                        }
                    ]
                }
        deployment_method : str
            The method of deployment.
        entity_id : str or list[str]
            The ID of the entity.
        excluded_project_patterns : str or list[str]
            Project patterns that should be excluded.
        falcon_client_key_id : str
            API client key ID.
        falcon_client_key_type : str
            API client key type.
        infra_project_id : str
            Infrastructure project ID.
        labels : dict
            Prop labels.
        products : list[dict]
            Products.
        registration_name : str
            Registration name.
        registration_scope : str
            Registration scope.
        resource_name_prefix : str
            Resource name prefix.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_google_registration_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_gcp_update_registration",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_registration(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a Google Cloud Registration and return the deleted registration in the response body.

        HTTP Method: DELETE

        Swagger URL
        -----------

        Keyword arguments
        -----------------
        ids : str
            Google Cloud Registration ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_gcp_delete_registration",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def cloud_registration_gcp_post_terraform_script(self: object,
                                                     body: dict = None,
                                                     **kwargs
                                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Generate Google Cloud Terraform deployment scripts (zip files).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-google-cloud-registration/cloud_registration_gcp_post_terraform_script

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "entity_id": [
                                "string"
                            ],
                            "excluded_project_patterns": [
                                "string"
                            ],
                            "falcon_client_key_id": "string",
                            "falcon_client_key_type": "string",
                            "infra_project_id": "string",
                            "labels": "string",
                            "realtime_visibility_enabled": true,
                            "registration_id": "string",
                            "registration_name": "string",
                            "resource_name_prefix": "string",
                            "resource_name_suffix": "string",
                            "tags": "string",
                            "vars_only": true,
                            "wif_project_id": "string"
                        }
                    ]
                }
        resources : list
            The resources value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_registration_gcp_post_terraform_script_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_gcp_post_terraform_script",
            body=body
            )

    cloud_registration_gcp_get_entities = get_entities
    cloud_registration_gcp_trigger_health_check = trigger_health_check
    cloud_registration_gcp_get_registration = get_registration
    cloud_registration_gcp_put_registration = update_registration
    cloud_registration_gcp_create_registration = create_registration
    cloud_registration_gcp_update_registration = cloud_registration_gcp_update_registration
    cloud_registration_gcp_delete_registration = delete_registration
