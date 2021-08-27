"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

quarantine - Falcon Quarantine API Interface Class

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
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._quarantine import _quarantine_endpoints as Endpoints


class Quarantine(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def action_update_count(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Returns count of potentially affected quarantined files for each action.
        """
        # [GET]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ActionUpdateCount",
            keywords=kwargs,
            params=parameters
            )

    def get_aggregate_files(self: object, body: dict) -> dict:
        """
        Get quarantine file aggregates as specified via json in request body.
        """
        # [POST]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAggregateFiles",
            body=body
            )

    def get_quarantine_files(self: object, body: dict) -> dict:
        """
        Get quarantine file metadata for specified ids.
        """
        # [POST]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetQuarantineFiles",
            body=body
            )

    def update_quarantined_detects_by_id(self: object, body: dict) -> dict:
        """
        Apply action by quarantine file ids
        """
        # [PATCH]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateQuarantinedDetectsByIds",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_quarantine_files(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get quarantine file ids that match the provided filter criteria.
        """
        # [GET]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryQuarantineFiles",
            keywords=kwargs,
            params=parameters
            )

    def update_quarantined_detects_by_query(self: object, body: dict) -> dict:
        """
        Apply quarantine file actions by query.
        """
        # [PATCH]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateQfByQuery",
            body=body
            )
    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    ActionUpdateCount = action_update_count
    GetAggregateFiles = get_aggregate_files
    GetQuarantineFiles = get_quarantine_files
    UpdateQuarantinedDetectsByIds = update_quarantined_detects_by_id
    QueryQuarantineFiles = query_quarantine_files
    UpdateQfByQuery = update_quarantined_detects_by_query
