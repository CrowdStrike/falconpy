"""Internal API endpoint constant library (deprecated operations).

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

_cspm_registration_endpoints = [
  [
    "GetConfigurationDetections",
    "GET",
    "/detects/entities/iom/v1",
    "Get list of active misconfigurations. This endpoint is deprecated, please use "
    "GetConfigurationDetectionIDsV2 and GetConfigurationDetectionEntities instead",
    "cspm_registration",
    [
      {
        "enum": [
          "aws",
          "azure",
          "gcp"
        ],
        "type": "string",
        "description": "Cloud Provider (e.g.: aws|azure|gcp)",
        "name": "cloud_provider",
        "in": "query"
      },
      {
        "type": "string",
        "description": "AWS account ID or GCP Project Number or Azure subscription ID",
        "name": "account_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Azure Subscription ID",
        "name": "azure_subscription_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Azure Tenant ID",
        "name": "azure_tenant_id",
        "in": "query"
      },
      {
        "enum": [
          "all",
          "new",
          "reoccurring"
        ],
        "type": "string",
        "description": "Status (e.g.: new|reoccurring|all)",
        "name": "status",
        "in": "query"
      },
      {
        "pattern": "^[0-9a-z-_]{2,}$",
        "type": "string",
        "description": "Cloud Provider Region",
        "name": "region",
        "in": "query"
      },
      {
        "enum": [
          "Critical",
          "High",
          "Informational",
          "Medium"
        ],
        "type": "string",
        "description": "Policy Severity",
        "name": "severity",
        "in": "query"
      },
      {
        "enum": [
          "ACM",
          "ACR",
          "Any",
          "App Engine",
          "AppService",
          "BigQuery",
          "Cloud Load Balancing",
          "Cloud Logging",
          "Cloud SQL",
          "Cloud Storage",
          "CloudFormation",
          "CloudTrail",
          "CloudWatch Logs",
          "Cloudfront",
          "Compute Engine",
          "Config",
          "Disk",
          "DynamoDB",
          "EBS",
          "EC2",
          "ECR",
          "EFS",
          "EKS",
          "ELB",
          "EMR",
          "Elasticache",
          "GuardDuty",
          "IAM",
          "Identity",
          "KMS",
          "KeyVault",
          "Kinesis",
          "Kubernetes",
          "Lambda",
          "LoadBalancer",
          "Monitor",
          "NLB/ALB",
          "NetworkSecurityGroup",
          "PostgreSQL",
          "RDS",
          "Redshift",
          "S3",
          "SES",
          "SNS",
          "SQLDatabase",
          "SQLServer",
          "SQS",
          "SSM",
          "Serverless Application Repository",
          "StorageAccount",
          "Subscriptions",
          "VPC",
          "VirtualMachine",
          "VirtualNetwork"
        ],
        "type": "string",
        "description": "Cloud Service (e.g.: EBS|EC2|S3 etc.)",
        "name": "service",
        "in": "query"
      },
      {
        "type": "string",
        "description": "String to get next page of results, is associated with a previous execution of "
        "GetConfigurationDetections. Cannot be combined with any filter except limit.",
        "name": "next_token",
        "in": "query"
      },
      {
        "pattern": "^\\d+$",
        "type": "integer",
        "description": "The maximum records to return. [1-500]",
        "name": "limit",
        "in": "query"
      }
    ]
  ]
]
