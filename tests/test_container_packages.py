# test_container_packages.py
# This class tests the container packages service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ContainerPackages

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ContainerPackages(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestContainerPackages:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "ReadPackagesCountByZeroDay": falcon.read_zero_day_counts(filter="cid:'12345678901234567890123456789012'"),
            "ReadPackagesByFixableVulnCount": falcon.read_fixable_vuln_count(filter="cid:'12345678901234567890123456789012'"),
            "ReadPackagesByVulnCount": falcon.read_vuln_count(filter="cid:'12345678901234567890123456789012'"),
            "ReadPackagesCombinedExport": falcon.read_combined_export(filter="cid:'12345678901234567890123456789012'"),
            "ReadPackagesCombined": falcon.read_combined(filter="cid:'12345678901234567890123456789012'"),
            "ReadPackagesCombinedV2": falcon.read_packages(limit=1),
            "ReadPackagesByImageCount": falcon.read_packages_by_image_count(limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
