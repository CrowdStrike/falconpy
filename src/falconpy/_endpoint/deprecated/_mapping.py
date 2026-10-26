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

_deprecated_op_mapping = {
    "QueryAWSAccounts": "GetCSPMAwsAccount",
    "GetAWSSettings": "",
    "GetAWSAccounts": "GetCSPMAwsAccount",
    "ProvisionAWSAccounts": "CreateCSPMAwsAccount",
    "DeleteAWSAccounts": "DeleteCSPMAwsAccount",
    "UpdateAWSAccounts": "PatchCSPMAwsAccount",
    "CreateOrUpdateAWSSettings": "",
    "VerifyAWSAccountAccess": "",
    "GetD4CAwsAccount": "GetCSPMAwsAccount",
    "CreateD4CAwsAccount": "CreateCSPMAwsAccount",
    "DeleteD4CAwsAccount": "DeleteCSPMAwsAccount",
    "GetD4CAwsConsoleSetupURLs": "GetCSPMAwsConsoleSetupURLs",
    "GetD4CAWSAccountScriptsAttachment": "GetCSPMAwsAccountScriptsAttachment",
    "GetDiscoverCloudAzureAccount": "GetCSPMAzureAccount",
    "CreateDiscoverCloudAzureAccount": "CreateCSPMAzureAccount",
    "UpdateDiscoverCloudAzureAccountClientID": "UpdateCSPMAzureAccountClientID",
    "GetDiscoverCloudAzureUserScriptsAttachment": "GetCSPMAzureUserScriptsAttachment",
    "GetDiscoverCloudCGPAccount": "",
    "CreateDiscoverCloudGCPAccount": "",
    "DiscoverCloudAzureDownloadCertificate": "AzureDownloadCertificate",
    "GetDiscoverCloudAzureTenantIDs": "",
    "GetDiscoverCloudGCPUserScripts": "",
    "GetHorizonD4CScripts": "",
    "GetAggregateDetects": "",
    "UpdateDetectsByIdsV2": "",
    "GetDetectSummaries": "",
    "QueryDetects": "",
    "AggregateFCIncidents": "",
    "QueryIncidentIdsByFilter": "",
    "CrowdScore": "",
    "GetBehaviors": "",
    "PerformIncidentAction": "",
    "GetIncidents": "",
    "QueryBehaviors": "",
    "QueryIncidents": "",
    "download_azure_script": "",
    "CreateFileV1": "",
    "UpdateFileV1": "",
    "combinedQueryInstalledPatches": "",
    "AggregatesKnowledgeBaseAuditEventsV1": "",
    "AggregatesKnowledgeBasesV1": "",
    "WorkflowExecuteInternal": "",
    "GetConfigurationDetections": "",
    "ArchiveUploadV1": "ArchiveUploadV2",
    "AzureDownloadCertificate": "",
    "AzureRefreshCertificate": "",
    "ConnectCSPMGCPAccount": "",
    "CreateCSPMAwsAccount": "",
    "CreateCSPMAzureAccount": "",
    "CreateCSPMAzureManagementGroup": "",
    "CreateCSPMGCPAccount": "",
    "CreateParser": "",
    "CreateUser": "",
    "DeleteCSPMAwsAccount": "",
    "DeleteCSPMAzureAccount": "",
    "DeleteCSPMAzureManagementGroup": "",
    "DeleteCSPMGCPAccount": "",
    "DeleteUser": "",
    "DownloadFile": "",
    "EnumerateFile": "",
    "FetchFilesDownloadInfo": "FetchFilesDownloadInfoV2",
    "GetAvailableRoleIds": "",
    "GetCSPMAwsAccount": "",
    "GetCSPMAwsConsoleSetupURLs": "",
    "GetCSPMAzureAccount": "",
    "GetCSPMAzureManagementGroup": "",
    "GetCSPMAzureUserScriptsAttachment": "",
    "GetCSPMGCPAccount": "",
    "GetCSPMGCPServiceAccountsExt": "",
    "GetCSPMGCPUserScriptsAttachment": "",
    "GetCSPMGCPValidateAccountsExt": "",
    "GetParser": "",
    "GetQueriesAlertsV1": "GetQueriesAlertsV2",
    "GetRoles": "",
    "GetUserRoleIds": "",
    "GrantUserRoleIds": "",
    "ImageMatchesPolicy": "",
    "PatchCSPMAwsAccount": "",
    "PatchEntitiesAlertsV2": "PatchEntitiesAlertsV3",
    "PostAggregatesAlertsV1": "PostAggregatesAlertsV2",
    "PostEntitiesAlertsV1": "PostEntitiesAlertsV2",
    "QueryDevicesByFilterScroll": "",
    "RetrieveEmailsByCID": "",
    "RetrieveUser": "",
    "RetrieveUserUUID": "",
    "RetrieveUserUUIDsByCID": "",
    "RevokeUserRoleIds": "",
    "UpdateCSPMAzureAccount": "",
    "UpdateCSPMAzureAccountClientID": "",
    "UpdateCSPMAzureTenantDefaultSubscriptionID": "",
    "UpdateCSPMGCPAccount": "",
    "UpdateCSPMGCPServiceAccountsExt": "",
    "UpdateParser": "",
    "UpdateUser": "",
    "ValidateCSPMGCPServiceAccountExt": "",
    "aggregates.notification-groups.post.v1": "aggregates_notification_groups_post_v2",
    "aggregates_notification_groups_post_v1": "aggregates_notification_groups_post_v2",
    "combinedUserRolesV1": "CombinedUserRolesV3",
    "createDeviceControlPolicies": "postDeviceControlPoliciesV2",
    "deleteCIDGroupMembers": "deleteCIDGroupMembersV2",
    "deleteCIDGroupMembersV1": "deleteCIDGroupMembersV2",
    "entities.files_download.post.v1": "",
    "entities.notification-groups.delete.v1": "entities_notification_groups_delete_v2",
    "entities.notification-groups.get.v1": "entities_notification_groups_get_v2",
    "entities.notification-groups.patch.v1": "entities_notification_groups_patch_v2",
    "entities.notification-groups.post.v1": "entities_notification_groups_post_v2",
    "entitiesRolesV1": "",
    "entities_files_download_post_v1": "",
    "entities_notification_groups_delete_v1": "entities_notification_groups_delete_v2",
    "entities_notification_groups_get_v1": "entities_notification_groups_get_v2",
    "entities_notification_groups_patch_v1": "entities_notification_groups_patch_v2",
    "entities_notification_groups_post_v1": "entities_notification_groups_post_v2",
    "getCIDGroupByIdV1": "getCIDGroupByIdV2",
    "getCIDGroupMembersByV1": "getCIDGroupMembersByV2",
    "getCloudEventIDs": "",
    "getDefaultDeviceControlPolicies": "",
    "getDeviceControlPolicies": "getDeviceControlPoliciesV2",
    "getUserGroupMembersByIDV1": "getUserGroupMembersByIDV2",
    "getUserGroupsByIDV1": "getUserGroupsByIDV2",
    "queries.notification-groups.get.v1": "queries_notification_groups_get_v2",
    "queries_notification_groups_get_v1": "queries_notification_groups_get_v2",
    "queryCombinedDeviceControlPolicies": "",
    "retrieveUser": "",
    "updateDefaultDeviceControlPolicies": "",
    "updateDeviceControlPolicies": "patchDeviceControlPoliciesV2"
}

_deprecated_cls_mapping = {
    "CloudConnectAWS": "CSPMRegistration",
    "D4CRegistration": "CSPMRegistration",
    "Iocs": "IOC",
    "Detects": "Alerts"
}
