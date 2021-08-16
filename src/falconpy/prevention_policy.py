"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

prevention_policy - CrowdStrike Falcon Prevention Policy API interface class

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
from ._util import force_default, handle_single_argument, process_service_request
from ._service_class import ServiceClass
from ._endpoint._prevention_policies import _prevention_policies_endpoints as Endpoints


class PreventionPolicy(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Prevention Policy in your environment by providing an FQL filter
        and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /prevention-policies/queryCombinedPreventionPolicyMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedPreventionPolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Prevention Policies in your environment by providing an FQL filter and
        paging details. Returns a set of Prevention Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /prevention-policies/queryCombinedPreventionPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedPreventionPolicies",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def perform_policies_action(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Prevention Policies specified in the request.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /prevention-policies/performPreventionPoliciesAction
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="performPreventionPoliciesAction",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    def set_policies_precedence(self: object, body: dict) -> dict:
        """
        Sets the precedence of Prevention Policies based on the order of IDs specified in the request.
        The first ID specified will have the highest precedence and the last ID specified will have the lowest.
        You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /prevention-policies/setPreventionPoliciesPrecedence
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="setPreventionPoliciesPrecedence",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Prevention Policies by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/getPreventionPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getPreventionPolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def create_policies(self: object, body: dict) -> dict:
        """
        Create Prevention Policies by specifying details about the policy to create.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/createPreventionPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createPreventionPolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a set of Prevention Policies by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/deletePreventionPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deletePreventionPolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def update_policies(self: object, body: dict) -> dict:
        """
        Update Prevention Policies by specifying the ID of the policy and details to update.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/updatePreventionPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updatePreventionPolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Prevention Policy in your environment by providing an FQL filter
        and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /prevention-policies/queryPreventionPolicyMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryPreventionPolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Prevention Policies in your environment by providing an FQL filter
        and paging details. Returns a set of Prevention Policy IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies/queryPreventionPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryPreventionPolicies",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    queryCombinedPreventionPolicyMembers = query_combined_policy_members
    queryCombinedPreventionPolicies = query_combined_policies
    performPreventionPoliciesAction = perform_policies_action
    setPreventionPoliciesPrecedence = set_policies_precedence
    getPreventionPolicies = get_policies
    createPreventionPolicies = create_policies
    deletePreventionPolicies = delete_policies
    updatePreventionPolicies = update_policies
    queryPreventionPolicyMembers = query_policy_members
    queryPreventionPolicies = query_policies


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Prevention_Policy = PreventionPolicy  # pylint: disable=C0103
