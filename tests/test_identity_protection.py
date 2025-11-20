# test_identity_protection.py
# This class tests the identity_protection service class
import os
import sys
import json
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# flake8: noqa=E402
from falconpy import IdentityProtection

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()

falcon = IdentityProtection(auth_object=config)
AllowedResponses = [200, 400, 403, 429]

# TEST_QUERY = r"""query ($after: Cursor) {
#   entities(types: [USER], archived: false, learned: false, first: 5, after: $after) {
#     nodes {
#       primaryDisplayName
#       secondaryDisplayName
#       accounts {
#         ... on ActiveDirectoryAccountDescriptor {
#           domain
#         }
#       }
#     }
#     pageInfo {
#       hasNextPage
#       endCursor
#     }
#   }
# }"""

TEST_QUERY = """
{
  entities (   
    roles: [BuiltinAdministratorRole]
    sortKey: PRIMARY_DISPLAY_NAME
    sortOrder: ASCENDING
    # Limit the response to two records:
    first: 2
  )
  {
    # Include pageInfo properties for pagination:  
    pageInfo {
      # Are there more results to obtain?  
      hasNextPage
      # Identify the last records in the results:
      endCursor
    }
    nodes {
      primaryDisplayName
      secondaryDisplayName
    }
  }
}
"""
class TestIdentityProtection:
    def idp_graphql(self):
        payload = {"query":"{\n  entities(first: 1)\n  {\n    nodes {\n      entityId    \n    }\n  }\n}"}
        result = falcon.GraphQL(query=TEST_QUERY, variables={"after": "$after"})
        if not isinstance(result, dict):
            result = json.loads(result.decode())
        else:
            result = result["body"]

        if result.get("data", {}).get("entities", {}).get("pageInfo", {}).get("hasNextPage", None):
            next_page = result["data"].get("entities", {}).get("pageInfo", {}).get("endCursor", None)
            result = falcon.graphql(query=TEST_QUERY, variables={"after": next_page})["body"]

        if "extensions" in result:
            if result["extensions"]["remainingPoints"] > 0:
                return True
            else:
                pytest.skip("Identity protection API failure")
                # return False
        else:
            # Prolly failed login, check yer API key
            # return False
            pytest.skip("Identity protection API failure")


    @pytest.mark.skipif(falcon.base_url.lower() in ["https://api.laggar.gcw.crowdstrike.com","usgov1"],
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_graphql(self):
        assert self.idp_graphql() is True


    def service_idp_remaining_tests(self):
        if falcon.base_url.lower() != "https://api.crowdstrike.com":
            pytest.skip("Identity protection testing is not supported in this region")
        error_checks = True
        tests = {
            "GetSensorAggregates": falcon.get_sensor_aggregates(date_ranges=[{}]),
            "GetSensorDetails": falcon.get_sensor_details(ids="12345678"),
            "QuerySensorsByFilter": falcon.query_sensors(limit=1),
            "get_policy_rules": falcon.get_policy_rules(ids="12345678"),
            "post_policy_rules": falcon.create_policy_rule(simulation_mode=True),
            "delete_policy_rules": falcon.delete_policy_rules("12345678"),
            "get_policy_rules_query": falcon.query_policy_rules(),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # print(f"{key}: {tests[key]}")
                error_checks = False

        return error_checks

    def test_remaining_functionality(self):
        assert self.service_idp_remaining_tests() is True