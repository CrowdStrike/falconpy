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

_skills_endpoints = [
  [
    "EntitiesSkillsDownloadV2",
    "GET",
    "/agentic-studio/entities/skills/download/v2",
    "Download a single skill blob as a zip archive.",
    "skills",
    [
      {
        "type": "string",
        "description": "ID of the skill to download.",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Include deleted skills in the result. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ],
  [
    "EntitiesSkillsV1",
    "GET",
    "/agentic-studio/entities/skills/v1",
    "Retrieve skill entities for the provided IDs.",
    "skills",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "IDs of skills to retrieve.",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Include deleted skills in the result. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ],
  [
    "EntitiesSkillsUpdateV1",
    "PUT",
    "/agentic-studio/entities/skills/v1",
    "Update an existing skill with a new zip archive.",
    "skills",
    [
      {
        "type": "string",
        "description": "ID of the skill to update",
        "name": "id",
        "in": "formData",
        "required": True
      },
      {
        "type": "file",
        "description": "Updated skill zip archive",
        "name": "skill_blob",
        "in": "formData",
        "required": True
      }
    ]
  ],
  [
    "EntitiesSkillsCreateV1",
    "POST",
    "/agentic-studio/entities/skills/v1",
    "Upload a new skill as a zip archive.",
    "skills",
    [
      {
        "type": "file",
        "description": "Skill zip archive to upload",
        "name": "skill_blob",
        "in": "formData",
        "required": True
      }
    ]
  ],
  [
    "EntitiesSkillsDeleteV1",
    "DELETE",
    "/agentic-studio/entities/skills/v1",
    "Delete a skill by its ID.",
    "skills",
    [
      {
        "type": "string",
        "description": "ID of the skill to delete",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "QueriesSkillsV1",
    "GET",
    "/agentic-studio/queries/skills/v1",
    "Query skills based on the provided filters.",
    "skills",
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
        "description": "Number of IDs to return.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Possible order by fields: name. Ex: 'name|asc'.",
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
        "description": "Include deleted skills in the result. Defaults to false.",
        "name": "include_deleted",
        "in": "query"
      }
    ]
  ]
]
