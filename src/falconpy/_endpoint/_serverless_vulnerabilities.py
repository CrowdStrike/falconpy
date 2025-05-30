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

_serverless_vulnerabilities_endpoints = [
  [
    "GetCombinedVulnerabilitiesSARIF",
    "GET",
    "/lambdas/combined/vulnerabilities/sarif/v1",
    "Retrieve all lambda vulnerabilities that match the given query and return in the SARIF format",
    "serverless_vulnerabilities",
    [
      {
        "type": "string",
        "description": "Filter lambda vulnerabilities using a query in Falcon Query Language (FQL).Supported "
        "filters:  application_name,application_name_version,cid,cloud_account_id,cloud_account_name,cloud_provider,cve "
        "_id,cvss_base_score,exprt_rating,first_seen_timestamp,function_name,function_resource_id,is_supported,is_valid "
        "_asset_id,layer,region,runtime,severity,timestamp,type",
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
        "description": "The offset from where to begin.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The fields to sort the records on. Supported columns:  [application_name "
        "application_name_version cid cloud_account_id cloud_account_name cloud_provider cve_id cvss_base_score "
        "exprt_rating first_seen_timestamp function_resource_id is_supported layer region runtime severity timestamp "
        "type]",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
