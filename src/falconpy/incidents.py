"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

incidents - CrowdStrike Falcon Incidents API interface class

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
from ._endpoint._incidents import _incidents_endpoints as Endpoints


class Incidents(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def crowdscore(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query environment wide CrowdScore and return the entity data.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/CrowdScore
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CrowdScore",
            keywords=kwargs,
            params=parameters
            )

    def get_behaviors(self: object, body: dict) -> dict:
        """
        Get details on behaviors by providing behavior IDs.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/GetBehaviors
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetBehaviors",
            body=body
            )

    def perform_incident_action(self: object, body: dict) -> dict:
        """
        Perform a set of actions on one or more incidents, such as
        adding tags or comments or updating the incident name or description.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/PerformIncidentAction
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PerformIncidentAction",
            body=body
            )

    def get_incidents(self: object, body: dict) -> dict:
        """
        Get details on incidents by providing incident IDs.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/GetIncidents
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIncidents",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_behaviors(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for behaviors by providing an FQL filter, sorting, and paging details.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/QueryBehaviors
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryBehaviors",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_incidents(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for incidents by providing an FQL filter, sorting, and paging details.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/QueryIncidents
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIncidents",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    CrowdScore = crowdscore
    GetBehaviors = get_behaviors
    PerformIncidentAction = perform_incident_action
    GetIncidents = get_incidents
    QueryBehaviors = query_behaviors
    QueryIncidents = query_incidents
