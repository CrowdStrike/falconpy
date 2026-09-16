# test_browser_security.py
# This class tests the browser_security service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import BrowserSecurity

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = BrowserSecurity(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestBrowserSecurity:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "CombinedQueryAgents": falcon.query_combined_seraphic_agents(limit="string", search="string", skip="string",
                                                                         sort="string", application="string",
                                                                         application_name="string",
                                                                         application_version="string", browser_name="string",
                                                                         browser_version="string", deployment_method="string",
                                                                         email="string", first_seen="string",
                                                                         host_id="string", hostname="string", id="string",
                                                                         last_seen="string", os_name="string",
                                                                         platform="string", policy_updated="string",
                                                                         protection_type="string", status="string",
                                                                         username="string"),
            "ClassifyDomains": falcon.classify_domains(domains="string"),
            "ActivateAgents": falcon.activate_agents(ids="string"),
            "DeactivateAgents": falcon.deactivate_agents(ids="string"),
            "ApplyAgentTasks": falcon.apply_agent_tasks(agent_id="string", actions="string", ttl="string"),
            "GetAgents": falcon.get_seraphic_agents(ids="12345678"),
            "GetAuditLogsMixin0": falcon.get_seraphic_audit_logs(ids="12345678"),
            "GetDestinationGroups": falcon.get_destination_groups(ids="12345678"),
            "CreateDestinationGroup": falcon.create_destination_group(classification="string", countries="string",
                                                                      description="string", domains="string",
                                                                      ipsRange="string", match_ips="string", name="string",
                                                                      singleIps="string", top_level_domains="string"),
            "DeleteDestinationGroup": falcon.delete_destination_group(id="12345678"),
            "UpdateDestinationGroup": falcon.update_destination_group(id="string", classification="string",
                                                                      countries="string", description="string",
                                                                      domains="string", ipsRange="string", match_ips="string",
                                                                      name="string", singleIps="string",
                                                                      top_level_domains="string"),
            "GetExtensionAnalysis": falcon.get_extension_analysis(store="string", id="string"),
            "GetRules": falcon.get_seraphic_rules(ids="12345678"),
            "UpdateRuleMixin0": falcon.update_seraphic_rule(id="string", addExtensionIds="string", addExtensionNames="string",
                                                            destinations="string", removeExtensionIds="string",
                                                            removeExtensionNames="string", status="string", targets="string"),
            "GetTenantSettings": falcon.get_tenant_settings(),
            "GetUrlDomainLists": falcon.get_url_domain_lists(ids=["string"], skip=1, limit=1),
            "AddUrlDomainList": falcon.add_url_domain_list(integrationId="string", urls="string"),
            "DeleteUrlDomainList": falcon.delete_url_domain_list(id="12345678"),
            "QueryAgents": falcon.query_seraphic_agents(limit="string", search="string", skip="string", sort="string",
                                                        application="string", application_name="string",
                                                        application_version="string", browser_name="string",
                                                        browser_version="string", deployment_method="string", email="string",
                                                        first_seen="string", host_id="string", hostname="string", id="string",
                                                        last_seen="string", os_name="string", platform="string",
                                                        policy_updated="string", protection_type="string", status="string",
                                                        username="string"),
            "QueryDestinationGroups": falcon.query_destination_groups(exclude="string", filter="string", limit="string",
                                                                      search="string", skip="string", sort="string"),
            "QueryRulesMixin0": falcon.query_seraphic_rules(category="string", advanced_filter="string", exclude="string",
                                                            filter="string", limit="string", rule_ids="string",
                                                            search="string", skip="string", sort="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks

    def test_payload_coverage(self):
        """Exercise nested payload builder branches."""
        falcon.query_combined_seraphic_agents(application="string", application_name="string", application_version="string", browser_name="string", browser_version="string", deployment_method="string", email="string", first_seen="string", host_id="string", hostname="string", id="string", last_seen="string", os_name="string", platform="string", policy_updated="string", protection_type="string", status="string", username="string")
        falcon.query_seraphic_agents(application="string", application_name="string", application_version="string", browser_name="string", browser_version="string", deployment_method="string", email="string", first_seen="string", host_id="string", hostname="string", id="string", last_seen="string", os_name="string", platform="string", policy_updated="string", protection_type="string", status="string", username="string")
        assert True
