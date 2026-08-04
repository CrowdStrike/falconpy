"""CrowdStrike Falcon AdmissionControlPolicies API interface class.

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
from ._payload import acp_custom_rules_policy_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._admission_control_policies import _admission_control_policies_endpoints as Endpoints


class AdmissionControlPolicies(ServiceClass):
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
    def get_policies(self: object,
                     *args,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get admission control policies.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-get-policies

        Keyword arguments
        -----------------
        ids : str or list[str]
            The list of policies to return (maximum 100 IDs allowed)
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
            operation_id="admission_control_get_policies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_policy(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create an admission control policy.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-create-policy

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "description": "string",
                    "name": "string"
                }
        description : str
            Description for the new policy.
        name : str
            Name of the new policy.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = {}
            keys = ["description", "name"]
            for key in keys:
                provided = kwargs.get(key, None)
                if provided:
                    body[key] = provided

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_create_policy",
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_policy(self: object,
                      body: dict = None,
                      parameters: dict = None,
                      **kwargs
                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an admission control policy.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-update-policy

        Keyword arguments
        -----------------
        ids : str
            The id of the admission control policy to update.
        body : dict
            full body payload, not required when using other keywords.
                {
                    "description": "string",
                    "is_enabled": true,
                    "name": "string"
                }
        description : str
            Description for the policy.
        is_enabled : bool
            Flag indicating if the policy is enabled.
        name : str
            Name of the policy.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = {}
            keys = ["description", "name", "is_enabled"]
            for key in keys:
                provided = kwargs.get(key, None)
                if provided:
                    body[key] = provided

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_update_policy",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_policies(self: object,
                        *args,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an admission control policy.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-delete-policies

        Keyword arguments
        -----------------
        ids : str or list[str]
            The ids of the policies to delete (maximum 100 IDs allowed)
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
            operation_id="admission_control_delete_policies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_host_groups(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add one or more host groups to an admission control policy.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-add-host-groups

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "host_groups": [
                        "string"
                    ],
                    "id": "string"
                }
        host_groups : str or list[str]
            List of host group IDs to add to the policy.
        id : str
            The ID of the admission control policy to modify.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = {}
            keys = ["host_groups", "id"]
            for key in keys:
                provided = kwargs.get(key, None)
                if provided:
                    if key == "host_groups" and isinstance(provided, str):
                        provided = provided.split(",")
                    body[key] = provided

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_add_host_groups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def remove_host_groups(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove one or more host groups from an admission control policy.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-remove-host-groups

        Keyword arguments
        -----------------
        policy_id : str
            The id of the policy to modify.
        host_group_ids : str or list[str]
            The ids of the host groups to remove (maximum 100 IDs allowed)
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
            operation_id="admission_control_remove_host_groups",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_policy_precedence(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update admission control policy precedence.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-update-policy-precedence

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "id": "string",
                    "precedence": 0
                }
        id : str
            The ID of the admission control policy.
        precedence : int
            Policy precedence value.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = {}
            keys = ["id", "precedence"]
            for key in keys:
                provided = kwargs.get(key, None)
                if provided:
                    body[key] = provided

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_update_policy_precedence",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_custom_rules(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add one or more custom Rego rules to a rule group in an admission control policy.

        The requested custom rules are also added to all other unspecified rule groups in the policy with action 'Disabled'.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-add-rule-group-custom-rule

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "id": "string",
                    "rule_groups": [
                        {
                        "custom_rules": [
                            {
                            "action": "string",
                            "id": "string"
                            }
                        ],
                        "id": "string"
                        }
                    ]
                }
        id : str
            The ID of the admission control policy.
        rule_groups : list[dict]
            List of rule group definitions containing custom rules to add.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = acp_custom_rules_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_add_rule_group_custom_rule",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_custom_rules(self: object,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete one or more custom Rego rules from all rule groups in an admission control policy.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-remove-rule-group-custom-rule

        Keyword arguments
        -----------------
        policy_id : str
            The id of the policy to modify.
        custom_rule_ids : str or list[str]
            The ids of the custom Rego rules to delete (maximum 100 IDs allowed)
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
            operation_id="admission_control_remove_rule_group_custom_rule",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def set_rule_group_precedence(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Change precedence of rule groups within an admission control policy.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-set-rule-group-precedence

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "id": "string",
                    "rule_groups": [
                        {
                        "id": "string"
                        }
                    ]
                }
        id : str
            The ID of the admission control policy.
        rule_groups : list[dict]
            List of rule group definitions specifying the new precedence order.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = acp_custom_rules_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_set_rule_group_precedence",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def replace_rule_group_selectors(self: object,
                                     body: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Replace labels and/or namespaces of a rule group within an admission control policy.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-replace-rule-group-selectors

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "id": "string",
                    "rule_groups": [
                        {
                        "id": "string",
                        "labels": [
                            {
                            "key": "string",
                            "operator": "string",
                            "value": "string"
                            }
                        ],
                        "namespaces": [
                            {
                            "value": "string"
                            }
                        ]
                        }
                    ]
                }
        id : str
            The ID of the admission control policy.
        rule_groups : list[dict]
            List of rule group definitions with replacement labels and namespaces.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = acp_custom_rules_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_replace_rule_group_selectors",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_rule_groups(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create one or more rule groups and add them to an existing admission control policy.

        The list of new rule groups will be created with the last rule group having highest precedence,
        second to last with second highest precedence, and so on.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-create-rule-groups

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "id": "string",
                    "rule_groups": [
                        {
                        "description": "string",
                        "name": "string"
                        }
                    ]
                }
        id : str
            The ID of the admission control policy.
        rule_groups : list[dict]
            List of rule group definitions to create.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = acp_custom_rules_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_create_rule_groups",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_rule_groups(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a rule group.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-update-rule-groups

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "id": "string",
                    "rule_groups": [
                        {
                        "custom_rules": [
                            {
                            "action": "string",
                            "id": "string"
                            }
                        ],
                        "default_rules": [
                            {
                            "action": "string",
                            "code": "string"
                            }
                        ],
                        "deny_on_error": {
                            "deny": true
                        },
                        "description": "string",
                        "id": "string",
                        "image_assessment": {
                            "enabled": true,
                            "unassessed_handling": "string"
                        },
                        "name": "string"
                        }
                    ]
                }
        id : str
            The ID of the admission control policy.
        rule_groups : list[dict]
            List of rule group definitions to update.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = acp_custom_rules_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_update_rule_groups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule_groups(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete rule groups.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-delete-rule-groups

        Keyword arguments
        -----------------
        policy_id : str
            The id of the policy to modify.
        rule_group_ids : str or list[str]
            The ids of the rule groups to delete (maximum 100 IDs allowed)
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
            operation_id="admission_control_delete_rule_groups",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policies(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search admission control policies.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-query-policies

        Keyword arguments
        -----------------
        filter : str
            FQL filter. String.
            Allowed properties:
              precedence          created_timestamp
              modified_timestamp  name
              description
        limit : int
            The maximum number of resources to return. The maximum allowed is 500.
        offset : int
            The number of results to skip before starting to return results.
        sort : str
            Field to sort on.
            Sortable fields:
                precedence          created_timestamp
                modified_timestamp
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
            operation_id="admission_control_query_policies",
            keywords=kwargs,
            params=parameters
            )

    admission_control_get_policies = get_policies
    admission_control_create_policy = create_policy
    admission_control_update_policy = update_policy
    admission_control_delete_policies = delete_policies
    admission_control_add_host_groups = add_host_groups
    admission_control_remove_host_groups = remove_host_groups
    admission_control_update_policy_precedence = update_policy_precedence
    admission_control_add_rule_group_custom_rule = add_custom_rules
    admission_control_remove_rule_group_custom_rule = delete_custom_rules
    admission_control_set_rule_group_precedence = set_rule_group_precedence
    admission_control_replace_rule_group_selectors = replace_rule_group_selectors
    admission_control_create_rule_groups = create_rule_groups
    admission_control_update_rule_groups = update_rule_groups
    admission_control_delete_rule_groups = delete_rule_groups
    admission_control_query_policies = query_policies
