"""
test_mobile_enrollment.py - This class tests the mobile enrollment service class
"""
import os
import sys
from datetime import datetime, timedelta, timezone
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import MobileEnrollment

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = MobileEnrollment(auth_object=config)
AllowedResponses = [200, 201, 403, 404, 429]


class TestMobileEnrollment:
    """Class to test the Mobile Enrollment Service Class."""

    def test_device_enroll(self):
        """Pytest harness hook"""
        result = falcon.device_enroll(
            action_name="re-enroll",
            email_addresses="no_reply@crowdstrike.com",
            expires_at=(datetime.now(timezone.utc) + timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%SZ")
        )
        assert bool(result["status_code"] in AllowedResponses) is True

    def test_device_enroll_v4(self):
        """Pytest harness hook"""
        result = falcon.device_enroll_v4(
            action_name="re-enroll",
            email_addresses="no_reply@crowdstrike.com",
            expires_at=(datetime.now(timezone.utc) + timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%SZ")
        )
        assert bool(result["status_code"] in AllowedResponses) is True
