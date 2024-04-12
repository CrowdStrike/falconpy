# test_unidentified_containers.py
# This class tests the unidentified containers service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import UnidentifiedContainers

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = UnidentifiedContainers(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestUnidentifiedContainers:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "ReadUnidentifiedContainersByDateRangeCount": falcon.read_count_by_date_range("cluster_name:'bob'"),
            "ReadUnidentifiedContainersCount": falcon.read_count(filter="cluster_name:'charlie'"),
            "SearchAndReadUnidentifiedContainers": falcon.search_and_read(filter="cid:'1234567890'", limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
