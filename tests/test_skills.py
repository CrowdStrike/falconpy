# test_skills.py
# This class tests the skills service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import Skills

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Skills(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429, 415, 500]

with open("tests/test.yml", "rb") as _fh:
    BINARY_FILE = _fh.read()


class TestSkills:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesSkillsDownloadV2": falcon.download_studio_skill(id="string", include_deleted=True),
            "EntitiesSkillsV1": falcon.get_studio_skills(ids=["string"], include_deleted=True),
            "EntitiesSkillsUpdateV1": falcon.update_studio_skill(),
            "EntitiesSkillsUpdateV1WithFile": falcon.update_studio_skill(skill_blob=BINARY_FILE, file_name="test.yml", id="12345678"),
            "EntitiesSkillsCreateV1": falcon.create_studio_skill(),
            "EntitiesSkillsCreateV1WithFile": falcon.create_studio_skill(skill_blob=BINARY_FILE, file_name="test.yml"),
            "EntitiesSkillsDeleteV1": falcon.delete_studio_skill(id="12345678"),
            "QueriesSkillsV1": falcon.query_studio_skills(offset=1, limit=1, sort="string", filter="string",
                                                          include_deleted=True),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
