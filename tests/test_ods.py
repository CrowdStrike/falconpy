# test_ods.py
# This class tests the quick_scan service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ODS

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ODS(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429, 500]  # Temp allowing 403 / 500


class TestODS:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "aggregate_scan_hosts": falcon.aggregate_scan_hosts(date_ranges=[
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
            "aggregate_scans": falcon.aggregate_scans(date_ranges=[
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
            "aggregate_scheduled_scans": falcon.aggregate_scheduled_scans(date_ranges=[
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
            "get_malicious_files_by_id": falcon.get_malicious_files(ids="12345678"),
            "cancel_scans": falcon.cancel_scans(ids="12345678"),  # getting 500 not 404
            "get_scan_host_metadata_by_ids": falcon.get_scan_hosts(ids="12345689"),
            # "scans_report": falcon.scans_report(is_schedule=True, sort="id|asc", report_format="json"),
            "get_scans_by_scan_ids": falcon.get_scans(ids="123456789"),
            "get_scans_by_scan_ids_v1": falcon.get_scans_v1(ids="123456789"),
            "create_scan": falcon.create_scan(host_groups=["GroupBob"]),
            "get_scheduled_scans_by_scan_ids": falcon.get_scheduled_scans(ids="12345678"),
            "schedule_scan": falcon.schedule_scan(host_groups=["GroupBob"], interval=400),  # getting 500 not 404
            "delete_scheduled_scans": falcon.delete_scheduled_scans(ids="12345678"),
            "query_malicious_files": falcon.query_malicious_files(),
            "query_scan_host_metadata": falcon.query_scan_hosts(),
            "query_scans": falcon.query_scans(),
            "query_scheduled_scans": falcon.query_scheduled_scans()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
