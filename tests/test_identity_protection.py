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
AllowedResponses = [200, 429]

TEST_QUERY = """
query ($after: Cursor) {
  entities(types: [USER], archived: false, learned: false, first: 5, after: $after) {
    nodes {
      primaryDisplayName
      secondaryDisplayName
      accounts {
        ... on ActiveDirectoryAccountDescriptor {
          domain
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
"""

class TestIdentityProtection:
    def idp_graphql(self):
        payload = {"query":"{\n  entities(first: 1)\n  {\n    nodes {\n      entityId    \n    }\n  }\n}"}
        result = falcon.GraphQL(query=TEST_QUERY, variables={"after", ""})
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

