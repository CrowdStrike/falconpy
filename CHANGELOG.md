# Version 1.4.6
## Added features and functionality
+ Added: Added _ExecuteCommandProxy_ operation to the __API Integrations__ service collection.
    - `_endpoint/_api_integrations.py`
    - `_payload/_api_integrations.py`
    - `api_integrations.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_api_integrations.py`

+ Added: Added new __ASPM__ service collection with 23 operations.
    - _UpsertBusinessApplications_
    - _GetExecutorNodes_
    - _UpdateExecutorNode_
    - _CreateExecutorNode_
    - _DeleteExecutorNode_
    - _GetIntegrationTasks_
    - _CreateIntegrationTask_
    - _UpdateIntegrationTask_
    - _DeleteIntegrationTask_
    - _RunIntegrationTask_
    - _GetIntegrationTypes_
    - _GetIntegrations_
    - _CreateIntegration_
    - _UpdateIntegration_
    - _DeleteIntegration_
    - _ExecuteQuery_
    - _ServiceNowGetDeployments_
    - _ServiceNowGetServices_
    - _GetServicesCount_
    - _GetServiceViolationTypes_
    - _GetTags_
    - _UpsertTags_
    - _DeleteTags_
    - `_endpoint/__init__.py`
    - `_endpoint/_aspm.py`
    - `_payload/__init__.py`
    - `_payload/_aspm.py`
    - `_util/_functions.py`
    - `_util/_uber.py`
    - `__init__.py`
    - `aspm.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_aspm.py`

+ Added: Added 1 new operation (_GetCredentialsIAC_) to the __Cloud Snapshots__ service collection.
    - `_endpoint/_cloud_snapshots.py`
    - `cloud_snapshots.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_cloud_snapshots.py`

+ Added: Added new operations, parameters and parameter options to the __Container Images__ service collection.
    - Added new _CombinedBaseImages_ operation.
    - Added new _CreateBaseImageEntities_ operation.
    - Added new _DeleteBaseImages_ operation.
    - Added `include_base_image_vuln` as a filter option to the _AggregateImageCount_ operation.
    - Added `source` as a sort option to the _GetCombinedImages_ operation.
    - Added `include_base_image_vuln` as a filter option to the _ReadCombinedImagesExport_ operation.
    - Added `source` as a sort option to the _ReadCombinedImagesExport_ operation.
    - Added `include_base_image_vuln` parameter to the _CombinedImageIssuesSummary_ operation.
    - Added `include_base_image_vuln` parameter to the _CombinedImageVulnerabilitySummary_ operation.
    - `_endpoint/_container_images.py`
    - `_payload/__init__.py`
    - `_payload/_container.py`
    - `container_images.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_container_images.py`

+ Added: Added parameters to multiple operations within the __CSPM Registration__ service collection.
    - Added `template` parameter to the _GetCSPMAwsConsoleSetupURLs_ operation.
    - Added `account_type`, `dspm_enabled`, `dspm_regions`, and `dspm_role` parameters to the _GetCSPMAwsAccountScriptsAttachment_ operation.
    - `_endpoint/_cspm_registration.py`
    - `cspm_registration.py`

+ Added: Added six new operations to the __Custom Storage__ service collection.
    - _ListObjectsByVersion_
    - _SearchObjectsByVersion_
    - _GetVersionedObject_
    - _PutObjectByVersion_
    - _DeleteVersionedObject_
    - _GetVersionedObjectMetadata_
    - `_endpoint/_custom_storage.py`
    - `_util/_functions.py`
    - `_util/_uber.py`
    - `custom_storage.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_custom_storage.py`

+ Added: Added `dspm_enabled`, `dspm_regions`, and `dspm_role` to the _GetD4CAWSAccountScriptsAttachment_ operation within the __D4C Registration__ service collection.
    - `_endpoint/_d4c_registration.py`
    - `d4c_registration.py`

+ Updated: Added new filter options to all operations within the __Compliance Assessment__ service collection.
    - `_endpoint/__init__.py`
    - `_endpoint/_compliance_assessments.py`
    - `compliance_assessments.py`

+ Added: Added `include_base_image_vuln` as an allowed filter option to multiple operations within the __Container Vulnerabilities__ service collection.
    - `_endpoint/_container_vulnerabilities.py`
    - `container_vulnerabilities.py`

+ Added: Added new __DataScanner__ service collection with 4 new operations.
    - _get_image_registry_credentials_
    - _get_data_scanner_tasks_
    - _update_data_scanner_tasks_
    - _handle_
    - `_endpoint/__init__.py`
    - `_endpoint/_datascanner.py`
    - `_endpoint/deprecated/__init__.py`
    - `_endpoint/deprecated/_datascanner.py`
    - `__init__.py`
    - `datascanner.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_datascanner.py`

+ Added: Added new __DeliverySettings__ service collection with 2 new operations.
    - _GetDeliverySettings_
    - _PostDeliverySettings_
    - `_endpoint/__init__.py`
    - `_endpoint/_delivery_settings.py`
    - `_payload/__init__.py`
    - `_payload/_delivery_settings.py`
    - `__init__.py`
    - `delivery_settings.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_delivery_settings.py`

+ Added: Added _combined_applications_ and _combined_hosts_ operations to the __Discover__ service collection.
    - `_endpoint/_discover.py`
    - `_endpoint/deprecated/_discover.py`
    - `discover.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_discover.py`

+ Added: Added new _ReadDriftIndicatorEntities_ operation to the __Drift Indicators__ service collection.
    - `_endpoint/_drift_indicators.py`
    - `drift_indicators.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_drift_indicators.py`

+ Added: Added new __Downloads__ service collection with 2 new operations.
    - _DownloadFile_
    - _EnumerateFile_
    - `_endpoint/__init__.py`
    - `_endpoint/_downloads.py`
    - `__init__.py`
    - `downloads.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_downloads.py`

+ Added: Added new _delete_external_assets_ operation to the __Exposure Management__ service collection.
    - `_endpoint/_exposure_management.py`
    - `_endpoint/deprecated/_exposure_management.py`
    - `exposure_management.py`

+ Added: Added `aid` parameter and two new values for `environment_id` to the _Submit_ operation within the __Falcon Intelligence Sandbox__ service collection.
    - `_endpoint/_falconx_sandbox.py`
    - `falconx_sandbox.py`

+ Added: Added `data_content` parameter to _IngestDataAsyncV1_ and _IngestData_ operations and added `job_status_only` parameter to the _GetSavedSearchesExecuteV1_ operation within the __Foundry LogScale__ service collection.
    - `_endpoint/_foundry_logscale.py`
    - `foundry_logscale.py`

+ Updated: Increased resultset max return for the _QueryDevicesByFilterScroll_ operation to align with new API maximums. (__Hosts__ Service Class)
    - `_endpoint/_hosts.py`
    - `hosts.py`

+ Added: Added 4 new operations to the __Identity Protection__ service collection. Deprecated `api_preempt_proxy_` prefix from all operation IDs.
    - _get_policy_rules_
    - _post_policy_rules_
    - _delete_policy_rules_
    - _get_policy_rules_query_
    - `_endpoint/_identity_protection.py`
    - `_endpoint/deprecated/_identity_protection.py`
    - `_payload/__init__.py`
    - `_payload/_identity_protection.py`
    - `identity_protection.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_identity_protection.py`

+ Added: Added `cl_regex` and `ifn_regex` parameters to the _queryIOAExclusionsV1_ operation within the __IOA Exclusions__ service collection.
    - `_endpoint/_ioa_exclusions.py`
    - `ioa_exclusions.py`

+ Added: Added 5 new operations to the __Kubernetes Protection__ service collection.
    - _ReadContainerEnrichment_
    - _ReadPodEnrichment_
    - _ReadDeploymentEnrichment_
    - _ReadNamespacesByDateRangeCount_
    - _ReadNamespaceCount_
    - `_endpoint/_kubernetes_protection.py`
    - `kubernetes_protection.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_kubernetes_protection.py`

+ Added: Added new __QuickScan Pro__ service collection with 6 new operations.
    - _UploadFileMixin0Mixin94_
    - _DeleteFile_
    - _GetScanResult_
    - _LaunchScan_
    - _DeleteScanResult_
    - _QueryScanResults_
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_quick_scan_pro.py`
    - `quick_scan_pro.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_quick_scan_pro.py`

+ Added: Added `secondary_sort` (Also accepted: `secondarySort`) parameter to the _QueryRulesV1_ operation within the __Recon__ service collection.
    - `_endpoint/_recon.py`
    - `_recon.py`

+ Added: Added new __Sensor Usage__ service collection with one operation (_GetSensorUsageWeekly_).
    - `_endpoint/__init__.py`
    - `_endpoint/_sensor_usage.py`
    - `__init__.py`
    - `sensor_usage.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_sensor_usage.py`

+ Added: Added `is_descendent_process` parameter to the _updateSensorVisibilityExclusionsV1_ operation within the __Sensor Visibility Exclusions__ service collection.
    - `_payload/_generic.py`
    - `sensor_visibility_exclusions.py`

+ Added: Added additional vertices types as possible values to the `combined_summary_get`, `entities_vertices_get`, and `entities_vertices_getv2` operations within the __ThreatGraph__ service collection.
    - `_endpoint/_threatgraph.py`
    - `_util/_functions.py`
    - `threatgraph.py`

## Issues resolved
+ Fixed: Resolve issue causing headers to not be passed to the _PutObject_ operation within the __Custom Storage__ service collection.
    - `custom_storage.py`

+ Updated: Fixed typing syntax on `update_device_tags` method. (__Hosts__ Service Class) 
    - `hosts.py`

+ Fixed: Added "all" as the default for the `groups` parameter if it is not present when calling the _createMLExclusionsV1_ operation. Closes #1233.
    - `ml_exclusions.py`
    - Thanks go out to @59e5aaf4 for identifying and reporting this issue! 🙇

## Other
+ Added: Added US-GOV-2 region to CrowdStrike container region (Container Base URL) enumerator.
    - `_enum/_container_base_url.py`
    - Thanks go out to @redhatrises for contributing this update! 🙇

+ Deprecated: Moved the _GetQueriesAlertsV1_, _PostEntitiesAlertsV1_, _PatchEntitiesAlertsV2_, and _PostAggregatesAlertsV1_ operations within the __Alerts__ service collection to a deprecated status.
    - `_endpoint/_alerts.py`
    - `alerts.py`

+ Updated: Cosmetic updates to multiple operation descriptions within the __Custom IOA__ service collection.
    - `_endpoint/_custom_ioa.py`
    - `_endpoint/deprecated/_custom_ioa.py`

+ Updated: Cosmetic updates to multiple operation descriptions and enumerators within the __Host Migration__ service collection.
    - `_endpoint/_host_migration.py`

+ Updated: Enumerator updated for the _QueryCasesIdsByFilter_ operation within the __Message Center__ service collection.
    - `_endpoint/_message_center.py`

+ Updated: Updated descriptions for _GetNotificationsDetailedTranslatedV1_ and _GetNotificationsDetailedV1_ operations within the __Recon__ service collection.
    - `_endpoint/_recon.py`
    - `_recon.py`

---

# Version 1.4.5
## Added features and functionality
+ Added: Added new __Host Migration__ service collection with 10 new operations.
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_host_migration.py`
    - `host_migration.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_host_migration.py`

+ Added: Added new __Certificate Based Exclusions__ service collection with six new operations.
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_certificate_based_exclusions.py`
    - `_endpoint/deprecated/_certificate_based_exclusions.py`
    - `_payload/__init__.py`
    - `_payload/_certificate_based_exclusions.py`
    - `certificate_based_exclusions.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_certificate_based_exclusions.py`

+ Added: Added new __Compliance Assessments__ service collection with 11 new operations.
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_compliance_assessments.py`
    - `compliance_assessments.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_compliance_assessments.py`

## Issues resolved
+ Fixed: Resolved comparison issue with version check helper method.
    - `_version.py`

## Other
+ Added: USGOV2 cloud region added to Base URL enumerator.
    - `_enum/_base_url.py`

+ Added: Automatic base URL detection from context objects when available.
    - `_auth_object/_falcon_interface.py`

+ Pinned: `setuptools` package pinned to version __70.3.0__ to avoid failures with new iterations of setuptools in Azure environments.
    - `requirements.txt`
    - `requirements-dev.txt`
    - `setup.py`
    - `dev-setup.py`
    - Thanks go out to @gansel51 for identifying this issue and contributing a fix! 🙇

+ Pinned: `zipp` package pinned to version __3.19.1__ to avoid a potential vulnerability.
    - `requirements-dev.txt`

---

# Version 1.4.4
## Added features and functionality
+ Added: Added new __API Integrations__ service collection with two new operations, __GetCombinedPluginConfigs__ and __ExecuteCommand__.
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_api_integrations.py`
    - `_payload/__init__.py`
    - `_payload/_api_integrations.py`
    - `api_integrations.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_api_integrations.py`
    - `tests/test_uber.py`

+ Added: Added new allowed parameters for the _GetCSPMAwsAccountScriptsAttachment_ operation within the __CSPM Registration__ service collection.
    - `_endpoint/_cspm_registration.py`
    - `cspm_registration.py`

+ Added: Added one new operation (_update_rules_v2_) to the __Custom IOA__ service collection.
    - `_endpoint/_custom_ioa.py`
    - `_endpoint/deprecated/_custom_ioa.py`
    - `custom_ioa.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_custom_ioa.py`

+ Added: Added new allowed parameters for the _GetD4CAWSAccountScriptsAttachment_ operation within the __D4C Registration__ service collection.
    - `_endpoint/_d4c_registration.py`
    - `d4c_registration.py`

+ Added: Added new __Exposure Management__ service collection with 6 new operations.
    - _aggregate_external_assets_
    - _blob_download_external_assets_
    - _blob_preview_external_assets_
    - _get_external_assets_
    - _patch_external_assets_
    - _query_external_assets_
    - `_endpoint/__init__.py`
    - `_endpoint/_exposure_management.py`
    - `_endpoint/deprecated/__init__.py`
    - `_endpoint/deprecated/_exposure_management.py`
    - `_payload/__init__.py`
    - `_payload/_exposure_management.py`
    - `__init__.py`
    - `exposure_management.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_exposure_management.py`

+ Added: Added five new operations to the __FileVantage__ service collection.
    - _getActionsMixin0_
    - _startActions_
    - _getContents_
    - _signalChangesExternal_
    - _queryActionsMixin0_
    - `_constant/__init__.py`
    - `_endpoint/_filevantage.py`
    - `_payload/__init__.py`
    - `_payload/_filevantage.py`
    - `filevantage.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_filevantage.py`

+ Added: Added `cql-master`, `cql-update`, and `cql-changelog` as allowed options for the `type` keyword within the _GetLatestIntelRuleFile_ and _QueryIntelRuleIds_ operations (__Intel__ service collection).
    - `_endpoint/_intel.py`
    - `intel.py`

+ Added: Added one new operation (_RequestDeviceEnrollmentV4_) to the __Mobile Enrollment__ service collection.
    - `_endpoint/_mobile_enrollment.py`
    - `_payload/__init__.py`
    - `_payload/_mobile_enrollment.py`
    - `mobile_enrollment.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_mobile_enrollment.py`

+ Added: Added new __ThreatGraph__ service collection with 5 new operations.
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_threatgraph.py`
    - `_util/_functions.py`
    - `_util/uber.py`
    - `threatgraph.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_threatgraph.py`

+ Added: Added two new operations (_WorkflowActivitiesCombined_ and _WorkflowTriggersCombined_) to the __Workflows__ service collection.
    - `_endpoint/_workflows.py`
    - `workflows.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_workflows.py`

## Issues resolved
+ Fixed: Resolved parameter abstraction issue when leveraging form data payloads with certain API operations. Closes #1160.
    - `_util/__init__.py`
    - `_util/_functions.py`
    - `falconx_sandbox.py`
    - `foundry_logscale.py`
    - `message_center.py`
    - `sample_uploads.py`
    - `workflows.py`
    > Unit testing expanding to complete code coverage.
    - `test_falconx_sandbox.py`
    - `test_message_center.py`
    - `test_sample_uploads.py`
    - `test_workflows.py`
    - Thanks go out to @Destom for reporting this issue! 🙇

+ Fixed: Resolved collision with the `action` keyword argument within the Uber Class and API operations using this string as a key. Closes #1161.
    - `_util/_uber.py`
    - `api_complete/_advanced.py`
    - Thanks go out to @Don-Swanson-Adobe for identifying and reporting this issue! 🙇

+ Fixed: Resolved potential ValueError when providing invalid values to version comparison method.
    - `_version.py`
    > Unit testing expanded to complete code coverage.
    - `test_timeout.py`

## Other
+ Adjusted: Unit testing adjusted to allow 204 responses from _DeletePolicy_ operation testing.
    - `test_image_assessment_policies.py`

+ Expanded: Unit testing expanded to test context authentication when `base_url` is not specified.
    - `test_zero_trust_assessment.py`

+ Updated: Updated enumerator for the `sort` parameter definition for the _QueryCasesIdsByFilter_ operation (__Message Center__ service collection).
    - `_endpoint/_message_center.py`

+ Updated: Updated `filter` parameter description for the _query_iot_hosts_ operation within the __Discover__ service collection.
    - `_endpoint/_discover.py`
    - `_endpoint/deprecated/_discover.py`

+ Removed: Removed one operation from the __Drift Indicators__ service collection.
    - _ReadDriftIndicatorEntities_
    - `_endpoint/_drift_indicators.py`
    - `drift_indicators.py`
    > Unit testing revised to complete code coverage.
    - `tests/test_drift_indicators.py`

+ Updated: Updated `sort` parameter description for the _query_rulesMixin0_ operation within the __Custom IOA__ service collection.
    - `_endpoint/_custom_ioa.py`
    - `_endpoint/deprecated/_custom_ioa.py`

+ Removed: Removed three operations from the __Kubernetes Protection__ service collection.
    - _ReadContainerEnrichment_
    - _ReadDeploymentEnrichment_
    - _ReadPodEnrichment_
    - `_endpoint/_kubernetes_protection.py`
    - `kubernetes_protection.py`
    > Unit testing revised to complete code coverage.
    - `tests/test_kubernetes_protection.py`

+ Updated: Updated `filter` parameter description for the _ReadRunningContainerImages_ operation within the __Kubernetes Protection__ service collection.
    - `_endpoint/_kubernetes_protection.py`

---

# Version 1.4.3
## Added features and functionality
+ Added: Context Authentication (supports Foundry execution environments).
    > FalconInterface object refactored to support new authentication mechanism, track mechanism used, add additional comments, and reduce overall complexity.
    - `_auth_object/_falcon_interface.py`
    > ServiceClass object updated to detect Object Authentication and track mechanism used.
    - `_service_class/_service_class.py`
    > New helper method defined to abstract Direct and Credential authentication creation of the _creds dictionary attribute.
    - `_util/__init__.py`
    - `_util/_auth.py`
    > Class instantiation logging updated to detail authentication mechanism used. Linting and cleanup.
    - `_util/_functions.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_authentications.py`
    - `tests/test_result_object.py`
    - `tests/test_zero_trust_assessment.py`

+ Added: Added _UpdateCSPMGCPServiceAccountsExt_ operation to the __CSPM Registration__ service collection.
    - `_endpoint/_cspm_registration.py`
    - `cspm_registration.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_cspm_registration.py`

+ Added: Added _UpdateD4CGCPServiceAccountsExt_ operation to the __D4C Registration__ service collection.
    - `_endpoint/_d4c_registration.py`
    - `d4c_registration.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_d4c_registration.py`

+ Added: Added `content_files`, `content_registry_values`, `enable_content_capture` and `enable_hash_capture` arguments to the _createRules_ and _updateRules_ operations within the __FileVantage__ service collection.
    - `_endpoint/_filevantage.py`
    - `_payload/_filevantage.py`
    - `filevantage.py`

+ Added: Added `iar_coverage` as an allowed filter argument to the _ReadClustersByKubernetesVersionCount_, _ReadClustersByStatusCount_, _ReadClusterCount_, and _ReadClusterCombined_ operations within the __Kubernetes Protection__ service collection.
    - `_endpoint/_kubernetes_protection.py`
    - `kubernetes_protection.py`


## Issues resolved
+ Fixed: 406 error when uploading Fusion workflows via the _WorkflowDefinitionsImport_ operation. Closes #1145.
    - `workflows.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_workflows.py`
    - `tests/test.yml`
    > Thanks go out to @RoemIko for identifying and reporting this issue! 🙇 

+ Fixed: Added missing `force_default` decorator to the _GetCSPMAwsConsoleSetupURLs_ and _GetCSPMAwsAccountScriptsAttachment_ operations within the __CSPM Registration__ Service Class.
    - `cspm_registration.py`


## Other
+ Updated: Updated `sort` argument description for the _ReadCombinedImagesExport_ operation (__Container Images__ service collection) within the endpoint module.
    - `_endpoint/_container_images.py`

+ Updated: Updated `filter` argument description for the _GetConfigurationDetectionIDsV2_ operation (__CSPM Registration__ service collection) within the endpoint module.
    - `_endpoint/_cspm_registration.py`

+ Updated: Updated enum for the _QueryActivityByCaseID_ operation (__Message Center__ service collection) within the endpoint module.
    - `_endpoint/_message_center.py`

+ Updated: Minor unit testing adjustments to handle updated API responses.
    - `tests/test_container_detections.py`
    - `tests/test_container_packages.py`
    - `tests/test_container_vulnerabilities.py`
    - `tests/test_drift_indicators.py`
    - `tests/test_unidentified_containers.py`

---

# Version 1.4.2
## Added features and functionality
+ Expanded: Environment Authentication functionality has been expanded to allow developers to customize the names of the environment keys used to store API credentials.
    - `_auth_object/_falcon_interface.py`
    - `_auth_object/_uber_interface.py`
    - `oauth2.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_authentications.py`
    ```python
    from falconpy import Hosts
    # We can now define the prefix and the names of the
    # environment values used for API key lookups
    environment_keys = {
        "prefix": "CROWDSTRIKE_",
        "id_name": "API_ID",
        "secret_name": "API_SECRET"
    }
    # These values are provided as a dictionary to the class
    hosts = Hosts(environment=environment_keys)
    # Usage of the class is the same
    results = hosts.query_devices_by_filter_scroll()
    ```

+ Added: `include_hidden` argument added to the _PostAggregatesAlertsV2_, _PatchEntitiesAlertsV3_, _PostEntitiesAlertsV2_ and _GetQueriesAlertsV2_ operations within the __Alerts__ Service Class.
    - `alerts.py`

+ Added: Added 4 new operations to the __Cloud Snapshots__ service collection.
    - _ReadDeploymentsCombined_
    - _ReadDeploymentsEntities_
    - _CreateDeploymentEntity_
    - _GetScanReport_
    - `_endpoint/_cloud_snapshots.py`
    - `_payload/__init__.py`
    - `_payload/_cloud_snapshots.py`
    - `cloud_snapshots.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_cloud_snapshots.py`

+ Added: Added _GetRuntimeDetectionsCombinedV2_ to the __Container Detections__ service collection.
    - `_endpoint/_container_detections.py`
    - `container_detections.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_container_detections.py`

+ Added: Added 3 new operations to the __CSPM Registration__ service collection.
    - _DeleteCSPMAzureManagementGroup_
    - _GetCSPMGCPValidateAccountsExt_
    - _ValidateCSPMGCPServiceAccountExt_
    - `_endpoint/_cspm_registration.py`
    - `_payload/__init__.py`
    - `_payload/_cspm_registration.py`
    - `cspm_registration.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_cspm_registration.py`

+ Added: Added _query_iot_hostsV2_ operation to the __Discover__ service collection.
    - `_endpoint/_discover.py`
    - `_endpoint/deprecated/_discover.py`
    - `discover.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_discover.py`

+ Added: Added _AggregateSupportIssues_ operation to the __Falcon Complete Dashboard__ service collection.
    - `_endpoint/_falcon_complete_dashboard.py`
    - `falcon_complete_dashboard.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_falcon_complete_dashboard.py`

+ Added: Added _IngestDataAsyncV1_ operation to the __Foundry LogScale__ service collection.
    - `_endpoint/_foundry_logscale.py`
    - `foundry_logscale.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_foundry_logscale.py`

+ Added: Added `infer_json_types` and `match_response_schema` arguments to the _CreateSavedSearchesDynamicExecuteV1_, _GetSavedSearchesExecuteV1_ and _CreateSavedSearchesExecuteV1_ operations within the __Foundry LogScale__ service collection.
    - `_endpoint/_foundry_logscale.py`
    - `foundry_logscale.py`

+ Added: Added `infer_json_types` argument to the _GetSavedSearchesJobResultsDownloadV1_ operation within the __Foundry LogScale__ service collection.
    - `_endpoint/_foundry_logscale.py`
    - `foundry_logscale.py`

+ Added: Added 3 new operations to the __Intel__ service collection.
    - _GetMalwareEntities_
    - _QueryMalware_
    - _QueryMitreAttacksForMalware_
    - `_endpoint/_intel.py`
    - `intel.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_intel.py`

+ Added: Added 4 new operations to the __Sensor Download__ service collection.
    - _GetCombinedSensorInstallersByQueryV2_
    - _DownloadSensorInstallerByIdV2_
    - _GetSensorInstallersEntitiesV2_
    - _GetSensorInstallersByQueryV2_
    - `_endpoint/_sensor_download.py`
    - `sensor_download.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_sensor_download.py`

+ Added: Added `sanitize` argument to the _WorkflowDefinitionsExport_ operation within the __Workflows__ service collection.
    - `_endpoint/_workflows.py`
    - `workflows.py`

+ Added: Added 2 new operations to the __Workflows__ service collection.
    - _WorkflowExecuteInternal_
    - _WorkflowMockExecute_
    - `_endpoint/workflows.py`
    - `_payload/__init__.py`
    - `_payload/_workflows.py`
    - `workflows.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_workflows.py`

## Issues resolved
+ Fixed: Resolved parsing issue with formData arguments provided to the _ArchiveUploadV2_ operation within the __SampleUploads__ Service Class. Closes #1122.
    - `sample_uploads.py`

+ Fixed: Resolved conversion issue with query string boolean parameters not being properly converted to lowercase before API submission. Closes #1129.
    - `_util/_functions.py`

## Other
+ Updated: Updated `body` argument description for the _PatchEntitiesAlertsV3_ operation within the endpoint module.
    - `_endpoint/_alerts.py`

+ Updated: Added `highest_cps_current_rating` as an allowed sort parameter to the _ReadCombinedImagesExport_ operation within the __Container Images__ service collection.
    - `_endpoint/_container_images.py`

+ Updated: Added `watch_permissions_key_changes` option to the _createRules_ operation within the __FileVantage__ service collection.
    - `_endpoint/_filevantage.py`

+ Updated: Updated operation and argument descriptions in the deprecated __IOCS__ service collection.
    - `_endpoint/_iocs.py`

+ Updated: Added `prevented` as an allowed filter to the _ReadKubernetesIomByDateRange_, _ReadKubernetesIomCount_, _SearchAndReadKubernetesIomEntities_ and _SearchKubernetesIoms_ operations within the __Kubernetes Protection__ service collection.
    - `_endpoint/_kubernetes_protection.py`

+ Updated: Updated the `body` argument description for the _BatchAdminCmd_ and _RTR_ExecuteAdminCommand_ operations within the __Real Time Response Admin__ service collection.
    - `_endpoint/_real_time_response_admin.py`
    - `_endpoint/deprecated/_real_time_response_admin.py`

+ Updated: Updated the `body` argument description for the _BatchActiveResponderCmd_, _BatchCmd_, _RTR_ExecuteActiveResponderCommand_, and _RTR_ExecuteCommand_ operations within the __Real Time Response__ service collection.
    - `_endpoint/_real_time_response.py`
    - `_endpoint/deprecated/_real_time_response.py`

+ Removed: The _CreateInventory_ operation is removed from the __Cloud Snapshots__ Service Class.
    - `_payload/__init__.py`
    - `_payload/_cloud_snapshots.py`
    - `cloud_snapshots.py`
    > Unit testing updated to reflect current functionality.
    - `tests/test_cloud_snapshots.py`

+ Removed: The _WorkflowDefinitionsCreate_ operation is removed from the __Workflows__ service collection.
    - `_endpoint/_workflows.py`
    - `workflows.py`
    > Unit testing updated to reflect current functionality.
    - `tests/test_workflows.py`

---

# Version 1.4.1
## Added features and functionality
+ Added: `include_hidden` argument added to the _PostAggregatesAlertsV2_, _PostEntitiesAlertsV2_, _PatchEntitiesAlertsV3_ and _GetQueriesAlertsV2_ operations.
    - `_endpoint/_alerts.py`

+ Added: _ReadContainerAlertsCountBySeverity_ operation added to the __Container Alerts__ service collection.
    - `_endpoint/_container_alerts.py`
    - `container_alerts.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_container_alerts.py`

+ Added: `cspm_lite` argument added to the _GetCSPMAwsAccount_ and _GetCSPMAzureAccount_ operations within the __CSPM Registration__ service collection.
    - `_endpoint/_cspm_registration.py`
    - `cspm_registration.py`

+ Added: `azure_management_group` argument added to the _GetCSPMAzureUserScriptsAttachment_ operation within the __CSPM Registration__ service collection.
    - `_endpoint/_cspm_registration.py`
    - `cspm_registration.py`

+ Added: 9 new operations added to the __CSPM Registration__ service collection.
    * _GetCSPMAzureManagementGroup_
    * _CreateCSPMAzureManagementGroup_
    * _GetCSPMCGPAccount_
    * _CreateCSPMGCPAccount_
    * _DeleteCSPMGCPAccount_
    * _UpdateCSPMGCPAccount_
    * _ConnectCSPMGCPAccount_
    * _GetCSPMGCPServiceAccountsExt_
    * _GetCSPMGCPUserScriptsAttachment_
    - `_endpoint/_cspm_registration.py`
    - `_payload/_cspm_registration.py`
    - `cspm_registration.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_cspm_registration.py`

+ Added: `azure_management_group` argument added to the _GetDiscoverCloudAzureUserScriptsAttachment_ operation within the __D4C Registration__ service collection.
    - `_endpoint/_d4c_registration.py`
    - `d4c_registration.py`

+ Added: 4 new operations added to the __D4C Registration__ service collection.
    * _DeleteD4CGCPAccount_
    * _ConnectD4CGCPAccount_
    * _GetD4CGCPServiceAccountsExt_
    * _GetD4CGCPUserScriptsAttachment_
    - `_endpoint/_d4c_registration.py`
    - `_payload/_d4c_registration.py`
    - `d4c_registration.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_d4c_registration.py`

+ Added: `execution_cid` argument added to the _WorkflowExecute_ operation within the __Workflows__ service collection.
    - `_endpoint/_workflows.py`
    - `workflows.py`

+ Added: New service collection __Image Assessment Policies__ containing 11 new operations.
    * _ReadPolicies_
    * _CreatePolicies_
    * _UpdatePolicies_
    * _DeletePolicy_
    * _ReadPolicyExclusions_
    * _UpdatePolicyExclusions_
    * _ReadPolicyGroups_
    * _CreatePolicyGroups_
    * _UpdatePolicyGroups_
    * _DeletePolicyGroup_
    * _UpdatePolicyPrecedence_
    - `_endpoint/__init__.py`
    - `_endpoint/_image_assessment_policies.py`
    > 3 new payload handlers are added.
    - `_payload/__init__.py`
    - `_payload/_container.py`
    - `__init__.py`
    - `image_assessment_policies.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_image_assessment_policies.py`

+ Added: 8 new operations added to the __Workflows__ service collection.
    * _WorkflowDefinitionsCombined_
    * _WorkflowExecutionsCombined_
    * _WorkflowDefinitionsExport_
    * _WorkflowDefinitionsImport_
    * _WorkflowDefinitionsUpdate_
    * _WorkflowDefinitionsCreate_
    * _WorkflowGetHumanInputV1_
    * _WorkflowUpdateHumanInputV1_
    - `_endpoint/_workflows.py`
    - `workflows.py`
    > 2 new payload handlers are added.
    - `_payload/__init__.py`
    - `_payload/_workflows.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_workflows.py`

## Issues resolved
+ Fixed: `member_cid` argument is not being passed to the authentication event when leveraging Environment Authentication. Closes #1105.
    - `_auth_object/_falcon_interface.py`

+ Fixed: `rule_ids` is not included in body payloads when the list is empty for the _update_rule_groups_ operation within the __Firewall Management__ Service Class. Closes #1107.
    - `_payload/_firewall.py`

+ Fixed: Added missing actions to _allowed_actions validator within `PerformActionV2` method of the __Hosts__ service collection. Closes #1108.
    - `hosts.py`
    - Thanks go out to @i-shubham01 for identifying and resolving this issue! 🙇

## Other
+ Updated: Enums added to _GetCSPMAwsAccount_ and _GetCSPMAwsConsoleSetupURLs_ operations within the __CSPM Registration__ endpoint module.
    - `_endpoint/_cspm_registration.py`

+ Updated: Several parameter descriptions within the __Custom IOA__ endpoint module updated.
    - `_endpoint/_custom_ioa.py`
    - `_endpoint/deprecated/_custom_ioa.py`

+ Updated: Enum updated within the _GetD4CAwsAccount_ operation of the __D4C Registration__ endpoint module.
    - `_endpoint/_d4c_registration.py`

+ Updated: Parameter description for the _Submit_ operation within the __Falcon Intelligence Sandbox__ endpoint module updated.
    - `_endpoint/_falconx_sandbox.py`

+ Updated: Multiple parameter descriptions within the __Kubernetes Protection__ endpoint module updated.
    - `_endpoint/_kubernetes_protection_.py`

+ Updated: Enum updated within the _QueryActivityByCaseID_ operation of the __Message Center__ endpoint module.
    - `_endpoint/_message_center.py`

---

# Version 1.4.0
## Other
+ Dropped: Python 3.6 support.
    > Unit testing adjusted to reflect supported versions.
    - `README.md`
    - `SECURITY.md`
    - `setup.py`

+ Refactored: Simple private child objects within the [__APIRequest__](https://www.falconpy.io/Usage/Extensibility.html#apirequest) object updated to leverage data classes.
    - `_api_request/_request_connection.py`
    - `_api_request/_request_payloads.py`
    - `_api_request/_request_validator.py`

---

# Version 1.3.5
## Added features and functionality
+ Added: 4 new operations added to the __*Alerts*__ service collection.
    - *PostAggregateAlertsV2*
    - *PostEntitiesAlertsV2*
    - *PatchEntitiesAlertsV3*
    - *GetQueriesAlertsV2*
    - `_endpoint/_alerts.py`
    - `alerts.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_alerts.py`
+ Added: `source_event_url` argument added to the _WorkflowExecute_ operation definition within the endpoint module.
    - `_endpoint/_workflows.py`
+ Added: New Configuration Assessment service collection providing 2 new operations.
    - *getCombinedAssessmentsQuery*
    - *getRuleDetails*
    - `_endpoint/__init__.py`
    - `_endpoint/_configuration_assessment.py`
    - `__init__.py`
    - `configuration_assessment.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_configuration_assessment.py`
+ Added: New Configuration Assessment Evaluation Logic service collection providing 1 new operation.
    - *getEvaluationLogicMixin0*
    - `_endpoint/__init__.py`
    - `_endpoint/_configuration_assessment_evaluation_logic.py`
    - `__init__.py`
    - `configuration_assessment_evaluation_logic.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_configuration_assessment_evaluation_logic.py`
+ Added: New Container Alerts service collection providing 2 new operations.
    - *ReadContainerAlertsCount*
    - *SearchAndReadContainerAlerts*
    - `_endpoint/__init__.py`
    - `_endpoint/_container_alerts.py`
    - `__init__.py`
    - `container_alerts.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_container_alerts.py`
+ Added: New Container Detections service collection providing 6 new operations.
    - *ReadDetectionsCountBySeverity*
    - *ReadDetectionsCountByType*
    - *ReadDetectionsCount*
    - *ReadCombinedDetections*
    - *ReadDetections*
    - *SearchDetections*
    - `_endpoint/__init__.py`
    - `_endpoint/_container_detections.py`
    - `__init__.py`
    - `container_detections.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_container_detections.py`
+ Added: New Container Images service collection providing 10 new operations.
    - *AggregateImageAssessmentHistory*
    - *AggregateImageCountByBaseOS*
    - *AggregateImageCountByState*
    - *AggregateImageCount*
    - *GetCombinedImages*
    - *CombinedImageByVulnerabilityCount*
    - *CombinedImageDetail*
    - *ReadCombinedImagesExport*
    - *CombinedImageIssuesSummary*
    - *CombinedImageVulnerabilitySummary*
    - `_endpoint/__init__.py`
    - `_endpoint/_container_images.py`
    - `__init__.py`
    - `container_images.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_container_images.py`
+ Added: New Container Packages service collection providing 5 new operations.
    - *ReadPackagesCountByZeroDay*
    - *ReadPackagesByFixableVulnCount*
    - *ReadPackagesByVulnCount*
    - *ReadPackagesCombinedExport*
    - *ReadPackagesCombined*
    - `_endpoint/__init__.py`
    - `_endpoint/_container_packages.py`
    - `__init__.py`
    - `container_packages.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_container_packages.py`
+ Added: New Container Vulnerabilities service collection providing 10 new operations.
    - *ReadCombinedVulnerabilities*
    - *ReadCombinedVulnerabilitiesInfo*
    - *ReadCombinedVulnerabilitiesDetails*
    - *ReadVulnerabilitiesPublicationDate*
    - *ReadVulnerabilitiesByImageCount*
    - *ReadVulnerabilityCount*
    - *ReadVulnerabilityCountBySeverity*
    - *ReadVulnerabilityCountByCPSRating*
    - *ReadVulnerabilityCountByCVSSScore*
    - *ReadVulnerabilityCountByActivelyExploited*
    - `_endpoint/__init__.py`
    - `_endpoint/_container_vulnerabilities.py`
    - `__init__.py`
    - `container_vulnerabilities.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_container_vulnerabilities.py`
+ Added: `next_token` argument added to the _GetConfigurationDetectionIDsV2_ operation within the __*CSPM Registration*__ service collection.
    - `_endpoint/_cspm_registration.py`
    - `cspm_registration.py`
+ Added: New Drift Indicators service collection providing 5 new operations.
    - *GetDriftIndicatorsValuesByDate*
    - *ReadDriftIndicatorsCount*
    - *SearchAndReadDriftIndicatorEntities*
    - *ReadDriftIndicatorEntities*
    - *SearchDriftIndicators*
    - `_endpoint/__init__.py`
    - `_endpoint/_drift_indicators.py`
    - `__init__.py`
    - `drift_indicators.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_drift_indicators.py`
+ Added: 3 new operations added to the __*Falcon Complete Dashboard*__ service collection.
    - *AggregatePreventionPolicy*
    - *AggregateSensorUpdatePolicy*
    - *AggregateTotalDeviceCounts*
    - `_endpoint/_falcon_complete_dashboard.py`
    - `falcon_complete_dashboard.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_falcon_complete_dashboard.py`
+ Added: New arguments added to 5 operations within the __*Foundry LogScale*__ service collection. 2 arguments are removed from 1 operation.
    - `check_test_data` is added to _ListReposV1_.
    - `app_id` is added to _CreateSavedSearchesDynamicExecuteV1_.
    - `app_id` is added to _GetSavedSearchesExecuteV1_.
    - `app_id` is added to _CreateSavedSearchesExecuteV1_.
    - `check_test_data` is added to _ListViewV1_.
    - The duplicative query string parameter arguments `mode` and `version` have been removed from _CreateSavedSearchesExecuteV1_.
    - `_endpoint/_foundry_logscale.py`
    - `foundry_logscale.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_foundry_logscale.py`
+ Added: 1 new operation added to the __*Hosts*__ service collection.
    - *QueryDeviceLoginHistoryV2*
    - `_endpoint/_hosts.py`
    - `hosts.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_hosts.py`
+ Added: 3 new operations added to the __*IOC*__ service collection. These operations replace legacy operations from the deprecated __*IOCS*__ service collection.
    - *indicator_get_device_count_v1* replaces _DevicesCount_.
    - *indicator_get_devices_ran_on_v1* replaces _DevicesRanOn_.
    - *indicator_get_processes_ran_on_v1* replaces _ProcessRanOn_.
    - `_endpoint/_ioc.py`
    - `_endpoint/deprecated/_ioc.py`
    - `ioc.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_ioc.py`
+ Added: 41 new operations added to the __*Kubernetes Protection*__ service collection.
    - *ReadClustersByDateRangeCount*
    - *ReadClustersByKubernetesVersionCount*
    - *ReadClustersByStatusCount*
    - *ReadClusterCount*
    - *ReadContainersByDateRangeCount*
    - *ReadContainerCountByRegistry*
    - *FindContainersCountAffectedByZeroDayVulnerabilities*
    - *ReadVulnerableContainerImageCount*
    - *ReadContainerCount*
    - *FindContainersByContainerRunTimeVersion*
    - *GroupContainersByManaged*
    - *ReadContainerImageDetectionsCountByDate*
    - *ReadContainerImagesByState*
    - *ReadContainersSensorCoverage*
    - *ReadContainerVulnerabilitiesBySeverityCount*
    - *ReadDeploymentsByDateRangeCount*
    - *ReadDeploymentCount*
    - *ReadClusterEnrichment*
    - *ReadContainerEnrichment*
    - *ReadDeploymentEnrichment*
    - *ReadNodeEnrichment*
    - *ReadPodEnrichment*
    - *ReadDistinctContainerImageCount*
    - *ReadContainerImagesByMostUsed*
    - *ReadKubernetesIomByDateRange*
    - *ReadKubernetesIomCount*
    - *ReadNodesByCloudCount*
    - *ReadNodesByContainerEngineVersionCount*
    - *ReadNodesByDateRangeCount*
    - *ReadNodeCount*
    - *ReadPodsByDateRangeCount*
    - *ReadPodCount*
    - *ReadClusterCombined*
    - *ReadRunningContainerImages*
    - *ReadContainerCombined*
    - *ReadDeploymentCombined*
    - *SearchAndReadKubernetesIomEntities*
    - *ReadNodeCombined*
    - *ReadPodCombined*
    - *ReadKubernetesIomEntities*
    - *SearchKubernetesIoms*
    - `_endpoint/_kubernetes_protection.py`
    - `kubernetes_protection.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_kubernetes_protection.py`
+ Added: 1 new operation added to the __*ODS*__ service collection.
    - *get_scans_by_scan_ids_v2*
    > *get_scans_by_scan_ids_v1* has been deprecated. The PEP8 method `get_scans` has been redirected to the new operation. Developers wanting to leverage the legacy operation should call `get_scans_v1` or `get_scans_by_scan_ids_v1`.
    - `_endpoint/_ods.py`
    - `_endpoint/deprecated/_ods.py`
    - `ods.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_ods.py`
+ Added: 2 new operations added to the __*Real Time Response Admin*__ service collection.
    - *RTR_GetFalconScripts*
    - *RTR_ListFalconScripts*
    - `_endpoint/_real_time_response_admin.py`
    - `_endpoint/deprecated/_real_time_response_admin.py`
    - `real_time_response_admin.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_real_time_response_admin.py`
+ Added: New Unidentified Containers service collection providing 3 new operations.
    - *ReadUnidentifiedContainersByDateRangeCount*
    - *ReadUnidentifiedContainersCount*
    - *SearchAndReadUnidentifiedContainers*
    - `_endpoint/__init__.py`
    - `_endpoint/_unidentified_containers.py`
    - `__init__.py`
    - `unidentified_containers.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_unidentified_containers.py`

## Issues resolved
+ Fixed: `batch_id` and `batch_get_cmd_req_id` not available on pythonic Result object.
    - `_result/_result.py`
+ Fixed: Pythonic responses not properly populating Result object resources attribute when a dictionary is returned for the resources branch.
    - `_result/_result.py`
+ Fixed: `trace_id` property is not available on Result objects that do not contain a Meta attribute.
    - `_result/_headers.py`
    - `_result/_result.py`
+ Fixed: Changes the datatype for the `ids` argument within the _GetCSPMPolicy_ operation from __`string`__ to __`integer`__.
    - `_endpoint/_cspm_registration.py`

## Other
+ Fixed: A typo that incorrectly listed the default value for the `limit` keyword was resolved in the QueryDetects operation docstring. Closes #1089.
    - `detects.py`
+ Refactored: Reduced complexity within the Result object constructor method by abstracting construction logic to a new method.
    - `_result/_result.py`
+ Regenerated: Updated endpoint module to align to new library automation, resulting in cosmetic changes to description fields.
    - `_endpoint/*`
+ Renamed: _RetrieveUser_ operation has been renamed to _retrieveUser_ within the __*User Management*__ service collection.
    - `_endpoint/_user_management.py`
+ Deprecated: Adds additional deprecated operation IDs to the __*Firewall Management*__ service collection.
    - `_endpoint/_firewall_management.py`
+ Fixed: Resolves a constant naming typo within the endpoint module for the __*Cloud Snapshots*__ service collection.
    - `_endpoint/__init__.py`
    - `_endpoint/_cloud_snapshots.py`
    - `cloud_snapshots.py`
+ Fixed: Endpoint definition mismatch in _UploadSampleV3_ operation within the __*Sample Uploads*__ service collection.
    - `_endpoint/_sample_uploads.py`
+ Fixed: Endpoint definition mismatch in _UploadSampleV2_ operation within the __*Falcon Intelligence Sandbox*__ service collection.
    - `_endpoint/_falconx_sandbox.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_falconx_sandbox.py`

---

# Version 1.3.4
## Added features and functionality
+ Added: Use a Service Class or the Uber Class as a context manager.
    > Leveraging this functionality will automatically revoke your bearer token on context manager exit.
    ```python
    from falconpy import Hosts
    with Hosts(pythonic=True) as hosts:
        for device in hosts.query_devices().data:
            print(device)
    ```
    - `_auth_object/_uber_interface.py`
    - `_service_class/_service_class.py`
+ Added: `app_id` keyword added to _CreateSavedSearchesIngestV1_ operation.
    - `foundry_logscale.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_foundry_logscale.py`

## Issues resolved
+ Fixed: _update_policy_container_ operation payload handler is missing the `policy_id` key. Closes #1068.
    - `_payload/_firewall.py`
    > Expanded unit testing to complete code coverage.
    - `tests/test_firewall_management.py`
+ Fixed: `after` property is missing from the __Meta__ object. Closes #1069.
    - `_result/_meta.py`
    - `_result/_result.py`
+ Fixed: Payload handler for _tokens_update_ operation is not properly passing the `revoked` key. Closes #1074.
    - `installation_tokens.py`
+ Fixed: API operations generating leveraging the raw attribute are not properly displaying results when leveraging result object expansion. Closes #1076.
    - `_result/_result.py`
+ Fixed: Per-operation pythonic override is not working as expected. Closes #1078.
    - `_util/_functions.py`

# Other
+ Changed: Updated field mapping for Uber Class path variables to a cleaner solution.
    - `_util/_uber.py`
+ Removed: The unsupported actions `add-rule-group` and `remove-rule-group` are removed from the _performFirewallPoliciesAction_ operation. Relates to #1059.
    - `firewall_policies.py`

---

# Version 1.3.3
## Added features and functionality
+ Added: Deprecation warnings for deprecated classes and operations. Closes #1055.
    - `_endpoint/__init__.py`
    - `_endpoint/deprecated/__init__.py`
    - `_endpoint/deprecated/_mapping.py`
    - `_error/__init__.py`
    - `_error/_warnings.py`
    - `_service_class/_service_class.py`
    - `_util/__init__.py`
    - `_util/_functions.py`
+ Added: New Custom Storage service collection.
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_custom_storage.py`
    - `_util/_functions.py`
    - `custom_storage.py`
    > Expanded unit testing to complete code coverage.
    - `tests/test_custom_storage.py`
    > The following new operations are provided by this service collection:
    + _ListObjects_
    + _SearchObjects_
    + _GetObject_
    + _PutObject_
    + _DeleteObject_
    + _GetObjectMetadata_
+ Added: New Workflows service collection.
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_workflows.py`
    - `_endpoint/_workflows.py`
    - `_payload/__init__.py`
    - `_payload/_generic.py`
    - `_payload/_workflows.py`
    - `workflows.py`
    > Expanded unit testing to complete code coverage.
    - `tests/test_workflows.py`
    > The following new operations are provided by this service collection:
    + _WorkflowExecute_
    + _WorkflowExecutionsAction_
    + _WorkflowExecutionResults_
    + _WorkflowSystemsDefinitionsDeProvision_
    + _WorkflowSystemsDefinitionsPromote_
    + _WorkflowSystemsDefinitionsProvision_
+ Added: New Real Time Response Audit service collection.
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_real_time_response_audit.py`
    - `real_time_response_audit.py`
    > Expanded unit testing to complete code coverage.
    - `tests/test_real_time_response_audit.py`
    > The following new operations are provided by this service collection:
    + _RTRAuditSessions_
+ Added: New Foundry LogScale service collection.
    - `__init__.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_foundry_logscale.py`
    - `_payload/__init__.py`
    - `_payload/_foundry.py`
    - `foundry_logscale.py`
    > Expanded unit testing to complete code coverage.
    - `tests/test_foundry_logscale.py`
    > The following new operations are provided by this service collection:
    + _ListReposV1_
    + _ListViewV1_
    + _IngestDataV1_
    + _CreateSavedSearchesDynamicExecuteV1_
    + _GetSavedSearchesExecuteV1_
    + _CreateSavedSearchesExecuteV1_
    + _CreateSavedSearchesIngestV1_
    + _GetSavedSearchesJobResultsDownloadV1_

## Issues resolved
+ Fixed: Error when trying to directly import falconpy module (no package installation). Closes #1056.
    - `_auth_object/_falcon_interface.py`
    - `_util/_functions.py`
    - Thanks go out to @tsullivan06 for identifying and reporting this issue. 🙇
+ Fixed: Legacy Uber Class is not logging Operation ID in debug logs. Closes #1057.
    - `api_complete/_legacy.py`
+ Fixed: Can not use `add-rule-group` and `remove-rule-group` actions with the __`performFirewallPoliciesAction`__ operation. Closes #1059.
    - `firewall_policies.py`
    - Thanks go out to @api-clobberer for identifying and reporting this issue. 🙇

---

# Version 1.3.2
> This release resolves a breaking change introduced in Version 1.3.0. This issue presents itself when developers attempt to call the `authenticated` method directly from the `OAuth2` Service Class. Review issue #1043 for more detail.

## Added features and functionality
+ Added: Expanded the Uber Class into a submodule, and restored the 1.2.16 version of this class as `APIHarness`. This class is now __DEPRECATED__. The 1.3.0 version of this class is now named `APIHarnessV2` (The advanced Uber Class) .
    - `_auth_object/_base_falcon_auth.py`
    - `_auth_object/_falcon_interface.py`
    - `_auth_object/_uber_interface.py`
    - `api_complete/__init__.py`
    - `api_complete/_advanced.py`
    - `api_complete/_legacy.py`
    - `__init__.py`
    > Expanded unit testing to complete code coverage.
    - `tests/test_authorizations.py`
    - `tests/test_falcon_container.py`
    - `tests/test_uber_api_complete.py`
    - `tests/test_uber.py`

## Issues resolved
+ Fixed: Error generated when trying leverage the legacy `authenticated` lambda method handler within the `OAuth2` Service Class. Closes #1043.
    - `_auth_object/_base_falcon_auth.py`
    - `_auth_object/_falcon_interface.py`
    - `_service_class/_service_class.py`
    - `oauth2.py`
    > Expanded unit testing to complete code coverage.
    - `tests/test_service_class.py`
    - Thanks go out to @morcef for identifying and reporting this issue. 🙇
+ Fixed: Type check failure when creating a mock of the `OAuth2` Service Class. Relates to #1043.
    - `_service_class/_base_service_class.py`
    - Thanks go out to @davidt99 for identifying / reporting this issue and providing the fix. 🙇

---

# Version 1.3.1
## Added features and functionality
+ Added: 1 new operation added (`highVolumeQueryChanges`) from the _FileVantage_ service collection.
    - `_endpoint/_filevantage.py`
    - `filevantage.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_filevantage.py`
+ Added: Warn when providing API arguments that are unnecessarily URLEncoded. Closes #850.
    - `_error/__init__.py`
    - `_error/_warnings.py`
    - `_util/_functions.py`
    - `_util/_uber.py`
    - `__init__.py`
    - Thanks go out to @aboese for suggesting this enhancement. 🙇
+ Added: `add_comment` keyword added to the _PerformIncidentAction_ operation within the _**Incidents**_ Service Class. Closes #1003.
    - `_payload/_incidents.py`
    - `incidents.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_incidents.py`
    - Thanks go out to @morcef for suggesting this enhancement. 🙇
+ Added: `add-rule-group` and `remove-rule-group` options added to _performFirewallPoliciesAction_ operation in the __Firewall Policies__ service collection.
    - `_endpoint/_firewall_policies.py`
    - `firewall_policies.py`
+ Added: Sort by `alert_ids` option added to _QueryBehaviors_ operation in the __Incidents_ service collection.
    - `_endpoint/_incidents.py`
+ Added: _AggregateAlerts_ and _QueryAlertIdsByFilter_ operations added to the __Falcon Complete Dashboard__ service collection.
    - `_endpoint/_falcon_complete_dashboard.py`
    - `falcon_complete_dashboard.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_falcon_complete_dashboard.py`
+ Added: _GetCombinedImages_ operation added to the __Falcon Container__ service collection.
    - `_endpoint/_falcon_container.py`
    - `falcon_container.py`
    > Unit testing expanded to complete code coverage.
    - `test_falcon_container.py`
+ Added: `ids` keyword argument added to _GetIntelReportPDF_ and _QueryMitreAttacks_ operations. `if_none_match` and `if_modified_since` keyword arguments added to _GetLatestIntelRuleFile_ operation. __Intel__ service collection.
    - `_endpoint/_intel.py`
    - `intel.py`
    > Unit testing expanded to complete code coverage.
    - `test_intel.py`
+ Added: Override functionality - All service classes are now able to call manually specified operation endpoints via the `override` method. This method mirrors functionality provided by the `override` keyword within the Uber Class.
    - `_service_class.py`
+ Added: 23 new operations added to the __FileVantage__ service collection.
    * updatePolicyHostGroups
    * updatePolicyPrecedence
    * updatePolicyRuleGroups
    * getPolicies
    * createPolicies
    * deletePolicies
    * updatePolicies
    * getScheduledExclusions
    * createScheduledExclusions
    * deleteScheduledExclusions
    * updateScheduledExclusions
    * updateRuleGroupPrecedence
    * getRules
    * createRules
    * deleteRules
    * updateRules
    * getRuleGroups
    * createRuleGroups
    * deleteRuleGroups
    * updateRuleGroups
    * highVolumeQueryChanges
    * queryRuleGroups
    * queryScheduledExclusions
    * queryPolicies
    - `_endpoint/_filevantage.py`
    - `filevantage.py`
    > 4 new payload handlers were implemented.
    - `_payload/__init__.py`
    - `_payload/_filevantage.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_filevantage.py`
+ Added: A new service collection, __Cloud Snapshots__ was implemented with three new operations (_GetCredentialsMixin0_, _CreateInventory_, and _RegisterCspmSnapshotAccount_).
    - `_endpoint/__init__.py`
    - `_endpoint/_cloud_snapshots.py`
    - `__init__.py`
    - `cloud_snapshots.py`
    > Two new payload handlers were implemented.
    - `_payload/__init__.py`
    - `_payload/_cloud_snapshots.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_cloud_snapshot.py`
+ Added: 3 new operations added to the __Identity Protection__ service collection (_GetSensorAggregates_, _GetSensorDetails_, and _QuerySensorsByFilter_).
    - `_endpoint/_identity_protection.py`
    - `identity_protection.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_identity_protection.py`

## Issues resolved
+ Fixed: API errors generated by the Uber Class do not stop execution when in pythonic mode.
    - `api_complete.py`
+ Fixed: Result object failure on JSON formatted list response from _report_executions_download_get_ operation within the __Report Executions__ service collection. Closes #1033.
    - `_result/result.py`

## Other
+ Deprecated: _deleteCIDGroupMembersV1_ is now deprecated. Calls to _deleteCIDGroupMembers_ are now redirected to _deleteCIDGroupMembersV2_. __MSSP__ service collection.
    - `_endpoint/_mssp.py`
    - `mssp.py`
    > Unit testing expanded to complete code coverage.
    - `test_mssp.py`

---

# Version 1.3.0
> Developer Enhancements Release 🎉
## Added features and functionality
+ Added: **Developer Extensibility features** - Enhanced existing programmatic architecture with new objects and submodules to address technical debt and provide developers with the necessary structures to easily extend core library functionality.
  + **_APIHarness_** - Derivative and an interface class commonly referred to as the _Uber Class_, APIHarness has been refactored to inherit common functionality provided by the **_FalconInterface_** class, remove technical debt, add typing, and expand available operations and extensibility features.
    + `api_complete.py`
  + **_APIRequest_** - Simple interface class comprised of multiple data classes that is leveraged for managing the components of a request sent to the CrowdStrike API. This is a new object.
    + `_api_request/__init__.py`
    + `_api_request/_request.py`
    + `_api_request/_request_behavior.py`
    + `_api_request/_request_connection.py`
    + `_api_request/_request_meta.py`
    + `_api_request/_request_payloads.py`
    + `_api_request/_request_validator.py`
  + **_Constant submodule_** - Stores global constants used throughout the library. This is a new module implemented to store new and pre-existing constants.
    + `_constant/__init__.py`
  + **_Enum submodule_** - Stores enumerators available within the library. This is a new module implemented to store pre-existing enumerators.
    + `_enum/__init__.py`
    + `_enum/_base_url.py`
    + `_enum/_container_base_url.py`
    + `_enum/_token_fail_reason.py`
  + **_Error submodule_** - Provides python native errors and warnings. This is a new module.
    + `_error/__init__.py`
    + `_error/_exceptions.py`
    + `_error/_warnings.py`
  + **_FalconInterface_** - Interface class that handles authentication and state management, also referred to as the authentication object or the `auth_object`. Refactored to address technical debt and add new functionality.
    + `_auth_object/__init__.py`
    + `_auth_object/_base_falcon_auth.py`
    + `_auth_object/_bearer_token.py`
    + `_auth_object/_falcon_interface.py`
    + `_auth_object/_interface_config.py`
    + `_auth_object/_uber_interface.py`
  + **_Log submodule_** - Provides debug logging functionality. This is a new module.
    + `_log/__init__.py`
    + `_log/_facility.py`
  + **_Result_** - Complex interface class that is leveraged to parse and return results received from the CrowdStrike API. This class has been refactored to address technical debt and provide new developer functionality and extensibility. Default behavior for requests received from the CrowdStrike API remains unchanged (results are returned as a Python dictionary). Expanded functionality provides developers the ability to handle received responses as python structures, allowing for easy iteration and processing without having to handle a dictionary.
    + `_result/__init__.py`
    + `_result/_base_resource.py`
    + `_result/_base_dictionary.py`
    + `_result/_errors.py`
    + `_result/_expanded_result.py`
    + `_result/_headers.py`
    + `_result/_meta.py`
    + `_result/_resources.py`
    + `_result/_response_component.py`
    + `_result/_result.py`
  + **_ServiceClass_** - Interface class leveraged by Service Classes to provide common functionality. This class has also been refactored to expand on functionality provided by the **_FalconInterface_** class, remove technical debt, add typing and expand extensibility features.
    + `_service_class/_init__.py`
    + `_service_class/_base_service_class.py`
    + `_service_class/_service_class.py`
  + **_Util submodule_** - Functions and utilities library containing both private and public methods. This is a new module implemented to store new and pre-existing functions.
    + `_util/__init__.py`
    + `_util/_auth.py`
    + `_util/_functions.py`
    + `_util/_uber.py`
+ Added: **Debug logging** - Native debug logging can now be activated per class upon construction. Logs are sanitized by default.
  ```python
  import logging
  from falconpy import Hosts

  logging.basicConfig(level=logging.DEBUG)
  hosts = Hosts(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, debug=True)
  result = hosts.query_devices_by_filter_scroll()
  ```
  Log sanitization can also be disabled when instantiating the class.
  ```python
  hosts = Hosts(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, debug=True, sanitize_log=False)
  ``` 
  Local unit testing has been expanded to take advantage of this functionality. To activate, set the environment variable `FALCONPY_UNIT_TEST_DEBUG` to __`DEBUG`__.
  + `_log/__init__.py`
  + `_log/_facility.py`
+ Added: **Environment Authentication** - New authentication mechanism that retrieves CrowdStrike API credentials that are pre-defined as variables within the runtime environment. These environment variables must be named `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` and both must be present in order for this mechanism to be used. Environment Authentication is the last mechanism attempted, meaning all other authentication mechanisms will take precedence.
  ```python
  from falconpy import Hosts

  hosts = Hosts()
  result = hosts.query_devices_by_filter_scroll()
  ```
  + `_auth_object/_falcon_interface.py`
+ Added: **Pythonic response handling** - Allows for the handling of responses received from the CrowdStrike API as pythonic structures as opposed to dictionaries.
  ```python
  from falconpy import Hosts

  hosts = Hosts(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, pythonic=True)
  host_list = hosts.query_devices_by_filter_scroll()
  for device in host_list:
      print(device)
  ```
  + `_result/__init__.py`
  + `_result/_base_resource.py`
  + `_result/_base_dictionary.py`
  + `_result/_errors.py`
  + `_result/_expanded_result.py`
  + `_result/_headers.py`
  + `_result/_meta.py`
  + `_result/_resources.py`
  + `_result/_response_component.py`
  + `_result/_result.py`
+ Added: **Pythonic errors and warnings** - Leverages native Python exceptions to implement error and warning handling.
  ```python
  from falconpy import Hosts, APIError

  hosts = Hosts(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, pythonic=True)
  try:
      device_detail = hosts.get_device_details("not-a-real-id")
  except APIError as not_found:
      print(not_found)
  ```
  + `_error/__init__.py`
  + `_error/_exceptions.py`
  + `_error/_warnings.py`
+ Added: **Typing** - Type hints have been added throughout the library. This is an ongoing initiative. 

## Issues resolved
+ Fixed: Unusual responses from operations within the Falcon Container service collection.
  + `_result/_result.py`
  + `_util/_functions.py`
+ Fixed: Uber Class functionality using operations within the OAuth2 service collection. Closes #835.
  + `api_complete.py`
  + `_auth_object/_falcon_interface.py`
  + `_auth_object/_uber_interface.py`
+ Fixed: Inbound strings provided to the `creds` and `proxy` keywords are not automatically converted to dictionaries. Closes #909.
  + `_auth_object/_falcon_interface.py`
+ Fixed: Fixed missing facet keyword in follow request for vulnerabilities - Grab CVEs for CID sample. Closes #1004.
  + `samples/spotlight/spotlight_grab_cves_for_cid.py`
+ Fixed: IDs are not being migrated to the body payload when calling the `PostEntitiesAlertsV1` operation. Closes #1016.
  + `_constant/__init__.py`
  + Thanks to @tsullivan06 for identifying this issue! 🙇 

## Other
+ Expanded: Unit testing expanded to complete code coverage.
+ Updated: Added column prune keyword to Grab CVEs by CID sample. Closes #1005.
  +  `samples/spotlight/spotlight_grab_cves_for_cid.py`
+ __PLEASE NOTE__: Python 3.6 support will be discontinued in __January 2024__.

---

# Version 1.2.16
## Added features and functionality
+ Added: New keywords were added to 1 operations within the __Alerts__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `PostAggregatesAlertsV1` operation.
    - `_payload/_generic.py`
    - `alerts.py`
+ Added: New keywords were added to 6 operations within the __CompleteDashboard__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregateBlockList` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregateDetections` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregateDeviceCountCollection` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregateEscalations` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregateFCIncidents` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregateRemediations` operation.
    - `falcon_complete_dashboard.py`
+ Added: 3 new operations added to the __CSPMRegistration__ Service Class, `GetConfigurationDetectionEntities`, `GetConfigurationDetectionIDsV2`, and `GetCSPMPoliciesDetails`.
    - `_endpoint/_cspm_registration.py`
    - `_payload/_cspm_registration.py`
    - `cspm_registration.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_cspm_registration.py`
+ Added: New keywords were added to 11 operations within the __CSPMRegistration__ Service Class.
    * _iam_role_arns_ and _migrated_ were added to the `GetCSPMAwsAccount` operation.
    * _account_type_, _behavior_assessment_enabled_, _iam_role_arn_, _is_master_, _sensor_management_enabled_ and _use_existing_cloudtrail_ were added to the `CreateCSPMAwsAccount` operation.
    * _behavior_assessment_enabled_, _iam_role_arn_, _remediation_region_, _remediation_tou_accepted_ and _sensor_management_enabled_ were added to the `UpdateCSPMAwsAccount` operation.
    * _ids_, _use_existing_cloudtrail_, and _region_ were added to the `GetCSPMAwsConsoleSetupURLs` operation.
    * _ids_ was added to the `GetCSPMAwsAccountScriptsAttachment` operation.
    * _tenant_ids_ was added to the `GetCSPMAzureAccount` operation.
    * _account_type_, _client_id_, _default_subscription_, _tenant_id_ and _years_valid_ were added to the `CreateCSPMAzureAccount` operation.
    * _retain_tenant_ and _tenant_ids_ were added to the `DeleteCSPMAzureAccount` operation.
    * _years_valid_ was added to the `AzureDownloadCertificate` operation.
    * _account_type_, _subscription_ids_, and _template_ were added to the `GetCSPMAzureUserScriptsAttachment` operation.
    * _resource_id_ and _resource_uuid_ were added to the `GetBehaviorDetections` operation.
    - `_endpoint/_cspm_registration.py`
    - `cspm_registration.py`
+ Added: 1 new operation added to the __D4CRegistration__ Service Class, `GetDiscoverCloudAzureTenantIDs`.
    - `_endpoint/_d4c_registration.py`
    - `d4c_registration.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_d4c_registration.py`
+ Added: New keywords were added to 11 operations within the __D4CRegistration__ Service Class.
    * _iam_role_arn_ was added to the `CreateD4CAwsAccount` operation.
    * _limit_, _offset_, _status_ and _tenant_ids_ were added to the `GetCSPMAzureAccount` operation.
    * _account_type_, _client_id_, _default_subscription_ and _years_valid_ were added to the `CreateCSPMAzureAccount` operation.
    * _object_id_ and _tenant_id_ were added to the `UpdateCSPMAzureAccountClientID` operation.
    * _subscription_ids_, _tenant_id_ and _template_ were added to the `GetCSPMAzureUserScriptsAttachment` operation.
    * _limit_, _offset_, _parent_type_, _sort_ and _status_ were added to the `GetCSPMCGPAccount` operation.
    * _years_valid_ was added to the `DiscoverCloudAzureDownloadCertificate` operation.
    * _parent_type_ was added to the `GetCSPMGCPUserScripts` operation.
    * _parent_type_ was added to the `CreateD4CGCPAccount` operation.
    - `_endpoint/_d4c_registration.py`
    - `_payload/_d4c_registration.py`
    - `d4c_registration.py`
+ Added: New keywords were added to 2 operations within the __Detects__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `GetAggregateDetects` operation.
    * _new_behaviors_processed_ was added to the `UpdateDetectsByIdsV2` operation.
    - `_payload/_detects.py`
    - `detects.py`
+ Added: _add-rule-group_ and _remove-rule-group_ added as possible values for the __*action_name*__ keyword within the `performDeviceControlPoliciesAction` operation in the __DeviceControlPolicies__ Service Class.
    - `_endpoint/_device_control_policy.py`
    - `device_control_policy.py`
+ Added: 3 new operations added to the __FalconXSandbox__ Service Class, `GetMemoryDumpExtractedStrings`, `GetMemoryDumpHexDump`, and `GetMemoryDump`.
    - `_endpoint/_falconx_sandbox.py`
    - `falconx_sandbox.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_falconx_sandbox.py`
+ Added: New __FDR__ Service Class with 5 new operations, `fdrschema_combined_event_get`, `fdrschema_entities_event_get`, `fdrschema_entities_field_get`, `fdrschema_queries_event_get`, and `fdrschema_queries_field_get`.
    - `_endpoint/_fdr.py`
    - `_endpoint/__init__.py`
    - `_endpoint/deprecated/_fdr.py`
    - `_endpoint/deprecated/__init__.py`
    - `fdr.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_fdr.py`
+ Added: New keyword was added to 1 operation within the __FalconContainer__ Service Class.
    * _applicationPackages_ was added to the `ReadImageVulnerabilities` operation.
    - `_payload/_container.py`
    - `falcon_container.py`
+ Added: New keywords were added to 9 operations within the __FirewallManagement__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `aggregate_events` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `aggregate_policy_rules` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `aggregate_rule_groups` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `aggregate_rules` operation.
    * _created_by_ and _created_on_ were added to the `upsert_network_locations` operation.
    * _created_by_ and _created_on_ were added to the `update_network_locations` operation.
    * _local_logging_ was added to the `update_policy_container_v1` operation.
    * _platform_ was added to the `create_rule_group` operation.
        > _platform_ids_ was removed from the `create_rule_group` operation
    * _fqdn_ and `fqdn_enabled` were added to the `create_rule_group_validation` operation.
    - `_payload/_firewall.py`
    - `firewall_management.py`
+ Added: New keyword was added to 1 operation within the __FlightControl__ Service Class.
    * _filter_ was added to the `queryChildren` operation.
    - `_endpoint/_mssp.py`
    - `mssp.py`
+ Added: New keyword was added to 1 operation within the __Hosts__ Service Class.
    * _disable_hostname_check_ was added to the `entities_perform_action` operation.
    - `_endpoint/_hosts.py`
    - `hosts.py`
+ Added: New keywords were added to 1 operation within the __Incidents__ Service Class.
    * _overwrite_detects_ and _update_detects_ were added to the `PerformIncidentAction` operation.
    - `_endpoint/_incidents.py`
    - `incidents.py`
+ Added: New keywords were added to 3 operations within the __IOC__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `indicator_aggregate_v1` operation.
    * _from_parent_ was added to the `GetIndicatorsReport` operation.
    * _from_parent_ was added to the `indicator_search_v1` operation.
    * _from_parent_ was added to the `indicator_update_v1` operation.
    - `_endpoint/_ioc.py`
    - `_payload/_ioc.py`
    - `ioc.py`
+ Added: New keywords were added to 3 operations within the __KubernetesProtection__ Service Class.
    * _is_horizon_acct_ was added to the `GetAWSAccountsMixin0` operation.
    * _is_self_managed_cluster_ was added to the `GetHelmValuesYaml` operation.
    * _status_ was added to the `GetClusters` operation.
    - `_endpoint/_kubernetes_protection.py`
    - `kubernetes_protection.py`
+ Added: 1 new operation added to the __ODS__ Service Class, `aggregate_query_scan_host_metadata`.
    - `_endpoint/_ods.py`
    - `_endpoint/deprecated/_ods.py`
    - `ods.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_ods.py`
+ Added: New keywords were added to 3 operations within the __ODS__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `aggregate_scans` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `aggregate_scheduled_scans` operation.
    * _scan_inclusions_ was added to the `schedule_scan` operation.
    - `_payload/_ods.py`
    - `ods.py`
+ Added: New keyword was added to 1 operation within the __OAuth2__ Service Class.
    * _client_id_ was added to the `revoke` operation.
    - `_endpoint/_oauth2.py`
    - `oauth2.py`
+ Added: New keywords were added to 2 operations within the __OverwatchDashboard__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregatesEventsCollections` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregatesEvents` operation.
    - `overwatch_dashboard.py`
+ Added: New keyword was added to 1 operation within the __Quarantine__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `GetAggregateFiles` operation.
    - `quarantine.py`
+ Added: New keyword was added to 1 operation within the __RealTimeResponse__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `RTR_AggregateSessions` operation.
    - `real_time_response.py`
+ Added: New keywords were added to 7 operations within the __Recon__ Service Class.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregateNotificationsExposedDataRecordsV1` operation.
    * _exclude_, _from_, _include_ and _max_doc_count_ were added to the `AggregateNotificationsV1` operation.
    * _content_format_ and _trigger_matchless_ were added to the `CreateActionsV1` operation.
    * _content_format_ and _trigger_matchless_ were added to the `UpdateActionsV1` operation.
    * _breach_monitoring_enabled_ and _substring_matching_enabled_ were added to the `CreateRulesV1` operation.
    * _breach_monitoring_enabled_ and _substring_matching_enabled_ were added to the `UpdateRulesV1` operation.
    * _notificationsDeletionRequested_ was added to the `DeleteRulesV1` operation.
    - `_endpoint/_recon.py`
    - `_payload/_recon.py`
    - `recon.py`
+ Added: New keywords were added to 3 operations within the __SensorUpdatePolicy__ Service Class.
    * _scheduler_, _show_early_adopter_builds_ and _variants_ were added to the `createSensorUpdatePoliciesV2` operation.
    * _scheduler_, _show_early_adopter_builds_ and _variants_ were added to the `updateSensorUpdatePoliciesV2` operation.
    * _stage_ was added to the `queryCombinedSensorUpdateBuilds` operation.
    - `_endpoint/_sensor_update_policy.py`
    - `sensor_update_policy.py`
+ Added: _add-rule-group_ and _remove-rule-group_ added as possible values for the __*action_name*__ keyword within the `performSensorUpdatePoliciesAction` operation in the __SensorUpdatePolicy__ Service Class.
    - `_endpoint/_sensor_update_policies.py`
    - `sensor_update_policies.py`
+ Added: New keyword was added to 1 operation within the __UserManagement__ Service Class.
    * _action_ was added to the `queryiesRolesV1` operation.
    - `_endpoint/_user_management.py`
    - `user_management.py`
+ Added: 1 new operation added to the __ZeroTrustAssessment__ Service Class, `getCombinedAssessmentsQuery`.
    - `_endpoint/_zero_trust_assessment.py`
    - `zero_trust_assessment.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_zero_trust_assessment.py`

## Other
+ Expanded: Additional parameters were added to the settings dictionary/keyword within the `createDeviceControlPolicies` and `updateDeviceControlPolicies` operations.
    - `_payload/_device_control_policies.py`
    - `device_control_policies.py`
+ Renamed: 1 keyword was renamed within the __FalconContainer__ Service Class.
    * _credentials_ was renamed to _credential_ within the `CreateRegistryEntities` operation.
    - `_payload/_container.py`
    - `falcon_container.py`
+ Reduced: Limit maximum for `queryCombinedSensorUpdateKernels` operation within the __SensorUpdatePolicy__ Service Class was changed from __*5000*__ to __500__.
    - `_endpoint/_sensor_update_policies.py`
+ Reduced: Limit maximum for `querySensorUpdateKernelsDistinct` operation within the __SensorUpdatePolicy__ Service Class was changed from __*5000*__ to __500__.
    - `_endpoint/_sensor_update_policies.py`
+ Increased: Limit maximum for `QueryAWSAccounts` operation within the __CloudConnectAWS__ Service Class was changed from __*500*__ to __1000__.
    - `_endpoint/_cloud_connect_aws.py`
+ Increased: Limit maximum for `QueryAWSAccountsForIDs` operation within the __CloudConnectAWS__ Service Class was changed from __*500*__ to __1000__.
    - `_endpoint/_cloud_connect_aws.py`
+ Renamed: 8 operations renamed within the __D4CRegistration__ Service Class. Legacy operation IDs were deprecated, with aliases created to avoid introducing breaking changes.
    * _GetCSPMAzureAccount_ is now `GetDiscoverCloudAzureAccount`.
    * _CreateCSPMAzureAccount_ is now `CreateDiscoverCloudAzureAccount`.
    * _UpdateCSPMAzureAccountClientID_ is now `UpdateDiscoverCloudAzureAccountClientID`.
    * _GetCSPMAzureUserScriptsAttachment_ is now `GetDiscoverCloudAzureUserScriptsAttachment`.
    * _GetCSPMAzureUserScripts_ is now `GetDiscoverCloudAzureUserScripts`.
    * _GetCSPMCGPAccount_ is now `GetD4CCGPAccount`.
    * _CreateCSPMGCPAccount_ is now `CreateD4CGCPAccount`.
    * _GetCSPMGCPUserScripts_ is now `GetD4CGCPUserScripts`.
    - `_endpoint/_d4c_registration.py`
    - `_endpoint/__init__.py`
    - `_endpoint/deprecated/_d4c_registration.py`
    - `_endpoint/deprecated/__init__.py`
    - `d4c_registration.py`
+ Renamed: 1 operation renamed within the __ZeroTrustAssessment__ Service Class. Legacy operation ID was deprecated, with an alias created to avoid introducing a breaking change.
    * _getComplianceV1_ is now `getAuditV1`.
    - `_endpoint/_zero_trust_assessment.py`
    - `_endpoint/__init__.py`
    - `_endpoint/deprecated/_zero_trust_assessment.py`
    - `_endpoint/deprecated/__init__.py`
    - `zero_trust_assessment.py`

---

# Version 1.2.15
## Added features and functionality
+ Added: 1 new operation added to the __ZeroTrustAssessment__ Service Class, `getAssessmentsByScoreV1`.
    - `_endpoint/_zero_trust_assessment.py`
    - `zero_trust_assessment.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_zero_trust_assessment.py`

## Issues resolved
+ Fixed: JSONDecoder error when running within an environment leveraging the `simplejson` 3rd party library versus the standard `json` library.
    - `_util.py`
    > Thanks to @khyberspache for identifying and resolving this issue! 🙇

---

# Version 1.2.14
## Added features and functionality
+ Updated: Added `image_id` and `digest` options to the `GetImageAssessmentReport` operation (__FalconContainer__ Service Class).
    - `_endpoint/_falcon_container.py`
    - `falcon_container.py`

+ Added: 5 new operations added to the __FalconContainer__ Service Class, `ReadRegistryEntitiesByUUID`, `CreateRegistryEntities`, `DeleteRegistryEntities`, `UpdateRegistryEntities`, `ReadRegistryEntities`.
    - `_endpoint/_falcon_container.py`
    - `falcon_container.py`
    > Adds one new payload handler.
    - `_payload/_container.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_falcon_container.py`

---

# Version 1.2.13
## Added features and functionality
+ Added: 2 new operations (IoT) added to the __Discover__ Service Class, `get_iot_hosts` and `query_iot_hosts`.
    - `_endpoint/_discover.py`
    - `_endpoint/deprecated/_discover.py`
    - `discover.py`
    - `tests/test_discover.py`
+ Added: 1 new operation added to the __MessageCenter__ Service Class, `CreateCaseV2`.
    - `_endpoint/_message_center.py`
    - `_payload/_message_center.py`
    - `message_center.py`
    - `tests/test_message_center.py`

## Issues resolved
+ Fixed: Docstring typo in the `GetAzureInstallScript` operation within the  __KubernetesProtection__ Service Class. Closes #933.
    - `kubernetes_protection.py`

---

# Version 1.2.12
## Added features and functionality
+ Added: Enhanced payload handler for `create_rule` operation to allow for passing a list of dictionaries for the `field_values` keyword. Closes #916.
    - `_payload/_ioa.py`
    - `tests/test_custom_ioa.py`
+ Added: 5 new operations added to the __KubernetesProtection__ Service Class, `GetAzureInstallScript`, `GetAzureTenantConfig`, `GetAzureTenantIDs`, `GetCombinedCloudClusters`, and `GetStaticScripts`.
    - `_endpoint/_kubernetes_protection.py`
    - `kubernetes_protection.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_kubernetes_protection.py`

## Issues resolved
+ Fixed: Updated docstring comments to properly reflect syntax for providing a trusted certificate bundle for API requests. Closes #910.
    - `_service_class.py`
    - `api_complete.py`
+ Pinned: IPython version pinned to 8.10.0 to avoid `SNYK-PYTHON-IPYTHON-3318382`.
    - `requirements-dev.txt`
+ Fixed: Added missing `ids` keyword handlers for Uber Class operation calls. Closes #919.
    - `_uber_default_preferences.py`
+ Fixed: Updated docstrings for `combinedQueryVulnerabilities` operation to properly list request limit of 5000. Closes #922.
    - `spotlight_vulnerabilities.py`

## Other
+ Updated: Removed unnecessary `source` parameter from endpoint module for `ArchiveUploadV2` operation.
    - `_endpoint/_sample_uploads.py`

---

# Version 1.2.11
## Added features and functionality
+ Added: Two new operations added to the __Discover__ Service Class, `query_applications` and `get_applications`.
    - `discover.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_discover.py`

## Issues resolved
+ Fixed: Added `variables` keyword to `GraphQL` within __IdentityProtection__ Service Class. Closes #902.
    - `identity_protection.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_identity_protection.py`
    - Thanks go out to @cl6227 for identifying and reporting this issue! 🙇

+ Fixed: Missing default value for `file_data` keyword argument of the `upload_sample` method of the __SampleUploads__ Service Class. Closes #898.
    - `falconx_sandbox.py`
    - Thanks go out to @awhogan for identifying and reporting this issue! 🙇

---

# Version 1.2.10
## Added features and functionality
+ Added: Two new operations added to the __DeviceControlPolicies__ Service Class, `getDefaultDeviceControlPolicies` and `updateDefaultDeviceControlPolicies`.
    - `device_control_policies.py`
    > Adds one new payload handler.
    - `_payload/__init__.py`
    - `_payload/_device_control_policy.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_device_control_policies.py`
+ Added: Three new operations to the __Intel__ Service Class, `GetMitreReport`, `PostMitreAttacks` and `QueryMitreAttacks`.
    - `intel.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_intel.py`

## Issues resolved
+ Fixed: Error handling `id` argument within the body payload handler for the `updateDeviceControlPolicies` operation.
    - `_payload/_device_control_policy.py`
    - Special thanks go out to @CommonVulnerability for reporting this issue and submitting the fix! 🙇

## Other
+ Updated: Removed `scans_report` operation from the new __ODS__ Service Class.
    - `ods.py`
    > Unit testing updated.
    - `tests/test_ods.py`

---

# Version 1.2.9
## Issues resolved
+ Fixed: Authentication object synchronization issue for certain scenarios. Relates to #829.
    - `_util.py`
    - Thanks go out to @davidt99 for contributing this fix!

---

# Version 1.2.8
## Issues resolved
+ Fixed: Add missing operation IDs to `PREFER_IDS_IN_BODY` constant to trigger Uber Class body payload abstraction for the `ids` keyword. Closes #864.
    - `_uber_default_preference.py`
    - Thanks to @tsullivan06 for identifying this issue!

---

# Version 1.2.7
## Added features and functionality
+ Added: One operation added to the __SampleUploads__ Service Class, `ArchiveUploadV1`.
    - `sample_uploads.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_sample_uploads.py`
+ Added: Four new operations to the __KubernetesProtection__ Service Class, `ListAzureAccounts`, `CreateAzureSubscription`, `DeleteAzureSubscription`, and `PatchAzureServicePrincipal`.
    - `kubernetes_protection.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_kubernetes_protection.py`

## Issues resolved
+ Fixed: Missing redirection endpoints for legacy operations within the __MSSP__ Service Class. (`getCIDGroupMembersByV1`, `getCIDGroupByIdV1`, `getUserGroupMembersByIDV1` and `getUserGroupsByIDV1`) Calls to the generic operation ID (ex: `getUserGroupsByID`) are redirected to the v2 equivalent. Closes #859.
    - `mssp.py`

+ Fixed: Added missing redirection for `update_policy_container_v2` operation to the __FirewallManagement__ Service Class. Closes #856.
    - `firewall_management.py`

---

# Version 1.2.6
## Added features and functionality
+ Added: Nine new operations added to the __FirewallManagement__ Service Class. (`get_network_location_details`, `update_network_locations_metadata`, `update_network_locations_precedence`, `get_network_locations`, `create_network_locations`, `update_network_locations`, `upsert_network_locations`, `delete_network_locations`, `query_network_locations`)
    - `firewall_management.py`
    - `_endpoint/_firewall_management.py`
    > Adds two new payload handlers.
    - `_payload/_firewall.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_firewall_management.py`

+ Added: Five new operations added to the Flight Control (__MSSP__) Service Class. (`getChildrenV2`, `getCIDGroupMembersByV2`, `getCIDGroupByIdV2`, `getUserGroupMembersByIDV2`, `getUserGroupsByIDV2`)
    - `mssp.py`
    - `_endpoint/_mssp.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_mssp.py`

+ Added: One new operation added to the __Hosts__ Service Class. (`entities_perform_action`)
    - `hosts.py`
    - `_endpoint/_hosts.py`
    > One new payload handler was added.
    - `_payload/_generic.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_hosts.py`

+ Added: One new operation added to the __InstallationTokens__ Service Class. (`customer_settings_update`)
    - `installation_tokens.py`
    - `_endpoint/_installation_tokens.py`
    > One new payload handler was added.
    - `_payload/_generic.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_installation_tokens.py`

+ Added: Two new operations added to the __Intel__ Service Class. (`GetVulnerabilities`, `QueryVulnerabilities`)
    - `intel.py`
    - `_endpoint/_intel.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_intel.py`

+ Added: New __ODS__ Service Class (On Demand Scan) with fifteen new operations. (`aggregate_scans`, `aggregate_scheduled_scans`, `get_malicious_files_by_id`, `cancel_scans`, `get_scan_host_metadata_by_ids`, `scans_report`, `get_scans_by_scan_ids`, `scans_report`, `get_scheduled_scans_by_scan_ids`, `schedule_scan`, `delete_scheduled_scans`, `query_malicious_files`, `query_scan_host_metadata`, `query_scans`, `query_scheduled_scans`)
    - `__init__.py`
    - `ods.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_ods.py`
    - `_endpoint/deprecated/__init__.py`
    - `_endpoint/deprecated/_ods.py`
    > Two new payload handlers were added.
    - `_payload/_ods.py`
    > New unit testing implemented to confirm functionality and complete code coverage.
    - `tests/test_ods.py`

+ Added: Seven new operations added to the __Recon__ Service Class. (`AggregateNotificationsExposedDataRecordsV1`, `GetFileContentForExportJobsV1`, `GetExportJobsV1`, `CreateExportJobsV1`, `DeleteExportJobsV1`, `GetNotificationsExposedDataRecordsV1`, `QueryNotificationsExposedDataRecordsV1`)
    - `recon.py`
    - `_endpoint/_recon.py`
    > One new payload handler was added.
    - `_payload/_recon.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_recon.py`

+ Added: Seven new operations added to the __SampleUploads__ Service Class. (`ArchiveListV1`, `ArchiveGetV1`, `ArchiveDeleteV1`, `ArchiveUploadV2`, `ExtractionListV1`, `ExtractionGetV1`, `ExtractionCreateV1`)
    - `sample_uploads.py`
    - `_endpoint/_sample_uploads.py`
    > One new payload handler was added.
    - `_payload/_sample_uploads.py`
    > Unit testing expanded to complete code coverage.
    - `tests/test_sample_uploads.py`
    - `tests/testfile.zip`

## Other
+ Changed: Due to updates in the latest Ubuntu version used in GitHub actions, unit testing for Python 3.6 has been split off to a stand alone workflow.
+ Added: Python 3.11 support.
    - `setup.py`
---

# Version 1.2.5
## Issues resolved
+ Fixed: Invalid `body` payload when leveraging the Uber Class to call the `RTR_DeleteSession` operation. Closes #839.
    - `_uber_default_preference.py`

---

# Version 1.2.4
## Added features and functionality
+ Added: New __TailoredIntelligence__ Service Class.
    - `__init__.py`
    - `tailored_intelligence.py`
    - `_endpoint/__init__.py`
    - `_endpoint/_tailored_intelligence.py`
    - `tests/test_tailored_intelligence.py`
    > Unit testing expanded to complete code coverage.
+ Added: `GetD4CAwsAccount`, `CreateD4CAwsAccount`, `DeleteD4CAwsAccount`, `GetD4CAwsConsoleSetupURLs`, `GetD4CAWSAccountScriptsAttachment`, and `GetHorizonD4CScripts` operations to the __D4CRegistration__ Service Class.
    - `d4c_registration.py`
    - `_endpoint/_d4c_registration.py`
    - `_payload/__init__.py`
    - `_payload/_d4c_registration.py`
    > Adds one new payload handler.
    - `tests/test_d4c_registration.py`
    > Unit testing expanded to complete code coverage.
+ Added: `update_policy_container_v1`, `create_rule_group_validation`, `update_rule_group_validation`, and `validate_filepath_pattern` operations to the __FirewallManagement__ Service Class.
    - `firewall_management.py`
    - `_endpoint/_firewall_management.py`
    > The legacy operation `update_policy_container` now points to the updated endpoint `/fwmgr/entities/policies/v2`.
    - `_payload/__init__.py`
    - `_payload/_firewall.py`
    > Adds two new payload handlers.
    - `tests/test_firewall_management.py`
    > Unit testing expanded to complete code coverage.
+ Added: `indicator_aggregate_v1`, `action_get_v1`, `GetIndicatorsReport`, `action_query_v1`, `ioc_type_query_v1`, `platform_query_v1`, and `severity_query_v1` operations to the __IOC__ Service Class.
    - `ioc.py`
    - `_endpoint/_ioc.py`
    - `_payload/__init__.py`
    - `_payload/_ioc.py`
    > Adds one new payload handler.
    - `tests/test_ioc.py`
    > Unit testing expanded to complete code coverage.
+ Added: _from_parent_ parameter to the `indicator_delete_v1` operation within the __IOC__ Service Class.
    - `ioc.py`
    - `_endpoint/_ioc.py`
+ Added: _timeout_ and _timeout_duration_ parameters to the `RTR_InitSession` operation within the __RealTimeResponse__ Service Class.
    - `real_time_response.py`
    - `_endpoint/_real_time_response.py`
+ Added: _host_timeout_duration_ parameter to the `BatchAdminCmd` operation within the __RealTimeResponseAdmin__ Service Class.
    - `real_time_response_admin.py`
    - `_endpoint/_real_time_response_admin.py`
+ Added: Maximum and minimum limits for the _limit_ parameter used by the `QueryNotificationsV1` operation within the __Recon__ Service Class.
    - `_endpoint/_recon.py`
+ Added: New `ReadImageVulnerabilities` operation to the __FalconContainer__ Service Class.
    - `falcon_container.py`
    - `_endpoint/_falcon_container.py`
    - `_payload/__init__.py`
    - `_payload/_container.py`
    > Adds one new payload handler.
    - `tests/test_falcon_container.py`
    > Unit testing expanded to complete code coverage.

## Other
+ Updated: Updated the description, changed datatype from `string` to `int` and added maximum / minimum limits for the _offset_ parameter used by the `QueryActionsV1` operation within the __Recon__ Service Class.
    - `_endpoint/_recon.py`
+ Removed: `X-CS-USERNAME` parameter from all operations within the __IOC__ Service Class.
    - `_endpoint/_ioc.py`
+ Updated: _query_rule_groups_full_ and _query_rule_groupsMixin0_ operations - Removed `description` as an available field from enum. Updated operation description.
    - `_endpoint/_custom_ioa.py`
+ Updated: Changed _collectionFormat_ value from `csv` to `multi` for multiple operations within the `_endpoint` module.
    - `_endpoint/_ioa_exclusions.py` (_getIOAExclusionsV1_, _deleteIOAExclusionsV1_)
    - `_endpoint/_ml_exclusions.py` (_getMLExclusionsV1_, _deleteMLExclusionsV1_)
    - `_endpoint/_sensor_visibility_exclusions.py` (_getSensorVisibilityExclusionsV1_, _deleteSensorVisibilityExclusionsV1_)
+ Updated: Removed _maxLength_ and _minLength_ values for multiple operations within the `_endpoint` module.
    - `_endpoint/_device_control_policies.py` (_getDeviceControlPolicies_, _deleteDeviceControlPolicies_)
    - `_endpoint/_firewall_policies.py` (_getFirewallPolicies_, _deleteFirewallPolicies_)
    - `_endpoint/_host_group.py` (_getHostGroups_, _deleteHostGroups_)
    - `_endpoint/_prevention_policies.py` (_getPreventionPolicies_, _deletePreventionPolicies_)
    - `_endpoint/_response_policies.py` (_getRTResponsePolicies_, _deleteRTResponsePolicies_)
    - `_endpoint/_sensor_update_policies.py` (_getSensorUpdatePolicies_, _deleteSensorUpdatePolicies_, _getSensorUpdatePoliciesV2_)
+ Updated: GovCloud headers are now returned when providing GovCloud credentials to a commercial cloud region. Deprecated fallback handler within `autodiscover_region` method.
    - `_util.py`
    > This code will be retained for now. As of this version, GovCloud region autodiscovery is __not__ supported.
+ Updated: Pinned `setuptools` version to 65.5.1 ([SNYK-PYTHON-SETUPTOOLS-3113904](https://security.snyk.io/vuln/SNYK-PYTHON-SETUPTOOLS-3113904)).
    - `requirements-dev.txt`

---

# Version 1.2.3
## Added features and functionality
+ Added: Specify `N-1` and `N-2` within the Sensor Download sample. Closes #793.
    - `samples/sensor_download/download_sensor.py`

## Issues resolved
+ Fixed: Invalid `body` payload passed when leveraging the Uber Class to call the `RTR_GetExtractedFileContents` operation. Closes #788.
    - `_uber_default_preference.py`

+ Fixed: Invalid data type comparison in RTR dump memory sample.
    - `samples/rtr/pid-dump/rtr_dump_memory.py`

+ Fixed: Invalid arguments provided to `execute_admin_command` method within RTR dump memory sample. Closes #789.
    - `samples/rtr/pid-dump/rtr_dump_memory.py`


---

# Version 1.2.2
## Added features and functionality
+ Added: Easy Object Authentication syntax.  You no longer need to specify the `auth_object` attribute of the Service Class you are using to authenticate to subsequent Service Classes. Legacy Object Authentication is still (and will always be) fully supported.
    ```python
    import os
    from falconpy import Hosts
    from falconpy import HostGroup

    # Old Syntax
    hosts = Hosts(client_id=os.getenv("FALCON_CLIENT_ID"),
                  client_secret=os.getenv("FALCON_CLIENT_SECRET")
                  )
    hostgroups = HostGroup(auth_object=hosts.auth_object)

    # New Syntax
    hosts = Hosts(client_id=os.getenv("FALCON_CLIENT_ID"),
                  client_secret=os.getenv("FALCON_CLIENT_SECRET")
                  )
    hostgroups = HostGroup(auth_object=hosts)
    ```
    - `_service_class.py`
    - `tests/test_authentications.py`

## Other
+ Changed: Updated development package module name to be `falconpydev` to prevent confusion with the production package module name.
    - `dev_setup.py`

---

# Version 1.2.1
## Added features and functionality
+ Added: Added alias for `post_device_details_v2` to Hosts Service Class. Closes #773.
    - `hosts.py`
    - `tests/manual/test_get_device_details.py`

## Issues resolved
+ Fixed: Typo in docstring for `perform_incident_action` method. Closes #776.
    - `incidents.py`
+ Fixed: Added `host_timeout_duration` documentation to docstrings within operations in the Real Time Response Service Class.
    - `real_time_response.py`

## Other
+ Updated: Adjusted unit testing to cover new API returns.
    - `tests/falcon_container.py`
    - `tests/kubernetes_protection.py`

---

# Version 1.2.0
## Added features and functionality
+ Updated: Updated operation payload parameter datatype details.
    - `_endpoint/_ioc.py`
    - `_endpoint/_recon.py`
    - `_endpoint/_sample_uploads.py`

+ Updated: Updated operation payload parameter data location details.
    - `_endpoint/_falconx_sandbox.py`
    - `_endpoint/_sample_uploads.py`

+ Added: New `host_timeout_duration` parameter to `BatchActiveResponderCmd`, `BatchCmd`, `BatchGetCmd` and `BatchInitSessions` operations within the Real Time Response Service Collection.
    - `_endpoint/_real_time_response.py`

+ Added: New `GetDeviceDetailsV2` and `PostDeviceDetailsV2` operations to Hosts Service Collection.
    > The operation `GetDeviceDetails` is now deprecated, and will eventually be removed from the CrowdStrike API. Due to backwards compatibility considerations, and the added functionality provided by the new endpoint, FalconPy will continue to support this operation ID by redirecting requests to `PostDeviceDetailsV2`. IDs that are provided in incorrect payload destinations due to the differences between a GET and POST operation are migrated to the appropriate dictionary before the request is made. This solution is implemented within the Hosts Service Class (`GetDeviceDetails`, `get_device_details`) and within the Uber Class. Developers __must__ upgrade installations to FalconPy v1.2.0 to benefit from this new functionality. __Administrators and end users are strongly urged to consider upgrading to v1.2.0 before this endpoint is removed.__
    - `_endpoint/_hosts.py`
    - `_uber_default_preference.py`
    - `api_complete.py`
    - `hosts.py`
    - `tests/test_get_device_details.py`

+ Added: Falcon Container registry functionality to Falcon Container Service Class.
    > This solution implements three "mock" operation IDs; `GetImageAssessmentReport` (`get_assessment`), `DeleteImageDetails` (`delete_image_details`), and `ImageMatchesPolicy` (`image_matches_policy`). All mocked operations are available from both the Service and Uber classes. The Falcon Container Registry base URL is calculated based upon the base URL used for authentication.
    - `_endpoint/_falcon_container.py`
    - `__init__.py`
    - `_container_base_url.py`
    - `_uber_default_preference.py`
    - `_util.py`
    - `api_complete.py`
    - `falcon_container.py`
    - `tests/test_falcon_container.py`

## Issues resolved
+ Fixed: Default NoneType preference for body payloads sent to the `RTR_ListFiles` and `RTR_ListFilesV2` operations. Closes #750.
    - `_uber_default_preference.py`

+ Removed: Unused header payload parameters from operation payloads.
    - `_endpoint/_falconx_sandbox.py`
    - `_endpoint/_firewall_management.py`
    - `_endpoint/_recon.py`
    - `_endpoint/_report_executions.py`
    - `_endpoint/_sample_uploads.py`

+ Removed: Duplicate parameter definition (`after`) from `indicator_combined_v1` operation.
    - `_endpoint/_ioc.py`

## Other
+ Updated: Comment updates.
    - `_endpoint/_d4c_registration.py`
+ Updated: Fixed docstring typo within `userActionV1` operation. Closes #763.
    - `user_management.py`

---

# Version 1.1.6
## Added features and functionality
+ Added: New Alerts service collection operation - `PatchEntitiesAlertsV2` (`update_alerts_v2`).
    - `_endpoint/_alerts.py`
    - `_payload/_alerts.py`
    - `alerts.py`
    - `tests/test_alerts.py`
+ Added: New Service Collection - Mobile Enrollment. Matching Service Class / Uber Class functionality. Unit testing expanded to cover new methods.
    - `_endpoint/_mobile_enrollment.py`
    - `mobile_enrollment.py`
    - `tests/test_mobile_enrollment.py`
+ Added: New User Management service collection operations
    * combinedUserRolesV1 - `get_user_grants`
    * get_user_roles - `get_user_grants`
    * get_user_roles_combined - `get_user_grants`
    * entitiesRolesV1 - `get_roles_mssp`
    * userActionV1 - `user_action`
    * userRolesActionV1 - `user_roles_action`
    * retrieveUsersGETV1 - `retrieve_users`
    * createUserV1 - `create_user_mssp`
    * deleteUserV1 - `delete_user_mssp`
    * updateUserV1 - `update_user_mssp`
    * queryRolesV1 - `query_roles`
    * queriesRolesV1 - `query_roles`
    * queryUserV1 - `query_users`
    - `user_management.py`
    - `tests/test_user_management.py`

+ Added: Extended custom headers (`ext_headers`) functionality for Service Classes.
    - `_service_class.py`

## Issues resolved
+ Added: Alias for `get_online_state_v1`. Closes #739.
    - `hosts.py`

---

# Version 1.1.5
## Added features and functionality
+ Added: New Service Collection - Alerts. Matching Service Class / Uber class functionality. Unit testing expanded to cover new methods.
    - `_endpoint/__init__.py`
    - `_endpoint/_alerts.py`
    - `_payload/__init__.py`
    - `_payload/_alerts.py`
    - `alerts.py`
    - `__init__.py`
    - `tests/test_alerts.py`
+ Added: Expanded IdentityProtection unit testing to cover `US-2`.
    - `tests/test_identity_protection.py`

## Issues resolved
+ Fixed: Uber Class override keyword requires a null action parameter. Closes #706.
    - `api_complete.py`
+ Fixed: Responses containing charset are not parsed as JSON. This impacted responses from the Identity Protection service collection. Closes #708.
    - `_util.py`
    - `tests/test_identity_protection.py`
    - Thanks to @hod-alpert for identifying and resolving this issue!

## Other
+ Moved: Abstracted Cloud Region autodiscovery functionality into a standalone method to reduce code segment size.
    - `_util.py`

---

# Version 1.1.4
## Added features and functionality
+ Added: New operation - AzureDownloadCertificate (CSPMRegistration)
    - `_endpoint/_cspm_registration.py`
    - `cspm_registration.py`
    - `tests/test_cspm_registration.py`
+ Added: New operation - DiscoverCloudAzureDownloadCertificate (D4CRegistration)
    - `_endpoint/_d4c_registration.py`
    - `d4c_registation.py`
    - `tests/test_d4c_registration.py`
+ Added: New parameter - `disable_hostname_check` (QueryString) in performGroupAction (HostGroup)
    - `_endpoint/_host_group.py`
    - `host_group.py`
+ Added: New operation - GetOnlineState_V1 (Hosts)
    - `_endpoint/_hosts.py`
    - `hosts.py`
    - `tests/test_hosts.py`
+ Added: New parameter - `include_relations` in QueryIntelIndicatorEntities and QueryIntelIndicatorIds (Intel)
    - `_endpoint/_intel.py`
    - `intel.py`
+ Added: New operations - RTR_GetPut_FilesV2 and RTR_GetScriptsV2 (RTR Administration)
    - `_endpoint/_real_time_response_admin.py`
    - `real_time_response_admin.py`
    - `tests/test_real_time_response_admin.py`
+ Updated: DataType - `csv` -> `multi` for the `facet` parameter in combinedQueryVulnerabilities (SpotlightVulnerabilities)
    - `_endpoint/_spotlight_vulnerabilities.py`

## Issues resolved
+ Fixed: Docstring typo in `create_rule_group` method (FirewallManagement)
    - `firewall_management.py`
+ Fixed: Typo in supported values definition for combinedQueryVulnerabilities endpoint definition.
    _ `_endpoint/_spotlight_vulnerabilities.py`

---

# Version 1.1.3
## Added features and functionality
+ Added: Firewall rules payload abstraction for the `create_rule_group` method. Firewall diff_operations payload abstraction for the `update_rule_group` method.
    - `_payload/_firewall.py`
    - `firewall_management.py`
    - `tests/test_firewall_management.py`

---

# Version 1.1.2
## Issues resolved
+ Fixed: Resolved issue with aggregate payload generation within the Detects, MessageCenter and Recon Service Classes. Closes #664.
    - `detects.py`
    - `message_center.py`
    - `recon.py`

## Other
+ Updated: Added macOS environment detail to docstring in `submit` method of the Falcon X Sandbox Service Class. Closes #651.
    - `falconx_sandbox.py`


---

# Version 1.1.1
## Issues resolved
+ Bug fix: Resolved issue impacting the creation of certain action parameters used within payloads for the `perform_incident_action` method of the Incidents Service Class. Closes #656.
    - `_payload/_incidents.py`

---

# Version 1.1.0
## Added features and functionality
+ Added: Results object expansion - expanded results are returned as a tuple, Ex: `(status_code, headers, content)`. This allows for
headers and status to be checked on binary API returns. Expanded results are supported for all calls to the API and can be requested from
any Service Class method or the Uber Class __command__ method using the keyword `expand_result`.
    - `_result.py`
    - `_util.py`
    - `api_complete.py`
    - `test_sample_uploads.py`

    __Example__
    ```python
    # Pass a boolean True to the `expand_result` keyword to request expanded results.
    download_result = samples.get_sample(ids=file_sha, expand_result=True)

    # We're returned a tuple (status, headers, content)
    # Status will be in 0
    print(f"Status returned: {download_result[0]}")
    # Headers will be in 1
    print(f"Headers returned: {download_result[1]}")
    # File content will be in 2
    with open(example_file, "wb") as download_file:
        download_file.write(download_result[2])
    ```

+ Added: Specify action_parameters keys for __perform__ operations using keywords instead of a list of dictionaries. 
    * Keyword: `group_id`
        - `device_control_policies.py` (_perform_action_ method)
        - `firewall_policies.py` (_perform_action_ method)
        - `prevention_policy.py` (_perform_policies_action_ method)
        - `response_policies.py` (_perform_policies_action_ method)
        - `sensor_update_policy.py` (_perform_policies_action_ method)
    * Keyword: `filter`
        - `host_group.py` (_perform_group_action_ method)
    * Keywords: `add_tag`, `delete_tag`, `unassign`, `update_name`, `update_assigned_to_v2`, `update_description`, `update_status`
        - `_payload/__init__.py`
        - `_payload/_incidents.py`
        - `incidents.py` (_perform_incident_action_ method)

## Other
+ Fixed: Docstring typo in sort options for `query_accounts` and `query_logins` methods within the Discover Service Class.
    - `discover.py`
+ Fixed: Docstring typo not listing `id` requirements for keyword submissions to the `indicator_update` method within the IOC Service Class.
    - `ioc.py`
+ Fixed: Docstring typo listing an incorrect return type for the `get_download` operation within the ReportExecutions Service Class.
    - `report_executions.py`
+ Fixed: Docstring typo in Real Time Response Service Class referencing non-existent `action_parameters` payload element.
    - `real_time_response.py`
+ Added: Babel fish operation ID to endpoint translator.
    - `util/babel_fish.py`
+ Added: FalconPy terminal word search utility.
    - `util/find-strings.sh`
+ Added: FalconPy module listing utility.
    - `util/public-modules.sh`
+ Added: FalconPy version check utility.
    - `util/vcheck.sh`

---

# Version 1.0.10
## Added features and functionality
+ Added: New versions of two operations within the Real Time Response Service Class. `list_files_v2` and `delete_file_v2` are used the same as the original methods, but provide more results detail. You should leverage `delete_file_v2` if you are retrieving files using `list_files_v2`.
    - `_endpoint/_real_time_response.py`
    - `real_time_response.py`
    - `tests/test_real_time_response.py`

---

# Version 1.0.9
## Added features and functionality
+ Added: New Discover service collection endpoints, matching Service Class operations and unit testing.
    * New method: _`get_accounts`_
    * New method: _`get_logins`_
    * New method: _`query_accounts`_
    * New method: _`query_logins`_
    - `_endpoint/_discover.py`
    - `discover.py`
    - `tests/test_discover.py`

## Other
+ Fixed: Docstring typo for the `combinedQueryVulnerabilities` operation within the Spotlight Vulnerabilities Service Class. Closes #608.
    - `spotlight_vulnerabilities.py`

---

# Version 1.0.8
## Added features and functionality
+ Added: Spotlight Evaluation Logic Service Class, related service collection endpoints and related unit tests.
    - `_endpoint/__init__.py`
    - `_endpoint/_spotlight_evaluation_logic.py`
    - `__init__.py`
    - `spotlight_evaluation_logic.py`
    - `tests/test_spotlight_evaluation_logic.py`

---

# Version 1.0.7
## Issues resolved
+ Fixed: Invalid empty payload sent by `report_executions_download_get` operation when leveraging the Uber Class. Closes #596.
    - `_util.py`
    - `api_complete.py`
    - `tests/test_uber_api_complete.py`
    - Thanks to @tsullivan06 for his assistance in identifying this issue!

## Other
+ Fixed: Typo in docstring - cspm_registration.py#571, `recurring` -> `reoccurring`.  Closes #592.
    - `cspm_registration.py`
+ Added: Updated docstring to reflect newly available host actions. Closes #585.
    - `hosts.py`

---

# Version 1.0.6
## Added features and functionality
+ Added: Return headers on failed authorization (401) when using the Uber class. Closes #578.
    - `_util.py`
    - `api_complete.py`
    - Thank you to @tsullivan06 for this enhancement suggestion!
+ Added: Allow dashed base url specifiers when creating instances of any class. Closes #580.
    - `_util.py`
    - Thanks to @jhseceng for this enhancement suggestion!

## Issues resolved
+ Fixed: Bandit false positive introduced by changes to hard-coded password scanning in v1.7.3. Relates to PyCQA/bandit#843.
    - `_token_fail_reason.py`
    - `api_complete.py`
    - `oauth2.py`

## Other
+ Updated: Docstrings updated to reflect newly available platform names (`android`, `iOS`). Closes #582.
    - `prevention_policy.py`

---

# Version 1.0.5
## Added features and functionality
+ Added: Argument check in `update_detects_by_ids` (UpdateDetectsByIdsV2). When only a `comment` keyword is provided, `show_in_ui` is appended to the request with a `True` value, which satisfies update requirements.
    - `detects.py`
    - `tests/test_detects.py`
+ Added: Default value of `0` for `sequence_id` keyword in `check_command_status`, `check_active_responder_command_status` and `check_admin_command_status` methods within Real Time Response Service Classes.
    - `real_time_response.py`
    - `real_time_response_admin.py`
+ Added: Publicly exposed `confirm_base_region`, `confirm_base_url` methods and `BaseURL` enumerator.
    - `__init__.py`

## Issues resolved
+ Fixed: Missing alias for `api_preempt_proxy_post_graphql` (Operation ID syntax) in Identity Protection Service Class. Closes #567.
    - `identity_protection.py`
    - Thanks to @tsullivan06 for identifying and reporting this issue!
+ Fixed: Incorrect variable used for dictionary key on boolean values within `command_payload` body payload handler. Closes #568.
    - `_payload/_real_time_response.py`
    - Relates to discussion [#415](https://github.com/CrowdStrike/falconpy/discussions/415)

---

# Version 1.0.4
## Added features and functionality
+ Added: Token renewal window customization. Developers may now customize the length of time between token expiration and token renewal. (Max: 20 minutes)
    ```python
    from falconpy import APIHarness
    from falconpy import OAuth2

    uber = APIHarness(client_id="CLIENT_ID", client_secret="CLIENT_SECRET", renew_window=300)
    service = OAuth2(client_id="CLIENT_ID", client_secret="CLIENT_SECRET", renew_window=60)
    ```
    - `_service_class.py`
    - `api_complete.py`
    - `oauth2.py`
    - `tests/test_authentications.py`
    - Thank you to @tsullivan06 for this contribution!

+ Added: Error handling for when calling `query_vulnerabilities_combined` (combinedQueryVulnerabilities) without specifying a `filter` argument. (Must be present as a keyword or as part of the `parameters` dictionary.)
    - `spotlight_vulnerabilities.py`
    - `tests/test_spotlight_vulnerabilities.py`
    - Thank you to @tsullivan06 for this contribution!

+ Added: Export of `ServiceClass` generic base class as part of `__all__` within `__init__.py`. This change will allow developers to inherit from the Service Class base class without importing a protected module (which generates a warning in some editors).
    ```python
    from falconpy import ServiceClass
    ```
    - `__init__.py`
    - Thank you to @morcef for this contribution!

## Issues resolved
+ Fixed: Authentication issue when provided a base_url containing a trailing backslash.
    - `_util.py`
    - `tests/test_authorizations.py`
    - Thanks to @mwb8 for identifying and reporting this issue!

---

# Version 1.0.3
## Issues resolved
+ Fixed: Bug in `process_service_request` (`_util.py`) impacting the `partition` keyword argument of the `refresh_active_stream` method in the Event Streams Service Class. Closes #547.
    - `_util.py`
    - `tests/test_event_streams.py`
    - Thanks go out to @kra-ts for contributing this fix!

---

# Version 1.0.2
## Added features and functionality
+ Added: New _queryCombinedSensorUpdateKernels_ and _querySensorUpdateKernelsDistinct_ operations. (**SensorUpdatePolicy Service Class, Uber Class**)
    - `_endpoint/_sensor_update_policies.py`
    - `_util.py`
    - `_version.py`
    - `api_complete.py`
    - `sensor_update_policy.py`
    - `tests/test_sensor_update_policy.py`
    - `tests/test_uber_api_complete.py`


---

# Version 1.0.1
## Issues resolved
+ Fixed: Parameter abstraction handling issue with the `organization_ids` keyword of the `delete_aws_account` and `get_aws_account` methods within the CSPMRegistration Service Class. Closes #539.
    - `cspm_registration.py`
    - `tests/test_cspm_registration.py`

---

# Version 1.0.0
**Stable Release**

## Other
+ Updated: Author information, `AUTHORS.md`
+ Updated: Contributor documentation, `CONTRIBUTING.md`
+ Formatting: Code of Conduct, `CODE_OF_CONDUCT.md`
+ Updated: Documentation primer, `docs/README.md`
+ Updated: Package metadata and classifiers, `setup.py`
+ Updated: Package information and repository overview, `README.md`
+ Updated: Pull Request template, `.github/pull_request_template.md`
+ Updated: Samples documentation, `samples/README.md`
+ Updated: Security Policy, `SECURITY.md`
+ Updated: Support documentation, `SUPPORT.md`
+ Added: Unit testing documentation, `tests/README.md`
+ Updated: Utilities documentation, `util/README.md`
+ Fixed: Minor comment typo in Offset vs. Token sample, `samples/hosts/offset_vs_token.py`

---

# Version 0.9.0
**Release Candidate**

## Added features and functionality
+ Added: Token generation failure reason tracking to Service and Uber classes. Closes #501.
    - `_service_class.py`
    - `api_complete.py`
    - `oauth2.py`

    **Example usage**
    ```python
    from falconpy import Detects

    detects = Detects(client_id="bad ID", client_secret="bad secret")
    if detects.token_status != 201:
        print(detects.token_fail_reason)
    ```

## Issues resolved
+ Fixed: Code hint warning in PyCharm for missing auth_object definition within _service_class.py.


---

# Version 0.8.11
## Added features and functionality
+ Added: FileVantage Service Class and all related endpoints.
    - `_endpoint/_filevantage.py`
    - `_endpoint/__init__.py`
    - `filevantage.py`
    - `tests/test_filevantage.py`

---

# Version 0.8.10
## Added features and functionality
+ Added: MessageCenter Service Class and all related endpoints.
    - `_endpoint/_message_center.py`
    - `_endpoint/__init__.py`
    - `_payload/_message_center.py`
    - `_payload/__init__.py`
    - `message_center.py`
    - `__init.py__`
    - `tests/test_message_center.py`
    - `.github/wordlist.txt`

## Issues resolved
+ Fixed: Argument passed to a keyword argument only method error handling.
    - `_util.py`
    - `tests/test_hosts.py`
+ Fixed: Added non-keyword argument handler for `get_sample` method.
    - `sample_uploads.py`

## Other
+ Updated: Minor linting adjustments.
    - `sample_uploads.py`
    - `tests/test_overwatch_dashboard.py`
    - `tests/test_prevention_policy.py`
+ Updated: README files updated to reflect new service collection.


---

# Version 0.8.9
## Added features and functionality
+ Added: New operations (GetBehaviorDetections, GetConfigurationDetections) to both the CSPMRegistration Service Class and the Uber Class. Closes #482.
    - `_endpoint/_cspm_registration.py`
    - `cspm_registration.py`
    - `tests/test_cspm_registration.py`

---

# Version 0.8.8
## Issues resolved
+ Fixed: Added missing payload parameters to body payload handler for `update_policy_settings` method (UpdateCSPMPolicySettings operation) within the CSPMRegistration Service Class. Closes #473.
    - `cspm_registration.py`
    - `_payload/_cspm_registration.py`
    - `tests/test_cspm_registration.py`

---

# Version 0.8.7
## Issues resolved
+ Fixed: Stemmed vs. exact comparison for endpoint operation lookup within `args_to_params` method. Closes #467.
    - `_util.py`

---

# Version 0.8.6
## Added features and functionality
+ Added: Cloud Region Autodiscovery - Automatically select the correct cloud region for _US1_, _US2_ and _EU1_ users.
    - When using a _valid_ login for _US1_, _US2_, and _EU1_, developers will no longer need to specify `base_url` when creating an instance of any Service Class, or the Uber Class.  Upon successful login, your correct region will be identified and used for all subsequent requests.  If you specify the wrong region for your instance, this will be corrected as part of authentication.
    - `_base_url.py`
    - `_util.py`
    - `_service_class.py`
    - `api_complete.py`
    - `oauth2.py`
    - `test_authentications.py`
    - `test_authorization.py`
    - All unit testing workflows updated to leverage new cross-region testing parameters.
> Please note: This functionality does __not__ support the GovCloud region or GovCloud API credentials.

---

# Version 0.8.5
## Issues resolved
+ Fixed: Issue when passing comma-delimited strings or boolean values as keywords to the body payload handler for `indicator_object`. Closes #447.
    - `_payload/_ioc.py`
    - `tests/test_ioc.py`
+ Fixed: Issue when passing comma-delimited string for the `groups` keyword to the body payload handler for `ioa_exclusion_payload`. Closes #448.
    - `_payload/_ioa.py`
    - `tests/test_ioa_exclusions.py`
+ Fixed: Issue when passing comma-delimited string for the `ids` keyword to the body payload handler for `update_detects_payload`. Resolved boolean handling of `show_in_ui` keyword. Closes #449.
    - `_payload/_detects.py`
    - `tests/test_detects.py`
+ Fixed: Issue when passing comma-delimited string for `user_tags` keyword to the body payload handler for `submit`. Closes #450.
    - `_payload/_falconx.py`
    - `tests/test_falconx_sandbox.py`
+ Fixed: Issue when passing comma-delimited string for `role_ids` keyword to the body payload handler for Flight Control POST / PATCH operations. Closed #451.
    - `_payload/_mssp.py`
    - `tests/test_mssp.py`
+ Fixed: Issue when passing comma-delimited strings or boolean False to certain keywords within the `command_payload` body payload handler. Closes #452.
    - `_payload/_real_time_response.py`
    - `tests/test_real_time_response.py`
+ Fixed: Issue when passing comma-delimited strings to MalQuery Service Class body payload handlers. Closes #453.
    - `_payload/_malquery.py`
    - `tests/test_malquery.py`
+ Fixed: Issue with passing comma-delimited string for `recipients` within body payload handler for `update_action` method within Recon Service Class. Closes #454.
    - `_payload/_recon.py`
    - `tests/test_recon.py`
+ Fixed: Issue with passing comma-delimited strings for `rule_ids` and `rule_versions` keywords within FirewallManagement Service Class body payload handlers. Closes #455.
    - `_payload/firewall.py`
    - `tests/test_firewall_management.py`
+ Fixed: Issue with passing comma-delimited string for the `groups` keyword within the generic exclusion body payload handler. Closes #456.
    - `_payload/_generic.py`
    - `tests/test_ml_exclusions.py`

---

# Version 0.8.4
## Issues resolved
+ Fixed: TypeError when using a valid credential in the wrong cloud environment. (GOV -> US1 only). Closes #433.
    - `oauth2.py`
    - `test_authentications.py`
    - Gratz to @tsullivan06 for his assistance in identifying and resolving this issue.
+ Fixed: Missing method aliases in OAuth2 Service Class. Closes #432.
    - `oauth2.py`
    - Kudos to @tsullivan06 for identifying this issue.
+ Fixed: Docstring typos in Custom IOA Service Class source.
    - `custom_ioa.py`

---

# Version 0.8.3
## Added features and functionality
+ Added: MSSP Direct Authentication - Additional authentication keyword is now available, `member_cid`, allowing developers targeting MSSP functionality to make use of Direct Authentication as opposed to still using Credential Authentication. This functionality is supported in all Service Classes and the Uber Class.
    - `_service_class.py`
    - `api_complete.py`
    - `oauth2.py`
    - `tests/test_authorization.py`

---

# Version 0.8.2
## Issues resolved
+ Fixed: Issue in `_util.args_to_params` when handling Python reserved words defined as keys incorrectly in the parameter dictionary. Closes #422.
    - Special thanks to @valerianrossigneux for originally identifying this issue, and his assistance testing a fix. :bow:

---

# Version 0.8.1
## Added features and functionality
+ Added: New Discover Service Class and matching unit testing to represent the recently released Falcon Discover API.
    - `discover.py`
    - `_endpoint/_discover.py`
    - `_endpoint/_deprecated/discover.py`
    - `tests/test_discover.py`
+ Added: New generic body payload handler for report execution / scheduling payloads.
    - `_payload/_reports.py`
+ Added: New `report_executions_retry` method and matching unit tests to ReportExecutions Service Class.
    - `report_executions.py`
    - `_endpoint/_report_executions.py`
+ Added: New `scheduled_reports_launch` method and matching unit tests to ScheduledReports Service Class.
    - `scheduled_reports.py`
    - `_endpoint/_scheduled_reports.py`


---

# Version 0.8.0
## Added features and functionality
+ Added: Parameter abstraction for the Uber Class.
    * Provides: Query string parameter payload abstraction for calls made using the Uber class.
    - `api_complete.py`
    - `_util.py`
+ Added: PEP-8 friendly `app_id` keyword for the `appId` parameter used by methods within the EventStreams Service Class.
    - `event_streams.py`

## Issues resolved
+ Fixed: Aggregate payload datatype mismatches in Recon Service Class methods.
    - `recon.py`
+ Fixed: Missing payload parameter in recon rule payload handler.
    - `_payload/_recon.py`
+ Fixed: Invalid query string parameter referenced in body payload handler for `query_sample` method within FalconXSandbox Service Class. Also resolved matching invalid docstring reference. Closes #409.
    - `falconx_sandbox.py`
+ Fixed: Minor formatting issues within docstrings in all package files.

## Other
+ Added: Docstring syntax validation workflow leveraging pydocstyle.
+ Removed: Deprecated `calc_url_from_args` method
    - `_util.py`
+ Removed: Deprecated `parse_id_list` method
    - `_util.py`


---

# Version 0.7.4
## Added features and functionality
+ Updated: Service Class Refactoring (Rev 4) 
    * Provides: Body Payload Abstraction - Abstracted BODY payload parameters for all methods using PATCH, POST or PUT requests into keywords. Legacy usage pattern of passing the BODY payload directly as the _body_ keyword is still supported. 
    * Provides: PEP-257 formatting of all docstrings.
    - `cspm_registration.py` - Closes #394
    - `device_control_policies.py` - Closes #396
    - `falconx_sandbox.py` - Closes #397
    - `mssp.py` - Closes #398
    - `kubernetes_protection.py` - Closes #399
    - `custom_ioa.py` - Closes #400
    - `falcon_complete_dashboard.py` - Closes #401
    - `firewall_policies.py` - Closes #402
    - `firewall_management.py` - Closes #403


---

# Version 0.7.3
## Added features and functionality
+ Added: New combinedQueryVulnerabilities operation to SpotlightVulnerabilities Service Class.
    - `spotlight_vulnerabilities.py` - Service Class
    - `_endpoint/_spotlight_vulnerabilities.py` - Endpoint module
    - `tests/test_spotlight_vulnerabilities.py` - Unit testing
+ Updated: Service Class Refactoring (Rev 4) 
    * Provides: Body Payload Abstraction - Abstracted BODY payload parameters for all methods using PATCH, POST or PUT requests into keywords. Legacy usage pattern of passing the BODY payload directly as the _body_ keyword is still supported. 
    * Provides: PEP-257 formatting of all docstrings.
    - `cloud_connect_aws.py` - Closes #386
    - `d4c_registration.py` - Closes #391
    - `ioc.py` - Closes #388
    - `iocs.py` - Closes #387
    - `identity_protection.py` - Closes #385
    - `incidents.py` - Closes #390
    - `overwatch_dashboard.py` - Closes #389
    - `real_time_response.py` - Closes #383
    - `real_time_response_admin.py` - Closes #384
    - `response_policies.py` - Closes #382


---

# Version 0.7.2
## Issues resolved
+ Fixed: Missing body payload in CloudConnectAWS.verify_aws_account_access. Closes #376.


---

# Version 0.7.1
## Added features and functionality
+ Updated: Service Class Refactoring (Rev 4) 
    * Provides: Body Payload Abstraction - Abstracted BODY payload parameters for all methods using PATCH, POST or PUT requests into keywords. Legacy usage pattern of passing the BODY payload directly as the _body_ keyword is still supported. 
    * Provides: PEP-257 formatting of all docstrings.
    - `host_group.py` - Closes #361
    - `ioa_exclusions.py` - Closes #359
    - `installation_tokens.py` - Closes #363
    - `ml_exclusions.py` - Closes #360
    - `prevention_policy.py` - Closes #364
    - `quarantine.py` - Closes #366
    - `sensor_update_policy.py` - Closes #368
    - `user_management.py` - Closes #367
+ Added: Class aliases for Sensor Update Policies and Prevention Policies service collections to provide classes that align to plural naming convention.

## Issues resolved
+ Fixed: Hard-coded user-agent header for all requests. Moving forward, developers may specify a custom string to be used as the User-Agent header for all requests. Closes #365.
    ```python
    from falconpy import Hosts
    falcon = Hosts(client_id="CLIENT_ID_HERE",
                   client_secret="CLIENT_SECRET_HERE",
                   user_agent="company-product/version"
                   )
    result = falcon.query_devices_by_filter_scroll()
    print(result)
    ```

---

# Version 0.7.0
## Added features and functionality
+ Added: Updated `__all__` parameter in root `__init__.py`, publishing all PEP8 class names. This change allows developers to import these classes directly.
    ```python
    from falconpy import Hosts
    falcon = Hosts(client_id="CLIENT_ID_HERE", client_secret="CLIENT_SECRET_HERE")
    result = falcon.query_devices_by_filter()
    print(result)
    ```
+ Added: Private Base URL enum. `_base_url.py`
    - You may now specify your base URL by name or by URL.
        + US1
        + US2
        + USGOV1
        + EU1
+ Added: Default value for _action_name_ parameter in __refresh_active_stream__ method of EventStreams service class. `event_streams.py`
+ Added: Payload handling sub-module. `_payload/`
    - `_payload/__init__.py`
    - `_payload/_detects.py`
    - `_payload/generic.py`
    - `_payload/malquery.py`
    - `_payload/recon.py`
+ Updated: Service Class Refactoring (Rev 4) 
    * Provides: Body Payload Abstraction - Abstracted BODY payload parameters for all methods using PATCH, POST or PUT requests into keywords. Legacy usage pattern of passing the BODY payload directly as the _body_ keyword is still supported. 
    * Provides: PEP-257 formatting of all docstrings.
    - `detects.py` - Closes #353.
    - `event_streams.py` - Closes #349
    - `falcon_container.py` - Closes #348
    - `hosts.py` - Closes #340.
    - `intel.py` - Closes #352
    - `malquery.py` - Closes #354
    - `quick_scan.py` - Closes #351
    - `recon.py` - Closes #350
    - `report_executions.py` - Closes #346
    - `sample_uploads.py` - Closes #344
    - `scheduled_reports.py` - Closes #345
    - `sensor_download.py` - Closes #343
    - `sensor_visibility_exclusions.py` - Closes #347
    - `spotlight_vulnerabilities.py` - Closes #342
    - `zero_trust_assessment.py` - Closes #341
+ Updated: Endpoint module updated to reflect recent swagger changes.
    - `_cspm_registration.py`
    - `_mssp.py`

## Issues resolved
+ Updated: Linter updates now result in usage of `format` being marked as a failure for scenarios where an `f-string` can be used. Updated all occurrences of this issue to make use of `f-string` formatting.
    - `_service_class.py`
    - `_util.py`
    - `api_complete.py`
    - `oauth2.py`

## Other
+ Updated: PEP-257 syntax applied to all docstrings in all touched files.
+ Updated: README.md updated

---

# Version 0.6.5
## Issues resolved
+ Removed: Hash Analyzer Service Class and all related unit tests. (Unavailable at this time)
    - `hash_analyzer.py`
    - `_endpoint/_hash_analyzer.py`
    - `test_hash_analyzer.py`
+ Fixed: Missing reference to _quarantine_endpoints in endpoint module.  `_endpoint/__init__.py`
    - This issue only impacted users leveraging the Uber class for these endpoints.

---

# Version 0.6.4
## Added features and functionality
+ Added: New Hash Analyzer Service Class `hash_analyzer.py`
    - Related unit tests `test_hash_analyzer.py`
    - Related endpoint module `_hash_analyzer.py`
+ Added: Quarantine Service Class unit tests `test_quarantine.py`

---

# Version 0.6.3
## Added features and functionality
+ Added: New FalconContainer Service Class. `falcon_container.py`
+ Added: Two new methods (operations)) to the Hosts Service Class. `hosts.py`
    - query_device_login_history / QueryDeviceLoginHistory
    - query_network_address_history / QueryGetNetworkAddressHistoryV1
+ Added: New method (operation)) to the SpotlightVulnerabilities Service Class. `spotlight_vulnerabilities.py`
    - get_remediations_v2 - getRemediationsV2
+ Migrated: Ported still viable methods from legacy IOCS Service Class `iocs.py` to the new IOC Service Class. `ioc.py`
    - devices_count / DevicesCount
    - devices_ran_on / DevicesRanOn
    - processes_ran_on / ProcessesRanOn
    - entities_processes / entities_processes
+ Updated: Deprecated 5 methods within the legacy IOCS Service Class. `iocs.py`
    - get_ioc / GetIOC
    - create_ioc / CreateIOC
    - delete_ioc / DeleteIOC
    - update_ioc / UpdateIOC
    - query_iocs / QueryIOCs
+ Updated: Deprecated cs_username keyword from all methods within CustomIOA and FirewallManagement Service Classes. `custom_ioa.py`, `firewall_management.py`
+ Added: New Quarantine Service Class and endpoints. `quarantine.py`
+ Updated: Updated endpoint for getComplianceV1 operation within ZeroTrustAssessment Service Class. `zero_trust_assessment.py`

---

# Version 0.6.2
## Issues resolved
+ Bug fix: Fixed Uber class passing empty **ids** parameter array when no _ids_ had been provided to the command method. Closes #314. `_util.py`

---

# Version 0.6.1
## Issues resolved
+ Bug fix: Fixed bad comparison for endpoint lookups when using Service Classes. Closes #305. `_util.py`
+ Bug fix: Fixed typo in operation ID for query_platforms method within CustomIOA Service Class. Closes #307. `custom_ioa.py`
+ Bug fix: Fixed typo in operation ID for create_user_groups method within FlightControl Service Class. Closes #308. `mssp.py`

---

# Version 0.6.0
## Added features and functionality
+ Refactored Cloud Connect AWS Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #271. `cloud_connect_aws.py`
+ Refactored CSPM Registration Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #272. `cspm_registration.py`
+ Refactored Custom IOA Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #258. `custom_ioa.py`
+ Refactored D4C Registration Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #273. `d4c_registration.py`
+ Refactored Detects Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #274. `detects.py`
+ Refactored Device Control Policies Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #275. `device_control_policies.py`
+ Refactored Events Streams Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #248. `event_streams.py`
+ Refactored Falcon Complete Dashboard Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #294. `falcon_complete_dashboard.py` 
+ Refactored Falcon Flight Control Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #292. `mssp.py`
+ Refactored Falcon X Sandbox Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #259. `falconx_sandbox.py`
+ Refactored Firewall Management Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #257. `firewall_management.py`
+ Refactored Firewall Policies Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #296. `firewall_policies.py`
+ Refactored Hosts Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #269. `hosts.py` 
+ Refactored Host Group Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #286. `host_group.py` 
+ Refactored Identity Protection Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #299. `identity_protection.py` 
+ Refactored Incidents Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #289. `incidents.py`
+ Refactored Installation Tokens Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #287. `installation_tokens.py` 
+ Refactored Intel Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #264. `intel.py`
+ Refactored IOA Exclusions Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #283. `ioa_exclusions.py`
+ Refactored IOC Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #267. `ioc.py` 
+ Refactored IOCs Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #284. `iocs.py`
+ Refactored Kubernetes Protection Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #293. `kubernetes_protection.py` 
+ Refactored MalQuery Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #298. `malquery.py` 
+ Refactored ML Exclusions Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #281. `ml_exclusions.py`
+ Refactored Overwatch Dashboard Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #278. `overwatch_dashboard.py`
+ Refactored Prevention Policy Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #290. `prevention_policy.py`
+ Refactored Quick Scan Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #282. `quick_scan.py`
+ Refactored Real Time Response Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #280. `real_time_response.py`
+ Refactored Real Time Response Admin Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #256. `real_time_response_admin.py`
+ Refactored Recon Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #297. `recon.py` 
+ Refactored Response Policies Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #295. `response_policies.py`
+ Refactored Sample Uploads Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #255. `sample_uploads.py`
+ Refactored Sensor Download Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #285. `sensor_download.py`
+ Refactored Sensor Update Policy Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #288. `sensor_update_policy.py`
+ Refactored Sensor Visibility Exclusions Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #279. `sensor_visibility_exclusions.py`
+ Refactored Spotlight Vulnerabilities Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #277. `spotlight_vulnerabilities.py`
+ Refactored User Management Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #276. `user_management.py`
+ Refactored Zero Trust Assessment Service Class to the latest pattern (rev 3), aligns syntax to PEP8. Closes #260. `zero_trust_assessment.py`

+ Added client_id and client_secret as keywords to the base Service Class, Uber Class, and Authentication class. `api_complete.py`, `oauth2.py`, `_service_class.py`

    > This change allows you to specify your API ID and secret when you create an instance of any of the service class. (Direct Authentication)
    ```python
    from falconpy.hosts import Hosts
    falcon = Hosts(client_id="CLIENT_ID_HERE", client_secret="CLIENT_SECRET_HERE")
    results = falcon.query_devices_by_filter(sort="devices.hostname|desc", limit=10)
    print(results)
    ```

+ Added _new_ Report Executions Service Class. `report_executions.py`
    - Basic unit test implemented: `test_report_executions.py`
+ Added _new_ Schedule Reports Service Class. `scheduled_reports.py`
    - Basic unit test implemented: `test_scheduled_reports.py`

+ Added new operation (getComplianceV1) to Zero Trust Assessment Service Class. `zero_trust_assessment.py`

## Issues resolved
+ Bug fix: Resolved HTTP status code 415 on calls to refreshActiveStreamSession (refresh_active_stream). Closes #247. `event_streams.py`
+ Bug fix: Resolved header pollution issue within Falcon X Sandbox Service Class. Closes #250. `falconx_sandbox.py`
+ Bug fix: Resolved header pollution issue within Firewall Management Service Class. Closes #252. `firewall_management.py`
+ Bug fix: Resolved header pollution issue within Custom IOA Service Class. Closes #253. `custom_ioa.py`
+ Bug fix: Resolved header pollution issue within Sample Uploads Service Class. Closes #254. `sample_uploads.py`
+ Bug fix: Resolved HTTP status code 500 error on calls to RTR_CreatePut_Files (create_put_files). Closes #261. `real_time_response_admin.py`
+ Bug fix: Resolved HTTP status code 400 or 500 error on calls to RTR_UpdateScripts (update_scripts) and calls to RTR_CreateScripts (create_scripts). Closes #262. `real_time_response_admin.py`
+ Bug fix: Added handle_single_argument helper to attempt to handle single arguments passed to Service Class methods. Addresses a potential breaking change introduced by v0.5.4. Closes #263. `_util.py` 

    > Developers should use keywords, __not arguments__, when specifying parameters provided to Service Class or the Uber Class command methods.
    #### Example
    ```python
    from falconpy.hosts import Hosts
    falcon = Hosts(creds={"client_id": "CLIENT_ID_HERE", "client_secret": "CLIENT_SECRET_HERE"})

    result = falcon.GetDeviceDetails(ids="12345"))   # This syntax will always work
    print(result)
    result = falcon.GetDeviceDetails("12345")        # This syntax may fail depending on method
    print(result)                                    # (will work in this example)
    bad_result = falcon.QueryHiddenDevices(1, 0, "devices.hostname|desc", "")
    print(bad_result)                                # This syntax will always fail
    ```
    > Whenever possible, Service Classes attempt to guess the keyword for the first argument passed (if present). Typically these are aligned to the one required parameter for the method. (_Example: the **ids** parameter_)
+ Related to #263: Updated Uber class to no longer leverage the force_default helper, allowing users to still use the first argument to specify the action to be performed. `api_complete.py`
+ Bug fix: Added the **after** parameter to the endpoint parameter definitions for _indicator_combined_v1_ and _indicator_search_v1_. Closes #266. `_endpoint/_ioc.py`
+ Bug fix: Multiple methods within the Flight Control Service Class make use of the wrong HTTP method. Closes #291. `mssp.py`

## Other
+ Initial refactoring of unit test harnesses for service classes detailed above.
+ Reduced token-related API requests performed by unit testing series.
+ Minor adjustment to Uber class unit tests to better demonstrate proper method usage.
+ Updated unit tests to support US-2 / Gov base URL testing.

---

# Version 0.5.6
## Added features and functionality
+ Added: New functionality for handling service class modules within FalconDebug.

## Issues resolved
+ Bug fix: Resolved JSONDecode error on RTR_DeleteSession. Closes #238.
+ Bug fix: Resolved issue with credential authentication in service classes not respecting custom API configuration attributes. Closes #242. 

## Other
+ Package metadata updates
+ Updated IDP unit tests to more accurately cover functionality
+ Flaky unit test adjustments
+ FalconDebug added to linting workflows `debug.py`

---

# Version 0.5.5
## Added features and functionality
+ Refactored Custom IOA Service Class to the new pattern to provide for new parameter handling functionality, closes #217. `custom_ioa.py`
+ Refactored Device Control Policies Service Class to the new pattern to provide for new parameter handling functionality, closes #224. `device_control_policies.py`
+ Refactored Firewall Policies Service Class to the new pattern to provide for new parameter handling functionality, closes #227. `firewall_policies.py`
+ Refactored Firewall Management Service Class to match the most recent pattern, closes #232. `firewall_management.py`
+ Refactored Falcon X Sandbox Service Class to the new pattern to provide for new parameter handling functionality, closes #226. `falconx_sandbox.py`
+ Refactored Hosts Service Class to the new pattern to provide for new parameter handling functionality, closes #218. `hosts.py`
+ Refactored Host Group Service Class to the new pattern to provide for new parameter handling functionality, closes #223. `host_group.py`
+ Refactored Intel Service Class to match the most recent pattern, closes #231. `intel.py`
+ Refactored OAuth2 class to reflect new functionality and linting patterns, closes #233. `oauth2.py`
+ Refactored Quick Scan Service Class to match the most recent pattern, closes #219. `quick_scan.py`
+ Refactored Real Time Response Service Class to match the most recent pattern, closes #230. `real_time_response.py`
+ Refactored Real Time Response Admin Service Class to match the most recent pattern, closes #229. `real_time_response_admin.py`
+ Refactored Sensor Updated Policy Service Class to the new pattern to provide for new parameter handling functionality, closes #222. `sensor_update_policy.py`
+ Refactored Sensor Downloads Service Class to the new pattern to provide for new parameter handling functionality, closes #221. `sensor_downloads.py`
+ Refactored Sample Uploads Service Class to the new pattern to provide for new parameter handling functionality, closes #220. `sample_uploads.py`
+ Refactored User Management Service Class to match the most recent pattern, closes #228. `user_management.py`

## Issues resolved
+ Bug fix: Resolved issue with the timeout parameter not being passed to the OAuth2 class when legacy authentication was being used. Closes #225.

## Other
+ Enabled Pylint stopping the build on linting failures within package source.
+ Unit test updates to expand code coverage for new code paths.
+ This update provides part of the functionality requested in #115.

---

# Version 0.5.4
## Added features and functionality
+ Added `identity_protection.py` - Identity Protection service class.
+ Added utility to create a zip archive to be used with AWS Lambda layers. (`create-lambda-layer.sh`)

## Issues resolved
+ Bug fix: Resolved order of operations issue with body validation in __validate_payload__ helper function. (`_util.py`)
+ Updated `cloud_connect_aws.py` - Cloud_Connect_AWS Service Class. Closes #209.
+ Updated `detects.py` - Detects Service Class. Closes #210.
+ Updated `event_streams.py` - Event Streams Service Class. Closes #212.
+ Updated `incidents.py` - Incidents Service Class. Closes #213.
+ Updated `spotlight_vulnerabilities.py` - Spotlight Vulnerabilities Service Class. Closes #214.
+ Updated `zero_trust_assessment.py` - Zero Trust Assessment Service Class. Closes #211.
+ Updated query used for unit testing of Spotlight Vulnerabilities service class. 2020 -> 2021 (`test_spotlight_vulnerabilities.py`)
+ Bug fix: Resolved flaky unit test for RegenerateAPIKey for Kubernetes Protection service class. (`test_kubernetes_protection.py`).

## Other
+ Added pylint workflow to push / pull_request actions.
+ _endpoint module updates to support new service class.
+ Added unit testing for new service class.
+ Unit testing updates to complete code coverage.
+ README.md updated.
+ Added additional classifiers and developer requirements to PIP package metadata. (`setup.py`)

---

# Version 0.5.3
## Issues resolved
+ Bug fix: Resolves #200 by moving the failing method (entities_processes) in `iocs.py` to the latest code pattern.

---

# Version 0.5.2
## Issues resolved
+ Fixed: Incorrect endpoint specified in the updateSensorUpdatePoliciesV2 method within the Sensor Update Policy service class.

---

# Version 0.5.1
## Issues resolved
+ Fixed: https://github.com/CrowdStrike/falconpy/issues/181 by adding the parameters to the create and update ioc functions.

---

# Version 0.5.0
## Added features and functionality
+ Added: IOC API Service Class (`ioc.py`)
    * indicator_combined_v1
    * indicator_get_v1
    * indicator_create_v1
    * indicator_delete_v1
    * indicator_update_v1
    * indicator_search_v1
+ Added: Kubernetes Protection API Service Class (`kubernetes_protection.py`)
    * GetAWSAccountsMixin0
    * CreateAWSAccount
    * DeleteAWSAccountsMixin0
    * UpdateAWSAccount
    * GetLocations
    * GetHelmValuesYaml
    * RegenerateAPIKey
    * GetClusters
    * TriggerScan
+ Added: Recon API Service Class (`recon.py`)
    * AggregateNotificationsV1
    * PreviewRuleV1
    * GetActionsV1
    * CreateActionsV1
    * DeleteActionV1
    * UpdateActionV1
    * GetNotificationsDetailedTranslatedV1
    * GetNotificationsDetailedV1
    * GetNotificationsTranslatedV1
    * GetNotificationsV1
    * DeleteNotificationsV1
    * UpdateNotificationsV1
    * GetRulesV1
    * CreateRulesV1
    * DeleteRulesV1
    * UpdateRulesV1
    * QueryActionsV1
    * QueryActionsV1
    * QueryNotificationsV1
    * QueryRulesV1
+ Added: Response Policies API Service Class (`response_policies.py`)
    * queryCombinedRTResponsePolicyMembers
    * queryCombinedRTResponsePolicies
    * performRTResponsePoliciesAction
    * setRTResponsePoliciesPrecedence
    * getRTResponsePolicies
    * createRTResponsePolicies
    * deleteRTResponsePolicies
    * updateRTResponsePolicies
    * queryRTResponsePolicyMembers
    * queryRTResponsePolicies
+ Updated: CSPM Registration API Service Class (`cspm_registration.py`)
    * Refactored to utilized updated pattern for Service Classes
    * Added: PatchCSPMAwsAccount function
    * Added: UpdateCSPMAzureTenantDefaultSubscriptionID function
    * Added: GetIOAEvents function
    * Added: GetIOAUsers function
    * Updated: Unit tests
+ Updated: Discover for Cloud Registration API Service Class (`d4c_registration.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: IOA Exclusions API Service Class (`ioa_exclusions.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: IOCs API Service Class (`iocs.py`)
    * Refactored to utilized updated pattern for Service Classes
    * Updated: Deprecated multiple endpoints as part of the release of the new IOC Service Class (`_endpoint/_iocs.py`)
+ Updated: Falcon Complete Dashboard API Service Class (`falcon_complete_dashboard.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Falcon Flight Control API Service Class (`mssp.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Installation Tokens API Service Class (`installation_tokens.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Malquery API Service Class (`malquery.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: ML Exclusions API Service Class (`ml_exclusions.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Overwatch Dashboard API Service Class (`overwatch_dashboard.py`)
    * Refactored to remove unnecessary private method call / import of the sys library
+ Updated: Prevention Policies API Service Class (`prevention_policy.py`)
    * Refactored to utilized updated pattern for Service Classes
    * Updated: Added _add-rule-group_ and _remove-rule-group_ actions to __action_name__ parameter for performPreventionPoliciesAction function. (`_endpoint/_prevention_policy.py`)
+ Updated: Sensor Visibility Exclusions API Service Class (`sensor_visibility_exclusions.py`)
    * Refactored to remove unnecessary private method call / import of the sys library

## Other
+ Added: CSPM Registration API sample - CSPM registration policy export (@mccbryan3)

---

# Version 0.4.10
## Added features and functionality
+ Added: Timeout support - Float / tuple that is passed to the requests library when performing
requests to the API. Can specify timeouts for connect, read and global.

## Issues resolved
+ Fixed: Service Class proxy functionality support

## Other
+ Timeout functionality unit tests (`test_timeout.py`)

---

# Version 0.4.9
## Added features and functionality
+ Added: Proxy support - dictionary of proxies that are passed to the requests library when
performing requests to the API.
+ Related to discussion post [#154](https://github.com/CrowdStrike/falconpy/discussions/154)

---

# Version 0.4.8
## Issues resolved
+ Fixed: Parsing issue with __ids__ argument within MSSP.getChildren (Flight Control Service Class)
    * Resolved by migrating `mssp.py` source to the new pattern being tested for Service Classes.
    * Closes [#144](https://github.com/CrowdStrike/falconpy/issues/144)

---

# Version 0.4.7
## Added features and functionality

> New Service Class pattern - Query String parameters can now be passed as function arguments.

> This functionality is currently only available in the following new Service Classes while
> regression testing is underway.

+ Added: D4C Registration API Service Class (`d4c_registration.py`)
    * GetCSPMAzureAccount
    * CreateCSPMAzureAccount
    * UpdateCSPMAzureAccountClientID
    * GetCSPMAzureUserScriptsAttachment
    * GetCSPMAzureUserScripts
    * GetCSPMCGPAccount
    * GetCSPMGCPAccount (redirects to GetCSPMCGPAccount)
    * CreateCSPMGCPAccount
    * GetCSPMGCPUserScriptsAttachment
    * GetCSPMGCPUserScripts
    - Added unit tests (`test_d4c_registration.py`)
+ Added: Installation Tokens API Service Class (`installation_tokens.py`)
    * audit_events_read
    * customer_settings_read
    * tokens_read
    * tokens_create
    * tokens_delete
    * tokens_update
    * audit_events_query
    * tokens_query
    - Added unit tests (`test_installation_tokens.py`)
+ Added: IOA Exclusions API Service Class (`ioa_exclusions.py`)
    * getIOAExclusionsV1
    * createIOAExclusionsV1
    * deleteIOAExclusionsV1
    * updateIOAExclusionsV1
    * queryIOAExclusionsV1
    - Added unit tests (`test_ioa_exclusions.py`)
+ Added: Falcon Complete Dashboard API Service Class (`falcon_complete_dashboard.py`)
    * AggregateAllowList
    * AggregateBlockList
    * AggregateDetections
    * AggregateDeviceCountCollection
    * AggregateEscalations
    * AggregateFCIncidents
    * AggregateRemediations
    * QueryAllowListFilter
    * QueryBlockListFilter
    * QueryDetectionIdsByFilter
    * GetDeviceCountCollectionQueriesByFilter
    * QueryEscalationsFilter
    * QueryIncidentIdsByFilter
    * QueryRemediationsFilter
    - Added unit tests (`test_falcon_complete_dashboard.py`)
+ Added: MalQuery API Service Class (`malquery.py`)
    + GetMalQueryQuotasV1
    + PostMalQueryFuzzySearchV1
    + GetMalQueryDownloadV1
    + GetMalQueryMetadataV1
    + GetMalQueryRequestV1
    + GetMalQueryEntitiesSamplesFetchV1
    + PostMalQueryEntitiesSamplesMultidownloadV1
    + PostMalQueryExactSearchV1
    + PostMalQueryHuntV1
    * Added unit tests (`test_malquery.py`)
+ Added: ML Exclusions API Service Class (`ml_exclusions.py`)
    * getMLExclusionsV1
    * createMLExclusionsV1
    * deleteMLExclusionsV1
    * updateMLExclusionsV1
    * queryMLExclusionsV1
    - Added unit tests (`test_ml_exclusions.py`)
+ Added: Overwatch Dashboard API Service Class (`overwatch_dashboard.py`)
    * AggregatesDetectionsGlobalCounts
    * AggregatesEventsCollections
    * AggregatesEvents
    * AggregatesIncidentsGlobalCounts
    * AggregatesOWEventsGlobalCounts
    - Added unit tests (`test_overwatch_dashboard.py`)
+ Added: Sensor Visibility Exclusions API Service Class (`sensor_visibility_exclusions.py`)
    * getSensorVisibilityExclusionsV1
    * createSVExclusionsV1
    * deleteSensorVisibilityExclusionsV1
    * updateSensorVisibilityExclusionsV1
    * querySensorVisibilityExclusionsV1
    - Added unit tests (`test_sensor_visibility_exclusions.py`)

## Other
+ Added: args_to_params function (`_util.py`) - Allows developers to specify parameter dictionary elements as function arguments
    ### Example
    ```python
    import json
    from falconpy.ml_exclusions import ML_Exclusions as FalconML
    falcon = FalconML(creds={"client_id": client_ID, "client_secret": client_secret})
    print(json.dumps(falcon.queryMLExclusionsV1(limit=10, offset=20, sort="value.asc"), indent=4))
    ```
    - Unrecognized parameter values are discarded
    - Initial testing in a limited number of Service Classes

---

# Version 0.4.6-spotlight-remediations-patch-1
## Added features and functionality
+ Added: Missing method to Spotlight_Vulnerabilities Service Class (`spotlight_vulnerabilities.py`)
    * getRemediations
    - Added unit test to existing test series (`test_spotlight_vulnerabilities.py`)

---

# Version 0.4.6
## Added features and functionality
+ Added: MSSP (Falcon Flight Control) Service Class
    * getChildren
    * getCIDGroupMembersBy
    * addCIDGroupMembers
    * deleteCIDGroupMembers
    * getCIDGroupById
    * createCIDGroups
    * deleteCIDGroups
    * updateCIDGroups
    * getRolesByID
    * addRole
    * deleteRoles
    * getUserGroupMembersByID
    * addUserGroupMembers
    * deleteUserGroupMembers
    * getUserGroupsByID
    * createUserGroup
    * deleteUserGroups
    * updateUserGroups
    * queryChildren
    * queryCIDGroupMembers
    * queryCIDGroups
    * queryRoles
    * queryUserGroupMembers
    * queryUserGroups
    - Added unit tests (`test_mssp.py`)

+ Added: Zero Trust Assessment Service Class
    * getAssessmentV1
    - Added unit tests (`test_zero_trust_assessment.py`)

## Issues resolved
+ Fixed KeyError when providing invalid credentials to a Service Class using Credential
  or Object authentication, Closes [#134](https://github.com/CrowdStrike/falconpy/issues/134)

## Other
+ Moved _endpoint constant library to a private submodule (No impact to existing usage)
    - Added payload parameter information to _endpoint constants
    - Adds service collection ID to endpoint lists
    - This prepares the package for new functionality planned for future releases
+ Added: `force_default` function - decorator function that forces default values for function arguments (`_util.py`)
    - Added: Helper function `get_default`
    - Refactored Uber class to leverage this new functionality
        * Unit tests refactored to cover new code paths (`test_uber_api_complete.py`)
    - Depending upon feedback, this updated pattern will be implemented within Service Classes to reduce overall function complexity
+ Linting
    > Developers: These patterns are being tested within the Uber Class for migration over to Service Classes in future versions
    - Reduced Uber class method complexity
        * Added: Helper function `calc_url_from_args` (`_util.py`)
        * Added: Helper function `_create_header_payload` (`api_complete.py`, Requires class internal variables)
    - Migrated Uber class variables to snake_case format
    - Removed unnecessarily complex lambdas
        * New class method: `valid_cred_format`, replaces previous lambda class attribute
        * New class method: `token_expired`, replaces previous lambda class attribute
    - Reduced overall number of instance attributes
    * Unit tests updated (`test_uber_api_complete.py`)
+ Minor unit test update to `test_cspm_registration.py`
+ Added `util/coverage.config`
    - Moved unit test coverage reporting over to configuration file for parameter management
+ Documentation updates

---

# Version 0.4.5
## Added features and functionality
+ Added: Custom Indicators of Attack (IOA) API Service Class (`custom_ioa.py`)
    * get_patterns
    * get_platformsMixin0
    * get_rule_groupsMixin0
    * create_rule_groupMixin0
    * delete_rule_groupsMixin0
    * update_rule_groupMixin0
    * get_rule_types
    * get_rules_get
    * get_rulesMixin0
    * create_rule
    * delete_rules
    * update_rules
    * validate
    * query_patterns
    * query_platformsMixin0
    * query_rule_groups_full
    * query_rule_groupsMixin0
    * query_rule_types
    * query_rulesMixin0
    - Added unit tests (`test_custom_ioa.py`)

+ Added: Falcon X Quick Scan API Service Class (`quick_scan.py`)
    * GetScansAggregates
    * GetScans
    * ScanSamples
    * QuerySubmissionsMixin0
    - Added unit tests (`test_quick_scan.py`)

+ Added: Uber class endpoints (`_endpoints.py`)
    * Falcon Complete Dashboard API
    * Falcon Overwatch Dashboard API
    * Falcon Flight Control API

## Issues resolved
+ Fixed unidiomatic type check in `_util.py` (_parse_id_list_)
+ Fixed potentially problematic default payload lists and dictionaries (Service Classes and Uber Class)

## Other
+ Added CHANGELOG.md
+ Documentation updates to reflect new service class and upcoming API additions
+ Minor comment updates
+ Adjusted GitHub actions to test operating systems as separate workflows
+ Minor GitHub workflow adjustments
+ Unit test updates
    - Cloud Connect AWS
    - CSPM Registration
    - Sensor Download

---

# Version 0.4.4
## Added features and functionality
+ Added: Sensor Download API Service Class (Contributor: @CalebSchwartz)
    * GetCombinedSensorInstallersByQuery
    * DownloadSensorInstallerById
    * GetSensorInstallersEntities
    * GetSensorInstallersCCIDByQuery
    * GetSensorInstallersByQuery
    - Added unit tests

## Issues resolved
+ Fixed: action_name parameter default bug. Resolved by setting a default value and overriding this value if action_name is present in the parameters dictionary, Closes #114. 

## Other
+ Documentation updated to reflect the new Sensor Download Service Class


---

# Version 0.4.3
## Added features and functionality
+ Added: Sample_Uploads service class (`sample_uploads.py`)
    * UploadSampleV3
    * GetSampleV3
    * DeleteSampleV3
    - Added: Sample_Uploads unit tests (`test_sample_uploads.py`)
+ Added: FalconDebug - Interactive Python3 debugger that provides a pre-defined API token.

## Issues resolved
+ Fixed: Issue with Uber class command method using the action_name variable instead of file_name variable for actions passing the file_name parameter.
+ Fixed: Issue with `setup.py` passing GitHub emoji text to the package description.
+ Fixed: Issue with Uber class unit testing not deleting uploaded files from Sample_Uploads API. (`test_uber_api_complete.py`)


---

# Version 0.4.2
## Added features and functionality
+ Added missing method: `hosts.py` - Added UpdateDeviceTags method to Hosts service class. (Contributor: @rewgord)
    - Unit test added to `test_hosts.py` to test device tagging functionality.
+ API Operation summaries added to the Uber class: `_endpoint.py` - This provides for upcoming functionality that will be announced in future updates.
+ New endpoints added to the Uber class: `_endpoint.py` 

> Deprecation Warning: Legacy API operation IDs that made use of the Python reserved characters "." and "-" have been deprecated. 
> New operation IDs have been generated for each that now aligns to the method names defined in the equivalent service class.

## Issues resolved
+ Added method validation to Uber class calls to the requests library. (HTTP 418 is sent when an invalid method is specified.)

## Other
+ Cleaned up `event_streams.py` class file to match new patterns.
+ Updated return type decorators for service_request and perform_request. (`_util.py`)
+ Updated return type decorators for GetArtifacts, GetReports and GetSampleV2. (`falconx_sandbox.py`)
+ Abstracted all remaining common error output code paths to a stand-alone generic method. (`_util.py`)


---

# Version 0.4.1
## Added features and functionality
+ New service class: cspm_registration.py - Provides the *CSPM_Registration* service class for handling Horizon registration in Azure and AWS.
    - Unit test added
+ Added methods: falconx_sandbox.py - Support for the following operations have been added to the *FalconX_Sandbox* service class.
    * QuerySampleV1
    * DeleteSampleV2
    * GetSampleV2
    * DeleteReport
    * GetReports
    - Unit test added

## Issues resolved
+ Bug fix: Resolved malformed validator in detects.py - UpdateDetectsByIdsV2
+ Bug fix: Added action_name parameter to operations that require the parameter. Closes #53.
  This issue impacted 6 service classes in total:
    - device_control_policies.py - *Device_Control_Policies* - performDeviceControlPoliciesAction
    - firewall_policies.py - *Firewall_Policies* - performFirewallPoliciesAction
    - host_group.py - *Host_Group* - performGroupAction
    - hosts.py - *Host* - PerformActionV2
    - prevention_policy.py - *Prevention_Policy* - performPreventionPoliciesAction
    - sensor_update_policy.py - *Sensor_Update_Policy* - performSensorUpdatePoliciesAction
   
    - This issue also impacted the Uber class, resulting in updates to the command method within the APIHarness class.

    - Unit tests modified

> Breaking Change: The action_name parameter does not currently accept unspecified values. This is resolved in the 0.4.4 version of the package.

## Other
+ Minor updates to `_endpoints.py` to reflect operation ID corrections for the CSPM registration API.
+ Abstracted common error output code paths to a stand-alone method within `_util.py`.


---

# Version 0.4.0
## Added features and functionality
+ Added additional HTTP status codes
+ Added parameter input validation handling
    - Additional validations are planned for all service classes. Currently only enabled in `cloud_connect_aws.py`. 
+ Added body payload input validation handling
    -  Additional validations are planned for all service classes. Currently only enabled in `cloud_connect_aws.py`.  
+ Added allowed HTTP method restrictions
+ Added ID list handling to API operations that require ID lists
    - Developers may now pass in a list of IDs or a comma-delimited string. 
+ Added status code response checks to authentication events
+ Instantiate Service classes without having to manage tokens
    - Pass in credentials (Now referred to as "credential authentication")
    - Pass in the entire auth object (Now referred to as "object authentication")
    > Please note: Passing a token into Service classes is still fully supported. This is now referred to as "legacy authentication".
+ Added automatic token refresh functionality to Service Class calls
    - Developers must make use of either credential or object authentication in order to leverage this functionality.

## Issues resolved
+ Added dynamic package metadata updates (Closes #14)
    - Generalized version control
        - New constant file: `_version.py`
+ Added user-agent string to HTTP headers. (Closes #57)
+ Resolved a bug with token deauthentication (Uber and Service classes)
+ Resolved a bug in Firewall_Management.update_rule_group

## Other
+ Abstracted calls to the requests library from all classes, reducing code segment size
    - New library: _util.py
    - New class: _service_class.py
    - New class: _result.py
    - All Service Classes refactored
+ Abstracted endpoint list from the Uber class to a standalone source file
    - New constant file: _endpoint.py
+ Linting / code cleanup
    - Added function input parameter datatype specifications (where possible)
    - Added function output datatype decorators
    - In order to reduce confusion, references to the `json` requests attribute are now always referred to as "body". 
    - References to the `data` requests attribute are still referred to as "data".
+ 100% unit test coverage
+ Internal documentation updates

---
