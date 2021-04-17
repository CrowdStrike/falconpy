"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

_endpoint._cspm_registration - Internal API endpoint constant library

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

_cspm_registration_endpoints = [
  [
    "GetCSPMAwsAccount",
    "GET",
    "/cloud-connect-cspm-aws/entities/account/v1?ids={}",
    "Returns information about the current status of an AWS account.",
    "cspm_registration",
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
          "pattern": "\\d{12}",
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
          "pattern": "^o-[0-9a-z]{10,32}$",
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
      }
    ]
  ],
  [
    "CreateCSPMAwsAccount",
    "POST",
    "/cloud-connect-cspm-aws/entities/account/v1",
    "Creates a new account in our system for a customer and generates a script for "
    "them to run in their AWS cloud environment to grant us access.",
    "cspm_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteCSPMAwsAccount",
    "DELETE",
    "/cloud-connect-cspm-aws/entities/account/v1?ids={}",
    "Deletes an existing AWS account or organization in our system.",
    "cspm_registration",
    [
      {
        "type": "array",
        "items": {
          "maxLength": 12,
          "minLength": 12,
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
          "pattern": "^o-[0-9a-z]{10,32}$",
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
    "GetCSPMAwsConsoleSetupURLs",
    "GET",
    "/cloud-connect-cspm-aws/entities/console-setup-urls/v1",
    "Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment.",
    "cspm_registration",
    []
  ],
  [
    "GetCSPMAwsAccountScriptsAttachment",
    "GET",
    "/cloud-connect-cspm-aws/entities/user-scripts-download/v1",
    "Return a script for customer to run in their cloud environment to grant us "
    "access to their AWS environment as a downloadable attachment.",
    "cspm_registration",
    []
  ],
  [
    "GetCSPMAzureAccount",
    "GET",
    "/cloud-connect-cspm-azure/entities/account/v1?ids={}",
    "Return information about Azure account registration",
    "cspm_registration",
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
      }
    ]
  ],
  [
    "CreateCSPMAzureAccount",
    "POST",
    "/cloud-connect-cspm-azure/entities/account/v1",
    "Creates a new account in our system for a customer and generates a script for them "
    "to run in their cloud environment to grant us access.",
    "cspm_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteCSPMAzureAccount",
    "DELETE",
    "/cloud-connect-cspm-azure/entities/account/v1?ids={}",
    "Deletes an Azure subscription from the system.",
    "cspm_registration",
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
        "description": "Azure subscription IDs to remove",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "UpdateCSPMAzureAccountClientID",
    "PATCH",
    "/cloud-connect-cspm-azure/entities/client-id/v1",
    "Update an Azure service account in our system by with the user-created client_id "
    "created with the public key we've provided",
    "cspm_registration",
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
      },
      {
        "maxLength": 36,
        "minLength": 36,
        "pattern": "^[0-9a-z-]{36}$",
        "type": "string",
        "description": "Tenant ID to update client ID for. Required if multiple tenants are registered.",
        "name": "tenant-id",
        "in": "query"
      },
      {
        "description": "This is a placeholder only. Please ignore this field.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetCSPMAzureUserScriptsAttachment",
    "GET",
    "/cloud-connect-cspm-azure/entities/user-scripts-download/v1",
    "Return a script for customer to run in their cloud environment to grant us access to "
    "their Azure environment as a downloadable attachment",
    "cspm_registration",
    [
      {
        "maxLength": 36,
        "minLength": 36,
        "pattern": "^[0-9a-z-]{36}$",
        "type": "string",
        "description": "Tenant ID to generate script for. Defaults to most recently registered tenant.",
        "name": "tenant-id",
        "in": "query"
      }
    ]
  ],
  [
    "GetCSPMPolicy",
    "GET",
    "/settings/entities/policy-details/v1?ids={}",
    "Given a policy ID, returns detailed policy information.",
    "cspm_registration",
    [
      {
        "pattern": "\\d{*}",
        "type": "string",
        "description": "Policy ID",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetCSPMPolicySettings",
    "GET",
    "/settings/entities/policy/v1",
    "Returns information about current policy settings.",
    "cspm_registration",
    [
      {
        "maxLength": 13,
        "minLength": 2,
        "pattern": "^(EC2|IAM|KMS|ACM|ELB|NLB/ALB|EBS|RDS|S3|Redshift|NetworkSecurityGroup|"
        "VirtualNetwork|Disk|PostgreSQL|AppService|KeyVault|VirtualMachine|Monitor|StorageAccount|LoadBalancer|SQLServer)$",
        "type": "string",
        "description": "Service type to filter policy settings by.",
        "name": "service",
        "in": "query",
        "required": True
      },
      {
        "pattern": "\\d{*}",
        "type": "string",
        "description": "Policy ID",
        "name": "policy-id",
        "in": "query"
      }
    ]
  ],
  [
    "UpdateCSPMPolicySettings",
    "PATCH",
    "/settings/entities/policy/v1",
    "Updates a policy setting - can be used to override policy severity or to disable a policy entirely.",
    "cspm_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetCSPMScanSchedule",
    "GET",
    "/settings/scan-schedule/v1",
    "Returns scan schedule configuration for one or more cloud platforms.",
    "cspm_registration",
    [
      {
        "type": "array",
        "items": {
          "maxLength": 5,
          "minLength": 3,
          "pattern": "^(aws|azure|gcp)$",
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Cloud Platform",
        "name": "cloud-platform",
        "in": "query"
      }
    ]
  ],
  [
    "UpdateCSPMScanSchedule",
    "POST",
    "/settings/scan-schedule/v1",
    "Updates scan schedule configuration for one or more cloud platforms.",
    "cspm_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ]
]
