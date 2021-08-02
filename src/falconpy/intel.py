"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

host_groups - CrowdStrike Falcon Threat Intelligence API interface class

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
# pylint: disable=C0103  # Aligning method names to API operation IDs
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._intel import _intel_endpoints as Endpoints


class Intel(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryIntelActorEntities(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get info about actors that match provided FQL filters.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorEntities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelActorEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryIntelIndicatorEntities(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get info about indicators that match provided FQL filters.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorEntities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelIndicatorEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryIntelReportEntities(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get info about reports that match provided FQL filters.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportEntities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelReportEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetIntelActorEntities(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve specific actors using their actor IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelActorEntities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelActorEntities",
            keywords=kwargs,
            params=parameters
            )

    def GetIntelIndicatorEntities(self: object, body: dict) -> dict:
        """
        Retrieve specific indicators using their indicator IDs.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelIndicatorEntities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelIndicatorEntities",
            method="POST",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetIntelReportPDF(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Return a Report PDF attachment.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportPDF
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelReportPDF",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetIntelReportEntities(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve specific reports using their report IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportEntities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelReportEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetIntelRuleFile(self: object, parameters: dict = None, **kwargs) -> dict:
        # There is an optional header you can see Accept to choose the result format. See Swagger.
        """
        Download earlier rule sets.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleFile
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelRuleFile",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetLatestIntelRuleFile(self: object, parameters: dict = None, **kwargs) -> dict:
        # There is an optional header you can see Accept to choose the result format. See Swagger.
        """
        Download the latest rule set.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetLatestIntelRuleFile
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetLatestIntelRuleFile",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetIntelRuleEntities(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve details for rule sets for the specified ids.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleEntities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntelRuleEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryIntelActorIds(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get actor IDs that match provided FQL filters.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorIds
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelActorIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryIntelIndicatorIds(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get indicators IDs that match provided FQL filters.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorIds
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelIndicatorIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryIntelReportIds(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get report IDs that match provided FQL filters.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelReportIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryIntelRuleIds(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for rule IDs that match provided filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIntelRuleIds",
            keywords=kwargs,
            params=parameters
            )
