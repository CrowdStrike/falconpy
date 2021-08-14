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
import os
from ._util import generate_ok_result, force_default, handle_single_argument, process_service_request
from ._service_class import ServiceClass
from ._endpoint._sensor_download import _sensor_download_endpoints as Endpoints


class SensorDownload(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_combined_sensor_installers_by_query(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve all metadata for installers from provided query
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /sensor-download/GetCombinedSensorInstallersByQuery
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCombinedSensorInstallersByQuery",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def download_sensor_installer(self: object,
                                  *args,
                                  parameters: dict = None,
                                  file_name: str = None,
                                  download_path: str = None,
                                  **kwargs) -> object:
        """
        Download the sensor by the sha256 id, into the specified directory.
        The path will be created for the user if it does not already exist
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/DownloadSensorInstallerById
        returned = process_service_request(
                        calling_object=self,
                        endpoints=Endpoints,
                        operation_id="DownloadSensorInstallerById",
                        keywords=kwargs,
                        params=handle_single_argument(args, parameters, "ids")
                        )
        if file_name and download_path and isinstance(returned, bytes):
            os.makedirs(download_path, exist_ok=True)
            # write the newly downloaded sensor into the aforementioned directory with provided file name
            with open(os.path.join(download_path, file_name), "wb") as sensor:
                sensor.write(returned)
            returned = generate_ok_result(message="Download successful")

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sensor_installer_entities(self: object, parameters: dict = None, **kwargs) -> object:
        """
        For a given list of SHA256's, retrieve the metadata for each installer
        such as the release_date and version among other fields
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersEntities
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersEntities",
            keywords=kwargs,
            params=parameters
            )

    def get_sensor_installer_ccid(self: object) -> dict:
        """
        Retrieve the CID for the current oauth environment
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersCCIDByQuery
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersCCIDByQuery"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sensor_installers_by_query(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a list of SHA256 for installers based on the filter
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersByQuery
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersByQuery",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetCombinedSensorInstallersByQuery = get_combined_sensor_installers_by_query
    DownloadSensorInstallerById = download_sensor_installer
    GetSensorInstallersEntities = get_sensor_installer_entities
    GetSensorInstallersCCIDByQuery = get_sensor_installer_ccid
    GetSensorInstallersByQuery = get_sensor_installers_by_query


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Sensor_Download = SensorDownload  # pylint: disable=C0103
