# test_scanning_orchestrator.py
# This class tests the scanning_orchestrator service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import ScanningOrchestrator

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ScanningOrchestrator(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestScanningOrchestrator:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "get_combined_schedules": falcon.get_combined_schedules(limit=1, offset=1, sort="string", filter="string"),
            "trigger_scan_by_schedule": falcon.trigger_scan_by_schedule(ids="string"),
            "get_schedules": falcon.get_schedules(ids="12345678"),
            "create_schedules": falcon.create_schedules(resources="string"),
            "delete_schedules": falcon.delete_schedules(ids="12345678"),
            "update_schedules": falcon.update_schedules(resources="string"),
            "get_service_types": falcon.get_service_types(scan_product="string"),
            "search_schedules": falcon.search_schedules(limit=1, offset=1, sort="string", filter="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
