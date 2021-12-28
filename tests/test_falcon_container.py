"""
test_falcon_container.py - This class tests the falcon_container service class
"""
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FalconContainer

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FalconContainer(auth_object=config)
AllowedResponses = [200, 201, 403, 404, 429]


class TestFalconContainer:

    def test_get_credentials(self):
        """Pytest harness hook"""
        assert bool(falcon.get_credentials()["status_code"] in AllowedResponses) is True
