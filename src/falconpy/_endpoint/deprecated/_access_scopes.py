"""Internal API endpoint constant library (deprecated operations)."""

_access_scopes_endpoints = [
  [
    "ListAccessScopesExternal",
    "GET",
    "/access-scope-management/entities/access-scopes/v1",
    "List Access Scopes By ID",
    "access_scopes",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "name": "ids",
        "in": "query"
      }
    ]
  ],
  [
    "QueryAccessScopesExternal",
    "GET",
    "/access-scope-management/queries/access-scopes/v1",
    "Query Access Scopes and returns IDs",
    "access_scopes",
    [
      {
        "type": "string",
        "description": "A valid FQL filter.\nAccess Scope fields: name, created_by, created_at.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "format": "int64",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "format": "int64",
        "name": "limit",
        "in": "query"
      }
    ]
  ]
]
