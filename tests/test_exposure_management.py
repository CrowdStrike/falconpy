# test_exposure_management.py
# This class tests the exposure management service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ExposureManagement

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ExposureManagement(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestExposureManagement:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "aggregate_assets": falcon.aggregate_assets(
                        date_ranges=[
                            {
                                "from": "string",
                                "to": "string"
                            }
                        ],
                        field="string",
                        filter="string",
                        interval="string",
                        min_doc_count=0,
                        missing="string",
                        name="string",
                        q="string",
                        ranges=[
                            {
                                "From": 0,
                                "To": 0
                            }
                        ],
                        size=0,
                        sort="string",
                        sub_aggregates=[
                            "string"
                        ],
                        time_zone="string",
                        type="string"
            ),
            "blob_download_external_assets": falcon.download_assets(assetId="whatever", hash="whatever"),
            "blob_preview_external_assets": falcon.preview_assets(assetId="whatever", hash="whatever"),
            "get_external_assets": falcon.get_assets("123456"),
            "patch_external_assets": falcon.update_assets(cid="whatever", action="whatever"),
            "query_external_assets_v1": falcon.query_assets_v1(),
            "query_external_assets": falcon.query_assets(),
            "delete_assets": falcon.delete_assets(ids="12345678", description="unit_testing"),
            "combined_ecosystem_subsidiaries": falcon.query_combined_ecosystem_subsidiaries(limit=1, version_id="1"),
            "get_ecosystem_subsidiaries": falcon.get_ecosystem_subsidiaries(id="12345678"),
            "post_external_assets_inventory_v1": falcon.add_assets(id="12345678", value="bob", subsidiary_id="12345678"),
            "query_ecosystem_subsidiaries": falcon.query_ecosystem_subsidiaries(limit=1, version_id="1")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
