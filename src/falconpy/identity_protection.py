"""CrowdStrike Identity Protection API Interface Class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

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
from ._util import process_service_request, force_default
from ._service_class import ServiceClass
from ._endpoint._identity_protection import _identity_protection_endpoints as Endpoints


class IdentityProtection(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["body"], default_types=["dict"])
    def graphql(self: object, body: dict = None, **kwargs) -> dict:
        r"""Identity Protection GraphQL API.

        Allows to retrieve entities, timeline activities, identity-based incidents and
        security assessment. Allows to perform actions on entities and identity-based incidents.

        Keyword arguments:
        body -- full body payload, not required if keywords are used.
                {
                    "query": "string"
                }
        query -- JSON-similar string.

        This method only supports keywords for providing arguments.
        Currently using a non-standard body payload format.
        Example payload:
        {
            "query": "{\n  entities(first: 1)\n  {\n    nodes {\n      entityId    \n    }\n  }\n}"
        }

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html
                   /identity-protection/api.preempt.proxy.post.graphql
        """
        if not body:
            body = {}
            body["query"] = kwargs.get("query", "{}")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="api_preempt_proxy_post_graphql",
            body=body
            )

    # This method name aligns to the operation ID in the API but
    # does not conform to snake_case / PEP8 and is defined here
    # for backwards compatibility / ease of use purposes
    GraphQL = graphql


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Identity_Protection = IdentityProtection  # pylint: disable=C0103
