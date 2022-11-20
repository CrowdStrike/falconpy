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

_d4c_registration_endpoints = [
  [
    "GetD4CAwsAccount",
    "GET",
    "/cloud-connect-aws/entities/account/v2",
    "Returns information about the current status of an AWS account.",
    "d4c_registration",
    [
      {
        "maxLength": 4,
        "minLength": 3,
        "pattern": "^(full|dry)$",
        "type": "string",
        "description": "Type of scan, dry or full, to perform on selected accounts",
        "name": "scan-type",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "AWS account IDs",
        "name": "ids",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "AWS organization IDs",
        "name": "organization-ids",
        "in": "query"
      },
      {
        "pattern": "^(provisioned|operational)$",
        "type": "string",
        "description": "Account status to filter results by.",
        "name": "status",
        "in": "query"
      },
      {
        "maxLength": 3,
        "minLength": 1,
        "type": "integer",
        "default": 100,
        "description": "The maximum records to return. Defaults to 100.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The offset to start retrieving records from",
        "name": "offset",
        "in": "query"
      },
      {
        "pattern": "^(true|false)$",
        "enum": [
          "false",
          "true"
        ],
        "type": "string",
        "description": "Only return migrated d4c accounts",
        "name": "migrated",
        "in": "query"
      }
    ]
  ],
  [
    "CreateD4CAwsAccount",
    "POST",
    "/cloud-connect-aws/entities/account/v2",
    "Creates a new account in our system for a customer and generates a script "
    "for them to run in their AWS cloud environment to grant us access.",
    "d4c_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteD4CAwsAccount",
    "DELETE",
    "/cloud-connect-aws/entities/account/v2",
    "Deletes an existing AWS account or organization in our system.",
    "d4c_registration",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "AWS account IDs to remove",
        "name": "ids",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "AWS organization IDs to remove",
        "name": "organization-ids",
        "in": "query"
      }
    ]
  ],
  [
    "GetD4CAwsConsoleSetupURLs",
    "GET",
    "/cloud-connect-aws/entities/console-setup-urls/v1",
    "Return a URL for customer to visit in their cloud environment to grant "
    "us access to their AWS environment.",
    "d4c_registration",
    [
      {
        "pattern": "^[0-9a-z-]{2,}$",
        "type": "string",
        "description": "Region",
        "name": "region",
        "in": "query"
      }
    ]
  ],
  [
    "GetD4CAWSAccountScriptsAttachment",
    "GET",
    "/cloud-connect-aws/entities/user-scripts-download/v1",
    "Return a script for customer to run in their cloud environment to grant "
    "us access to their AWS environment as a downloadable attachment.",
    "d4c_registration",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "AWS account IDs",
        "name": "ids",
        "in": "query"
      }
    ]
  ],
  [
    "GetCSPMAzureAccount",
    "GET",
    "/cloud-connect-azure/entities/account/v1",
    "Return information about Azure account registration",
    "d4c_registration",
    [
      {
        "type": "array",
        "items": {
          "maxLength": 36,
          "minLength": 36,
          "pattern": "^[0-9a-z-]{36}$",
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "SubscriptionIDs of accounts to select for this status operation. "
        "If this is empty then all accounts are returned.",
        "name": "ids",
        "in": "query"
      },
      {
        "maxLength": 4,
        "minLength": 3,
        "pattern": "^(full|dry)$",
        "type": "string",
        "description": "Type of scan, dry or full, to perform on selected accounts",
        "name": "scan-type",
        "in": "query"
      }
    ]
  ],
  [
    "CreateCSPMAzureAccount",
    "POST",
    "/cloud-connect-azure/entities/account/v1",
    "Creates a new account in our system for a customer and generates a script for them to run "
    "in their cloud environment to grant us access.",
    "d4c_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "UpdateCSPMAzureAccountClientID",
    "PATCH",
    "/cloud-connect-azure/entities/client-id/v1",
    "Update an Azure service account in our system by with the user-created client_id "
    "created with the public key we've provided",
    "d4c_registration",
    [
      {
        "maxLength": 36,
        "minLength": 36,
        "pattern": "^[0-9a-z-]{36}$",
        "type": "string",
        "description": "ClientID to use for the Service Principal associated with the customer's Azure account",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "DiscoverCloudAzureDownloadCertificate",
    "GET",
    "/cloud-connect-azure/entities/download-certificate/v1",
    "Returns JSON object(s) that contain the base64 encoded certificate for a service principal.",
    "d4c_registration",
    [
      {
        "type": "array",
        "items": {
          "maxLength": 36,
          "minLength": 36,
          "pattern": "^[0-9a-z-]{36}$",
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Azure Tenant ID",
        "name": "tenant_id",
        "in": "query",
        "required": True
      },
      {
        "maxLength": 5,
        "minLength": 4,
        "pattern": "^(true|false)$",
        "enum": [
          "false",
          "true"
        ],
        "type": "string",
        "default": False,
        "name": "refresh",
        "in": "query"
      }
    ]
  ],
  [
    "GetCSPMAzureUserScriptsAttachment",
    "GET",
    "/cloud-connect-azure/entities/user-scripts-download/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their "
    "Azure environment as a downloadable attachment",
    "d4c_registration",
    []
  ],
  [
    "GetCSPMAzureUserScripts",
    "GET",
    "/cloud-connect-azure/entities/user-scripts/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their "
    "Azure environment",
    "d4c_registration",
    []
  ],
  [
    "GetCSPMCGPAccount",
    "GET",
    "/cloud-connect-gcp/entities/account/v1",
    "Returns information about the current status of an GCP account.",
    "d4c_registration",
    [
      {
        "maxLength": 4,
        "minLength": 3,
        "pattern": "^(full|dry)$",
        "type": "string",
        "description": "Type of scan, dry or full, to perform on selected accounts",
        "name": "scan-type",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "pattern": "\\d{10,}",
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Parent IDs of accounts",
        "name": "ids",
        "in": "query"
      }
    ]
  ],
  [
    "CreateCSPMGCPAccount",
    "POST",
    "/cloud-connect-gcp/entities/account/v1",
    "Creates a new account in our system for a customer and generates a new service account for them "
    "to add access to in their GCP environment to grant us access.",
    "d4c_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetCSPMGCPUserScriptsAttachment",
    "GET",
    "/cloud-connect-gcp/entities/user-scripts-download/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their "
    "GCP environment as a downloadable attachment",
    "d4c_registration",
    []
  ],
  [
    "GetCSPMGCPUserScripts",
    "GET",
    "/cloud-connect-gcp/entities/user-scripts/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their "
    "GCP environment",
    "d4c_registration",
    []
  ],
  [
    "GetHorizonD4CScripts",
    "GET",
    "/settings-discover/entities/gen/scripts/v1",
    "Returns static install scripts for Horizon.",
    "d4c_registration",
    [
      {
        "pattern": "^(true|false)$",
        "enum": [
          "false",
          "true"
        ],
        "type": "string",
        "description": "Get static script for single account",
        "name": "single_account",
        "in": "query"
      },
      {
        "pattern": "^o-[0-9a-z]{10,32}$",
        "type": "string",
        "description": "AWS organization ID",
        "name": "organization-id",
        "in": "query"
      },
      {
        "pattern": "^(true|false)$",
        "enum": [
          "false",
          "true"
        ],
        "type": "string",
        "name": "delete",
        "in": "query"
      },
      {
        "pattern": "^(commercial|gov)$",
        "enum": [
          "commercial",
          "gov"
        ],
        "type": "string",
        "description": "Account type (e.g.: commercial,gov) Only applicable when "
        "registering AWS commercial account in a Gov environment",
        "name": "account_type",
        "in": "query"
      }
    ]
  ]
]
