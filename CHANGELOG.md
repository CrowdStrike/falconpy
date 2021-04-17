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

## Other
+ Moved _endpoint constant library to a private submodule (No impact to existing usage)
    - Added payload parameter information to _endpoint constants
    - Adds service collection ID to endpoint lists
    - This prepares the package for new functionality planned for future releases
+ Minor unit test update to `test_cspm_registration.py`g
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