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

_hosts_endpoints = [
  [
    "CombinedHiddenDevicesByFilter",
    "GET",
    "/devices/combined/devices-hidden/v1",
    "Search for hidden hosts in your environment by platform, hostname, IP, and other criteria. Returns full device records.",
    "hosts",
    [
      {
        "type": "string",
        "description": "The offset to page from, provided from the previous call as the \"next\" value, for "
        "the next result set. For the first call, do not supply an offset.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 100,
        "description": "The maximum records to return. [1-10000]",
        "name": "limit",
        "in": "query"
      },
      {
        "enum": [
          "device_policies.jumpcloud.policy_type",
          "device_policies.content-update.policy_type",
          "group_hash",
          "k8s_cluster_version",
          "machine_domain",
          "os_version",
          "release_group",
          "policies.policy_type",
          "device_policies.device_control.policy_id",
          "device_policies.device_control.applied",
          "managed_apps.jumpcloud.version",
          "device_policies.exposure-management.applied",
          "ou",
          "policies.policy_id",
          "device_policies.automox.applied",
          "device_policies.jumpcloud.applied",
          "device_policies.firewall.applied",
          "detection_suppression_status",
          "device_policies.browser-extension.policy_type",
          "config_id_base",
          "device_policies.device_control.policy_type",
          "device_policies.fim.applied",
          "device_policies.data-protection.policy_type",
          "device_policies.aws-verified-access.applied",
          "instance_id",
          "_all",
          "device_policies.mobile.policy_id",
          "product_type_desc",
          "device_policies.sensor_update.uninstall_protection",
          "device_policies.vulnerability-management.policy_id",
          "device_policies.data-protection.policy_id",
          "reduced_functionality_mode",
          "serial_number",
          "pod_namespace",
          "license_activation_state",
          "agent_load_flags",
          "device_policies.airlock.policy_id",
          "device_policies.content-update.applied",
          "zone_group",
          "hostname",
          "local_ip",
          "device_policies.it-automation.applied",
          "local_ip.raw",
          "default_gateway_ip",
          "device_policies.exposure-management.policy_type",
          "device_policies.application-abuse-prevention.policy_type",
          "device_policies.airlock.applied",
          "device_policies.netskope.applied",
          "device_policies.ztl.policy_type",
          "pod_ip4",
          "device_policies.logscale-collector.applied",
          "cid",
          "policies.applied",
          "device_policies.sensor_update.policy_type",
          "device_policies.identity-endpoint.policy_id",
          "device_policies.ztl.policy_id",
          "first_seen",
          "safe_mode",
          "device_policies.system-tray.policy_type",
          "device_policies.fim.policy_type",
          "device_policies.sca.applied",
          "device_policies.it-automation.policy_id",
          "mac_address",
          "pod_host_ip4",
          "policy_id",
          "device_policies.kubernetes-admission-control.applied",
          "device_policies.cloud-ml.policy_type",
          "device_policies.data-protection-cloud.policy_type",
          "internet_exposure",
          "device_policies.browser-extension.policy_id",
          "device_policies.prevention.policy_id",
          "device_policies.sensor_update.applied",
          "device_policies.identity-protection.policy_id",
          "migration_completed_time",
          "device_policies.browser-extension.applied",
          "os_build",
          "device_policies.identity-endpoint.applied",
          "device_policies.kubernetes-admission-control.policy_type",
          "device_policies.cloud-ml.policy_id",
          "device_policies.sca.policy_type",
          "k8s_cluster_git_version",
          "device_policies.logscale-collector.policy_type",
          "device_policies.application-abuse-prevention.applied",
          "device_id",
          "product_type",
          "device_policies.content-update.policy_id",
          "device_policies.cloud-ml.applied",
          "device_policies.aws-verified-access.policy_type",
          "device_policies.aws-verified-access.policy_id",
          "managed_apps.automox.version",
          "linux_sensor_mode",
          "last_login_user_sid",
          "device_policies.prevention.applied",
          "device_policies.data-protection.applied",
          "device_policies.remote_response.applied",
          "filesystem_containment_status",
          "device_policies.data-protection-cloud.applied",
          "device_policies.firewall.policy_id",
          "chassis_type_desc",
          "config_id_build",
          "first_login_timestamp",
          "device_policies.data-protection-cloud.policy_id",
          "device_policies.host-retention.policy_id",
          "managed_apps.netskope.version",
          "cpu_signature",
          "cpu_vendor",
          "pod_id",
          "external_ip",
          "device_policies.it-automation.policy_type",
          "device_policies.firewall.rule_set_id",
          "tags",
          "pod_hostname",
          "deployment_type",
          "last_reboot",
          "host_utc_offset",
          "platform_name",
          "device_policies.sensor_update.policy_id",
          "device_policies.airlock.policy_type",
          "device_policies.consumer-subscription.policy_type",
          "device_policies.remote_response.policy_id",
          "pod_annotations",
          "k8s_cluster_id",
          "device_policies.fem-browser-extension-control.applied",
          "device_policies.identity-protection.applied",
          "last_login_user",
          "modified_timestamp",
          "device_policies.netskope.policy_type",
          "device_policies.netskope.policy_id",
          "device_policies.fim.policy_id",
          "managed_apps.airlock.version",
          "managed_apps.identity-protection.version",
          "kernel_version",
          "last_login_uid",
          "device_policies.consumer-subscription.policy_id",
          "device_policies.sca.policy_id",
          "pod_ip6",
          "pod_service_account_name",
          "device_policies.network-scan-content.policy_id",
          "device_policies.logscale-collector.policy_id",
          "device_policies.fem-browser-extension-control.policy_id",
          "device_policies.identity-endpoint.policy_type",
          "device_policies.remote_response.policy_type",
          "site_name",
          "system_product_name",
          "device_policies.jumpcloud.policy_id",
          "device_policies.kubernetes-admission-control.policy_id",
          "device_policies.system-tray.applied",
          "device_policies.mobile.policy_type",
          "device_policies.mobile.applied",
          "pod_host_ip6",
          "last_seen",
          "device_policies.automox.policy_id",
          "device_policies.ztl.applied",
          "device_policies.consumer-subscription.applied",
          "device_policies.host-retention.policy_type",
          "pointer_size",
          "chassis_type",
          "device_policies.exposure-management.policy_id",
          "config_id_platform",
          "device_policies.prevention.policy_type",
          "device_policies.identity-protection.policy_type",
          "device_policies.system-tray.policy_id",
          "device_policies.vulnerability-management.applied",
          "device_policies.host-retention.applied",
          "device_policies.firewall.policy_type",
          "rtr_state",
          "bios_version",
          "last_login_timestamp",
          "major_version",
          "pod_name",
          "connection_ip",
          "connection_mac_address",
          "os_product_name",
          "device_policies.network-scan-content.policy_type",
          "agent_version",
          "bios_manufacturer",
          "first_login_user",
          "pod_labels",
          "device_policies.application-abuse-prevention.policy_id",
          "platform_id",
          "system_manufacturer",
          "device_policies.automox.policy_type",
          "device_policies.network-scan-content.applied",
          "minor_version",
          "status",
          "device_policies.vulnerability-management.policy_type",
          "groups",
          "email",
          "device_policies.fem-browser-extension-control.policy_type",
          "service_provider",
          "service_provider_account_id",
          "managed_apps.aws-verified-access.version"
        ],
        "type": "string",
        "description": "The property to sort by (e.g. status.desc or hostname.asc). If not specified, the "
        "default sort will be device_id.asc. This should be supplied for each consecutive call.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results. This should be "
        "supplied for each consecutive call.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The fields to return, comma delimited if specifying more than one field. For example: "
        "fields=hostname,device_id would return device records only containing the hostname and device_id",
        "name": "fields",
        "in": "query"
      }
    ]
  ],
  [
    "QueryDeviceLoginHistory",
    "POST",
    "/devices/combined/devices/login-history/v1",
    "Retrieve details about recent login sessions for a set of devices.",
    "hosts",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryDeviceLoginHistoryV2",
    "POST",
    "/devices/combined/devices/login-history/v2",
    "Retrieve details about recent interactive login sessions for a set of devices powered by the Host "
    "Timeline. A max of 10 device ids can be specified",
    "hosts",
    [
      {
        "type": "integer",
        "default": 10,
        "description": "The maximum number of results to return [1-100].",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "default": "now-7d",
        "description": "The inclusive beginning of the time window to search.",
        "name": "from",
        "in": "query"
      },
      {
        "type": "string",
        "default": "now",
        "description": "The inclusive end of the time window to search.",
        "name": "to",
        "in": "query"
      },
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryGetNetworkAddressHistoryV1",
    "POST",
    "/devices/combined/devices/network-address-history/v1",
    "Retrieve history of IP and MAC addresses of devices.",
    "hosts",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "CombinedDevicesByFilter",
    "GET",
    "/devices/combined/devices/v1",
    "Search for hosts in your environment by platform, hostname, IP, and other criteria. Returns full device records.",
    "hosts",
    [
      {
        "type": "string",
        "description": "The offset to page from, provided from the previous call as the \"next\" value, for "
        "the next result set. For the first call, do not supply an offset.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 100,
        "description": "The maximum records to return. [1-10000]",
        "name": "limit",
        "in": "query"
      },
      {
        "enum": [
          "device_policies.jumpcloud.policy_type",
          "device_policies.content-update.policy_type",
          "group_hash",
          "k8s_cluster_version",
          "machine_domain",
          "os_version",
          "release_group",
          "policies.policy_type",
          "device_policies.device_control.policy_id",
          "device_policies.device_control.applied",
          "managed_apps.jumpcloud.version",
          "device_policies.exposure-management.applied",
          "ou",
          "policies.policy_id",
          "device_policies.automox.applied",
          "device_policies.jumpcloud.applied",
          "device_policies.firewall.applied",
          "detection_suppression_status",
          "device_policies.browser-extension.policy_type",
          "config_id_base",
          "device_policies.device_control.policy_type",
          "device_policies.fim.applied",
          "device_policies.data-protection.policy_type",
          "device_policies.aws-verified-access.applied",
          "instance_id",
          "_all",
          "device_policies.mobile.policy_id",
          "product_type_desc",
          "device_policies.sensor_update.uninstall_protection",
          "device_policies.vulnerability-management.policy_id",
          "device_policies.data-protection.policy_id",
          "reduced_functionality_mode",
          "serial_number",
          "pod_namespace",
          "license_activation_state",
          "agent_load_flags",
          "device_policies.airlock.policy_id",
          "device_policies.content-update.applied",
          "zone_group",
          "hostname",
          "local_ip",
          "device_policies.it-automation.applied",
          "local_ip.raw",
          "default_gateway_ip",
          "device_policies.exposure-management.policy_type",
          "device_policies.application-abuse-prevention.policy_type",
          "device_policies.airlock.applied",
          "device_policies.netskope.applied",
          "device_policies.ztl.policy_type",
          "pod_ip4",
          "device_policies.logscale-collector.applied",
          "cid",
          "policies.applied",
          "device_policies.sensor_update.policy_type",
          "device_policies.identity-endpoint.policy_id",
          "device_policies.ztl.policy_id",
          "first_seen",
          "safe_mode",
          "device_policies.system-tray.policy_type",
          "device_policies.fim.policy_type",
          "device_policies.sca.applied",
          "device_policies.it-automation.policy_id",
          "mac_address",
          "pod_host_ip4",
          "policy_id",
          "device_policies.kubernetes-admission-control.applied",
          "device_policies.cloud-ml.policy_type",
          "device_policies.data-protection-cloud.policy_type",
          "internet_exposure",
          "device_policies.browser-extension.policy_id",
          "device_policies.prevention.policy_id",
          "device_policies.sensor_update.applied",
          "device_policies.identity-protection.policy_id",
          "migration_completed_time",
          "device_policies.browser-extension.applied",
          "os_build",
          "device_policies.identity-endpoint.applied",
          "device_policies.kubernetes-admission-control.policy_type",
          "device_policies.cloud-ml.policy_id",
          "device_policies.sca.policy_type",
          "k8s_cluster_git_version",
          "device_policies.logscale-collector.policy_type",
          "device_policies.application-abuse-prevention.applied",
          "device_id",
          "product_type",
          "device_policies.content-update.policy_id",
          "device_policies.cloud-ml.applied",
          "device_policies.aws-verified-access.policy_type",
          "device_policies.aws-verified-access.policy_id",
          "managed_apps.automox.version",
          "linux_sensor_mode",
          "last_login_user_sid",
          "device_policies.prevention.applied",
          "device_policies.data-protection.applied",
          "device_policies.remote_response.applied",
          "filesystem_containment_status",
          "device_policies.data-protection-cloud.applied",
          "device_policies.firewall.policy_id",
          "chassis_type_desc",
          "config_id_build",
          "first_login_timestamp",
          "device_policies.data-protection-cloud.policy_id",
          "device_policies.host-retention.policy_id",
          "managed_apps.netskope.version",
          "cpu_signature",
          "cpu_vendor",
          "pod_id",
          "external_ip",
          "device_policies.it-automation.policy_type",
          "device_policies.firewall.rule_set_id",
          "tags",
          "pod_hostname",
          "deployment_type",
          "last_reboot",
          "host_utc_offset",
          "platform_name",
          "device_policies.sensor_update.policy_id",
          "device_policies.airlock.policy_type",
          "device_policies.consumer-subscription.policy_type",
          "device_policies.remote_response.policy_id",
          "pod_annotations",
          "k8s_cluster_id",
          "device_policies.fem-browser-extension-control.applied",
          "device_policies.identity-protection.applied",
          "last_login_user",
          "modified_timestamp",
          "device_policies.netskope.policy_type",
          "device_policies.netskope.policy_id",
          "device_policies.fim.policy_id",
          "managed_apps.airlock.version",
          "managed_apps.identity-protection.version",
          "kernel_version",
          "last_login_uid",
          "device_policies.consumer-subscription.policy_id",
          "device_policies.sca.policy_id",
          "pod_ip6",
          "pod_service_account_name",
          "device_policies.network-scan-content.policy_id",
          "device_policies.logscale-collector.policy_id",
          "device_policies.fem-browser-extension-control.policy_id",
          "device_policies.identity-endpoint.policy_type",
          "device_policies.remote_response.policy_type",
          "site_name",
          "system_product_name",
          "device_policies.jumpcloud.policy_id",
          "device_policies.kubernetes-admission-control.policy_id",
          "device_policies.system-tray.applied",
          "device_policies.mobile.policy_type",
          "device_policies.mobile.applied",
          "pod_host_ip6",
          "last_seen",
          "device_policies.automox.policy_id",
          "device_policies.ztl.applied",
          "device_policies.consumer-subscription.applied",
          "device_policies.host-retention.policy_type",
          "pointer_size",
          "chassis_type",
          "device_policies.exposure-management.policy_id",
          "config_id_platform",
          "device_policies.prevention.policy_type",
          "device_policies.identity-protection.policy_type",
          "device_policies.system-tray.policy_id",
          "device_policies.vulnerability-management.applied",
          "device_policies.host-retention.applied",
          "device_policies.firewall.policy_type",
          "rtr_state",
          "bios_version",
          "last_login_timestamp",
          "major_version",
          "pod_name",
          "connection_ip",
          "connection_mac_address",
          "os_product_name",
          "device_policies.network-scan-content.policy_type",
          "agent_version",
          "bios_manufacturer",
          "first_login_user",
          "pod_labels",
          "device_policies.application-abuse-prevention.policy_id",
          "platform_id",
          "system_manufacturer",
          "device_policies.automox.policy_type",
          "device_policies.network-scan-content.applied",
          "minor_version",
          "status",
          "device_policies.vulnerability-management.policy_type",
          "groups",
          "email",
          "device_policies.fem-browser-extension-control.policy_type",
          "service_provider",
          "service_provider_account_id",
          "managed_apps.aws-verified-access.version"
        ],
        "type": "string",
        "description": "The property to sort by (e.g. status.desc or hostname.asc). If not specified, the "
        "default sort will be device_id.asc. This should be supplied for each consecutive call.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results. This should be "
        "supplied for each consecutive call.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The fields to return, comma delimited if specifying more than one field. For example: "
        "fields=hostname,device_id would return device records only containing the hostname and device_id",
        "name": "fields",
        "in": "query"
      }
    ]
  ],
  [
    "PerformActionV2",
    "POST",
    "/devices/entities/devices-actions/v2",
    "Take various actions on the hosts in your environment. Contain or lift containment on a host. Delete or restore a host.",
    "hosts",
    [
      {
        "type": "string",
        "description": "Specify one of these actions:\n  contain - This action contains the host, which stops "
        "any network communications to locations other than the CrowdStrike cloud and IPs specified in your "
        "[containment policy](https://falcon.crowdstrike.com/support/documentation/11/getting-started-"
        "guide#containmentpolicy)  lift_containment: This action lifts containment on the host, which returns its "
        "network communications to normal  hide_host: This action will delete a host. After the host is deleted, no new "
        " detections for that host will be reported via UI or APIs  unhide_host: This action will restore a host. "
        "Detection reporting will resume after the host is restored",
        "name": "action_name",
        "in": "query",
        "required": True
      },
      {
        "description": "The host agent ID (AID) of the host you want to contain. Get an agent ID from a "
        "detection, the Falcon console, or the Streaming API.\n\nProvide the ID in JSON format with the key ids and the "
        "value in square brackets, such as: \n\n\"ids\": [\"123456789\"]",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "UpdateDeviceTags",
    "PATCH",
    "/devices/entities/devices/tags/v1",
    "Append or remove one or more Falcon Grouping Tags on one or more hosts.  Tags must be of the form FalconGroupingTags/",
    "hosts",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetDeviceDetails",
    "POST",
    "/devices/entities/devices/v2",
    "Get details on one or more hosts by providing host IDs in a POST body.  Supports up to a maximum 5000 IDs.",
    "hosts",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetDeviceDetailsV1",
    "GET",
    "/devices/entities/devices/v1",
    "Get details on one or more hosts by providing agent IDs (AID). You can get a host's agent IDs (AIDs) from "
    "the /devices/queries/devices/v1 endpoint, the Falcon console or the Streaming API",
    "hosts",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The host agentIDs used to get details on",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetDeviceDetailsV2",
    "GET",
    "/devices/entities/devices/v2",
    "Get details on one or more hosts by providing host IDs as a query parameter.  Supports up to a maximum 100 IDs.",
    "hosts",
    [
      {
        "maxItems": 100,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The host agentIDs used to get details on",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "PostDeviceDetailsV2",
    "POST",
    "/devices/entities/devices/v2",
    "Get details on one or more hosts by providing host IDs in a POST body.  Supports up to a maximum 5000 IDs.",
    "hosts",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "entities_perform_action",
    "POST",
    "/devices/entities/group-actions/v1",
    "Performs the specified action on the provided group IDs.",
    "hosts",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The group ids to act on",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "enum": [
          "add_group_member",
          "remove_all",
          "remove_group_member"
        ],
        "type": "string",
        "description": "The action to perform.",
        "name": "action_name",
        "in": "query",
        "required": True
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Bool to disable hostname check on add-member",
        "name": "disable_hostname_check",
        "in": "query"
      },
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetOnlineState_V1",
    "GET",
    "/devices/entities/online-state/v1",
    "Get the online status for one or more hosts by specifying each host’s unique ID. Successful requests "
    "return an HTTP 200 response and the status for each host identified by a `state` of `online`, `offline`, or "
    "`unknown` for each host, identified by host `id`.\n\nUse QueryDevicesByFilterScroll to get a list of host "
    "IDs.",
    "hosts",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The unique ID of the host to get the online status of.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "QueryHiddenDevices",
    "GET",
    "/devices/queries/devices-hidden/v1",
    "Retrieve hidden hosts that match the provided filter criteria.",
    "hosts",
    [
      {
        "type": "integer",
        "description": "The offset to start retrieving records from",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum records to return. [1-5000]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The property to sort by (e.g. status.desc or hostname.asc)",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "QueryDevicesByFilterScroll",
    "GET",
    "/devices/queries/devices-scroll/v1",
    "Search for hosts in your environment by platform, hostname, IP, and other criteria with continuous "
    "pagination capability (based on offset pointer which expires after 2 minutes with no maximum limit)",
    "hosts",
    [
      {
        "type": "string",
        "description": "The offset to page from, provided from the previous scroll call, for the next result "
        "set. For the first call, do not supply an offset.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum records to return. [1-10000]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The property to sort by (e.g. status.desc or hostname.asc)",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "QueryDevicesByFilter",
    "GET",
    "/devices/queries/devices/v1",
    "Search for hosts in your environment by platform, hostname, IP, and other criteria.",
    "hosts",
    [
      {
        "type": "integer",
        "description": "The offset to start retrieving records from",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum records to return. [1-5000]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The property to sort by (e.g. status.desc or hostname.asc)",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
