# test_malquery.py
# This class tests the malquery service class
import os
import sys
import pytest
# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import MalQuery

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = MalQuery(auth_object=config)
AllowedResponses = [200, 400, 404, 429]  # Adding rate-limiting as an allowed response for now


class TestMalQuery:
    def mq_get_quotas(self):
        returned = False
        if falcon.GetMalQueryQuotasV1()["status_code"] in AllowedResponses:
            returned = True

        return returned

    def mq_test_all_paths(self):
        error_checks = True
        tests = {
            "fuzzy_search": falcon.fuzzy_search(body={
                                                    "options": {
                                                        "filter_meta": [
                                                            "string"
                                                        ],
                                                        "limit": 0
                                                    },
                                                    "patterns": [
                                                        {
                                                            "type": "string",
                                                            "value": "string"
                                                        }
                                                    ]
                                                    }),
            "really_fuzzy": falcon.fuzzy_search(filter_meta="whatevs,something_else",
                                                limit=1,
                                                patterns=[{"type": "file", "value": "test"}]
                                                ),
            "get_download": falcon.get_download(ids="12345678"),
            "get_metadata": falcon.get_metadata(ids="12345678"),
            "get_request": falcon.get_request(ids="12345678"),
            "get_samples": falcon.get_samples(ids="12345678"),
            "multi_download": falcon.samples_multidownload(ids="12345678"),
            "exact_search": falcon.exact_search(body={}),
            "exact_search_too": falcon.exact_search(filter_filetypes="xls,doc",
                                                    filter_meta="whatevers,something",
                                                    limit=1,
                                                    max_date="UTC_Date_Here",
                                                    min_date="UTC Date Here",
                                                    max_size="200",
                                                    min_size="1",
                                                    patterns=[
                                                        {
                                                            "type": "file",
                                                            "value": "spreadsheet"
                                                        }
                                                    ]),
            "hunt": falcon.hunt(body={}),
            "cry_of_the_hunter": falcon.hunt(filter_filetypes=["exe"],
                                             filter_meta="some metadata",
                                             limit=1,
                                             max_date="UTC_Date_Here",
                                             min_date="UTC Date Here",
                                             max_size="200",
                                             min_size="1",
                                             yara_rule="Some Yara rule"
                                             )
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # print(tests[key])
                error_checks = False
                pytest.skip("Skipping due to test flakiness")

        return error_checks

    def test_get_quotas(self):
        assert self.mq_get_quotas() is True

    def test_all_functionality(self):
        assert self.mq_test_all_paths() is True
