# test_deployments.py
# This class tests the deployments service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Deployments

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Deployments(auth_object=config)
AllowedResponses = [200, 201, 207, 403, 404, 429]


class TestDeployments:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetDeploymentsExternalV1": falcon.get_deployments(ids="12345678"),
            "CombinedReleasesV1Mixin0": falcon.query_releases(limit=1),
            "CombinedReleaseNotesV1": falcon.query_release_notes(limit=1),
            "GetEntityIDsByQueryPOST": falcon.get_release_notes_v1(ids="12345678"),
            "GetEntityIDsByQueryPOSTV2": falcon.get_release_notes(ids="12345678"),
            "QueryReleaseNotesV1": falcon.query_release_note_ids(limit=1),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
