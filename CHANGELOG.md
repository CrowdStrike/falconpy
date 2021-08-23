# Version 0.6.2
## Issues resolved
+ Bug fix: Fixed Uber class passing empty **ids** parameter array when no _ids_ had been provided to the command method. Closes #314. `_util.py`

# Version 0.6.1
## Issues resolved
+ Bug fix: Fixed bad comparison for endpoint lookups when using Service Classes. Closes #305. `_util.py`
+ Bug fix: Fixed typo in operation ID for query_platforms method within CustomIOA Service Class. Closes #307. `custom_ioa.py`
+ Bug fix: Fixed typo in operation ID for create_user_groups method within FlightControl Service Class. Closes #308. `mssp.py`

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

# Version 0.5.3
## Issues resolved
+ Bug fix: Resolves #200 by moving the failing method (entities_processes) in `iocs.py` to the latest code pattern.

# Version 0.5.2
## Issues resolved
+ Fixed: Incorrect endpoint specified in the updateSensorUpdatePoliciesV2 method within the Sensor Update Policy service class.

# Version 0.5.1
## Issues resolved
+ Fixed: https://github.com/CrowdStrike/falconpy/issues/181 by adding the parameters to the create and update ioc functions.

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

# Version 0.4.10
## Added features and functionality
+ Added: Timeout support - Float / tuple that is passed to the requests library when performing
requests to the API. Can specify timeouts for connect, read and global.

## Issues resolved
+ Fixed: Service Class proxy functionality support

## Other
+ Timeout functionality unit tests (`test_timeout.py`)

# Version 0.4.9
## Added features and functionality
+ Added: Proxy support - dictionary of proxies that are passed to the requests library when
performing requests to the API.
+ Related to discussion post [#154](https://github.com/CrowdStrike/falconpy/discussions/154)

# Version 0.4.8
## Issues resolved
+ Fixed: Parsing issue with __ids__ argument within MSSP.getChildren (Flight Control Service Class)
    * Resolved by migrating `mssp.py` source to the new pattern being tested for Service Classes.
    * Closes [#144](https://github.com/CrowdStrike/falconpy/issues/144)

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
# Version 0.4.6-spotlight-remediations-patch-1
## Added features and functionality
+ Added: Missing method to Spotlight_Vulnerabilities Service Class (`spotlight_vulnerabilities.py`)
    * getRemediations
    - Added unit test to existing test series (`test_spotlight_vulnerabilities.py`)
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
