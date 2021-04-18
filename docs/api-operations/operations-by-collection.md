# Operations by Collection

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Table of Contents

|  |  |  |  |
| :--- | :--- | :--- | :--- |
| [Cloud Connect AWS](operations-by-collection.md#Cloud-Connect-AWS) | [D4C Registration](operations-by-collection.md#D4C-Registration) | [CSPM Registration](operations-by-collection.md#CSPM-Registration) | [Detects](operations-by-collection.md#Detects) |
| [Host Group](operations-by-collection.md#Host-Group) | [Hosts](operations-by-collection.md#Hosts) | [Falcon Complete Dashboard](operations-by-collection.md#Falcon-Complete-Dashboard) | [Falconx Sandbox](operations-by-collection.md#Falconx-Sandbox) |
| [Firewall Management](operations-by-collection.md#Firewall-Management) | [Incidents](operations-by-collection.md#Incidents) | [IOCs](operations-by-collection.md#IOCs) | [Installation Tokens](operations-by-collection.md#Installation-Tokens) |
| [Intel](operations-by-collection.md#Intel) | [Custom IOA](operations-by-collection.md#Custom-IOA) | [Malquery](operations-by-collection.md#Malquery) | [MSSP \(Flight Control\)](operations-by-collection.md#MSSP-Flight-Control) |
| [OAuth2](operations-by-collection.md#OAuth2) | [Overwatch Dashboard](operations-by-collection.md#Overwatch-Dashboard) | [Device Control Policies](operations-by-collection.md#Device-Control-Policies) | [Firewall Policies](operations-by-collection.md#Firewall-Policies) |
| [Prevention Policies](operations-by-collection.md#Prevention-Policies) | [Sensor Update Policies](operations-by-collection.md#Sensor-Update-Policies) | [IOA Exclusions](operations-by-collection.md#IOA-Exclusions) | [ML Exclusions](operations-by-collection.md#ML-Exclusions) |
| [Sensor Visibility Exclusions](operations-by-collection.md#Sensor-Visibility-Exclusions) | [Real Time Response](operations-by-collection.md#Real-Time-Response) | [Real Time Response Admin](operations-by-collection.md#Real-Time-Response-Admin) | [Sample Uploads](operations-by-collection.md#Sample-Uploads) |
| [Quick Scan](operations-by-collection.md#Quick-Scan) | [Sensor Download](operations-by-collection.md#Sensor-Download) | [Event Streams](operations-by-collection.md#Event-Streams) | [Spotlight Vulnerabilities](operations-by-collection.md#Spotlight-Vulnerabilities) |
| [User Management](operations-by-collection.md#User-Management) | [Zero Trust Assessment](operations-by-collection.md#Zero-Trust-Assessment) |  |  |

## All Operations by Service Collection

### Cloud Connect AWS

| Operation ID | Description |
| :--- | :--- |
| [QueryAWSAccounts](../service-collections/cloud-connect-aws.md#QueryAWSAccounts) | Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS accounts which match the filter criteria |
| [GetAWSSettings](../service-collections/cloud-connect-aws.md#GetAWSSettings) | Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts |
| [GetAWSAccounts](../service-collections/cloud-connect-aws.md#GetAWSAccounts) | Retrieve a set of AWS Accounts by specifying their IDs |
| [ProvisionAWSAccounts](../service-collections/cloud-connect-aws.md#ProvisionAWSAccounts) | Provision AWS Accounts by specifying details about the accounts to provision |
| [DeleteAWSAccounts](../service-collections/cloud-connect-aws.md#DeleteAWSAccounts) | Delete a set of AWS Accounts by specifying their IDs |
| [UpdateAWSAccounts](../service-collections/cloud-connect-aws.md#UpdateAWSAccounts) | Update AWS Accounts by specifying the ID of the account and details to update |
| [CreateOrUpdateAWSSettings](../service-collections/cloud-connect-aws.md#CreateOrUpdateAWSSettings) | Create or update Global Settings which are applicable to all provisioned AWS accounts |
| [VerifyAWSAccountAccess](../service-collections/cloud-connect-aws.md#VerifyAWSAccountAccess) | Performs an Access Verification check on the specified AWS Account IDs |
| [QueryAWSAccountsForIDs](../service-collections/cloud-connect-aws.md#QueryAWSAccountsForIDs) | Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS account IDs which match the filter criteria |

### D4C Registration

| Operation ID | Description |
| :--- | :--- |
| [GetCSPMAzureAccount](../service-collections/d4c-registration.md#GetCSPMAzureAccount) | Return information about Azure account registration |
| [CreateCSPMAzureAccount](../service-collections/d4c-registration.md#CreateCSPMAzureAccount) | Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access. |
| [UpdateCSPMAzureAccountClientID](../service-collections/d4c-registration.md#UpdateCSPMAzureAccountClientID) | Update an Azure service account in our system by with the user-created client\_id created with the public key we've provided |
| [GetCSPMAzureUserScriptsAttachment](../service-collections/d4c-registration.md#GetCSPMAzureUserScriptsAttachment) | Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment |
| [GetCSPMAzureUserScripts](../service-collections/d4c-registration.md#GetCSPMAzureUserScripts) | Return a script for customer to run in their cloud environment to grant us access to their Azure environment |

### CSPM Registration

| Operation ID | Description |
| :--- | :--- |
| [GetCSPMAwsAccount](../service-collections/cspm-registration.md#GetCSPMAwsAccount) | Returns information about the current status of an AWS account. |
| [CreateCSPMAwsAccount](../service-collections/cspm-registration.md#CreateCSPMAwsAccount) | Creates a new account in our system for a customer and generates a script for them to run in their AWS cloud environment to grant us access. |
| [DeleteCSPMAwsAccount](../service-collections/cspm-registration.md#DeleteCSPMAwsAccount) | Deletes an existing AWS account or organization in our system. |
| [GetCSPMAwsConsoleSetupURLs](../service-collections/cspm-registration.md#GetCSPMAwsConsoleSetupURLs) | Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment. |
| [GetCSPMAwsAccountScriptsAttachment](../service-collections/cspm-registration.md#GetCSPMAwsAccountScriptsAttachment) | Return a script for customer to run in their cloud environment to grant us access to their AWS environment as a downloadable attachment. |
| [GetCSPMAzureAccount](../service-collections/cspm-registration.md#GetCSPMAzureAccount) | Return information about Azure account registration |
| [CreateCSPMAzureAccount](../service-collections/cspm-registration.md#CreateCSPMAzureAccount) | Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access. |
| [DeleteCSPMAzureAccount](../service-collections/cspm-registration.md#DeleteCSPMAzureAccount) | Deletes an Azure subscription from the system. |
| [UpdateCSPMAzureAccountClientID](../service-collections/cspm-registration.md#UpdateCSPMAzureAccountClientID) | Update an Azure service account in our system by with the user-created client\_id created with the public key we've provided |
| [GetCSPMAzureUserScriptsAttachment](../service-collections/cspm-registration.md#GetCSPMAzureUserScriptsAttachment) | Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment |
| [GetCSPMCGPAccount](../service-collections/d4c-registration.md#GetCSPMCGPAccount) | Returns information about the current status of an GCP account. |
| [CreateCSPMGCPAccount](../service-collections/d4c-registration.md#CreateCSPMGCPAccount) | Creates a new account in our system for a customer and generates a new service account for them to add access to in their GCP environment to grant us access. |
| [GetCSPMGCPUserScriptsAttachment](../service-collections/d4c-registration.md#GetCSPMGCPUserScriptsAttachment) | Return a script for customer to run in their cloud environment to grant us access to their GCP environment as a downloadable attachment |
| [GetCSPMGCPUserScripts](../service-collections/d4c-registration.md#GetCSPMGCPUserScripts) | Return a script for customer to run in their cloud environment to grant us access to their GCP environment |

### Detects

| Operation ID | Description |
| :--- | :--- |
| [GetAggregateDetects](../service-collections/detects.md#GetAggregateDetects) | Get detect aggregates as specified via json in request body. |
| [UpdateDetectsByIdsV2](../service-collections/detects.md#UpdateDetectsByIdsV2) | Modify the state, assignee, and visibility of detections |
| [GetDetectSummaries](../service-collections/detects.md#GetDetectSummaries) | View information about detections |
| [QueryDetects](../service-collections/detects.md#QueryDetects) | Search for detection IDs that match a given query |

### Host Group

| Operation ID | Description |
| :--- | :--- |
| [queryCombinedGroupMembers](../service-collections/host-group.md#queryCombinedGroupMembers) | Search for members of a Host Group in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedHostGroups](../service-collections/host-group.md#queryCombinedHostGroups) | Search for Host Groups in your environment by providing an FQL filter and paging details. Returns a set of Host Groups which match the filter criteria |

### Hosts

| Operation ID | Description |
| :--- | :--- |
| [PerformActionV2](../service-collections/hosts.md#PerformActionV2) | Take various actions on the hosts in your environment. Contain or lift containment on a host. Delete or restore a host. |
| [UpdateDeviceTags](../service-collections/hosts.md#UpdateDeviceTags) | Append or remove one or more Falcon Grouping Tags on one or more hosts. |
| [GetDeviceDetails](../service-collections/hosts.md#GetDeviceDetails) | Get details on one or more hosts by providing agent IDs \(AID\). You can get a host's agent IDs \(AIDs\) from the /devices/queries/devices/v1 endpoint, the Falcon console or the Streaming API |
| [performGroupAction](../service-collections/host-group.md#performGroupAction) | Perform the specified action on the Host Groups specified in the request |
| [getHostGroups](../service-collections/host-group.md#getHostGroups) | Retrieve a set of Host Groups by specifying their IDs |
| [createHostGroups](../service-collections/host-group.md#createHostGroups) | Create Host Groups by specifying details about the group to create |
| [deleteHostGroups](../service-collections/host-group.md#deleteHostGroups) | Delete a set of Host Groups by specifying their IDs |
| [updateHostGroups](../service-collections/host-group.md#updateHostGroups) | Update Host Groups by specifying the ID of the group and details to update |
| [QueryHiddenDevices](../service-collections/hosts.md#QueryHiddenDevices) | Retrieve hidden hosts that match the provided filter criteria. |
| [QueryDevicesByFilterScroll](../service-collections/hosts.md#QueryDevicesByFilterScroll) | Search for hosts in your environment by platform, hostname, IP, and other criteria with continuous pagination capability \(based on offset pointer which expires after 2 minutes with no maximum limit\) |
| [QueryDevicesByFilter](../service-collections/hosts.md#QueryDevicesByFilter) | Search for hosts in your environment by platform, hostname, IP, and other criteria. |
| [queryGroupMembers](../service-collections/host-group.md#queryGroupMembers) | Search for members of a Host Group in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [queryHostGroups](../service-collections/host-group.md#queryHostGroups) | Search for Host Groups in your environment by providing an FQL filter and paging details. Returns a set of Host Group IDs which match the filter criteria |

### Falcon Complete Dashboard

| Operation ID | Description |
| :--- | :--- |
| [AggregateAllowList](../service-collections/falcon-complete-dashboard.md#AggregateAllowList) | Retrieve aggregate allowlist ticket values based on the matched filter |
| [AggregateBlockList](../service-collections/falcon-complete-dashboard.md#AggregateBlockList) | Retrieve aggregate blocklist ticket values based on the matched filter |
| [AggregateDetections](../service-collections/falcon-complete-dashboard.md#AggregateDetections) | Retrieve aggregate detection values based on the matched filter |
| [AggregateDeviceCountCollection](../service-collections/falcon-complete-dashboard.md#AggregateDeviceCountCollection) | Retrieve aggregate host/devices count based on the matched filter |
| [AggregateEscalations](../service-collections/falcon-complete-dashboard.md#AggregateEscalations) | Retrieve aggregate escalation ticket values based on the matched filter |
| [AggregateFCIncidents](../service-collections/falcon-complete-dashboard.md#AggregateFCIncidents) | Retrieve aggregate incident values based on the matched filter |
| [AggregateRemediations](../service-collections/falcon-complete-dashboard.md#AggregateRemediations) | Retrieve aggregate remediation ticket values based on the matched filter |
| [QueryAllowListFilter](../service-collections/falcon-complete-dashboard.md#QueryAllowListFilter) | Retrieve allowlist tickets that match the provided filter criteria with scrolling enabled |
| [QueryBlockListFilter](../service-collections/falcon-complete-dashboard.md#QueryBlockListFilter) | Retrieve block listtickets that match the provided filter criteria with scrolling enabled |
| [QueryDetectionIdsByFilter](../service-collections/falcon-complete-dashboard.md#QueryDetectionIdsByFilter) | Retrieve DetectionsIds that match the provided FQL filter, criteria with scrolling enabled |
| [GetDeviceCountCollectionQueriesByFilter](../service-collections/falcon-complete-dashboard.md#GetDeviceCountCollectionQueriesByFilter) | Retrieve device count collection Ids that match the provided FQL filter, criteria with scrolling enabled |
| [QueryEscalationsFilter](../service-collections/falcon-complete-dashboard.md#QueryEscalationsFilter) | Retrieve escalation tickets that match the provided filter criteria with scrolling enabled |
| [QueryIncidentIdsByFilter](../service-collections/falcon-complete-dashboard.md#QueryIncidentIdsByFilter) | Retrieve incidents that match the provided filter criteria with scrolling enabled |
| [QueryRemediationsFilter](../service-collections/falcon-complete-dashboard.md#QueryRemediationsFilter) | Retrieve remediation tickets that match the provided filter criteria with scrolling enabled |

### Falconx Sandbox

| Operation ID | Description |
| :--- | :--- |
| [GetArtifacts](../service-collections/falconx-sandbox.md#GetArtifacts) | Download IOC packs, PCAP files, and other analysis artifacts. |
| [GetSummaryReports](../service-collections/falconx-sandbox.md#GetSummaryReports) | Get a short summary version of a sandbox report. |
| [GetReports](../service-collections/falconx-sandbox.md#GetReports) | Get a full sandbox report. |
| [DeleteReport](../service-collections/falconx-sandbox.md#DeleteReport) | Delete report based on the report ID. Operation can be checked for success by polling for the report ID on the report-summaries endpoint. |
| [GetSubmissions](../service-collections/falconx-sandbox.md#GetSubmissions) | Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. |
| [Submit](../service-collections/falconx-sandbox.md#Submit) | Submit an uploaded file or a URL for sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. |
| [QueryReports](../service-collections/falconx-sandbox.md#QueryReports) | Find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs that match your criteria. |
| [QuerySubmissions](../service-collections/falconx-sandbox.md#QuerySubmissions) | Find submission IDs for uploaded files by providing an FQL filter and paging details. Returns a set of submission IDs that match your criteria. |

### Firewall Management

| Operation ID | Description |
| :--- | :--- |
| [aggregate\_events](../service-collections/firewall-management.md#aggregate_events) | Aggregate events for customer |
| [aggregate\_policy\_rules](../service-collections/firewall-management.md#aggregate_policy_rules) | Aggregate rules within a policy for customer |
| [aggregate\_rule\_groups](../service-collections/firewall-management.md#aggregate_rule_groups) | Aggregate rule groups for customer |
| [aggregate\_rules](../service-collections/firewall-management.md#aggregate_rules) | Aggregate rules for customer |
| [get\_events](../service-collections/firewall-management.md#get_events) | Get events entities by ID and optionally version |
| [get\_firewall\_fields](../service-collections/firewall-management.md#get_firewall_fields) | Get the firewall field specifications by ID |
| [get\_platforms](../service-collections/firewall-management.md#get_platforms) | Get platforms by ID, e.g., windows or mac or droid |
| [get\_policy\_containers](../service-collections/firewall-management.md#get_policy_containers) | Get policy container entities by policy ID |
| [update\_policy\_container](../service-collections/firewall-management.md#update_policy_container) | Update an identified policy container |
| [get\_rule\_groups](../service-collections/firewall-management.md#get_rule_groups) | Get rule group entities by ID. These groups do not contain their rule entites, just the rule IDs in precedence order. |
| [create\_rule\_group](../service-collections/firewall-management.md#create_rule_group) | Create new rule group on a platform for a customer with a name and description, and return the ID |
| [delete\_rule\_groups](../service-collections/firewall-management.md#delete_rule_groups) | Delete rule group entities by ID |
| [update\_rule\_group](../service-collections/firewall-management.md#update_rule_group) | Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules |
| [get\_rules](../service-collections/firewall-management.md#get_rules) | Get rule entities by ID \(64-bit unsigned int as decimal string\) or Family ID \(32-character hexadecimal string\) |
| [query\_events](../service-collections/firewall-management.md#query_events) | Find all event IDs matching the query with filter |
| [query\_firewall\_fields](../service-collections/firewall-management.md#query_firewall_fields) | Get the firewall field specification IDs for the provided platform |
| [query\_platforms](../service-collections/firewall-management.md#query_platforms) | Get the list of platform names |
| [query\_policy\_rules](../service-collections/firewall-management.md#query_policy_rules) | Find all firewall rule IDs matching the query with filter, and return them in precedence order |
| [query\_rule\_groups](../service-collections/firewall-management.md#query_rule_groups) | Find all rule group IDs matching the query with filter |
| [query\_rules](../service-collections/firewall-management.md#query_rules) | Find all rule IDs matching the query with filter |

### Incidents

| Operation ID | Description |
| :--- | :--- |
| [CrowdScore](../service-collections/incidents.md#CrowdScore) | Query environment wide CrowdScore and return the entity data |
| [GetBehaviors](../service-collections/incidents.md#GetBehaviors) | Get details on behaviors by providing behavior IDs |
| [PerformIncidentAction](../service-collections/incidents.md#PerformIncidentAction) | Perform a set of actions on one or more incidents, such as adding tags or comments or updating the incident name or description |
| [GetIncidents](../service-collections/incidents.md#GetIncidents) | Get details on incidents by providing incident IDs |
| [QueryBehaviors](../service-collections/incidents.md#QueryBehaviors) | Search for behaviors by providing an FQL filter, sorting, and paging details |
| [QueryIncidents](../service-collections/incidents.md#QueryIncidents) | Search for incidents by providing an FQL filter, sorting, and paging details |

### IOCs

| Operation ID | Description |
| :--- | :--- |
| [DevicesCount](../service-collections/iocs.md#DevicesCount) | Number of hosts in your customer account that have observed a given custom IOC |
| [GetIOC](../service-collections/iocs.md#GetIOC) | Get an IOC by providing a type and value |
| [CreateIOC](../service-collections/iocs.md#CreateIOC) | Create a new IOC |
| [DeleteIOC](../service-collections/iocs.md#DeleteIOC) | Delete an IOC by providing a type and value |
| [UpdateIOC](../service-collections/iocs.md#UpdateIOC) | Update an IOC by providing a type and value |
| [DevicesRanOn](../service-collections/iocs.md#DevicesRanOn) | Find hosts that have observed a given custom IOC. For details about those hosts, use GET /devices/entities/devices/v1 |
| [QueryIOCs](../service-collections/iocs.md#QueryIOCs) | Search the custom IOCs in your customer account |
| [ProcessesRanOn](../service-collections/iocs.md#ProcessesRanOn) | Search for processes associated with a custom IOC |

### Installation Tokens

| Operation ID | Description |
| :--- | :--- |
| [audit\_events\_read](../service-collections/installation-tokens.md#audit_events_read) | Gets the details of one or more audit events by id. |
| [customer\_settings\_read](../service-collections/installation-tokens.md#customer_settings_read) | Check current installation token settings. |
| [tokens\_read](../service-collections/installation-tokens.md#tokens_read) | Gets the details of one or more tokens by id. |
| [tokens\_create](../service-collections/installation-tokens.md#tokens_create) | Creates a token. |
| [tokens\_delete](../service-collections/installation-tokens.md#tokens_delete) | Deletes a token immediately. To revoke a token, use PATCH /installation-tokens/entities/tokens/v1 instead. |
| [tokens\_update](../service-collections/installation-tokens.md#tokens_update) | Updates one or more tokens. Use this endpoint to edit labels, change expiration, revoke, or restore. |
| [audit\_events\_query](../service-collections/installation-tokens.md#audit_events_query) | Search for audit events by providing an FQL filter and paging details. |
| [tokens\_query](../service-collections/installation-tokens.md#tokens_query) | Search for tokens by providing an FQL filter and paging details. |

### Intel

| Operation ID | Description |
| :--- | :--- |
| [QueryIntelActorEntities](../service-collections/intel.md#QueryIntelActorEntities) | Get info about actors that match provided FQL filters. |
| [QueryIntelIndicatorEntities](../service-collections/intel.md#QueryIntelIndicatorEntities) | Get info about indicators that match provided FQL filters. |
| [QueryIntelReportEntities](../service-collections/intel.md#QueryIntelReportEntities) | Get info about reports that match provided FQL filters. |
| [GetIntelActorEntities](../service-collections/intel.md#GetIntelActorEntities) | Retrieve specific actors using their actor IDs. |
| [GetIntelIndicatorEntities](../service-collections/intel.md#GetIntelIndicatorEntities) | Retrieve specific indicators using their indicator IDs. |
| [GetIntelReportPDF](../service-collections/intel.md#GetIntelReportPDF) | Return a Report PDF attachment |
| [GetIntelReportEntities](../service-collections/intel.md#GetIntelReportEntities) | Retrieve specific reports using their report IDs. |
| [GetIntelRuleFile](../service-collections/intel.md#GetIntelRuleFile) | Download earlier rule sets. |
| [GetLatestIntelRuleFile](../service-collections/intel.md#GetLatestIntelRuleFile) | Download the latest rule set. |
| [GetIntelRuleEntities](../service-collections/intel.md#GetIntelRuleEntities) | Retrieve details for rule sets for the specified ids. |
| [QueryIntelActorIds](../service-collections/intel.md#QueryIntelActorIds) | Get actor IDs that match provided FQL filters. |
| [QueryIntelIndicatorIds](../service-collections/intel.md#QueryIntelIndicatorIds) | Get indicators IDs that match provided FQL filters. |
| [QueryIntelReportIds](../service-collections/intel.md#QueryIntelReportIds) | Get report IDs that match provided FQL filters. |
| [QueryIntelRuleIds](../service-collections/intel.md#QueryIntelRuleIds) | Search for rule IDs that match provided filter criteria. |

### Custom IOA

| Operation ID | Description |
| :--- | :--- |
| [get\_patterns](../service-collections/custom-ioa.md#get_patterns) | Get pattern severities by ID. |
| [get\_platformsMixin0](../service-collections/custom-ioa.md#get_platformsMixin0) | Get platforms by ID. |
| [get\_rule\_groupsMixin0](../service-collections/custom-ioa.md#get_rule_groupsMixin0) | Get rule groups by ID. |
| [create\_rule\_groupMixin0](../service-collections/custom-ioa.md#create_rule_groupMixin0) | Create a rule group for a platform with a name and an optional description. Returns the rule group. |
| [delete\_rule\_groupsMixin0](../service-collections/custom-ioa.md#delete_rule_groupsMixin0) | Delete rule groups by ID. |
| [update\_rule\_groupMixin0](../service-collections/custom-ioa.md#update_rule_groupMixin0) | Update a rule group. The following properties can be modified: name, description, enabled. |
| [get\_rule\_types](../service-collections/custom-ioa.md#get_rule_types) | Get rule types by ID. |
| [get\_rules\_get](../service-collections/custom-ioa.md#get_rules_get) | Get rules by ID and optionally version in the following format: `ID[:version]`. |
| [get\_rulesMixin0](../service-collections/custom-ioa.md#get_rulesMixin0) | Get rules by ID and optionally version in the following format: `ID[:version]`. The max number of IDs is constrained by URL size. |
| [create\_rule](../service-collections/custom-ioa.md#create_rule) | Create a rule within a rule group. Returns the rule. |
| [delete\_rules](../service-collections/custom-ioa.md#delete_rules) | Delete rules from a rule group by ID. |
| [update\_rules](../service-collections/custom-ioa.md#update_rules) | Update rules within a rule group. Return the updated rules. |
| [validate](../service-collections/custom-ioa.md#validate) | Validates field values and checks for matches if a test string is provided. |
| [query\_patterns](../service-collections/custom-ioa.md#query_patterns) | Get all pattern severity IDs. |
| [query\_platformsMixin0](../service-collections/custom-ioa.md#query_platformsMixin0) | Get all platform IDs. |
| [query\_rule\_groups\_full](../service-collections/custom-ioa.md#query_rule_groups_full) | Find all rule groups matching the query with optional filter. |
| [query\_rule\_groupsMixin0](../service-collections/custom-ioa.md#query_rule_groupsMixin0) | Finds all rule group IDs matching the query with optional filter. |
| [query\_rule\_types](../service-collections/custom-ioa.md#query_rule_types) | Get all rule type IDs. |
| [query\_rulesMixin0](../service-collections/custom-ioa.md#query_rulesMixin0) | Finds all rule IDs matching the query with optional filter. |

### Malquery

| Operation ID | Description |
| :--- | :--- |
| [GetMalQueryQuotasV1](../service-collections/malquery.md#GetMalQueryQuotasV1) | Get information about search and download quotas in your environment |
| [PostMalQueryFuzzySearchV1](../service-collections/malquery.md#PostMalQueryFuzzySearchV1) | Search Falcon MalQuery quickly, but with more potential for false positives. Search for a combination of hex patterns and strings in order to identify samples based upon file content at byte level granularity. |
| [GetMalQueryDownloadV1](../service-collections/malquery.md#GetMalQueryDownloadV1) | Download a file indexed by MalQuery. Specify the file using its SHA256. Only one file is supported at this time |
| [GetMalQueryMetadataV1](../service-collections/malquery.md#GetMalQueryMetadataV1) | Retrieve indexed files metadata by their hash |
| [GetMalQueryRequestV1](../service-collections/malquery.md#GetMalQueryRequestV1) | Check the status and results of an asynchronous request, such as hunt or exact-search. Supports a single request id at this time. |
| [GetMalQueryEntitiesSamplesFetchV1](../service-collections/malquery.md#GetMalQueryEntitiesSamplesFetchV1) | Fetch a zip archive with password 'infected' containing the samples. Call this once the /entities/samples-multidownload request has finished processing |
| [PostMalQueryEntitiesSamplesMultidownloadV1](../service-collections/malquery.md#PostMalQueryEntitiesSamplesMultidownloadV1) | Schedule samples for download. Use the result id with the /request endpoint to check if the download is ready after which you can call the /entities/samples-fetch to get the zip |
| [PostMalQueryExactSearchV1](../service-collections/malquery.md#PostMalQueryExactSearchV1) | Search Falcon MalQuery for a combination of hex patterns and strings in order to identify samples based upon file content at byte level granularity. You can filter results on criteria such as file type, file size and first seen date. Returns a request id which can be used with the /request endpoint |
| [PostMalQueryHuntV1](../service-collections/malquery.md#PostMalQueryHuntV1) | Schedule a YARA-based search for execution. Returns a request id which can be used with the /request endpoint |

### MSSP \(Flight Control\)

| Operation ID | Description |
| :--- | :--- |
| [getChildren](../service-collections/mssp.md#getChildren) | Get link to child customer by child CID\(s\) |
| [getCIDGroupMembersBy](../service-collections/mssp.md#getCIDGroupMembersBy) | Get CID Group members by CID Group IDs. |
| [addCIDGroupMembers](../service-collections/mssp.md#addCIDGroupMembers) | Add new CID Group member. |
| [deleteCIDGroupMembers](../service-collections/mssp.md#deleteCIDGroupMembers) | Delete CID Group members entry. |
| [getCIDGroupById](../service-collections/mssp.md#getCIDGroupById) | Get CID Group\(s\) by ID\(s\). |
| [createCIDGroups](../service-collections/mssp.md#createCIDGroups) | Create new CID Group\(s\). Maximum 500 CID Group\(s\) allowed. |
| [deleteCIDGroups](../service-collections/mssp.md#deleteCIDGroups) | Delete CID Group\(s\) by ID\(s\). |
| [updateCIDGroups](../service-collections/mssp.md#updateCIDGroups) | Update existing CID Group\(s\). CID Group ID is expected for each CID Group definition provided in request body. CID Group member\(s\) remain unaffected. |
| [getRolesByID](../service-collections/mssp.md#getRolesByID) | Get MSSP Role assignment\(s\). MSSP Role assignment is of the format :. |
| [addRole](../service-collections/mssp.md#addRole) | Assign new MSSP Role\(s\) between User Group and CID Group. It does not revoke existing role\(s\) between User Group and CID Group. User Group ID and CID Group ID have to be specified in request. |
| [deletedRoles](../service-collections/mssp.md#deletedRoles) | Delete MSSP Role assignment\(s\) between User Group and CID Group. User Group ID and CID Group ID have to be specified in request. Only specified roles are removed if specified in request payload, else association between User Group and CID Group is dissolved completely \(if no roles specified\). |
| [getUserGroupMembersByID](../service-collections/mssp.md#getUserGroupMembersByID) | Get User Group members by User Group ID\(s\). |
| [addUserGroupMembers](../service-collections/mssp.md#addUserGroupMembers) | Add new User Group member. Maximum 500 members allowed per User Group. |
| [deleteUserGroupMembers](../service-collections/mssp.md#deleteUserGroupMembers) | Delete User Group members entry. |
| [getUserGroupsByID](../service-collections/mssp.md#getUserGroupsByID) | Get User Group by ID\(s\). |
| [createUserGroups](../service-collections/mssp.md#createUserGroups) | Create new User Group\(s\). Maximum 500 User Group\(s\) allowed per customer. |
| [deleteUserGroups](../service-collections/mssp.md#deleteUserGroups) | Delete User Group\(s\) by ID\(s\). |
| [updateUserGroups](../service-collections/mssp.md#updateUserGroups) | Update existing User Group\(s\). User Group ID is expected for each User Group definition provided in request body. User Group member\(s\) remain unaffected. |
| [queryChildren](../service-collections/mssp.md#queryChildren) | Query for customers linked as children |
| [queryCIDGroupMembers](../service-collections/mssp.md#queryCIDGroupMembers) | Query a CID Groups members by associated CID. |
| [queryCIDGroups](../service-collections/mssp.md#queryCIDGroups) | Query CID Groups. |
| [queryRoles](../service-collections/mssp.md#queryRoles) | Query MSSP Role assignment. At least one of CID Group ID or User Group ID should also be provided. Role ID is optional. |
| [queryUserGroupMembers](../service-collections/mssp.md#queryUserGroupMembers) | Query User Group member by User UUID. |
| [queryUserGroups](../service-collections/mssp.md#queryUserGroups) | Query User Groups. |

### OAuth2

| Operation ID | Description |
| :--- | :--- |
| [oauth2RevokeToken](../service-collections/oauth2.md#oauth2RevokeToken) | Revoke a previously issued OAuth2 access token before the end of its standard 30-minute lifespan. |
| [oauth2AccessToken](../service-collections/oauth2.md#oauth2AccessToken) | Generate an OAuth2 access token |

### Overwatch Dashboard

| Operation ID | Description |
| :--- | :--- |
| [AggregatesDetectionsGlobalCounts](../service-collections/overwatch-dashboard.md#AggregatesDetectionsGlobalCounts) | Get the total number of detections pushed across all customers |
| [AggregatesEventsCollections](../service-collections/overwatch-dashboard.md#AggregatesEventsCollections) | Get OverWatch detection event collection info by providing an aggregate query |
| [AggregatesEvents](../service-collections/overwatch-dashboard.md#AggregatesEvents) | Get aggregate OverWatch detection event info by providing an aggregate query |
| [AggregatesIncidentsGlobalCounts](../service-collections/overwatch-dashboard.md#AggregatesIncidentsGlobalCounts) | Get the total number of incidents pushed across all customers |
| [AggregatesOWEventsGlobalCounts](../service-collections/overwatch-dashboard.md#AggregatesOWEventsGlobalCounts) | Get the total number of OverWatch events across all customers |

### Device Control Policies

| Operation ID | Description |
| :--- | :--- |
| [queryCombinedDeviceControlPolicyMembers](../service-collections/device-control-policies.md#queryCombinedDeviceControlPolicyMembers) | Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedDeviceControlPolicies](../service-collections/device-control-policies.md#queryCombinedDeviceControlPolicies) | Search for Device Control Policies in your environment by providing an FQL filter and paging details. Returns a set of Device Control Policies which match the filter criteria |

### Firewall Policies

| Operation ID | Description |
| :--- | :--- |
| [queryCombinedFirewallPolicyMembers](../service-collections/firewall-policies.md#queryCombinedFirewallPolicyMembers) | Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedFirewallPolicies](../service-collections/firewall-policies.md#queryCombinedFirewallPolicies) | Search for Firewall Policies in your environment by providing an FQL filter and paging details. Returns a set of Firewall Policies which match the filter criteria |

### Prevention Policies

| Operation ID | Description |
| :--- | :--- |
| [queryCombinedPreventionPolicyMembers](../service-collections/prevention-policies.md#queryCombinedPreventionPolicyMembers) | Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedPreventionPolicies](../service-collections/prevention-policies.md#queryCombinedPreventionPolicies) | Search for Prevention Policies in your environment by providing an FQL filter and paging details. Returns a set of Prevention Policies which match the filter criteria |

### Sensor Update Policies

| Operation ID | Description |
| :--- | :--- |
| [revealUninstallToken](../service-collections/sensor-update-policies.md#revealUninstallToken) | Reveals an uninstall token for a specific device. To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device\_id' |
| [queryCombinedSensorUpdateBuilds](../service-collections/sensor-update-policies.md#queryCombinedSensorUpdateBuilds) | Retrieve available builds for use with Sensor Update Policies |
| [queryCombinedSensorUpdatePolicyMembers](../service-collections/sensor-update-policies.md#queryCombinedSensorUpdatePolicyMembers) | Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedSensorUpdatePolicies](../service-collections/sensor-update-policies.md#queryCombinedSensorUpdatePolicies) | Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria |
| [queryCombinedSensorUpdatePoliciesV2](../service-collections/sensor-update-policies.md#queryCombinedSensorUpdatePoliciesV2) | Search for Sensor Update Policies with additional support for uninstall protection in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria |
| [performDeviceControlPoliciesAction](../service-collections/device-control-policies.md#performDeviceControlPoliciesAction) | Perform the specified action on the Device Control Policies specified in the request |
| [setDeviceControlPoliciesPrecedence](../service-collections/device-control-policies.md#setDeviceControlPoliciesPrecedence) | Sets the precedence of Device Control Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [getDeviceControlPolicies](../service-collections/device-control-policies.md#getDeviceControlPolicies) | Retrieve a set of Device Control Policies by specifying their IDs |
| [createDeviceControlPolicies](../service-collections/device-control-policies.md#createDeviceControlPolicies) | Create Device Control Policies by specifying details about the policy to create |
| [deleteDeviceControlPolicies](../service-collections/device-control-policies.md#deleteDeviceControlPolicies) | Delete a set of Device Control Policies by specifying their IDs |
| [updateDeviceControlPolicies](../service-collections/device-control-policies.md#updateDeviceControlPolicies) | Update Device Control Policies by specifying the ID of the policy and details to update |
| [performFirewallPoliciesAction](../service-collections/firewall-policies.md#performFirewallPoliciesAction) | Perform the specified action on the Firewall Policies specified in the request |
| [setFirewallPoliciesPrecedence](../service-collections/firewall-policies.md#setFirewallPoliciesPrecedence) | Sets the precedence of Firewall Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [getFirewallPolicies](../service-collections/firewall-policies.md#getFirewallPolicies) | Retrieve a set of Firewall Policies by specifying their IDs |
| [createFirewallPolicies](../service-collections/firewall-policies.md#createFirewallPolicies) | Create Firewall Policies by specifying details about the policy to create |
| [deleteFirewallPolicies](../service-collections/firewall-policies.md#deleteFirewallPolicies) | Delete a set of Firewall Policies by specifying their IDs |
| [updateFirewallPolicies](../service-collections/firewall-policies.md#updateFirewallPolicies) | Update Firewall Policies by specifying the ID of the policy and details to update |

### IOA Exclusions

| Operation ID | Description |
| :--- | :--- |
| [getIOAExclusionsV1](../service-collections/ioa-exclusions.md#getIOAExclusionsV1) | Get a set of IOA Exclusions by specifying their IDs |
| [createIOAExclusionsV1](../service-collections/ioa-exclusions.md#createIOAExclusionsV1) | Create the IOA exclusions |
| [deleteIOAExclusionsV1](../service-collections/ioa-exclusions.md#deleteIOAExclusionsV1) | Delete the IOA exclusions by id |
| [updateIOAExclusionsV1](../service-collections/ioa-exclusions.md#updateIOAExclusionsV1) | Update the IOA exclusions |

### ML Exclusions

| Operation ID | Description |
| :--- | :--- |
| [getMLExclusionsV1](../service-collections/ml-exclusions.md#getMLExclusionsV1) | Get a set of ML Exclusions by specifying their IDs |
| [createMLExclusionsV1](../service-collections/ml-exclusions.md#createMLExclusionsV1) | Create the ML exclusions |
| [deleteMLExclusionsV1](../service-collections/ml-exclusions.md#deleteMLExclusionsV1) | Delete the ML exclusions by id |
| [updateMLExclusionsV1](../service-collections/ml-exclusions.md#updateMLExclusionsV1) | Update the ML exclusions |
| [performPreventionPoliciesAction](../service-collections/prevention-policies.md#performPreventionPoliciesAction) | Perform the specified action on the Prevention Policies specified in the request |
| [setPreventionPoliciesPrecedence](../service-collections/prevention-policies.md#setPreventionPoliciesPrecedence) | Sets the precedence of Prevention Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [getPreventionPolicies](../service-collections/prevention-policies.md#getPreventionPolicies) | Retrieve a set of Prevention Policies by specifying their IDs |
| [createPreventionPolicies](../service-collections/prevention-policies.md#createPreventionPolicies) | Create Prevention Policies by specifying details about the policy to create |
| [deletePreventionPolicies](../service-collections/prevention-policies.md#deletePreventionPolicies) | Delete a set of Prevention Policies by specifying their IDs |
| [updatePreventionPolicies](../service-collections/prevention-policies.md#updatePreventionPolicies) | Update Prevention Policies by specifying the ID of the policy and details to update |
| [performSensorUpdatePoliciesAction](../service-collections/sensor-update-policies.md#performSensorUpdatePoliciesAction) | Perform the specified action on the Sensor Update Policies specified in the request |
| [setSensorUpdatePoliciesPrecedence](../service-collections/sensor-update-policies.md#setSensorUpdatePoliciesPrecedence) | Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [getSensorUpdatePolicies](../service-collections/sensor-update-policies.md#getSensorUpdatePolicies) | Retrieve a set of Sensor Update Policies by specifying their IDs |
| [createSensorUpdatePolicies](../service-collections/sensor-update-policies.md#createSensorUpdatePolicies) | Create Sensor Update Policies by specifying details about the policy to create |
| [deleteSensorUpdatePolicies](../service-collections/sensor-update-policies.md#deleteSensorUpdatePolicies) | Delete a set of Sensor Update Policies by specifying their IDs |
| [updateSensorUpdatePolicies](../service-collections/sensor-update-policies.md#updateSensorUpdatePolicies) | Update Sensor Update Policies by specifying the ID of the policy and details to update |
| [getSensorUpdatePoliciesV2](../service-collections/sensor-update-policies.md#getSensorUpdatePoliciesV2) | Retrieve a set of Sensor Update Policies with additional support for uninstall protection by specifying their IDs |
| [createSensorUpdatePoliciesV2](../service-collections/sensor-update-policies.md#createSensorUpdatePoliciesV2) | Create Sensor Update Policies by specifying details about the policy to create with additional support for uninstall protection |
| [updateSensorUpdatePoliciesV2](../service-collections/sensor-update-policies.md#updateSensorUpdatePoliciesV2) | Update Sensor Update Policies by specifying the ID of the policy and details to update with additional support for uninstall protection |

### Sensor Visibility Exclusions

| Operation ID | Description |
| :--- | :--- |
| [getSensorVisibilityExclusionsV1](../service-collections/sensor-visibility-exclusions.md#getSensorVisibilityExclusionsV1) | Get a set of Sensor Visibility Exclusions by specifying their IDs |
| [createSVExclusionsV1](../service-collections/sensor-visibility-exclusions.md#createSVExclusionsV1) | Create the sensor visibility exclusions |
| [deleteSensorVisibilityExclusionsV1](../service-collections/sensor-visibility-exclusions.md#deleteSensorVisibilityExclusionsV1) | Delete the sensor visibility exclusions by id |
| [updateSensorVisibilityExclusionsV1](../service-collections/sensor-visibility-exclusions.md#updateSensorVisibilityExclusionsV1) | Update the sensor visibility exclusions |
| [queryDeviceControlPolicyMembers](../service-collections/device-control-policies.md#queryDeviceControlPolicyMembers) | Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [queryDeviceControlPolicies](../service-collections/device-control-policies.md#queryDeviceControlPolicies) | Search for Device Control Policies in your environment by providing an FQL filter and paging details. Returns a set of Device Control Policy IDs which match the filter criteria |
| [queryFirewallPolicyMembers](../service-collections/firewall-policies.md#queryFirewallPolicyMembers) | Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [queryFirewallPolicies](../service-collections/firewall-policies.md#queryFirewallPolicies) | Search for Firewall Policies in your environment by providing an FQL filter and paging details. Returns a set of Firewall Policy IDs which match the filter criteria |
| [queryIOAExclusionsV1](../service-collections/ioa-exclusions.md#queryIOAExclusionsV1) | Search for IOA exclusions. |
| [queryMLExclusionsV1](../service-collections/ml-exclusions.md#queryMLExclusionsV1) | Search for ML exclusions. |
| [queryPreventionPolicyMembers](../service-collections/prevention-policies.md#queryPreventionPolicyMembers) | Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [queryPreventionPolicies](../service-collections/prevention-policies.md#queryPreventionPolicies) | Search for Prevention Policies in your environment by providing an FQL filter and paging details. Returns a set of Prevention Policy IDs which match the filter criteria |
| [querySensorUpdatePolicyMembers](../service-collections/sensor-update-policies.md#querySensorUpdatePolicyMembers) | Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [querySensorUpdatePolicies](../service-collections/sensor-update-policies.md#querySensorUpdatePolicies) | Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria |
| [querySensorVisibilityExclusionsV1](../service-collections/sensor-visibility-exclusions.md#querySensorVisibilityExclusionsV1) | Search for sensor visibility exclusions. |
| [entities\_processes](../service-collections/iocs.md#entities_processes) | For the provided ProcessID retrieve the process details |

### Real Time Response

| Operation ID | Description |
| :--- | :--- |
| [RTR\_AggregateSessions](../service-collections/real-time-response.md#RTR_AggregateSessions) | Get aggregates on session data. |
| [BatchActiveResponderCmd](../service-collections/real-time-response.md#BatchActiveResponderCmd) | Batch executes a RTR active-responder command across the hosts mapped to the given batch ID. |

### Real Time Response Admin

| Operation ID | Description |
| :--- | :--- |
| [BatchAdminCmd](../service-collections/real-time-response-admin.md#BatchAdminCmd) | Batch executes a RTR administrator command across the hosts mapped to the given batch ID. |
| [BatchCmd](../service-collections/real-time-response.md#BatchCmd) | Batch executes a RTR read-only command across the hosts mapped to the given batch ID. |
| [BatchGetCmdStatus](../service-collections/real-time-response.md#BatchGetCmdStatus) | Retrieves the status of the specified batch get command.  Will return successful files when they are finished processing. |
| [BatchGetCmd](../service-collections/real-time-response.md#BatchGetCmd) | Batch executes `get` command across hosts to retrieve files. After this call is made `GET /real-time-response/combined/batch-get-command/v1` is used to query for the results. |
| [BatchInitSessions](../service-collections/real-time-response.md#BatchInitSessions) | Batch initialize a RTR session on multiple hosts.  Before any RTR commands can be used, an active session is needed on the host. |
| [BatchRefreshSessions](../service-collections/real-time-response.md#BatchRefreshSessions) | Batch refresh a RTR session on multiple hosts. RTR sessions will expire after 10 minutes unless refreshed. |
| [RTR\_CheckActiveResponderCommandStatus](../service-collections/real-time-response.md#RTR_CheckActiveResponderCommandStatus) | Get status of an executed active-responder command on a single host. |
| [RTR\_ExecuteActiveResponderCommand](../service-collections/real-time-response.md#RTR_ExecuteActiveResponderCommand) | Execute an active responder command on a single host. |
| [RTR\_CheckAdminCommandStatus](../service-collections/real-time-response-admin.md#RTR_CheckAdminCommandStatus) | Get status of an executed RTR administrator command on a single host. |
| [RTR\_ExecuteAdminCommand](../service-collections/real-time-response-admin.md#RTR_ExecuteAdminCommand) | Execute a RTR administrator command on a single host. |
| [RTR\_CheckCommandStatus](../service-collections/real-time-response.md#RTR_CheckCommandStatus) | Get status of an executed command on a single host. |
| [RTR\_ExecuteCommand](../service-collections/real-time-response.md#RTR_ExecuteCommand) | Execute a command on a single host. |
| [RTR\_GetExtractedFileContents](../service-collections/real-time-response.md#RTR_GetExtractedFileContents) | Get RTR extracted file contents for specified session and sha256. |
| [RTR\_ListFiles](../service-collections/real-time-response.md#RTR_ListFiles) | Get a list of files for the specified RTR session. |
| [RTR\_DeleteFile](../service-collections/real-time-response.md#RTR_DeleteFile) | Delete a RTR session file. |
| [RTR\_GetPut\_Files](../service-collections/real-time-response-admin.md#RTR_GetPut_Files) | Get put-files based on the ID's given. These are used for the RTR `put` command. |
| [RTR\_CreatePut\_Files](../service-collections/real-time-response-admin.md#RTR_CreatePut_Files) | Upload a new put-file to use for the RTR `put` command. |
| [RTR\_DeletePut\_Files](../service-collections/real-time-response-admin.md#RTR_DeletePut_Files) | Delete a put-file based on the ID given.  Can only delete one file at a time. |
| [RTR\_ListQueuedSessions](../service-collections/real-time-response.md#RTR_ListQueuedSessions) | Get queued session metadata by session ID. |
| [RTR\_DeleteQueuedSession](../service-collections/real-time-response.md#RTR_DeleteQueuedSession) | Delete a queued session command |
| [RTR\_PulseSession](../service-collections/real-time-response.md#RTR_PulseSession) | Refresh a session timeout on a single host. |
| [RTR\_GetScripts](../service-collections/real-time-response-admin.md#RTR_GetScripts) | Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command. |
| [RTR\_CreateScripts](../service-collections/real-time-response-admin.md#RTR_CreateScripts) | Upload a new custom-script to use for the RTR `runscript` command. |
| [RTR\_DeleteScripts](../service-collections/real-time-response-admin.md#RTR_DeleteScripts) | Delete a custom-script based on the ID given.  Can only delete one script at a time. |
| [RTR\_UpdateScripts](../service-collections/real-time-response-admin.md#RTR_UpdateScripts) | Upload a new scripts to replace an existing one. |
| [RTR\_ListSessions](../service-collections/real-time-response.md#RTR_ListSessions) | Get session metadata by session id. |
| [RTR\_InitSession](../service-collections/real-time-response.md#RTR_InitSession) | Initialize a new session with the RTR cloud. |
| [RTR\_DeleteSession](../service-collections/real-time-response.md#RTR_DeleteSession) | Delete a session. |
| [RTR\_ListPut\_Files](../service-collections/real-time-response-admin.md#RTR_ListPut_Files) | Get a list of put-file ID's that are available to the user for the `put` command. |
| [RTR\_ListScripts](../service-collections/real-time-response-admin.md#RTR_ListScripts) | Get a list of custom-script ID's that are available to the user for the `runscript` command. |
| [RTR\_ListAllSessions](../service-collections/real-time-response.md#RTR_ListAllSessions) | Get a list of session\_ids. |
| [GetSampleV2](../service-collections/falconx-sandbox.md#GetSampleV2) | Retrieves the file associated with the given ID \(SHA256\) |
| [UploadSampleV2](../service-collections/falconx-sandbox.md#UploadSampleV2) | Upload a file for sandbox analysis. After uploading, use `/falconx/entities/submissions/v1` to start analyzing the file. |
| [DeleteSampleV2](../service-collections/falconx-sandbox.md#DeleteSampleV2) | Removes a sample, including file, meta and submissions from the collection |

### Sample Uploads

| Operation ID | Description |
| :--- | :--- |
| [GetSampleV3](../service-collections/sample-uploads.md#GetSampleV3) | Retrieves the file associated with the given ID \(SHA256\) |
| [UploadSampleV3](../service-collections/sample-uploads.md#UploadSampleV3) | Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint. |
| [DeleteSampleV3](../service-collections/sample-uploads.md#DeleteSampleV3) | Removes a sample, including file, meta and submissions from the collection |
| [QuerySampleV1](../service-collections/falconx-sandbox.md#QuerySampleV1) | Retrieves a list with sha256 of samples that exist and customer has rights to access them, maximum number of accepted items is 200 |

### Quick Scan

| Operation ID | Description |
| :--- | :--- |
| [GetScansAggregates](../service-collections/quick-scan.md#GetScansAggregates) | Get scans aggregations as specified via json in request body. |
| [GetScans](../service-collections/quick-scan.md#GetScans) | Check the status of a volume scan. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute |
| [ScanSamples](../service-collections/quick-scan.md#ScanSamples) | Submit a volume of files for ml scanning. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute |
| [QuerySubmissionsMixin0](../service-collections/quick-scan.md#QuerySubmissionsMixin0) | Find IDs for submitted scans by providing an FQL filter and paging details. Returns a set of volume IDs that match your criteria. |

### Sensor Download

| Operation ID | Description |
| :--- | :--- |
| [GetCombinedSensorInstallersByQuery](../service-collections/sensor-download.md#GetCombinedSensorInstallersByQuery) | Get sensor installer details by provided query |

### Event Streams

| Operation ID | Description |
| :--- | :--- |
| [refreshActiveStreamSession](../service-collections/event-streams.md#refreshActiveStreamSession) | Refresh an active event stream. Use the URL shown in a GET /sensors/entities/datafeed/v2 response. |
| [listAvailableStreamsOAuth2](../service-collections/event-streams.md#listAvailableStreamsOAuth2) | Discover all event streams in your environment |
| [DownloadSensorInstallerById](../service-collections/sensor-download.md#DownloadSensorInstallerById) | Download sensor installer by SHA256 ID |
| [GetSensorInstallersEntities](../service-collections/sensor-download.md#GetSensorInstallersEntities) | Get sensor installer details by provided SHA256 IDs |
| [GetSensorInstallersCCIDByQuery](../service-collections/sensor-download.md#GetSensorInstallersCCIDByQuery) | Get CCID to use with sensor installers |
| [GetSensorInstallersByQuery](../service-collections/sensor-download.md#GetSensorInstallersByQuery) | Get sensor installer IDs by provided query |
| [GetCSPMPolicy](../service-collections/cspm-registration.md#GetCSPMPolicy) | Given a policy ID, returns detailed policy information. |
| [GetCSPMPolicySettings](../service-collections/cspm-registration.md#GetCSPMPolicySettings) | Returns information about current policy settings. |
| [UpdateCSPMPolicySettings](../service-collections/cspm-registration.md#UpdateCSPMPolicySettings) | Updates a policy setting - can be used to override policy severity or to disable a policy entirely. |
| [GetCSPMScanSchedule](../service-collections/cspm-registration.md#GetCSPMScanSchedule) | Returns scan schedule configuration for one or more cloud platforms. |
| [UpdateCSPMScanSchedule](../service-collections/cspm-registration.md#UpdateCSPMScanSchedule) | Updates scan schedule configuration for one or more cloud platforms. |

### Spotlight Vulnerabilities

| Operation ID | Description |
| :--- | :--- |
| [getVulnerabilities](../service-collections/spotlight-vulnerabilities.md#getVulnerabilities) | Get details on vulnerabilities by providing one or more IDs |
| [queryVulnerabilities](../service-collections/spotlight-vulnerabilities.md#queryVulnerabilities) | Search for Vulnerabilities in your environment by providing an FQL filter and paging details. Returns a set of Vulnerability IDs which match the filter criteria |

### User Management

| Operation ID | Description |
| :--- | :--- |
| [GetRoles](../service-collections/user-management.md#GetRoles) | Get info about a role |
| [GrantUserRoleIds](../service-collections/user-management.md#GrantUserRoleIds) | Assign one or more roles to a user |
| [RevokeUserRoleIds](../service-collections/user-management.md#RevokeUserRoleIds) | Revoke one or more roles from a user |
| [GetAvailableRoleIds](../service-collections/user-management.md#GetAvailableRoleIds) | Show role IDs for all roles available in your customer account. For more information on each role, provide the role ID to `/customer/entities/roles/v1`. |
| [GetUserRoleIds](../service-collections/user-management.md#GetUserRoleIds) | Show role IDs of roles assigned to a user. For more information on each role, provide the role ID to `/customer/entities/roles/v1`. |
| [RetrieveUser](../service-collections/user-management.md#RetrieveUser) | Get info about a user |
| [CreateUser](../service-collections/user-management.md#CreateUser) | Create a new user. After creating a user, assign one or more roles with POST /user-roles/entities/user-roles/v1 |
| [DeleteUser](../service-collections/user-management.md#DeleteUser) | Delete a user permanently |
| [UpdateUser](../service-collections/user-management.md#UpdateUser) | Modify an existing user's first or last name |
| [RetrieveEmailsByCID](../service-collections/user-management.md#RetrieveEmailsByCID) | List the usernames \(usually an email address\) for all users in your customer account |
| [RetrieveUserUUIDsByCID](../service-collections/user-management.md#RetrieveUserUUIDsByCID) | List user IDs for all users in your customer account. For more information on each user, provide the user ID to `/users/entities/user/v1`. |
| [RetrieveUserUUID](../service-collections/user-management.md#RetrieveUserUUID) | Get a user's ID by providing a username \(usually an email address\) |

### Zero Trust Assessment

| Operation ID | Description |
| :--- | :--- |
| [getAssessmentV1](../service-collections/zero-trust-assessment.md#getAssessmentV1) | Get Zero Trust Assessment data for one or more hosts by providing agent IDs \(AID\) and a customer ID \(CID\). |

