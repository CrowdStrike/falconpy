import os
import sys
import pytest
from tests import test_authorization as Authorization
from falconpy import SensorDownload

sys.path.append(os.path.abspath('src'))
AllowedResponses = [200, 401, 429]  # Adding rate-limiting as an allowed response for now
appId = "pytest-sensor_download-unit-test"
auth = Authorization.TestAuthorization()
config = auth.getConfigObject()

# Temp workaround due to 500s outta GovCloud
# if config.base_url == "https://api.laggar.gcw.crowdstrike.com":
#     AllowedResponses.append(500)

sensor_download_client = SensorDownload(auth_object=config)


class TestSensorDownload():
    """Sensor Download unit test series"""
    @staticmethod
    def _get_cid():
        resp = sensor_download_client.GetSensorInstallersCCIDByQuery()
        return True if resp["status_code"] in AllowedResponses else False

    @staticmethod
    def _get_multiple_shas():
        params = {"filter": 'platform:"linux"', "sort": "release_date|desc"}
        try:
            shas = sensor_download_client.GetSensorInstallersByQueryV2(parameters=params)["body"]["resources"]
        except KeyError:
            # Workflow download error, skip it
            shas = True
            pytest.skip("Workflow-related upload error, skipping.")

        return shas

    def _download_sensor(self, style = "v2"):
        sha_id = self._get_multiple_shas()[0]
        if style == "v1":
            resp = sensor_download_client.DownloadSensorInstallerById(parameters={"id": sha_id})
        else:
            resp = sensor_download_client.DownloadSensorInstallerByIdV2(parameters={"id": sha_id})
        if isinstance(resp, bytes):
            return True
        else:
            return False

    def _download_sensor_file(self, style = "v2"):
        file_name = "sensor.rpm"
        directory_path = "."
        sha_id = self._get_multiple_shas()[0]
        if style == "v1":
            _ = sensor_download_client.DownloadSensorInstallerById(parameters={"id": sha_id},
                                                                   file_name=file_name,
                                                                   download_path=directory_path
                                                                   )
        else:
            _ = sensor_download_client.DownloadSensorInstallerByIdV2(parameters={"id": sha_id},
                                                                     file_name=file_name,
                                                                     download_path=directory_path
                                                                     )
        if os.path.exists("sensor.rpm"):
            os.remove("sensor.rpm")
            return True
        else:
            return False

    @staticmethod
    def _get_metadata_for_filter():
        # Testing new parameter functionality
        # params = {"filter": 'platform:"windows"', "sort": "release_date|desc"}
        # resp = sensor_download_client.GetCombinedSensorInstallersByQuery(parameters=params)
        resp = sensor_download_client.GetCombinedSensorInstallersByQuery(filter='platform:"windows"', sort="release_date|desc")
        return True if resp["status_code"] in AllowedResponses else False

    @staticmethod
    def _get_metadata_for_filter_v2():
        # Testing new parameter functionality
        # params = {"filter": 'platform:"windows"', "sort": "release_date|desc"}
        # resp = sensor_download_client.GetCombinedSensorInstallersByQuery(parameters=params)
        resp = sensor_download_client.GetCombinedSensorInstallersByQueryV2(filter='platform:"windows"', sort="release_date|desc")
        return True if resp["status_code"] in AllowedResponses else False

    def _get_metadata_for_ids(self):
        sha_ids = self._get_multiple_shas()
        resp = sensor_download_client.GetSensorInstallersEntities(ids=sha_ids)
        return True if resp["status_code"] in AllowedResponses else False

    def _get_metadata_for_ids_v2(self):
        sha_ids = self._get_multiple_shas()
        resp = sensor_download_client.GetSensorInstallersEntitiesV2(ids=sha_ids)
        return True if resp["status_code"] in AllowedResponses else False

    @staticmethod
    def _get_all_metadata():
        resp = sensor_download_client.GetCombinedSensorInstallersByQuery()
        return True if resp["status_code"] in AllowedResponses else False

    @staticmethod
    def _get_all_metadata2():
        resp = sensor_download_client.GetSensorInstallersByQuery()
        return True if resp["status_code"] in AllowedResponses else False

    def test_download_windows_sensor(self):
        assert self._download_sensor(style="v1") is True

    def test_download_windows_sensor_file(self):
        assert self._download_sensor_file(style="v1") is True

    def test_download_windows_sensor_v2(self):
        assert self._download_sensor() is True

    def test_download_windows_sensor_file_v2(self):
        assert self._download_sensor_file() is True

    def test_get_sha_window_sensor(self):
        assert self._get_metadata_for_filter() is True

    def test_get_sha_window_sensor_v2(self):
        assert self._get_metadata_for_filter_v2() is True

    def test_get_ccid(self):
        assert self._get_cid() is True

    def test_get_shas(self):
        assert len(self._get_multiple_shas()) > 0

    def test_get_multiple_shas(self):
        assert self._get_metadata_for_ids() is True

    def test_get_multiple_shas_v2(self):
        assert self._get_metadata_for_ids_v2() is True

    def test_get_all_metadata(self):
        assert self._get_all_metadata() is True

    def test_get_all_metadata2(self):
        assert self._get_all_metadata2() is True
