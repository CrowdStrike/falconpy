"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

ioc - CrowdStrike Falcon Indicators of Compromise API interface class v2

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
from ._util import force_default, process_service_request, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._ioc import _ioc_endpoints as Endpoints
from ._endpoint._iocs import _iocs_endpoints as LegacyEndpoints


class IOC(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_combined(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get Combined for Indicators.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.combined.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_combined_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_get(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get Indicators by ids.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.get.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_create(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Create Indicators.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.create.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_create_v1",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_delete(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete Indicators by ids.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.delete.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_delete_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_update(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Update Indicators.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.update.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_update_v1",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def indicator_search(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Indicators.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioc/indicator.search.v1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="indicator_search_v1",
            keywords=kwargs,
            params=parameters
            )

    # These methods are ported from the legacy IOCS Service Class, as they have not been deprecated
    @force_default(defaults=["parameters"], default_types=["dict"])
    def devices_count(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Number of hosts in your customer account that have observed a given custom IOC.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesCount
        return process_service_request(
            calling_object=self,
            endpoints=LegacyEndpoints,
            operation_id="DevicesCount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def devices_ran_on(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find hosts that have observed a given custom IOC.
        For details about those hosts, use the hosts API interface.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesRanOn
        return process_service_request(
            calling_object=self,
            endpoints=LegacyEndpoints,
            operation_id="DevicesRanOn",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def processes_ran_on(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for processes associated with a custom IOC
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/ProcessesRanOn
        return process_service_request(
            calling_object=self,
            endpoints=LegacyEndpoints,
            operation_id="ProcessesRanOn",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def entities_processes(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        For the provided ProcessID retrieve the process details.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/entities.processes
        return process_service_request(
            calling_object=self,
            endpoints=LegacyEndpoints,
            operation_id="entities_processes",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    # These names are acceptable and match the API operation IDs.
    # They are defined here for ease of use purposes.
    indicator_combined_v1 = indicator_combined
    indicator_get_v1 = indicator_get
    indicator_create_v1 = indicator_create
    indicator_delete_v1 = indicator_delete
    indicator_update_v1 = indicator_update
    indicator_search_v1 = indicator_search
    # Legacy operation IDs, these are not acceptable PEP8 syntax
    # and are defined here for backwards compatibility / ease of
    # use purposes. These endpoints were ported from IOCS.py
    #                - jshcodes@CrowdStrike, see Discussion #319
    DevicesCount = devices_count
    DevicesRanOn = devices_ran_on
    ProcessesRanOn = processes_ran_on
