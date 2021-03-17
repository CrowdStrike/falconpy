"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

_endpoint - Internal API endpoint constant library

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

api_endpoints = [
  [
    "QueryAWSAccounts",
    "GET",
    "/cloud-connect-aws/combined/accounts/v1",
    "Search for provisioned AWS Accounts by providing an FQL filter and paging details. "
    "Returns a set of AWS accounts which match the filter criteria"
  ],
  [
    "GetAWSSettings",
    "GET",
    "/cloud-connect-aws/combined/settings/v1",
    "Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts"
  ],
  [
    "GetAWSAccounts",
    "GET",
    "/cloud-connect-aws/entities/accounts/v1?ids={}",
    "Retrieve a set of AWS Accounts by specifying their IDs"
  ],
  [
    "ProvisionAWSAccounts",
    "POST",
    "/cloud-connect-aws/entities/accounts/v1",
    "Provision AWS Accounts by specifying details about the accounts to provision"
  ],
  [
    "UpdateAWSAccounts",
    "PATCH",
    "/cloud-connect-aws/entities/accounts/v1",
    "Update AWS Accounts by specifying the ID of the account and details to update"
  ],
  [
    "DeleteAWSAccounts",
    "DELETE",
    "/cloud-connect-aws/entities/accounts/v1?ids={}",
    "Delete a set of AWS Accounts by specifying their IDs"
  ],
  [
    "CreateOrUpdateAWSSettings",
    "POST",
    "/cloud-connect-aws/entities/settings/v1",
    "Create or update Global Settings which are applicable to all provisioned AWS accounts"
  ],
  [
    "VerifyAWSAccountAccess",
    "POST",
    "/cloud-connect-aws/entities/verify-account-access/v1?ids={}",
    "Performs an Access Verification check on the specified AWS Account IDs"
  ],
  [
    "QueryAWSAccountsForIDs",
    "GET",
    "/cloud-connect-aws/queries/accounts/v1",
    "Search for provisioned AWS Accounts by providing an FQL filter and paging details. "
    "Returns a set of AWS account IDs which match the filter criteria"
  ],
  [
    "GetCSPMAzureAccount",
    "GET",
    "/cloud-connect-azure/entities/account/v1?ids={}",
    "Return information about Azure account registration"
  ],
  [
    "CreateCSPMAzureAccount",
    "POST",
    "/cloud-connect-azure/entities/account/v1",
    "Creates a new account in our system for a customer and generates a script for them to "
    "run in their cloud environment to grant us access."
  ],
  [
    "UpdateCSPMAzureAccountClientID",
    "PATCH",
    "/cloud-connect-azure/entities/client-id/v1",
    "Update an Azure service account in our system by with the user-created client_id created with "
    "the public key we've provided"
  ],
  [
    "GetCSPMAzureUserScriptsAttachment",
    "GET",
    "/cloud-connect-azure/entities/user-scripts-download/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their "
    "Azure environment as a downloadable attachment"
  ],
  [
    "GetCSPMAzureUserScripts",
    "GET",
    "/cloud-connect-azure/entities/user-scripts/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their Azure environment"
  ],
  [
    "GetCSPMAwsAccount",
    "GET",
    "/cloud-connect-cspm-aws/entities/account/v1?ids={}",
    "Returns information about the current status of an AWS account."
  ],
  [
    "CreateCSPMAwsAccount",
    "POST",
    "/cloud-connect-cspm-aws/entities/account/v1",
    "Creates a new account in our system for a customer and generates a script for them to run in their "
    "AWS cloud environment to grant us access."
  ],
  [
    "DeleteCSPMAwsAccount",
    "DELETE",
    "/cloud-connect-cspm-aws/entities/account/v1?ids={}",
    "Deletes an existing AWS account or organization in our system."
  ],
  [
    "GetCSPMAwsConsoleSetupURLs",
    "GET",
    "/cloud-connect-cspm-aws/entities/console-setup-urls/v1",
    "Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment."
  ],
  [
    "GetCSPMAwsAccountScriptsAttachment",
    "GET",
    "/cloud-connect-cspm-aws/entities/user-scripts-download/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their AWS "
    "environment as a downloadable attachment."
  ],
  [
    "GetCSPMAzureAccount",
    "GET",
    "/cloud-connect-cspm-azure/entities/account/v1?ids={}",
    "Return information about Azure account registration"
  ],
  [
    "CreateCSPMAzureAccount",
    "POST",
    "/cloud-connect-cspm-azure/entities/account/v1",
    "Creates a new account in our system for a customer and generates a script for them to run in their "
    "cloud environment to grant us access."
  ],
  [
    "DeleteCSPMAzureAccount",
    "DELETE",
    "/cloud-connect-cspm-azure/entities/account/v1?ids={}",
    "Deletes an Azure subscription from the system."
  ],
  [
    "UpdateCSPMAzureAccountClientID",
    "PATCH",
    "/cloud-connect-cspm-azure/entities/client-id/v1",
    "Update an Azure service account in our system by with the user-created client_id created with the "
    "public key we've provided"
  ],
  [
    "GetCSPMAzureUserScriptsAttachment",
    "GET",
    "/cloud-connect-cspm-azure/entities/user-scripts-download/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their Azure "
    "environment as a downloadable attachment"
  ],
  [
    "GetCSPMCGPAccount",
    "GET",
    "/cloud-connect-gcp/entities/account/v1?ids={}",
    "Returns information about the current status of an GCP account."
  ],
  [
    "CreateCSPMGCPAccount",
    "POST",
    "/cloud-connect-gcp/entities/account/v1",
    "Creates a new account in our system for a customer and generates a new service account for them "
    "to add access to in their GCP environment to grant us access."
  ],
  [
    "GetCSPMGCPUserScriptsAttachment",
    "GET",
    "/cloud-connect-gcp/entities/user-scripts-download/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their "
    "GCP environment as a downloadable attachment"
  ],
  [
    "GetCSPMGCPUserScripts",
    "GET",
    "/cloud-connect-gcp/entities/user-scripts/v1",
    "Return a script for customer to run in their cloud environment to grant us access to their GCP environment"
  ],
  [
    "GetAggregateDetects",
    "POST",
    "/detects/aggregates/detects/GET/v1",
    "Get detect aggregates as specified via json in request body."
  ],
  [
    "UpdateDetectsByIdsV2",
    "PATCH",
    "/detects/entities/detects/v2",
    "Modify the state, assignee, and visibility of detections"
  ],
  [
    "GetDetectSummaries",
    "POST",
    "/detects/entities/summaries/GET/v1",
    "View information about detections"
  ],
  [
    "QueryDetects",
    "GET",
    "/detects/queries/detects/v1",
    "Search for detection IDs that match a given query"
  ],
  [
    "queryCombinedGroupMembers",
    "GET",
    "/devices/combined/host-group-members/v1",
    "Search for members of a Host Group in your environment by providing an FQL filter and paging details. "
    "Returns a set of host details which match the filter criteria"
  ],
  [
    "queryCombinedHostGroups",
    "GET",
    "/devices/combined/host-groups/v1",
    "Search for Host Groups in your environment by providing an FQL filter and paging details. "
    "Returns a set of Host Groups which match the filter criteria"
  ],
  [
    "PerformActionV2",
    "POST",
    "/devices/entities/devices-actions/v2",
    "Take various actions on the hosts in your environment. Contain or lift containment on a host. Delete or restore a host."
  ],
  [
    "UpdateDeviceTags",
    "PATCH",
    "/devices/entities/devices/tags/v1",
    "Append or remove one or more Falcon Grouping Tags on one or more hosts."
  ],
  [
    "GetDeviceDetails",
    "GET",
    "/devices/entities/devices/v1?ids={}",
    "Get details on one or more hosts by providing agent IDs (AID). You can get a host's agent IDs (AIDs) "
    "from the /devices/queries/devices/v1 endpoint, the Falcon console or the Streaming API"
  ],
  [
    "performGroupAction",
    "POST",
    "/devices/entities/host-group-actions/v1",
    "Perform the specified action on the Host Groups specified in the request"
  ],
  [
    "getHostGroups",
    "GET",
    "/devices/entities/host-groups/v1?ids={}",
    "Retrieve a set of Host Groups by specifying their IDs"
  ],
  [
    "createHostGroups",
    "POST",
    "/devices/entities/host-groups/v1",
    "Create Host Groups by specifying details about the group to create"
  ],
  [
    "updateHostGroups",
    "PATCH",
    "/devices/entities/host-groups/v1",
    "Update Host Groups by specifying the ID of the group and details to update"
  ],
  [
    "deleteHostGroups",
    "DELETE",
    "/devices/entities/host-groups/v1?ids={}",
    "Delete a set of Host Groups by specifying their IDs"
  ],
  [
    "QueryHiddenDevices",
    "GET",
    "/devices/queries/devices-hidden/v1",
    "Retrieve hidden hosts that match the provided filter criteria."
  ],
  [
    "QueryDevicesByFilterScroll",
    "GET",
    "/devices/queries/devices-scroll/v1",
    "Search for hosts in your environment by platform, hostname, IP, and other criteria with continuous "
    "pagination capability (based on offset pointer which expires after 2 minutes with no maximum limit)"
  ],
  [
    "QueryDevicesByFilter",
    "GET",
    "/devices/queries/devices/v1",
    "Search for hosts in your environment by platform, hostname, IP, and other criteria."
  ],
  [
    "queryGroupMembers",
    "GET",
    "/devices/queries/host-group-members/v1",
    "Search for members of a Host Group in your environment by providing an FQL filter and paging details. "
    "Returns a set of Agent IDs which match the filter criteria"
  ],
  [
    "queryHostGroups",
    "GET",
    "/devices/queries/host-groups/v1",
    "Search for Host Groups in your environment by providing an FQL filter and paging details. "
    "Returns a set of Host Group IDs which match the filter criteria"
  ],
  [
    "GetArtifacts",
    "GET",
    "/falconx/entities/artifacts/v1",
    "Download IOC packs, PCAP files, and other analysis artifacts."
  ],
  [
    "GetSummaryReports",
    "GET",
    "/falconx/entities/report-summaries/v1?ids={}",
    "Get a short summary version of a sandbox report."
  ],
  [
    "GetReports",
    "GET",
    "/falconx/entities/reports/v1?ids={}",
    "Get a full sandbox report."
  ],
  [
    "DeleteReport",
    "DELETE",
    "/falconx/entities/reports/v1?ids={}",
    "Delete report based on the report ID. Operation can be checked for success by "
    "polling for the report ID on the report-summaries endpoint."
  ],
  [
    "GetSubmissions",
    "GET",
    "/falconx/entities/submissions/v1?ids={}",
    "Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes."
  ],
  [
    "Submit",
    "POST",
    "/falconx/entities/submissions/v1",
    "Submit an uploaded file or a URL for sandbox analysis. Time required for analysis "
    "varies but is usually less than 15 minutes."
  ],
  [
    "QueryReports",
    "GET",
    "/falconx/queries/reports/v1",
    "Find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs that match your criteria."
  ],
  [
    "QuerySubmissions",
    "GET",
    "/falconx/queries/submissions/v1",
    "Find submission IDs for uploaded files by providing an FQL filter and paging details. "
    "Returns a set of submission IDs that match your criteria."
  ],
  [
    "aggregate_events",
    "POST",
    "/fwmgr/aggregates/events/GET/v1",
    "Aggregate events for customer"
  ],
  [
    "aggregate_policy_rules",
    "POST",
    "/fwmgr/aggregates/policy-rules/GET/v1",
    "Aggregate rules within a policy for customer"
  ],
  [
    "aggregate_rule_groups",
    "POST",
    "/fwmgr/aggregates/rule-groups/GET/v1",
    "Aggregate rule groups for customer"
  ],
  [
    "aggregate_rules",
    "POST",
    "/fwmgr/aggregates/rules/GET/v1",
    "Aggregate rules for customer"
  ],
  [
    "get_events",
    "GET",
    "/fwmgr/entities/events/v1?ids={}",
    "Get events entities by ID and optionally version"
  ],
  [
    "get_firewall_fields",
    "GET",
    "/fwmgr/entities/firewall-fields/v1?ids={}",
    "Get the firewall field specifications by ID"
  ],
  [
    "get_platforms",
    "GET",
    "/fwmgr/entities/platforms/v1?ids={}",
    "Get platforms by ID, e.g., windows or mac or droid"
  ],
  [
    "get_policy_containers",
    "GET",
    "/fwmgr/entities/policies/v1?ids={}",
    "Get policy container entities by policy ID"
  ],
  [
    "update_policy_container",
    "PUT",
    "/fwmgr/entities/policies/v1",
    "Update an identified policy container"
  ],
  [
    "get_rule_groups",
    "GET",
    "/fwmgr/entities/rule-groups/v1?ids={}",
    "Get rule group entities by ID. These groups do not contain their rule entites, just the rule IDs in precedence order."
  ],
  [
    "create_rule_group",
    "POST",
    "/fwmgr/entities/rule-groups/v1",
    "Create new rule group on a platform for a customer with a name and description, and return the ID"
  ],
  [
    "update_rule_group",
    "PATCH",
    "/fwmgr/entities/rule-groups/v1",
    "Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules"
  ],
  [
    "delete_rule_groups",
    "DELETE",
    "/fwmgr/entities/rule-groups/v1?ids={}",
    "Delete rule group entities by ID"
  ],
  [
    "get_rules",
    "GET",
    "/fwmgr/entities/rules/v1?ids={}",
    "Get rule entities by ID (64-bit unsigned int as decimal string) or Family ID (32-character hexadecimal string)"
  ],
  [
    "query_events",
    "GET",
    "/fwmgr/queries/events/v1",
    "Find all event IDs matching the query with filter"
  ],
  [
    "query_firewall_fields",
    "GET",
    "/fwmgr/queries/firewall-fields/v1",
    "Get the firewall field specification IDs for the provided platform"
  ],
  [
    "query_platforms",
    "GET",
    "/fwmgr/queries/platforms/v1",
    "Get the list of platform names"
  ],
  [
    "query_policy_rules",
    "GET",
    "/fwmgr/queries/policy-rules/v1",
    "Find all firewall rule IDs matching the query with filter, and return them in precedence order"
  ],
  [
    "query_rule_groups",
    "GET",
    "/fwmgr/queries/rule-groups/v1",
    "Find all rule group IDs matching the query with filter"
  ],
  [
    "query_rules",
    "GET",
    "/fwmgr/queries/rules/v1",
    "Find all rule IDs matching the query with filter"
  ],
  [
    "CrowdScore",
    "GET",
    "/incidents/combined/crowdscores/v1",
    "Query environment wide CrowdScore and return the entity data"
  ],
  [
    "GetBehaviors",
    "POST",
    "/incidents/entities/behaviors/GET/v1",
    "Get details on behaviors by providing behavior IDs"
  ],
  [
    "PerformIncidentAction",
    "POST",
    "/incidents/entities/incident-actions/v1",
    "Perform a set of actions on one or more incidents, such as adding tags or "
    "comments or updating the incident name or description"
  ],
  [
    "GetIncidents",
    "POST",
    "/incidents/entities/incidents/GET/v1",
    "Get details on incidents by providing incident IDs"
  ],
  [
    "QueryBehaviors",
    "GET",
    "/incidents/queries/behaviors/v1",
    "Search for behaviors by providing an FQL filter, sorting, and paging details"
  ],
  [
    "QueryIncidents",
    "GET",
    "/incidents/queries/incidents/v1",
    "Search for incidents by providing an FQL filter, sorting, and paging details"
  ],
  [
    "DevicesCount",
    "GET",
    "/indicators/aggregates/devices-count/v1",
    "Number of hosts in your customer account that have observed a given custom IOC"
  ],
  [
    "GetIOC",
    "GET",
    "/indicators/entities/iocs/v1",
    "Get an IOC by providing a type and value"
  ],
  [
    "CreateIOC",
    "POST",
    "/indicators/entities/iocs/v1",
    "Create a new IOC"
  ],
  [
    "UpdateIOC",
    "PATCH",
    "/indicators/entities/iocs/v1",
    "Update an IOC by providing a type and value"
  ],
  [
    "DeleteIOC",
    "DELETE",
    "/indicators/entities/iocs/v1",
    "Delete an IOC by providing a type and value"
  ],
  [
    "DevicesRanOn",
    "GET",
    "/indicators/queries/devices/v1",
    "Find hosts that have observed a given custom IOC. For details about those hosts, use GET /devices/entities/devices/v1"
  ],
  [
    "QueryIOCs",
    "GET",
    "/indicators/queries/iocs/v1",
    "Search the custom IOCs in your customer account"
  ],
  [
    "ProcessesRanOn",
    "GET",
    "/indicators/queries/processes/v1",
    "Search for processes associated with a custom IOC"
  ],
  [
    "audit_events_read",
    "GET",
    "/installation-tokens/entities/audit-events/v1?ids={}",
    "Gets the details of one or more audit events by id."
  ],
  [
    "customer_settings_read",
    "GET",
    "/installation-tokens/entities/customer-settings/v1",
    "Check current installation token settings."
  ],
  [
    "tokens_read",
    "GET",
    "/installation-tokens/entities/tokens/v1?ids={}",
    "Gets the details of one or more tokens by id."
  ],
  [
    "tokens_create",
    "POST",
    "/installation-tokens/entities/tokens/v1",
    "Creates a token."
  ],
  [
    "tokens_update",
    "PATCH",
    "/installation-tokens/entities/tokens/v1?ids={}",
    "Updates one or more tokens. Use this endpoint to edit labels, change expiration, revoke, or restore."
  ],
  [
    "tokens_delete",
    "DELETE",
    "/installation-tokens/entities/tokens/v1?ids={}",
    "Deletes a token immediately. To revoke a token, use PATCH /installation-tokens/entities/tokens/v1 instead."
  ],
  [
    "audit_events_query",
    "GET",
    "/installation-tokens/queries/audit-events/v1",
    "Search for audit events by providing an FQL filter and paging details."
  ],
  [
    "tokens_query",
    "GET",
    "/installation-tokens/queries/tokens/v1",
    "Search for tokens by providing an FQL filter and paging details."
  ],
  [
    "QueryIntelActorEntities",
    "GET",
    "/intel/combined/actors/v1",
    "Get info about actors that match provided FQL filters."
  ],
  [
    "QueryIntelIndicatorEntities",
    "GET",
    "/intel/combined/indicators/v1",
    "Get info about indicators that match provided FQL filters."
  ],
  [
    "QueryIntelReportEntities",
    "GET",
    "/intel/combined/reports/v1",
    "Get info about reports that match provided FQL filters."
  ],
  [
    "GetIntelActorEntities",
    "GET",
    "/intel/entities/actors/v1?ids={}",
    "Retrieve specific actors using their actor IDs."
  ],
  [
    "GetIntelIndicatorEntities",
    "POST",
    "/intel/entities/indicators/GET/v1",
    "Retrieve specific indicators using their indicator IDs."
  ],
  [
    "GetIntelReportPDF",
    "GET",
    "/intel/entities/report-files/v1",
    "Return a Report PDF attachment"
  ],
  [
    "GetIntelReportEntities",
    "GET",
    "/intel/entities/reports/v1?ids={}",
    "Retrieve specific reports using their report IDs."
  ],
  [
    "GetIntelRuleFile",
    "GET",
    "/intel/entities/rules-files/v1",
    "Download earlier rule sets."
  ],
  [
    "GetLatestIntelRuleFile",
    "GET",
    "/intel/entities/rules-latest-files/v1",
    "Download the latest rule set."
  ],
  [
    "GetIntelRuleEntities",
    "GET",
    "/intel/entities/rules/v1?ids={}",
    "Retrieve details for rule sets for the specified ids."
  ],
  [
    "QueryIntelActorIds",
    "GET",
    "/intel/queries/actors/v1",
    "Get actor IDs that match provided FQL filters."
  ],
  [
    "QueryIntelIndicatorIds",
    "GET",
    "/intel/queries/indicators/v1",
    "Get indicators IDs that match provided FQL filters."
  ],
  [
    "QueryIntelReportIds",
    "GET",
    "/intel/queries/reports/v1",
    "Get report IDs that match provided FQL filters."
  ],
  [
    "QueryIntelRuleIds",
    "GET",
    "/intel/queries/rules/v1",
    "Search for rule IDs that match provided filter criteria."
  ],
  [
    "get_patterns",
    "GET",
    "/ioarules/entities/pattern-severities/v1?ids={}",
    "Get pattern severities by ID."
  ],
  [
    "get_platformsMixin0",
    "GET",
    "/ioarules/entities/platforms/v1?ids={}",
    "Get platforms by ID."
  ],
  [
    "get_rule_groupsMixin0",
    "GET",
    "/ioarules/entities/rule-groups/v1?ids={}",
    "Get rule groups by ID."
  ],
  [
    "create_rule_groupMixin0",
    "POST",
    "/ioarules/entities/rule-groups/v1",
    "Create a rule group for a platform with a name and an optional description. Returns the rule group."
  ],
  [
    "update_rule_groupMixin0",
    "PATCH",
    "/ioarules/entities/rule-groups/v1",
    "Update a rule group. The following properties can be modified: name, description, enabled."
  ],
  [
    "delete_rule_groupsMixin0",
    "DELETE",
    "/ioarules/entities/rule-groups/v1?ids={}",
    "Delete rule groups by ID."
  ],
  [
    "get_rule_types",
    "GET",
    "/ioarules/entities/rule-types/v1?ids={}",
    "Get rule types by ID."
  ],
  [
    "get_rules_get",
    "POST",
    "/ioarules/entities/rules/GET/v1",
    "Get rules by ID and optionally version in the following format: `ID[:version]`."
  ],
  [
    "get_rulesMixin0",
    "GET",
    "/ioarules/entities/rules/v1?ids={}",
    "Get rules by ID and optionally version in the following format: `ID[:version]`. "
    "The max number of IDs is constrained by URL size."
  ],
  [
    "create_rule",
    "POST",
    "/ioarules/entities/rules/v1",
    "Create a rule within a rule group. Returns the rule."
  ],
  [
    "update_rules",
    "PATCH",
    "/ioarules/entities/rules/v1",
    "Update rules within a rule group. Return the updated rules."
  ],
  [
    "delete_rules",
    "DELETE",
    "/ioarules/entities/rules/v1?ids={}",
    "Delete rules from a rule group by ID."
  ],
  [
    "validate",
    "POST",
    "/ioarules/entities/rules/validate/v1",
    "Validates field values and checks for matches if a test string is provided."
  ],
  [
    "query_patterns",
    "GET",
    "/ioarules/queries/pattern-severities/v1",
    "Get all pattern severity IDs."
  ],
  [
    "query_platformsMixin0",
    "GET",
    "/ioarules/queries/platforms/v1",
    "Get all platform IDs."
  ],
  [
    "query_rule_groups_full",
    "GET",
    "/ioarules/queries/rule-groups-full/v1",
    "Find all rule groups matching the query with optional filter."
  ],
  [
    "query_rule_groupsMixin0",
    "GET",
    "/ioarules/queries/rule-groups/v1",
    "Finds all rule group IDs matching the query with optional filter."
  ],
  [
    "query_rule_types",
    "GET",
    "/ioarules/queries/rule-types/v1",
    "Get all rule type IDs."
  ],
  [
    "query_rulesMixin0",
    "GET",
    "/ioarules/queries/rules/v1",
    "Finds all rule IDs matching the query with optional filter."
  ],
  [
    "GetMalQueryQuotasV1",
    "GET",
    "/malquery/aggregates/quotas/v1",
    "Get information about search and download quotas in your environment"
  ],
  [
    "PostMalQueryFuzzySearchV1",
    "POST",
    "/malquery/combined/fuzzy-search/v1",
    "Search Falcon MalQuery quickly, but with more potential for false positives. Search for a combination of "
    "hex patterns and strings in order to identify samples based upon file content at byte level granularity."
  ],
  [
    "GetMalQueryDownloadV1",
    "GET",
    "/malquery/entities/download-files/v1?ids={}",
    "Download a file indexed by MalQuery. Specify the file using its SHA256. Only one file is supported at this time"
  ],
  [
    "GetMalQueryMetadataV1",
    "GET",
    "/malquery/entities/metadata/v1?ids={}",
    "Retrieve indexed files metadata by their hash"
  ],
  [
    "GetMalQueryRequestV1",
    "GET",
    "/malquery/entities/requests/v1?ids={}",
    "Check the status and results of an asynchronous request, such as hunt or exact-search. "
    "Supports a single request id at this time."
  ],
  [
    "GetMalQueryEntitiesSamplesFetchV1",
    "GET",
    "/malquery/entities/samples-fetch/v1?ids={}",
    "Fetch a zip archive with password 'infected' containing the samples. Call this once the /entities/samples-multidownload "
    "request has finished processing"
  ],
  [
    "PostMalQueryEntitiesSamplesMultidownloadV1",
    "POST",
    "/malquery/entities/samples-multidownload/v1",
    "Schedule samples for download. Use the result id with the /request endpoint to check if the download is ready "
    "after which you can call the /entities/samples-fetch to get the zip"
  ],
  [
    "PostMalQueryExactSearchV1",
    "POST",
    "/malquery/queries/exact-search/v1",
    "Search Falcon MalQuery for a combination of hex patterns and strings in order to identify samples based "
    "upon file content at byte level granularity. You can filter results on criteria such as file type, file size "
    "and first seen date. Returns a request id which can be used with the /request endpoint"
  ],
  [
    "PostMalQueryHuntV1",
    "POST",
    "/malquery/queries/hunt/v1",
    "Schedule a YARA-based search for execution. Returns a request id which can be used with the /request endpoint"
  ],
  [
    "oauth2RevokeToken",
    "POST",
    "/oauth2/revoke",
    "Revoke a previously issued OAuth2 access token before the end of its standard 30-minute lifespan."
  ],
  [
    "oauth2AccessToken",
    "POST",
    "/oauth2/token",
    "Generate an OAuth2 access token"
  ],
  [
    "queryCombinedDeviceControlPolicyMembers",
    "GET",
    "/policy/combined/device-control-members/v1",
    "Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. "
    "Returns a set of host details which match the filter criteria"
  ],
  [
    "queryCombinedDeviceControlPolicies",
    "GET",
    "/policy/combined/device-control/v1",
    "Search for Device Control Policies in your environment by providing an FQL filter and paging details. "
    "Returns a set of Device Control Policies which match the filter criteria"
  ],
  [
    "queryCombinedFirewallPolicyMembers",
    "GET",
    "/policy/combined/firewall-members/v1",
    "Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. "
    "Returns a set of host details which match the filter criteria"
  ],
  [
    "queryCombinedFirewallPolicies",
    "GET",
    "/policy/combined/firewall/v1",
    "Search for Firewall Policies in your environment by providing an FQL filter and paging details. "
    "Returns a set of Firewall Policies which match the filter criteria"
  ],
  [
    "queryCombinedPreventionPolicyMembers",
    "GET",
    "/policy/combined/prevention-members/v1",
    "Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. "
    "Returns a set of host details which match the filter criteria"
  ],
  [
    "queryCombinedPreventionPolicies",
    "GET",
    "/policy/combined/prevention/v1",
    "Search for Prevention Policies in your environment by providing an FQL filter and paging details. "
    "Returns a set of Prevention Policies which match the filter criteria"
  ],
  [
    "revealUninstallToken",
    "POST",
    "/policy/combined/reveal-uninstall-token/v1",
    "Reveals an uninstall token for a specific device. To retrieve the bulk maintenance token pass the "
    "value 'MAINTENANCE' as the value for 'device_id'"
  ],
  [
    "queryCombinedSensorUpdateBuilds",
    "GET",
    "/policy/combined/sensor-update-builds/v1",
    "Retrieve available builds for use with Sensor Update Policies"
  ],
  [
    "queryCombinedSensorUpdatePolicyMembers",
    "GET",
    "/policy/combined/sensor-update-members/v1",
    "Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. "
    "Returns a set of host details which match the filter criteria"
  ],
  [
    "queryCombinedSensorUpdatePolicies",
    "GET",
    "/policy/combined/sensor-update/v1",
    "Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. "
    "Returns a set of Sensor Update Policies which match the filter criteria"
  ],
  [
    "queryCombinedSensorUpdatePoliciesV2",
    "GET",
    "/policy/combined/sensor-update/v2",
    "Search for Sensor Update Policies with additional support for uninstall protection in your environment by "
    "providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria"
  ],
  [
    "performDeviceControlPoliciesAction",
    "POST",
    "/policy/entities/device-control-actions/v1",
    "Perform the specified action on the Device Control Policies specified in the request"
  ],
  [
    "setDeviceControlPoliciesPrecedence",
    "POST",
    "/policy/entities/device-control-precedence/v1",
    "Sets the precedence of Device Control Policies based on the order of IDs specified in the request. "
    "The first ID specified will have the highest precedence and the last ID specified will have the lowest. "
    "You must specify all non-Default Policies for a platform when updating precedence"
  ],
  [
    "getDeviceControlPolicies",
    "GET",
    "/policy/entities/device-control/v1?ids={}",
    "Retrieve a set of Device Control Policies by specifying their IDs"
  ],
  [
    "createDeviceControlPolicies",
    "POST",
    "/policy/entities/device-control/v1",
    "Create Device Control Policies by specifying details about the policy to create"
  ],
  [
    "updateDeviceControlPolicies",
    "PATCH",
    "/policy/entities/device-control/v1",
    "Update Device Control Policies by specifying the ID of the policy and details to update"
  ],
  [
    "deleteDeviceControlPolicies",
    "DELETE",
    "/policy/entities/device-control/v1?ids={}",
    "Delete a set of Device Control Policies by specifying their IDs"
  ],
  [
    "performFirewallPoliciesAction",
    "POST",
    "/policy/entities/firewall-actions/v1",
    "Perform the specified action on the Firewall Policies specified in the request"
  ],
  [
    "setFirewallPoliciesPrecedence",
    "POST",
    "/policy/entities/firewall-precedence/v1",
    "Sets the precedence of Firewall Policies based on the order of IDs specified in the request. "
    "The first ID specified will have the highest precedence and the last ID specified will have the lowest. "
    "You must specify all non-Default Policies for a platform when updating precedence"
  ],
  [
    "getFirewallPolicies",
    "GET",
    "/policy/entities/firewall/v1?ids={}",
    "Retrieve a set of Firewall Policies by specifying their IDs"
  ],
  [
    "createFirewallPolicies",
    "POST",
    "/policy/entities/firewall/v1",
    "Create Firewall Policies by specifying details about the policy to create"
  ],
  [
    "updateFirewallPolicies",
    "PATCH",
    "/policy/entities/firewall/v1",
    "Update Firewall Policies by specifying the ID of the policy and details to update"
  ],
  [
    "deleteFirewallPolicies",
    "DELETE",
    "/policy/entities/firewall/v1?ids={}",
    "Delete a set of Firewall Policies by specifying their IDs"
  ],
  [
    "getIOAExclusionsV1",
    "GET",
    "/policy/entities/ioa-exclusions/v1?ids={}",
    "Get a set of IOA Exclusions by specifying their IDs"
  ],
  [
    "createIOAExclusionsV1",
    "POST",
    "/policy/entities/ioa-exclusions/v1",
    "Create the IOA exclusions"
  ],
  [
    "updateIOAExclusionsV1",
    "PATCH",
    "/policy/entities/ioa-exclusions/v1",
    "Update the IOA exclusions"
  ],
  [
    "deleteIOAExclusionsV1",
    "DELETE",
    "/policy/entities/ioa-exclusions/v1?ids={}",
    "Delete the IOA exclusions by id"
  ],
  [
    "getMLExclusionsV1",
    "GET",
    "/policy/entities/ml-exclusions/v1?ids={}",
    "Get a set of ML Exclusions by specifying their IDs"
  ],
  [
    "createMLExclusionsV1",
    "POST",
    "/policy/entities/ml-exclusions/v1",
    "Create the ML exclusions"
  ],
  [
    "updateMLExclusionsV1",
    "PATCH",
    "/policy/entities/ml-exclusions/v1",
    "Update the ML exclusions"
  ],
  [
    "deleteMLExclusionsV1",
    "DELETE",
    "/policy/entities/ml-exclusions/v1?ids={}",
    "Delete the ML exclusions by id"
  ],
  [
    "performPreventionPoliciesAction",
    "POST",
    "/policy/entities/prevention-actions/v1",
    "Perform the specified action on the Prevention Policies specified in the request"
  ],
  [
    "setPreventionPoliciesPrecedence",
    "POST",
    "/policy/entities/prevention-precedence/v1",
    "Sets the precedence of Prevention Policies based on the order of IDs specified in the request. "
    "The first ID specified will have the highest precedence and the last ID specified will have the lowest. "
    "You must specify all non-Default Policies for a platform when updating precedence"
  ],
  [
    "getPreventionPolicies",
    "GET",
    "/policy/entities/prevention/v1?ids={}",
    "Retrieve a set of Prevention Policies by specifying their IDs"
  ],
  [
    "createPreventionPolicies",
    "POST",
    "/policy/entities/prevention/v1",
    "Create Prevention Policies by specifying details about the policy to create"
  ],
  [
    "updatePreventionPolicies",
    "PATCH",
    "/policy/entities/prevention/v1",
    "Update Prevention Policies by specifying the ID of the policy and details to update"
  ],
  [
    "deletePreventionPolicies",
    "DELETE",
    "/policy/entities/prevention/v1?ids={}",
    "Delete a set of Prevention Policies by specifying their IDs"
  ],
  [
    "performSensorUpdatePoliciesAction",
    "POST",
    "/policy/entities/sensor-update-actions/v1",
    "Perform the specified action on the Sensor Update Policies specified in the request"
  ],
  [
    "setSensorUpdatePoliciesPrecedence",
    "POST",
    "/policy/entities/sensor-update-precedence/v1",
    "Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request. "
    "The first ID specified will have the highest precedence and the last ID specified will have the lowest. "
    "You must specify all non-Default Policies for a platform when updating precedence"
  ],
  [
    "getSensorUpdatePolicies",
    "GET",
    "/policy/entities/sensor-update/v1?ids={}",
    "Retrieve a set of Sensor Update Policies by specifying their IDs"
  ],
  [
    "createSensorUpdatePolicies",
    "POST",
    "/policy/entities/sensor-update/v1",
    "Create Sensor Update Policies by specifying details about the policy to create"
  ],
  [
    "updateSensorUpdatePolicies",
    "PATCH",
    "/policy/entities/sensor-update/v1",
    "Update Sensor Update Policies by specifying the ID of the policy and details to update"
  ],
  [
    "deleteSensorUpdatePolicies",
    "DELETE",
    "/policy/entities/sensor-update/v1?ids={}",
    "Delete a set of Sensor Update Policies by specifying their IDs"
  ],
  [
    "getSensorUpdatePoliciesV2",
    "GET",
    "/policy/entities/sensor-update/v2?ids={}",
    "Retrieve a set of Sensor Update Policies with additional support for uninstall protection by specifying their IDs"
  ],
  [
    "createSensorUpdatePoliciesV2",
    "POST",
    "/policy/entities/sensor-update/v2",
    "Create Sensor Update Policies by specifying details about the policy to create with "
    "additional support for uninstall protection"
  ],
  [
    "updateSensorUpdatePoliciesV2",
    "PATCH",
    "/policy/entities/sensor-update/v2",
    "Update Sensor Update Policies by specifying the ID of the policy and details to update with "
    "additional support for uninstall protection"
  ],
  [
    "getSensorVisibilityExclusionsV1",
    "GET",
    "/policy/entities/sv-exclusions/v1?ids={}",
    "Get a set of Sensor Visibility Exclusions by specifying their IDs"
  ],
  [
    "createSVExclusionsV1",
    "POST",
    "/policy/entities/sv-exclusions/v1",
    "Create the sensor visibility exclusions"
  ],
  [
    "updateSensorVisibilityExclusionsV1",
    "PATCH",
    "/policy/entities/sv-exclusions/v1",
    "Update the sensor visibility exclusions"
  ],
  [
    "deleteSensorVisibilityExclusionsV1",
    "DELETE",
    "/policy/entities/sv-exclusions/v1?ids={}",
    "Delete the sensor visibility exclusions by id"
  ],
  [
    "queryDeviceControlPolicyMembers",
    "GET",
    "/policy/queries/device-control-members/v1",
    "Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. "
    "Returns a set of Agent IDs which match the filter criteria"
  ],
  [
    "queryDeviceControlPolicies",
    "GET",
    "/policy/queries/device-control/v1",
    "Search for Device Control Policies in your environment by providing an FQL filter and paging details. "
    "Returns a set of Device Control Policy IDs which match the filter criteria"
  ],
  [
    "queryFirewallPolicyMembers",
    "GET",
    "/policy/queries/firewall-members/v1",
    "Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. "
    "Returns a set of Agent IDs which match the filter criteria"
  ],
  [
    "queryFirewallPolicies",
    "GET",
    "/policy/queries/firewall/v1",
    "Search for Firewall Policies in your environment by providing an FQL filter and paging details. "
    "Returns a set of Firewall Policy IDs which match the filter criteria"
  ],
  [
    "queryIOAExclusionsV1",
    "GET",
    "/policy/queries/ioa-exclusions/v1",
    "Search for IOA exclusions."
  ],
  [
    "queryMLExclusionsV1",
    "GET",
    "/policy/queries/ml-exclusions/v1",
    "Search for ML exclusions."
  ],
  [
    "queryPreventionPolicyMembers",
    "GET",
    "/policy/queries/prevention-members/v1",
    "Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. "
    "Returns a set of Agent IDs which match the filter criteria"
  ],
  [
    "queryPreventionPolicies",
    "GET",
    "/policy/queries/prevention/v1",
    "Search for Prevention Policies in your environment by providing an FQL filter and paging details. "
    "Returns a set of Prevention Policy IDs which match the filter criteria"
  ],
  [
    "querySensorUpdatePolicyMembers",
    "GET",
    "/policy/queries/sensor-update-members/v1",
    "Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging "
    "details. Returns a set of Agent IDs which match the filter criteria"
  ],
  [
    "querySensorUpdatePolicies",
    "GET",
    "/policy/queries/sensor-update/v1",
    "Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. "
    "Returns a set of Sensor Update Policy IDs which match the filter criteria"
  ],
  [
    "querySensorVisibilityExclusionsV1",
    "GET",
    "/policy/queries/sv-exclusions/v1",
    "Search for sensor visibility exclusions."
  ],
  [
    "entities_processes",
    "GET",
    "/processes/entities/processes/v1?ids={}",
    "For the provided ProcessID retrieve the process details"
  ],
  [
    "RTR_AggregateSessions",
    "POST",
    "/real-time-response/aggregates/sessions/GET/v1",
    "Get aggregates on session data."
  ],
  [
    "BatchActiveResponderCmd",
    "POST",
    "/real-time-response/combined/batch-active-responder-command/v1",
    "Batch executes a RTR active-responder command across the hosts mapped to the given batch ID."
  ],
  [
    "BatchAdminCmd",
    "POST",
    "/real-time-response/combined/batch-admin-command/v1",
    "Batch executes a RTR administrator command across the hosts mapped to the given batch ID."
  ],
  [
    "BatchCmd",
    "POST",
    "/real-time-response/combined/batch-command/v1",
    "Batch executes a RTR read-only command across the hosts mapped to the given batch ID."
  ],
  [
    "BatchGetCmdStatus",
    "GET",
    "/real-time-response/combined/batch-get-command/v1",
    "Retrieves the status of the specified batch get command.  Will return successful files when they are finished processing."
  ],
  [
    "BatchGetCmd",
    "POST",
    "/real-time-response/combined/batch-get-command/v1",
    "Batch executes `get` command across hosts to retrieve files. After this call is made "
    "`GET /real-time-response/combined/batch-get-command/v1` is used to query for the results."
  ],
  [
    "BatchInitSessions",
    "POST",
    "/real-time-response/combined/batch-init-session/v1",
    "Batch initialize a RTR session on multiple hosts.  Before any RTR commands can be used, "
    "an active session is needed on the host."
  ],
  [
    "BatchRefreshSessions",
    "POST",
    "/real-time-response/combined/batch-refresh-session/v1",
    "Batch refresh a RTR session on multiple hosts. RTR sessions will expire after 10 minutes unless refreshed."
  ],
  [
    "RTR_CheckActiveResponderCommandStatus",
    "GET",
    "/real-time-response/entities/active-responder-command/v1",
    "Get status of an executed active-responder command on a single host."
  ],
  [
    "RTR_ExecuteActiveResponderCommand",
    "POST",
    "/real-time-response/entities/active-responder-command/v1",
    "Execute an active responder command on a single host."
  ],
  [
    "RTR_CheckAdminCommandStatus",
    "GET",
    "/real-time-response/entities/admin-command/v1",
    "Get status of an executed RTR administrator command on a single host."
  ],
  [
    "RTR_ExecuteAdminCommand",
    "POST",
    "/real-time-response/entities/admin-command/v1",
    "Execute a RTR administrator command on a single host."
  ],
  [
    "RTR_CheckCommandStatus",
    "GET",
    "/real-time-response/entities/command/v1",
    "Get status of an executed command on a single host."
  ],
  [
    "RTR_ExecuteCommand",
    "POST",
    "/real-time-response/entities/command/v1",
    "Execute a command on a single host."
  ],
  [
    "RTR_GetExtractedFileContents",
    "GET",
    "/real-time-response/entities/extracted-file-contents/v1",
    "Get RTR extracted file contents for specified session and sha256."
  ],
  [
    "RTR_ListFiles",
    "GET",
    "/real-time-response/entities/file/v1",
    "Get a list of files for the specified RTR session."
  ],
  [
    "RTR_DeleteFile",
    "DELETE",
    "/real-time-response/entities/file/v1?ids={}",
    "Delete a RTR session file."
  ],
  [
    "RTR_GetPut_Files",
    "GET",
    "/real-time-response/entities/put-files/v1?ids={}",
    "Get put-files based on the ID's given. These are used for the RTR `put` command."
  ],
  [
    "RTR_CreatePut_Files",
    "POST",
    "/real-time-response/entities/put-files/v1",
    "Upload a new put-file to use for the RTR `put` command."
  ],
  [
    "RTR_DeletePut_Files",
    "DELETE",
    "/real-time-response/entities/put-files/v1?ids={}",
    "Delete a put-file based on the ID given.  Can only delete one file at a time."
  ],
  [
    "RTR_ListQueuedSessions",
    "POST",
    "/real-time-response/entities/queued-sessions/GET/v1",
    "Get queued session metadata by session ID."
  ],
  [
    "RTR_DeleteQueuedSession",
    "DELETE",
    "/real-time-response/entities/queued-sessions/command/v1",
    "Delete a queued session command"
  ],
  [
    "RTR_PulseSession",
    "POST",
    "/real-time-response/entities/refresh-session/v1",
    "Refresh a session timeout on a single host."
  ],
  [
    "RTR_GetScripts",
    "GET",
    "/real-time-response/entities/scripts/v1?ids={}",
    "Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command."
  ],
  [
    "RTR_CreateScripts",
    "POST",
    "/real-time-response/entities/scripts/v1",
    "Upload a new custom-script to use for the RTR `runscript` command."
  ],
  [
    "RTR_UpdateScripts",
    "PATCH",
    "/real-time-response/entities/scripts/v1",
    "Upload a new scripts to replace an existing one."
  ],
  [
    "RTR_DeleteScripts",
    "DELETE",
    "/real-time-response/entities/scripts/v1?ids={}",
    "Delete a custom-script based on the ID given.  Can only delete one script at a time."
  ],
  [
    "RTR_ListSessions",
    "POST",
    "/real-time-response/entities/sessions/GET/v1",
    "Get session metadata by session id."
  ],
  [
    "RTR_InitSession",
    "POST",
    "/real-time-response/entities/sessions/v1",
    "Initialize a new session with the RTR cloud."
  ],
  [
    "RTR_DeleteSession",
    "DELETE",
    "/real-time-response/entities/sessions/v1",
    "Delete a session."
  ],
  [
    "RTR_ListPut_Files",
    "GET",
    "/real-time-response/queries/put-files/v1",
    "Get a list of put-file ID's that are available to the user for the `put` command."
  ],
  [
    "RTR_ListScripts",
    "GET",
    "/real-time-response/queries/scripts/v1",
    "Get a list of custom-script ID's that are available to the user for the `runscript` command."
  ],
  [
    "RTR_ListAllSessions",
    "GET",
    "/real-time-response/queries/sessions/v1",
    "Get a list of session_ids."
  ],
  [
    "GetSampleV2",
    "GET",
    "/samples/entities/samples/v2?ids={}",
    "Retrieves the file associated with the given ID (SHA256)"
  ],
  [
    "UploadSampleV2",
    "POST",
    "/samples/entities/samples/v2",
    "Upload a file for sandbox analysis. After uploading, use `/falconx/entities/submissions/v1` to start analyzing the file."
  ],
  [
    "DeleteSampleV2",
    "DELETE",
    "/samples/entities/samples/v2?ids={}",
    "Removes a sample, including file, meta and submissions from the collection"
  ],
  [
    "GetSampleV3",
    "GET",
    "/samples/entities/samples/v3?ids={}",
    "Retrieves the file associated with the given ID (SHA256)"
  ],
  [
    "UploadSampleV3",
    "POST",
    "/samples/entities/samples/v3",
    "Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint."
  ],
  [
    "DeleteSampleV3",
    "DELETE",
    "/samples/entities/samples/v3?ids={}",
    "Removes a sample, including file, meta and submissions from the collection"
  ],
  [
    "QuerySampleV1",
    "POST",
    "/samples/queries/samples/GET/v1",
    "Retrieves a list with sha256 of samples that exist and customer has rights to access them, "
    "maximum number of accepted items is 200"
  ],
  [
    "GetScansAggregates",
    "POST",
    "/scanner/aggregates/scans/GET/v1",
    "Get scans aggregations as specified via json in request body."
  ],
  [
    "GetScans",
    "GET",
    "/scanner/entities/scans/v1?ids={}",
    "Check the status of a volume scan. Time required for analysis increases with the number of "
    "samples in a volume but usually it should take less than 1 minute"
  ],
  [
    "ScanSamples",
    "POST",
    "/scanner/entities/scans/v1",
    "Submit a volume of files for ml scanning. Time required for analysis increases with the number "
    "of samples in a volume but usually it should take less than 1 minute"
  ],
  [
    "QuerySubmissionsMixin0",
    "GET",
    "/scanner/queries/scans/v1",
    "Find IDs for submitted scans by providing an FQL filter and paging details. "
    "Returns a set of volume IDs that match your criteria."
  ],
  [
    "GetCombinedSensorInstallersByQuery",
    "GET",
    "/sensors/combined/installers/v1",
    "Get sensor installer details by provided query"
  ],
  [
    "refreshActiveStreamSession",
    "POST",
    "/sensors/entities/datafeed-actions/v1/{}",
    "Refresh an active event stream. Use the URL shown in a GET /sensors/entities/datafeed/v2 response."
  ],
  [
    "listAvailableStreamsOAuth2",
    "GET",
    "/sensors/entities/datafeed/v2",
    "Discover all event streams in your environment"
  ],
  [
    "DownloadSensorInstallerById",
    "GET",
    "/sensors/entities/download-installer/v1",
    "Download sensor installer by SHA256 ID"
  ],
  [
    "GetSensorInstallersEntities",
    "GET",
    "/sensors/entities/installers/v1?ids={}",
    "Get sensor installer details by provided SHA256 IDs"
  ],
  [
    "GetSensorInstallersCCIDByQuery",
    "GET",
    "/sensors/queries/installers/ccid/v1",
    "Get CCID to use with sensor installers"
  ],
  [
    "GetSensorInstallersByQuery",
    "GET",
    "/sensors/queries/installers/v1",
    "Get sensor installer IDs by provided query"
  ],
  [
    "GetCSPMPolicy",
    "GET",
    "/settings/entities/policy-details/v1?ids={}",
    "Given a policy ID, returns detailed policy information."
  ],
  [
    "GetCSPMPolicySettings",
    "GET",
    "/settings/entities/policy/v1",
    "Returns information about current policy settings."
  ],
  [
    "UpdateCSPMPolicySettings",
    "PATCH",
    "/settings/entities/policy/v1",
    "Updates a policy setting - can be used to override policy severity or to disable a policy entirely."
  ],
  [
    "GetCSPMScanSchedule",
    "GET",
    "/settings/scan-schedule/v1",
    "Returns scan schedule configuration for one or more cloud platforms."
  ],
  [
    "UpdateCSPMScanSchedule",
    "POST",
    "/settings/scan-schedule/v1",
    "Updates scan schedule configuration for one or more cloud platforms."
  ],
  [
    "getVulnerabilities",
    "GET",
    "/spotlight/entities/vulnerabilities/v2?ids={}",
    "Get details on vulnerabilities by providing one or more IDs"
  ],
  [
    "queryVulnerabilities",
    "GET",
    "/spotlight/queries/vulnerabilities/v1",
    "Search for Vulnerabilities in your environment by providing an FQL filter and paging details. "
    "Returns a set of Vulnerability IDs which match the filter criteria"
  ],
  [
    "GetRoles",
    "GET",
    "/user-roles/entities/user-roles/v1?ids={}",
    "Get info about a role"
  ],
  [
    "GrantUserRoleIds",
    "POST",
    "/user-roles/entities/user-roles/v1",
    "Assign one or more roles to a user"
  ],
  [
    "RevokeUserRoleIds",
    "DELETE",
    "/user-roles/entities/user-roles/v1?ids={}",
    "Revoke one or more roles from a user"
  ],
  [
    "GetAvailableRoleIds",
    "GET",
    "/user-roles/queries/user-role-ids-by-cid/v1",
    "Show role IDs for all roles available in your customer account. For more information on each role, "
    "provide the role ID to `/customer/entities/roles/v1`."
  ],
  [
    "GetUserRoleIds",
    "GET",
    "/user-roles/queries/user-role-ids-by-user-uuid/v1",
    "Show role IDs of roles assigned to a user. For more information on each role, "
    "provide the role ID to `/customer/entities/roles/v1`."
  ],
  [
    "RetrieveUser",
    "GET",
    "/users/entities/users/v1?ids={}",
    "Get info about a user"
  ],
  [
    "CreateUser",
    "POST",
    "/users/entities/users/v1",
    "Create a new user. After creating a user, assign one or more roles with POST /user-roles/entities/user-roles/v1"
  ],
  [
    "UpdateUser",
    "PATCH",
    "/users/entities/users/v1",
    "Modify an existing user's first or last name"
  ],
  [
    "DeleteUser",
    "DELETE",
    "/users/entities/users/v1",
    "Delete a user permanently"
  ],
  [
    "RetrieveEmailsByCID",
    "GET",
    "/users/queries/emails-by-cid/v1",
    "List the usernames (usually an email address) for all users in your customer account"
  ],
  [
    "RetrieveUserUUIDsByCID",
    "GET",
    "/users/queries/user-uuids-by-cid/v1",
    "List user IDs for all users in your customer account. For more information on each user, "
    "provide the user ID to `/users/entities/user/v1`."
  ],
  [
    "RetrieveUserUUID",
    "GET",
    "/users/queries/user-uuids-by-email/v1",
    "Get a user's ID by providing a username (usually an email address)"
  ],
  #                                                                             .---.        .-----------
  #                                                                            /     \  __  /    ------
  #                                                                           / /     \(..)/    -----
  #  _____                                     __            __              //////   ' \/ `   ---
  # |     \.-----.-----.----.-----.----.---.-.|  |_.-----.--|  |            //// / // :    : ---
  # |  --  |  -__|  _  |   _|  -__|  __|  _  ||   _|  -__|  _  |           // /   /  /`    '--
  # |_____/|_____|   __|__| |_____|____|___._||____|_____|_____|          //          //..\\
  #              |__|                                                                UU    UU
  # The following operations reference legacy naming convention and are considered deprecated.
  # These operation IDs are maintained for backwards compatibility purposes only, Move all code
  # references to use the new operations IDs defined above that align with the IDs defined in
  # the service classes.
  [
    "entities.processes",
    "GET",
    "/processes/entities/processes/v1?ids={}",
    "For the provided ProcessID retrieve the process details"
  ],
  [
    "aggregate-events",
    "POST",
    "/fwmgr/aggregates/events/GET/v1",
    "Aggregate events for customer"
  ],
  [
    "aggregate-policy-rules",
    "POST",
    "/fwmgr/aggregates/policy-rules/GET/v1",
    "Aggregate rules within a policy for customer"
  ],
  [
    "aggregate-rule-groups",
    "POST",
    "/fwmgr/aggregates/rule-groups/GET/v1",
    "Aggregate rule groups for customer"
  ],
  [
    "aggregate-rules",
    "POST",
    "/fwmgr/aggregates/rules/GET/v1",
    "Aggregate rules for customer"
  ],
  [
    "get-events",
    "GET",
    "/fwmgr/entities/events/v1?ids={}",
    "Get events entities by ID and optionally version"
  ],
  [
    "get-firewall-fields",
    "GET",
    "/fwmgr/entities/firewall-fields/v1?ids={}",
    "Get the firewall field specifications by ID"
  ],
  [
    "get-platforms",
    "GET",
    "/fwmgr/entities/platforms/v1?ids={}",
    "Get platforms by ID, e.g., windows or mac or droid"
  ],
  [
    "get-policy-containers",
    "GET",
    "/fwmgr/entities/policies/v1?ids={}",
    "Get policy container entities by policy ID"
  ],
  [
    "update-policy-container",
    "PUT",
    "/fwmgr/entities/policies/v1",
    "Update an identified policy container"
  ],
  [
    "get-rule-groups",
    "GET",
    "/fwmgr/entities/rule-groups/v1?ids={}",
    "Get rule group entities by ID. These groups do not contain their rule entites, just the rule IDs in precedence order."
  ],
  [
    "create-rule-group",
    "POST",
    "/fwmgr/entities/rule-groups/v1",
    "Create new rule group on a platform for a customer with a name and description, and return the ID"
  ],
  [
    "update-rule-group",
    "PATCH",
    "/fwmgr/entities/rule-groups/v1",
    "Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules"
  ],
  [
    "delete-rule-groups",
    "DELETE",
    "/fwmgr/entities/rule-groups/v1?ids={}",
    "Delete rule group entities by ID"
  ],
  [
    "get-rules",
    "GET",
    "/fwmgr/entities/rules/v1?ids={}",
    "Get rule entities by ID (64-bit unsigned int as decimal string) or Family ID (32-character hexadecimal string)"
  ],
  [
    "query-events",
    "GET",
    "/fwmgr/queries/events/v1",
    "Find all event IDs matching the query with filter"
  ],
  [
    "query-firewall-fields",
    "GET",
    "/fwmgr/queries/firewall-fields/v1",
    "Get the firewall field specification IDs for the provided platform"
  ],
  [
    "query-platforms",
    "GET",
    "/fwmgr/queries/platforms/v1",
    "Get the list of platform names"
  ],
  [
    "query-policy-rules",
    "GET",
    "/fwmgr/queries/policy-rules/v1",
    "Find all firewall rule IDs matching the query with filter, and return them in precedence order"
  ],
  [
    "query-rule-groups",
    "GET",
    "/fwmgr/queries/rule-groups/v1",
    "Find all rule group IDs matching the query with filter"
  ],
  [
    "query-rules",
    "GET",
    "/fwmgr/queries/rules/v1",
    "Find all rule IDs matching the query with filter"
  ],
  [
    "audit-events-read",
    "GET",
    "/installation-tokens/entities/audit-events/v1?ids={}",
    "Gets the details of one or more audit events by id."
  ],
  [
    "customer-settings-read",
    "GET",
    "/installation-tokens/entities/customer-settings/v1",
    "Check current installation token settings."
  ],
  [
    "tokens-read",
    "GET",
    "/installation-tokens/entities/tokens/v1?ids={}",
    "Gets the details of one or more tokens by id."
  ],
  [
    "tokens-create",
    "POST",
    "/installation-tokens/entities/tokens/v1",
    "Creates a token."
  ],
  [
    "tokens-update",
    "PATCH",
    "/installation-tokens/entities/tokens/v1?ids={}",
    "Updates one or more tokens. Use this endpoint to edit labels, change expiration, revoke, or restore."
  ],
  [
    "tokens-delete",
    "DELETE",
    "/installation-tokens/entities/tokens/v1?ids={}",
    "Deletes a token immediately. To revoke a token, use PATCH /installation-tokens/entities/tokens/v1 instead."
  ],
  [
    "audit-events-query",
    "GET",
    "/installation-tokens/queries/audit-events/v1",
    "Search for audit events by providing an FQL filter and paging details."
  ],
  [
    "tokens-query",
    "GET",
    "/installation-tokens/queries/tokens/v1",
    "Search for tokens by providing an FQL filter and paging details."
  ],
  [
    "get-patterns",
    "GET",
    "/ioarules/entities/pattern-severities/v1?ids={}",
    "Get pattern severities by ID."
  ],
  [
    "get-platformsMixin0",
    "GET",
    "/ioarules/entities/platforms/v1?ids={}",
    "Get platforms by ID."
  ],
  [
    "get-rule-groupsMixin0",
    "GET",
    "/ioarules/entities/rule-groups/v1?ids={}",
    "Get rule groups by ID."
  ],
  [
    "create-rule-groupMixin0",
    "POST",
    "/ioarules/entities/rule-groups/v1",
    "Create a rule group for a platform with a name and an optional description. Returns the rule group."
  ],
  [
    "update-rule-groupMixin0",
    "PATCH",
    "/ioarules/entities/rule-groups/v1",
    "Update a rule group. The following properties can be modified: name, description, enabled."
  ],
  [
    "delete-rule-groupsMixin0",
    "DELETE",
    "/ioarules/entities/rule-groups/v1?ids={}",
    "Delete rule groups by ID."
  ],
  [
    "get-rule-types",
    "GET",
    "/ioarules/entities/rule-types/v1?ids={}",
    "Get rule types by ID."
  ],
  [
    "get-rules-get",
    "POST",
    "/ioarules/entities/rules/GET/v1",
    "Get rules by ID and optionally version in the following format: `ID[:version]`."
  ],
  [
    "get-rulesMixin0",
    "GET",
    "/ioarules/entities/rules/v1?ids={}",
    "Get rules by ID and optionally version in the following format: `ID[:version]`. "
    "The max number of IDs is constrained by URL size."
  ],
  [
    "create-rule",
    "POST",
    "/ioarules/entities/rules/v1",
    "Create a rule within a rule group. Returns the rule."
  ],
  [
    "update-rules",
    "PATCH",
    "/ioarules/entities/rules/v1",
    "Update rules within a rule group. Return the updated rules."
  ],
  [
    "delete-rules",
    "DELETE",
    "/ioarules/entities/rules/v1?ids={}",
    "Delete rules from a rule group by ID."
  ],
  [
    "query-patterns",
    "GET",
    "/ioarules/queries/pattern-severities/v1",
    "Get all pattern severity IDs."
  ],
  [
    "query-platformsMixin0",
    "GET",
    "/ioarules/queries/platforms/v1",
    "Get all platform IDs."
  ],
  [
    "query-rule-groups-full",
    "GET",
    "/ioarules/queries/rule-groups-full/v1",
    "Find all rule groups matching the query with optional filter."
  ],
  [
    "query-rule-groupsMixin0",
    "GET",
    "/ioarules/queries/rule-groups/v1",
    "Finds all rule group IDs matching the query with optional filter."
  ],
  [
    "query-rule-types",
    "GET",
    "/ioarules/queries/rule-types/v1",
    "Get all rule type IDs."
  ],
  [
    "query-rulesMixin0",
    "GET",
    "/ioarules/queries/rules/v1",
    "Finds all rule IDs matching the query with optional filter."
  ],
  [
    "RTR-AggregateSessions",
    "POST",
    "/real-time-response/aggregates/sessions/GET/v1",
    "Get aggregates on session data."
  ],
  [
    "RTR-CheckActiveResponderCommandStatus",
    "GET",
    "/real-time-response/entities/active-responder-command/v1",
    "Get status of an executed active-responder command on a single host."
  ],
  [
    "RTR-ExecuteActiveResponderCommand",
    "POST",
    "/real-time-response/entities/active-responder-command/v1",
    "Execute an active responder command on a single host."
  ],
  [
    "RTR-CheckAdminCommandStatus",
    "GET",
    "/real-time-response/entities/admin-command/v1",
    "Get status of an executed RTR administrator command on a single host."
  ],
  [
    "RTR-ExecuteAdminCommand",
    "POST",
    "/real-time-response/entities/admin-command/v1",
    "Execute a RTR administrator command on a single host."
  ],
  [
    "RTR-CheckCommandStatus",
    "GET",
    "/real-time-response/entities/command/v1",
    "Get status of an executed command on a single host."
  ],
  [
    "RTR-ExecuteCommand",
    "POST",
    "/real-time-response/entities/command/v1",
    "Execute a command on a single host."
  ],
  [
    "RTR-GetExtractedFileContents",
    "GET",
    "/real-time-response/entities/extracted-file-contents/v1",
    "Get RTR extracted file contents for specified session and sha256."
  ],
  [
    "RTR-ListFiles",
    "GET",
    "/real-time-response/entities/file/v1",
    "Get a list of files for the specified RTR session."
  ],
  [
    "RTR-DeleteFile",
    "DELETE",
    "/real-time-response/entities/file/v1?ids={}",
    "Delete a RTR session file."
  ],
  [
    "RTR-GetPut-Files",
    "GET",
    "/real-time-response/entities/put-files/v1?ids={}",
    "Get put-files based on the ID's given. These are used for the RTR `put` command."
  ],
  [
    "RTR-CreatePut-Files",
    "POST",
    "/real-time-response/entities/put-files/v1",
    "Upload a new put-file to use for the RTR `put` command."
  ],
  [
    "RTR-DeletePut-Files",
    "DELETE",
    "/real-time-response/entities/put-files/v1?ids={}",
    "Delete a put-file based on the ID given.  Can only delete one file at a time."
  ],
  [
    "RTR-ListQueuedSessions",
    "POST",
    "/real-time-response/entities/queued-sessions/GET/v1",
    "Get queued session metadata by session ID."
  ],
  [
    "RTR-DeleteQueuedSession",
    "DELETE",
    "/real-time-response/entities/queued-sessions/command/v1",
    "Delete a queued session command"
  ],
  [
    "RTR-PulseSession",
    "POST",
    "/real-time-response/entities/refresh-session/v1",
    "Refresh a session timeout on a single host."
  ],
  [
    "RTR-GetScripts",
    "GET",
    "/real-time-response/entities/scripts/v1?ids={}",
    "Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command."
  ],
  [
    "RTR-CreateScripts",
    "POST",
    "/real-time-response/entities/scripts/v1",
    "Upload a new custom-script to use for the RTR `runscript` command."
  ],
  [
    "RTR-UpdateScripts",
    "PATCH",
    "/real-time-response/entities/scripts/v1",
    "Upload a new scripts to replace an existing one."
  ],
  [
    "RTR-DeleteScripts",
    "DELETE",
    "/real-time-response/entities/scripts/v1?ids={}",
    "Delete a custom-script based on the ID given.  Can only delete one script at a time."
  ],
  [
    "RTR-ListSessions",
    "POST",
    "/real-time-response/entities/sessions/GET/v1",
    "Get session metadata by session id."
  ],
  [
    "RTR-InitSession",
    "POST",
    "/real-time-response/entities/sessions/v1",
    "Initialize a new session with the RTR cloud."
  ],
  [
    "RTR-DeleteSession",
    "DELETE",
    "/real-time-response/entities/sessions/v1",
    "Delete a session."
  ],
  [
    "RTR-ListPut-Files",
    "GET",
    "/real-time-response/queries/put-files/v1",
    "Get a list of put-file ID's that are available to the user for the `put` command."
  ],
  [
    "RTR-ListScripts",
    "GET",
    "/real-time-response/queries/scripts/v1",
    "Get a list of custom-script ID's that are available to the user for the `runscript` command."
  ],
  [
    "RTR-ListAllSessions",
    "GET",
    "/real-time-response/queries/sessions/v1",
    "Get a list of session_ids."
  ]
]
