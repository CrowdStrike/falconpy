"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

spotlight_vulnerabilities - CrowdStrike Falcon Spotlight Vulnerability API interface class

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
from ._endpoint._spotlight_vulnerabilities import _spotlight_vulnerabilities_endpoints as Endpoints


class SpotlightVulnerabilities(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_vulnerabilities(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get details on vulnerabilities by providing one or more IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/spotlight-vulnerabilities/getVulnerabilities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getVulnerabilities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_vulnerabilities(self: object, parameters: dict = None,  **kwargs) -> dict:
        """
        Search for Vulnerabilities in your environment by providing an FQL filter
        and paging details. Returns a set of Vulnerability IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/spotlight-vulnerabilities/queryVulnerabilities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryVulnerabilities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_remediations(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get details on remediations by providing one or more IDs.
        """
        # [GET] Not in swagger
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getRemediations",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    getVulnerabilities = get_vulnerabilities
    queryVulnerabilities = query_vulnerabilities
    getRemediations = get_remediations


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Spotlight_Vulnerabilities = SpotlightVulnerabilities  # pylint: disable=C0103
