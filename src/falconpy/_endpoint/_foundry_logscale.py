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

_foundry_logscale_endpoints = [
  [
    "ListReposV1",
    "GET",
    "/loggingapi/combined/repos/v1",
    "Lists available repositories and views",
    "foundry_logscale",
    [
      {
        "type": "boolean",
        "default": False,
        "description": "Include whether test data is present in the application repository",
        "name": "check_test_data",
        "in": "query"
      }
    ]
  ],
  [
    "IngestDataV1",
    "POST",
    "/loggingapi/entities/data-ingestion/ingest/v1",
    "Ingest data into the application repository",
    "foundry_logscale",
    [
      {
        "type": "file",
        "description": "Data file to ingest",
        "name": "data_file",
        "in": "formData",
        "required": True
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Custom tag for ingested data in the form tag:value",
        "name": "tag",
        "in": "formData"
      },
      {
        "type": "string",
        "description": "Tag the data with the specified source",
        "name": "tag_source",
        "in": "formData"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Tag the data with test-ingest",
        "name": "test_data",
        "in": "formData"
      }
    ]
  ],
  [
    "CreateSavedSearchesDynamicExecuteV1",
    "POST",
    "/loggingapi/entities/saved-searches/execute-dynamic/v1",
    "Execute a dynamic saved search",
    "foundry_logscale",
    [
      {
        "type": "string",
        "description": "Application ID.",
        "name": "app_id",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Include generated schemas in the response",
        "name": "include_schema_generation",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Include test data when executing searches",
        "name": "include_test_data",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Whether to include metadata in the response",
        "name": "metadata",
        "in": "query"
      },
      {
        "enum": [
          "sync",
          "async"
        ],
        "type": "string",
        "description": "Mode to execute the query under.",
        "name": "mode",
        "in": "query"
      },
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetSavedSearchesExecuteV1",
    "GET",
    "/loggingapi/entities/saved-searches/execute/v1",
    "Get the results of a saved search",
    "foundry_logscale",
    [
      {
        "type": "string",
        "description": "Job ID for a previously executed async query",
        "name": "job_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Application ID.",
        "name": "app_id",
        "in": "query"
      },
      {
        "minimum": 0,
        "type": "string",
        "description": "Maximum number of records to return.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Whether to include metadata in the response",
        "name": "metadata",
        "in": "query"
      },
      {
        "minimum": 0,
        "type": "string",
        "description": "Starting pagination offset of records to return.",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "CreateSavedSearchesExecuteV1",
    "POST",
    "/loggingapi/entities/saved-searches/execute/v1",
    "Execute a saved search",
    "foundry_logscale",
    [
      {
        "type": "string",
        "description": "Application ID.",
        "name": "app_id",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Whether to include search field details",
        "name": "detailed",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Include test data when executing searches",
        "name": "include_test_data",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Whether to include metadata in the response",
        "name": "metadata",
        "in": "query"
      },
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "CreateSavedSearchesIngestV1",
    "POST",
    "/loggingapi/entities/saved-searches/ingest/v1",
    "Populate a saved search",
    "foundry_logscale",
    [
      {
        "type": "string",
        "description": "Application ID.",
        "name": "app_id",
        "in": "query"
      }
    ]
  ],
  [
    "GetSavedSearchesJobResultsDownloadV1",
    "GET",
    "/loggingapi/entities/saved-searches/job-results-download/v1",
    "Get the results of a saved search as a file",
    "foundry_logscale",
    [
      {
        "type": "string",
        "description": "Job ID for a previously executed async query",
        "name": "job_id",
        "in": "query",
        "required": True
      },
      {
        "enum": [
          "json",
          "csv"
        ],
        "type": "string",
        "description": "Result Format",
        "name": "result_format",
        "in": "query"
      }
    ]
  ],
  [
    "ListViewV1",
    "GET",
    "/loggingapi/entities/views/v1",
    "List views",
    "foundry_logscale",
    [
      {
        "type": "boolean",
        "default": False,
        "description": "Include whether test data is present in the application repository",
        "name": "check_test_data",
        "in": "query"
      }
    ]
  ]
]
