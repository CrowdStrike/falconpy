"""Falcon Custom Indicators of Attack API Interface Class.

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
from ._payload import ioa_custom_payload, generic_payload_list
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._custom_ioa import _custom_ioa_endpoints as Endpoints


class CustomIOA(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (OAuth2.token())
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_patterns(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get pattern severities by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-patterns

        Keyword arguments
        -----------------
        ids : str or list[str]
            Pattern IDs.
        parameters : dict
            full parameters payload, not required if using `ids` keyword.

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
            operation_id="get_patterns",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_platforms(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get platforms by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-platformsMixin0

        Keyword arguments
        -----------------
        ids : str or list[str]
            Platform IDs.
        parameters : dict
            full parameters payload, not required if using `ids` keyword.

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
            operation_id="get_platformsMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_groups(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get rule groups by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rule-groupsMixin0

        Keyword arguments
        -----------------
        ids : str or list[str]
            Rule group IDs.
        parameters : dict
            full parameters payload, not required if using `ids` keyword.

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
            operation_id="get_rule_groupsMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_rule_group(self: object,
                          body: dict = None,
                          cs_username: str = None,  # pylint: disable=W0613  # deprecated
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a rule group for a platform with a name and an optional description.

        Returns the rule group.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/create-rule-groupMixin0

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
        comment : str
            Comment for the rule group.
        description : str
            Rule group description.
        name : str
            Name of the rule group.
        platform : str
            Platform this rule group applies to. Allowed values: `windows`, `mac`, `linux`

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ioa_custom_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_rule_groupMixin0",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule_groups(self: object,
                           *args,
                           cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete rule groups by ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/delete-rule-groupsMixin0

        Keyword arguments
        -----------------
        comment : str
            Explains why the rule group is being deleted.
        ids : str or list[str]
            Rule group IDs to be deleted.
        parameters : dict
            full parameters payload, not required if using `ids` keyword.

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
            operation_id="delete_rule_groupsMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_rule_group(self: object,
                          body: dict = None,
                          cs_username: str = None,  # pylint: disable=W0613  # deprecated
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a rule group.

        The following properties can be modified: `name`, `description`, `enabled`.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/update-rule-groupMixin0

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "comment": "string",
                    "description": "string",
                    "enabled": true,
                    "id": "string",
                    "name": "string",
                    "rulegroup_version": 0
                }
        comment : str
            Comment for the rule group.
        description : str
            Rule group description.
        enabled : bool
            Flag indicating if the group is enabled.
        id : str
            ID of the rule group.
        name : str
            Name of the rule group.
        rulegroup_version : int
            Rule group version to modify.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ioa_custom_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_rule_groupMixin0",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_types(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get rule types by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rule-types

        Keyword arguments
        -----------------
        ids : str or list[str]
            Rule type IDs.
        parameters : dict
            full parameters payload, not required if using `ids` keyword.

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
            operation_id="get_rule_types",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_rules_get(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get rules by ID and optionally version in the following format: ID[:version].

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rules-get

        Keyword arguments
        -----------------
        body : dict
            full body payload in JSON format, not required if using `ids` keyword is used.
        ids : str or list[str]
            Rule IDs to retrieve.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = generic_payload_list(submitted_keywords=kwargs, payload_value="ids")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_rules_get",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get rules by ID and optionally version in the following format: ID[:version].

        The max number of IDs is constrained by URL size.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/get-rulesMixin0

        Keyword arguments
        -----------------
        ids : str or list[str]
            Rule IDs.
        parameters : dict
            full parameters payload, not required if using `ids` keyword.

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
            operation_id="get_rulesMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_rule(self: object,
                    body: dict = None,
                    cs_username: str = None,  # pylint: disable=W0613  # deprecated
                    **kwargs
                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a rule within a rule group. Returns the rule.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/create-rule

        Keyword arguments
        -----------------
        body : dict
            full body payload in JSON format, not required if using other keywords.
                {
                    "comment": "string",
                    "description": "string",
                    "disposition_id": 0,
                    "field_values": [
                        {
                            "final_value": "string",
                            "label": "string",
                            "name": "string",
                            "type": "string",
                            "value": "string",
                            "values": [
                                {
                                    "label": "string",
                                    "value": "string"
                                }
                            ]
                        }
                    ],
                    "name": "string",
                    "pattern_severity": "string",
                    "rulegroup_id": "string",
                    "ruletype_id": "string"
                }
        comment : str
            Comment related to this update.
        description : str
            Rule description.
        disposition_id : int
            Disposition ID.
        field_values : list
            Rule values represented as an object. Dictionary.
            {
                "final_value": "string",
                "label": "string",
                "name": "string",
                "type": "string",
                "value": "string",
                "values": [
                    {
                        "label": "string",
                        "value": "string"
                    }
                ]
            }
        name : str
            Name of the rule.
        pattern_severity : str
            Severity.
        rulegroup_id : str
            ID of the rule group.
        ruletype_id : str
            ID of the rule type.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ioa_custom_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_rule",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rules(self: object,
                     cs_username: str = None,  # pylint: disable=W0613  # deprecated
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete rules from a rule group by ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/delete-rules

        Keyword arguments
        -----------------
        comment : str
            Explains why the entity is being deleted.
        ids : str or list[str]
            Rule IDs to be deleted.
        parameters : dict
            full parameters payload, not required if using `ids` keyword.
        rule_group_id : str
            The parent rule group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="delete_rules",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_rules(self: object,
                     body: dict = None,
                     cs_username: str = None,  # pylint: disable=W0613  # deprecated
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update rules within a rule group. Return the updated rules.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/update-rules

        Keyword arguments
        -----------------
        body : dict
            full body payload in JSON format, not required if using other keywords.
                {
                    "comment": "string",
                    "rule_updates": [
                        {
                            "description": "string",
                            "disposition_id": 0,
                            "enabled": true,
                            "field_values": [
                                {
                                    "final_value": "string",
                                    "label": "string",
                                    "name": "string",
                                    "type": "string",
                                    "value": "string",
                                    "values": [
                                        {
                                            "label": "string",
                                            "value": "string"
                                        }
                                    ]
                                }
                            ],
                            "instance_id": "string",
                            "name": "string",
                            "pattern_severity": "string",
                            "rulegroup_version": 0
                        }
                    ],
                    "rulegroup_id": "string",
                    "rulegroup_version": 0
                }
        comment : str
            Comment related to this update.
        rulegroup_id : str
            ID of the rule group.
        rule_updates : list
            JSON dictionary representing the rule updates to
            be performed. Only one rule update can be done
            in this manner. Dictionary.
            {
                "description": "string",
                "disposition_id": 0,
                "enabled": true,
                "field_values": [
                    {
                        "final_value": "string",
                        "label": "string",
                        "name": "string",
                        "type": "string",
                        "value": "string",
                        "values": [
                            {
                                "label": "string",
                                "value": "string"
                            }
                        ]
                    }
                ],
                "instance_id": "string",
                "name": "string",
                "pattern_severity": "string",
                "rulegroup_version": 0
            }
        rulegroup_version : int
            Version of the rule group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ioa_custom_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_rules",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_rules_v2(self: object,
                        body: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update rules within a rule group. Return the updated rules.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/update-rules-v2

        Keyword arguments
        -----------------
        body : dict
            full body payload in JSON format, not required if using other keywords.
                {
                    "comment": "string",
                    "rule_updates": [
                        {
                            "description": "string",
                            "disposition_id": 0,
                            "enabled": true,
                            "field_values": [
                                {
                                    "final_value": "string",
                                    "label": "string",
                                    "name": "string",
                                    "type": "string",
                                    "value": "string",
                                    "values": [
                                        {
                                            "label": "string",
                                            "value": "string"
                                        }
                                    ]
                                }
                            ],
                            "instance_id": "string",
                            "name": "string",
                            "pattern_severity": "string",
                            "rulegroup_version": 0
                        }
                    ],
                    "rulegroup_id": "string",
                    "rulegroup_version": 0
                }
        comment : str
            Comment related to this update.
        rulegroup_id : str
            ID of the rule group.
        rule_updates : list
            JSON dictionary representing the rule updates to
            be performed. Only one rule update can be done
            in this manner. Dictionary.
            {
                "description": "string",
                "disposition_id": 0,
                "enabled": true,
                "field_values": [
                    {
                        "final_value": "string",
                        "label": "string",
                        "name": "string",
                        "type": "string",
                        "value": "string",
                        "values": [
                            {
                                "label": "string",
                                "value": "string"
                            }
                        ]
                    }
                ],
                "instance_id": "string",
                "name": "string",
                "pattern_severity": "string",
                "rulegroup_version": 0
            }
        rulegroup_version : int
            Version of the rule group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ioa_custom_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_rules_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def validate(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Validate field values and check for matches if a test string is provided.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/validate

        Keyword arguments
        -----------------
        body : dict
            full body payload in JSON format, not required if using other keywords.
                {
                    "fields": [
                        {
                            "name": "string",
                            "test_data": "string",
                            "type": "string",
                            "values": [
                                {
                                    "label": "string",
                                    "value": "string"
                                }
                            ]
                        }
                    ]
                }
        fields : list
            List of fields to validate. List of dictionaries.
            {
                "name": "string",
                "test_data": "string",
                "type": "string",
                "values": [
                    {
                        "label": "string",
                        "value": "string"
                    }
                ]
            }

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'fields'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = generic_payload_list(submitted_keywords=kwargs, payload_value="fields")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="validate",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_patterns(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all pattern severity IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-patterns

        Keyword arguments
        -----------------
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
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
            operation_id="query_patterns",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_platforms(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all platform IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-platformsMixin0

        Keyword arguments
        -----------------
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
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
            operation_id="query_platformsMixin0",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_groups_full(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find all rule groups matching the query with optional filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-groups-full

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying the filter parameters. String.
            Filter term criteria:
            enabled                   rules.name
            platform                  rules.description
            name                      rules.pattern_severity
            description               rules.ruletype_name
            rules.action_label        rules.enabled
            Filter range criteria:
            created_on
            modified_on (use any common date format, e.g. '2010-05-15T14:55:21.892315096Z')
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Match query criteria, which includes all the filter string fields.
        sort : str
            FQL syntax specifying sort criteria. String.
            Possible order by fields:
            created_by              enabled
            created_on              name
            modified_by             description
            modified_on

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rule_groups_full",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_groups(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find all rule group IDs matching the query with optional filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-groupsMixin0

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying the filter parameters. String.
            Filter term criteria:
            enabled                   rules.name
            platform                  rules.description
            name                      rules.pattern_severity
            description               rules.ruletype_name
            rules.action_label        rules.enabled
            Filter range criteria:
            created_on
            modified_on (use any common date format, e.g. '2010-05-15T14:55:21.892315096Z')
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Match query criteria, which includes all the filter string fields.
        sort : str
            FQL syntax specifying sort criteria. String.
            Possible order by fields:
            created_by              enabled
            created_on              name
            modified_by             description
            modified_on

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rule_groupsMixin0",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_types(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all rule type IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rule-types

        Keyword arguments
        -----------------
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
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
            operation_id="query_rule_types",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rules(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find all rule IDs matching the query with optional filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa/query-rulesMixin0

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying the filter parameters. String.
            Filter term criteria:
            enabled                   rules.name
            platform                  rules.description
            name                      rules.pattern_severity
            description               rules.ruletype_name
            rules.action_label        rules.enabled
            Filter range criteria:
            created_on
            modified_on (use any common date format, e.g. '2010-05-15T14:55:21.892315096Z')
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Match query criteria, which includes all the filter string fields.
        sort : str
            FQL syntax specifying sort criteria. String.
            Possible order by fields:
            rules.ruletype_name                 rules.created_on
            rules.enabled                       rules.current_version.description
            rules.created_by                    rules.current_version.pattern_severity
            rules.current_version.name          rules.current_version.action_label
            rules.current_version.modified_by   rules.current_version.modified_on

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rulesMixin0",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    get_platformsMixin0 = get_platforms
    get_rule_groupsMixin0 = get_rule_groups
    create_rule_groupMixin0 = create_rule_group
    delete_rule_groupMixin0 = delete_rule_groups  # Typo fix
    delete_rule_groupsMixin0 = delete_rule_groups
    update_rule_groupMixin0 = update_rule_group
    get_rulesMixin0 = get_rules
    query_platformsMixin0 = query_platforms
    query_rule_groupsMixin0 = query_rule_groups
    query_rulesMixin0 = query_rules


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Custom_IOA = CustomIOA  # pylint: disable=C0103
