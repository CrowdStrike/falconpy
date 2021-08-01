"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

device_control_policies - CrowdStrike Falcon Device Control Policies API interface class

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
from ._endpoint._device_control_policies import _device_control_policies_endpoints as Endpoints


class Device_Control_Policies(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryCombinedDeviceControlPolicyMembers(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Device Control Policy in your environment by providing an FQL filter
        and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...   /device-control-policies/queryCombinedDeviceControlPolicyMembers
        operation_id = "queryCombinedDeviceControlPolicyMembers"
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
    def queryCombinedDeviceControlPolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Device Control Policies in your environment by providing an FQL filter and
        paging details. Returns a set of Device Control Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /device-control-policies/queryCombinedDeviceControlPolicies
        operation_id = "queryCombinedDeviceControlPolicies"
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
    def performDeviceControlPoliciesAction(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Device Control Policies in your environment by providing an FQL filter
        and paging details. Returns a set of Device Control Policies which match the filter criteria.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /device-control-policies/performDeviceControlPoliciesAction
        _allowed_actions = ['add-host-group', 'disable', 'enable', 'remove-host-group']
        operation_id = "performDeviceControlPoliciesAction"
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

    def setDeviceControlPoliciesPrecedence(self: object, body: dict) -> dict:
        """
        Sets the precedence of Device Control Policies based on the order of IDs specified in the request.
        The first ID specified will have the highest precedence and the last ID specified will have the lowest.
        You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /device-control-policies/performDeviceControlPoliciesAction
        operation_id = "setDeviceControlPoliciesPrecedence"
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
    def getDeviceControlPolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Device Control Policies by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /device-control-policies/getDeviceControlPolicies
        operation_id = "getDeviceControlPolicies"
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

    def createDeviceControlPolicies(self: object, body: dict) -> dict:
        """
        Create Device Control Policies by specifying details about the policy to create.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /device-control-policies/createDeviceControlPolicies
        operation_id = "createDeviceControlPolicies"
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
    def deleteDeviceControlPolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a set of Device Control Policies by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          ...  /device-control-policies/createDeviceControlPolicies
        operation_id = "deleteDeviceControlPolicies"
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

    def updateDeviceControlPolicies(self: object, body: dict) -> dict:
        """
        Update Device Control Policies by specifying the ID of the policy and details to update.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /device-control-policies/updateDeviceControlPolicies
        operation_id = "updateDeviceControlPolicies"
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
    def queryDeviceControlPolicyMembers(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Device Control Policy in your environment by providing an FQL filter
        and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /device-control-policies/queryDeviceControlPolicyMembers
        operation_id = "queryDeviceControlPolicyMembers"
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
    def queryDeviceControlPolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Device Control Policies in your environment by providing an FQL filter and paging details.
        Returns a set of Device Control Policy IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /device-control-policies/queryDeviceControlPolicyMembers
        operation_id = "queryDeviceControlPolicies"
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
