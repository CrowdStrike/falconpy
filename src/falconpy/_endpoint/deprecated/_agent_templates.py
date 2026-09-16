"""Internal API endpoint constant library (deprecated operations)."""

_agent_templates_endpoints = [
  [
    "EntitiesAgentTemplatesV1",
    "GET",
    "/agentic-studio/entities/agent-templates/v1",
    "Retrieve agent template entities for the provided IDs",
    "agent_templates",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "IDs of agent templates to retrieve.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "QueriesAgentTemplatesV1",
    "GET",
    "/agentic-studio/queries/agent-templates/v1",
    "Query agent template IDs with pagination",
    "agent_templates",
    [
      {
        "type": "integer",
        "description": "Starting index of overall result set from which to return ids.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 30,
        "maximum": 500,
        "minimum": 1,
        "description": "Number of IDs to return.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL query specifying the filter parameters.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Possible order by fields: name, id, author, model, created_at, updated_at. Ex: 'name|asc'.",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
