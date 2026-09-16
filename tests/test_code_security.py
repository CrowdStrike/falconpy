# test_code_security.py
# This class tests the code_security service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import CodeSecurity

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CodeSecurity(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestCodeSecurity:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetSCMRepositoryAggregates": falcon.get_scm_repository_aggregates(field="string", filter="string"),
            "GetBranchConfig": falcon.get_branch_config(connection_id="string", repository_ids="string"),
            "CreateBranchConfig": falcon.create_branch_config(),
            "DeleteBranchConfig": falcon.delete_branch_config(ids="12345678"),
            "UpdateBranchConfig": falcon.update_branch_config(id="string"),
            "ListSCMConnections": falcon.list_scm_connections(provider="string"),
            "GetSCMConnection": falcon.get_scm_connection(),
            "GetSCMConnectionWithPathParam": falcon.get_scm_connection(uuid="12345678"),
            "DeleteSCMConnection": falcon.delete_scm_connection(),
            "DeleteSCMConnectionWithPathParam": falcon.delete_scm_connection(uuid="12345678"),
            "TriggerSCMSync": falcon.trigger_scm_sync(),
            "TriggerSCMSyncWithPathParam": falcon.trigger_scm_sync(uuid="12345678", body={}),
            "ListExclusionRules": falcon.list_scm_exclusion_rules(connection_id="string"),
            "CreateExclusionRule": falcon.create_scm_exclusion_rule(),
            "DeleteExclusionRule": falcon.delete_scm_exclusion_rule(),
            "DeleteExclusionRuleWithPathParam": falcon.delete_scm_exclusion_rule(id="12345678"),
            "ListSCMRepositories": falcon.list_scm_repositories(filter="string", sort="string", limit=1, offset=1),
            "ExchangeGitHubAppCode": falcon.exchange_github_app_code(code="string", installation_id="string", org="string",
                                                                     state="string"),
            "RegisterSCMApp": falcon.register_scm_app(app_id="string", installation_id="string", org="string",
                                                      private_key="string", webhook_secret="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
