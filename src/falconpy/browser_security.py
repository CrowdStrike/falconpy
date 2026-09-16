"""CrowdStrike Falcon BrowserSecurity API interface class.

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
from ._payload import activate_agents_payload, add_url_domain_list_payload, apply_agent_tasks_payload, classify_domains_payload
from ._payload import create_destination_group_payload, deactivate_agents_payload, query_combined_seraphic_agents_payload
from ._payload import query_destination_groups_payload, query_seraphic_agents_payload, query_seraphic_rules_payload
from ._payload import update_destination_group_payload, update_seraphic_rule_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._browser_security import _browser_security_endpoints as Endpoints


class BrowserSecurity(ServiceClass):
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

    @force_default(defaults=["body"], default_types=["dict"])
    def query_combined_seraphic_agents(self: object,
                                       body: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query agents and return their details in a single call.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/CombinedQueryAgents

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "filter": {
                        "application": [
                            "string"
                        ],
                        "application_name": [
                            "string"
                        ],
                        "application_version": [
                            "string"
                        ],
                        "browser_name": [
                            "string"
                        ],
                        "browser_version": [
                            "string"
                        ],
                        "deployment_method": [
                            "string"
                        ],
                        "email": [
                            "string"
                        ],
                        "first_seen": {
                            "end": "string",
                            "start": "string"
                        },
                        "host_id": [
                            "string"
                        ],
                        "hostname": [
                            "string"
                        ],
                        "id": [
                            "string"
                        ],
                        "last_seen": {
                            "end": "string",
                            "start": "string"
                        },
                        "os_name": [
                            "string"
                        ],
                        "platform": [
                            "string"
                        ],
                        "policy_updated": [
                            "string"
                        ],
                        "protection_type": [
                            "string"
                        ],
                        "status": [
                            "string"
                        ],
                        "username": [
                            "string"
                        ]
                    },
                    "limit": 0,
                    "search": "string",
                    "skip": 0,
                    "sort": [
                        {
                            "field": "string",
                            "order": "string"
                        }
                    ]
                }
        filter : dict
            The filter value.
        limit : int
            The limit value.
        search : str
            The search value.
        skip : int
            The skip value.
        sort : list
            The sort value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = query_combined_seraphic_agents_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CombinedQueryAgents",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def classify_domains(self: object,
                         body: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Classify domains via the Seraphic Enterprise Browser classification engine.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/ClassifyDomains

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "domains": [
                        "string"
                    ]
                }
        domains : list
            The domains value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = classify_domains_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ClassifyDomains",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def activate_agents(self: object,
                        body: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Activate agents by ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/ActivateAgents

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : list
            The ids value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = activate_agents_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ActivateAgents",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def deactivate_agents(self: object,
                          body: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Deactivate agents by ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/DeactivateAgents

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : list
            The ids value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = deactivate_agents_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeactivateAgents",
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def apply_agent_tasks(self: object,
                          body: dict = None,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Apply tasks to a Seraphic Enterprise Browser agent.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/ApplyAgentTasks

        Keyword arguments
        -----------------
        agent_id : str
            The agent ID to apply the tasks to.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "actions": [
                        {
                            "action": "string",
                            "args": [
                                "string"
                            ]
                        }
                    ],
                    "ttl": 0
                }
        actions : list
            The actions value.
        ttl : int
            The ttl value.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = apply_agent_tasks_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ApplyAgentTasks",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_seraphic_agents(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve agents by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/GetAgents

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more resource IDs.
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
            operation_id="GetAgents",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_seraphic_audit_logs(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve audit log entries by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/GetAuditLogsMixin0

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more resource IDs.
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
            operation_id="GetAuditLogsMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_destination_groups(self: object,
                               *args,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve destination groups by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/GetDestinationGroups

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more resource IDs.
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
            operation_id="GetDestinationGroups",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_destination_group(self: object,
                                 body: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a destination group.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/CreateDestinationGroup

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "classification": [
                        "string"
                    ],
                    "countries": [
                        "string"
                    ],
                    "description": "string",
                    "domains": [
                        "string"
                    ],
                    "ipsRange": [
                        "string"
                    ],
                    "match_ips": true,
                    "name": "string",
                    "singleIps": [
                        "string"
                    ],
                    "top_level_domains": [
                        "string"
                    ]
                }
        classification : list
            The classification value.
        countries : list
            The countries value.
        description : str
            The description value.
        domains : list
            The domains value.
        ipsRange : list
            The ipsRange value.
        match_ips : bool
            The match_ips value.
        name : str
            The name value.
        singleIps : list
            The singleIps value.
        top_level_domains : list
            The top_level_domains value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = create_destination_group_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateDestinationGroup",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_destination_group(self: object,
                                 *args,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a destination group.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/DeleteDestinationGroup

        Keyword arguments
        -----------------
        id : str or list[str]
            The resource ID.
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
            operation_id="DeleteDestinationGroup",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_destination_group(self: object,
                                 body: dict = None,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Partial-update a destination group.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/UpdateDestinationGroup

        Keyword arguments
        -----------------
        id : str
            The resource ID.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "classification": [
                        "string"
                    ],
                    "countries": [
                        "string"
                    ],
                    "description": "string",
                    "domains": [
                        "string"
                    ],
                    "ipsRange": [
                        "string"
                    ],
                    "match_ips": true,
                    "name": "string",
                    "singleIps": [
                        "string"
                    ],
                    "top_level_domains": [
                        "string"
                    ]
                }
        classification : list
            The classification value.
        countries : list
            The countries value.
        description : str
            The description value.
        domains : list
            The domains value.
        ipsRange : list
            The ipsRange value.
        match_ips : bool
            The match_ips value.
        name : str
            The name value.
        singleIps : list
            The singleIps value.
        top_level_domains : list
            The top_level_domains value.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_destination_group_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateDestinationGroup",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_extension_analysis(self: object,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve browser-extension risk analysis by store and extension ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/GetExtensionAnalysis

        Keyword arguments
        -----------------
        store : str
            The extension store.
        id : str
            The extension ID.
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
            operation_id="GetExtensionAnalysis",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_seraphic_rules(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve rules by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/GetRules

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more resource IDs.
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
            operation_id="GetRules",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_seraphic_rule(self: object,
                             body: dict = None,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Partial-update a rule (extensions, targets, destination groups, status).

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/UpdateRuleMixin0

        Keyword arguments
        -----------------
        id : str
            The resource ID.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "addExtensionIds": [
                        "string"
                    ],
                    "addExtensionNames": [
                        "string"
                    ],
                    "destinations": "string",
                    "removeExtensionIds": [
                        "string"
                    ],
                    "removeExtensionNames": [
                        "string"
                    ],
                    "status": "string",
                    "targets": "string"
                }
        addExtensionIds : list
            The addExtensionIds value.
        addExtensionNames : list
            The addExtensionNames value.
        destinations : dict
            The destinations value.
        removeExtensionIds : list
            The removeExtensionIds value.
        removeExtensionNames : list
            The removeExtensionNames value.
        status : dict
            The status value.
        targets : dict
            The targets value.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_seraphic_rule_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateRuleMixin0",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_tenant_settings(self: object,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Seraphic Enterprise Browser tenant settings.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/GetTenantSettings

        Keyword arguments
        -----------------
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
            operation_id="GetTenantSettings",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_url_domain_lists(self: object,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve URL/domain integration lists by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/GetUrlDomainLists

        Keyword arguments
        -----------------
        ids : list
            One or more resource IDs.
        skip : int
            Number of items to skip. Default 0.
        limit : int
            Maximum items to return. Default 50.
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
            operation_id="GetUrlDomainLists",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_url_domain_list(self: object,
                            body: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add URLs and domains to an integration list.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/AddUrlDomainList

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "integrationId": "string",
                    "urls": [
                        "string"
                    ]
                }
        integrationId : str
            The integrationId value.
        urls : list
            The urls value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = add_url_domain_list_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AddUrlDomainList",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_url_domain_list(self: object,
                               *args,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete URLs and domains from an integration list.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/DeleteUrlDomainList

        Keyword arguments
        -----------------
        id : str or list[str]
            The resource ID.
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
            operation_id="DeleteUrlDomainList",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def query_seraphic_agents(self: object,
                              body: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query agent IDs by filter, sort and pagination.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/QueryAgents

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "filter": {
                        "application": [
                            "string"
                        ],
                        "application_name": [
                            "string"
                        ],
                        "application_version": [
                            "string"
                        ],
                        "browser_name": [
                            "string"
                        ],
                        "browser_version": [
                            "string"
                        ],
                        "deployment_method": [
                            "string"
                        ],
                        "email": [
                            "string"
                        ],
                        "first_seen": {
                            "end": "string",
                            "start": "string"
                        },
                        "host_id": [
                            "string"
                        ],
                        "hostname": [
                            "string"
                        ],
                        "id": [
                            "string"
                        ],
                        "last_seen": {
                            "end": "string",
                            "start": "string"
                        },
                        "os_name": [
                            "string"
                        ],
                        "platform": [
                            "string"
                        ],
                        "policy_updated": [
                            "string"
                        ],
                        "protection_type": [
                            "string"
                        ],
                        "status": [
                            "string"
                        ],
                        "username": [
                            "string"
                        ]
                    },
                    "limit": 0,
                    "search": "string",
                    "skip": 0,
                    "sort": [
                        {
                            "field": "string",
                            "order": "string"
                        }
                    ]
                }
        filter : dict
            The filter value.
        limit : int
            The limit value.
        search : str
            The search value.
        skip : int
            The skip value.
        sort : list
            The sort value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = query_seraphic_agents_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryAgents",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def query_destination_groups(self: object,
                                 body: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query destination groups by filter, sort and pagination.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/QueryDestinationGroups

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "exclude": [
                        "string"
                    ],
                    "filter": "string",
                    "limit": 0,
                    "search": "string",
                    "skip": 0,
                    "sort": [
                        "string"
                    ]
                }
        exclude : list
            The exclude value.
        filter : dict
            The filter value.
        limit : int
            The limit value.
        search : str
            The search value.
        skip : int
            The skip value.
        sort : list
            The sort value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = query_destination_groups_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryDestinationGroups",
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def query_seraphic_rules(self: object,
                             body: dict = None,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query rules within a category by filter, sort and pagination.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/browser-security/QueryRulesMixin0

        Keyword arguments
        -----------------
        category : str
            The rule category to query.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "advanced_filter": "string",
                    "exclude": [
                        "string"
                    ],
                    "filter": "string",
                    "limit": 0,
                    "rule_ids": [
                        "string"
                    ],
                    "search": "string",
                    "skip": 0,
                    "sort": [
                        "string"
                    ]
                }
        advanced_filter : dict
            The advanced_filter value.
        exclude : list
            The exclude value.
        filter : dict
            The filter value.
        limit : int
            The limit value.
        rule_ids : list
            The rule_ids value.
        search : str
            The search value.
        skip : int
            The skip value.
        sort : list
            The sort value.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = query_seraphic_rules_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryRulesMixin0",
            keywords=kwargs,
            params=parameters,
            body=body
            )
    CombinedQueryAgents = query_combined_seraphic_agents
    ClassifyDomains = classify_domains
    ActivateAgents = activate_agents
    DeactivateAgents = deactivate_agents
    ApplyAgentTasks = apply_agent_tasks
    GetAgents = get_seraphic_agents
    GetAuditLogsMixin0 = get_seraphic_audit_logs
    GetDestinationGroups = get_destination_groups
    CreateDestinationGroup = create_destination_group
    DeleteDestinationGroup = delete_destination_group
    UpdateDestinationGroup = update_destination_group
    GetExtensionAnalysis = get_extension_analysis
    GetRules = get_seraphic_rules
    UpdateRuleMixin0 = update_seraphic_rule
    GetTenantSettings = get_tenant_settings
    GetUrlDomainLists = get_url_domain_lists
    AddUrlDomainList = add_url_domain_list
    DeleteUrlDomainList = delete_url_domain_list
    QueryAgents = query_seraphic_agents
    QueryDestinationGroups = query_destination_groups
    QueryRulesMixin0 = query_seraphic_rules
