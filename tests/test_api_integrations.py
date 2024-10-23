# test_api_integraitons.py
# This class tests the API integrations service collection

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import APIIntegrations

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = APIIntegrations(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestAPIIntegrations:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetCombinedPluginConfigs": falcon.get_plugin_configs(),
            "ExecuteCommandProxy": falcon.execute_command_proxy(config_auth_type="string",
                        config_id="string",
                        definition_id="string",
                        id="string",
                        operation_id="string",
                        description="string",
                        version=123,
                        cookie={"Yes": "Please"},
                        header={"NotThe": "Footer"}
            ),
            "ExecuteCommand": falcon.execute_command(config_auth_type="string",
                        config_id="string",
                        definition_id="string",
                        id="string",
                        operation_id="string",
                        description="string",
                        version=123
            )
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
