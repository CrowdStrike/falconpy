# test_certificate_based_exclusions.py
# This class tests the CertificateBasedExclusions service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Classes to test - manually imported from sibling folder
from falconpy import HostMigration
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = HostMigration(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429, 500]


class TestHostMigration:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "aggregate_host_migration": falcon.aggregate_host_migration(body={}),
            "aggregate_migration": falcon.aggregate_migration(body={}),
            "perform_host_migration_action": falcon.perform_host_migration_action(id="1234567",
                                                                                  action_name="remove_hosts",
                                                                                  ids="1234567",
                                                                                  action_parameters=[{
                                                                                      "name": "group_id",
                                                                                      "value": "1234567"}]),
            "perform_host_migration_action_two": falcon.perform_host_migration_action(id="1234567",
                                                                                  action_name="kablooie",
                                                                                  ids="1234567",
                                                                                  action_parameters=[{
                                                                                      "name": "group_id",
                                                                                      "value": "1234567"}],
                                                                                      filter="something"),
            "get_host_migration_details": falcon.get_host_migration_details(ids="12345678"),
            "get_migration_destination": falcon.get_migration_destination(filter="filter"),
            "get_migration_destination_also": falcon.get_migration_destination(device_ids="12345678,87654321"),
            "perform_migration_job_action": falcon.perform_migration_job_action(action_name="rename_migration",
                                                                                filter="filter",
                                                                                ids="12345677",
                                                                                action_parameters=[{
                                                                                    "name": "my_migration",
                                                                                    "value": "new_migration"}]),
            "perform_migration_job_action_too": falcon.perform_migration_job_action(action_name="kaboom",
                                                                                filter="filter",
                                                                                ids="12345677",
                                                                                action_parameters=[{
                                                                                    "name": "my_migration",
                                                                                    "value": "new_migration"}]),
            "get_migration_job_details": falcon.get_migration_job_details(ids=12345678),
            "create_migration": falcon.create_migration(filter="test: 'test'",
                                                        name="name",
                                                        target_cid="cid",
                                                        device_ids=["12345678"]),
            "query_host_migration_ids": falcon.query_host_migration_ids(id="12345678",
                                                                        limit=1,
                                                                        filter="test:'test'"),
            "query_migration_jobs": falcon.query_migration_jobs()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
