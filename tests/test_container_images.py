# test_container_images.py
# This class tests the container images service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ContainerImages

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ContainerImages(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestContainerImages:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "AggregateImageAssessmentHistory": falcon.aggregate_assessment_history(filter="repository:'larry'"),
            "AggregateImageCountByBaseOS": falcon.aggregate_count_by_base_os(filter="repository:'testing'"),
            "AggregateImageCountByState": falcon.aggregate_count_by_state(filter="repository:'testing'"),
            "AggregateImageCount": falcon.aggregate_count(filter="repository:'testing'"),
            "GetCombinedImages": falcon.get_combined_images(filter="repository:'testing'"),
            "CombinedImageByVulnerabilityCount": falcon.get_combined_images_by_vulnerability_count(filter="repository:'testing'"),
            "CombinedImageDetail": falcon.get_combined_detail(filter="repository:'testing'"),
            "ReadCombinedImagesExport": falcon.read_combined_export(filter="repository:'testing'"),
            "CombinedImageIssuesSummary": falcon.get_combined_issues_summary(filter="repository:'testing'"),
            "CombinedImageVulnerabilitySummary": falcon.get_combined_vulnerabilities_summary(filter="repository:'testing'"),
            "CombinedBaseImages": falcon.get_combined_base_images(),
            "CreateBaseImageEntities": falcon.create_base_images(image_id="12345678", image_digest="1234", repository="bob", registry="aws", tag="bob"),
            "DeleteBaseImages": falcon.delete_base_images("12345678")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                if key != "DeleteBaseImages":
                    error_checks = False
                    # print(key)
                    # print(tests[key])
        assert error_checks
