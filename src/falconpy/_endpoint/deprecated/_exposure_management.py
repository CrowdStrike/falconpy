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

_exposure_management_endpoints = [
  [
    "aggregate-external-assets",
    "POST",
    "/fem/aggregates/external-assets/v1",
    "Returns external assets aggregates.",
    "exposure_management",
    [
      {
        "description": "Aggregation specification.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "blob-download-external-assets",
    "GET",
    "/fem/entities/blobs-download/v1",
    "Download the entire contents of the blob. The relative link to this endpoint is returned in the GET "
    "/entities/external-assets/v1 request.",
    "exposure_management",
    [
      {
        "type": "string",
        "description": "The Asset ID",
        "name": "assetId",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "The File Hash",
        "name": "hash",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "blob-preview-external-assets",
    "GET",
    "/fem/entities/blobs-preview/v1",
    "Download a preview of the blob. The relative link to this endpoint is returned in the GET "
    "/entities/external-assets/v1 request.",
    "exposure_management",
    [
      {
        "type": "string",
        "description": "The Asset ID",
        "name": "assetId",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "The File Hash",
        "name": "hash",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "get-external-assets",
    "GET",
    "/fem/entities/external-assets/v1",
    "Get details on external assets by providing one or more IDs.",
    "exposure_management",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more asset IDs (max: 100). Find asset IDs with GET `/fem/queries/external-assets/v1`",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "patch-external-assets",
    "PATCH",
    "/fem/entities/external-assets/v1",
    "Update the details of external assets.",
    "exposure_management",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "query-external-assets",
    "GET",
    "/fem/queries/external-assets/v1",
    "Get a list of external asset IDs that match the provided filter conditions. Use these IDs with the "
    "/entities/external-assets/v1 endpoints",
    "exposure_management",
    [
      {
        "type": "string",
        "description": "Starting index of result set from which to return IDs.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Number of IDs to return.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Order by fields.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter assets using an FQL query. Common filter options "
        "include:<ul><li>asset_type:'ip'</li><li>last_seen_timestamp:>'now-7d'</li></ul>\n\t\t\t</br>Available filter "
        "fields that support exact match: asset_id, asset_type, confidence, connectivity_status, criticality, "
        "criticality_description, criticality_timestamp, criticality_username, data_providers, discovered_by, "
        "dns_domain.fqdn, dns_domain.isps, dns_domain.parent_domain, dns_domain.resolved_ips, "
        "dns_domain.services.applications.category, dns_domain.services.applications.cpe, "
        "dns_domain.services.applications.name, dns_domain.services.applications.vendor, "
        "dns_domain.services.applications.version, dns_domain.services.cloud_provider, dns_domain.services.cpes, "
        "dns_domain.services.hosting_provider, dns_domain.services.last_seen, dns_domain.services.platform_name, "
        "dns_domain.services.port, dns_domain.services.protocol, dns_domain.services.protocol_port, "
        "dns_domain.services.status, dns_domain.services.status_code, dns_domain.services.transport, dns_domain.type, "
        "first_seen, id, internet_exposure, ip.asn, ip.cloud_vm.description, ip.cloud_vm.instance_id, "
        "ip.cloud_vm.lifecycle, ip.cloud_vm.mac_address, ip.cloud_vm.owner_id, ip.cloud_vm.platform, "
        "ip.cloud_vm.private_ip, ip.cloud_vm.public_ip, ip.cloud_vm.region, ip.cloud_vm.security_groups, "
        "ip.cloud_vm.source, ip.cloud_vm.status, ip.fqdns, ip.ip_address, ip.isp, ip.location.area_code, "
        "ip.location.city, ip.location.country_code, ip.location.country_name, ip.location.postal_code, "
        "ip.location.region_code, ip.location.region_name, ip.location.timezone, ip.ptr, ip.aid, "
        "ip.services.applications.category, ip.services.applications.cpe, ip.services.applications.name, "
        "ip.services.applications.vendor, ip.services.applications.version, ip.services.cloud_provider, "
        "ip.services.cpes, ip.services.first_seen, ip.services.last_seen, ip.services.platform_name, ip.services.port, "
        "ip.services.protocol, ip.services.protocol_port, ip.services.status, ip.services.status_code, "
        "ip.services.transport, last_seen, manual, perimeter, subsidiaries.id, subsidiaries.name, triage.action, "
        "triage.assigned_to, triage.status, triage.updated_by, triage.updated_timestamp\n\t\t\t</br>Available filter "
        "fields that supports wildcard (*): asset_id, asset_type, confidence, connectivity_status, criticality, "
        "criticality_username, data_providers, discovered_by, dns_domain.fqdn, dns_domain.isps, "
        "dns_domain.parent_domain, dns_domain.resolved_ips, dns_domain.services.applications.category, "
        "dns_domain.services.applications.cpe, dns_domain.services.applications.name, "
        "dns_domain.services.applications.vendor, dns_domain.services.applications.version, "
        "dns_domain.services.cloud_provider, dns_domain.services.cpes, dns_domain.services.hosting_provider, "
        "dns_domain.services.id, dns_domain.services.platform_name, dns_domain.services.port, "
        "dns_domain.services.protocol, dns_domain.services.protocol_port, dns_domain.services.status, "
        "dns_domain.services.status_code, dns_domain.services.transport, dns_domain.type, id, internet_exposure, "
        "ip.asn, ip.cloud_vm.instance_id, ip.cloud_vm.lifecycle, ip.cloud_vm.mac_address, ip.cloud_vm.owner_id, "
        "ip.cloud_vm.platform, ip.cloud_vm.private_ip, ip.cloud_vm.public_ip, ip.cloud_vm.region, "
        "ip.cloud_vm.security_groups, ip.cloud_vm.source, ip.cloud_vm.status, ip.fqdns, ip.ip_address, ip.isp, "
        "ip.location.area_code, ip.location.city, ip.location.country_code, ip.location.country_name, "
        "ip.location.postal_code, ip.location.region_code, ip.location.region_name, ip.location.timezone, ip.ptr, "
        "ip.aid, ip.services.applications.category, ip.services.applications.cpe, ip.services.applications.name, "
        "ip.services.applications.vendor, ip.services.applications.version, ip.services.cloud_provider, "
        "ip.services.cpes, ip.services.platform_name, ip.services.port, ip.services.protocol, "
        "ip.services.protocol_port, ip.services.status, ip.services.status_code, ip.services.transport, manual, "
        "perimeter, subsidiaries.id, subsidiaries.name, triage.action, triage.assigned_to, triage.status, "
        "triage.updated_by\n\t\t\t</br>Available filter fields that supports in ([v1, v2]): asset_id, asset_type, "
        "confidence, connectivity_status, criticality, criticality_username, data_providers, discovered_by, "
        "dns_domain.fqdn, dns_domain.isps, dns_domain.parent_domain, dns_domain.services.applications.category, "
        "dns_domain.services.applications.cpe, dns_domain.services.applications.name, "
        "dns_domain.services.applications.vendor, dns_domain.services.applications.version, "
        "dns_domain.services.cloud_provider, dns_domain.services.cpes, dns_domain.services.id, "
        "dns_domain.services.platform_name, dns_domain.services.port, dns_domain.services.protocol, "
        "dns_domain.services.protocol_port, dns_domain.services.status, dns_domain.services.status_code, "
        "dns_domain.services.transport, dns_domain.type, id, internet_exposure, ip.asn, ip.cloud_vm.instance_id, "
        "ip.cloud_vm.lifecycle, ip.cloud_vm.mac_address, ip.cloud_vm.owner_id, ip.cloud_vm.platform, "
        "ip.cloud_vm.region, ip.cloud_vm.security_groups, ip.cloud_vm.source, ip.cloud_vm.status, ip.fqdns, ip.isp, "
        "ip.location.area_code, ip.location.city, ip.location.country_code, ip.location.country_name, "
        "ip.location.postal_code, ip.location.region_code, ip.location.region_name, ip.location.timezone, ip.ptr, "
        "ip.aid, ip.services.applications.category, ip.services.applications.cpe, ip.services.applications.name, "
        "ip.services.applications.vendor, ip.services.applications.version, ip.services.cloud_provider, "
        "ip.services.cpes, ip.services.platform_name, ip.services.port, ip.services.protocol, "
        "ip.services.protocol_port, ip.services.status, ip.services.status_code, ip.services.transport, manual, "
        "perimeter, subsidiaries.id, subsidiaries.name, triage.action, triage.assigned_to, triage.status, "
        "triage.updated_by\n\t\t\t</br>Available filter fields that supports range comparisons (>, <, >=, <=): "
        "criticality_timestamp, dns_domain.resolved_ips, dns_domain.services.first_seen, dns_domain.services.last_seen, "
        " dns_domain.services.port, dns_domain.services.status_code, first_seen, ip.cloud_vm.private_ip, "
        "ip.cloud_vm.public_ip, ip.ip_address, ip.services.first_seen, ip.services.last_seen, ip.services.port, "
        "ip.services.status_code, last_seen, triage.updated_timestamp\n\t\t\t</br>All filter fields and operations "
        "supports negation (!).",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
