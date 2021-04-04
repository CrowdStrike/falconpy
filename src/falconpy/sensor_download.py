from ._util import service_request, parse_id_list, generate_ok_result
from ._service_class import ServiceClass

import os


class Sensor_Download(ServiceClass):

    def GetCombinedSensorInstallersByQuery(self: object, parameters: dict = {}) -> dict:
        """
        retrieve all metadata for installers from provided query
        """
        FULL_URL = self.base_url+'/sensors/combined/installers/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def DownloadSensorInstallerById(self: object,
                                    parameters: dict,
                                    file_name: str = None,
                                    download_path: str = None
                                    ) -> object:
        """
        download the sensor by the sha256 into the specified directory.
        the path will be created for the user if it does not already exist
        """
        FULL_URL = self.base_url+"/sensors/entities/download-installer/v1"
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   verify=self.ssl_verify
                                   )
        if file_name and download_path and isinstance(returned, bytes):
            os.makedirs(download_path, exist_ok=True)
            # write the newly downloaded sensor into the aforementioned directory with provided file name
            with open(os.path.join(download_path, file_name), "wb") as sensor:
                sensor.write(returned)
            returned = generate_ok_result(message="Download successful")
        return returned

    def GetSensorInstallersEntities(self: object, ids: list or str) -> object:
        """
        For a given list of SHA256's, retrieve the metadata for each installer
        such as the release_date and version among other fields
        """
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/sensors/entities/installers/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetSensorInstallersCCIDByQuery(self: object) -> dict:
        """
        retrieve the CID for the current oauth environment
        """
        FULL_URL = self.base_url+'/sensors/queries/installers/ccid/v1'
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetSensorInstallersByQuery(self: object, parameters: dict = {}) -> dict:
        """
        retrieve a list of SHA256 for installers based on the filter
        """
        FULL_URL = self.base_url+'/sensors/queries/installers/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned
