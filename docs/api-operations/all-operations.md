# All Operations

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Alphabetical list of all CrowdStrike OAuth2 API operations

| Operation ID | Service Collection | Description |
| :--- | :--- | :--- |
| [addCIDGroupMembers](../service-collections/mssp.md#addCIDGroupMembers) | MSSP \(Flight Control\) | Add new CID Group member. |
| [addRole](../service-collections/mssp.md#addRole) | MSSP \(Flight Control\) | Assign new MSSP Role\(s\) between User Group and CID Group. It does not revoke existing role\(s\) between User Group and CID Group. User Group ID and CID Group ID have to be specified in request. |
| [addUserGroupMembers](../service-collections/mssp.md#addUserGroupMembers) | MSSP \(Flight Control\) | Add new User Group member. Maximum 500 members allowed per User Group. |
| [aggregate\_events](../service-collections/firewall-management.md#aggregate_events) | Firewall Management | Aggregate events for customer |
| [aggregate\_policy\_rules](../service-collections/firewall-management.md#aggregate_policy_rules) | Firewall Management | Aggregate rules within a policy for customer |
| [aggregate\_rule\_groups](../service-collections/firewall-management.md#aggregate_rule_groups) | Firewall Management | Aggregate rule groups for customer |
| [aggregate\_rules](../service-collections/firewall-management.md#aggregate_rules) | Firewall Management | Aggregate rules for customer |
| [AggregateAllowList](../service-collections/falcon-complete-dashboard.md#AggregateAllowList) | Falcon Complete Dashboard | Retrieve aggregate allowlist ticket values based on the matched filter |
| [AggregateBlockList](../service-collections/falcon-complete-dashboard.md#AggregateBlockList) | Falcon Complete Dashboard | Retrieve aggregate blocklist ticket values based on the matched filter |
| [AggregateDetections](../service-collections/falcon-complete-dashboard.md#AggregateDetections) | Falcon Complete Dashboard | Retrieve aggregate detection values based on the matched filter |
| [AggregateDeviceCountCollection](../service-collections/falcon-complete-dashboard.md#AggregateDeviceCountCollection) | Falcon Complete Dashboard | Retrieve aggregate host/devices count based on the matched filter |
| [AggregateEscalations](../service-collections/falcon-complete-dashboard.md#AggregateEscalations) | Falcon Complete Dashboard | Retrieve aggregate escalation ticket values based on the matched filter |
| [AggregateFCIncidents](../service-collections/falcon-complete-dashboard.md#AggregateFCIncidents) | Falcon Complete Dashboard | Retrieve aggregate incident values based on the matched filter |
| [AggregateRemediations](../service-collections/falcon-complete-dashboard.md#AggregateRemediations) | Falcon Complete Dashboard | Retrieve aggregate remediation ticket values based on the matched filter |
| [AggregatesDetectionsGlobalCounts](../service-collections/overwatch-dashboard.md#AggregatesDetectionsGlobalCounts) | Overwatch Dashboard | Get the total number of detections pushed across all customers |
| [AggregatesEvents](../service-collections/overwatch-dashboard.md#AggregatesEvents) | Overwatch Dashboard | Get aggregate OverWatch detection event info by providing an aggregate query |
| [AggregatesEventsCollections](../service-collections/overwatch-dashboard.md#AggregatesEventsCollections) | Overwatch Dashboard | Get OverWatch detection event collection info by providing an aggregate query |
| [AggregatesIncidentsGlobalCounts](../service-collections/overwatch-dashboard.md#AggregatesIncidentsGlobalCounts) | Overwatch Dashboard | Get the total number of incidents pushed across all customers |
| [AggregatesOWEventsGlobalCounts](../service-collections/overwatch-dashboard.md#AggregatesOWEventsGlobalCounts) | Overwatch Dashboard | Get the total number of OverWatch events across all customers |
| [audit\_events\_query](../service-collections/installation-tokens.md#audit_events_query) | Installation Tokens | Search for audit events by providing an FQL filter and paging details. |
| [audit\_events\_read](../service-collections/installation-tokens.md#audit_events_read) | Installation Tokens | Gets the details of one or more audit events by id. |
| [BatchActiveResponderCmd](../service-collections/real-time-response.md#BatchActiveResponderCmd) | Real Time Response | Batch executes a RTR active-responder command across the hosts mapped to the given batch ID. |
| [BatchAdminCmd](../service-collections/real-time-response-admin.md#BatchAdminCmd) | Real Time Response Admin | Batch executes a RTR administrator command across the hosts mapped to the given batch ID. |
| [BatchCmd](../service-collections/real-time-response.md#BatchCmd) | Real Time Response | Batch executes a RTR read-only command across the hosts mapped to the given batch ID. |
| [BatchGetCmd](../service-collections/real-time-response.md#BatchGetCmd) | Real Time Response | Batch executes `get` command across hosts to retrieve files. After this call is made `GET /real-time-response/combined/batch-get-command/v1` is used to query for the results. |
| [BatchGetCmdStatus](../service-collections/real-time-response.md#BatchGetCmdStatus) | Real Time Response | Retrieves the status of the specified batch get command.  Will return successful files when they are finished processing. |
| [BatchInitSessions](../service-collections/real-time-response.md#BatchInitSessions) | Real Time Response | Batch initialize a RTR session on multiple hosts.  Before any RTR commands can be used, an active session is needed on the host. |
| [BatchRefreshSessions](../service-collections/real-time-response.md#BatchRefreshSessions) | Real Time Response | Batch refresh a RTR session on multiple hosts. RTR sessions will expire after 10 minutes unless refreshed. |
| [create\_rule](../service-collections/custom-ioa.md#create_rule) | Custom IOA | Create a rule within a rule group. Returns the rule. |
| [create\_rule\_group](../service-collections/firewall-management.md#create_rule_group) | Firewall Management | Create new rule group on a platform for a customer with a name and description, and return the ID |
| [create\_rule\_groupMixin0](../service-collections/custom-ioa.md#create_rule_groupMixin0) | Custom IOA | Create a rule group for a platform with a name and an optional description. Returns the rule group. |
| [createCIDGroups](../service-collections/mssp.md#createCIDGroups) | MSSP \(Flight Control\) | Create new CID Group\(s\). Maximum 500 CID Group\(s\) allowed. |
| [CreateCSPMAwsAccount](../service-collections/cspm-registration.md#CreateCSPMAwsAccount) | CSPM Registration | Creates a new account in our system for a customer and generates a script for them to run in their AWS cloud environment to grant us access. |
| [CreateCSPMAzureAccount](../service-collections/d4c-registration.md#CreateCSPMAzureAccount) | D4C Registration | Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access. |
| [CreateCSPMAzureAccount](../service-collections/cspm-registration.md#CreateCSPMAzureAccount) | CSPM Registration | Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access. |
| [CreateCSPMGCPAccount](../service-collections/d4c-registration.md#CreateCSPMGCPAccount) | D4C Registration | Creates a new account in our system for a customer and generates a new service account for them to add access to in their GCP environment to grant us access. |
| [createDeviceControlPolicies](../service-collections/device-control-policies.md#createDeviceControlPolicies) | Device Control Policies | Create Device Control Policies by specifying details about the policy to create |
| [createFirewallPolicies](../service-collections/firewall-policies.md#createFirewallPolicies) | Firewall Policies | Create Firewall Policies by specifying details about the policy to create |
| [createHostGroups](../service-collections/host-group.md#createHostGroups) | Host Group | Create Host Groups by specifying details about the group to create |
| [createIOAExclusionsV1](../service-collections/ioa-exclusions.md#createIOAExclusionsV1) | IOA Exclusions | Create the IOA exclusions |
| [CreateIOC](../service-collections/iocs.md#CreateIOC) | IOCs | Create a new IOC |
| [createMLExclusionsV1](../service-collections/ml-exclusions.md#createMLExclusionsV1) | ML Exclusions | Create the ML exclusions |
| [CreateOrUpdateAWSSettings](../service-collections/cloud-connect-aws.md#CreateOrUpdateAWSSettings) | Cloud Connect AWS | Create or update Global Settings which are applicable to all provisioned AWS accounts |
| [createPreventionPolicies](../service-collections/prevention-policies.md#createPreventionPolicies) | Prevention Policies | Create Prevention Policies by specifying details about the policy to create |
| [createSensorUpdatePolicies](../service-collections/sensor-update-policies.md#createSensorUpdatePolicies) | Sensor Update Policies | Create Sensor Update Policies by specifying details about the policy to create |
| [createSensorUpdatePoliciesV2](../service-collections/sensor-update-policies.md#createSensorUpdatePoliciesV2) | Sensor Update Policies | Create Sensor Update Policies by specifying details about the policy to create with additional support for uninstall protection |
| [createSVExclusionsV1](../service-collections/sensor-visibility-exclusions.md#createSVExclusionsV1) | Sensor Visibility Exclusions | Create the sensor visibility exclusions |
| [CreateUser](../service-collections/user-management.md#CreateUser) | User Management | Create a new user. After creating a user, assign one or more roles with POST /user-roles/entities/user-roles/v1 |
| [createUserGroups](../service-collections/mssp.md#createUserGroups) | MSSP \(Flight Control\) | Create new User Group\(s\). Maximum 500 User Group\(s\) allowed per customer. |
| [CrowdScore](../service-collections/incidents.md#CrowdScore) | Incidents | Query environment wide CrowdScore and return the entity data |
| [customer\_settings\_read](../service-collections/installation-tokens.md#customer_settings_read) | Installation Tokens | Check current installation token settings. |
| [delete\_rule\_groups](../service-collections/firewall-management.md#delete_rule_groups) | Firewall Management | Delete rule group entities by ID |
| [delete\_rule\_groupsMixin0](../service-collections/custom-ioa.md#delete_rule_groupsMixin0) | Custom IOA | Delete rule groups by ID. |
| [delete\_rules](../service-collections/custom-ioa.md#delete_rules) | Custom IOA | Delete rules from a rule group by ID. |
| [DeleteAWSAccounts](../service-collections/cloud-connect-aws.md#DeleteAWSAccounts) | Cloud Connect AWS | Delete a set of AWS Accounts by specifying their IDs |
| [deleteCIDGroupMembers](../service-collections/mssp.md#deleteCIDGroupMembers) | MSSP \(Flight Control\) | Delete CID Group members entry. |
| [deleteCIDGroups](../service-collections/mssp.md#deleteCIDGroups) | MSSP \(Flight Control\) | Delete CID Group\(s\) by ID\(s\). |
| [DeleteCSPMAwsAccount](../service-collections/cspm-registration.md#DeleteCSPMAwsAccount) | CSPM Registration | Deletes an existing AWS account or organization in our system. |
| [DeleteCSPMAzureAccount](../service-collections/cspm-registration.md#DeleteCSPMAzureAccount) | CSPM Registration | Deletes an Azure subscription from the system. |
| [deleteDeviceControlPolicies](../service-collections/device-control-policies.md#deleteDeviceControlPolicies) | Device Control Policies | Delete a set of Device Control Policies by specifying their IDs |
| [deletedRoles](../service-collections/mssp.md#deletedRoles) | MSSP \(Flight Control\) | Delete MSSP Role assignment\(s\) between User Group and CID Group. User Group ID and CID Group ID have to be specified in request. Only specified roles are removed if specified in request payload, else association between User Group and CID Group is dissolved completely \(if no roles specified\). |
| [deleteFirewallPolicies](../service-collections/firewall-policies.md#deleteFirewallPolicies) | Firewall Policies | Delete a set of Firewall Policies by specifying their IDs |
| [deleteHostGroups](../service-collections/host-group.md#deleteHostGroups) | Host Group | Delete a set of Host Groups by specifying their IDs |
| [deleteIOAExclusionsV1](../service-collections/ioa-exclusions.md#deleteIOAExclusionsV1) | IOA Exclusions | Delete the IOA exclusions by id |
| [DeleteIOC](../service-collections/iocs.md#DeleteIOC) | IOCs | Delete an IOC by providing a type and value |
| [deleteMLExclusionsV1](../service-collections/ml-exclusions.md#deleteMLExclusionsV1) | ML Exclusions | Delete the ML exclusions by id |
| [deletePreventionPolicies](../service-collections/prevention-policies.md#deletePreventionPolicies) | Prevention Policies | Delete a set of Prevention Policies by specifying their IDs |
| [DeleteReport](../service-collections/falconx-sandbox.md#DeleteReport) | Falconx Sandbox | Delete report based on the report ID. Operation can be checked for success by polling for the report ID on the report-summaries endpoint. |
| [DeleteSampleV2](../service-collections/falconx-sandbox.md#DeleteSampleV2) | Falconx Sandbox | Removes a sample, including file, meta and submissions from the collection |
| [DeleteSampleV3](../service-collections/sample-uploads.md#DeleteSampleV3) | Sample Uploads | Removes a sample, including file, meta and submissions from the collection |
| [deleteSensorUpdatePolicies](../service-collections/sensor-update-policies.md#deleteSensorUpdatePolicies) | Sensor Update Policies | Delete a set of Sensor Update Policies by specifying their IDs |
| [deleteSensorVisibilityExclusionsV1](../service-collections/sensor-visibility-exclusions.md#deleteSensorVisibilityExclusionsV1) | Sensor Visibility Exclusions | Delete the sensor visibility exclusions by id |
| [DeleteUser](../service-collections/user-management.md#DeleteUser) | User Management | Delete a user permanently |
| [deleteUserGroupMembers](../service-collections/mssp.md#deleteUserGroupMembers) | MSSP \(Flight Control\) | Delete User Group members entry. |
| [deleteUserGroups](../service-collections/mssp.md#deleteUserGroups) | MSSP \(Flight Control\) | Delete User Group\(s\) by ID\(s\). |
| [DevicesCount](../service-collections/iocs.md#DevicesCount) | IOCs | Number of hosts in your customer account that have observed a given custom IOC |
| [DevicesRanOn](../service-collections/iocs.md#DevicesRanOn) | IOCs | Find hosts that have observed a given custom IOC. For details about those hosts, use GET /devices/entities/devices/v1 |
| [DownloadSensorInstallerById](../service-collections/sensor-download.md#DownloadSensorInstallerById) | Sensor Download | Download sensor installer by SHA256 ID |
| [entities\_processes](../service-collections/iocs.md#entities_processes) | IOCs | For the provided ProcessID retrieve the process details |
| [get\_events](../service-collections/firewall-management.md#get_events) | Firewall Management | Get events entities by ID and optionally version |
| [get\_firewall\_fields](../service-collections/firewall-management.md#get_firewall_fields) | Firewall Management | Get the firewall field specifications by ID |
| [get\_patterns](../service-collections/custom-ioa.md#get_patterns) | Custom IOA | Get pattern severities by ID. |
| [get\_platforms](../service-collections/firewall-management.md#get_platforms) | Firewall Management | Get platforms by ID, e.g., windows or mac or droid |
| [get\_platformsMixin0](../service-collections/custom-ioa.md#get_platformsMixin0) | Custom IOA | Get platforms by ID. |
| [get\_policy\_containers](../service-collections/firewall-management.md#get_policy_containers) | Firewall Management | Get policy container entities by policy ID |
| [get\_rule\_groups](../service-collections/firewall-management.md#get_rule_groups) | Firewall Management | Get rule group entities by ID. These groups do not contain their rule entites, just the rule IDs in precedence order. |
| [get\_rule\_groupsMixin0](../service-collections/custom-ioa.md#get_rule_groupsMixin0) | Custom IOA | Get rule groups by ID. |
| [get\_rule\_types](../service-collections/custom-ioa.md#get_rule_types) | Custom IOA | Get rule types by ID. |
| [get\_rules](../service-collections/firewall-management.md#get_rules) | Firewall Management | Get rule entities by ID \(64-bit unsigned int as decimal string\) or Family ID \(32-character hexadecimal string\) |
| [get\_rules\_get](../service-collections/custom-ioa.md#get_rules_get) | Custom IOA | Get rules by ID and optionally version in the following format: `ID[:version]`. |
| [get\_rulesMixin0](../service-collections/custom-ioa.md#get_rulesMixin0) | Custom IOA | Get rules by ID and optionally version in the following format: `ID[:version]`. The max number of IDs is constrained by URL size. |
| [GetAggregateDetects](../service-collections/detects.md#GetAggregateDetects) | Detects | Get detect aggregates as specified via json in request body. |
| [GetArtifacts](../service-collections/falconx-sandbox.md#GetArtifacts) | Falconx Sandbox | Download IOC packs, PCAP files, and other analysis artifacts. |
| [getAssessmentV1](../service-collections/zero-trust-assessment.md#getAssessmentV1) | Zero Trust Assessment | Get Zero Trust Assessment data for one or more hosts by providing agent IDs \(AID\) and a customer ID \(CID\). |
| [GetAvailableRoleIds](../service-collections/user-management.md#GetAvailableRoleIds) | User Management | Show role IDs for all roles available in your customer account. For more information on each role, provide the role ID to `/customer/entities/roles/v1`. |
| [GetAWSAccounts](../service-collections/cloud-connect-aws.md#GetAWSAccounts) | Cloud Connect AWS | Retrieve a set of AWS Accounts by specifying their IDs |
| [GetAWSSettings](../service-collections/cloud-connect-aws.md#GetAWSSettings) | Cloud Connect AWS | Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts |
| [GetBehaviors](../service-collections/incidents.md#GetBehaviors) | Incidents | Get details on behaviors by providing behavior IDs |
| [getChildren](../service-collections/mssp.md#getChildren) | MSSP \(Flight Control\) | Get link to child customer by child CID\(s\) |
| [getCIDGroupById](../service-collections/mssp.md#getCIDGroupById) | MSSP \(Flight Control\) | Get CID Group\(s\) by ID\(s\). |
| [getCIDGroupMembersBy](../service-collections/mssp.md#getCIDGroupMembersBy) | MSSP \(Flight Control\) | Get CID Group members by CID Group IDs. |
| [GetCombinedSensorInstallersByQuery](../service-collections/sensor-download.md#GetCombinedSensorInstallersByQuery) | Sensor Download | Get sensor installer details by provided query |
| [GetCSPMAwsAccount](../service-collections/cspm-registration.md#GetCSPMAwsAccount) | CSPM Registration | Returns information about the current status of an AWS account. |
| [GetCSPMAwsAccountScriptsAttachment](../service-collections/cspm-registration.md#GetCSPMAwsAccountScriptsAttachment) | CSPM Registration | Return a script for customer to run in their cloud environment to grant us access to their AWS environment as a downloadable attachment. |
| [GetCSPMAwsConsoleSetupURLs](../service-collections/cspm-registration.md#GetCSPMAwsConsoleSetupURLs) | CSPM Registration | Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment. |
| [GetCSPMAzureAccount](../service-collections/d4c-registration.md#GetCSPMAzureAccount) | D4C Registration | Return information about Azure account registration |
| [GetCSPMAzureAccount](../service-collections/cspm-registration.md#GetCSPMAzureAccount) | CSPM Registration | Return information about Azure account registration |
| [GetCSPMAzureUserScripts](../service-collections/d4c-registration.md#GetCSPMAzureUserScripts) | D4C Registration | Return a script for customer to run in their cloud environment to grant us access to their Azure environment |
| [GetCSPMAzureUserScriptsAttachment](../service-collections/d4c-registration.md#GetCSPMAzureUserScriptsAttachment) | D4C Registration | Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment |
| [GetCSPMAzureUserScriptsAttachment](../service-collections/cspm-registration.md#GetCSPMAzureUserScriptsAttachment) | CSPM Registration | Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment |
| [GetCSPMCGPAccount](../service-collections/d4c-registration.md#GetCSPMCGPAccount) | D4C Registration | Returns information about the current status of an GCP account. |
| [GetCSPMGCPUserScripts](../service-collections/d4c-registration.md#GetCSPMGCPUserScripts) | D4C Registration | Return a script for customer to run in their cloud environment to grant us access to their GCP environment |
| [GetCSPMGCPUserScriptsAttachment](../service-collections/d4c-registration.md#GetCSPMGCPUserScriptsAttachment) | D4C Registration | Return a script for customer to run in their cloud environment to grant us access to their GCP environment as a downloadable attachment |
| [GetCSPMPolicy](../service-collections/cspm-registration.md#GetCSPMPolicy) | CSPM Registration | Given a policy ID, returns detailed policy information. |
| [GetCSPMPolicySettings](../service-collections/cspm-registration.md#GetCSPMPolicySettings) | CSPM Registration | Returns information about current policy settings. |
| [GetCSPMScanSchedule](../service-collections/cspm-registration.md#GetCSPMScanSchedule) | CSPM Registration | Returns scan schedule configuration for one or more cloud platforms. |
| [GetDetectSummaries](../service-collections/detects.md#GetDetectSummaries) | Detects | View information about detections |
| [getDeviceControlPolicies](../service-collections/device-control-policies.md#getDeviceControlPolicies) | Device Control Policies | Retrieve a set of Device Control Policies by specifying their IDs |
| [GetDeviceCountCollectionQueriesByFilter](../service-collections/falcon-complete-dashboard.md#GetDeviceCountCollectionQueriesByFilter) | Falcon Complete Dashboard | Retrieve device count collection Ids that match the provided FQL filter, criteria with scrolling enabled |
| [GetDeviceDetails](../service-collections/hosts.md#GetDeviceDetails) | Hosts | Get details on one or more hosts by providing agent IDs \(AID\). You can get a host's agent IDs \(AIDs\) from the /devices/queries/devices/v1 endpoint, the Falcon console or the Streaming API |
| [getFirewallPolicies](../service-collections/firewall-policies.md#getFirewallPolicies) | Firewall Policies | Retrieve a set of Firewall Policies by specifying their IDs |
| [getHostGroups](../service-collections/host-group.md#getHostGroups) | Host Group | Retrieve a set of Host Groups by specifying their IDs |
| [GetIncidents](../service-collections/incidents.md#GetIncidents) | Incidents | Get details on incidents by providing incident IDs |
| [GetIntelActorEntities](../service-collections/intel.md#GetIntelActorEntities) | Intel | Retrieve specific actors using their actor IDs. |
| [GetIntelIndicatorEntities](../service-collections/intel.md#GetIntelIndicatorEntities) | Intel | Retrieve specific indicators using their indicator IDs. |
| [GetIntelReportEntities](../service-collections/intel.md#GetIntelReportEntities) | Intel | Retrieve specific reports using their report IDs. |
| [GetIntelReportPDF](../service-collections/intel.md#GetIntelReportPDF) | Intel | Return a Report PDF attachment |
| [GetIntelRuleEntities](../service-collections/intel.md#GetIntelRuleEntities) | Intel | Retrieve details for rule sets for the specified ids. |
| [GetIntelRuleFile](../service-collections/intel.md#GetIntelRuleFile) | Intel | Download earlier rule sets. |
| [getIOAExclusionsV1](../service-collections/ioa-exclusions.md#getIOAExclusionsV1) | IOA Exclusions | Get a set of IOA Exclusions by specifying their IDs |
| [GetIOC](../service-collections/iocs.md#GetIOC) | IOCs | Get an IOC by providing a type and value |
| [GetLatestIntelRuleFile](../service-collections/intel.md#GetLatestIntelRuleFile) | Intel | Download the latest rule set. |
| [GetMalQueryDownloadV1](../service-collections/malquery.md#GetMalQueryDownloadV1) | Malquery | Download a file indexed by MalQuery. Specify the file using its SHA256. Only one file is supported at this time |
| [GetMalQueryEntitiesSamplesFetchV1](../service-collections/malquery.md#GetMalQueryEntitiesSamplesFetchV1) | Malquery | Fetch a zip archive with password 'infected' containing the samples. Call this once the /entities/samples-multidownload request has finished processing |
| [GetMalQueryMetadataV1](../service-collections/malquery.md#GetMalQueryMetadataV1) | Malquery | Retrieve indexed files metadata by their hash |
| [GetMalQueryQuotasV1](../service-collections/malquery.md#GetMalQueryQuotasV1) | Malquery | Get information about search and download quotas in your environment |
| [GetMalQueryRequestV1](../service-collections/malquery.md#GetMalQueryRequestV1) | Malquery | Check the status and results of an asynchronous request, such as hunt or exact-search. Supports a single request id at this time. |
| [getMLExclusionsV1](../service-collections/ml-exclusions.md#getMLExclusionsV1) | ML Exclusions | Get a set of ML Exclusions by specifying their IDs |
| [getPreventionPolicies](../service-collections/prevention-policies.md#getPreventionPolicies) | Prevention Policies | Retrieve a set of Prevention Policies by specifying their IDs |
| [GetReports](../service-collections/falconx-sandbox.md#GetReports) | Falconx Sandbox | Get a full sandbox report. |
| [GetRoles](../service-collections/user-management.md#GetRoles) | User Management | Get info about a role |
| [getRolesByID](../service-collections/mssp.md#getRolesByID) | MSSP \(Flight Control\) | Get MSSP Role assignment\(s\). MSSP Role assignment is of the format :. |
| [GetSampleV2](../service-collections/falconx-sandbox.md#GetSampleV2) | Falconx Sandbox | Retrieves the file associated with the given ID \(SHA256\) |
| [GetSampleV3](../service-collections/sample-uploads.md#GetSampleV3) | Sample Uploads | Retrieves the file associated with the given ID \(SHA256\) |
| [GetScans](../service-collections/quick-scan.md#GetScans) | Quick Scan | Check the status of a volume scan. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute |
| [GetScansAggregates](../service-collections/quick-scan.md#GetScansAggregates) | Quick Scan | Get scans aggregations as specified via json in request body. |
| [GetSensorInstallersByQuery](../service-collections/sensor-download.md#GetSensorInstallersByQuery) | Sensor Download | Get sensor installer IDs by provided query |
| [GetSensorInstallersCCIDByQuery](../service-collections/sensor-download.md#GetSensorInstallersCCIDByQuery) | Sensor Download | Get CCID to use with sensor installers |
| [GetSensorInstallersEntities](../service-collections/sensor-download.md#GetSensorInstallersEntities) | Sensor Download | Get sensor installer details by provided SHA256 IDs |
| [getSensorUpdatePolicies](../service-collections/sensor-update-policies.md#getSensorUpdatePolicies) | Sensor Update Policies | Retrieve a set of Sensor Update Policies by specifying their IDs |
| [getSensorUpdatePoliciesV2](../service-collections/sensor-update-policies.md#getSensorUpdatePoliciesV2) | Sensor Update Policies | Retrieve a set of Sensor Update Policies with additional support for uninstall protection by specifying their IDs |
| [getSensorVisibilityExclusionsV1](../service-collections/sensor-visibility-exclusions.md#getSensorVisibilityExclusionsV1) | Sensor Visibility Exclusions | Get a set of Sensor Visibility Exclusions by specifying their IDs |
| [GetSubmissions](../service-collections/falconx-sandbox.md#GetSubmissions) | Falconx Sandbox | Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. |
| [GetSummaryReports](../service-collections/falconx-sandbox.md#GetSummaryReports) | Falconx Sandbox | Get a short summary version of a sandbox report. |
| [getUserGroupMembersByID](../service-collections/mssp.md#getUserGroupMembersByID) | MSSP \(Flight Control\) | Get User Group members by User Group ID\(s\). |
| [getUserGroupsByID](../service-collections/mssp.md#getUserGroupsByID) | MSSP \(Flight Control\) | Get User Group by ID\(s\). |
| [GetUserRoleIds](../service-collections/user-management.md#GetUserRoleIds) | User Management | Show role IDs of roles assigned to a user. For more information on each role, provide the role ID to `/customer/entities/roles/v1`. |
| [getVulnerabilities](../service-collections/spotlight-vulnerabilities.md#getVulnerabilities) | Spotlight Vulnerabilities | Get details on vulnerabilities by providing one or more IDs |
| [GrantUserRoleIds](../service-collections/user-management.md#GrantUserRoleIds) | User Management | Assign one or more roles to a user |
| [listAvailableStreamsOAuth2](../service-collections/event-streams.md#listAvailableStreamsOAuth2) | Event Streams | Discover all event streams in your environment |
| [oauth2AccessToken](../service-collections/oauth2.md#oauth2AccessToken) | OAuth2 | Generate an OAuth2 access token |
| [oauth2RevokeToken](../service-collections/oauth2.md#oauth2RevokeToken) | OAuth2 | Revoke a previously issued OAuth2 access token before the end of its standard 30-minute lifespan. |
| [PerformActionV2](../service-collections/hosts.md#PerformActionV2) | Hosts | Take various actions on the hosts in your environment. Contain or lift containment on a host. Delete or restore a host. |
| [performDeviceControlPoliciesAction](../service-collections/device-control-policies.md#performDeviceControlPoliciesAction) | Device Control Policies | Perform the specified action on the Device Control Policies specified in the request |
| [performFirewallPoliciesAction](../service-collections/firewall-policies.md#performFirewallPoliciesAction) | Firewall Policies | Perform the specified action on the Firewall Policies specified in the request |
| [performGroupAction](../service-collections/host-group.md#performGroupAction) | Host Group | Perform the specified action on the Host Groups specified in the request |
| [PerformIncidentAction](../service-collections/incidents.md#PerformIncidentAction) | Incidents | Perform a set of actions on one or more incidents, such as adding tags or comments or updating the incident name or description |
| [performPreventionPoliciesAction](../service-collections/prevention-policies.md#performPreventionPoliciesAction) | Prevention Policies | Perform the specified action on the Prevention Policies specified in the request |
| [performSensorUpdatePoliciesAction](../service-collections/sensor-update-policies.md#performSensorUpdatePoliciesAction) | Sensor Update Policies | Perform the specified action on the Sensor Update Policies specified in the request |
| [PostMalQueryEntitiesSamplesMultidownloadV1](../service-collections/malquery.md#PostMalQueryEntitiesSamplesMultidownloadV1) | Malquery | Schedule samples for download. Use the result id with the /request endpoint to check if the download is ready after which you can call the /entities/samples-fetch to get the zip |
| [PostMalQueryExactSearchV1](../service-collections/malquery.md#PostMalQueryExactSearchV1) | Malquery | Search Falcon MalQuery for a combination of hex patterns and strings in order to identify samples based upon file content at byte level granularity. You can filter results on criteria such as file type, file size and first seen date. Returns a request id which can be used with the /request endpoint |
| [PostMalQueryFuzzySearchV1](../service-collections/malquery.md#PostMalQueryFuzzySearchV1) | Malquery | Search Falcon MalQuery quickly, but with more potential for false positives. Search for a combination of hex patterns and strings in order to identify samples based upon file content at byte level granularity. |
| [PostMalQueryHuntV1](../service-collections/malquery.md#PostMalQueryHuntV1) | Malquery | Schedule a YARA-based search for execution. Returns a request id which can be used with the /request endpoint |
| [ProcessesRanOn](../service-collections/iocs.md#ProcessesRanOn) | IOCs | Search for processes associated with a custom IOC |
| [ProvisionAWSAccounts](../service-collections/cloud-connect-aws.md#ProvisionAWSAccounts) | Cloud Connect AWS | Provision AWS Accounts by specifying details about the accounts to provision |
| [query\_events](../service-collections/firewall-management.md#query_events) | Firewall Management | Find all event IDs matching the query with filter |
| [query\_firewall\_fields](../service-collections/firewall-management.md#query_firewall_fields) | Firewall Management | Get the firewall field specification IDs for the provided platform |
| [query\_patterns](../service-collections/custom-ioa.md#query_patterns) | Custom IOA | Get all pattern severity IDs. |
| [query\_platforms](../service-collections/firewall-management.md#query_platforms) | Firewall Management | Get the list of platform names |
| [query\_platformsMixin0](../service-collections/custom-ioa.md#query_platformsMixin0) | Custom IOA | Get all platform IDs. |
| [query\_policy\_rules](../service-collections/firewall-management.md#query_policy_rules) | Firewall Management | Find all firewall rule IDs matching the query with filter, and return them in precedence order |
| [query\_rule\_groups](../service-collections/firewall-management.md#query_rule_groups) | Firewall Management | Find all rule group IDs matching the query with filter |
| [query\_rule\_groups\_full](../service-collections/custom-ioa.md#query_rule_groups_full) | Custom IOA | Find all rule groups matching the query with optional filter. |
| [query\_rule\_groupsMixin0](../service-collections/custom-ioa.md#query_rule_groupsMixin0) | Custom IOA | Finds all rule group IDs matching the query with optional filter. |
| [query\_rule\_types](../service-collections/custom-ioa.md#query_rule_types) | Custom IOA | Get all rule type IDs. |
| [query\_rules](../service-collections/firewall-management.md#query_rules) | Firewall Management | Find all rule IDs matching the query with filter |
| [query\_rulesMixin0](../service-collections/custom-ioa.md#query_rulesMixin0) | Custom IOA | Finds all rule IDs matching the query with optional filter. |
| [QueryAllowListFilter](../service-collections/falcon-complete-dashboard.md#QueryAllowListFilter) | Falcon Complete Dashboard | Retrieve allowlist tickets that match the provided filter criteria with scrolling enabled |
| [QueryAWSAccounts](../service-collections/cloud-connect-aws.md#QueryAWSAccounts) | Cloud Connect AWS | Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS accounts which match the filter criteria |
| [QueryAWSAccountsForIDs](../service-collections/cloud-connect-aws.md#QueryAWSAccountsForIDs) | Cloud Connect AWS | Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS account IDs which match the filter criteria |
| [QueryBehaviors](../service-collections/incidents.md#QueryBehaviors) | Incidents | Search for behaviors by providing an FQL filter, sorting, and paging details |
| [QueryBlockListFilter](../service-collections/falcon-complete-dashboard.md#QueryBlockListFilter) | Falcon Complete Dashboard | Retrieve block listtickets that match the provided filter criteria with scrolling enabled |
| [queryChildren](../service-collections/mssp.md#queryChildren) | MSSP \(Flight Control\) | Query for customers linked as children |
| [queryCIDGroupMembers](../service-collections/mssp.md#queryCIDGroupMembers) | MSSP \(Flight Control\) | Query a CID Groups members by associated CID. |
| [queryCIDGroups](../service-collections/mssp.md#queryCIDGroups) | MSSP \(Flight Control\) | Query CID Groups. |
| [queryCombinedDeviceControlPolicies](../service-collections/device-control-policies.md#queryCombinedDeviceControlPolicies) | Device Control Policies | Search for Device Control Policies in your environment by providing an FQL filter and paging details. Returns a set of Device Control Policies which match the filter criteria |
| [queryCombinedDeviceControlPolicyMembers](../service-collections/device-control-policies.md#queryCombinedDeviceControlPolicyMembers) | Device Control Policies | Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedFirewallPolicies](../service-collections/firewall-policies.md#queryCombinedFirewallPolicies) | Firewall Policies | Search for Firewall Policies in your environment by providing an FQL filter and paging details. Returns a set of Firewall Policies which match the filter criteria |
| [queryCombinedFirewallPolicyMembers](../service-collections/firewall-policies.md#queryCombinedFirewallPolicyMembers) | Firewall Policies | Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedGroupMembers](../service-collections/host-group.md#queryCombinedGroupMembers) | Host Group | Search for members of a Host Group in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedHostGroups](../service-collections/host-group.md#queryCombinedHostGroups) | Host Group | Search for Host Groups in your environment by providing an FQL filter and paging details. Returns a set of Host Groups which match the filter criteria |
| [queryCombinedPreventionPolicies](../service-collections/prevention-policies.md#queryCombinedPreventionPolicies) | Prevention Policies | Search for Prevention Policies in your environment by providing an FQL filter and paging details. Returns a set of Prevention Policies which match the filter criteria |
| [queryCombinedPreventionPolicyMembers](../service-collections/prevention-policies.md#queryCombinedPreventionPolicyMembers) | Prevention Policies | Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedSensorUpdateBuilds](../service-collections/sensor-update-policies.md#queryCombinedSensorUpdateBuilds) | Sensor Update Policies | Retrieve available builds for use with Sensor Update Policies |
| [queryCombinedSensorUpdatePolicies](../service-collections/sensor-update-policies.md#queryCombinedSensorUpdatePolicies) | Sensor Update Policies | Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria |
| [queryCombinedSensorUpdatePoliciesV2](../service-collections/sensor-update-policies.md#queryCombinedSensorUpdatePoliciesV2) | Sensor Update Policies | Search for Sensor Update Policies with additional support for uninstall protection in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria |
| [queryCombinedSensorUpdatePolicyMembers](../service-collections/sensor-update-policies.md#queryCombinedSensorUpdatePolicyMembers) | Sensor Update Policies | Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [QueryDetectionIdsByFilter](../service-collections/falcon-complete-dashboard.md#QueryDetectionIdsByFilter) | Falcon Complete Dashboard | Retrieve DetectionsIds that match the provided FQL filter, criteria with scrolling enabled |
| [QueryDetects](../service-collections/detects.md#QueryDetects) | Detects | Search for detection IDs that match a given query |
| [queryDeviceControlPolicies](../service-collections/device-control-policies.md#queryDeviceControlPolicies) | Device Control Policies | Search for Device Control Policies in your environment by providing an FQL filter and paging details. Returns a set of Device Control Policy IDs which match the filter criteria |
| [queryDeviceControlPolicyMembers](../service-collections/device-control-policies.md#queryDeviceControlPolicyMembers) | Device Control Policies | Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [QueryDevicesByFilter](../service-collections/hosts.md#QueryDevicesByFilter) | Hosts | Search for hosts in your environment by platform, hostname, IP, and other criteria. |
| [QueryDevicesByFilterScroll](../service-collections/hosts.md#QueryDevicesByFilterScroll) | Hosts | Search for hosts in your environment by platform, hostname, IP, and other criteria with continuous pagination capability \(based on offset pointer which expires after 2 minutes with no maximum limit\) |
| [QueryEscalationsFilter](../service-collections/falcon-complete-dashboard.md#QueryEscalationsFilter) | Falcon Complete Dashboard | Retrieve escalation tickets that match the provided filter criteria with scrolling enabled |
| [queryFirewallPolicies](../service-collections/firewall-policies.md#queryFirewallPolicies) | Firewall Policies | Search for Firewall Policies in your environment by providing an FQL filter and paging details. Returns a set of Firewall Policy IDs which match the filter criteria |
| [queryFirewallPolicyMembers](../service-collections/firewall-policies.md#queryFirewallPolicyMembers) | Firewall Policies | Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [queryGroupMembers](../service-collections/host-group.md#queryGroupMembers) | Host Group | Search for members of a Host Group in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [QueryHiddenDevices](../service-collections/hosts.md#QueryHiddenDevices) | Hosts | Retrieve hidden hosts that match the provided filter criteria. |
| [queryHostGroups](../service-collections/host-group.md#queryHostGroups) | Host Group | Search for Host Groups in your environment by providing an FQL filter and paging details. Returns a set of Host Group IDs which match the filter criteria |
| [QueryIncidentIdsByFilter](../service-collections/falcon-complete-dashboard.md#QueryIncidentIdsByFilter) | Falcon Complete Dashboard | Retrieve incidents that match the provided filter criteria with scrolling enabled |
| [QueryIncidents](../service-collections/incidents.md#QueryIncidents) | Incidents | Search for incidents by providing an FQL filter, sorting, and paging details |
| [QueryIntelActorEntities](../service-collections/intel.md#QueryIntelActorEntities) | Intel | Get info about actors that match provided FQL filters. |
| [QueryIntelActorIds](../service-collections/intel.md#QueryIntelActorIds) | Intel | Get actor IDs that match provided FQL filters. |
| [QueryIntelIndicatorEntities](../service-collections/intel.md#QueryIntelIndicatorEntities) | Intel | Get info about indicators that match provided FQL filters. |
| [QueryIntelIndicatorIds](../service-collections/intel.md#QueryIntelIndicatorIds) | Intel | Get indicators IDs that match provided FQL filters. |
| [QueryIntelReportEntities](../service-collections/intel.md#QueryIntelReportEntities) | Intel | Get info about reports that match provided FQL filters. |
| [QueryIntelReportIds](../service-collections/intel.md#QueryIntelReportIds) | Intel | Get report IDs that match provided FQL filters. |
| [QueryIntelRuleIds](../service-collections/intel.md#QueryIntelRuleIds) | Intel | Search for rule IDs that match provided filter criteria. |
| [queryIOAExclusionsV1](../service-collections/ioa-exclusions.md#queryIOAExclusionsV1) | IOA Exclusions | Search for IOA exclusions. |
| [QueryIOCs](../service-collections/iocs.md#QueryIOCs) | IOCs | Search the custom IOCs in your customer account |
| [queryMLExclusionsV1](../service-collections/ml-exclusions.md#queryMLExclusionsV1) | ML Exclusions | Search for ML exclusions. |
| [queryPreventionPolicies](../service-collections/prevention-policies.md#queryPreventionPolicies) | Prevention Policies | Search for Prevention Policies in your environment by providing an FQL filter and paging details. Returns a set of Prevention Policy IDs which match the filter criteria |
| [queryPreventionPolicyMembers](../service-collections/prevention-policies.md#queryPreventionPolicyMembers) | Prevention Policies | Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [QueryRemediationsFilter](../service-collections/falcon-complete-dashboard.md#QueryRemediationsFilter) | Falcon Complete Dashboard | Retrieve remediation tickets that match the provided filter criteria with scrolling enabled |
| [QueryReports](../service-collections/falconx-sandbox.md#QueryReports) | Falconx Sandbox | Find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs that match your criteria. |
| [queryRoles](../service-collections/mssp.md#queryRoles) | MSSP \(Flight Control\) | Query MSSP Role assignment. At least one of CID Group ID or User Group ID should also be provided. Role ID is optional. |
| [QuerySampleV1](../service-collections/falconx-sandbox.md#QuerySampleV1) | Falconx Sandbox | Retrieves a list with sha256 of samples that exist and customer has rights to access them, maximum number of accepted items is 200 |
| [querySensorUpdatePolicies](../service-collections/sensor-update-policies.md#querySensorUpdatePolicies) | Sensor Update Policies | Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria |
| [querySensorUpdatePolicyMembers](../service-collections/sensor-update-policies.md#querySensorUpdatePolicyMembers) | Sensor Update Policies | Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [querySensorVisibilityExclusionsV1](../service-collections/sensor-visibility-exclusions.md#querySensorVisibilityExclusionsV1) | Sensor Visibility Exclusions | Search for sensor visibility exclusions. |
| [QuerySubmissions](../service-collections/falconx-sandbox.md#QuerySubmissions) | Falconx Sandbox | Find submission IDs for uploaded files by providing an FQL filter and paging details. Returns a set of submission IDs that match your criteria. |
| [QuerySubmissionsMixin0](../service-collections/quick-scan.md#QuerySubmissionsMixin0) | Quick Scan | Find IDs for submitted scans by providing an FQL filter and paging details. Returns a set of volume IDs that match your criteria. |
| [queryUserGroupMembers](../service-collections/mssp.md#queryUserGroupMembers) | MSSP \(Flight Control\) | Query User Group member by User UUID. |
| [queryUserGroups](../service-collections/mssp.md#queryUserGroups) | MSSP \(Flight Control\) | Query User Groups. |
| [queryVulnerabilities](../service-collections/spotlight-vulnerabilities.md#queryVulnerabilities) | Spotlight Vulnerabilities | Search for Vulnerabilities in your environment by providing an FQL filter and paging details. Returns a set of Vulnerability IDs which match the filter criteria |
| [refreshActiveStreamSession](../service-collections/event-streams.md#refreshActiveStreamSession) | Event Streams | Refresh an active event stream. Use the URL shown in a GET /sensors/entities/datafeed/v2 response. |
| [RetrieveEmailsByCID](../service-collections/user-management.md#RetrieveEmailsByCID) | User Management | List the usernames \(usually an email address\) for all users in your customer account |
| [RetrieveUser](../service-collections/user-management.md#RetrieveUser) | User Management | Get info about a user |
| [RetrieveUserUUID](../service-collections/user-management.md#RetrieveUserUUID) | User Management | Get a user's ID by providing a username \(usually an email address\) |
| [RetrieveUserUUIDsByCID](../service-collections/user-management.md#RetrieveUserUUIDsByCID) | User Management | List user IDs for all users in your customer account. For more information on each user, provide the user ID to `/users/entities/user/v1`. |
| [revealUninstallToken](../service-collections/sensor-update-policies.md#revealUninstallToken) | Sensor Update Policies | Reveals an uninstall token for a specific device. To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device\_id' |
| [RevokeUserRoleIds](../service-collections/user-management.md#RevokeUserRoleIds) | User Management | Revoke one or more roles from a user |
| [RTR\_AggregateSessions](../service-collections/real-time-response.md#RTR_AggregateSessions) | Real Time Response | Get aggregates on session data. |
| [RTR\_CheckActiveResponderCommandStatus](../service-collections/real-time-response.md#RTR_CheckActiveResponderCommandStatus) | Real Time Response | Get status of an executed active-responder command on a single host. |
| [RTR\_CheckAdminCommandStatus](../service-collections/real-time-response-admin.md#RTR_CheckAdminCommandStatus) | Real Time Response Admin | Get status of an executed RTR administrator command on a single host. |
| [RTR\_CheckCommandStatus](../service-collections/real-time-response.md#RTR_CheckCommandStatus) | Real Time Response | Get status of an executed command on a single host. |
| [RTR\_CreatePut\_Files](../service-collections/real-time-response-admin.md#RTR_CreatePut_Files) | Real Time Response Admin | Upload a new put-file to use for the RTR `put` command. |
| [RTR\_CreateScripts](../service-collections/real-time-response-admin.md#RTR_CreateScripts) | Real Time Response Admin | Upload a new custom-script to use for the RTR `runscript` command. |
| [RTR\_DeleteFile](../service-collections/real-time-response.md#RTR_DeleteFile) | Real Time Response | Delete a RTR session file. |
| [RTR\_DeletePut\_Files](../service-collections/real-time-response-admin.md#RTR_DeletePut_Files) | Real Time Response Admin | Delete a put-file based on the ID given.  Can only delete one file at a time. |
| [RTR\_DeleteQueuedSession](../service-collections/real-time-response.md#RTR_DeleteQueuedSession) | Real Time Response | Delete a queued session command |
| [RTR\_DeleteScripts](../service-collections/real-time-response-admin.md#RTR_DeleteScripts) | Real Time Response Admin | Delete a custom-script based on the ID given.  Can only delete one script at a time. |
| [RTR\_DeleteSession](../service-collections/real-time-response.md#RTR_DeleteSession) | Real Time Response | Delete a session. |
| [RTR\_ExecuteActiveResponderCommand](../service-collections/real-time-response.md#RTR_ExecuteActiveResponderCommand) | Real Time Response | Execute an active responder command on a single host. |
| [RTR\_ExecuteAdminCommand](../service-collections/real-time-response-admin.md#RTR_ExecuteAdminCommand) | Real Time Response Admin | Execute a RTR administrator command on a single host. |
| [RTR\_ExecuteCommand](../service-collections/real-time-response.md#RTR_ExecuteCommand) | Real Time Response | Execute a command on a single host. |
| [RTR\_GetExtractedFileContents](../service-collections/real-time-response.md#RTR_GetExtractedFileContents) | Real Time Response | Get RTR extracted file contents for specified session and sha256. |
| [RTR\_GetPut\_Files](../service-collections/real-time-response-admin.md#RTR_GetPut_Files) | Real Time Response Admin | Get put-files based on the ID's given. These are used for the RTR `put` command. |
| [RTR\_GetScripts](../service-collections/real-time-response-admin.md#RTR_GetScripts) | Real Time Response Admin | Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command. |
| [RTR\_InitSession](../service-collections/real-time-response.md#RTR_InitSession) | Real Time Response | Initialize a new session with the RTR cloud. |
| [RTR\_ListAllSessions](../service-collections/real-time-response.md#RTR_ListAllSessions) | Real Time Response | Get a list of session\_ids. |
| [RTR\_ListFiles](../service-collections/real-time-response.md#RTR_ListFiles) | Real Time Response | Get a list of files for the specified RTR session. |
| [RTR\_ListPut\_Files](../service-collections/real-time-response-admin.md#RTR_ListPut_Files) | Real Time Response Admin | Get a list of put-file ID's that are available to the user for the `put` command. |
| [RTR\_ListQueuedSessions](../service-collections/real-time-response.md#RTR_ListQueuedSessions) | Real Time Response | Get queued session metadata by session ID. |
| [RTR\_ListScripts](../service-collections/real-time-response-admin.md#RTR_ListScripts) | Real Time Response Admin | Get a list of custom-script ID's that are available to the user for the `runscript` command. |
| [RTR\_ListSessions](../service-collections/real-time-response.md#RTR_ListSessions) | Real Time Response | Get session metadata by session id. |
| [RTR\_PulseSession](../service-collections/real-time-response.md#RTR_PulseSession) | Real Time Response | Refresh a session timeout on a single host. |
| [RTR\_UpdateScripts](../service-collections/real-time-response-admin.md#RTR_UpdateScripts) | Real Time Response Admin | Upload a new scripts to replace an existing one. |
| [ScanSamples](../service-collections/quick-scan.md#ScanSamples) | Quick Scan | Submit a volume of files for ml scanning. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute |
| [setDeviceControlPoliciesPrecedence](../service-collections/device-control-policies.md#setDeviceControlPoliciesPrecedence) | Device Control Policies | Sets the precedence of Device Control Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [setFirewallPoliciesPrecedence](../service-collections/firewall-policies.md#setFirewallPoliciesPrecedence) | Firewall Policies | Sets the precedence of Firewall Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [setPreventionPoliciesPrecedence](../service-collections/prevention-policies.md#setPreventionPoliciesPrecedence) | Prevention Policies | Sets the precedence of Prevention Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [setSensorUpdatePoliciesPrecedence](../service-collections/sensor-update-policies.md#setSensorUpdatePoliciesPrecedence) | Sensor Update Policies | Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [Submit](../service-collections/falconx-sandbox.md#Submit) | Falconx Sandbox | Submit an uploaded file or a URL for sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. |
| [tokens\_create](../service-collections/installation-tokens.md#tokens_create) | Installation Tokens | Creates a token. |
| [tokens\_delete](../service-collections/installation-tokens.md#tokens_delete) | Installation Tokens | Deletes a token immediately. To revoke a token, use PATCH /installation-tokens/entities/tokens/v1 instead. |
| [tokens\_query](../service-collections/installation-tokens.md#tokens_query) | Installation Tokens | Search for tokens by providing an FQL filter and paging details. |
| [tokens\_read](../service-collections/installation-tokens.md#tokens_read) | Installation Tokens | Gets the details of one or more tokens by id. |
| [tokens\_update](../service-collections/installation-tokens.md#tokens_update) | Installation Tokens | Updates one or more tokens. Use this endpoint to edit labels, change expiration, revoke, or restore. |
| [update\_policy\_container](../service-collections/firewall-management.md#update_policy_container) | Firewall Management | Update an identified policy container |
| [update\_rule\_group](../service-collections/firewall-management.md#update_rule_group) | Firewall Management | Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules |
| [update\_rule\_groupMixin0](../service-collections/custom-ioa.md#update_rule_groupMixin0) | Custom IOA | Update a rule group. The following properties can be modified: name, description, enabled. |
| [update\_rules](../service-collections/custom-ioa.md#update_rules) | Custom IOA | Update rules within a rule group. Return the updated rules. |
| [UpdateAWSAccounts](../service-collections/cloud-connect-aws.md#UpdateAWSAccounts) | Cloud Connect AWS | Update AWS Accounts by specifying the ID of the account and details to update |
| [updateCIDGroups](../service-collections/mssp.md#updateCIDGroups) | MSSP \(Flight Control\) | Update existing CID Group\(s\). CID Group ID is expected for each CID Group definition provided in request body. CID Group member\(s\) remain unaffected. |
| [UpdateCSPMAzureAccountClientID](../service-collections/d4c-registration.md#UpdateCSPMAzureAccountClientID) | D4C Registration | Update an Azure service account in our system by with the user-created client\_id created with the public key we've provided |
| [UpdateCSPMAzureAccountClientID](../service-collections/cspm-registration.md#UpdateCSPMAzureAccountClientID) | CSPM Registration | Update an Azure service account in our system by with the user-created client\_id created with the public key we've provided |
| [UpdateCSPMPolicySettings](../service-collections/cspm-registration.md#UpdateCSPMPolicySettings) | CSPM Registration | Updates a policy setting - can be used to override policy severity or to disable a policy entirely. |
| [UpdateCSPMScanSchedule](../service-collections/cspm-registration.md#UpdateCSPMScanSchedule) | CSPM Registration | Updates scan schedule configuration for one or more cloud platforms. |
| [UpdateDetectsByIdsV2](../service-collections/detects.md#UpdateDetectsByIdsV2) | Detects | Modify the state, assignee, and visibility of detections |
| [updateDeviceControlPolicies](../service-collections/device-control-policies.md#updateDeviceControlPolicies) | Device Control Policies | Update Device Control Policies by specifying the ID of the policy and details to update |
| [UpdateDeviceTags](../service-collections/hosts.md#UpdateDeviceTags) | Hosts | Append or remove one or more Falcon Grouping Tags on one or more hosts. |
| [updateFirewallPolicies](../service-collections/firewall-policies.md#updateFirewallPolicies) | Firewall Policies | Update Firewall Policies by specifying the ID of the policy and details to update |
| [updateHostGroups](../service-collections/host-group.md#updateHostGroups) | Host Group | Update Host Groups by specifying the ID of the group and details to update |
| [updateIOAExclusionsV1](../service-collections/ioa-exclusions.md#updateIOAExclusionsV1) | IOA Exclusions | Update the IOA exclusions |
| [UpdateIOC](../service-collections/iocs.md#UpdateIOC) | IOCs | Update an IOC by providing a type and value |
| [updateMLExclusionsV1](../service-collections/ml-exclusions.md#updateMLExclusionsV1) | ML Exclusions | Update the ML exclusions |
| [updatePreventionPolicies](../service-collections/prevention-policies.md#updatePreventionPolicies) | Prevention Policies | Update Prevention Policies by specifying the ID of the policy and details to update |
| [updateSensorUpdatePolicies](../service-collections/sensor-update-policies.md#updateSensorUpdatePolicies) | Sensor Update Policies | Update Sensor Update Policies by specifying the ID of the policy and details to update |
| [updateSensorUpdatePoliciesV2](../service-collections/sensor-update-policies.md#updateSensorUpdatePoliciesV2) | Sensor Update Policies | Update Sensor Update Policies by specifying the ID of the policy and details to update with additional support for uninstall protection |
| [updateSensorVisibilityExclusionsV1](../service-collections/sensor-visibility-exclusions.md#updateSensorVisibilityExclusionsV1) | Sensor Visibility Exclusions | Update the sensor visibility exclusions |
| [UpdateUser](../service-collections/user-management.md#UpdateUser) | User Management | Modify an existing user's first or last name |
| [updateUserGroups](../service-collections/mssp.md#updateUserGroups) | MSSP \(Flight Control\) | Update existing User Group\(s\). User Group ID is expected for each User Group definition provided in request body. User Group member\(s\) remain unaffected. |
| [UploadSampleV2](../service-collections/falconx-sandbox.md#UploadSampleV2) | Falconx Sandbox | Upload a file for sandbox analysis. After uploading, use `/falconx/entities/submissions/v1` to start analyzing the file. |
| [UploadSampleV3](../service-collections/sample-uploads.md#UploadSampleV3) | Sample Uploads | Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint. |
| [validate](../service-collections/custom-ioa.md#validate) | Custom IOA | Validates field values and checks for matches if a test string is provided. |
| [VerifyAWSAccountAccess](../service-collections/cloud-connect-aws.md#VerifyAWSAccountAccess) | Cloud Connect AWS | Performs an Access Verification check on the specified AWS Account IDs |

