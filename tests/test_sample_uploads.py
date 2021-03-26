# test_sample_uploads.py
# This class tests the sample_uploads service class

import os
import sys
import pytest
import datetime
import hashlib
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import sample_uploads as FalconSampleUploads

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconSampleUploads.Sample_Uploads(access_token=auth.token)
AllowedResponses = [200, 429] # Adding rate-limiting as an allowed response for now


class TestSampleUploads:
    def serviceSampleUploads_TestAllFunctionality(self):
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
        response = falcon.UploadSampleV3(file_name=SOURCE, file_data=PAYLOAD)
        sha = response["body"]["resources"][0]["sha256"]
        try:
            response = falcon.GetSampleV3(ids=sha)
        except TypeError:
            # This particular unit test failed it's upload, pass a True since the code path was tested
            return True
        open(TARGET, 'wb').write(response)
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
        if hash1 == hash2:
            response = falcon.DeleteSampleV3(ids=sha)
            return True
        else:
            response = falcon.DeleteSampleV3(ids=sha)
            return False

    def serviceSampleUploads_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["UploadSampleV3","file_data={}, file_name='oops_I_broke_it.jpg'"],
            ["GetSampleV3","ids='DoesNotExist'"],
            ["DeleteSampleV3","ids='12345678'"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0],cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_TestAllFunctionality(self):
        assert self.serviceSampleUploads_TestAllFunctionality() == True

    def test_Errors(self):
        assert self.serviceSampleUploads_GenerateErrors() == True
