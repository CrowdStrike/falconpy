"""Internal API endpoint constant library (deprecated operations)."""

_spotlight_vulnerabilities_endpoints = [
  [
    "combinedQueryInstalledPatches",
    "GET",
    "/spotlight/combined/installed-patches/v1",
    "Gets installed patches information for hosts.",
    "spotlight_vulnerabilities",
    [
      {
        "type": "string",
        "description": "A pagination token used with the limit parameter to manage pagination of results. On "

        "your first request, don't provide an after token. On subsequent requests, provide the after token from the "

        "previous response to continue from that place in the results.",

        "name": "after",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Maximum number of entities to return.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort installed patches by their properties.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter items using a query in Falcon Query Language (FQL).",
        "name": "filter",
        "in": "query",
        "required": True
      }
    ]
  ]
]
