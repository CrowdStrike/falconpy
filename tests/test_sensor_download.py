import os
import shutil
import sys

from tests import test_authorization as Authorization
from falconpy import sensor_download as FalconSensorDownload

sys.path.append(os.path.abspath('src'))
AllowedResponses = [200, 429] # Adding rate-limiting as an allowed response for now
appId = "pytest-sensor_download-unit-test"
auth = Authorization.TestAuthorization()
auth.serviceAuth()

sensor_download_client = FalconSensorDownload.Sensor_Download(access_token=auth.token)

class TestSensorDownload():
    
    @staticmethod
    def _get_cid():
        cid = sensor_download_client.GetSensorInstallersCCIDByQuery()["resources"][0]
        return True if cid else False

    @staticmethod
    def _get_multiple_shas():
        params = {"filter": 'platform:"windows"', "sort": "release_date|desc"}
        shas = sensor_download_client.GetSensorInstallersByQuery(params)["resources"]
        return shas

    def _download_sensor(self):
        file_name = "falconwinddows.exe"
        directory_path = "sensor_downloads"
        sha_id = self._get_multiple_shas()[0]
        sensor_download_client.DownloadSensorInstallerById(_id=sha_id, file_name=file_name, directory_path=directory_path)
        path = os.path.join(directory_path)
        if os.path.exists(path):
            # cleaning up dir
            shutil.rmtree(directory_path)
            return True
        return False

    @staticmethod
    def _get_metadata_for_filter():
        params = {"filter": 'platform:"windows"', "sort": "release_date|desc"}
        resources = sensor_download_client.GetCombinedSensorInstallersByQuery(params)["resources"]
        return True if len(resources) > 0 else False

    def _get_metadata_for_ids(self):
        sha_ids = self._get_multiple_shas()
        resources = sensor_download_client.GetSensorInstallersEntities(ids=sha_ids)["resources"]
        return True if len(resources) > 0 else False

    def test_download_windows_sensor(self):
        assert self._download_sensor == True

    def test_get_sha_window_sensor(self):
        assert self._get_metadata_for_filter == True

    def test_get_ccid(self):
        assert self._get_cid() == True

    def test_get_shas(self):
        assert len(self._get_multiple_shas()) > 0

    def test_get_mutliple_shas(self):
        assert self._get_metadata_for_ids() == True