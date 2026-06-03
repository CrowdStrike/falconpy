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

_api_clients_endpoints = [
  [
    "GetAccessibleScopes",
    "GET",
    "/api-clients/entities/accessible-scopes/v1",
    "Get all available scopes for customer.",
    "api_clients",
    []
  ],
  [
    "ResetAPIClientSecret",
    "POST",
    "/api-clients/entities/api-clients-actions/v1",
    "Reset existing API Client(s)'s secret based on API Client ID(s) provided as request parameter(s) 'ids'. "
    "API Client Secret can be reset by specifying appropriate action in request parameter 'action_name'.",
    "api_clients",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The API Client ID(s) for which to perform action on API Client(s).",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Action to perform as part of API Client update. Only allowed value is 'reset_secret'.",
        "name": "action_name",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetAPIClients",
    "GET",
    "/api-clients/entities/api-clients/v1",
    "Get API Client(s) based on API Client ID(s) provided as request parameter(s) 'ids'.",
    "api_clients",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The API Client ID(s) for which to obtain API Client definition(s).",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "CreateAPIClient",
    "POST",
    "/api-clients/entities/api-clients/v1",
    "Create new API Client.",
    "api_clients",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteAPIClients",
    "DELETE",
    "/api-clients/entities/api-clients/v1",
    "Delete existing API Client(s) based on API Client ID(s) provided as request parameter(s) 'ids'.",
    "api_clients",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The API Client ID(s) for which API Client(s) have to be deleted.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "UpdateAPIClient",
    "PATCH",
    "/api-clients/entities/api-clients/v1",
    "Update existing API Client based on API Client ID provided as request parameter 'ids'. Client Secret "
    "remains unaffected.",
    "api_clients",
    [
      {
        "type": "string",
        "description": "The API Client ID for which to update the API Client definition.",
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
    "GetAllAPIClientIdsForCustomer",
    "GET",
    "/api-clients/queries/api-clients/v1",
    "Get All API client ID(s) for customer.",
    "api_clients",
    [
      {
        "type": "integer",
        "default": 0,
        "description": "Starting index of overall result set from which to return ids.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 10,
        "description": "Number of ids to return.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "default": "created_timestamp",
        "description": "Possible values for sort by field includes id, name, created_by, updated_by, "
        "created_timestamp, last_modified. Ex: 'name|asc', 'name|desc', etc.",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
