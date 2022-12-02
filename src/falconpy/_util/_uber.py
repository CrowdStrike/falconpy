"""FalconPy Uber Class helper methods.

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
from typing import Tuple
from ._functions import args_to_params, return_preferred_default
from .._constant import PREFER_IDS_IN_BODY, MOCK_OPERATIONS
from .._enum import BaseURL, ContainerBaseURL


def create_uber_header_payload(hdrs: dict, passed_arguments: dict) -> dict:
    """Create the HTTP header payload.

    Creates the HTTP header payload based upon the existing class headers and passed arguments.
    """
    payload = hdrs
    if "headers" in passed_arguments:
        for item in passed_arguments["headers"]:
            payload[item] = passed_arguments["headers"][item]
    # Allow Content-Type to be specified as a keyword.
    if "content_type" in passed_arguments:
        payload["Content-Type"] = str(passed_arguments["content_type"])

    return payload


def handle_field(tgt: str, kwa: dict, fld: str) -> str:
    """Embed the distinct_field value (SensorUpdatePolicy) within the endpoint URL."""
    # Could potentially be zero
    return tgt.format(str(kwa.get(fld, None))) if kwa.get(fld, None) is not None else tgt


def handle_body_payload_ids(kwa: dict) -> dict:
    """Migrates the IDs parameter list over to the body payload."""
    if kwa.get("action", None) in PREFER_IDS_IN_BODY:
        if kwa.get("ids", None):
            # Handle the GET to POST method redirection for passed IDs
            if not kwa.get("body", {}).get("ids", None):
                if "body" not in kwa:
                    kwa["body"] = {}
                kwa["body"]["ids"] = kwa["ids"]
        # Handle any body payload ID lists that are still strings
        if isinstance(kwa.get("body", {}).get("ids", {}), str):
            kwa["body"]["ids"] = kwa["body"]["ids"].split(",")
    return kwa


def scrub_target(oper: str, scrubbed: str, kwas: dict) -> str:
    """Scrubs the endpoint target by performing any outstanding string replacements."""
    field_mapping = {
        "image_id": "DeleteImageDetails",
        "partition": "refreshActiveStreamSession",
        "distinct_field": "querySensorUpdateKernelsDistinct"
    }
    for field_name, field_value in field_mapping.items():
        if oper == field_value:  # Only perform replacements on mapped operation IDs.
            scrubbed = handle_field(scrubbed, kwas, field_name)

    return scrubbed


def handle_container_operations(kwa: dict, base_string: str) -> Tuple[dict, str, bool]:
    """Handle Base URLs and keyword arguments for container registry operations."""
    # Default to non-container registry operations
    do_container = False
    if kwa.get("action", None) in MOCK_OPERATIONS:
        for base in [burl for burl in dir(BaseURL) if "__" not in burl]:
            if BaseURL[base].value == base_string.replace("https://", ""):
                base_string = f"https://{ContainerBaseURL[base].value}"
                do_container = True
        if kwa.get("action", None) == "ImageMatchesPolicy":
            if "parameters" not in kwa:
                kwa["parameters"] = {}
            kwa["parameters"]["policy_type"] = "image-prevention-policy"
    return kwa, base_string, do_container


def uber_request_keywords(caller,
                          meth: str,                            # .        o
                          oper: str,                            # .           o
                          tgt: str,                             # .      o
                          kwa: dict,                            # .         O
                          do_cont: bool                         # .       \/|\/
                          ) -> dict:                            # .        / \  o
    """Generate a properly formatted mapping of the keywords for this request."""
    return {
        "method": meth,
        "endpoint": tgt,
        "body": kwa.get("body", return_preferred_default(oper)),
        "data": kwa.get("data", return_preferred_default(oper)),
        "params": args_to_params(kwa.get("parameters", {}), kwa, caller.commands, oper),
        "headers": create_uber_header_payload(caller.auth_headers, kwa),
        "files": kwa.get("files", return_preferred_default(oper, "list")),
        "verify": caller.ssl_verify,
        "proxy": caller.proxy,
        "timeout": caller.timeout,
        "user_agent": caller.user_agent,
        "expand_result": kwa.get("expand_result", False),
        "container": do_cont,
        "log_util": caller.log,
        "debug_record_count": caller.debug_record_count,
        "sanitize": caller.sanitize_log
    }
