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

_admission_control_policies_endpoints = [
  [
    "admission-control-get-policies",
    "GET",
    "/admission-control-policies/entities/policies/v1",
    "Get admission control policies.",
    "admission_control_policies",
    [
      {
        "maxItems": 100,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The list of policies to return (maximum 100 IDs allowed).",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "admission-control-create-policy",
    "POST",
    "/admission-control-policies/entities/policies/v1",
    "Create an admission control policy.",
    "admission_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "admission-control-update-policy",
    "PATCH",
    "/admission-control-policies/entities/policies/v1",
    "Update an admission control policy.",
    "admission_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      },
      {
        "type": "string",
        "description": "The id of the admission control policy to update.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "admission-control-delete-policies",
    "DELETE",
    "/admission-control-policies/entities/policies/v1",
    "Delete an admission control policy.",
    "admission_control_policies",
    [
      {
        "maxItems": 100,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The ids of the policies to delete (maximum 100 IDs allowed).",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "admission-control-add-host-groups",
    "POST",
    "/admission-control-policies/entities/policy-host-groups/v1",
    "Add one or more host groups to an admission control policy.",
    "admission_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "admission-control-remove-host-groups",
    "DELETE",
    "/admission-control-policies/entities/policy-host-groups/v1",
    "Remove one or more host groups from an admission control policy.",
    "admission_control_policies",
    [
      {
        "type": "string",
        "description": "The id of the policy to modify.",
        "name": "policy_id",
        "in": "query",
        "required": True
      },
      {
        "maxItems": 100,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The ids of the host groups to remove (maximum 100 IDs allowed).",
        "name": "host_group_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "admission-control-update-policy-precedence",
    "PATCH",
    "/admission-control-policies/entities/policy-precedence/v1",
    "Update admission control policy precedence.",
    "admission_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "admission-control-add-rule-group-custom-rule",
    "POST",
    "/admission-control-policies/entities/policy-rule-group-custom-rules/v1",
    "Add one or more custom Rego rules to a rule group in an admission control policy. The requested custom "
    "rules are also added to all other unspecified rule groups in the policy with action 'Disabled'.",
    "admission_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "admission-control-remove-rule-group-custom-rule",
    "DELETE",
    "/admission-control-policies/entities/policy-rule-group-custom-rules/v1",
    "Delete one or more custom Rego rules from all rule groups in an admission control policy.",
    "admission_control_policies",
    [
      {
        "type": "string",
        "description": "The id of the policy to modify.",
        "name": "policy_id",
        "in": "query",
        "required": True
      },
      {
        "maxItems": 100,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The ids of the custom Rego rules to delete (maximum 100 IDs allowed).",
        "name": "custom_rule_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "admission-control-set-rule-group-precedence",
    "PUT",
    "/admission-control-policies/entities/policy-rule-group-precedence/v1",
    "Change precedence of rule groups within an admission control policy.",
    "admission_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "admission-control-replace-rule-group-selectors",
    "PUT",
    "/admission-control-policies/entities/policy-rule-group-selectors/v1",
    "Replace labels and/or namespaces of a rule group within an admission control policy.",
    "admission_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "admission-control-create-rule-groups",
    "POST",
    "/admission-control-policies/entities/policy-rule-groups/v1",
    "Create one or more rule groups and add them to an existing admission control policy. The list of new rule "
    " groups will be created with the last rule group having highest precedence, second to last with second highest "
    "precedence, and so on.",
    "admission_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "admission-control-update-rule-groups",
    "PATCH",
    "/admission-control-policies/entities/policy-rule-groups/v1",
    "Update a rule group. Change rule group name, description, deny on error, Image Assessment settings, "
    "default rule actions, and custom rule actions.",
    "admission_control_policies",
    [
      {
        "description": "Valid rule action values:  Disabled  Prevent  Alert\n\nValid image assessment "
        "unassessed handling values:  Prevent  Alert  Allow Without Alert\n\nDefault rule codes:  201000: Privileged "
        "container(s)  201001: Sensitive data in environment  201002: Sensitive data in secretKeyRef  201004: "
        "Container(s) run as root  201005: Container(s) without runAsNonRoot  201006: Privilege escalation allowed  "
        "201007: Container(s) with network capabilities  201008: Container(s) with unsafe procMount  201009: "
        "Container(s) using unsafe sysctls  201010: Container(s) without resource limits  201011: Sensitive host "
        "directories mounted in container(s)  201012: Container(s) with sysadmin capability  201015: Host port attached "
        " to container(s)  201016: Host network attached to container(s)  201017: Container(s) in host PID namespace  "
        "201018: Container(s) in host IPC namespace  201019: Workload in default namespace  201020: Workload with "
        "unconfined seccomp profile  201021: Workload without SELinux or AppArmor  201022: Container(s) with many "
        "capabilities  201023: Workload without recommended seccomp profile  201024: Workload without securityContext  "
        "201025: Container runtime socket in container(s)  201026: Container(s) entrypoint contains network scanning "
        "command  201027: Container(s) entrypoint contains chroot command  201028: Malformed sysctl value  201029: "
        "Service account token automounted\n",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "admission-control-delete-rule-groups",
    "DELETE",
    "/admission-control-policies/entities/policy-rule-groups/v1",
    "Delete rule groups.",
    "admission_control_policies",
    [
      {
        "type": "string",
        "description": "The id of the policy to modify.",
        "name": "policy_id",
        "in": "query",
        "required": True
      },
      {
        "maxItems": 100,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The ids of the rule groups to delete (maximum 100 IDs allowed).",
        "name": "rule_group_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "admission-control-query-policies",
    "GET",
    "/admission-control-policies/queries/policies/v1",
    "Search admission control policies.",
    "admission_control_policies",
    [
      {
        "type": "string",
        "description": "FQL filter, allowed properties:   precedence  created_timestamp  modified_timestamp  "
        "name  description",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 100,
        "description": "The maximum number of resources to return. The maximum allowed is 500.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "description": "The number of results to skip before starting to return results.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Field to sort on. Sortable fields:   precedence  created_timestamp  modified_timestamp "
        "\n\nUse the |asc or |desc suffix to specify sort direction.",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
