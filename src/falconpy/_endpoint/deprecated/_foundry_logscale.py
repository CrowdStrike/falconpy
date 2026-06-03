"""Internal API endpoint constant library (deprecated operations)."""

_foundry_logscale_endpoints = [
  [
    "CreateFileV1",
    "POST",
    "/loggingapi/entities/lookup-files/v1",
    "Creates a lookup file",
    "foundry_logscale",
    [
      {
        "type": "file",
        "description": "File to be uploaded",
        "name": "file",
        "in": "formData",
        "required": True
      },
      {
        "type": "string",
        "maxLength": 50,
        "minLength": 5,
        "description": "Name used to identify the file",
        "name": "name",
        "in": "formData",
        "required": True
      },
      {
        "type": "string",
        "maxLength": 255,
        "minLength": 5,
        "description": "File description",
        "name": "description",
        "in": "formData"
      },
      {
        "type": "string",
        "maxLength": 32,
        "minLength": 32,
        "description": "Unique identifier of the file being updated.",
        "name": "id",
        "in": "formData"
      },
      {
        "type": "string",
        "maxLength": 255,
        "minLength": 5,
        "description": "Name of repository or view to save the file",
        "name": "repo",
        "in": "formData"
      }
    ]
  ],
  [
    "UpdateFileV1",
    "PATCH",
    "/loggingapi/entities/lookup-files/v1",
    "Updates a lookup file",
    "foundry_logscale",
    [
      {
        "type": "string",
        "minLength": 32,
        "description": "Unique identifier of the file being updated.",
        "name": "id",
        "in": "formData",
        "required": True
      },
      {
        "type": "string",
        "maxLength": 255,
        "minLength": 5,
        "description": "File description",
        "name": "description",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "File to be uploaded",
        "name": "file",
        "in": "formData"
      }
    ]
  ]
]
