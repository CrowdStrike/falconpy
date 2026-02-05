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

from samples.sensor_update_policies.policy_wonk import create_policy
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

        Keyword arguments:
        ids -- The list of policies to return (maximum 100 IDs allowed). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-get-policies
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

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "description": "string",
                    "name": "string"
                }
        description -- String.
        name -- String.
        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-create-policy
        """
        if not body:
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

        Keyword arguments:
        ids -- The id of the admission control policy to update. String.
        body -- full body payload, not required when using other keywords.
                {
                    "description": "string",
                    "is_enabled": true,
                    "name": "string"
                }
        description -- String.
        is_enabled - Boolean.
        name -- String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-update-policy
        """
        if not body:
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

        Keyword arguments:
        ids -- The ids of the policies to delete (maximum 100 IDs allowed). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-delete-policies
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

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "host_groups": [
                        "string"
                    ],
                    "id": "string"
                }
        host_groups -- String or list of strings.
        id -- String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-add-host-groups
        """
        if not body:
            keys = ["host_groups", "id"]
            for key in keys:
                provided = kwargs.get(key, None)
                if provided:
                    if provided == "host_groups" and isinstance(provided, str):
                        provided = provided.split(",")
                        body[provided] = kwargs.get(key, None)
                    else:
                        body[provided] = kwargs.get(key, None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_add_host_groups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def remove_host_groups(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove one or more host groups from an admission control policy.

        Keyword arguments:
        policy_id -- The id of the policy to modify. String.
        host_group_ids -- The ids of the host groups to remove (maximum 100 IDs allowed). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-remove-host-groups
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

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "id": "string",
                    "precedence": 0
                }
        id -- String.
        precendence -- Integer.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-update-policy-precedence
        """
        if not body:
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

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
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
        id -- String.
        rule_groups -- List of dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-add-rule-group-custom-rule
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

        Keyword arguments:
        policy_id -- The id of the policy to modify. String.
        custom_rule_ids -- The ids of the custom Rego rules to delete (maximum 100 IDs allowed). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-remove-rule-group-custom-rule
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

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "id": "string",
                    "rule_groups": [
                        {
                        "id": "string"
                        }
                    ]
                }
        id -- String.
        rule_groups -- List of dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PUT

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-set-rule-group-precedence
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

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
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
        id -- String.
        rule_groups -- List of dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PUT

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-replace-rule-group-selectors
        """
        if not body:
            body = acp_custom_rules_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_replace_rule_group_selectors",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def create_rule_groups(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create one or more rule groups and add them to an existing admission control policy.
        The list of new rule groups will be created with the last rule group having highest precedence,
        second to last with second highest precedence, and so on.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "id": "string",
                    "rule_groups": [
                        {
                        "description": "string",
                        "name": "string"
                        }
                    ]
                }
        id -- String.
        rule_groups -- List of dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-create-rule-groups
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

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
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
        id -- String.
        rule_groups -- List of dictionaries.
        
        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-update-rule-groups
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="admission_control_update_rule_groups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule_groups(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete rule groups.

        Keyword arguments:
        policy_id -- The id of the policy to modify. String.
        rule_group_ids -- The ids of the rule groups to delete (maximum 100 IDs allowed). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-delete-rule-groups
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

        Keyword arguments:
        filter -- FQL filter. String.
                  Allowed properties: 
                    precedence          created_timestamp
                    modified_timestamp  name
                    description
        limit -- The maximum number of resources to return. The maximum allowed is 500. Integer.
        offset -- The number of results to skip before starting to return results. Integer.
        sort -- Field to sort on.
                Sortable fields:
                    precedence          created_timestamp
                    modified_timestamp
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/admission-control-policies/admission-control-query-policies
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