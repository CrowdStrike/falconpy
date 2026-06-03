# test_api_clients.py
# This class tests the api_clients service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import ApiClients

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ApiClients(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429, 500]


class TestApiClients:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetAccessibleScopes": falcon.get_accessible_scopes(),
            "ResetAPIClientSecret": falcon.reset_api_client_secret(ids=["string"], action_name="string"),
            "GetAPIClients": falcon.get_api_clients(ids="12345678"),
            "CreateAPIClient": falcon.create_api_client(description="string", name="string", scopes="string"),
            "DeleteAPIClients": falcon.delete_api_clients(ids="12345678"),
            "UpdateAPIClient": falcon.update_api_client(ids="string", description="string", name="string", scopes="string"),
            "GetAllAPIClientIdsForCustomer": falcon.get_all_api_client_ids_for_customer(offset=1, limit=1, sort="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
