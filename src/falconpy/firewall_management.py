"""CrowdStrike Falcon Firewall Management API interface class.

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
# pylint: disable=C0302,R0904
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import (
    aggregate_payload,
    firewall_container_payload,
    firewall_rule_group_validation_payload,
    firewall_rule_group_payload,
    firewall_rule_group_update_payload,
    firewall_filepattern_payload,
    network_locations_metadata_payload,
    network_locations_create_payload
    )
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._firewall_management import _firewall_management_endpoints as Endpoints


class FirewallManagement(ServiceClass):
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

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_events(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate events for customer.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_events

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "exclude": "string",
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "include": "string",
                        "interval": "string",
                        "max_doc_count": 0,
                        "min_doc_count": 0,
                        "missing": "string",
                        "name": "string",
                        "q": "string",
                        "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                        ],
                        "size": 0,
                        "sort": "string",
                        "sub_aggregates": [
                            null
                        ],
                        "time_zone": "string",
                        "type": "string"
                    }
                ]
        date_ranges : list[dict]
            If peforming a date range query specify the from and to date ranges.
            These can be in common date formats like 2019-07-18 or now.
        exclude : str
            Fields to exclude.
        field : str
            Term you want to aggregate on. If doing a date_range query,
            this is the date field you want to apply the date ranges to.
        filter : str
            Optional filter criteria in the form of an FQL query.
            For more information about FQL queries, see our FQL documentation in Falcon.
        from : int
        include : str
            Fields to include.
        interval : str
        max_doc_count : int
            Maximum number of documents.
        min_doc_count : int
            Minimum number of documents.
        missing : str
        name : str
            Scan name.
        q : str
            FQL syntax.
        ranges : list[dict]
        size : int
        sort : str
            FQL syntax.
        sub_aggregates : list[str]
        time_zone : str
        type : str
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_events",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_policy_rules(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate rules within a policy for customer.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_policy_rules

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "exclude": "string",
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "include": "string",
                        "interval": "string",
                        "max_doc_count": 0,
                        "min_doc_count": 0,
                        "missing": "string",
                        "name": "string",
                        "q": "string",
                        "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                        ],
                        "size": 0,
                        "sort": "string",
                        "sub_aggregates": [
                            null
                        ],
                        "time_zone": "string",
                        "type": "string"
                    }
                ]
        date_ranges : list[dict]
            If peforming a date range query specify the from and to date ranges.
            These can be in common date formats like 2019-07-18 or now.
        exclude : str
            Fields to exclude.
        field : str
            Term you want to aggregate on. If doing a date_range query,
            this is the date field you want to apply the date ranges to.
        filter : str
            Optional filter criteria in the form of an FQL query.
            For more information about FQL queries, see our FQL documentation in Falcon.
        from : int
        include : str
            Fields to include.
        interval : str
        max_doc_count : int
            Maximum number of documents.
        min_doc_count : int
            Minimum number of documents.
        missing : str
        name : str
            Scan name.
        q : str
            FQL syntax.
        ranges : list[dict]
        size : int
        sort : str
            FQL syntax.
        sub_aggregates : list[str]
        time_zone : str
        type : str
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_policy_rules",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_rule_groups(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate rule groups for customer.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rule_groups

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "exclude": "string",
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "include": "string",
                        "interval": "string",
                        "max_doc_count": 0,
                        "min_doc_count": 0,
                        "missing": "string",
                        "name": "string",
                        "q": "string",
                        "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                        ],
                        "size": 0,
                        "sort": "string",
                        "sub_aggregates": [
                            null
                        ],
                        "time_zone": "string",
                        "type": "string"
                    }
                ]
        date_ranges : list[dict]
            If peforming a date range query specify the from and to date ranges.
            These can be in common date formats like 2019-07-18 or now.
        exclude : str
            Fields to exclude.
        field : str
            Term you want to aggregate on. If doing a date_range query,
            this is the date field you want to apply the date ranges to.
        filter : str
            Optional filter criteria in the form of an FQL query.
            For more information about FQL queries, see our FQL documentation in Falcon.
        from : int
        include : str
            Fields to include.
        interval : str
        max_doc_count : int
            Maximum number of documents.
        min_doc_count : int
            Minimum number of documents.
        missing : str
        name : str
            Scan name.
        q : str
            FQL syntax.
        ranges : list[dict]
        size : int
        sort : str
            FQL syntax.
        sub_aggregates : list[str]
        time_zone : str
        type : str
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_rule_groups",
            body=body
            )

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_rules(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate rules for customer.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/aggregate_rules

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "exclude": "string",
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "include": "string",
                        "interval": "string",
                        "max_doc_count": 0,
                        "min_doc_count": 0,
                        "missing": "string",
                        "name": "string",
                        "q": "string",
                        "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                        ],
                        "size": 0,
                        "sort": "string",
                        "sub_aggregates": [
                            null
                        ],
                        "time_zone": "string",
                        "type": "string"
                    }
                ]
        date_ranges : list[dict]
            If peforming a date range query specify the from and to date ranges.
            These can be in common date formats like 2019-07-18 or now.
        exclude : str
            Fields to exclude.
        field : str
            Term you want to aggregate on. If doing a date_range query,
            this is the date field you want to apply the date ranges to.
        filter : str
            Optional filter criteria in the form of an FQL query.
            For more information about FQL queries, see our FQL documentation in Falcon.
        from : int
        include : str
            Fields to include.
        interval : str
        max_doc_count : int
            Maximum number of documents.
        min_doc_count : int
            Minimum number of documents.
        missing : str
        name : str
            Scan name.
        q : str
            FQL syntax.
        ranges : list[dict]
        size : int
        sort : str
            FQL syntax.
        sub_aggregates : list[str]
        time_zone : str
        type : str
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_rules",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_events(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get events entities by ID and optionally version.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_events

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the events to retrieve.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="get_events",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_firewall_fields(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the firewall field specifications by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_firewall_fields

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the rule types to retrieve.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="get_firewall_fields",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_network_locations_details(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get network location entities by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rule_groups

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the event(s) to retrieve.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="get_network_locations_details",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_network_locations_metadata(self: object,
                                          body: dict = None,
                                          parameters: dict = None,
                                          **kwargs
                                          ) -> dict:
        """Update the network locations metadata such as polling intervals for the cid.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update-network-locations-metadata

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "cid": "string",
                    "dns_resolution_targets_polling_interval": 0,
                    "https_reachable_hosts_polling_interval": 0,
                    "icmp_request_targets_polling_interval": 0,
                    "location_precedence": [
                        "string"
                    ]
                }
        cid : str
            CID for the location.
        comment : str
            Audit log comment for the action performed.
        dns_resolution_targets_polling_interval : int
        https_reachable_hsots_polling_interval : int
        icmp_request_targets_polling_interval : int
        location_precedencee : list[str]
            Reorder precedence of network locations.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = network_locations_metadata_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_network_locations_metadata",
            body=body,
            params=parameters
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_network_locations_precedence(self: object,
                                            body: dict = None,
                                            parameters: dict = None,
                                            **kwargs
                                            ) -> dict:
        """Update the network locations precedence according to the list of IDs provided.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update-network-locations-precedence

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "cid": "string",
                    "location_precedence": [
                        "string"
                    ]
                }
        cid : str
            CID for the location.
        comment : str
            Audit log comment for the action performed.
        location_precedencee : list[str]
            Reorder precedence of network locations.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = network_locations_metadata_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_network_locations_precedence",
            body=body,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_network_locations(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get network location entities by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get-network-locations

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the location(s) to retrieve.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="get_network_locations",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def create_network_locations(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
        """Create new network locations provided and return the ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/create-network-locations

        Keyword arguments
        -----------------
        add_fw_rules : bool
            Flag to indicate if the cloned locatoin needs to be added to the same
            firewall rules that encompass the original location.
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "connection_types": {
                        "wired": true,
                        "wireless": {
                        "enabled": true,
                        "require_encryption": true,
                        "ssids": [
                                "string"
                            ]
                        }
                    },
                    "default_gateways": [
                        "string"
                    ],
                    "description": "string",
                    "dhcp_servers": [
                            "string"
                        ],
                    "dns_resolution_targets": {
                        "targets": [
                            {
                                "hostname": "string",
                                "ip_match": [
                                    "string"
                                ]
                            }
                        ]
                    },
                    "dns_servers": [
                            "string"
                        ],
                    "enabled": true,
                    "host_addresses": [
                            "string"
                        ],
                    "https_reachable_hosts": {
                        "hostnames": [
                            "string"
                        ]
                    },
                    "icmp_request_targets": {
                        "targets": [
                            "string"
                        ]
                    },
                    "name": "string"
                }
        clone_id : str
            A network location ID from which to copy rules. If this is provided then all
            other keywords except `add_fw_rules` and `comment` are ignored.
        comment : str
            Audit log comment for this action.
        connection_types : dict
            Connections available at the location.
        default_gateways : str or list[str]
            List of available default gateways.
        description : str
            Description of the location.
        dhcp_servers : str or list[str]
            List of available DHCP servers.
        dns_resolution_targets : dict
            Dictionary containing a list of DNS resolution targets.
        dns_servers : str or list[str]
            List of available DNS servers.
        enabled : bool
            Flag indicating if this location is enabled.
        host_addresses : str or list[str]
            List of available host addresses.
        https_reachable_hosts : dict
            Dictionary of hosts reachable via HTTPS at this location.
        icmp_request_targets : dict
            Dictionary of targets for ICMP monitoring requests.
        name : str
            Name for this rule.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = network_locations_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_network_locations",
            keywords=kwargs,
            body=body,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def upsert_network_locations(self: object, body: dict = None, **kwargs) -> dict:
        """Update the network locations provided and return the ID.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/upsert-network-locations

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "connection_types": {
                        "wired": true,
                        "wireless": {
                        "enabled": true,
                        "require_encryption": true,
                        "ssids": [
                            "string"
                            ]
                        }
                    },
                    "created_by": "string",
                    "created_on": "string",
                    "default_gateways": [
                        "string"
                    ],
                    "description": "string",
                    "dhcp_servers": [
                        "string"
                        ],
                    "dns_resolution_targets": {
                        "targets": [
                            {
                                "hostname": "string",
                                "ip_match": [
                                    "string"
                                ]
                            }
                        ]
                    },
                    "dns_servers": [
                        "string"
                        ],
                    "enabled": true,
                    "host_addresses": [
                        "string"
                        ],
                    "https_reachable_hosts": {
                        "hostnames": [
                            "string"
                        ]
                    },
                    "icmp_request_targets": {
                        "targets": [
                        "string"
                        ]
                    },
                    "name": "string",
                    "id": "string",
                    "modified_by": "string",
                    "modified_on": "string"
                }
        comment : str
            Audit log comment for this action.
        connection_types : dict
            Connections available at the location.
        created_on : str
            Timestamp.
        created_by : str
        default_gateways : str or list[str]
            List of available default gateways.
        description : str
            Description of the location.
        dhcp_servers : str or list[str]
            List of available DHCP servers.
        dns_resolution_targets : dict
            Dictionary containing a list of DNS resolution targets.
        dns_servers : str or list[str]
            List of available DNS servers.
        enabled : bool
            Flag indicating if this location is enabled.
        host_addresses : str or list[str]
            List of available host addresses.
        https_reachable_hosts : dict
            Dictionary of hosts reachable via HTTPS at this location.
        icmp_request_targets : dict
            Dictionary of targets for ICMP monitoring requests.
        id : str
            Network location ID to be updated.
        modified_by : str
            User UUID that modified this location.
        modified_on : str
            UTC formatted date string of the update.
        name : str
            Name for this rule.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = network_locations_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="upsert_network_locations",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_network_locations(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
        """Create new network locations provided and return the ID.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update-network-locations

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "connection_types": {
                        "wired": true,
                        "wireless": {
                        "enabled": true,
                        "require_encryption": true,
                        "ssids": [
                            "string"
                            ]
                        }
                    },
                    "created_by": "string",
                    "created_on": "string",
                    "default_gateways": [
                        "string"
                    ],
                    "description": "string",
                    "dhcp_servers": [
                        "string"
                        ],
                    "dns_resolution_targets": {
                        "targets": [
                            {
                                "hostname": "string",
                                "ip_match": [
                                    "string"
                                ]
                            }
                        ]
                    },
                    "dns_servers": [
                        "string"
                        ],
                    "enabled": true,
                    "host_addresses": [
                        "string"
                        ],
                    "https_reachable_hosts": {
                        "hostnames": [
                            "string"
                        ]
                    },
                    "icmp_request_targets": {
                        "targets": [
                        "string"
                        ]
                    },
                    "name": "string",
                    "id": "string",
                    "modified_by": "string",
                    "modified_on": "string"
                }
        comment : str
            Audit log comment for this action.
        connection_types : dict
            Connections available at the location.
        created_on : str
            Timestamp.
        created_by : str
        default_gateways : str or list[str]
            List of available default gateways.
        description : str
            Description of the location.
        dhcp_servers : str or list[str]
            List of available DHCP servers.
        dns_resolution_targets : dict
            Dictionary containing a list of DNS resolution targets.
        dns_servers : str or list[str]
            List of available DNS servers.
        enabled : bool
            Flag indicating if this location is enabled.
        host_addresses : str or list[str]
            List of available host addresses.
        https_reachable_hosts : dict
            Dictionary of hosts reachable via HTTPS at this location.
        icmp_request_targets : dict
            Dictionary of targets for ICMP monitoring requests.
        id : str
            Network location ID to be updated.
        modified_by : str
            User UUID that modified this location.
        modified_on : str
            UTC formatted date string of the update.
        name : str
            Name for this rule.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = network_locations_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_network_locations",
            keywords=kwargs,
            body=body,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_network_locations(self: object,
                                 *args,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> dict:
        """Delete network location entities by ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/delete-network-locations

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the network location(s) to delete.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="delete_network_locations",
            params=handle_single_argument(args, parameters, "ids"),
            keywords=kwargs
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_platforms(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get platforms by ID, e.g., windows or mac or droid.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_platforms

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the platforms to retrieve.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="get_platforms",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy_containers(self: object,
                              *args,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get policy container entities by policy ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_policy_containers

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the policy container(s) to retrieve.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="get_policy_containers",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_policy_container_v1(self: object,
                                   body: dict = None,
                                   cs_username: str = None,  # pylint: disable=W0613  # deprecated
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an identified policy container.

        **DEPRECATED**

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update-policy-container-v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "default_inbound": "string",
                    "default_outbound": "string",
                    "enforce": true,
                    "is_default_policy": true,
                    "local_logging": true,
                    "platform_id": "string",
                    "policy_id": "string",
                    "rule_group_ids": [
                        "string"
                    ],
                    "test_mode": true,
                    "tracking": "string"
                }
        default_inbound : str
            Default inbound.
        default_outbound : str
            Default outbound.
        enforce : bool
            Flag indicating if the policy is enforced.
        is_default_policy : bool
            Flag indicating if the policy is the default.
        local_logging : bool
            Flag indicating if local logging should be enabled.
        platform_id : str
            Platform ID. (`windows`, `mac`, `linux`)
        policy_id : str
            ID of the policy to be updated.
        rule_group_ids : str or list[str]
            Rule group IDs this policy applies to.
        test_mode : bool
            Flag indicating if this policy is in test mode.
        tracking : str
            Tracking.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = firewall_container_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_policy_container_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_policy_container(self: object,
                                body: dict,
                                cs_username: str = None,  # pylint: disable=W0613  # deprecated
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an identified policy container.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update-policy-container

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "default_inbound": "string",
                    "default_outbound": "string",
                    "enforce": boolean,
                    "is_default_policy": boolean,
                    "local_logging": boolean
                    "platform_id": "string",
                    "policy_id": "string",
                    "rule_group_ids": [
                        "string"
                    ],
                    "test_mode": boolean,
                    "tracking": "string"
                }
        default_inbound : str
            Default inbound.
        default_outbound : str
            Default outbound.
        enforce : bool
            Flag indicating if the policy is enforced.
        is_default_policy : bool
            Flag indicating if the policy is the default.
        local_logging : bool
            Flag indicating if local logging functionality is enabled.
        platform_id : str
            Platform ID. (`windows`, `mac`, `linux`)
        policy_id : str
            ID of the policy to be updated.
        rule_group_ids : str or list[str]
            Rule group IDs this policy applies to.
        test_mode : bool
            Flag indicating if this policy is in test mode.
        tracking : str
            Tracking.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = firewall_container_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_policy_container",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_groups(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get rule group entities by ID.

        These groups do not contain their rule entites, just the rule IDs in precedence order.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rule_groups

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the rule group(s) to retrieve.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="get_rule_groups",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def create_rule_group(self: object,
                          body: dict = None,
                          cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create new rule group on a platform for a customer with a name and description.

        Returns the ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/create-rule-group

        Keyword arguments
        -----------------
        action : str
            Rule action to perform. String. Overridden if 'rules' keyword is provided.
        address_family : str
            Address type, String. Either 'IP4', 'IP6' or 'NONE'.
            Overridden if 'rules' keyword is provided.
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "description": "string",
                    "enabled": true,
                    "name": "string",
                    "platform": "string",
                    "rules": [
                        {
                            "action": "string",
                            "address_family": "string",
                            "description": "string",
                            "direction": "string",
                            "enabled": true,
                            "fields": [
                                {
                                    "final_value": "string",
                                    "label": "string",
                                    "name": "string",
                                    "type": "string",
                                    "value": "string",
                                    "values": [
                                        "string"
                                    ]
                                }
                            ],
                            "icmp": {
                                "icmp_code": "string",
                                "icmp_type": "string"
                            },
                            "local_address": [
                                {
                                    "address": "string",
                                    "netmask": 0
                                }
                            ],
                            "local_port": [
                                {
                                    "end": 0,
                                    "start": 0
                                }
                            ],
                            "log": true,
                            "monitor": {
                                "count": "string",
                                "period_ms": "string"
                            },
                            "name": "string",
                            "protocol": "string",
                            "remote_address": [
                                {
                                    "address": "string",
                                    "netmask": 0
                                }
                            ],
                            "remote_port": [
                                {
                                    "end": 0,
                                    "start": 0
                                }
                            ],
                            "temp_id": "string"
                        }
                    ]
                }
        clone_id : str
            A rule group ID from which to copy rules.
            If this is provided the `rules` keyword is ignored.
        comment : str
            Audit log comment for this action.
        description : str
            Rule group description.
        direction : str
            Traffic direction for created rule. String. Either 'IN', 'OUT' or 'BOTH'.
            Overridden if 'rules' keyword is provided.
        enabled : bool
            Flag indicating if the rule group is enabled.
        fields : str
            Fields to impact. Dictionary or list of dictionaries.
            Overridden if 'rules' keyword is provided.
        icmp : str
            ICMP protocol options. Dictionary.  Overridden if 'rules' keyword is provided.
        library : str
            If this flag is set to true then the rules will be cloned from the
            clone_id from the CrowdStrike Firewall Rule Groups Library.
        local_address : str
            Local address and netmask detail. Dictionary or list of dictionaries.
            Overridden if 'rules' keyword is provided.
        local_port : str
            Local port range. Dictionary or list of dictionaries.
            Overridden if 'rules' keyword is provided.
        log : str
            Log rule matches. Boolean. Overridden if 'rules' keyword is provided.
        name : str
            Rule group name.
        monitor : str
            Monitor count / period. Dictionary. Overridden if 'rules' keyword is provided.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        platform : str
            OS platform covered by rule.
        protocol : str
            Integer protocol specified. Integer. Overridden if 'rules' keyword is provided.
            (TCP = 6, UDP = 17)
        remote_address : str
            Remote address and netmask detail. Dictionary or list of dictionaries.
            Overridden if 'rules' keyword is provided.
        remote_port : str
            Remote port range. Dictionary or list of dictionaries.
            Overridden if 'rules' keyword is provided.
        rule_description : str
            Description for created rule. String.
            Overridden if 'rules' keyword is provided.
        rule_enabled : str
            Enablement status for new rule. Boolean.
            Overridden if 'rules' keyword is provided.
        rule_name : str
            Name for the new rule. String.  Overridden if 'rules' keyword is provided.
        rules : list
            Rule(s) in JSON format. Single dictionary or List of dictionaries.
            {
                "action": "string",
                "address_family": "string",
                "description": "string",
                "direction": "string",
                "enabled": true,
                "fields": [
                    {
                        "final_value": "string",
                        "label": "string",
                        "name": "string",
                        "type": "string",
                        "value": "string",
                        "values": [
                            "string"
                        ]
                    }
                ],
                "icmp": {
                    "icmp_code": "string",
                    "icmp_type": "string"
                },
                "local_address": [
                    {
                        "address": "string",
                        "netmask": 0
                    }
                ],
                "local_port": [
                    {
                        "end": 0,
                        "start": 0
                    }
                ],
                "log": true,
                "monitor": {
                    "count": "string",
                    "period_ms": "string"
                },
                "name": "string",
                "protocol": "string",
                "remote_address": [
                    {
                        "address": "string",
                        "netmask": 0
                    }
                ],
                "remote_port": [
                    {
                        "end": 0,
                        "start": 0
                    }
                ],
                "temp_id": "string"
            }
        temp_id : str
            String to use for rule temporary ID. String.
            Overridden if 'rules' keyword is provided.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = firewall_rule_group_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_rule_group",
            body=body,
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_rule_groups(self: object,
                           *args,
                           cs_username: str = None,  # pylint: disable=W0613  # cs_username is deprecated
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete rule group entities by ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/delete-rule-groups

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the rule group(s) to delete.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="delete_rule_groups",
            params=handle_single_argument(args, parameters, "ids"),
            keywords=kwargs
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def update_rule_group(self: object,
                          body: dict = None,
                          cs_username: str = None,  # pylint: disable=W0613  # deprecated
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update name, description, or enabled status of a rule group and underlying rules.

        Can also create, edit, delete, or reorder rules.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update-rule-group

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "diff_operations": [
                        {
                            "from": "string",
                            "op": "string",
                            "path": "string"
                        }
                    ],
                    "diff_type": "string",
                    "id": "string",
                    "rule_ids": [
                        "string"
                    ],
                    "rule_versions": [
                        0
                    ],
                    "tracking": "string"
                }
        comment : str
            Audit log comment for this action.
        diff_from : str
            From value for diff. String. Overridden if 'diff_operations' is provided.
        diff_op : str
            Operation for diff. String. Overridden if 'diff_operations' is provided.
        diff_operations : list
            Diff operations to perform against the rule group.
            Single.
        diff_path : str
            Path for diff. String. Overridden if 'diff_operations' is provided.
        diff_type : str
            Type of diff to apply.
        id : str
            ID of the rule group to update.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        rule_ids : str or list[str]
            Rule ID(s)
        rule_versions : list[int]
            Rule version(s)
        tracking : str
            Tracking.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = firewall_rule_group_update_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_rule_group",
            body=body,
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def create_rule_group_validation(self: object,
                                     body: dict = None,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Validate the request for creating a new rule group on a platform for a customer with a name and description.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/create-rule-group-validation

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "description": "string",
                    "enabled": true,
                    "name": "string",
                    "platform": "string",
                    "rules": [
                        {
                        "action": "string",
                        "address_family": "string",
                        "description": "string",
                        "direction": "string",
                        "enabled": true,
                        "fields": [
                            {
                            "final_value": "string",
                            "label": "string",
                            "name": "string",
                            "type": "string",
                            "value": "string",
                            "values": [
                                "string"
                            ]
                            }
                        ],
                        "fqdn": "string",
                        "fqdn_enabled": true,
                        "icmp": {
                            "icmp_code": "string",
                            "icmp_type": "string"
                        },
                        "local_address": [
                            {
                            "address": "string",
                            "netmask": 0
                            }
                        ],
                        "local_port": [
                            {
                            "end": 0,
                            "start": 0
                            }
                        ],
                        "log": true,
                        "monitor": {
                            "count": "string",
                            "period_ms": "string"
                        },
                        "name": "string",
                        "protocol": "string",
                        "remote_address": [
                            {
                            "address": "string",
                            "netmask": 0
                            }
                        ],
                        "remote_port": [
                            {
                            "end": 0,
                            "start": 0
                            }
                        ],
                        "temp_id": "string"
                        }
                    ]
                }
        clone_id : str
            A rule group ID from which to copy rules. If this is provided then the
            'rules' property of the body and the 'rules' keyword are ignored.
        comment : str
            Audit log comment for this action.
        description : str
            Description of the rule.
        enabled : bool
            Flag indicating if this rule is enabled.
        library : str
            If this flag is set to true then the rules will be cloned from the clone_id
            from the CrowdStrike Firewall Rule Groups Library.
        name : str
            Name for this rule.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        platform : str
            Platform name this rule applies to.
        rules : list[dict]
            JSON formatted list of rules to validate.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = firewall_rule_group_validation_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_rule_group_validation",
            keywords=kwargs,
            body=body,
            params=parameters
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def update_rule_group_validation(self: object,
                                     body: dict = None,
                                     cs_username: str = None,  # pylint: disable=W0613  # deprecated
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Validate the request.

        Validates the request of updating name, description, or enabled status
        of a rule group, or create, edit, delete, or reorder rules.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/update-rule-group-validation

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if other keywords are provided.
                {
                    "diff_operations": [
                        {
                            "from": "string",
                            "op": "string",
                            "path": "string"
                        }
                    ],
                    "diff_type": "string",
                    "id": "string",
                    "rule_ids": [
                        "string"
                    ],
                    "rule_versions": [
                        0
                    ],
                    "tracking": "string"
                }
        comment : str
            Audit log comment for this action.
        diff_from : str
            From value for diff. String. Overridden if 'diff_operations' is provided.
        diff_op : str
            Operation for diff. String. Overridden if 'diff_operations' is provided.
        diff_operations : list
            Diff operations to perform against the rule group.
            Single.
        diff_path : str
            Path for diff. String. Overridden if 'diff_operations' is provided.
        diff_type : str
            Type of diff to apply.
        id : str
            ID of the rule group to update.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        rule_ids : str or list[str]
            Rule ID(s)
        rule_versions : list[int]
            Rule version(s)
        tracking : str
            Tracking.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = firewall_rule_group_update_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_rule_group_validation",
            body=body,
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rules(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get rule entities by ID or Family ID.

        ID = 64-bit unsigned int as decimal string
        Family ID = 32-character hexadecimal string

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/get_rules

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the rule(s) to retrieve.
        parameters : dict
            full parameters payload, not required if `ids` keyword is provided.

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
            operation_id="get_rules",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def validate_filepath_pattern(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Validate that the test pattern matches the executable filepath glob pattern.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/validate-filepath-pattern

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if using other keywords.
                {
                    "filepath_pattern": "string",
                    "filepath_test_string": "string"
                }
        filepath_pattern : str
            Pattern to test against.
        filepath_test_string : str
            File path string to be tested.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = firewall_filepattern_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="validate_filepath_pattern",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_events(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find all event IDs matching the query with filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_events

        Keyword arguments
        -----------------
        after : str
            A pagination token used with the limit parameter to manage pagination
            of results. On your first request, don't provide an after token. On
            subsequent requests, provide the after token from the previous response
            to continue from that place in the results.
        filter : str
            FQL query specifying the filter parameters.
            Filter term criteria:
            enabled           name
            platform          description
            Filter range criteria:
            created_on
            modified_on
            (use any common date format, such as '2010-05-15T14:55:21.892315096Z')
        limit : int
            The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset : str
            The integer offset to start retrieving records from. Defaults to 0.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_on|desc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_events",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_firewall_fields(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the firewall field specification IDs for the provided platform.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_firewall_fields

        Keyword arguments
        -----------------
        platform_id : str
            Get fields configuration for this platform.
        limit : int
            The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset : str
            The integer offset to start retrieving records from. Defaults to 0.
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
            operation_id="query_firewall_fields",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_network_locations(self: object, parameters: dict = None, **kwargs) -> dict:
        """Find all network location IDs matching the query with filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query-network-locations

        Keyword arguments
        -----------------
        after : str
            A pagination token used with the limit parameter to manage pagination
            of results. On your first request, don't provide an after token. On
            subsequent requests, provide the after token from the previous response
            to continue from that place in the results.
        filter : str
            FQL query specifying the filter parameters.
        limit : int
            The maximum number of rule IDs to return.
        offset : str
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_network_locations",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_platforms(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the list of platform names.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_platforms

        Keyword arguments
        -----------------
        limit : int (1-100)
            The maximum number of rule IDs to return.
        offset : str
            The integer offset to start retrieving records from. Defaults to 0.
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
            operation_id="query_platforms",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policy_rules(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find all firewall rule IDs matching the query with filter.

        Results are returned in precedence order.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_policy_rules

        Keyword arguments
        -----------------
        after : str
            A pagination token used with the limit parameter to manage pagination
            of results. On your first request, don't provide an after token. On
            subsequent requests, provide the after token from the previous response
            to continue from that place in the results.
        filter : str
            FQL query specifying the filter parameters.
            Filter term criteria:
            enabled           name
            platform          description
            Filter range criteria:
            created_on
            modified_on
            (use any common date format, such as '2010-05-15T14:55:21.892315096Z')
        limit : int
            The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset : str
            The integer offset to start retrieving records from. Defaults to 0.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_on|desc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_policy_rules",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_groups(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find all rule group IDs matching the query with filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups

        Keyword arguments
        -----------------
        after : str
            A pagination token used with the limit parameter to manage pagination
            of results. On your first request, don't provide an after token. On
            subsequent requests, provide the after token from the previous response
            to continue from that place in the results.
        filter : str
            FQL query specifying the filter parameters.
            Filter term criteria:
            enabled           name
            platform          description
            Filter range criteria:
            created_on
            modified_on
            (use any common date format, such as '2010-05-15T14:55:21.892315096Z')
        limit : int
            The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset : str
            The integer offset to start retrieving records from. Defaults to 0.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_on|desc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rule_groups",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rules(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find all rule IDs matching the query with filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management/query_rule_groups

        Keyword arguments
        -----------------
        after : str
            A pagination token used with the limit parameter to manage pagination
            of results. On your first request, don't provide an after token. On
            subsequent requests, provide the after token from the previous response
            to continue from that place in the results.
        filter : str
            FQL query specifying the filter parameters.
            Filter term criteria:
            enabled           name
            platform          description
            Filter range criteria:
            created_on
            modified_on
            (use any common date format, such as '2010-05-15T14:55:21.892315096Z')
        limit : int
            The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        offset : str
            The integer offset to start retrieving records from. Defaults to 0.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_on|desc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_rules",
            keywords=kwargs,
            params=parameters
            )

    update_policy_container_v2 = update_policy_container


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Firewall_Management = FirewallManagement  # pylint: disable=C0103
