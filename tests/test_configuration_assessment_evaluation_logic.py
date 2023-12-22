"""
test_configuration_assessment_evaluation_logic.py - 
This class tests the configuration assessment evaluation logic service class
"""
import os
import sys
from datetime import datetime, timedelta
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ConfigurationAssessmentEvaluationLogic

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ConfigurationAssessmentEvaluationLogic(auth_object=config)
AllowedResponses = [200, 201, 403, 404, 429]


class TestConfigurationAssessmentEvaluationLogic:
    """Class to test the Configuration Assessment Evaluation Logic Service Class."""

    def test_get_eval_logic(self):
        """Pytest harness hook"""
        result = falcon.get_evaluation_logic(ids="12345678")
        assert bool(result["status_code"] in AllowedResponses) is True
