"""Internal API endpoint constant library (deprecated operations)."""

_knowledge_base_audit_events_endpoints = [
  [
    "AggregatesKnowledgeBaseAuditEventsV1",
    "POST",
    "/agentic-studio/aggregates/knowledge_base_audit_events/v1",
    "Aggregate knowledge base audit events based on the provided msa criteria.",
    "knowledge_base_audit_events",
    [
      {
        "description": "Aggregate requests for knowledge base audit event data.",
        "name": "body",
        "in": "body",
        "required": True
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Include audit events for deleted knowledge bases. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ]
]
