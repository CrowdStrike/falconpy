"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

sensor_download - Falcon Sensor Download API Interface Class

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
import os
from ._util import service_request, generate_ok_result, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._sensor_download import _sensor_download_endpoints as Endpoints


class Sensor_Download(ServiceClass):
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetCombinedSensorInstallersByQuery(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve all metadata for installers from provided query
        """
        operation_id = "GetCombinedSensorInstallersByQuery"
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
    def DownloadSensorInstallerById(self: object,
                                    parameters: dict = None,
                                    file_name: str = None,
                                    download_path: str = None,
                                    **kwargs) -> object:
        """
        Download the sensor by the sha256 id, into the specified directory.
        The path will be created for the user if it does not already exist
        """
        operation_id = "DownloadSensorInstallerById"
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
        if file_name and download_path and isinstance(returned, bytes):
            os.makedirs(download_path, exist_ok=True)
            # write the newly downloaded sensor into the aforementioned directory with provided file name
            with open(os.path.join(download_path, file_name), "wb") as sensor:
                sensor.write(returned)
            returned = generate_ok_result(message="Download successful")
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetSensorInstallersEntities(self: object, parameters: dict = None, **kwargs) -> object:
        """
        For a given list of SHA256's, retrieve the metadata for each installer
        such as the release_date and version among other fields
        """
        operation_id = "GetSensorInstallersEntities"
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

    def GetSensorInstallersCCIDByQuery(self: object) -> dict:
        """
        Retrieve the CID for the current oauth environment
        """
        operation_id = "GetSensorInstallersCCIDByQuery"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetSensorInstallersByQuery(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a list of SHA256 for installers based on the filter
        """
        operation_id = "GetSensorInstallersByQuery"
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
