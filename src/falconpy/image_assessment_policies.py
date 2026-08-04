"""CrowdStrike Falcon Image Assessment Policies API interface class.

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
from ._payload import image_policy_payload, image_exclusions_payload, image_group_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._image_assessment_policies import _image_assessment_policies_endpoints as Endpoints


class ImageAssessmentPolicies(ServiceClass):
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

    def read_policies(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all Image Assessment policies.

        This method does not accept keyword arguments.

        This method does not accept arguments.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/ReadPolicies

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadPolicies"
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_policies(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Image Assessment policies.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/CreatePolicies

        Keyword arguments
        -----------------
        body : dict
            Full body payload, not required when using other arguments.
                {
                    "description": "string",
                    "name": "string"
                }
        description : str
            Policy description.
        name : str
            Policy name.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = image_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreatePolicies",
            body=body
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def update_policies(self: object,
                        body: dict = None,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Image Assessment Policy entities.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/UpdatePolicies

        Keyword arguments
        -----------------
        id : str
            Image Assessment Policy entity UUID
        body : dict
            Full body payload in JSON format. Not required when using other keywords.
                {
                    "description": "string",
                    "is_enabled": boolean,
                    "name": "string",
                    "policy_data": {
                        "rules": [
                            {
                                "action": "string",
                                "policy_rules_data": {
                                    "conditions": [
                                        {}
                                    ]
                                }
                            }
                        ]
                    }
                }
        description : str
            Policy description.
        is_enabled : bool
            Flag indicating if the policy is enabled.
        name : str
            Policy name.
        policy_data : dict
            Policy detail in JSON format.
        rules : str
            List of rules for the policy. List of dictionaries or a single dictionary.
            Overridden if policy_data is supplied.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = image_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdatePolicies",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_policy(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete Image Assessment Policy by policy UUID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/DeletePolicy

        Keyword arguments
        -----------------
        id : str
            Image Assessment Policy entity UUID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeletePolicy",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    def read_policy_exclusions(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Image Assessment Policy Exclusion entities.

        This method does not accept keyword arguments.

        This method does not accept arguments.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/ReadPolicyExclusions

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadPolicyExclusions"
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_policy_exclusions(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Image Assessment Policy Exclusion entities.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/UpdatePolicyExclusions

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format, not required if using other keywords.
                {
                    "conditions": [
                        {
                            "description": "string",
                            "prop": "string",
                            "ttl": 0,
                            "value": [
                                "string"
                            ]
                        }
                    ]
                }
        conditions : list[dict]
            List of conditions to apply to the exclusion policy.
        description : str
            Condition description. Ignored if conditions list is provided.
        prop : str
            Condition property. Ignored if conditions list is provided.
        ttl : int
            Condition time to live. Ignored if conditions list is provided.
        value : list[str]
            Condition values. Ignored if conditions list is provided.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = image_exclusions_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdatePolicyExclusions",
            body=body
            )

    def read_policy_groups(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Image Assessment Policy Group entities.

        This method does not accept keyword arguments.

        This method does not accept arguments.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/ReadPolicyGroups

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadPolicyGroups"
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_policy_groups(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Image Assessment Policy Group entities.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/CreatePolicyGroups

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format, not required whe using other keywords.
                {
                    "description": "string",
                    "name": "string",
                    "policy_group_data": {
                        "conditions": [
                            {}
                        ]
                    },
                    "policy_id": "string"
                }
        conditions : str
            List of policy conditions to apply. Dictionary or list of dictionaries.
            Overridden if policy_group_data is supplied.
        description : str
            Policy group description.
        name : str
            Policy group name.
        policy_group_data : dict
            Policy group conditions.
        policy_id : str
            Policy ID to update.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = image_group_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreatePolicyGroups",
            body=body
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def update_policy_groups(self: object,
                             body: dict = None,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Image Assessment Policy Group entities.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/UpdatePolicyGroups

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format, not required when using other keywords.
                {
                    "description": "string",
                    "name": "string",
                    "policy_group_data": {
                        "conditions": [
                            {}
                        ]
                    }
                }
        conditions : str
            List of policy conditions to apply. Dictionary or list of dictionaries.
            Overridden if policy_group_data is supplied.
        description : str
            Policy group description.
        id : str
            Policy Image Group entity UUID.
        name : str
            Policy group name.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        policy_group_data : dict
            List of policy conditions.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = image_group_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdatePolicyGroups",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_policy_group(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete Image Assessment Policy Group entities.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/DeletePolicyGroup

        Keyword arguments
        -----------------
        id : str
            Policy Image Group entity UUID
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeletePolicyGroup",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_policy_precedence(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Image Assessment Policy precedence.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/image-assessment-policies/UpdatePolicyPrecedence

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format, not required when using other keywords.
                {
                    "precedence": [
                        "string"
                    ]
                }
        precedence : str or list[str]
            List of policy IDs in precedence order.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            prec = kwargs.get("precedence", None)
            if isinstance(prec, str):
                prec = prec.split(",")
            if prec:
                body["precedence"] = prec

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdatePolicyPrecedence",
            body=body
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here
    # for backwards compatibility / ease of use purposes
    ReadPolicies = read_policies
    CreatePolicies = create_policies
    UpdatePolicies = update_policies
    DeletePolicy = delete_policy
    ReadPolicyExclusions = read_policy_exclusions
    UpdatePolicyExclusions = update_policy_exclusions
    ReadPolicyGroups = read_policy_groups
    CreatePolicyGroups = create_policy_groups
    UpdatePolicyGroups = update_policy_groups
    DeletePolicyGroup = delete_policy_group
    UpdatePolicyPrecedence = update_policy_precedence
