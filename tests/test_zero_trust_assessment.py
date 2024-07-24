"""
test_zero_trust_assessment.py - This class tests the zero_trust_assessment service class.

Thanks to my service class name, I also happen to be the last unit test series executed.
This means I test context authentication and logout on my way out the door.
"""
import os
import sys
from contextvars import ContextVar #, copy_context
from dataclasses import field, dataclass
import pytest
from typing import Dict
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ZeroTrustAssessment, APIHarnessV2

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ZeroTrustAssessment(auth_object=config)
AllowedResponses = [200, 201, 401, 403, 404, 429]  # Allowing 403 for unscopeable query_combined_assessments

@dataclass
class BaselessContextRequest:
    access_token: str = field(default='')


class ContextRequest:
    access_token: str = field(default='')
    cs_cloud: str = field(default='')


class TestZeroTrustAssessment:

    def test_get_assessment(self):
        """Pytest harness hook"""
        assert bool(falcon.getAssessmentV1(ids="12345678")["status_code"] in AllowedResponses) is True

    def test_get_complance(self):
        """Pytest harness hook"""
        assert bool(falcon.get_compliance()["status_code"] in AllowedResponses) is True

    def test_get_assessments_by_score(self):
        """Pytest harness hook"""
        assert bool(falcon.get_assessments_by_score(filter="score:>1")["status_code"] in AllowedResponses) is True

    def test_query_combined_assessment(self):
        """Pytest harness hook"""
        assert bool(falcon.query_combined_assessments()["status_code"] in AllowedResponses) is True

    # Test context authentication right before logout
    @pytest.mark.skipif(config.base_url != "https://api.crowdstrike.com",
                    reason="Unit testing unavailable in this region"
                    )
    def test_context_authentication_no_base(self):
        request_context = ContextVar("request", default=BaselessContextRequest())
        req: BaselessContextRequest = request_context.get()
        req.access_token = auth.authorization.token()["body"]["access_token"]
        tok = request_context.set(req)
        zta = ZeroTrustAssessment(pythonic=True, debug=config.debug)
        request_context.reset(tok)
        assert bool(zta.get_assessments_by_score(filter="score:>30").status_code == 200)

    @pytest.mark.skipif(config.base_url != "https://api.crowdstrike.com",
                    reason="Unit testing unavailable in this region"
                    )
    def test_uber_context_authentication_no_base(self):
        request_context = ContextVar("request", default=BaselessContextRequest())
        req: BaselessContextRequest = request_context.get()
        req.access_token = auth.authorization.token()["body"]["access_token"]
        tok = request_context.set(req)
        uber = APIHarnessV2(pythonic=True, debug=config.debug)
        request_context.reset(tok)
        assert min(bool(uber.command("QueryDevicesByFilterScroll").status_code == 200),
                   bool(uber.auth_style == "CONTEXT")
                   )

    @pytest.mark.skipif(config.base_url != "https://api.crowdstrike.com",
                    reason="Unit testing unavailable in this region"
                    )
    def test_context_authentication(self):
        another_request_context = ContextVar("another-request", default=ContextRequest())
        req: ContextRequest = another_request_context.get()
        req.access_token = auth.authorization.token()["body"]["access_token"]
        req.cs_cloud = config.base_url
        another_request_context.set(req)
        zta = ZeroTrustAssessment(pythonic=True, debug=config.debug)
        assert bool(zta.get_assessments_by_score(filter="score:>30").status_code == 200)

    # This should be the last test executed, log out the token
    @staticmethod
    def test_logout():
        """Pytest harness hook"""
        assert bool(auth.clear_env_token()) is True
