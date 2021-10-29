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
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import generic_payload_list
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
    def query_actor_entities(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get info about actors that match provided FQL filters.

        Keyword arguments:
        fields -- The fields to return, or a predefined set of fields in the form of the collection
                  name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                  Defaults to __basic__.
        filter -- The filter expression that should be used to limit the results. FQL syntax.
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
        limit -- The maximum number of actors to return. [integer, 1-5000]
        offset -- The integer offset to start retrieving records from.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. created_date.desc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorEntities
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelActorEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_indicator_entities(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get info about indicators that match provided FQL filters.

        Keyword arguments:
        fields -- The fields to return, or a predefined set of fields in the form of the collection
                  name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                  Defaults to __basic__.
        filter -- The filter expression that should be used to limit the results. FQL syntax.
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
                  labels.last_valid_on
        include_deleted -- include both published and deleted indicators.
                           Boolean, defaults to False.
        limit -- The maximum number of indicators to return. [integer, 1-50000]
        offset -- The integer offset to start retrieving records from.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. published_date|asc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorEntities
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelIndicatorEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_report_entities(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get info about reports that match provided FQL filters.

        Keyword arguments:
        fields -- The fields to return, or a predefined set of fields in the form of the collection
                  name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                  Defaults to __basic__.
        filter -- The filter expression that should be used to limit the results. FQL syntax.
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
        limit -- The maximum number of reports to return. [integer, 1-5000]
        offset -- The integer offset to start retrieving records from.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. created_date|asc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportEntities
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelReportEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_actor_entities(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Retrieve specific actors using their actor IDs.

        Keyword arguments:
        fields -- The fields to return, or a predefined set of fields in the form of the collection
                  name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                  Defaults to __basic__.
        ids -- One or more actor IDs. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelActorEntities
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelActorEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_indicator_entities(self: object, *args, body: dict = None, **kwargs) -> dict:
        """Retrieve specific indicators using their indicator IDs.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids -- ID(s) of the indicator entities to retrieve. String or list of strings.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelIndicatorEntities
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
    def get_report_pdf(self: object, *args, parameters: dict = None, **kwargs) -> object:
        """Return a Report PDF attachment.

        Keyword arguments:
        id -- One or more actor IDs. String or list of strings.
        parameters - full parameters payload, not required if id is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'id'.
                   All others are ignored.

        Returns: binary object on SUCCESS, dict object containing API response on FAILURE.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportPDF
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelReportPDF",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_report_entities(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Retrieve specific reports using their report IDs.

        Keyword arguments:
        fields -- The fields to return, or a predefined set of fields in the form of the collection
                  name surround by two underscores: __<collection_name>__. e.g. slug __full__.
                  Defaults to __basic__.
        ids -- One or more actor IDs. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportEntities
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

        Keyword arguments:
        format -- Choose the format you want the rule set in. Either zip or gzip. Defaults to zip.
        id -- One or more actor IDs. String or list of strings.
        parameters - full parameters payload, not required if id is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'id'.
                   All others are ignored.

        Returns: binary object on SUCCESS, dict object containing API response on FAILURE.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleFile
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

        Keyword arguments:
        format -- Choose the format you want the rule set in. Either zip or gzip. Defaults to zip.
        parameters - full parameters payload, not required if other keywords are used.
        type -- The rule news report type. The following values are accepted:
                common-event-format         snort-suricata-update
                netwitness                  yara-changelog
                snort-suricata-changelog    yara-master
                snort-suricata-master       yara-update

        Arguments: When not specified, the first argument to this method is assumed to be 'type'.
                   All others are ignored.

        Returns: binary object on SUCCESS, dict object containing API response on FAILURE.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetLatestIntelRuleFile
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetLatestIntelRuleFile",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "type")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_rule_entities(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Retrieve details for rule sets for the specified ids.

        Keyword arguments:
        ids -- One or more actor IDs. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleEntities
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelRuleEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_actor_ids(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get actor IDs that match provided FQL filters.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
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
        limit -- The maximum number of actors to return. [integer, 1-5000]
        offset -- The integer offset to start retrieving records from.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. created_date|asc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorIds
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelActorIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_indicator_ids(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get indicators IDs that match provided FQL filters.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
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
                  labels.last_valid_on
        include_deleted -- include both published and deleted indicators.
                           Boolean, defaults to False.
        limit -- The maximum number of indicators to return. [integer, 1-50000]
        offset -- The integer offset to start retrieving records from.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. published_date|asc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorIds
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelIndicatorIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_report_ids(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get report IDs that match provided FQL filters.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
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
        limit -- The maximum number of reports to return. [integer, 1-5000]
        offset -- The integer offset to start retrieving records from.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. created_date|asc).

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelReportIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_rule_ids(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for rule IDs that match provided filter criteria.

        Keyword arguments:
        description -- substring match on the description field. List of strings.
        limit -- The maximum number of rule IDs to return. [integer, 1-5000] Defaults to 10.
        max_created_date -- Filter results to those created on or before a certain date. String.
        min_created_date -- Filter results to those created on or after a certain date. String.
        name -- search by rule title. List of strings.
        offset -- The integer offset to start retrieving records from. Defaults to 0.
        parameters - full parameters payload, not required if using other keywords.
        q -- Perform a generic substring search across all fields.
        sort -- The property to sort by. FQL syntax (e.g. created_date|asc).
        tags -- search for rule tags. List of strings.
        type -- The rule news report type. Required.
                The following values are accepted:
                common-event-format         snort-suricata-update
                netwitness                  yara-changelog
                snort-suricata-changelog    yara-master
                snort-suricata-master       yara-update

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelRuleIds",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    QueryIntelActorEntities = query_actor_entities
    QueryIntelIndicatorEntities = query_indicator_entities
    QueryIntelReportEntities = query_report_entities
    GetIntelActorEntities = get_actor_entities
    GetIntelIndicatorEntities = get_indicator_entities
    GetIntelReportPDF = get_report_pdf
    GetIntelReportEntities = get_report_entities
    GetIntelRuleFile = get_rule_file
    GetLatestIntelRuleFile = get_latest_rule_file
    GetIntelRuleEntities = get_rule_entities
    QueryIntelActorIds = query_actor_ids
    QueryIntelIndicatorIds = query_indicator_ids
    QueryIntelReportIds = query_report_ids
    QueryIntelRuleIds = query_rule_ids
