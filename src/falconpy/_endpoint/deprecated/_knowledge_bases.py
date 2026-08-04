"""Internal API endpoint constant library (deprecated operations)."""

_knowledge_bases_endpoints = [
  [
    "AggregatesKnowledgeBasesV1",
    "POST",
    "/agentic-studio/aggregates/knowledge_bases/v1",
    "Aggregate knowledge bases based on the provided msa criteria.",
    "knowledge_bases",
    [
      {
        "type": "boolean",
        "default": False,
        "description": "Include deleted knowledge bases in the result. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      },
      {
        "description": "Aggregate requests for knowledge base data.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ]
]
