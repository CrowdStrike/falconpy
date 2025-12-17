# test_saas_security.py
# This class tests the SaasSecurity service class

# import json
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Classes to test - manually imported from sibling folder
from falconpy import SaasSecurity
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = SaasSecurity(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429, 500]


class TestSaasSecurity:
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetMetricsV3": falcon.GetMetricsV3(),
            "GetAlertsV3": falcon.GetAlertsV3(),
            "GetAppInventoryUsers": falcon.GetAppInventoryUsers(item_id="1234567|||app123"),
            "GetAppInventory": falcon.GetAppInventory(),
            "GetSecurityCheckAffectedV3": falcon.GetSecurityCheckAffectedV3(id="1234567"),
            "DismissAffectedEntityV3": falcon.DismissAffectedEntityV3(id="1234567", body={}),
            "DismissSecurityCheckV3": falcon.DismissSecurityCheckV3(id="1234567", body={}),
            "GetSecurityChecksV3": falcon.GetSecurityChecksV3(),
            "GetSecurityCheckComplianceV3": falcon.GetSecurityCheckComplianceV3(id="1234567"),
            "IntegrationBuilderEndTransactionV3": falcon.IntegrationBuilderEndTransactionV3(id="1234567"),
            "IntegrationBuilderResetV3": falcon.IntegrationBuilderResetV3(id="1234567"),
            "IntegrationBuilderGetStatusV3": falcon.IntegrationBuilderGetStatusV3(id="1234567"),
            "IntegrationBuilderUploadV3": falcon.IntegrationBuilderUploadV3(id="1234567", source_id="source123", body={}),
            "GetAssetInventoryV3": falcon.GetAssetInventoryV3(),
            "GetDeviceInventoryV3": falcon.GetDeviceInventoryV3(),
            "GetIntegrationsV3": falcon.GetIntegrationsV3(),
            "GetActivityMonitorV3": falcon.GetActivityMonitorV3(integration_id="1234567"),
            "GetSupportedSaasV3": falcon.GetSupportedSaasV3(),
            "GetSystemLogsV3": falcon.GetSystemLogsV3(),
            "GetSystemUsersV3": falcon.GetSystemUsersV3(),
            "GetUserInventoryV3": falcon.GetUserInventoryV3()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
