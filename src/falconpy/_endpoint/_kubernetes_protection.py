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

_kubernetes_protection_endpoints = [
  [
    "GetAWSAccountsMixin0",
    "GET",
    "/kubernetes-protection/entities/accounts/aws/v1",
    "Provides a list of AWS accounts.",
    "kubernetes_protection",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "AWS Account IDs",
        "name": "ids",
        "in": "query"
      },
      {
        "pattern": "^(true|false)$",
        "enum": [
          "false",
          "true"
        ],
        "type": "string",
        "description": "Filter by whether an account originates from Horizon or not",
        "name": "is_horizon_acct",
        "in": "query"
      },
      {
        "pattern": "^(provisioned|operational)$",
        "enum": [
          "operational",
          "provisioned"
        ],
        "type": "string",
        "description": "Filter by account status",
        "name": "status",
        "in": "query"
      },
      {
        "maximum": 1000,
        "minimum": 0,
        "type": "integer",
        "description": "Limit returned accounts",
        "name": "limit",
        "in": "query"
      },
      {
        "minimum": 0,
        "type": "integer",
        "description": "Offset returned accounts",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "CreateAWSAccount",
    "POST",
    "/kubernetes-protection/entities/accounts/aws/v1",
    "Creates a new AWS account in our system for a customer and generates the installation script",
    "kubernetes_protection",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "UpdateAWSAccount",
    "PATCH",
    "/kubernetes-protection/entities/accounts/aws/v1",
    "Updates the AWS account per the query parameters provided",
    "kubernetes_protection",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "AWS Account ID",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "pattern": "^[a-z\\d-]+$",
        "type": "string",
        "description": "Default Region for Account Automation",
        "name": "region",
        "in": "query"
      }
    ]
  ],
  [
    "DeleteAWSAccountsMixin0",
    "DELETE",
    "/kubernetes-protection/entities/accounts/aws/v1",
    "Delete AWS accounts.",
    "kubernetes_protection",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "AWS Account IDs",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "ListAzureAccounts",
    "GET",
    "/kubernetes-protection/entities/accounts/azure/v1",
    "Provides the azure subscriptions registered to Kubernetes Protection",
    "kubernetes_protection",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Azure Tenant IDs",
        "name": "ids",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Azure Subscription IDs",
        "name": "subscription_id",
        "in": "query"
      },
      {
        "pattern": "^(provisioned|operational)$",
        "enum": [
          "operational",
          "provisioned"
        ],
        "type": "string",
        "description": "Filter by account status",
        "name": "status",
        "in": "query"
      },
      {
        "pattern": "^(true|false)$",
        "enum": [
          "false",
          "true"
        ],
        "type": "string",
        "description": "Filter by whether an account originates from Horizon or not",
        "name": "is_horizon_acct",
        "in": "query"
      },
      {
        "maximum": 1000,
        "minimum": 0,
        "type": "integer",
        "description": "Limit returned accounts",
        "name": "limit",
        "in": "query"
      },
      {
        "minimum": 0,
        "type": "integer",
        "description": "Offset returned accounts",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "CreateAzureSubscription",
    "POST",
    "/kubernetes-protection/entities/accounts/azure/v1",
    "Creates a new Azure Subscription in our system",
    "kubernetes_protection",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteAzureSubscription",
    "DELETE",
    "/kubernetes-protection/entities/accounts/azure/v1",
    "Deletes a new Azure Subscription in our system",
    "kubernetes_protection",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Azure Subscription IDs",
        "name": "ids",
        "in": "query"
      }
    ]
  ],
  [
    "GetLocations",
    "GET",
    "/kubernetes-protection/entities/cloud-locations/v1",
    "Provides the cloud locations acknowledged by the Kubernetes Protection service",
    "kubernetes_protection",
    [
      {
        "enum": [
          "aws",
          "azure",
          "gcp"
        ],
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Cloud Provider",
        "name": "clouds",
        "in": "query"
      }
    ]
  ],
  [
    "GetCombinedCloudClusters",
    "GET",
    "/kubernetes-protection/entities/cloud_cluster/v1",
    "Returns a combined list of provisioned cloud accounts and known kubernetes clusters",
    "kubernetes_protection",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Cloud location",
        "name": "locations",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Cloud Account IDs",
        "name": "ids",
        "in": "query"
      },
      {
        "enum": [
          "aks",
          "eks"
        ],
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Cluster Service",
        "name": "cluster_service",
        "in": "query"
      },
      {
        "enum": [
          "Not Installed",
          "Running",
          "Stopped"
        ],
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Cluster Status",
        "name": "cluster_status",
        "in": "query"
      },
      {
        "maximum": 1000,
        "minimum": 0,
        "type": "integer",
        "description": "Limit returned accounts",
        "name": "limit",
        "in": "query"
      },
      {
        "minimum": 0,
        "type": "integer",
        "description": "Offset returned accounts",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "GetAzureTenantConfig",
    "GET",
    "/kubernetes-protection/entities/config/azure/v1",
    "Gets the Azure tenant Config",
    "kubernetes_protection",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Azure Tenant IDs",
        "name": "ids",
        "in": "query"
      },
      {
        "maximum": 1000,
        "minimum": 0,
        "type": "integer",
        "description": "Limit returned accounts",
        "name": "limit",
        "in": "query"
      },
      {
        "minimum": 0,
        "type": "integer",
        "description": "Offset returned accounts",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "GetStaticScripts",
    "GET",
    "/kubernetes-protection/entities/gen/scripts/v1",
    "Gets static bash scripts that are used during registration",
    "kubernetes_protection",
    []
  ],
  [
    "GetHelmValuesYaml",
    "GET",
    "/kubernetes-protection/entities/integration/agent/v1",
    "Provides a sample Helm values.yaml file for a customer to install alongside the agent Helm chart",
    "kubernetes_protection",
    [
      {
        "type": "string",
        "description": "Cluster name. For EKS it will be cluster ARN.",
        "name": "cluster_name",
        "in": "query",
        "required": True
      },
      {
        "type": "boolean",
        "description": "Set to true if the cluster is not managed by a cloud provider, false if it is.",
        "name": "is_self_managed_cluster",
        "in": "query"
      }
    ]
  ],
  [
    "RegenerateAPIKey",
    "POST",
    "/kubernetes-protection/entities/integration/api-key/v1",
    "Regenerate API key for docker registry integrations",
    "kubernetes_protection",
    []
  ],
  [
    "GetClusters",
    "GET",
    "/kubernetes-protection/entities/kubernetes/clusters/v1",
    "Provides the clusters acknowledged by the Kubernetes Protection service",
    "kubernetes_protection",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Cluster name. For EKS it will be cluster ARN.",
        "name": "cluster_names",
        "in": "query"
      },
      {
        "enum": [
          "Not Installed",
          "Running",
          "Stopped"
        ],
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Cluster Status",
        "name": "status",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Cluster Account id. For EKS it will be AWS account ID.",
        "name": "account_ids",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Cloud location",
        "name": "locations",
        "in": "query"
      },
      {
        "enum": [
          "aks",
          "eks"
        ],
        "type": "string",
        "description": "Cluster Service",
        "name": "cluster_service",
        "in": "query"
      },
      {
        "maximum": 1000,
        "minimum": 0,
        "type": "integer",
        "description": "Limit returned accounts",
        "name": "limit",
        "in": "query"
      },
      {
        "minimum": 0,
        "type": "integer",
        "description": "Offset returned accounts",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "TriggerScan",
    "POST",
    "/kubernetes-protection/entities/scan/trigger/v1",
    "Triggers a dry run or a full scan of a customer's kubernetes footprint",
    "kubernetes_protection",
    [
      {
        "pattern": "^(dry-run|full|cluster-refresh)$",
        "enum": [
          "cluster-refresh",
          "dry-run",
          "full"
        ],
        "type": "string",
        "default": "dry-run",
        "description": "Scan Type to do",
        "name": "scan_type",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "PatchAzureServicePrincipal",
    "PATCH",
    "/kubernetes-protection/entities/service-principal/azure/v1",
    "Adds the client ID for the given tenant ID to our system",
    "kubernetes_protection",
    [
      {
        "maxLength": 36,
        "minLength": 36,
        "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$",
        "type": "string",
        "description": "Azure Tenant ID",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "maxLength": 36,
        "minLength": 36,
        "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$",
        "type": "string",
        "description": "Azure Client ID",
        "name": "client_id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetAzureTenantIDs",
    "GET",
    "/kubernetes-protection/entities/tenants/azure/v1",
    "Provides all the azure subscriptions and tenants",
    "kubernetes_protection",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Azure Tenant IDs",
        "name": "ids",
        "in": "query"
      },
      {
        "enum": [
          "Not Installed",
          "Running",
          "Stopped"
        ],
        "type": "string",
        "description": "Cluster Status",
        "name": "status",
        "in": "query"
      },
      {
        "maximum": 1000,
        "minimum": 0,
        "type": "integer",
        "description": "Limit returned accounts",
        "name": "limit",
        "in": "query"
      },
      {
        "minimum": 0,
        "type": "integer",
        "description": "Offset returned accounts",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "GetAzureInstallScript",
    "GET",
    "/kubernetes-protection/entities/user-script/azure/v1",
    "Provides the script to run for a given tenant id and subscription IDs",
    "kubernetes_protection",
    [
      {
        "maxLength": 36,
        "minLength": 36,
        "pattern": "^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$",
        "type": "string",
        "description": "Azure Tenant ID",
        "name": "id",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Azure Subscription IDs",
        "name": "subscription_id",
        "in": "query"
      }
    ]
  ]
]
