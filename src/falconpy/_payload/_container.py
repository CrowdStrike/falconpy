"""Internal payload handling library - Falcon Container Payloads.

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


def image_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted image vulnerability request payload.

    {
        "applicationPackages": [
            {
                "libraries": [
                    {
                        "Hash": "string",
                        "LayerHash": "string",
                        "LayerIndex": 0,
                        "License": "string",
                        "Name": "string",
                        "Path": "string",
                        "Version": "string"
                    }
                ],
                "type": "string"
            }
        ],
        "osversion": "string",
        "packages": [
            {
                "LayerHash": "string",
                "LayerIndex": 0,
                "MajorVersion": "string",
                "PackageHash": "string",
                "PackageProvider": "string",
                "PackageSource": "string",
                "Product": "string",
                "SoftwareArchitecture": "string",
                "Status": "string",
                "Vendor": "string"
            }
        ]
    }
    """
    returned_payload = {}
    keys = ["osversion", "packages", "applicationPackages"]
    for key in keys:
        if passed_keywords.get(key, None):
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def registry_payload(passed_keywords: dict) -> dict:
    """Craft a properly formatted Registry Connection payload.

    {
        "credential": {
            "details": {
                "aws_iam_role": "string",
                "aws_external_id": "string",
                "username": "string",
                "password": "string",
                "domain_url": "string",
                "credential_type": "string",
                "compartment_ids": [
                    "string"
                ]
                "project_id": "string",
                "scope_name": "string",
                "service_account_json: {
                    "type": "string",
                    "private_key_id": "string",
                    "client_email": "string",
                    "client_id": "string",
                    "project_id": "string"
                }
            }
        },
        "id": "string",
        "state": "string",
        "type": "string",
        "url": "string",
        "url_uniqueness_key": "string",
        "user_defined_alias": "string"
    }
    """
    returned_payload = {}
    top_keys = [
        "credentials", "type", "url", "url_uniqueness_key", "user_defined_alias", "details", "id",
        "state", "credential"
        ]  # id and state are for update payloads only.
    detail_keys = [
        "aws_iam_role", "aws_external_id", "username", "password", "domain_url",
        "credential_type", "compartment_ids", "project_id", "service_account_json"
    ]
    for key in top_keys:
        if passed_keywords.get(key, None):
            # Fix for credentials -> credential parameter name change
            key = "credential" if key == "credentials" else key
            if isinstance(key, str):  # Reserved word collision, force a string comparison
                returned_payload[key] = passed_keywords.get(key)
            if key == "details":
                # details is a child branch of credentials.
                # Passing credential AND details may have unusual results
                # depending on the order of the keys received.
                returned_payload["credential"] = {}
                returned_payload["credential"]["details"] = passed_keywords.get(key)

    for key in detail_keys:
        if "credential" not in returned_payload:
            returned_payload["credential"] = {}
        if "details" not in returned_payload["credential"]:
            returned_payload["credential"]["details"] = {}
        if passed_keywords.get(key, None):
            # compartment_ids must be passed as a list.
            # service_account_json should be provided as a dictionary.
            returned_payload["credential"]["details"][key] = passed_keywords.get(key)

    return returned_payload
