# test_container_vulnerabilities.py
# This class tests the container vulnerabilities service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ContainerVulnerabilities

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ContainerVulnerabilities(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestContainerVulnerabilities:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "ReadCombinedVulnerabilities": falcon.read_combined_vulnerabilities(filter="cid:'12345678901234567890123456789012'"),
            "ReadCombinedVulnerabilitiesInfo": falcon.read_combined_vulnerabilities_info(cve_id="1234567890"),
            "ReadCombinedVulnerabilitiesDetails": falcon.read_combined_vulnerability_detail(filter="cid:'12345678901234567890123456789012'"),
            "ReadVulnerabilitiesPublicationDate": falcon.read_vulnerabilities_by_pub_date(filter="cid:'12345678901234567890123456789012'"),
            "ReadVulnerabilitiesByImageCount": falcon.read_vulnerabilities_by_count(filter="cid:'12345678901234567890123456789012'"),
            "ReadVulnerabilityCount": falcon.read_vulnerability_count(filter="cid:'12345678901234567890123456789012'"),
            "ReadVulnerabilityCountBySeverity": falcon.read_vulnerability_counts_by_severity(filter="cid:'12345678901234567890123456789012'"),
            "ReadVulnerabilityCountByCPSRating": falcon.read_vulnerability_counts_by_cps_rating(filter="cid:'12345678901234567890123456789012'"),
            "ReadVulnerabilityCountByCVSSScore": falcon.read_vulnerability_counts_by_cvss_score(filter="cid:'12345678901234567890123456789012'"),
            "ReadVulnerabilityCountByActivelyExploited": falcon.read_vulnerability_counts_by_active_exploited(filter="cid:'12345678901234567890123456789012'")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
