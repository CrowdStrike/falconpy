""" test_firewall_management.py - This class tests the firewall_management service class"""
import os
import sys
import datetime
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.firewall_management import Firewall_Management as FalconFirewall

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconFirewall(access_token=token)
AllowedResponses = [200, 201, 202, 203, 204, 400, 404, 429]
fmt = '%Y-%m-%d %H:%M:%S'
stddate = datetime.datetime.now().strftime(fmt)
sdtdate = datetime.datetime.strptime(stddate, fmt)
sdtdate = sdtdate.timetuple()
jdate = sdtdate.tm_yday
jdate = "{}{}".format(stddate.replace("-", "").replace(":", "").replace(" ", ""), jdate)
rule_group_name = f"falconpy_debug_{jdate}"
rule_group_id = ""


class TestFirewallManagement:
    """Test harness for the Firewall Management Service Class"""

    @staticmethod
    def set_rule_group_id():
        result = falcon.create_rule_group(body={
            "name": rule_group_name,
            "enabled": False
        }, cs_username="HarryHenderson")
        global rule_group_id
        rule_group_id = result["body"]["resources"][0]

        return result

    def firewall_test_all_code_paths(self):
        """Test every code path, accepts all errors except 500"""
        error_checks = True
        tests = {
            "aggregate_events": falcon.aggregate_events(body={}),
            "aggregate_policy_rules": falcon.aggregate_policy_rules(body={}),
            "aggregate_rule_groups": falcon.aggregate_rule_groups(body={}),
            "aggregate_rules": falcon.aggregate_rules(body={}),
            "get_events": falcon.get_events(ids="12345678"),
            "get_firewall_fields": falcon.get_firewall_fields(ids="12345678"),
            "get_platforms": falcon.get_platforms(ids="12345678"),
            "get_policy_containers": falcon.get_policy_containers(ids="12345678"),
            "update_policy_container": falcon.update_policy_container(body={}, cs_username="BillTheCat"),
            "create_rule_group": self.set_rule_group_id(),
            "get_rule_groups": falcon.get_rule_groups(ids=rule_group_id),
            "update_rule_group": falcon.update_rule_group(body={
                "id": rule_group_id,
                "name": rule_group_name,
                "enabled": True
            }, cs_username="Calcifer"),
            "delete_rule_groups": falcon.delete_rule_groups(ids=rule_group_id, cs_username="KyloRen"),
            "get_rules": falcon.get_rules(ids="12345678"),
            "query_events": falcon.query_events(),
            "query_firewall_fields": falcon.query_firewall_fields(),
            "query_platforms": falcon.query_platforms(),
            "query_policy_rules": falcon.query_policy_rules(),
            "query_rule_groups": falcon.query_rule_groups(),
            "query_rules": falcon.query_rules()
        }
        for key in tests:

            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
#               print(f"Failed on {key} with {tests[key]}")
#            print(tests[key])
        return error_checks

    def test_all_paths(self):
        """Pytest harness hook"""
        assert self.firewall_test_all_code_paths() is True
