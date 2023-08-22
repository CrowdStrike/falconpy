"""
test_filevantage.py -  This class tests the FileVantage service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FileVantage

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FileVantage(auth_object=config)
AllowedResponses = [200, 202, 429]  # Adding rate-limiting as an allowed response for now


class TestFileVantage:
    """
    FileVantage Service Class test harness
    """
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_query_changes(self):
        """Pytest harness hook"""
        assert bool(falcon.query_changes(limit=1)["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_query_changes_scroll(self):
        """Pytest harness hook"""
        assert bool(falcon.query_changes_scroll(limit=1)["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_get_changes(self):
        """Pytest harness hook"""
        # Also testing lazy loading of the ids parameter
        assert bool(
            falcon.get_changes("12345678")["status_code"] in AllowedResponses
        ) is True
