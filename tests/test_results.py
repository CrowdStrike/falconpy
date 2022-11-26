"""
test_results.py -  This class tests the Results class
"""
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# We'll use Hosts to retrieve data to test results with
from falconpy import Hosts

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Hosts(auth_object=config)
AllowedResponses = [200, 202, 429]  # Adding rate-limiting as an allowed response for now

class TestResults:
    """
    Results Class test harness
    """
    pass
    # def test_query_changes(self):
    #     """Pytest harness hook"""
    #     assert bool(True) is True


    # def test_get_changes(self):
    #     """Pytest harness hook"""
    #     # Also testing lazy loading of the ids parameter
    #     assert bool(
    #         falcon.get_changes("12345678")["status_code"] in AllowedResponses
    #     ) is True
