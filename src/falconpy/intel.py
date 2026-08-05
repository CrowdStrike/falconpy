"""CrowdStrike Falcon Threat Intelligence API interface class.

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
from ._payload import generic_payload_list, cao_incidents_aggregates_v1_payload, cao_incidents_entities_v1_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._intel import _intel_endpoints as Endpoints


class Intel(ServiceClass):
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
    def query_actor_entities(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get info about actors that match provided FQL filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorEntities

        Keyword arguments
        -----------------
        fields : str or list[str]
            The fields to return, or a predefined set of fields in the form of the collection
            name surround by two underscores: __<collection_name>__. e.g. slug __full__.
            Defaults to __basic__.
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            Available filter parameters:
            actors                sub_type.name
            actors.id             sub_type.slug
            actors.name           tags
            actors.slug           tags.id
            actors.url            tags.slug
            created_date          tags.value
            description           target_countries
            id                    target_countries.id
            last_modified_date    target_countries.slug
            motivations           target_countries.value
            motivations.id        target_industries
            motivations.slug      target_industries.id
            motivations.value     target_industries.slug
            name                  target_industries.value
            name.raw              type
            short_description     type.id
            slug                  type.name
            sub_type              type.slug
            sub_type.id           url
            animal_classifier
        limit : int (1-5000)
            The maximum number of actors to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_date.desc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelActorEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_indicator_entities(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get info about indicators that match provided FQL filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorEntities

        Keyword arguments
        -----------------
        fields : str
            The fields to return, or a predefined set of fields in the form of the collection
            name surround by two underscores: __<collection_name>__. e.g. slug __full__.
            Defaults to __basic__.
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            Available filter parameters:
            _marker               labels.name
            actors                last_updated
            deleted               malicious_confidence
            domain_types          malware_families
            id                    published_date
            indicator             reports
            ip_address_types      targets
            kill_chains           threat_types
            labels                type
            labels.created_on     vulnerabilities
            labels.last_valid_on  reports.slug
        include_deleted : bool
            include both published and deleted indicators.
            Boolean, defaults to False.
        include_relations : bool
            include related indicators. Boolean, defaults to True.
        limit : int (1-50000)
            The maximum number of indicators to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. published_date|asc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelIndicatorEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_report_entities(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get info about reports that match provided FQL filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportEntities

        Keyword arguments
        -----------------
        fields : str or list[str]
            The fields to return, or a predefined set of fields in the form of the collection
            name surround by two underscores: __<collection_name>__. e.g. slug __full__.
            Defaults to __basic__.
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            Available filter parameters:
            actors                              sub_type
            actors.animal_classifier            sub_type.id
            actors.id                           sub_type.name
            actors.name                         sub_type.slug
            actors.slug                         tags
            actors.url                          tags.id
            created_date                        tags.slug
            description                         tags.value
            id                                  target_countries
            last_modified_date                  target_countries.id
            malware                             target_countries.slug
            malware.community_identifiers       target_countries.value
            malware.family_name                 target_industries
            malware.slug                        target_industries.id
            motivations                         target_industries.slug
            motivations.id                      target_industries.value
            motivations.slug                    type
            motivations.value                   type.id
            name                                type.name
            name.raw                            type.slug
            short_description                   url
            slug                                summary
        limit : int (1-5000)
            The maximum number of reports to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_date|asc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelReportEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_actor_entities(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve specific actors using their actor IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelActorEntities

        Keyword arguments
        -----------------
        fields : str or list[str]
            The fields to return, or a predefined set of fields in the form of the collection
            name surround by two underscores: __<collection_name>__. e.g. slug __full__.
            Defaults to __basic__.
        ids : str or list[str]
            One or more actor IDs.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

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
            operation_id="GetIntelActorEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_indicator_entities(self: object,
                               *args,
                               body: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve specific indicators using their indicator IDs.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelIndicatorEntities

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when ids keyword is provided.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            ID(s) of the indicator entities to retrieve.

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
            body = generic_payload_list(submitted_arguments=args,
                                        submitted_keywords=kwargs,
                                        payload_value="ids"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelIndicatorEntities",
            body=body,
            body_validator={"ids": list} if self.validate_payloads else None,
            body_required=["ids"] if self.validate_payloads else None
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_mitre_report(self: object,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Union[Dict[str, Union[int, dict]], bytes], Result]:
        """Export Mitre ATT&CK information for a given actor.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetMitreReport

        Keyword arguments
        -----------------
        actor_id : str
            Actor ID, derived from the actor name.
        format : str
            Report format. Accepted options: 'CSV' or 'JSON'
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
            operation_id="GetMitreReport",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def mitre_attacks(self: object, *args, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve reports and observable IDs associated with the given actor and attacks.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/PostMitreAttacks

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when ids keyword is provided.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            ID(s) of the indicator entities to retrieve.

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
            body = generic_payload_list(submitted_arguments=args,
                                        submitted_keywords=kwargs,
                                        payload_value="ids"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PostMitreAttacks",
            body=body,
            body_validator={"ids": list} if self.validate_payloads else None,
            body_required=["ids"] if self.validate_payloads else None
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_malware_report(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs) -> Union[Dict[str, Union[int, dict]], bytes]:
        """Export Mitre ATT&CK information for a given malware family.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetMalwareMitreReport

        Keyword arguments
        -----------------
        id : str
            Malware family name. String.
            Malware family names should be in lower case with spaces, dots and
            slashes replaced with dashes.
        format : str
            Report format. String.  Supported values: CSV, JSON or JSON_NAVIGATOR.
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
        # If not specified, default to JSON.
        if not kwargs.get("format", None):
            parameters["format"] = "JSON"

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetMalwareMitreReport",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_malware_entities(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs) -> Union[Dict[str, Union[int, dict]], bytes]:
        """Get malware entities for specified ids.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetMalwareEntities

        Keyword arguments
        -----------------
        ids : str or list[str]
            Malware family entities to retrieve. String or list of strings.
            Malware family names should be in lower case with spaces, dots and
            slashes replaced with dashes.
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
            operation_id="GetMalwareEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_report_pdf(self: object, *args, parameters: dict = None, **kwargs) -> object:
        """Return a Report PDF attachment.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportPDF

        Keyword arguments
        -----------------
        id : str
            One or more actor IDs.
        ids : str
            The ID of the report you want to download as a PDF.
            This parameter is used only if no id parameter given.
        parameters : dict
            full parameters payload, not required if id is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        binary object on SUCCESS, dict object containing API response on FAILURE.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelReportPDF",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_malware_entities(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get malware entities that match provided FQL filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryMalwareEntities

        Keyword arguments
        -----------------
        offset : int
            Set the starting row number to return malware IDs from. Defaults to 0.
        limit : int
            Set the number of malware IDs to return. The value must be between 1 and 5000.
        sort : str
            Order fields in ascending or descending order. String.
            Ex: created_date|asc.
        filter : str
            Filter your query by specifying FQL filter parameters.
            The `last_updated` and `created_timestamp` fields are returned as ISO 8601
            timestamp strings for this operation, so their filter values must be
            quoted. Ex: last_updated:>='2026-01-28T10:22:34Z'. An unquoted value
            is parsed as an integer, so a Unix epoch timestamp is accepted without
            error but matches nothing and the filter appears to be ignored.
        q : str
            Perform a generic substring search across all fields.
        fields : str or list[str]
            The fields to return.
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
            operation_id="QueryMalwareEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_report_entities(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve specific reports using their report IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportEntities

        Keyword arguments
        -----------------
        fields : str or list[str]
            The fields to return, or a predefined set of fields in the form of the collection
            name surround by two underscores: __<collection_name>__. e.g. slug __full__.
            Defaults to __basic__.
        ids : str or list[str]
            One or more actor IDs.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

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
            operation_id="GetIntelReportEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_file(self: object, *args, parameters: dict = None, **kwargs) -> object:
        """Download earlier rule sets.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleFile

        Keyword arguments
        -----------------
        format : str
            Choose the format you want the rule set in. Either zip or gzip. Defaults to zip.
        id : int
            One or more actor IDs.
        parameters : dict
            full parameters payload, not required if id is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        binary object on SUCCESS, dict object containing API response on FAILURE.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelRuleFile",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_latest_rule_file(self: object, *args, parameters: dict = None, **kwargs) -> object:
        """Download the latest rule set.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetLatestIntelRuleFile

        Keyword arguments
        -----------------
        if_none_match : str
            Download the latest rule set only if it doesn't have an ETag
            matching the given ones.
        if_modified_since : str
            Download the latest rule set only if the rule was modified after this date.
            http, ANSIC and RFC850 formats accepted.
        format : str
            Choose the format you want the rule set in. Either zip or gzip. Defaults to zip.
        parameters : dict
            full parameters payload, not required if other keywords are used.
        type : str
            The rule news report type. The following values are accepted:
            common-event-format         snort-suricata-update
            netwitness                  yara-changelog
            snort-suricata-changelog    yara-master
            snort-suricata-master       yara-update
            cql-master                  cql-changelog
            cql-update

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'type'.
        All others are ignored.

        Returns
        -------
        binary object on SUCCESS, dict object containing API response on FAILURE.
        """
        headers = {}
        if kwargs.get("if_none_match", None):
            headers["If-None-Match"] = kwargs.get("if_none_match")
        if kwargs.get("if_modified_since", None):
            headers["If-Modified-Since"] = kwargs.get("if_modified_since")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetLatestIntelRuleFile",
            keywords=kwargs,
            headers=headers,
            params=handle_single_argument(args, parameters, "type")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_entities(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve details for rule sets for the specified ids.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleEntities

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more actor IDs.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

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
            operation_id="GetIntelRuleEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_actor_ids(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get actor IDs that match provided FQL filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorIds

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            Available filter parameters:
            actors                sub_type.name
            actors.id             sub_type.slug
            actors.name           tags
            actors.slug           tags.id
            actors.url            tags.slug
            created_date          tags.value
            description           target_countries
            id                    target_countries.id
            last_modified_date    target_countries.slug
            motivations           target_countries.value
            motivations.id        target_industries
            motivations.slug      target_industries.id
            motivations.value     target_industries.slug
            name                  target_industries.value
            name.raw              type
            short_description     type.id
            slug                  type.name
            sub_type              type.slug
            sub_type.id           url
            animal_classifier
        limit : int (1-5000)
            The maximum number of actors to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_date|asc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelActorIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_indicator_ids(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get indicators IDs that match provided FQL filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorIds

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            Available filter parameters:
            _marker               labels.name
            actors                last_updated
            deleted               malicious_confidence
            domain_types          malware_families
            id                    published_date
            indicator             reports
            ip_address_types      targets
            kill_chains           threat_types
            labels                type
            labels.created_on     vulnerabilities
            labels.last_valid_on  reports.slug
        include_deleted : bool
            include both published and deleted indicators.
            Boolean, defaults to False.
        include_relations : bool
            include related indicators. Boolean, defaults to True.
        limit : int (1-50000)
            The maximum number of indicators to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. published_date|asc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelIndicatorIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_mitre_attacks(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get MITRE tactics and techniques for the given actor.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryMitreAttacks

        Keyword arguments
        -----------------
        id : str
            Actor ID, derived from the actor name. (Example: fancy-bear)
        ids : str or list[str]
            The actor ID(derived from the actor's name) for which to retrieve a list of attacks.
            Example: fancy-bear. Multiple values are allowed.
        parameters : dict
            full parameters payload, not required if using `id` keyword.

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
            operation_id="QueryMitreAttacks",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_mitre_attacks_for_malware(self: object,
                                        *args,
                                        parameters: dict = None,
                                        **kwargs) -> Union[Dict[str, Union[int, dict]], bytes]:
        """Get MITRE tactics and techniques for the given malware.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryMitreAttacksForMalware

        Keyword arguments
        -----------------
        ids : str or list[str]
            Malware family entities to retrieve. String or list of strings.
            Malware family names should be in lower case with spaces, dots and
            slashes replaced with dashes.
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
            operation_id="QueryMitreAttacksForMalware",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_report_ids(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get report IDs that match provided FQL filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            Available filter parameters:
            actors                              sub_type
            actors.animal_classifier            sub_type.id
            actors.id                           sub_type.name
            actors.name                         sub_type.slug
            actors.slug                         tags
            actors.url                          tags.id
            created_date                        tags.slug
            description                         tags.value
            id                                  target_countries
            last_modified_date                  target_countries.id
            malware                             target_countries.slug
            malware.community_identifiers       target_countries.value
            malware.family_name                 target_industries
            malware.slug                        target_industries.id
            motivations                         target_industries.slug
            motivations.id                      target_industries.value
            motivations.slug                    type
            motivations.value                   type.id
            name                                type.name
            name.raw                            type.slug
            short_description                   url
            slug                                summary
        limit : int (1-5000)
            The maximum number of reports to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_date|asc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelReportIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_ids(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for rule IDs that match provided filter criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds

        Keyword arguments
        -----------------
        description : str or list[str]
            substring match on the description field.
        limit : int
            The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        max_created_date : str
            Filter results to those created on or before a certain date.
        min_created_date : int
            Filter results to those created on or after a certain date.
        name : str or list[str]
            search by rule title.
        offset : int
            The integer offset to start retrieving records from. Defaults to 0.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_date|asc).
        tags : str or list[str]
            search for rule tags.
        type : str
            The rule news report type. Required.
            The following values are accepted:
            common-event-format         snort-suricata-update
            netwitness                  yara-changelog
            snort-suricata-changelog    yara-master
            snort-suricata-master       yara-update
            cql-master                  cql-changelog
            cql-update

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelRuleIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_malware(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get malware family names that match provided FQL filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryMalware

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            The `last_updated` and `created_timestamp` fields are returned as ISO 8601
            timestamp strings for this operation, so their filter values must be
            quoted. Ex: last_updated:>='2026-01-28T10:22:34Z'. An unquoted value
            is parsed as an integer, so a Unix epoch timestamp is accepted without
            error but matches nothing and the filter appears to be ignored.
        limit : int (1-5000)
            The maximum number of actors to return.
        offset : int
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Perform a generic substring search across all fields.
        sort : str
            The property to sort by. FQL syntax (e.g. created_date|asc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryMalware",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_vulnerabilities(self: object, *args, body: dict = None, **kwargs) -> dict:
        """Retrieve specific vulnerabilities using their indicator IDs.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetVulnerabilities

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when ids keyword is provided.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            ID(s) of the indicator entities to retrieve.

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
            body = generic_payload_list(submitted_arguments=args,
                                        submitted_keywords=kwargs,
                                        payload_value="ids"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetVulnerabilities",
            body=body,
            body_validator={"ids": list} if self.validate_payloads else None,
            body_required=["ids"] if self.validate_payloads else None
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_vulnerabilities(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for rule IDs that match provided filter criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryVulnerabilities

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying the filter parameters. String.
            Filter parameters include:
              _all                            related_actors
              affected_products.product       related_actors.animal_classifier
              affected_products.vendor        related_actors.name
              community_identifiers           related_reports.serial_id
              cve                             related_reports.title
              cvss_v3_base                    related_threats
              cvss_v3_base.score              related_threats.name
              cvss_v3_base.severity           severity
              exploit_status                  updated_timestamp
              publish_date
        limit : int
            The maximum number of IDs to return.
        offset : str
            The integer offset to start retrieving records from. Defaults to 0.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        q : str
            Match phrase_prefix query criteria; included fields:
            _all (all filter string fields indexed).
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
            operation_id="QueryVulnerabilities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def cao_incidents_aggregates_v1(self: object,
                                    body: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Perform statistical aggregations over incident data.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/cao_incidents_aggregates_v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                    ],
                    "exclude": "string",
                    "extended_bounds": {
                        "max": "string",
                        "min": "string"
                    },
                    "field": "string",
                    "filter": "string",
                    "filters_spec": {
                        "filters": "string",
                        "other_bucket": true,
                        "other_bucket_key": "string"
                    },
                    "from": 0,
                    "include": "string",
                    "interval": "string",
                    "max_doc_count": 0,
                    "min_doc_count": 0,
                    "missing": "string",
                    "name": "string",
                    "percents": [
                        "string"
                    ],
                    "q": "string",
                    "ranges": [
                        {
                            "From": 0.0,
                            "To": 0.0
                        }
                    ],
                    "size": 0,
                    "sort": "string",
                    "sub_aggregates": [
                        "string"
                    ],
                    "time_zone": "string",
                    "type": "string"
                }
        date_ranges : list
            The date_ranges value.
        exclude : str
            The exclude value.
        extended_bounds : dict
            The extended_bounds value.
        field : str
            The field value.
        filter : str
            The filter value.
        filters_spec : dict
            The filters_spec value.
        from : int
            The from value.
        include : str
            The include value.
        interval : str
            The interval value.
        max_doc_count : int
            The max_doc_count value.
        min_doc_count : int
            The min_doc_count value.
        missing : str
            The missing value.
        name : str
            The name value.
        percents : list
            The percents value.
        q : str
            The q value.
        ranges : list
            The ranges value.
        size : int
            The size value.
        sort : str
            The sort value.
        sub_aggregates : list
            The sub_aggregates value.
        time_zone : str
            The time_zone value.
        type : str
            The type value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cao_incidents_aggregates_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cao_incidents_aggregates_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def cao_incidents_entities_v1(self: object,
                                  body: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve full details for one or more adversary incidents by their IDs.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/cao_incidents_entities_v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            The ids value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cao_incidents_entities_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cao_incidents_entities_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def cao_incidents_queries_v1(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for adversary incidents using FQL criteria and return a paginated list of matching incident IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/cao_incidents_queries_v1

        Keyword arguments
        -----------------
        sort : str
            The property to sort on, followed by a dot (.), followed by the sort direction, either "asc" or "desc".
            Available sort properties: ActivityStart, ActivityEnd, PublishDate, InvolvesAdversaries.Name,
            InvolvesAdversaries.Slug, LastModifiedAt.
        filter : str
            Optional filter and sort criteria in the form of an FQL query. String.
            Available filters:
                  ActivityEnd                             ActivityStart
                  All                                     Id
                  InvolvesAdversaries.AnimalClassifier    InvolvesAdversaries.Id
                  InvolvesAdversaries.Name                InvolvesAdversaries.Slug
                  InvolvesIndicators.Value                InvolvesThreats.FamilyName
                  LastModifiedAt                          MitreAttack.Id
                  MitreAttack.TacticId                    MitreAttack.TacticName
                  MitreAttack.TechniqueId                 MitreAttack.TechniqueName
                  Motivations.Slug                        Objectives.Slug
                  PublishDate                             ReferencesNotableEvents.Title
                  TargetCountries.Slug                    TargetIndustries.Slug
                  TargetRegions.Slug                      TargetingProfile.Slug
                  TargetsVulnerabilities.CVE              Title
        limit : int
            The maximum records to return. Cannot be higher than 200.
        offset : str
            Starting index of overall result set from which to return ids.
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
            operation_id="cao_incidents_queries_v1",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    cao_incidents_aggregates_v1 = cao_incidents_aggregates_v1
    cao_incidents_entities_v1 = cao_incidents_entities_v1
    cao_incidents_queries_v1 = cao_incidents_queries_v1
    QueryIntelActorEntities = query_actor_entities
    QueryIntelIndicatorEntities = query_indicator_entities
    QueryIntelReportEntities = query_report_entities
    QueryVulnerabilities = query_vulnerabilities
    GetVulnerabilities = get_vulnerabilities
    GetIntelActorEntities = get_actor_entities
    GetIntelIndicatorEntities = get_indicator_entities
    GetMitreReport = get_mitre_report
    GetMalwareMitreReport = get_malware_report
    PostMitreAttacks = mitre_attacks
    GetMalwareEntities = get_malware_entities
    GetIntelReportPDF = get_report_pdf
    QueryMalwareEntities = query_malware_entities
    GetIntelReportEntities = get_report_entities
    GetIntelRuleFile = get_rule_file
    GetLatestIntelRuleFile = get_latest_rule_file
    GetIntelRuleEntities = get_rule_entities
    QueryMitreAttacks = query_mitre_attacks
    QueryMitreAttacksForMalware = query_mitre_attacks_for_malware
    QueryIntelActorIds = query_actor_ids
    QueryMalware = query_malware
    QueryIntelIndicatorIds = query_indicator_ids
    QueryIntelReportIds = query_report_ids
    QueryIntelRuleIds = query_rule_ids
