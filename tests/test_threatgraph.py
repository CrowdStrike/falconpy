# test_threatgraph.py
# This class tests the ThreatGraph service collection

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ThreatGraph

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ThreatGraph(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 401, 403, 404, 429]


class TestThreatGraph:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "combined_edges_get": falcon.get_edges(),
            "combined_ran_on_get": falcon.get_ran_on(),
            "combined_summary_get": falcon.get_summary(ids="1234567"),
            "entities_vertices_get": falcon.get_vertices_v1(ids="whatever123"),
            "entities_vertices_getv2": falcon.get_vertices(ids="someotherID", vertex_type="incident"),
            "queries_edgetypes_get": falcon.get_edge_types()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
