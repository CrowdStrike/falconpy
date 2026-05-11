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
  ],
  [
    "EntitiesKnowledgeBasesV1",
    "GET",
    "/agentic-studio/entities/knowledge_bases/v1",
    "Retrieve knowledge base entities for the provided id.",
    "knowledge_bases",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "IDs of entities to retrieve.",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Include deleted knowledge bases in the result. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ],
  [
    "EntitiesKnowledgeBasesCreateV1",
    "POST",
    "/agentic-studio/entities/knowledge_bases/v1",
    "Create or update a knowledge base. For deletion, provide knowledge base with IsDeleted=true.",
    "knowledge_bases",
    [
      {
        "description": "Knowledge base definition to create or update",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "EntitiesKnowledgeBasesUpdateV1",
    "PATCH",
    "/agentic-studio/entities/knowledge_bases/v1",
    "Update an existing knowledge base.",
    "knowledge_bases",
    [
      {
        "description": "Knowledge base definition with updated fields",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueriesKnowledgeBasesV1",
    "GET",
    "/agentic-studio/queries/knowledge_bases/v1",
    "Query knowledge bases based on the provided filters.",
    "knowledge_bases",
    [
      {
        "type": "integer",
        "description": "Starting index of overall result set from which to return ids.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 10,
        "maximum": 500,
        "minimum": 1,
        "description": "Number of IDs to return. Offset + limit should NOT be above 10K.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Possible order by fields: name, created_at. Ex: 'created_at|desc' or 'name|asc'.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL query specifying the filter parameters.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Include deleted knowledge bases in the result. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ]
]
