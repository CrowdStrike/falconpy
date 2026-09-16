# test_network_containment.py
# This class tests the network_containment service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import NetworkContainment

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NetworkContainment(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestNetworkContainment:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetContainmentAllowlistRules": falcon.get_allowlist_rules(ids="12345678"),
            "CreateContainmentAllowlistRules": falcon.create_allowlist_rules(rules="string"),
            "DeleteContainmentAllowlistRules": falcon.delete_allowlist_rules(ids="12345678"),
            "UpdateContainmentAllowlistRules": falcon.update_allowlist_rules(rules="string"),
            "QueryContainmentAllowlistRules": falcon.query_allowlist_rules(filter="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
