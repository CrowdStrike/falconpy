"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

quick_scan - Falcon Quick Scan API Interface Class

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
from ._endpoint._quick_scan import _quick_scan_endpoints as Endpoints


class QuickScan(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def get_scans_aggregates(self: object, body: dict) -> dict:
        """
        Get scans aggregations as specified via json in request body.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/GetScansAggregates
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetScansAggregates",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scans(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Check the status of a volume scan. Time required for analysis increases with the number
        of samples in a volume but usually it should take less than 1 minute
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/GetScans
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetScans",
            keywords=kwargs,
            params=parameters
            )

    def scan_samples(self: object, body: dict) -> dict:
        """
        Get scans aggregations as specified via json in request body.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/ScanSamples
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ScanSamples",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_submissions(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find IDs for submitted scans by providing an FQL filter and paging details.
        Returns a set of volume IDs that match your criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/QuerySubmissionsMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QuerySubmissionsMixin0",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetScansAggregates = get_scans_aggregates
    GetScans = get_scans
    ScanSamples = scan_samples
    QuerySubmissionsMixin0 = query_submissions


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Quick_Scan = QuickScan  # pylint: disable=C0103
