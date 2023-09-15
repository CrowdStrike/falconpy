"""
test_falcon_container.py - This class tests the falcon_container service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FalconContainer, APIHarness, APIHarnessV2

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FalconContainer(auth_object=config)
uber = APIHarness(client_id=falcon.auth_object.creds["client_id"],
                  client_secret=falcon.auth_object.creds["client_secret"],
                  base_url=falcon.auth_object.base_url
                  )
uber2 = APIHarnessV2(client_id=falcon.auth_object.creds["client_id"],
                     client_secret=falcon.auth_object.creds["client_secret"],
                     base_url=falcon.auth_object.base_url
                     )
AllowedResponses = [200, 201, 204, 400, 403, 404, 429, 500, 502]  # Allowing no content returned as code paths are confirmed


class TestFalconContainer:
    def run_tests(self):
        error_checks = True

        tests = {
            "GetAssessment": falcon.get_assessment(repository="misp", tag="latest"),
            "GetCombinedImages": falcon.get_combined_images(),
            "DeleteImageDetails": falcon.delete_image_details("whatever"),
            "ImageMatchesPolicy": falcon.image_matches_policy(repository="whatever", tag="whatever", body={}),
            "GetAssessmentUber": uber.command("GetImageAssessmentReport", repository="misp", tag="latest"),
            "DeleteImageDetailsUber": uber.command("DeleteImageDetails", image_id="12345678"),
            "ImageMatchesPolicyUber": uber.command("ImageMatchesPolicy", repository="whatever", tag="whatever"),
            "GetAssessmentUber2": uber2.command("GetImageAssessmentReport", repository="misp", tag="latest"),
            "DeleteImageDetailsUber2": uber2.command("DeleteImageDetails", image_id="12345678"),
            "ImageMatchesPolicyUber2": uber2.command("ImageMatchesPolicy", repository="whatever", tag="whatever"),
            "read_image_vulnerabilities": falcon.read_image_vulnerabilities(osversion="Windows", packages={"LayerIndex": 1}),
            "ReadRegistryEntities": falcon.read_registry_entities(),
            "ReadRegistryEntitiesByUUID": falcon.read_registry_entities_by_uuid(ids="12345678"),
            "DeleteRegistryEntities": falcon.delete_registry_entities(ids="12345678"),
            "UpdateRegistryEntities": falcon.update_registry_entities(credential={}, type="gcr", url="https://whatevs",
                                                                      url_uniqueness_key="banana", user_defined_alias="BoB",
                                                                      details={"aws_iam_role":"aws:arn::whatevs", "aws_external_id": "yellow"}
                                                                      ),
            "CreateRegistryEntities": falcon.create_registry_entities(type="github", url="https://somewheres", username="larry",
                                                                      password="top_secret"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(tests[key])
                # print(f"{key} operation returned a {tests[key]['status_code']} status code")

        return error_checks

    def test_get_credentials(self):
        """Pytest harness hook"""
        assert bool(falcon.get_credentials()["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(os.getenv("DEBUG_API_BASE_URL", "us1").lower() in ["https://api.eu-1.crowdstrike.com", "eu1", "https://api.laggar.gcw.crowdstrike.com", "usgov1"],
                        reason="Unit testing unavailable on US-GOV-1 / EU-1"
                        )
    def test_remaining_code_paths(self):
        """Pytest harness hook"""
        assert self.run_tests() is True
