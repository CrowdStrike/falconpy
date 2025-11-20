""" test_firewall_management.py - This class tests the firewall_management service class"""
import os
import sys
import datetime
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FirewallManagement

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FirewallManagement(auth_object=config)
AllowedResponses = [200, 201, 202, 203, 204, 400, 401, 403, 404, 429]
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
        result = falcon.create_rule_group(name=rule_group_name,
                                          enabled=False,
                                          cs_username="HarryHenderson"
                                          )
        global rule_group_id
        rule_group_id = "1234567890"
        if result["status_code"] not in [400, 401, 403, 404, 429]:
            try:
                if result["body"]["resources"]:
                    rule_group_id = result["body"]["resources"][0]
            except KeyError:
                pytest.skip("Skipped due to API issue.")

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
            "update_policy_container": falcon.update_policy_container(default_inbound="something",
                                                                      default_outbound="something_else",
                                                                      platform_id="linux",
                                                                      enforce=False,
                                                                      is_default_policy=False,
                                                                      test_mode=True,
                                                                      rule_group_ids=["12345", "67890"],
                                                                      local_logging=False,
                                                                      policy_id="987123"
                                                                      ),
            "update_policy_container_v1": falcon.update_policy_container_v1(default_inbound="something",
                                                                            default_outbound="something_else",
                                                                            platform_id="linux",
                                                                            enforce=False,
                                                                            local_logging=False,
                                                                            is_default_policy=False,
                                                                            test_mode=True,
                                                                            rule_group_ids="12345,67890",
                                                                            policy_id="987123"
                                                                            ),
            "create_rule_group": self.set_rule_group_id(),
            "create_rule_group_fail_one": falcon.create_rule_group(rules={"whatever": "bro"}),
            "create_rule_group_fail_two": falcon.create_rule_group(rules=[{"whatever": "bro"}]),
            "create_rule_group_fail_three": falcon.create_rule_group(fields={},
                                                                     icmp={},
                                                                     local_address={},
                                                                     remote_address={},
                                                                     local_port={},
                                                                     remote_port={},
                                                                     log=False,
                                                                     monitor={},
                                                                     name="testing",
                                                                     temp_id="whatever",
                                                                     rule_enabled=False,
                                                                     rule_description="Unit testing",
                                                                     address_family="ip4",
                                                                     rule_name="Testing",
                                                                     action="deny",
                                                                     direction="out",
                                                                     protocol=6,
                                                                     platform_ids="windows"
                                                                     ),
            "create_rule_group_fail_four": falcon.create_rule_group(fields=[],
                                                                    icmp={},
                                                                    local_address=[],
                                                                    remote_address=[],
                                                                    local_port=[],
                                                                    remote_port=[],
                                                                    log=False,
                                                                    monitor={},
                                                                    name="testing",
                                                                    temp_id="whatever",
                                                                    rule_enabled=False,
                                                                    rule_description="Unit testing",
                                                                    address_family="ip4",
                                                                    rule_name="Testing",
                                                                    action="deny",
                                                                    direction="out",
                                                                    protocol=6,
                                                                    platform_ids=["windows"]
                                                                    ),
            "create_rule_group_validation": falcon.create_rule_group_validation(description="Testing",
                                                                                enabled=False,
                                                                                name="Debug testing",
                                                                                platform="Windows",
                                                                                rules=[{"name": "Testing"}]
                                                                                ),
            "update_rule_group_validation": falcon.update_rule_group_validation(id="12345678",
                                                                                tracking="Whatever",
                                                                                diff_operations=[{"whatever": "brah"}],
                                                                                rule_ids="12345,67890",
                                                                                rule_versions="1,2,3"),
            "validate_filepath_pattern": falcon.validate_filepath_pattern(filepath_pattern="**/*.py", filepath_test_string="works.py"),    
            "get_rule_groups": falcon.get_rule_groups(ids=rule_group_id),
            "updat3_rule_group": falcon.update_rule_group(id="12345678",
                                                          tracking="Whatever",
                                                          diff_operations=[{"whatever": "brah"}],
                                                          rule_ids="12345,67890",
                                                          rule_versions="1,2,3"
                                                          ),
            "update_rule_group": falcon.update_rule_group(id="12345678",
                                                          name=rule_group_name,
                                                          enabled=False,
                                                          diff_from="somewhere",
                                                          diff_op="something",
                                                          diff_path="somepath"
                                                          ),
            "update_rule_group_again": falcon.update_rule_group(id="12345678",
                                                          name=rule_group_name,
                                                          enabled=False,
                                                          diff_operations={"whatever": "dude"}
                                                          ),
            "delete_rule_groups": falcon.delete_rule_groups(ids=rule_group_id, cs_username="KyloRen"),
            "get_rules": falcon.get_rules(ids="12345678"),
            "query_events": falcon.query_events(),
            "query_firewall_fields": falcon.query_firewall_fields(),
            "query_platforms": falcon.query_platforms(),
            "query_policy_rules": falcon.query_policy_rules(),
            "query_rule_groups": falcon.query_rule_groups(),
            "query_rules": falcon.query_rules(),
            "get_network_locations_details": falcon.get_network_locations_details(ids="12345678"),
            "update_network_locations_metadata": falcon.update_network_locations_metadata(cid="12345678",
                                                                                          dns_resolution_targets_polling_interval=10,
                                                                                          https_reachable_hosts_polling_interval=10,
                                                                                          icmp_request_targets_polling_interval=10,
                                                                                          location_precedence=["BobIsFirst"]),
            "update_network_locations_precedence": falcon.update_network_locations_precedence(cid="1234567", location_precedence=["LarryIsSecond"]),
            "get_network_locations": falcon.get_network_locations(ids="987654321"),
            "create_network_locations": falcon.create_network_locations(connection_types={"wired": True},
                                                                        created_by="12345678",
                                                                        created_on="Yesterday",
                                                                        default_gateways=["1.2.3.4"],
                                                                        description="ThisLocation",
                                                                        dhcp_servers=["10.10.1.10"],
                                                                        dns_resolution_targets={"targets": [{
                                                                            "hostname": "ChucksBox",
                                                                            "ip_match": "10.12.12.120"
                                                                        }]},
                                                                        dns_servers=["5.4.3.2"],
                                                                        enabled=False,
                                                                        host_addresses=["9.8.7.7"],
                                                                        https_reachable_hosts={
                                                                            "hostnames": ["Daryl", "Charlie"]
                                                                        },
                                                                        icmp_request_targets={
                                                                            "targets": ["Tom", "Sarah"]
                                                                        },
                                                                        name="FalconPy Unit Testing"),
            "update_network_locations": falcon.update_network_locations(connection_types={"wired": True},
                                                                        created_by="12345678",
                                                                        created_on="Yesterday",
                                                                        default_gateways=["1.2.3.4"],
                                                                        description="ThisLocation",
                                                                        dhcp_servers=["10.10.1.10"],
                                                                        dns_resolution_targets={"targets": [{
                                                                            "hostname": "ChucksBox",
                                                                            "ip_match": "10.12.12.120"
                                                                        }]},
                                                                        dns_servers=["5.4.3.2"],
                                                                        enabled=False,
                                                                        host_addresses=["9.8.7.7"],
                                                                        https_reachable_hosts={
                                                                            "hostnames": ["Daryl", "Charlie"]
                                                                        },
                                                                        icmp_request_targets={
                                                                            "targets": ["Tom", "Sarah"]
                                                                        },
                                                                        name="FalconPy Unit Testing",
                                                                        id="12345677",
                                                                        modified_by="Douglas",
                                                                        modified_on="Last Thursday"
                                                                        ),
            "upsert_network_locations": falcon.upsert_network_locations(connection_types={"wired": True},
                                                                        created_by="12345678",
                                                                        created_on="Yesterday",
                                                                        default_gateways=["1.2.3.4"],
                                                                        description="ThisLocation",
                                                                        dhcp_servers=["10.10.1.10"],
                                                                        dns_resolution_targets={"targets": [{
                                                                            "hostname": "ChucksBox",
                                                                            "ip_match": "10.12.12.120"
                                                                        }]},
                                                                        dns_servers=["5.4.3.2"],
                                                                        enabled=False,
                                                                        host_addresses=["9.8.7.7"],
                                                                        https_reachable_hosts={
                                                                            "hostnames": ["Daryl", "Charlie"]
                                                                        },
                                                                        icmp_request_targets={
                                                                            "targets": ["Tom", "Sarah"]
                                                                        },
                                                                        name="FalconPy Unit Testing",
                                                                        id="12345677",
                                                                        modified_by="Douglas",
                                                                        modified_on="Last Thursday"),
            "delete_network_locations": falcon.delete_network_locations(ids="3841341345"),
            "query_network_locations": falcon.query_network_locations()
        }
        for key in tests:

            if tests[key]["status_code"] not in AllowedResponses:
                if os.getenv("DEBUG_API_BASE_URL", "us1").lower() != "https://api.laggar.gcw.crowdstrike.com":
                    # Flakiness
                    if not key in ["delete_rule_groups", "get_network_locations", "update_network_locations_precedence"]:
                        error_checks = False
                # print(f"Failed on {key} with {tests[key]}")

        return error_checks

    @pytest.mark.skipif(os.getenv("DEBUG_API_BASE_URL", "us1").lower() in [
        "https://api.laggar.gcw.crowdstrike.com", "usgov1"
        ], reason="GovCloud flakiness")
    def test_all_paths(self):
        """Pytest harness hook"""
        assert self.firewall_test_all_code_paths() is True