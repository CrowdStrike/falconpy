# test_identity_protection.py
# This class tests the identity_protection service class
import os
import sys
import json
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# flake8: noqa=E402
from falconpy.identity_protection import Identity_Protection as FalconIDP

auth = Authorization.TestAuthorization()
auth.serviceAuth()

falcon = FalconIDP(creds=json.loads(str(auth.config).replace("falcon_","").replace("'",'"')))
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestIdentityProtection:
    def serviceIDP_GraphQL(self):
        payload = {"query":"{\n  entities(first: 1)\n  {\n    nodes {\n      entityId    \n    }\n  }\n}"}
        # GraphQL is sometimes returning results as binary encoded
        result = falcon.GraphQL(body=payload)
        if not isinstance(result, dict):
            result = result.decode()
        if json.loads(result)["extensions"]["remainingPoints"] > 0:
            return True
        else:
            return False

    def test_GraphQL(self):
        assert self.serviceIDP_GraphQL() is True
