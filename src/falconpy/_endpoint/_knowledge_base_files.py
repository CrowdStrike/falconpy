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

_knowledge_base_files_endpoints = [
  [
    "EntitiesKnowledgeBaseFilesDownloadV1",
    "GET",
    "/agentic-studio/entities/knowledge_base_files/download/v1",
    "Download knowledge base file entities for the provided id.",
    "knowledge_base_files",
    [
      {
        "type": "string",
        "description": "ID of the knowledge base",
        "name": "knowledge_base_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "ID of entities to retrieve.",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "EntitiesKnowledgeBaseFilesV1",
    "GET",
    "/agentic-studio/entities/knowledge_base_files/v1",
    "Retrieve knowledge base file entities for the provided id.",
    "knowledge_base_files",
    [
      {
        "type": "string",
        "description": "ID of the knowledge base",
        "name": "knowledge_base_id",
        "in": "query",
        "required": True
      },
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
        "description": "Include deleted knowledge base files in the result. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ],
  [
    "EntitiesKnowledgeBaseFilesUpdateV1",
    "PUT",
    "/agentic-studio/entities/knowledge_base_files/v1",
    "Update an existing file in a knowledge base. Supports updating file content and optionally its description.",
    "knowledge_base_files",
    [
      {
        "type": "string",
        "description": "ID of the document to update",
        "name": "id",
        "in": "formData",
        "required": True
      },
      {
        "type": "file",
        "description": "New file content to replace the existing document",
        "name": "file",
        "in": "formData",
        "required": True
      },
      {
        "type": "string",
        "description": "New description for the document",
        "name": "file_description",
        "in": "formData"
      }
    ]
  ],
  [
    "EntitiesKnowledgeBaseFilesCreateV1",
    "POST",
    "/agentic-studio/entities/knowledge_base_files/v1",
    "Upload a file to a knowledge base.",
    "knowledge_base_files",
    [
      {
        "type": "string",
        "description": "ID of the knowledge base",
        "name": "knowledge_base_id",
        "in": "formData",
        "required": True
      },
      {
        "type": "file",
        "description": "File to be uploaded",
        "name": "file",
        "in": "formData",
        "required": True
      },
      {
        "type": "string",
        "description": "Description for the uploaded file",
        "name": "file_description",
        "in": "formData"
      }
    ]
  ],
  [
    "EntitiesKnowledgeBaseFilesDeleteV1",
    "DELETE",
    "/agentic-studio/entities/knowledge_base_files/v1",
    "Delete document from knowledge base.",
    "knowledge_base_files",
    [
      {
        "type": "string",
        "description": "ID of the knowledge base",
        "name": "knowledge_base_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "ID of the document to delete",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "QueriesKnowledgeBaseFilesV1",
    "GET",
    "/agentic-studio/queries/knowledge_base_files/v1",
    "Query knowledge base files based on the provided filters.",
    "knowledge_base_files",
    [
      {
        "type": "string",
        "description": "ID of the knowledge base",
        "name": "knowledge_base_id",
        "in": "query",
        "required": True
      },
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
        "description": "FQL query specifying the filter parameters.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Include deleted knowledge base files in the result. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ]
]
