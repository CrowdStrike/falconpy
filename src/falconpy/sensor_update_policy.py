"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

iocs - CrowdStrike Falcon Sensor Policy Management API interface class

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
from ._util import parse_id_list, service_request, generate_error_result
from ._service_class import ServiceClass


class Sensor_Update_Policy(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def revealUninstallToken(self: object, body: dict) -> dict:
        """ Reveals an uninstall token for a specific device.
            To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device_id'.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/revealUninstallToken
        FULL_URL = self.base_url+'/policy/combined/reveal-uninstall-token/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryCombinedSensorUpdateBuilds(self: object, parameters: dict = None) -> dict:
        """ Retrieve available builds for use with Sensor Update Policies. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdateBuilds
        FULL_URL = self.base_url+'/policy/combined/sensor-update-builds/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryCombinedSensorUpdatePolicyMembers(self: object, parameters: dict = None) -> dict:
        """ Search for members of a Sensor Update Policy in your environment by providing an FQL
            filter and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdatePolicyMembers
        FULL_URL = self.base_url+'/policy/combined/sensor-update-members/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryCombinedSensorUpdatePolicies(self: object, parameters: dict = None) -> dict:
        """ Search for Sensor Update Policies in your environment by providing an FQL filter and paging details.
            Returns a set of Sensor Update Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/combined/sensor-update/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryCombinedSensorUpdatePoliciesV2(self: object, parameters: dict = None) -> dict:
        """ Search for Sensor Update Policies with additional support for uninstall protection in your environment
            by providing an FQL filter and paging details.
            Returns a set of Sensor Update Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdatePoliciesV2
        FULL_URL = self.base_url+'/policy/combined/sensor-update/v2'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def performSensorUpdatePoliciesAction(self: object, parameters: dict, body: dict, action_name: str = None) -> dict:
        """ Perform the specified action on the Sensor Update Policies specified in the request. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/performSensorUpdatePoliciesAction
        if "action_name" in parameters:
            action_name = parameters["action_name"].lower()
        ALLOWED_ACTIONS = ['add-host-group', 'disable', 'enable', 'remove-host-group']
        if action_name.lower() in ALLOWED_ACTIONS:
            FULL_URL = self.base_url+'/policy/entities/sensor-update-actions/v1'
            HEADERS = self.headers
            BODY = body
            PARAMS = parameters
            returned = service_request(caller=self,
                                       method="POST",
                                       endpoint=FULL_URL,
                                       params=PARAMS,
                                       body=BODY,
                                       headers=HEADERS,
                                       verify=self.ssl_verify
                                       )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")

        return returned

    def setSensorUpdatePoliciesPrecedence(self: object, body: dict) -> dict:
        """ Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request.
            The first ID specified will have the highest precedence and the last ID specified will have the lowest.
            You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/setSensorUpdatePoliciesPrecedence
        FULL_URL = self.base_url+'/policy/entities/sensor-update-precedence/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def getSensorUpdatePolicies(self: object, ids) -> dict:
        """ Retrieve a set of Sensor Update Policies by specifying their IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/getSensorUpdatePolicies
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createSensorUpdatePolicies(self: object, body: dict) -> dict:
        """ Create Sensor Update Policies by specifying details about the policy to create. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/createSensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteSensorUpdatePolicies(self: object, ids) -> dict:
        """ Delete a set of Sensor Update Policies by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          ...  /sensor-update-policies/deleteSensorUpdatePolicies
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateSensorUpdatePolicies(self: object, body: dict) -> dict:
        """ Update Sensor Update Policies by specifying the ID of the policy and details to update. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /sensor-update-policies/updateSensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def getSensorUpdatePoliciesV2(self: object, ids) -> dict:
        """ Retrieve a set of Sensor Update Policies with additional
            support for uninstall protection by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/getSensorUpdatePoliciesV2
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v2?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createSensorUpdatePoliciesV2(self: object, body: dict) -> dict:
        """ Create Sensor Update Policies by specifying details about the
            policy to create with additional support for uninstall protection.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/createSensorUpdatePoliciesV2
        FULL_URL = self.base_url+'/policy/entities/sensor-update/v2'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateSensorUpdatePoliciesV2(self: object, body: dict) -> dict:
        """ Update Sensor Update Policies by specifying the ID of the policy
            and details to update with additional support for uninstall protection.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /sensor-update-policies/updateSensorUpdatePoliciesV2
        FULL_URL = self.base_url+'/users/entities/users/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def querySensorUpdatePolicyMembers(self: object, parameters: dict = None) -> dict:
        """ Search for members of a Sensor Update Policy in your environment by providing an FQL
            filter and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/querySensorUpdatePolicyMembers
        FULL_URL = self.base_url+'/policy/queries/sensor-update-members/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def querySensorUpdatePolicies(self: object, parameters: dict = None) -> dict:
        """ Search for Sensor Update Policies in your environment by providing an FQL filter and
            paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/querySensorUpdatePolicies
        FULL_URL = self.base_url+'/policy/queries/sensor-update/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned
