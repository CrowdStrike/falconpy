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
from ._util import process_service_request, force_default, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._response_policies import _response_policies_endpoints as Endpoints


class ResponsePolicies(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Response policy in your environment by providing an FQL filter and paging details.
        Returns a set of host details which match the filter criteria
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/queryCombinedRTResponsePolicyMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedRTResponsePolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Response Policies in your environment by providing an FQL filter and paging details.
        Returns a set of Response Policies which match the filter criteria
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/queryCombinedRTResponsePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedRTResponsePolicies",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def perform_policies_action(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Response Policies specified in the request
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/performRTResponsePoliciesAction
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="performRTResponsePoliciesAction",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    def set_policies_precedence(self: object, body: dict) -> dict:
        """
        Sets the precedence of Response Policies based on the order of IDs specified in the request.
        The first ID specified will have the highest precedence and the last ID specified will have the lowest.
        You must specify all non-Default Policies for a platform when updating precedence
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/setRTResponsePoliciesPrecedence
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="setRTResponsePoliciesPrecedence",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Response Policies by specifying their IDs
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/response-policies/getRTResponsePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getRTResponsePolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def create_policies(self: object, body: dict) -> dict:
        """
        Create Response Policies by specifying details about the policy to create
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/createRTResponsePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createRTResponsePolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """
        Delete a set of Response Policies by specifying their IDs
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #              /response-policies/deleteRTResponsePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteRTResponsePolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def update_policies(self: object, body: dict) -> dict:
        """
        Update Response Policies by specifying the ID of the policy and details to update
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/updateRTResponsePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateRTResponsePolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Response policy in your environment by providing an FQL filter and paging details.
        Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/queryRTResponsePolicyMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryRTResponsePolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Response Policies in your environment by providing an FQL filter with sort and/or paging details.
        This returns a set of Response Policy IDs that match the given criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /response-policies/queryRTResponsePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryRTResponsePolicies",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    queryCombinedRTResponsePolicyMembers = query_combined_policy_members
    queryCombinedRTResponsePolicies = query_combined_policies
    performRTResponsePoliciesAction = perform_policies_action
    setRTResponsePoliciesPrecedence = set_policies_precedence
    getRTResponsePolicies = get_policies
    createRTResponsePolicies = create_policies
    deleteRTResponsePolicies = delete_policies
    updateRTResponsePolicies = update_policies
    queryRTResponsePolicyMembers = query_policy_members
    queryRTResponsePolicies = query_policies


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Response_Policies = ResponsePolicies  # pylint: disable=C0103
