# test_federated_connections.py
# This class tests the federated_connections service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import FederatedConnections

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FederatedConnections(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestFederatedConnections:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "PostFederatedConnectionsConfig": falcon.post_federated_connections_config(cluster_url="string",
                                                                                       connection_id="string",
                                                                                       view_token="string"),
            "DeleteFederatedConnectionsConfig": falcon.delete_federated_connections_config(connection_id="string"),
            "PatchFederatedConnectionsConfig": falcon.patch_federated_connections_config(connection_id="string",
                                                                                         cluster_url="string",
                                                                                         view_token="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
