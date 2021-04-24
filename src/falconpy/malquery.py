"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

malquery - Falcon MalQuery API Interface Class

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
import sys
from ._util import service_request, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._malquery import _malquery_endpoints as Endpoints


class MalQuery(ServiceClass):  # pylint: disable=C0103  # Matching API
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class, a
       existing instance of the authentication class as an object or a
       valid set of credentials.
    """
    def GetMalQueryQuotasV1(self: object) -> dict:  # pylint: disable=C0103  # Matching API
        """Get information about search and download quotas in your environment"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery/GetMalQueryQuotasV1
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def PostMalQueryFuzzySearchV1(self: object, body: dict) -> dict:  # pylint: disable=C0103  # Matching API
        """Search Falcon MalQuery quickly, but with more potential for false positives.
           Search for a combination of hex patterns and strings in order to identify
           samples based upon file content at byte level granularity.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery/PostMalQueryFuzzySearchV1
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
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
    def GetMalQueryDownloadV1(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """Download a file indexed by MalQuery. Specify the file using its SHA256.
           Only one file is supported at this time.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery/GetMalQueryDownloadV1
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetMalQueryMetadataV1(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """Retrieve indexed files metadata by their hash"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery/GetMalQueryMetadataV1
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetMalQueryRequestV1(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  # Matching API
        """Check the status and results of an asynchronous request, such as hunt or exact-search.
           Supports a single request id at this time.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery/GetMalQueryRequestV1
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetMalQueryEntitiesSamplesFetchV1(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """Fetch a zip archive with password 'infected' containing the samples.
           Call this once the /entities/samples-multidownload request has finished processing
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery/GetMalQueryEntitiesSamplesFetchV1
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def PostMalQueryEntitiesSamplesMultidownloadV1(self: object, body: dict) -> dict:  # pylint: disable=C0103  # Matching API
        """Schedule samples for download. Use the result id with the /request endpoint to check
           if the download is ready after which you can call the /entities/samples-fetch to get the zip.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /malquery/PostMalQueryEntitiesSamplesMultidownloadV1
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
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

    def PostMalQueryExactSearchV1(self: object, body: dict) -> dict:  # pylint: disable=C0103  # Matching API
        """Search Falcon MalQuery for a combination of hex patterns and strings in order to identify samples
           based upon file content at byte level granularity. You can filter results on criteria such as file type,
           file size and first seen date. Returns a request id which can be used with the /request endpoint.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery/PostMalQueryExactSearchV1
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
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

    def PostMalQueryHuntV1(self: object, body: dict) -> dict:  # pylint: disable=C0103  # Matching API
        """Schedule a YARA-based search for execution.
           Returns a request id which can be used with the /request endpoint.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery/PostMalQueryHuntV1
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
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
