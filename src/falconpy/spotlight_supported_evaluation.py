"""CrowdStrike Falcon Spotlight Supported Evaluation API interface class.

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
from typing import Dict, Union
from ._util import force_default, process_service_request
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._spotlight_supported_evaluation import _spotlight_supported_evaluation_endpoints as Endpoints


class SpotlightSupportedEvaluation(ServiceClass):
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

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_supported_evaluations(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Perform a combined query and get for RiskSupportedEvaluation entities.

        Keyword arguments:
        after -- A pagination token used with the limit parameter to manage pagination
                 of results. On your first request, don't provide an after token. On
                 subsequent requests, provide the after token from the previous response
                 to continue from that place in the results. String.
        filter -- Filter items using a query in Falcon Query Language (FQL). String.
                  Wildcards * and empty filter values are unsupported.
                  Available filter fields that support exact match:
                    id                risk_id
                    risk_provider     finding_provider
                    platform
                  Available filter fields that support range comparisons (>, <, >=, <=):
                    created_timestamp   updated_timestamp
        limit -- The number of items to return in this response (default: 100, max: 400).
                 Use with the after parameter to manage pagination of results. Integer.
        offset -- Starting index of overall result set from which to return ids. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.
        risk_provider -- Zero or more risk providers. Zero means all. String or list of strings.
                         Supported values: S (for Falcon sensor).
        sort -- Sort vulnerabilities by their properties. String.
                Available sort options: created_timestamp|asc/desc, updated_timestamp|asc/desc.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/spotlight-supported-evaluation/combinedSupportedEvaluationExt
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="combinedSupportedEvaluationExt",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    combinedSupportedEvaluationExt = get_supported_evaluations
