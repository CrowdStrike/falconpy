"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

detects - CrowdStrike Falcon Detections API interface class

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
from ._endpoint._detects import _detects_endpoints as Endpoints


class Detects(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def get_aggregate_detects(self: object, body: dict) -> dict:
        """
        Get detect aggregates as specified via json in request body.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/GetAggregateDetects
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAggregateDetects",
            body=body
            )

    def update_detects_by_ids(self: object, body: dict) -> dict:
        """
        Modify the state, assignee, and visibility of detections.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/UpdateDetectsByIdsV2
        body_validator = {
            "assigned_to_uuid": str,
            "ids": list,
            "show_in_ui": bool,
            "status": str,
            "comment": str
        }
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateDetectsByIdsV2",
            body=body,
            body_validator=body_validator,
            body_required=["ids"]
            )

    def get_detect_summaries(self: object, body: dict) -> dict:
        """
        View information about detections.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/GetDetectSummaries
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDetectSummaries",
            body=body,
            body_validator={"ids": list},
            body_required=["ids"]
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_detects(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for detection IDs that match a given query.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/QueryDetects
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryDetects",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetAggregateDetects = get_aggregate_detects
    UpdateDetectsByIdsV2 = update_detects_by_ids
    GetDetectSummaries = get_detect_summaries
    QueryDetects = query_detects
