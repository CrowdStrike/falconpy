"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

firewall_policies - CrowdStrike Falcon Firewall Policy API interface class

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
from ._endpoint._firewall_policies import _firewall_policies_endpoints as Endpoints


class Firewall_Policies(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryCombinedFirewallPolicyMembers(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Firewall Policy in your environment by providing an FQL filter
        and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /firewall-policies/queryCombinedFirewallPolicyMembers
        operation_id = "queryCombinedFirewallPolicyMembers"
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
    def queryCombinedFirewallPolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Firewall Policies in your environment by providing an FQL filter and paging details.
        Returns a set of Firewall Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/queryCombinedFirewallPolicies
        operation_id = "queryCombinedFirewallPolicies"
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
    def performFirewallPoliciesAction(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Firewall Policies specified in the request.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /firewall-policies/performFirewallPoliciesAction

        _allowed_actions = ['add-host-group', 'disable', 'enable', 'remove-host-group']
        operation_id = "performFirewallPoliciesAction"
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

    def setFirewallPoliciesPrecedence(self: object, body: dict) -> dict:
        """
        Sets the precedence of Firewall Policies based on the order of IDs specified in the request.
        The first ID specified will have the highest precedence and the last ID specified will have the lowest.
        You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /firewall-policies/setFirewallPoliciesPrecedence
        operation_id = "setFirewallPoliciesPrecedence"
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
    def getFirewallPolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Firewall Policies by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/getFirewallPolicies
        operation_id = "getFirewallPolicies"
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

    @force_default(defaults=["parameters"], default_types=["dict"])
    def createFirewallPolicies(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Create Firewall Policies by specifying details about the policy to create.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/createFirewallPolicies
        operation_id = "createFirewallPolicies"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def deleteFirewallPolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a set of Firewall Policies by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/deleteFirewallPolicies
        operation_id = "deleteFirewallPolicies"
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

    def updateFirewallPolicies(self: object, body: dict) -> dict:
        """
        Update Firewall Policies by specifying the ID of the policy and details to update.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/updateFirewallPolicies
        operation_id = "updateFirewallPolicies"
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
    def queryFirewallPolicyMembers(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Firewall Policy in your environment by providing an FQL filter and
        paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/queryFirewallPolicyMembers
        operation_id = "queryFirewallPolicyMembers"
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
    def queryFirewallPolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Firewall Policies in your environment by providing an FQL filter and paging details.
        Returns a set of Firewall Policy IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies/queryFirewallPolicies
        operation_id = "queryFirewallPolicies"
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
