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

_container_images_endpoints = [
  [
    "AggregateImageAssessmentHistory",
    "GET",
    "/container-security/aggregates/images/assessment-history/v1",
    "Image assessment history",
    "container_images",
    [
      {
        "type": "string",
        "description": "Filter using a query in Falcon Query Language (FQL). Supported filters:  cid,registry,repository",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "AggregateImageCountByBaseOS",
    "GET",
    "/container-security/aggregates/images/count-by-os-distribution/v1",
    "Aggregate count of images grouped by Base OS distribution",
    "container_images",
    [
      {
        "type": "string",
        "description": "Filter images using a query in Falcon Query Language (FQL). Supported filters:  "
        "arch,base_os,cid,registry,repository,tag",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "AggregateImageCountByState",
    "GET",
    "/container-security/aggregates/images/count-by-state/v1",
    "Aggregate count of images grouped by state",
    "container_images",
    [
      {
        "type": "string",
        "description": "Filter images using a query in Falcon Query Language (FQL). Supported filters:  "
        "cid,last_seen,registry,repository",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "AggregateImageCount",
    "GET",
    "/container-security/aggregates/images/count/v1",
    "Aggregate count of images",
    "container_images",
    [
      {
        "type": "string",
        "description": "Filter images using a query in Falcon Query Language (FQL). Supported filters:  arch,b"
        "ase_os,cid,container_id,container_running_status,cps_rating,crowdstrike_user,cve_id,detection_count,detection_"
        "name,detection_severity,first_seen,image_digest,image_id,layer_digest,package_name_version,registry,repository"
        ",tag,vulnerability_count,vulnerability_severity",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "GetCombinedImages",
    "GET",
    "/container-security/combined/image-assessment/images/v1",
    "Get image assessment results by providing an FQL filter and paging details",
    "container_images",
    [
      {
        "type": "string",
        "description": "Filter images using a query in Falcon Query Language (FQL). Supported filters:  "
        "container_id, container_running_status, cve_id, detection_name, detection_severity, first_seen, image_digest, "
        "image_id, registry, repository, tag, vulnerability_severity",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The upper-bound on the number of records to retrieve [1-100]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The offset from where to begin.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The fields to sort the records on. Supported columns:  [first_seen "
        "highest_detection_severity highest_vulnerability_severity image_digest image_id registry repository tag]",
        "name": "sort",
        "in": "query"
      }
    ]
  ],
  [
    "CombinedImageByVulnerabilityCount",
    "GET",
    "/container-security/combined/images/by-vulnerability-count/v1",
    "Retrieve top x images with the most vulnerabilities",
    "container_images",
    [
      {
        "type": "string",
        "description": "Filter images using a query in Falcon Query Language (FQL). Supported filters:  "
        "arch,base_os,cid,registry,repository,tag",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The upper-bound on the number of records to retrieve.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "This is not used in the backend but is added here for compatibility purposes as some "
        "clients expects this i.e UI widgets.",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "CombinedImageDetail",
    "GET",
    "/container-security/combined/images/detail/v1",
    "Retrieve image entities identified by the provided filter criteria",
    "container_images",
    [
      {
        "type": "string",
        "description": "Filter images using a query in Falcon Query Language (FQL). Supported filters:  "
        "registry,repository,tag",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "boolean",
        "description": "(true/false) include image config, default is false",
        "name": "with_config",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The upper-bound on the number of records to retrieve.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The offset from where to begin.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The fields to sort the records on.",
        "name": "sort",
        "in": "query"
      }
    ]
  ],
  [
    "ReadCombinedImagesExport",
    "GET",
    "/container-security/combined/images/export/v1",
    "Retrieve images with an option to expand aggregated vulnerabilities/detections",
    "container_images",
    [
      {
        "type": "string",
        "description": "Filter images using a query in Falcon Query Language (FQL). Supported filters:  arch,b"
        "ase_os,cid,container_id,container_running_status,cps_rating,crowdstrike_user,cve_id,detection_count,detection_"
        "name,detection_severity,first_seen,image_digest,image_id,layer_digest,package_name_version,registry,repository"
        ",tag,vulnerability_count,vulnerability_severity",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "boolean",
        "description": "expand vulnerabilities",
        "name": "expand_vulnerabilities",
        "in": "query"
      },
      {
        "type": "boolean",
        "description": "expand detections",
        "name": "expand_detections",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The upper-bound on the number of records to retrieve.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The offset from where to begin.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The fields to sort the records on. Supported columns:  [base_os cid containers "
        "detections firstScanned first_seen highest_cps_current_rating highest_detection_severity "
        "highest_vulnerability_severity image_digest image_id last_seen layers_with_vulnerabilities packages registry "
        "repository tag vulnerabilities]",
        "name": "sort",
        "in": "query"
      }
    ]
  ],
  [
    "CombinedImageIssuesSummary",
    "GET",
    "/container-security/combined/images/issues-summary/v1",
    "Retrieve image issues summary such as Image detections, Runtime detections, Policies, vulnerabilities",
    "container_images",
    [
      {
        "type": "string",
        "description": "CID",
        "name": "cid",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "registry name",
        "name": "registry",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "repository name",
        "name": "repository",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "tag name",
        "name": "tag",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "CombinedImageVulnerabilitySummary",
    "GET",
    "/container-security/combined/images/vulnerabilities-summary/v1",
    "aggregates information about vulnerabilities for an image",
    "container_images",
    [
      {
        "type": "string",
        "description": "CID",
        "name": "cid",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "registry name",
        "name": "registry",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "repository name",
        "name": "repository",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "tag name",
        "name": "tag",
        "in": "query",
        "required": True
      }
    ]
  ]
]
