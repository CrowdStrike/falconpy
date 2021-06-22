"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

response_policies - CrowdStrike Falcon Real Time Response Policies API interface class

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
from ._util import service_request, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._response_policies import _response_policies_endpoints as Endpoints


class Response_Policies(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryCombinedRTResponsePolicyMembers(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for members of a Response policy in your environment by providing an FQL filter and paging details.
           Returns a set of host details which match the filter criteria
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/queryCombinedRTResponsePolicyMembers
        operation_id = "queryCombinedRTResponsePolicyMembers"
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
    def queryCombinedRTResponsePolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for Response Policies in your environment by providing an FQL filter and paging details.
           Returns a set of Response Policies which match the filter criteria
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/queryCombinedRTResponsePolicies
        operation_id = "queryCombinedRTResponsePolicies"
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
    def performRTResponsePoliciesAction(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """Perform the specified action on the Response Policies specified in the request"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/performRTResponsePoliciesAction
        operation_id = "performRTResponsePoliciesAction"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def setRTResponsePoliciesPrecedence(self: object, body: dict) -> dict:
        """Sets the precedence of Response Policies based on the order of IDs specified in the request.
           The first ID specified will have the highest precedence and the last ID specified will have the lowest.
           You must specify all non-Default Policies for a platform when updating precedence
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/setRTResponsePoliciesPrecedence
        operation_id = "setRTResponsePoliciesPrecedence"
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
    def getRTResponsePolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve a set of Response Policies by specifying their IDs"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/response-policies/getRTResponsePolicies
        operation_id = "getRTResponsePolicies"
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

    def createRTResponsePolicies(self: object, body: dict) -> dict:
        """Create Response Policies by specifying details about the policy to create"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/createRTResponsePolicies
        operation_id = "createRTResponsePolicies"
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
    def deleteRTResponsePolicies(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """Delete a set of Response Policies by specifying their IDs"""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #              /response-policies/deleteRTResponsePolicies
        operation_id = "deleteRTResponsePolicies"
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

    def updateRTResponsePolicies(self: object, body: dict) -> dict:  # pylint: disable=C0103  # Matching API
        """Update Response Policies by specifying the ID of the policy and details to update"""
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/updateRTResponsePolicies
        operation_id = "updateRTResponsePolicies"
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
    def queryRTResponsePolicyMembers(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for members of a Response policy in your environment by providing an FQL filter and paging details.
           Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/queryRTResponsePolicyMembers
        operation_id = "queryRTResponsePolicyMembers"
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
    def queryRTResponsePolicies(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for Response Policies in your environment by providing an FQL filter with sort and/or paging details.
           This returns a set of Response Policy IDs that match the given criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/queryRTResponsePolicies
        operation_id = "queryRTResponsePolicies"
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
