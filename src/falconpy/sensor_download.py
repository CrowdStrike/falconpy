from ._util import service_request, generate_error_result, parse_id_list
from ._service_class import ServiceClass

import os

class Sensor_Download(ServiceClass):

    def GetCombinedSensorInstallersByQuery(self: object, params: dict) -> dict:
        """
        retrieve all metadata for installers from provided query
        """
        FULL_URL = self.base_url+'/sensors/combined/installers/v1'
        HEADERS = self.headers
        PARAMS = params
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def DownloadSensorInstallerById(self: object, _id: str, download_path: str="sensor_downloads"):
        """
        download the sensor by the sha256 into the specified directory.
        the path will be created for the user if it does not already exist
        """
        # create the directory if doesn't exist
        os.makedirs(download_path, exist_ok=True)
        # _id is the sha256 of the sensor
        FULL_URL = self.base_url+"/sensors/entities/download-installer/v1?id={}".format(_id)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        # probably can't just return a response but need to chunk out the file writes
        return returned

    def GetSensorInstallersEntities(self: object, ids: list):
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

    def GetSensorInstallersCCIDByQuery(self: object):
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

    def GetSensorInstallersByQuery(self: object, params: dict) -> dict:
        """
        retrieve a list of SHA256 for installers based on the filter
        """
        FULL_URL = self.base_url+'/sensors/queries/installers/v1'
        HEADERS = self.headers
        PARAMS = params
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   param=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned