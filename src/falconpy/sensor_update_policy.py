"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

sensor_update_policy - CrowdStrike Falcon Sensor Policy Management API interface class

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
from ._util import service_request, generate_error_result, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._sensor_update_policies import _sensor_update_policies_endpoints as Endpoints


class Sensor_Update_Policy(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def revealUninstallToken(self: object, body: dict) -> dict:
        """
        Reveals an uninstall token for a specific device.
        To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device_id'.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/revealUninstallToken
        operation_id = "revealUninstallToken"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryCombinedSensorUpdateBuilds(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve available builds for use with Sensor Update Policies.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdateBuilds
        operation_id = "queryCombinedSensorUpdateBuilds"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryCombinedSensorUpdatePolicyMembers(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Sensor Update Policy in your environment by providing an FQL
        filter and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdatePolicyMembers
        operation_id = "queryCombinedSensorUpdatePolicyMembers"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryCombinedSensorUpdatePolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Sensor Update Policies in your environment by providing an FQL filter and paging details.
        Returns a set of Sensor Update Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdatePolicies
        operation_id = "queryCombinedSensorUpdatePolicies"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryCombinedSensorUpdatePoliciesV2(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Sensor Update Policies with additional support for uninstall protection in your environment
        by providing an FQL filter and paging details.
        Returns a set of Sensor Update Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdatePoliciesV2
        operation_id = "queryCombinedSensorUpdatePoliciesV2"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def performSensorUpdatePoliciesAction(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Sensor Update Policies specified in the request.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/performSensorUpdatePoliciesAction
        _allowed_actions = ['add-host-group', 'disable', 'enable', 'remove-host-group']
        operation_id = "performSensorUpdatePoliciesAction"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        if "action_name" not in parameter_payload:
            parameter_payload["action_name"] = "Not Specified"
        if parameter_payload["action_name"].lower() in _allowed_actions:
            returned = service_request(caller=self,
                                       method="POST",
                                       endpoint=target_url,
                                       body=body_payload,
                                       params=parameter_payload,
                                       headers=header_payload,
                                       verify=self.ssl_verify
                                       )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")

        return returned

    def setSensorUpdatePoliciesPrecedence(self: object, body: dict) -> dict:
        """
        Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request.
        The first ID specified will have the highest precedence and the last ID specified will have the lowest.
        You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/setSensorUpdatePoliciesPrecedence
        operation_id = "setSensorUpdatePoliciesPrecedence"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def getSensorUpdatePolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Sensor Update Policies by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/getSensorUpdatePolicies
        operation_id = "getSensorUpdatePolicies"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createSensorUpdatePolicies(self: object, body: dict) -> dict:
        """
        Create Sensor Update Policies by specifying details about the policy to create.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/createSensorUpdatePolicies
        operation_id = "createSensorUpdatePolicies"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def deleteSensorUpdatePolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a set of Sensor Update Policies by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          ...  /sensor-update-policies/deleteSensorUpdatePolicies
        operation_id = "deleteSensorUpdatePolicies"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateSensorUpdatePolicies(self: object, body: dict) -> dict:
        """
        Update Sensor Update Policies by specifying the ID of the policy and details to update.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /sensor-update-policies/updateSensorUpdatePolicies
        operation_id = "updateSensorUpdatePolicies"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def getSensorUpdatePoliciesV2(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Sensor Update Policies with additional
        support for uninstall protection by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/getSensorUpdatePoliciesV2
        operation_id = "getSensorUpdatePoliciesV2"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createSensorUpdatePoliciesV2(self: object, body: dict) -> dict:
        """
        Create Sensor Update Policies by specifying details about the
        policy to create with additional support for uninstall protection.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/createSensorUpdatePoliciesV2
        operation_id = "createSensorUpdatePoliciesV2"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateSensorUpdatePoliciesV2(self: object, body: dict) -> dict:
        """
        Update Sensor Update Policies by specifying the ID of the policy
        and details to update with additional support for uninstall protection.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /sensor-update-policies/updateSensorUpdatePoliciesV2
        operation_id = "updateSensorUpdatePoliciesV2"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def querySensorUpdatePolicyMembers(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Sensor Update Policy in your environment by providing an FQL
        filter and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/querySensorUpdatePolicyMembers
        operation_id = "querySensorUpdatePolicyMembers"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def querySensorUpdatePolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Sensor Update Policies in your environment by providing an FQL filter and
        paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/querySensorUpdatePolicies
        operation_id = "querySensorUpdatePolicies"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
