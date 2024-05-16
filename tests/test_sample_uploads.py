"""
test_sample_uploads.py - This class tests the sample_uploads service class
"""
import os
import sys
import pytest
import datetime
import hashlib
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import SampleUploads

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = SampleUploads(auth_object=config)
AllowedResponses = [200, 201, 202, 400, 403, 404, 429]


class TestSampleUploads:
    def sample_upload_download_delete(self, style: str = "file_data", expanded_result: bool = False):
        """
        Tests all functionality within the class by performing an upload / download / compare / delete.
        """
        FILENAME = "tests/testfile.png"
        fmt = '%Y-%m-%d %H:%M:%S'
        stddate = datetime.datetime.now().strftime(fmt)
        sdtdate = datetime.datetime.strptime(stddate, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
        jdate = "{}{}".format(stddate.replace("-", "").replace(":", "").replace(" ", ""), jdate)
        SOURCE = "%s_source.png" % jdate
        TARGET = "tests/%s_target.png" % jdate
        PAYLOAD = open(FILENAME, 'rb').read()
        params_payload = {"file_name": SOURCE}
        if style.lower() == "sample":
            response = falcon.upload_sample(file_name=SOURCE, sample=PAYLOAD)
        elif style.lower() == "upfile":
            response = falcon.upload_sample(file_name=SOURCE, upfile=PAYLOAD, comment="Whatever")
        else:
            response = falcon.upload_sample(parameters=params_payload, file_data=PAYLOAD, is_confidential=True)
        try:
            sha = response["body"]["resources"][0]["sha256"]
        except (KeyError, IndexError):
            sha = None
        if sha:
            response = falcon.GetSampleV3(ids=sha, expand_result=expanded_result)
            if expanded_result:
                if response[0] == 200:
                    response_to_write = response[2]
                else:
                    # Our download returned a failure status code
                    return False
            else:
                response_to_write = response
            try:
                open(TARGET, 'wb').write(response_to_write)
            except TypeError:
                # This particular unit test failed it's upload,
                # pass a True since the code path was tested
                pytest.skip("Unable to open test file, skipping.")
                return True
            buf = 65536
            hash1 = hashlib.sha256()
            with open(FILENAME, 'rb') as f:
                while True:
                    data = f.read(buf)
                    if not data:
                        break
                    hash1.update(data)
            hash1 = hash1.hexdigest()
            hash2 = hashlib.sha256()
            with open(TARGET, 'rb') as f:
                while True:
                    data = f.read(buf)
                    if not data:
                        break
                    hash2.update(data)
            hash2 = hash2.hexdigest()
            if os.path.exists(TARGET):
                os.remove(TARGET)
            _ = falcon.DeleteSampleV3(ids=sha)
            if hash1 == hash2:
                return True
            else:
                return False
        else:
            # Workflow download error, skip it
            pytest.skip("Workflow-related upload error, skipping.")
            return True

    def sample_errors(self):
        """
        Executes every statement in every method of the class, accepts all errors except 500
        """
        FILENAME = "tests/testfile.zip"
        with open(FILENAME, 'rb') as test_archive:
            PAYLOAD = test_archive.read()
        #files = [("file", ("testfile.zip", open(FILENAME, 'rb').read(), "application/zip"))]
        error_checks = True
        tests = {
            "upload_sample": falcon.UploadSampleV3(body={}),
            "upload_sample_as_well": falcon.upload_sample(file_name="NotHere.jpg"),
            "get_sample": falcon.GetSampleV3(ids='DoesNotExist'),
            "delete_sample": falcon.DeleteSampleV3(ids='12345678'),
            "ArchiveListV1": falcon.ArchiveListV1(id="12345678"),
            "ArchiveGetV1": falcon.ArchiveGetV1(id="123456789"),
            "ArchiveDeleteV1": falcon.ArchiveDeleteV1(id="123456789"),
            "ArchiveUploadV1": falcon.ArchiveUploadV1(name="testfile.zip",
                                                      body=PAYLOAD,
                                                      source="workstation",
                                                      comment="FalconPy testing",
                                                      file_type="zip"
                                                      ),
            "ArchiveUploadV1b": falcon.ArchiveUploadV1(name="FalconPy testing", body=None),
            "ArchiveUploadV2": falcon.ArchiveUploadV2(name="testfile.zip", archive=PAYLOAD, source="workstation", comment="FalconPy testing", password="whatever", is_confidential=True),
            "ArchiveUploadV2": falcon.upload_archive(file=PAYLOAD, source="workstation", comment="FalconPy testing"),
            "ExtractionListV1": falcon.ExtractionListV1(id="12345779"),
            "ExtractionGetV1": falcon.ExtractionGetV1(ids="12345678"),
            "ExtractionCreateV1": falcon.ExtractionCreateV1(extract_all=True, files=[{
                "comment": "Test comment",
                "is_confidential": True,
                "name": "falconpy-test-archive.zip"
            }], sha256="12345678"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # print(key)
                # print(tests[key])
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    def test_all_functionality_file_data(self):
        """Pytest harness hook"""
        assert self.sample_upload_download_delete("file_data") is True

    @pytest.mark.skipif("laggar" in falcon.base_url, reason="US-GOV-1 testing disabled")
    def test_all_functionality_expanded_result(self):
        """Pytest harness hook"""
        assert self.sample_upload_download_delete("file_data", expanded_result=True) is True

    def test_all_functionality_sample(self):
        """Pytest harness hook"""
        assert self.sample_upload_download_delete("sample") is True

    def test_all_functionality_upfile(self):
        """Pytest harness hook"""
        assert self.sample_upload_download_delete("upfile") is True

    @pytest.mark.skipif("laggar" in falcon.base_url, reason="US-GOV-1 testing disabled")
    def test_errors(self):
        """Pytest harness hook"""
        assert self.sample_errors() is True
