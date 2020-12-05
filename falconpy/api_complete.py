#####################################################################################################
# CROWDSTRIKE FALCON                                                                                #
# OAuth2 API - Customer SDK                                                                         #
#                                                                                                   #
# api_complete.py - All-in-one CrowdStrike Falcon OAuth2 API harness                                #
#####################################################################################################
# Copyright CrowdStrike 2020

# By accessing or using this script, sample code, application programming interface, tools, 
# and/or associated documentation (if any) (collectively, “Tools”), You (i) represent and 
# warrant that You are entering into this Agreement on behalf of a company, organization 
# or another legal entity (“Entity”) that is currently a customer or partner of 
# CrowdStrike, Inc. (“CrowdStrike”), and (ii) have the authority to bind such Entity and 
# such Entity agrees to be bound by this Agreement.

# CrowdStrike grants Entity a non-exclusive, non-transferable, non-sublicensable, royalty 
# free and limited license to access and use the Tools solely for Entity’s internal business 
# purposes and in accordance with its obligations under any agreement(s) it may have with 
# CrowdStrike. Entity acknowledges and agrees that CrowdStrike and its licensors retain all 
# right, title and interest in and to the Tools, and all intellectual property rights 
# embodied therein, and that Entity has no right, title or interest therein except for the 
# express licenses granted hereunder and that Entity will treat such Tools as CrowdStrike’s 
# confidential information.

# THE TOOLS ARE PROVIDED “AS-IS” WITHOUT WARRANTY OF ANY KIND, WHETHER EXPRESS, IMPLIED OR 
# STATUTORY OR OTHERWISE. CROWDSTRIKE SPECIFICALLY DISCLAIMS ALL SUPPORT OBLIGATIONS AND 
# ALL WARRANTIES, INCLUDING WITHOUT LIMITATION, ALL IMPLIED WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT. IN NO EVENT SHALL CROWDSTRIKE 
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THE TOOLS, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import requests
import json
import time
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class APIHarness:
    """ This one does it all. It's like the One Ring with significantly fewer orcs. """

    def __init__(self, creds, base_url="https://api.crowdstrike.com"):
        """ Instantiates an instance of the base class, ingests credentials and the base URL and initializes global variables. """
    
        self.creds = creds
        self.base_url = base_url
        self.token = False
        self.token_expiration = 0
        self.token_renew_window = 20
        self.token_time = time.time()
        self.token_expired = lambda: True if (time.time() - self.token_time) >= (self.token_expiration - self.token_renew_window) else False
        self.authenticated = False
        self.valid_cred_format = lambda: True if "client_id" in self.creds and "client_secret" in self.creds else False
        self.headers = lambda: { 'Authorization': 'Bearer {}'.format(self.token) } if self.token else {}
        # This is a list of available commands, additional endpoints (commands) can be added ad-hoc
        # [Command Name, HTTP Method, Endpoint]
        self.commands = [
            ["QueryAWSAccounts", "GET", "/cloud-connect-aws/combined/accounts/v1"], 
            ["GetAWSSettings", "GET", "/cloud-connect-aws/combined/settings/v1"], 
            ["GetAWSAccounts", "GET", "/cloud-connect-aws/entities/accounts/v1?ids={}"], 
            ["ProvisionAWSAccounts", "POST", "/cloud-connect-aws/entities/accounts/v1"], 
            ["UpdateAWSAccounts", "PATCH", "/cloud-connect-aws/entities/accounts/v1"], 
            ["DeleteAWSAccounts", "DELETE", "/cloud-connect-aws/entities/accounts/v1?ids={}"], 
            ["CreateOrUpdateAWSSettings", "POST", "/cloud-connect-aws/entities/settings/v1"], 
            ["VerifyAWSAccountAccess", "POST", "/cloud-connect-aws/entities/verify-account-access/v1?ids={}"], 
            ["QueryAWSAccountsForIDs", "GET", "/cloud-connect-aws/queries/accounts/v1"], 
            ["GetCSPMAzureAccount", "GET", "/cloud-connect-azure/entities/account/v1?ids={}"], 
            ["CreateCSPMAzureAccount", "POST", "/cloud-connect-azure/entities/account/v1"], 
            ["UpdateCSPMAzureAccountClientID", "PATCH", "/cloud-connect-azure/entities/client-id/v1"], 
            ["GetCSPMAzureUserScriptsAttachment", "GET", "/cloud-connect-azure/entities/user-scripts-download/v1"], 
            ["GetCSPMAzureUserScripts", "GET", "/cloud-connect-azure/entities/user-scripts/v1"], 
            ["GetCSPMAwsAccount", "GET", "/cloud-connect-cspm-aws/entities/account/v1?ids={}"], 
            ["CreateCSPMAwsAccount", "POST", "/cloud-connect-cspm-aws/entities/account/v1"], 
            ["DeleteCSPMAwsAccount", "DELETE", "/cloud-connect-cspm-aws/entities/account/v1?ids={}"], 
            ["GetCSPMAwsConsoleSetupURLs", "GET", "/cloud-connect-cspm-aws/entities/console-setup-urls/v1"], 
            ["GetCSPMAwsAccountScriptsAttachment", "GET", "/cloud-connect-cspm-aws/entities/user-scripts-download/v1"], 
            ["GetCSPMAzureAccount", "GET", "/cloud-connect-cspm-azure/entities/account/v1?ids={}"], 
            ["CreateCSPMAzureAccount", "POST", "/cloud-connect-cspm-azure/entities/account/v1"], 
            ["DeleteCSPMAzureAccount", "DELETE", "/cloud-connect-cspm-azure/entities/account/v1?ids={}"], 
            ["UpdateCSPMAzureAccountClientID", "PATCH", "/cloud-connect-cspm-azure/entities/client-id/v1"], 
            ["GetCSPMAzureUserScriptsAttachment", "GET", "/cloud-connect-cspm-azure/entities/user-scripts-download/v1"], 
            ["GetCSPMCGPAccount", "GET", "/cloud-connect-gcp/entities/account/v1?ids={}"], 
            ["CreateCSPMGCPAccount", "POST", "/cloud-connect-gcp/entities/account/v1"], 
            ["GetCSPMGCPUserScriptsAttachment", "GET", "/cloud-connect-gcp/entities/user-scripts-download/v1"], 
            ["GetCSPMGCPUserScripts", "GET", "/cloud-connect-gcp/entities/user-scripts/v1"], 
            ["GetAggregateDetects", "POST", "/detects/aggregates/detects/GET/v1"], 
            ["UpdateDetectsByIdsV2", "PATCH", "/detects/entities/detects/v2"], 
            ["GetDetectSummaries", "POST", "/detects/entities/summaries/GET/v1"], 
            ["QueryDetects", "GET", "/detects/queries/detects/v1"], 
            ["queryCombinedGroupMembers", "GET", "/devices/combined/host-group-members/v1"], 
            ["queryCombinedHostGroups", "GET", "/devices/combined/host-groups/v1"], 
            ["PerformActionV2", "POST", "/devices/entities/devices-actions/v2"], 
            ["GetDeviceDetails", "GET", "/devices/entities/devices/v1?ids={}"], 
            ["performGroupAction", "POST", "/devices/entities/host-group-actions/v1"], 
            ["getHostGroups", "GET", "/devices/entities/host-groups/v1?ids={}"], 
            ["createHostGroups", "POST", "/devices/entities/host-groups/v1"], 
            ["updateHostGroups", "PATCH", "/devices/entities/host-groups/v1"], 
            ["deleteHostGroups", "DELETE", "/devices/entities/host-groups/v1?ids={}"], 
            ["QueryHiddenDevices", "GET", "/devices/queries/devices-hidden/v1"], 
            ["QueryDevicesByFilterScroll", "GET", "/devices/queries/devices-scroll/v1"], 
            ["QueryDevicesByFilter", "GET", "/devices/queries/devices/v1"], 
            ["queryGroupMembers", "GET", "/devices/queries/host-group-members/v1"], 
            ["queryHostGroups", "GET", "/devices/queries/host-groups/v1"], 
            ["GetArtifacts", "GET", "/falconx/entities/artifacts/v1"], 
            ["GetSummaryReports", "GET", "/falconx/entities/report-summaries/v1?ids={}"], 
            ["GetReports", "GET", "/falconx/entities/reports/v1?ids={}"], 
            ["DeleteReport", "DELETE", "/falconx/entities/reports/v1?ids={}"], 
            ["GetSubmissions", "GET", "/falconx/entities/submissions/v1?ids={}"], 
            ["Submit", "POST", "/falconx/entities/submissions/v1"], 
            ["QueryReports", "GET", "/falconx/queries/reports/v1"], 
            ["QuerySubmissions", "GET", "/falconx/queries/submissions/v1"], 
            ["aggregate-events", "POST", "/fwmgr/aggregates/events/GET/v1"], 
            ["aggregate-policy-rules", "POST", "/fwmgr/aggregates/policy-rules/GET/v1"], 
            ["aggregate-rule-groups", "POST", "/fwmgr/aggregates/rule-groups/GET/v1"], 
            ["aggregate-rules", "POST", "/fwmgr/aggregates/rules/GET/v1"], 
            ["get-events", "GET", "/fwmgr/entities/events/v1?ids={}"], 
            ["get-firewall-fields", "GET", "/fwmgr/entities/firewall-fields/v1?ids={}"], 
            ["get-platforms", "GET", "/fwmgr/entities/platforms/v1?ids={}"], 
            ["get-policy-containers", "GET", "/fwmgr/entities/policies/v1?ids={}"], 
            ["get-rule-groups", "GET", "/fwmgr/entities/rule-groups/v1?ids={}"], 
            ["create-rule-group", "POST", "/fwmgr/entities/rule-groups/v1"], 
            ["update-rule-group", "PATCH", "/fwmgr/entities/rule-groups/v1"], 
            ["delete-rule-groups", "DELETE", "/fwmgr/entities/rule-groups/v1?ids={}"], 
            ["get-rules", "GET", "/fwmgr/entities/rules/v1?ids={}"], 
            ["query-events", "GET", "/fwmgr/queries/events/v1"], 
            ["query-firewall-fields", "GET", "/fwmgr/queries/firewall-fields/v1"], 
            ["query-platforms", "GET", "/fwmgr/queries/platforms/v1"], 
            ["query-policy-rules", "GET", "/fwmgr/queries/policy-rules/v1"], 
            ["query-rule-groups", "GET", "/fwmgr/queries/rule-groups/v1"], 
            ["query-rules", "GET", "/fwmgr/queries/rules/v1"], 
            ["CrowdScore", "GET", "/incidents/combined/crowdscores/v1"], 
            ["GetBehaviors", "POST", "/incidents/entities/behaviors/GET/v1"], 
            ["PerformIncidentAction", "POST", "/incidents/entities/incident-actions/v1"], 
            ["GetIncidents", "POST", "/incidents/entities/incidents/GET/v1"], 
            ["QueryBehaviors", "GET", "/incidents/queries/behaviors/v1"], 
            ["QueryIncidents", "GET", "/incidents/queries/incidents/v1"], 
            ["DevicesCount", "GET", "/indicators/aggregates/devices-count/v1"], 
            ["GetIOC", "GET", "/indicators/entities/iocs/v1"], 
            ["CreateIOC", "POST", "/indicators/entities/iocs/v1"], 
            ["UpdateIOC", "PATCH", "/indicators/entities/iocs/v1"], 
            ["DeleteIOC", "DELETE", "/indicators/entities/iocs/v1"], 
            ["DevicesRanOn", "GET", "/indicators/queries/devices/v1"], 
            ["QueryIOCs", "GET", "/indicators/queries/iocs/v1"], 
            ["ProcessesRanOn", "GET", "/indicators/queries/processes/v1"], 
            ["audit-events-read", "GET", "/installation-tokens/entities/audit-events/v1?ids={}"], 
            ["customer-settings-read", "GET", "/installation-tokens/entities/customer-settings/v1"], 
            ["tokens-read", "GET", "/installation-tokens/entities/tokens/v1?ids={}"], 
            ["tokens-create", "POST", "/installation-tokens/entities/tokens/v1"], 
            ["tokens-update", "PATCH", "/installation-tokens/entities/tokens/v1?ids={}"], 
            ["tokens-delete", "DELETE", "/installation-tokens/entities/tokens/v1?ids={}"], 
            ["audit-events-query", "GET", "/installation-tokens/queries/audit-events/v1"], 
            ["tokens-query", "GET", "/installation-tokens/queries/tokens/v1"], 
            ["QueryIntelActorEntities", "GET", "/intel/combined/actors/v1"], 
            ["QueryIntelIndicatorEntities", "GET", "/intel/combined/indicators/v1"], 
            ["QueryIntelReportEntities", "GET", "/intel/combined/reports/v1"], 
            ["GetIntelActorEntities", "GET", "/intel/entities/actors/v1?ids={}"], 
            ["GetIntelIndicatorEntities", "POST", "/intel/entities/indicators/GET/v1"], 
            ["GetIntelReportPDF", "GET", "/intel/entities/report-files/v1"], 
            ["GetIntelReportEntities", "GET", "/intel/entities/reports/v1?ids={}"], 
            ["GetIntelRuleFile", "GET", "/intel/entities/rules-files/v1"], 
            ["GetLatestIntelRuleFile", "GET", "/intel/entities/rules-latest-files/v1"], 
            ["GetIntelRuleEntities", "GET", "/intel/entities/rules/v1?ids={}"], 
            ["QueryIntelActorIds", "GET", "/intel/queries/actors/v1"], 
            ["QueryIntelIndicatorIds", "GET", "/intel/queries/indicators/v1"], 
            ["QueryIntelReportIds", "GET", "/intel/queries/reports/v1"], 
            ["QueryIntelRuleIds", "GET", "/intel/queries/rules/v1"], 
            ["get-patterns", "GET", "/ioarules/entities/pattern-severities/v1?ids={}"], 
            ["get-platformsMixin0", "GET", "/ioarules/entities/platforms/v1?ids={}"], 
            ["get-rule-groupsMixin0", "GET", "/ioarules/entities/rule-groups/v1?ids={}"], 
            ["create-rule-groupMixin0", "POST", "/ioarules/entities/rule-groups/v1"], 
            ["update-rule-groupMixin0", "PATCH", "/ioarules/entities/rule-groups/v1"], 
            ["delete-rule-groupsMixin0", "DELETE", "/ioarules/entities/rule-groups/v1?ids={}"], 
            ["get-rule-types", "GET", "/ioarules/entities/rule-types/v1?ids={}"], 
            ["get-rules-get", "POST", "/ioarules/entities/rules/GET/v1"], 
            ["get-rulesMixin0", "GET", "/ioarules/entities/rules/v1?ids={}"], 
            ["create-rule", "POST", "/ioarules/entities/rules/v1"], 
            ["update-rules", "PATCH", "/ioarules/entities/rules/v1"], 
            ["delete-rules", "DELETE", "/ioarules/entities/rules/v1?ids={}"], 
            ["validate", "POST", "/ioarules/entities/rules/validate/v1"], 
            ["query-patterns", "GET", "/ioarules/queries/pattern-severities/v1"], 
            ["query-platformsMixin0", "GET", "/ioarules/queries/platforms/v1"], 
            ["query-rule-groups-full", "GET", "/ioarules/queries/rule-groups-full/v1"], 
            ["query-rule-groupsMixin0", "GET", "/ioarules/queries/rule-groups/v1"], 
            ["query-rule-types", "GET", "/ioarules/queries/rule-types/v1"], 
            ["query-rulesMixin0", "GET", "/ioarules/queries/rules/v1"], 
            ["GetMalQueryQuotasV1", "GET", "/malquery/aggregates/quotas/v1"], 
            ["PostMalQueryFuzzySearchV1", "POST", "/malquery/combined/fuzzy-search/v1"], 
            ["GetMalQueryDownloadV1", "GET", "/malquery/entities/download-files/v1?ids={}"], 
            ["GetMalQueryMetadataV1", "GET", "/malquery/entities/metadata/v1?ids={}"], 
            ["GetMalQueryRequestV1", "GET", "/malquery/entities/requests/v1?ids={}"], 
            ["GetMalQueryEntitiesSamplesFetchV1", "GET", "/malquery/entities/samples-fetch/v1?ids={}"], 
            ["PostMalQueryEntitiesSamplesMultidownloadV1", "POST", "/malquery/entities/samples-multidownload/v1"], 
            ["PostMalQueryExactSearchV1", "POST", "/malquery/queries/exact-search/v1"], 
            ["PostMalQueryHuntV1", "POST", "/malquery/queries/hunt/v1"], 
            ["oauth2RevokeToken", "POST", "/oauth2/revoke"], 
            ["oauth2AccessToken", "POST", "/oauth2/token"], 
            ["queryCombinedDeviceControlPolicyMembers", "GET", "/policy/combined/device-control-members/v1"], 
            ["queryCombinedDeviceControlPolicies", "GET", "/policy/combined/device-control/v1"], 
            ["queryCombinedFirewallPolicyMembers", "GET", "/policy/combined/firewall-members/v1"], 
            ["queryCombinedFirewallPolicies", "GET", "/policy/combined/firewall/v1"], 
            ["queryCombinedPreventionPolicyMembers", "GET", "/policy/combined/prevention-members/v1"], 
            ["queryCombinedPreventionPolicies", "GET", "/policy/combined/prevention/v1"], 
            ["revealUninstallToken", "POST", "/policy/combined/reveal-uninstall-token/v1"], 
            ["queryCombinedSensorUpdateBuilds", "GET", "/policy/combined/sensor-update-builds/v1"], 
            ["queryCombinedSensorUpdatePolicyMembers", "GET", "/policy/combined/sensor-update-members/v1"], 
            ["queryCombinedSensorUpdatePolicies", "GET", "/policy/combined/sensor-update/v1"], 
            ["queryCombinedSensorUpdatePoliciesV2", "GET", "/policy/combined/sensor-update/v2"], 
            ["performDeviceControlPoliciesAction", "POST", "/policy/entities/device-control-actions/v1"], 
            ["setDeviceControlPoliciesPrecedence", "POST", "/policy/entities/device-control-precedence/v1"], 
            ["getDeviceControlPolicies", "GET", "/policy/entities/device-control/v1?ids={}"], 
            ["createDeviceControlPolicies", "POST", "/policy/entities/device-control/v1"], 
            ["updateDeviceControlPolicies", "PATCH", "/policy/entities/device-control/v1"], 
            ["deleteDeviceControlPolicies", "DELETE", "/policy/entities/device-control/v1?ids={}"], 
            ["performFirewallPoliciesAction", "POST", "/policy/entities/firewall-actions/v1"], 
            ["setFirewallPoliciesPrecedence", "POST", "/policy/entities/firewall-precedence/v1"], 
            ["getFirewallPolicies", "GET", "/policy/entities/firewall/v1?ids={}"], 
            ["createFirewallPolicies", "POST", "/policy/entities/firewall/v1"], 
            ["updateFirewallPolicies", "PATCH", "/policy/entities/firewall/v1"], 
            ["deleteFirewallPolicies", "DELETE", "/policy/entities/firewall/v1?ids={}"], 
            ["getIOAExclusionsV1", "GET", "/policy/entities/ioa-exclusions/v1?ids={}"], 
            ["createIOAExclusionsV1", "POST", "/policy/entities/ioa-exclusions/v1"], 
            ["updateIOAExclusionsV1", "PATCH", "/policy/entities/ioa-exclusions/v1"], 
            ["deleteIOAExclusionsV1", "DELETE", "/policy/entities/ioa-exclusions/v1?ids={}"], 
            ["getMLExclusionsV1", "GET", "/policy/entities/ml-exclusions/v1?ids={}"], 
            ["createMLExclusionsV1", "POST", "/policy/entities/ml-exclusions/v1"], 
            ["updateMLExclusionsV1", "PATCH", "/policy/entities/ml-exclusions/v1"], 
            ["deleteMLExclusionsV1", "DELETE", "/policy/entities/ml-exclusions/v1?ids={}"], 
            ["performPreventionPoliciesAction", "POST", "/policy/entities/prevention-actions/v1"], 
            ["setPreventionPoliciesPrecedence", "POST", "/policy/entities/prevention-precedence/v1"], 
            ["getPreventionPolicies", "GET", "/policy/entities/prevention/v1?ids={}"], 
            ["createPreventionPolicies", "POST", "/policy/entities/prevention/v1"], 
            ["updatePreventionPolicies", "PATCH", "/policy/entities/prevention/v1"], 
            ["deletePreventionPolicies", "DELETE", "/policy/entities/prevention/v1?ids={}"], 
            ["performSensorUpdatePoliciesAction", "POST", "/policy/entities/sensor-update-actions/v1"], 
            ["setSensorUpdatePoliciesPrecedence", "POST", "/policy/entities/sensor-update-precedence/v1"], 
            ["getSensorUpdatePolicies", "GET", "/policy/entities/sensor-update/v1?ids={}"], 
            ["createSensorUpdatePolicies", "POST", "/policy/entities/sensor-update/v1"], 
            ["updateSensorUpdatePolicies", "PATCH", "/policy/entities/sensor-update/v1"], 
            ["deleteSensorUpdatePolicies", "DELETE", "/policy/entities/sensor-update/v1?ids={}"], 
            ["getSensorUpdatePoliciesV2", "GET", "/policy/entities/sensor-update/v2?ids={}"], 
            ["createSensorUpdatePoliciesV2", "POST", "/policy/entities/sensor-update/v2"], 
            ["updateSensorUpdatePoliciesV2", "PATCH", "/policy/entities/sensor-update/v2"], 
            ["getSensorVisibilityExclusionsV1", "GET", "/policy/entities/sv-exclusions/v1?ids={}"], 
            ["createSVExclusionsV1", "POST", "/policy/entities/sv-exclusions/v1"], 
            ["updateSensorVisibilityExclusionsV1", "PATCH", "/policy/entities/sv-exclusions/v1"], 
            ["deleteSensorVisibilityExclusionsV1", "DELETE", "/policy/entities/sv-exclusions/v1?ids={}"], 
            ["queryDeviceControlPolicyMembers", "GET", "/policy/queries/device-control-members/v1"], 
            ["queryDeviceControlPolicies", "GET", "/policy/queries/device-control/v1"], 
            ["queryFirewallPolicyMembers", "GET", "/policy/queries/firewall-members/v1"], 
            ["queryFirewallPolicies", "GET", "/policy/queries/firewall/v1"], 
            ["queryIOAExclusionsV1", "GET", "/policy/queries/ioa-exclusions/v1"], 
            ["queryMLExclusionsV1", "GET", "/policy/queries/ml-exclusions/v1"], 
            ["queryPreventionPolicyMembers", "GET", "/policy/queries/prevention-members/v1"], 
            ["queryPreventionPolicies", "GET", "/policy/queries/prevention/v1"], 
            ["querySensorUpdatePolicyMembers", "GET", "/policy/queries/sensor-update-members/v1"], 
            ["querySensorUpdatePolicies", "GET", "/policy/queries/sensor-update/v1"], 
            ["querySensorVisibilityExclusionsV1", "GET", "/policy/queries/sv-exclusions/v1"], 
            ["entities.processes", "GET", "/processes/entities/processes/v1?ids={}"], 
            ["RTR-AggregateSessions", "POST", "/real-time-response/aggregates/sessions/GET/v1"], 
            ["BatchActiveResponderCmd", "POST", "/real-time-response/combined/batch-active-responder-command/v1"], 
            ["BatchAdminCmd", "POST", "/real-time-response/combined/batch-admin-command/v1"], 
            ["BatchCmd", "POST", "/real-time-response/combined/batch-command/v1"], 
            ["BatchGetCmdStatus", "GET", "/real-time-response/combined/batch-get-command/v1"], 
            ["BatchGetCmd", "POST", "/real-time-response/combined/batch-get-command/v1"], 
            ["BatchInitSessions", "POST", "/real-time-response/combined/batch-init-session/v1"], 
            ["BatchRefreshSessions", "POST", "/real-time-response/combined/batch-refresh-session/v1"], 
            ["RTR-CheckActiveResponderCommandStatus", "GET", "/real-time-response/entities/active-responder-command/v1"], 
            ["RTR-ExecuteActiveResponderCommand", "POST", "/real-time-response/entities/active-responder-command/v1"], 
            ["RTR-CheckAdminCommandStatus", "GET", "/real-time-response/entities/admin-command/v1"], 
            ["RTR-ExecuteAdminCommand", "POST", "/real-time-response/entities/admin-command/v1"], 
            ["RTR-CheckCommandStatus", "GET", "/real-time-response/entities/command/v1"], 
            ["RTR-ExecuteCommand", "POST", "/real-time-response/entities/command/v1"], 
            ["RTR-GetExtractedFileContents", "GET", "/real-time-response/entities/extracted-file-contents/v1"], 
            ["RTR-ListFiles", "GET", "/real-time-response/entities/file/v1"], 
            ["RTR-DeleteFile", "DELETE", "/real-time-response/entities/file/v1?ids={}"], 
            ["RTR-GetPut-Files", "GET", "/real-time-response/entities/put-files/v1?ids={}"], 
            ["RTR-CreatePut-Files", "POST", "/real-time-response/entities/put-files/v1"], 
            ["RTR-DeletePut-Files", "DELETE", "/real-time-response/entities/put-files/v1?ids={}"], 
            ["RTR-ListQueuedSessions", "POST", "/real-time-response/entities/queued-sessions/GET/v1"], 
            ["RTR-DeleteQueuedSession", "DELETE", "/real-time-response/entities/queued-sessions/command/v1"], 
            ["RTR-PulseSession", "POST", "/real-time-response/entities/refresh-session/v1"], 
            ["RTR-GetScripts", "GET", "/real-time-response/entities/scripts/v1?ids={}"], 
            ["RTR-CreateScripts", "POST", "/real-time-response/entities/scripts/v1"], 
            ["RTR-UpdateScripts", "PATCH", "/real-time-response/entities/scripts/v1"], 
            ["RTR-DeleteScripts", "DELETE", "/real-time-response/entities/scripts/v1?ids={}"], 
            ["RTR-ListSessions", "POST", "/real-time-response/entities/sessions/GET/v1"], 
            ["RTR-InitSession", "POST", "/real-time-response/entities/sessions/v1"], 
            ["RTR-DeleteSession", "DELETE", "/real-time-response/entities/sessions/v1"], 
            ["RTR-ListPut-Files", "GET", "/real-time-response/queries/put-files/v1"], 
            ["RTR-ListScripts", "GET", "/real-time-response/queries/scripts/v1"], 
            ["RTR-ListAllSessions", "GET", "/real-time-response/queries/sessions/v1"], 
            ["GetSampleV2", "GET", "/samples/entities/samples/v2?ids={}"], 
            ["UploadSampleV2", "POST", "/samples/entities/samples/v2"], 
            ["DeleteSampleV2", "DELETE", "/samples/entities/samples/v2?ids={}"], 
            ["GetSampleV3", "GET", "/samples/entities/samples/v3?ids={}"], 
            ["UploadSampleV3", "POST", "/samples/entities/samples/v3"], 
            ["DeleteSampleV3", "DELETE", "/samples/entities/samples/v3?ids={}"], 
            ["QuerySampleV1", "POST", "/samples/queries/samples/GET/v1"], 
            ["GetScansAggregates", "POST", "/scanner/aggregates/scans/GET/v1"], 
            ["GetScans", "GET", "/scanner/entities/scans/v1?ids={}"], 
            ["ScanSamples", "POST", "/scanner/entities/scans/v1"], 
            ["QuerySubmissionsMixin0", "GET", "/scanner/queries/scans/v1"], 
            ["GetCombinedSensorInstallersByQuery", "GET", "/sensors/combined/installers/v1"], 
            ["refreshActiveStreamSession", "POST", "/sensors/entities/datafeed-actions/v1/{}"], 
            ["listAvailableStreamsOAuth2", "GET", "/sensors/entities/datafeed/v2"], 
            ["DownloadSensorInstallerById", "GET", "/sensors/entities/download-installer/v1"], 
            ["GetSensorInstallersEntities", "GET", "/sensors/entities/installers/v1?ids={}"], 
            ["GetSensorInstallersCCIDByQuery", "GET", "/sensors/queries/installers/ccid/v1"], 
            ["GetSensorInstallersByQuery", "GET", "/sensors/queries/installers/v1"], 
            ["GetCSPMPolicy", "GET", "/settings/entities/policy-details/v1?ids={}"], 
            ["GetCSPMPolicySettings", "GET", "/settings/entities/policy/v1"], 
            ["UpdateCSPMPolicySettings", "PATCH", "/settings/entities/policy/v1"], 
            ["GetCSPMScanSchedule", "GET", "/settings/scan-schedule/v1"], 
            ["UpdateCSPMScanSchedule", "POST", "/settings/scan-schedule/v1"], 
            ["getVulnerabilities", "GET", "/spotlight/entities/vulnerabilities/v2?ids={}"], 
            ["queryVulnerabilities", "GET", "/spotlight/queries/vulnerabilities/v1"], 
            ["GetRoles", "GET", "/user-roles/entities/user-roles/v1?ids={}"], 
            ["GrantUserRoleIds", "POST", "/user-roles/entities/user-roles/v1"], 
            ["RevokeUserRoleIds", "DELETE", "/user-roles/entities/user-roles/v1?ids={}"], 
            ["GetAvailableRoleIds", "GET", "/user-roles/queries/user-role-ids-by-cid/v1"], 
            ["GetUserRoleIds", "GET", "/user-roles/queries/user-role-ids-by-user-uuid/v1"], 
            ["RetrieveUser", "GET", "/users/entities/users/v1?ids={}"], 
            ["CreateUser", "POST", "/users/entities/users/v1"], 
            ["UpdateUser", "PATCH", "/users/entities/users/v1"], 
            ["DeleteUser", "DELETE", "/users/entities/users/v1"], 
            ["RetrieveEmailsByCID", "GET", "/users/queries/emails-by-cid/v1"], 
            ["RetrieveUserUUIDsByCID", "GET", "/users/queries/user-uuids-by-cid/v1"], 
            ["RetrieveUserUUID", "GET", "/users/queries/user-uuids-by-email/v1"]
        ]
        
    class Result:
        """ Subclass to handle parsing of result client output. """
        def __init__(self):
            """ Instantiates the subclass and initializes the result object. """
            self.result_obj = {}

        def __call__(self, status_code, headers, body):
            """ Formats values into a properly formatted result object. """
            self.result_obj['status_code'] = status_code
            self.result_obj['headers'] = dict(headers)
            self.result_obj['body'] = body
            
            return self.result_obj

    def authenticate(self):
        """ Generates an authorization token. """
        FULL_URL = self.base_url+'/oauth2/token'
        DATA = {}
        if self.valid_cred_format():
            DATA = {
                'client_id': self.creds['client_id'],
                'client_secret': self.creds['client_secret']
            }
        try:
            response = requests.request("POST", FULL_URL, data=DATA, headers={}, verify=False)
            result = self.Result()(status_code=response.status_code,headers={},body=response.json())["body"]
            self.token = result["access_token"]
            self.token_expiration = result["expires_in"]
            self.token_time = time.time()
            self.authenticated = True
        except Exception:
            self.authenticated = False
        
        return self.authenticated

    def deauthenticate(self):
        """ Revokes the specified authorization token. """
        FULL_URL = self.base_url+'/oauth2/revoke'
        HEADERS = { 'Authorization': 'basic {}'.format(self.token) }
        DATA = { 'token': '{}'.format(self.token) }
        revoked = False
        try:
            requests.request("POST", FULL_URL, data=DATA, headers=HEADERS, verify=False)
            self.authenticated = False
            self.token = False
            revoked = True
        except Exception:
            revoked = False
            
        return revoked

    def command(self, action="", parameters={}, body={}, data={}, ids=False, partition=False, override=False, files=[], content_type=False):
        """ Checks token expiration, renewing when necessary, then performs the request. """
        if self.token_expired():
            self.authenticate()
        if override:
            CMD = [["Manual"] + override.split(",")]
        else:
            CMD = [a for a in self.commands if a[0] == action]
        if CMD:
            FULL_URL = self.base_url+"{}".format(CMD[0][2])
            if ids:
                ID_LIST = str(ids).replace(",","&ids=")
                FULL_URL = FULL_URL.format(ID_LIST)
            if partition:
                FULL_URL = FULL_URL.format(str(partition))
            HEADERS = self.headers()
            if content_type:
                HEADERS["Content-Type"] = str(content_type)
            DATA = data
            BODY = body
            PARAMS = parameters
            FILES = files
            if self.authenticated:
                try:
                    response = requests.request(CMD[0][1].upper(), FULL_URL, json=BODY, data=DATA, params=PARAMS, headers=HEADERS, files=FILES, verify=False)
                    returned = self.Result()(status_code=response.status_code, headers=response.headers, body=response.json())
                except Exception as e:
                    returned = self.Result()(status_code=500, headers={}, body=str(e))
            else:
                returned = self.Result()(status_code=500, headers={}, body={"errors":[{"message":"Failed to issue token."}],"resources":""})
        else:
            returned = self.Result()(status_code=500, headers={}, body={"errors":[{"message":"Invalid API service method."}],"resources":""})

        return returned
