"""Internal API endpoint constant library.

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

_intel_endpoints = [
  [
    "QueryIntelActorEntities",
    "GET",
    "/intel/combined/actors/v1",
    "Get info about actors that match provided FQL filters.",
    "intel",
    [
      {
        "type": "integer",
        "description": "Set the starting row number to return actors from. Defaults to 0.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Set the number of actors to return. The value must be between 1 and 5000.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Order fields in ascending or descending order.\n\nEx: created_date|asc.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter your query by specifying FQL filter parameters. "
        "Filter parameters include:\n\nactors, actors.id, actors.name, actors.slug, "
        "actors.url, created_date, description, id, last_modified_date, motivations, "
        "motivations.id, motivations.slug, motivations.value, name, name.raw, short_description, "
        "slug, sub_type, sub_type.id, sub_type.name, sub_type.slug, tags, tags.id, tags.slug, "
        "tags.value, target_countries, target_countries.id, target_countries.slug, target_countries.value, "
        "target_industries, target_industries.id, target_industries.slug, target_industries.value, "
        "type, type.id, type.name, type.slug, url.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Perform a generic substring search across all fields.",
        "name": "q",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The fields to return, or a predefined set of fields in the form of the collection "
        "name surrounded by two underscores like:\n\n\\_\\_\\<collection\\>\\_\\_.\n\n"
        "Ex: slug \\_\\_full\\_\\_.\n\nDefaults to \\_\\_basic\\_\\_.",
        "name": "fields",
        "in": "query"
      }
    ]
  ],
  [
    "QueryIntelIndicatorEntities",
    "GET",
    "/intel/combined/indicators/v1",
    "Get info about indicators that match provided FQL filters.",
    "intel",
    [
      {
        "type": "integer",
        "description": "Set the starting row number to return indicators from. Defaults to 0.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Set the number of indicators to return. The number must be between 1 and 50000",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Order fields in ascending or descending order.\n\nEx: published_date|asc.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter your query by specifying FQL filter parameters. "
        "Filter parameters include:\n\n_marker, actors, deleted, domain_types, id, indicator, "
        "ip_address_types, kill_chains, labels, labels.created_on, labels.last_valid_on, labels.name, "
        "last_updated, malicious_confidence, malware_families, published_date, reports, targets, "
        "threat_types, type, vulnerabilities.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Perform a generic substring search across all fields.",
        "name": "q",
        "in": "query"
      },
      {
        "type": "boolean",
        "description": "If true, include both published and deleted indicators in the response. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ],
  [
    "QueryIntelReportEntities",
    "GET",
    "/intel/combined/reports/v1",
    "Get info about reports that match provided FQL filters.",
    "intel",
    [
      {
        "type": "integer",
        "description": "Set the starting row number to return reports from. Defaults to 0.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Set the number of reports to return. The value must be between 1 and 5000.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Order fields in ascending or descending order. Ex: created_date|asc.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter your query by specifying FQL filter parameters. "
        "Filter parameters include:\n\nactors, actors.id, actors.name, actors.slug, actors.url, "
        "created_date, description, id, last_modified_date, motivations, motivations.id, motivations.slug, "
        "motivations.value, name, name.raw, short_description, slug, sub_type, sub_type.id, sub_type.name, "
        "sub_type.slug, tags, tags.id, tags.slug, tags.value, target_countries, target_countries.id, "
        "target_countries.slug, target_countries.value, target_industries, target_industries.id, "
        "target_industries.slug, target_industries.value, type, type.id, type.name, type.slug, url.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Perform a generic substring search across all fields.",
        "name": "q",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The fields to return, or a predefined set of fields in the form of the collection "
        "name surrounded by two underscores like:\n\n\\_\\_\\<collection\\>\\_\\_.\n\n"
        "Ex: slug \\_\\_full\\_\\_.\n\nDefaults to \\_\\_basic\\_\\_.",
        "name": "fields",
        "in": "query"
      }
    ]
  ],
  [
    "GetIntelActorEntities",
    "GET",
    "/intel/entities/actors/v1",
    "Retrieve specific actors using their actor IDs.",
    "intel",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the actors you want to retrieve.",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The fields to return, or a predefined set of fields in the form of the "
        "collection name surrounded by two underscores like:\n\n\\_\\_\\<collection\\>\\_\\_.\n\n"
        "Ex: slug \\_\\_full\\_\\_.\n\nDefaults to \\_\\_basic\\_\\_.",
        "name": "fields",
        "in": "query"
      }
    ]
  ],
  [
    "GetIntelIndicatorEntities",
    "POST",
    "/intel/entities/indicators/GET/v1",
    "Retrieve specific indicators using their indicator IDs.",
    "intel",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetIntelReportPDF",
    "GET",
    "/intel/entities/report-files/v1",
    "Return a Report PDF attachment",
    "intel",
    [
      {
        "type": "string",
        "description": "The ID of the report you want to download as a PDF.",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetIntelReportEntities",
    "GET",
    "/intel/entities/reports/v1",
    "Retrieve specific reports using their report IDs.",
    "intel",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the reports you want to retrieve.",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The fields to return, or a predefined set of fields in the form of the "
        "collection name surrounded by two underscores like:\n\n\\_\\_\\<collection\\>\\_\\_.\n\n"
        "Ex: slug \\_\\_full\\_\\_.\n\nDefaults to \\_\\_basic\\_\\_.",
        "name": "fields",
        "in": "query"
      }
    ]
  ],
  [
    "GetIntelRuleFile",
    "GET",
    "/intel/entities/rules-files/v1",
    "Download earlier rule sets.",
    "intel",
    [
      {
        "type": "string",
        "description": "Choose the format you want the rule set in.",
        "name": "Accept",
        "in": "header"
      },
      {
        "type": "integer",
        "description": "The ID of the rule set.",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Choose the format you want the rule set in. Valid formats are zip and gzip. Defaults to zip.",
        "name": "format",
        "in": "query"
      }
    ]
  ],
  [
    "GetLatestIntelRuleFile",
    "GET",
    "/intel/entities/rules-latest-files/v1",
    "Download the latest rule set.",
    "intel",
    [
      {
        "type": "string",
        "description": "Choose the format you want the rule set in.",
        "name": "Accept",
        "in": "header"
      },
      {
        "type": "string",
        "description": "The rule news report type. Accepted values:\n\nsnort-suricata-master\n\n"
        "snort-suricata-update\n\nsnort-suricata-changelog\n\nyara-master\n\nyara-update\n\n"
        "yara-changelog\n\ncommon-event-format\n\nnetwitness",
        "name": "type",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Choose the format you want the rule set in. Valid formats are zip and gzip. Defaults to zip.",
        "name": "format",
        "in": "query"
      }
    ]
  ],
  [
    "GetIntelRuleEntities",
    "GET",
    "/intel/entities/rules/v1",
    "Retrieve details for rule sets for the specified ids.",
    "intel",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The ids of rules to return.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "QueryIntelActorIds",
    "GET",
    "/intel/queries/actors/v1",
    "Get actor IDs that match provided FQL filters.",
    "intel",
    [
      {
        "type": "integer",
        "description": "Set the starting row number to return actors IDs from. Defaults to 0.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Set the number of actor IDs to return. The value must be between 1 and 5000.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Order fields in ascending or descending order.\n\nEx: created_date|asc.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter your query by specifying FQL filter parameters. "
        "Filter parameters include:\n\nactors, actors.id, actors.name, actors.slug, actors.url, "
        "created_date, description, id, last_modified_date, motivations, motivations.id, motivations.slug, "
        "motivations.value, name, name.raw, short_description, slug, sub_type, sub_type.id, sub_type.name, "
        "sub_type.slug, tags, tags.id, tags.slug, tags.value, target_countries, target_countries.id, "
        "target_countries.slug, target_countries.value, target_industries, target_industries.id, "
        "target_industries.slug, target_industries.value, type, type.id, type.name, type.slug, url.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Perform a generic substring search across all fields.",
        "name": "q",
        "in": "query"
      }
    ]
  ],
  [
    "QueryIntelIndicatorIds",
    "GET",
    "/intel/queries/indicators/v1",
    "Get indicators IDs that match provided FQL filters.",
    "intel",
    [
      {
        "type": "integer",
        "description": "Set the starting row number to return indicator IDs from. Defaults to 0.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Set the number of indicator IDs to return. The number must be between 1 and 50000",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Order fields in ascending or descending order.\n\nEx: published_date|asc.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter your query by specifying FQL filter parameters. "
        "Filter parameters include:\n\n_marker, actors, deleted, domain_types, id, indicator, ip_address_types, "
        "kill_chains, labels, labels.created_on, labels.last_valid_on, labels.name, last_updated, malicious_confidence, "
        "malware_families, published_date, reports, targets, threat_types, type, vulnerabilities.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Perform a generic substring search across all fields.",
        "name": "q",
        "in": "query"
      },
      {
        "type": "boolean",
        "description": "If true, include both published and deleted indicators in the response. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ],
  [
    "QueryIntelReportIds",
    "GET",
    "/intel/queries/reports/v1",
    "Get report IDs that match provided FQL filters.",
    "intel",
    [
      {
        "type": "integer",
        "description": "Set the starting row number to return report IDs from. Defaults to 0.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Set the number of report IDs to return. The value must be between 1 and 5000.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Order fields in ascending or descending order.\n\nEx: created_date|asc.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter your query by specifying FQL filter parameters. "
        "Filter parameters include:\n\nactors, actors.id, actors.name, actors.slug, actors.url, "
        "created_date, description, id, last_modified_date, motivations, motivations.id, motivations.slug, "
        "motivations.value, name, name.raw, short_description, slug, sub_type, sub_type.id, sub_type.name, "
        "sub_type.slug, tags, tags.id, tags.slug, tags.value, target_countries, target_countries.id, "
        "target_countries.slug, target_countries.value, target_industries, target_industries.id, "
        "arget_industries.slug, target_industries.value, type, type.id, type.name, type.slug, url.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Perform a generic substring search across all fields.",
        "name": "q",
        "in": "query"
      }
    ]
  ],
  [
    "QueryIntelRuleIds",
    "GET",
    "/intel/queries/rules/v1",
    "Search for rule IDs that match provided filter criteria.",
    "intel",
    [
      {
        "type": "integer",
        "description": "Set the starting row number to return reports from. Defaults to 0.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The number of rule IDs to return. Defaults to 10.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Order fields in ascending or descending order.\n\nEx: created_date|asc.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Search by rule title.",
        "name": "name",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The rule news report type. Accepted values:\n\nsnort-suricata-master\n\n"
        "snort-suricata-update\n\nsnort-suricata-changelog\n\nyara-master\n\nyara-update\n\n"
        "yara-changelog\n\ncommon-event-format\n\nnetwitness",
        "name": "type",
        "in": "query",
        "required": True
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Substring match on description field.",
        "name": "description",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Search for rule tags.",
        "name": "tags",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Filter results to those created on or after a certain date.",
        "name": "min_created_date",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter results to those created on or before a certain date.",
        "name": "max_created_date",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Perform a generic substring search across all fields.",
        "name": "q",
        "in": "query"
      }
    ]
  ]
]
