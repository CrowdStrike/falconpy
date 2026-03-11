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
# pylint: disable=C0302

_ngsiem_endpoints = [
  [
    "UploadLookupV1",
    "POST",
    "/humio/api/v1/repositories/{repository}/files",
    "Upload file to NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "file",
        "description": "file to upload",
        "name": "file",
        "in": "formData",
        "required": True
      }
    ]
  ],
  [
    "GetLookupV1",
    "GET",
    "/humio/api/v1/repositories/{repository}/files/{filename}",
    "Download lookup file from NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of lookup file",
        "name": "filename",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "GetLookupFromPackageWithNamespaceV1",
    "GET",
    "/humio/api/v1/repositories/{repository}/files/{namespace}/{package}/{filename}",
    "Download lookup file in namespaced package from NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of namespace",
        "name": "namespace",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of package",
        "name": "package",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of lookup file",
        "name": "filename",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "GetLookupFromPackageV1",
    "GET",
    "/humio/api/v1/repositories/{repository}/files/{package}/{filename}",
    "Download lookup file in package from NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of package",
        "name": "package",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of lookup file",
        "name": "filename",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "StartSearchV1",
    "POST",
    "/humio/api/v1/repositories/{repository}/queryjobs",
    "Initiate search",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "description": "Query Job JSON request body",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetSearchStatusV1",
    "GET",
    "/humio/api/v1/repositories/{repository}/queryjobs/{id}",
    "Get status of search",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "id of query",
        "name": "id",
        "in": "path",
        "required": True
      },
      {
        "type": "integer",
        "description": "pagination limit",
        "name": "paginationLimit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "pagination offset",
        "name": "paginationOffset",
        "in": "query"
      }
    ]
  ],
  [
    "StopSearchV1",
    "DELETE",
    "/humio/api/v1/repositories/{repository}/queryjobs/{id}",
    "Stop search",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "id of query",
        "name": "id",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "GetDashboardTemplate",
    "GET",
    "/ngsiem-content/entities/dashboards-template/v1",
    "Retrieve Dashboard in NGSIEM as LogScale YAML Template",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "dashboard ID value",
        "name": "ids",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "dashboards"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "query"
      }
    ]
  ],
  [
    "CreateDashboardFromTemplate",
    "POST",
    "/ngsiem-content/entities/dashboards-template/v1",
    "Create Dashboard from LogScale YAML Template in NGSIEM",
    "ngsiem",
    [
      {
        "enum": [
          "all",
          "falcon",
          "third-party"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "formData"
      },
      {
        "type": "string",
        "description": "name of the dashboard",
        "name": "name",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "LogScale dashboard YAML template content, see schema at https://schemas.humio.com/",
        "name": "yaml_template",
        "in": "formData"
      }
    ]
  ],
  [
    "UpdateDashboardFromTemplate",
    "PATCH",
    "/ngsiem-content/entities/dashboards-template/v1",
    "Update Dashboard from LogScale YAML Template in NGSIEM.",
    "ngsiem",
    [
      {
        "enum": [
          "all",
          "falcon",
          "third-party"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "formData"
      },
      {
        "type": "string",
        "description": "id of the dashboard",
        "name": "ids",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "LogScale dashboard YAML template content, see schema at https://schemas.humio.com/",
        "name": "yaml_template",
        "in": "formData"
      }
    ]
  ],
  [
    "DeleteDashboard",
    "DELETE",
    "/ngsiem-content/entities/dashboards/v1",
    "Delete Dashboard in NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "dashboard ID value",
        "name": "ids",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "falcon",
          "third-party"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "query"
      }
    ]
  ],
  [
    "UpdateLookupFileEntries",
    "PATCH",
    "/ngsiem-content/entities/lookupfiles-entries/v1",
    "Update entries in an existing Lookup File in NGSIEM",
    "ngsiem",
    [
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "formData"
      },
      {
        "type": "string",
        "description": "Filename of the lookup file to update",
        "name": "filename",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "The file content for updating or appending the entries",
        "name": "file",
        "in": "formData"
      },
      {
        "enum": [
          "append",
          "update"
        ],
        "type": "string",
        "description": "How to update the file entries",
        "name": "update_mode",
        "in": "formData"
      },
      {
        "type": "string",
        "description": "For update mode, the comma separated list of key columns to use when matching entries "
        "(REQUIRED when update_mode=update)",
        "name": "key_columns",
        "in": "formData"
      },
      {
        "enum": [
          "true",
          "false"
        ],
        "type": "string",
        "description": "For update mode, whether to ignore case when matching keys (REQUIRED when update_mode=update)",
        "name": "ignore_case",
        "in": "formData"
      }
    ]
  ],
  [
    "GetLookupFile",
    "GET",
    "/ngsiem-content/entities/lookupfiles/v1",
    "Retrieve Lookup File in NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "lookup file filename",
        "name": "filename",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "dashboards",
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "query"
      }
    ]
  ],
  [
    "CreateLookupFile",
    "POST",
    "/ngsiem-content/entities/lookupfiles/v1",
    "Create Lookup File in NGSIEM",
    "ngsiem",
    [
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "formData"
      },
      {
        "type": "string",
        "description": "Filename of the lookup file to create",
        "name": "filename",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "file content to upload",
        "name": "file",
        "in": "formData"
      }
    ]
  ],
  [
    "UpdateLookupFile",
    "PATCH",
    "/ngsiem-content/entities/lookupfiles/v1",
    "Update an entire Lookup File in NGSIEM",
    "ngsiem",
    [
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "formData"
      },
      {
        "type": "string",
        "description": "Filename of the lookup file to update",
        "name": "filename",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "file content to upload",
        "name": "file",
        "in": "formData"
      }
    ]
  ],
  [
    "DeleteLookupFile",
    "DELETE",
    "/ngsiem-content/entities/lookupfiles/v1",
    "Delete Lookup File in NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "lookup file filename",
        "name": "filename",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "query"
      }
    ]
  ],
  [
    "GetParserTemplate",
    "GET",
    "/ngsiem-content/entities/parsers-template/v1",
    "Retrieve Parser in NGSIEM as LogScale YAML Template",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "parser ID value",
        "name": "ids",
        "in": "query"
      },
      {
        "enum": [
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "query"
      }
    ]
  ],
  [
    "CreateParserFromTemplate",
    "POST",
    "/ngsiem-content/entities/parsers-template/v1",
    "Create Parser from LogScale YAML Template in NGSIEM",
    "ngsiem",
    [
      {
        "enum": [
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "LogScale Parser YAML template content, see schema at https://schemas.humio.com/",
        "name": "yaml_template",
        "in": "formData"
      }
    ]
  ],
  [
    "UpdateParserFromTemplate",
    "PATCH",
    "/ngsiem-content/entities/parsers-template/v1",
    "Update Parser in NGSIEM from YAML Template. Please note that name changes are not supported, but rather "
    "should be created as a new parser.",
    "ngsiem",
    [
      {
        "enum": [
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "formData"
      },
      {
        "type": "string",
        "description": "id of the parser",
        "name": "ids",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "LogScale Parser YAML template content, see schema at https://schemas.humio.com/",
        "name": "yaml_template",
        "in": "formData"
      }
    ]
  ],
  [
    "UpdateParserAutoUpdatePolicy",
    "PUT",
    "/ngsiem-content/entities/parsers/autoupdate/v1",
    "Updates a parser auto update policy - 'on' enables auto-updates, 'off' disables them",
    "ngsiem",
    [
      {
        "description": "update parser auto update policy request",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "BulkInstallParsers",
    "POST",
    "/ngsiem-content/entities/parsers/bulk-install/v1",
    "Installs multiple CrowdStrike-managed out-of-the-box (OOTB) parsers into the customer's repository in a "
    "single operation. This endpoint provisions multiple pre-built parsers with their specific versions for the "
    "requesting customer ID (CID). The parsers are installed as-is and cannot be modified by the customer. Requires "
    "an array of parsers with parser_id and version in the request body. Maximum 100 parsers per request.",
    "ngsiem",
    [
      {
        "description": "bulk install parsers request",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "InstallParser",
    "POST",
    "/ngsiem-content/entities/parsers/install/v1",
    "Installs a CrowdStrike-managed out-of-the-box (OOTB) parser into the customer's repository. This endpoint "
    " provisions a pre-built parser with a specific version for the requesting customer ID (CID). The parser is "
    "installed as-is and cannot be modified by the customer. Requires parser_id and version in the request body.",
    "ngsiem",
    [
      {
        "description": "create parser install request",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetParser",
    "GET",
    "/ngsiem-content/entities/parsers/v1",
    "Retrieve Parser in NGSIEM. This endpoint has been deprecated in favour of the GET /entities/parsers-template/v1 API.",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "parser ID value",
        "name": "ids",
        "in": "query"
      },
      {
        "enum": [
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "query"
      }
    ]
  ],
  [
    "CreateParser",
    "POST",
    "/ngsiem-content/entities/parsers/v1",
    "Create Parser in NGSIEM. This endpoint has been deprecated in favour of the POST /entities/parsers-template/v1 API.",
    "ngsiem",
    [
      {
        "description": "create parser request",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "UpdateParser",
    "PATCH",
    "/ngsiem-content/entities/parsers/v1",
    "Update Parser in NGSIEM. Please note that name changes are not supported, but rather should be created as "
    "a new parser.  This endpoint has been deprecated in favour of the PATCH /entities/parsers-template/v1 API.",
    "ngsiem",
    [
      {
        "description": "update parser request",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteParser",
    "DELETE",
    "/ngsiem-content/entities/parsers/v1",
    "Delete Parser in NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "parser ID value",
        "name": "ids",
        "in": "query"
      },
      {
        "enum": [
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "query"
      }
    ]
  ],
  [
    "GetSavedQueryTemplate",
    "GET",
    "/ngsiem-content/entities/savedqueries-template/v1",
    "Retrieve Saved Query in NGSIEM as LogScale YAML Template",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "saved query ID value",
        "name": "ids",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "dashboards"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "query"
      }
    ]
  ],
  [
    "CreateSavedQuery",
    "POST",
    "/ngsiem-content/entities/savedqueries-template/v1",
    "Create Saved Query from LogScale YAML Template in NGSIEM",
    "ngsiem",
    [
      {
        "enum": [
          "all",
          "falcon",
          "third-party"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "LogScale Saved Query YAML template content, see schema at https://schemas.humio.com/",
        "name": "yaml_template",
        "in": "formData"
      }
    ]
  ],
  [
    "UpdateSavedQueryFromTemplate",
    "PATCH",
    "/ngsiem-content/entities/savedqueries-template/v1",
    "Update Saved Query from LogScale YAML Template in NGSIEM.",
    "ngsiem",
    [
      {
        "enum": [
          "all",
          "falcon",
          "third-party"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "formData"
      },
      {
        "type": "string",
        "description": "id of the saved query",
        "name": "ids",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "LogScale Saved Query YAML template content, see schema at https://schemas.humio.com/",
        "name": "yaml_template",
        "in": "formData"
      }
    ]
  ],
  [
    "DeleteSavedQuery",
    "DELETE",
    "/ngsiem-content/entities/savedqueries/v1",
    "Delete Saved Query in NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "saved query ID value",
        "name": "ids",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "falcon",
          "third-party"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "query"
      }
    ]
  ],
  [
    "ListDashboards",
    "GET",
    "/ngsiem-content/queries/dashboards/v1",
    "List Dashboards in NGSIEM",
    "ngsiem",
    [
      {
        "pattern": "^\\d{1,4}$",
        "type": "string",
        "default": "50",
        "description": "maximum number of results to return",
        "name": "limit",
        "in": "query"
      },
      {
        "pattern": "^\\d{1,4}$",
        "type": "string",
        "default": "0",
        "description": "number of results to offset the returned results by",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL filter to apply to the name of the content, only currently support text match on "
        "name field: name:~'value'",
        "name": "filter",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "dashboards"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "query"
      }
    ]
  ],
  [
    "ListLookupFiles",
    "GET",
    "/ngsiem-content/queries/lookupfiles/v1",
    "List Lookup Files in NGSIEM",
    "ngsiem",
    [
      {
        "pattern": "^\\d{1,4}$",
        "type": "string",
        "default": "50",
        "description": "maximum number of results to return",
        "name": "limit",
        "in": "query"
      },
      {
        "pattern": "^\\d{1,4}$",
        "type": "string",
        "default": "0",
        "description": "number of results to offset the returned results by",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL filter to apply to the name of the content, only currently support text match on "
        "name field: name:~'value'",
        "name": "filter",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "dashboards",
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "query"
      }
    ]
  ],
  [
    "ListParsers",
    "GET",
    "/ngsiem-content/queries/parsers/v1",
    "List Parsers in NGSIEM",
    "ngsiem",
    [
      {
        "pattern": "^\\d{1,4}$",
        "type": "string",
        "default": "50",
        "description": "maximum number of results to return",
        "name": "limit",
        "in": "query"
      },
      {
        "pattern": "^\\d{1,4}$",
        "type": "string",
        "default": "0",
        "description": "number of results to offset the returned results by",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL filter to apply to the name of the content, only currently support text match on "
        "name field: name:~'value'",
        "name": "filter",
        "in": "query"
      },
      {
        "enum": [
          "parsers-repository"
        ],
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "query"
      },
      {
        "enum": [
          "true",
          "false"
        ],
        "type": "string",
        "description": "filter parsers by update availability",
        "name": "update_available",
        "in": "query",
        "allowEmptyValue": True
      },
      {
        "enum": [
          "ootb",
          "custom"
        ],
        "type": "string",
        "description": "filter parsers by type",
        "name": "parser_type",
        "in": "query",
        "allowEmptyValue": True
      }
    ]
  ],
  [
    "ListSavedQueries",
    "GET",
    "/ngsiem-content/queries/savedqueries/v1",
    "Get Saved Queries in NGSIEM",
    "ngsiem",
    [
      {
        "pattern": "^\\d{1,4}$",
        "type": "string",
        "default": "50",
        "description": "maximum number of results to return",
        "name": "limit",
        "in": "query"
      },
      {
        "pattern": "^\\d{1,4}$",
        "type": "string",
        "default": "0",
        "description": "number of results to offset the returned results by",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL filter to apply to the name of the content, only currently support text match on "
        "name field: name:~'value'",
        "name": "filter",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "falcon",
          "third-party",
          "dashboards"
        ],
        "type": "string",
        "description": "name of search domain (view or repo)",
        "name": "search_domain",
        "in": "query"
      }
    ]
  ],
  [
    "ExternalListDataConnections",
    "GET",
    "/ngsiem/combined/connections/v1",
    "List and search data connections",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Optional filter criteria in FQL format",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Starting position for pagination",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Maximum number of items to return",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort field and direction",
        "name": "sort",
        "in": "query"
      }
    ]
  ],
  [
    "ExternalListDataConnectors",
    "GET",
    "/ngsiem/combined/connectors/v1",
    "List available data connectors",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Optional filter criteria in FQL format",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Starting position for pagination",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Maximum number of items to return",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort field and direction",
        "name": "sort",
        "in": "query"
      }
    ]
  ],
  [
    "ExternalGetDataConnectionStatus",
    "GET",
    "/ngsiem/entities/connections/status/v1",
    "Get data connection provisioning status",
    "ngsiem",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Unique identifier of the data connection",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "ExternalUpdateDataConnectionStatus",
    "PATCH",
    "/ngsiem/entities/connections/status/v1",
    "Update data connection status",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Unique identifier of the data connection",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ExternalGetDataConnectionToken",
    "GET",
    "/ngsiem/entities/connections/token/v1",
    "Get Ingest token for data connection",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Unique identifier of the data connection",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "ExternalRegenerateDataConnectionToken",
    "POST",
    "/ngsiem/entities/connections/token/v1",
    "Regenerate Ingest token for data connection",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Unique identifier of the data connection",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "ExternalGetDataConnectionByID",
    "GET",
    "/ngsiem/entities/connections/v1",
    "Get data connection by ID",
    "ngsiem",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Unique identifier of the data connection",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "ExternalCreateDataConnection",
    "POST",
    "/ngsiem/entities/connections/v1",
    "Create a new data connection",
    "ngsiem",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ExternalUpdateDataConnection",
    "PATCH",
    "/ngsiem/entities/connections/v1",
    "Update a data connection",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Unique identifier of the data connection",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ExternalDeleteDataConnection",
    "DELETE",
    "/ngsiem/entities/connections/v1",
    "Delete a data connection",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Unique identifier of the data connection",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "ExternalListConnectorConfigs",
    "GET",
    "/ngsiem/entities/connectors/configs/v1",
    "List configurations for a data connector",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Unique identifier of the data connector",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "ExternalCreateConnectorConfig",
    "POST",
    "/ngsiem/entities/connectors/configs/v1",
    "Create a new configuration for a data connector",
    "ngsiem",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ExternalPatchConnectorConfig",
    "PATCH",
    "/ngsiem/entities/connectors/configs/v1",
    "Patch configurations for a data connector",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Unique id of the config to update",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ExternalDeleteConnectorConfigs",
    "DELETE",
    "/ngsiem/entities/connectors/configs/v1",
    "Delete data connection config",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "Unique identifier of the connector",
        "name": "connector_id",
        "in": "query",
        "required": True
      },
      {
        "maxItems": 20,
        "uniqueItems": True,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Unique identifiers of the config(s) to delete",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ]
]
