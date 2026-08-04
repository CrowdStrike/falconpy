"""Falcon Sensor Download API Interface Class.

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
import os
from typing import Dict, Union
from requests import Response
from ._util import generate_ok_result, force_default
from ._util import handle_single_argument, process_service_request
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._sensor_download import _sensor_download_endpoints as Endpoints


class SensorDownload(ServiceClass):
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
    def get_combined_sensor_installers_by_query(self: object,
                                                parameters: dict = None,
                                                **kwargs
                                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve all metadata for installers from provided query.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetCombinedSensorInstallersByQuery

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        limit : int (1-5000)
            The maximum number of records to return.
        offset : int
            The first item to return, where 0 is the latest item. (Integer)
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. status.desc or hostname.asc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCombinedSensorInstallersByQuery",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_combined_sensor_installers_by_query_v2(self: object,
                                                   parameters: dict = None,
                                                   **kwargs
                                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve all metadata for installers from provided query.

        Also provides architectural details.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetCombinedSensorInstallersByQueryV2

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        limit : int (1-5000)
            The maximum number of records to return.
        offset : int
            The first item to return, where 0 is the latest item. (Integer)
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. status.desc or hostname.asc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCombinedSensorInstallersByQueryV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def download_sensor_installer(self: object,
                                  *args,
                                  parameters: dict = None,
                                  file_name: str = None,
                                  download_path: str = None,
                                  **kwargs) -> Union[Dict[str, Union[int, dict]], Result, Response]:
        """Download the sensor by the sha256 id, into the specified directory.

        The path will be created for the user if it does not already exist.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/DownloadSensorInstallerById

        Keyword arguments
        -----------------
        download_path : str
            Path to the folder to save installer file.
            Must be present to cause a file download.
        id : str
            SHA256 of the installer to download.
        file_name : str
            Name to use for saved file. Must be present to cause a file download.
        parameters : dict
            Full parameters payload, not required if id is provided as a keyword.
        stream : bool
            Enable streaming download of the file.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        binary object on SUCCESS, dict object containing API response on FAILURE.
        """
        returned = process_service_request(
                        calling_object=self,
                        endpoints=Endpoints,
                        operation_id="DownloadSensorInstallerById",
                        keywords=kwargs,
                        params=handle_single_argument(args, parameters, "ids"),
                        stream=kwargs.get("stream", False)
                        )
        if file_name and download_path and isinstance(returned, bytes):
            os.makedirs(download_path, exist_ok=True)
            # write the newly downloaded sensor into the
            # aforementioned directory with provided file name
            with open(os.path.join(download_path, file_name), "wb") as sensor:
                sensor.write(returned)
            returned = generate_ok_result(message="Download successful")

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def download_sensor_installer_v2(self: object,
                                     *args,
                                     parameters: dict = None,
                                     file_name: str = None,
                                     download_path: str = None,
                                     **kwargs) -> Union[Dict[str, Union[int, dict]], Result, Response]:
        """Download the sensor by the sha256 id, into the specified directory.

        The path will be created for the user if it does not already exist.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/DownloadSensorInstallerByIdV2

        Keyword arguments
        -----------------
        download_path : str
            Path to the folder to save installer file.
            Must be present to cause a file download.
        id : str
            SHA256 of the installer to download.
        file_name : str
            Name to use for saved file. Must be present to cause a file download.
        parameters : dict
            Full parameters payload, not required if id is provided as a keyword.
        stream : bool
            Enable streaming download of the file.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        binary object on SUCCESS, dict object containing API response on FAILURE.
        """
        returned = process_service_request(
                        calling_object=self,
                        endpoints=Endpoints,
                        operation_id="DownloadSensorInstallerByIdV2",
                        keywords=kwargs,
                        params=handle_single_argument(args, parameters, "ids"),
                        stream=kwargs.get("stream", False)
                        )
        if file_name and download_path and isinstance(returned, bytes):
            os.makedirs(download_path, exist_ok=True)
            # write the newly downloaded sensor into the
            # aforementioned directory with provided file name
            with open(os.path.join(download_path, file_name), "wb") as sensor:
                sensor.write(returned)
            returned = generate_ok_result(message="Download successful")

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sensor_installer_entities(self: object,
                                      *args,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> object:
        """For a given list of SHA256's, retrieve the metadata for each installer.

        (Examples: release_date, version).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersEntities

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of SHA256s for installers to retrieve details for.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sensor_installer_entities_v2(self: object,
                                         *args,
                                         parameters: dict = None,
                                         **kwargs
                                         ) -> object:
        """For a given list of SHA256's, retrieve the metadata for each installer.

        (Examples: release_date, version).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersEntitiesV2

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of SHA256s for installers to retrieve details for.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersEntitiesV2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def get_sensor_installer_ccid(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve the CID for the current oauth environment.

        This method does not accept arguments.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersCCIDByQuery

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersCCIDByQuery"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sensor_installers_by_query(self: object,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a list of SHA256 for installers based on the filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersByQuery

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        limit : int (1-500)
            The maximum number of records to return.
        offset : int
            The first item to return, where 0 is the latest item. (Integer)
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. version|ASC, release_date|DESC).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersByQuery",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sensor_installers_by_query_v2(self: object,
                                          parameters: dict = None,
                                          **kwargs
                                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a list of SHA256 for installers based on the filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersByQueryV2

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        limit : int (1-500)
            The maximum number of records to return.
        offset : int
            The first item to return, where 0 is the latest item. (Integer)
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. version|ASC, release_date|DESC).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersByQueryV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_combined_sensor_installers_by_query_v3(self: object,
                                                   parameters: dict = None,
                                                   **kwargs
                                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get sensor installer details by provided query.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetCombinedSensorInstallersByQueryV3

        Keyword arguments
        -----------------
        offset : int
            The first item to return, where 0 is the latest item.
        limit : int
            The number of items to return in this response (default: 100, max: 500)
        sort : str
            Sort items using their properties.
        filter : str
            Filter items using a query in Falcon Query Language (FQL)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCombinedSensorInstallersByQueryV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def download_sensor_installer_v3(self: object,
                                     *args,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download sensor installer by SHA256 ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/DownloadSensorInstallerByIdV3

        Keyword arguments
        -----------------
        id : str
            SHA256 of the installer to download.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DownloadSensorInstallerByIdV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sensor_installer_entities_v3(self: object,
                                         *args,
                                         parameters: dict = None,
                                         **kwargs
                                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get sensor installer details by provided SHA256 IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersEntitiesV3

        Keyword arguments
        -----------------
        ids : str or list[str]
            The IDs of the installers.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersEntitiesV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sensor_installers_by_query_v3(self: object,
                                          *args,
                                          parameters: dict = None,
                                          **kwargs
                                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get sensor installer IDs by provided query.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download/GetSensorInstallersByQueryV3

        Keyword arguments
        -----------------
        offset : int
            The first item to return, where 0 is the latest item.
        limit : int
            The number of items to return in this response (default: 100, max: 500)
        sort : str
            Sort items using their properties.
        filter : str
            Filter items using a query in Falcon Query Language (FQL)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSensorInstallersByQueryV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetCombinedSensorInstallersByQuery = get_combined_sensor_installers_by_query
    GetCombinedSensorInstallersByQueryV2 = get_combined_sensor_installers_by_query_v2
    DownloadSensorInstallerById = download_sensor_installer
    DownloadSensorInstallerByIdV2 = download_sensor_installer_v2
    GetSensorInstallersEntities = get_sensor_installer_entities
    GetSensorInstallersEntitiesV2 = get_sensor_installer_entities_v2
    GetSensorInstallersCCIDByQuery = get_sensor_installer_ccid
    GetSensorInstallersByQuery = get_sensor_installers_by_query
    GetSensorInstallersByQueryV2 = get_sensor_installers_by_query_v2
    GetCombinedSensorInstallersByQueryV3 = get_combined_sensor_installers_by_query_v3
    DownloadSensorInstallerByIdV3 = download_sensor_installer_v3
    GetSensorInstallersEntitiesV3 = get_sensor_installer_entities_v3
    GetSensorInstallersByQueryV3 = get_sensor_installers_by_query_v3


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Sensor_Download = SensorDownload  # pylint: disable=C0103
