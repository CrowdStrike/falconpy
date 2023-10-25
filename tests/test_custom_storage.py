"""
test_custom_storage.py - This class tests the Custom Storage service class
"""
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CustomStorage, APIHarnessV2

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
uber = APIHarnessV2(creds=config.creds)
falcon = CustomStorage(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]  # Temp allow 403


class TestCustomStorage:
    def run_all_tests(self):
        error_checks = True
        tests = {
            "ListObjects" : falcon.list(collection_name="Whatever"),
            "SearchObjects" : falcon.search(collection_name="whatever"),
            "GetObject" : falcon.get(collection_name="whatever", object_key="whatever_else"),
            "PutObject" : falcon.upload(collection_name="whatever", object_key="whatever_else"),
            "DeleteObject" : falcon.delete(collection_name="whatever", object_key="whatever_else"),
            "FailBecauseMissingCollectionNameListObjects" : falcon.list(),
            "FailBecauseMissingCollectionNameSearchObjects" : falcon.search(),
            "GetObjectMetadata" : falcon.metadata(collection_name="whatever", object_key="whatever_else"),
            "UberStyleGetObjectMetadata" : uber.command("GetObjectMetadata", collection_name="whatever", object_key="whatever_else"),
            "FailBecauseMissingObjectKeyMetadata" : falcon.metadata(collection_name="no_object_key"),
            "FailBecauseMissingObjectKeyDeleteObject" : falcon.delete(collection_name="no_object_key"),
            "FailBecauseMissingObjectKeyPutObject" : falcon.upload(collection_name="no_object_key"),
            "FailBecauseMissingObjectKeyGetObject" : falcon.get(collection_name="no_object_key")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                if "FailBecauseMissing" in key and tests[key]["status_code"] == 500:
                    error_checks = True
                # if not error_checks:
                #     print(tests[key])

        return error_checks

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_functionality(self):
        assert self.run_all_tests() is True
