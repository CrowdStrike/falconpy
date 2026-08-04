"""CrowdStrike Falcon CloudPolicies API interface class.

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
# pylint: disable=C0302
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._cloud_policies import _cloud_policies_endpoints as Endpoints
from ._payload._cloud_policies import (
    cloud_policies_rule_assign_payload,
    cloud_policies_compliance_control_payload,
    cloud_policies_evaluation_payload,
    cloud_policies_rule_override_payload,
    cloud_policies_rule_create_payload,
    cloud_policies_rule_update_payload,
    cloud_policies_suppression_rule_payload
    )


class CloudPolicies(ServiceClass):
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
    def get_rule_input_schema(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get rule input schema for given resource type.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/GetRuleInputSchema

        Keyword arguments
        -----------------
        domain : str
            domain.
        subdomain : str
            subdomain.
        cloud_provider : str
            Cloud service provider for the resource type.
        resource_type : str
            Selects the resource type for which to retrieve the rule input schema.
        enriched : bool
            When true, returns the enriched schema with inlined related resource types. Defaults to true.
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
            operation_id="GetRuleInputSchema",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def replace_control_rules(self: object,
                              body: dict = None,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Assign rules to a compliance control (full replace).

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/ReplaceControlRules

        Keyword arguments
        -----------------
        ids : str
            The UUID of the compliance control to assign rules to.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "rule_ids": [
                        "string"
                    ]
                }
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        rule_ids : str or list[str]
            The ids of the rules to replace.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_rule_assign_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReplaceControlRules",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_compliance_controls(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get compliance controls by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/GetComplianceControls

        Keyword arguments
        -----------------
        ids : str or list[str]
            The uuids of compliance controls to retrieve.
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
            operation_id="GetComplianceControls",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_compliance_control(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new custom compliance control.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/CreateComplianceControl

        Keyword arguments
        -----------------
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "description": "string",
                    "framework_id": "string",
                    "name": "string",
                    "section_name": "string"
                }
        description : str
            The description of hte custom compliance control.
        framework_id : str
            The framework ID of the custom compliance control.
        name : str
            The name of the custom compliance control.
        section_name : str
            The section name of the custom compliance control.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_compliance_control_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateComplianceControl",
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_compliance_control(self: object,
                                  body: dict = None,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a custom compliance control.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/UpdateComplianceControl

        Keyword arguments
        -----------------
        ids : str
            The uuid of compliance control to update.
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "description": "string",
                    "name": "string"
                }
        description : str
            The description of hte custom compliance control.
        name : str
            The name of the custom compliance control.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_compliance_control_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateComplianceControl",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_compliance_control(self: object,
                                  *args,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete custom compliance controls.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/DeleteComplianceControl

        Keyword arguments
        -----------------
        ids : str or list[str]
            The uuids of compliance control to delete.
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
            operation_id="DeleteComplianceControl",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def rename_section_compliance_framework(self: object,
                                            body: dict = None,
                                            parameters: dict = None,
                                            **kwargs
                                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Rename a section in a custom compliance framework.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/RenameSectionComplianceFramework

        Keyword arguments
        -----------------
        ids : str
            The uuid of compliance framework containing the section to rename.
        sectionName : str
            The current name of the section to rename.
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "section_name": "string"
                }
        section_name : str
            The new section name of the custom compliance control.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_compliance_control_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RenameSectionComplianceFramework",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_compliance_frameworks(self: object,
                                  *args,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get compliance frameworks by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/GetComplianceFrameworks

        Keyword arguments
        -----------------
        ids : str or list[str]
            The uuids of compliance frameworks to retrieve.
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
            operation_id="GetComplianceFrameworks",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_compliance_framework(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new custom compliance framework.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/CreateComplianceFramework

        Keyword arguments
        -----------------
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "active": true,
                    "description": "string",
                    "name": "string"
                }
        active : bool
            Value to determine if the compliance framework will be active.
        description : str
            The description of the new compliance framework.
        name : str
            The name of the new compliance framework.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_compliance_control_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateComplianceFramework",
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_compliance_framework(self: object,
                                    body: dict = None,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a custom compliance framework.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/UpdateComplianceFramework

        Keyword arguments
        -----------------
        ids : str
            The uuids of compliance framework to update.
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "active": true,
                    "description": "string",
                    "name": "string"
                }
        active : bool
            Value to determine if the compliance framework will be active.
        description : str
            The description of the new compliance framework.
        name : str
            The name of the new compliance framework.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_compliance_control_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateComplianceFramework",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_compliance_framework(self: object,
                                    *args,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a custom compliance framework and all associated controls and rule assignments.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/DeleteComplianceFramework

        Keyword arguments
        -----------------
        ids : str
            The uuids of compliance framework to delete.
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
            operation_id="DeleteComplianceFramework",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_enriched_asset(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get enriched assets that combine a primary resource with all its related resources.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/GetEnrichedAsset

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of asset IDs (maximum 100 IDs allowed)
        domain : str
            Rule domain (Currently only used for KAC Rego rules)
        subdomain : str
            Rule subdomain (Currently only used for KAC Rego rules)
        resource_type : str
            Currently the Resource type field is only used when KAC Rules are specified vai Domain: Runtime &
            Subdomain: IOM. For KAC rules, we return static sample data instead of real
            assets b/c we don't have KAC payloads stored for customers. This field valued
            selects what sample data resource type we return which the UI shows in the
            Rego Editor to do test evaluations.
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
            operation_id="GetEnrichedAsset",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def get_evaluation_result(self: object,
                              body: dict = None,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get evaluation results based on the provided rule.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/GetEvaluationResult

        Keyword arguments
        -----------------
        cloud_provider : str
            Cloud Service Provider of the provided IDs.
        resource_type : str
            Resource Type of the provided IDs.
        ids : str or list[str]
            List of assets to evaluate (maximum 100 IDs allowed)
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "input": {},
                    "logic": "string"
                }
        input : dict
            The input for the provided rule.
        logic : str
            The logic of the provided rule.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_evaluation_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetEvaluationResult",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_override(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a rule override.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/GetRuleOverride

        Keyword arguments
        -----------------
        ids : str or list[str]
            The uuids of rule overrides to retrieve.
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
            operation_id="GetRuleOverride",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_rule_override(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new rule override.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/CreateRuleOverride

        Keyword arguments
        -----------------
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "overrides": [
                        {
                            "comment": "string",
                            "crn": "string",
                            "expires_at": "2025-11-10T21:16:14.315Z",
                            "override_type": "string",
                            "overrides_details": "string",
                            "reason": "string",
                            "rule_id": "string",
                            "target_region": "string"
                        }
                    ]
                }
        overrides : list[dict]
            The new rule override.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_rule_override_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateRuleOverride",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_rule_override(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a rule override.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/UpdateRuleOverride

        Keyword arguments
        -----------------
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "overrides": [
                        {
                            "comment": "string",
                            "crn": "string",
                            "expires_at": "2025-11-10T21:16:14.315Z",
                            "override_type": "string",
                            "overrides_details": "string",
                            "reason": "string",
                            "rule_id": "string",
                            "target_region": "string"
                        }
                    ]
                }
        overrides : list[dict]
            The new rule override.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_rule_override_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateRuleOverride",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule_override(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a rule override.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/DeleteRuleOverride

        Keyword arguments
        -----------------
        ids : str or list[str]
            The uuids of rule overrides to delete.
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
            operation_id="DeleteRuleOverride",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule(self: object,
                 *args,
                 parameters: dict = None,
                 **kwargs
                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a rule by id.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/GetRule

        Keyword arguments
        -----------------
        ids : str or list[str]
            The uuids of rules to retrieve.
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
            operation_id="GetRule",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_rule(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new rule.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/CreateRuleMixin0

        Keyword arguments
        -----------------
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
            Rule severity integer to provide maps to the following:
            0=Critical, 1=High, 2=Medium and 3=Low.
            For CSPM IOM Custom Rules, logic is mandatory and
            parent_rule_id should not be specified.
            For Runtime IOM Custom Rules (KAC), logic is mandatory.
            Fields controls, resource_type, and parent_rule_id should not be specified.
            For Managed Rule duplication, parent_rule_id is mandatory
            and logic should be not specified.
                {
                    "alert_info": "string",
                    "attack_types": "string",
                    "controls": [
                        {
                            "Authority": "string",
                            "Code": "string"
                        }
                    ],
                    "description": "string",
                    "domain": "string",
                    "logic": "string",
                    "name": "string",
                    "parent_rule_id": "string",
                    "platform": "string",
                    "provider": "string",
                    "remediation_info": "string",
                    "remediation_url": "string",
                    "resource_type": "string",
                    "severity": 0,
                    "subdomain": "string"
                }
        alert_info : str
            The info of the alert.
        attack_types : str
            The type of attacks.
        controls : list[dict]
            The authority and code of the rule.
        description : str
            The description of the rule.
        domain : str
            The domain of the rule.
        logic : str
            The logic for the rule.
        name : str
            The name of the rule.
        parent_rule_id : str
            The id of the parent.
        platform : str
            The platform covered by the rule.
        provider : str
            The provider for the rule.
        remediation_info : str
            The remediation info provided by the rule.
        remediation_url : str
            The URL providing the remediation.
        resource_type : str
            The type of the resource.
        severity : int
            The severity level.
        subdomain : str
            The subdomain for the rule.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_rule_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateRuleMixin0",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_rule(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a rule.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/UpdateRule

        Keyword arguments
        -----------------
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "alert_info": "string",
                    "attack_types": [
                            "string"
                    ],
                    "category": "string",
                    "controls": [
                        {
                            "authority": "string",
                            "code": "string"
                        }
                    ],
                    "description": "string",
                    "name": "string",
                    "rule_logic_list": [
                        {
                            "logic": "string",
                            "platform": "string",
                            "remediation_info": "string",
                            "remediation_url": "string"
                        }
                    ],
                    "severity": 0,
                    "uuid": "string"
                }
        alert_info : str
            The info of the alert.
        attack_types : str or list[str]
            The type of attacks.
        controls : list[dict]
            The authority and code of the rule.
        description : str
            The description of the rule.
        name : str
            The name of the rule.
        rule_logic_list : list[dict]
            The logic list data.
        severity : int
            The severity level.
        uuid : str
            The uuid of the rule to update.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_rule_update_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateRule",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule(self: object,
                    *args,
                    parameters: dict = None,
                    **kwargs
                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a rule.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/DeleteRuleMixin0

        Keyword arguments
        -----------------
        ids : str or list[str]
            The uuids of rules to delete.
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
            operation_id="DeleteRuleMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_compliance_controls(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for compliance controls by various parameters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/QueryComplianceControls

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. String.
            Allowed filter fields:
              compliance_control_name                 compliance_control_authority
              compliance_control_type 	            compliance_control_section
              compliance_control_requirement	        compliance_control_benchmark_name
              compliance_control_benchmark_version
        limit : int
            The maximum number of resources to return. The maximum allowed is 500.
        offset : int
            The number of results to skip before starting to return results.
        sort : str
            The sort expression that should be used to sort the results. String.
            Use the '|asc' or '|desc' suffix to specify sort direction.
            Sortable fields:
                compliance_control_authority	        compliance_control_type
                compliance_control_section              compliance_control_requirement
                compliance_control_benchmark_name	    compliance_control_benchmark_version
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
            operation_id="QueryComplianceControls",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_compliance_frameworks(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for compliance frameworks by various parameters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/QueryComplianceFrameworks

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. String.
            Allowed filter fields:
              compliance_framework_name       compliance_framework_version
              compliance_framework_authority
        limit : int
            The maximum number of resources to return. The maximum allowed is 500.
        offset : int
            The number of results to skip before starting to return results.
        sort : str
            The sort expression that should be used to sort the results. String.
            Use the '|asc' or '|desc' suffix to specify sort direction.
            Sortable fields:
                compliance_framework_name       compliance_framework_version
                compliance_framework_authority
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
            operation_id="QueryComplianceFrameworks",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for rules by various parameters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/QueryRule

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. String.
            Allowed filter fields:
              rule_auto_remediable                rule_mitre_tactic
              rule_category                       rule_mitre_technique
              rule_cloneable                      rule_name
              rule_compliance_benchmark            rule_origin
              rule_compliance_benchmark_uuid       rule_parent_uuid
              rule_compliance_framework            rule_provider
              rule_control_requirement             rule_resource_type
              rule_control_section                 rule_resource_type_name
              rule_created_at                      rule_risk_factor
              rule_description                     rule_service
              rule_domain                          rule_severity
              rule_short_code                      rule_status
              rule_subdomain                       rule_updated_at
              rule_updated_by
        limit : int
            The maximum number of resources to return. The maximum allowed is 500.
        offset : int
            The number of results to skip before starting to return results.
        sort : str
            The sort expression that should be used to sort the results. String.
            Use the '|asc' or '|desc' suffix to specify sort direction.
            Sortable fields:
                rule_auto_remediable                rule_mitre_tactic
                rule_category                       rule_mitre_technique
                rule_cloneable                      rule_name
                rule_compliance_benchmark            rule_origin
                rule_compliance_benchmark_uuid       rule_parent_uuid
                rule_compliance_framework            rule_provider
                rule_control_requirement             rule_resource_type
                rule_control_section                 rule_resource_type_name
                rule_created_at                      rule_risk_factor
                rule_description                     rule_service
                rule_domain                          rule_severity
                rule_short_code                      rule_status
                rule_subdomain                       rule_updated_at
                rule_updated_by
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
            operation_id="QueryRule",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_suppression_rules(self: object,
                              *args,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Suppression Rules by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/GetSuppressionRules

        Keyword arguments
        -----------------
        ids : str or list[str]
            The uuids of the suppression rules to retrieve.
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
            operation_id="GetSuppressionRules",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_suppression_rule(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new suppression rule.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/CreateSuppressionRule

        Keyword arguments
        -----------------
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "description": "string",
                    "id": "string",
                    "name": "string",
                    "rule_selection_filter": {
                        "rule_ids": [
                        "string"
                        ],
                        "rule_names": [
                        "string"
                        ],
                        "rule_origins": [
                        "string"
                        ],
                        "rule_providers": [
                        "string"
                        ],
                        "rule_services": [
                        "string"
                        ],
                        "rule_severities": [
                        "string"
                        ]
                    },
                    "rule_selection_type": "string",
                    "scope_asset_filter": {
                        "account_ids": [
                        "string"
                        ],
                        "cloud_group_ids": [
                        "string"
                        ],
                        "cloud_providers": [
                        "string"
                        ],
                        "regions": [
                        "string"
                        ],
                        "resource_ids": [
                        "string"
                        ],
                        "resource_names": [
                        "string"
                        ],
                        "resource_types": [
                        "string"
                        ],
                        "service_categories": [
                        "string"
                        ],
                        "tags": [
                        "string"
                        ]
                    },
                    "scope_type": "string",
                    "suppression_comment": "string",
                    "suppression_expiration_date": "string",
                    "suppression_reason": "string"
                }
        description : str
            Description of the suppression rule.
        domain : str
            Policy domain for the rule.
        name : str
            Name of the suppression rule.
        rule_selection_filter : dict
            Filter criteria for selecting rules. Dictionary of lists.
        rule_selection_type : str
            Type of rule selection.
        scope_asset_filter : dict
            Filter criteria for scoping assets. Dictionary of lists.
        scope_type : str
            Type of scope for the rule.
        subdomain : str
            Policy subdomain for the rule.
        suppression_comment : str
            Comment explaining the suppression.
        suppression_expiration_date : str
            Expiration date for the suppression.
        suppression_reason : str
            Reason for the suppression.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_suppression_rule_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateSuppressionRule",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_suppression_rule(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a suppression rule.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/UpdateSuppressionRule

        Keyword arguments
        -----------------
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "description": "string",
                    "id": "string",
                    "name": "string",
                    "rule_selection_filter": {
                        "rule_ids": [
                        "string"
                        ],
                        "rule_names": [
                        "string"
                        ],
                        "rule_origins": [
                        "string"
                        ],
                        "rule_providers": [
                        "string"
                        ],
                        "rule_services": [
                        "string"
                        ],
                        "rule_severities": [
                        "string"
                        ]
                    },
                    "rule_selection_type": "string",
                    "scope_asset_filter": {
                        "account_ids": [
                        "string"
                        ],
                        "cloud_group_ids": [
                        "string"
                        ],
                        "cloud_providers": [
                        "string"
                        ],
                        "regions": [
                        "string"
                        ],
                        "resource_ids": [
                        "string"
                        ],
                        "resource_names": [
                        "string"
                        ],
                        "resource_types": [
                        "string"
                        ],
                        "service_categories": [
                        "string"
                        ],
                        "tags": [
                        "string"
                        ]
                    },
                    "scope_type": "string",
                    "suppression_comment": "string",
                    "suppression_expiration_date": "string",
                    "suppression_reason": "string"
                }
        description : str
            Description of the suppression rule.
        id : str
            Identifier of the suppression rule to update.
        name : str
            Name of the suppression rule.
        rule_selection_filter : dict
            Filter criteria for selecting rules. Dictionary of lists.
        rule_selection_type : str
            Type of rule selection.
        scope_asset_filter : dict
            Filter criteria for scoping assets. Dictionary of lists.
        scope_type : str
            Type of scope for the rule.
        suppression_comment : str
            Comment explaining the suppression.
        suppression_expiration_date : str
            Expiration date for the suppression.
        suppression_reason : str
            Reason for the suppression.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cloud_policies_suppression_rule_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateSuppressionRule",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_suppression_rules(self: object,
                                 *args,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete Suppression Rules by ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/DeleteSuppressionRules

        Keyword arguments
        -----------------
        ids : str or list[str]
            The uuids of the suppression rules to delete. A maximum of 10 IDs can be provided. String or array of strings.
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
            operation_id="DeleteSuppressionRules",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_suppression_rules(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query suppression rules with filtering, sorting and pagination.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/QuerySuppressionRules

        Keyword arguments
        -----------------
        filter : str
            FQL expression to filter suppression rules. String.
            The allowed properties are:
                name        description         domain
                subdomain   suppression_reason  suppression_expiration_date
                create_by   created_at          last_modified_at
                disabled    groups
        limit : int
            The maximum number of resources to return. The maximum allowed is 50.
        offset : int
            The number of results to skip before starting to return results.
        sort : str
            Field to sort on. String.
            Sortable fields:
                name        description         domain
                subdomain   suppression_reason  suppression_expiration_date
                create_by   created_at          last_modified_at
                disabled    groups
            Use the `.asc` or `.desc` suffix to specify sort direction.
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
            operation_id="QuerySuppressionRules",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def clone_compliance_framework(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Clone an existing compliance framework to create a custom copy.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-policies/CloneComplianceFramework

        Keyword arguments
        -----------------
        ids : str
            The uuid of the compliance framework to clone.
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
            operation_id="CloneComplianceFramework",
            keywords=kwargs,
            params=parameters
            )

    CloneComplianceFramework = clone_compliance_framework
    ReplaceControlRules = replace_control_rules
    GetComplianceControls = get_compliance_controls
    CreateComplianceControl = create_compliance_control
    UpdateComplianceControl = update_compliance_control
    DeleteComplianceControl = delete_compliance_control
    RenameSectionComplianceFramework = rename_section_compliance_framework
    GetComplianceFrameworks = get_compliance_frameworks
    CreateComplianceFramework = create_compliance_framework
    UpdateComplianceFramework = update_compliance_framework
    DeleteComplianceFramework = delete_compliance_framework
    GetEvaluationResult = get_evaluation_result
    GetRuleOverride = get_rule_override
    CreateRuleOverride = create_rule_override
    UpdateRuleOverride = update_rule_override
    DeleteRuleOverride = delete_rule_override
    GetRule = get_rule
    CreateRuleMixin0 = create_rule
    UpdateRule = update_rule
    DeleteRuleMixin0 = delete_rule
    QueryComplianceControls = query_compliance_controls
    QueryComplianceFrameworks = query_compliance_frameworks
    QueryRule = query_rule
    GetRuleInputSchema = get_rule_input_schema
    GetEnrichedAsset = get_enriched_asset
    QuerySuppressionRules = query_suppression_rules
    DeleteSuppressionRules = delete_suppression_rules
    UpdateSuppressionRule = update_suppression_rule
    CreateSuppressionRule = create_suppression_rule
    GetSuppressionRules = get_suppression_rules
