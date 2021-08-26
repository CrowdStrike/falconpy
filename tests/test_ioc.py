# test_ioc.py
# This class tests the IOC service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.ioc import IOC

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = IOC(access_token=token)
AllowedResponses = [200, 201, 404, 429]


class TestIOC:
    def ioc_run_all_tests(self):
        error_checks = True
        bogey = "1a2bcde34f5c6d789012fe3fa456f7e8"
        tests = {
            "indicator_combined": falcon.indicator_combined_v1(limit=1),
            "indicator_get": falcon.indicator_get_v1(ids='12345678'),
            "indicator_create": falcon.indicator_create_v1(body={}),
            "indicator_delete": falcon.indicator_delete_v1(ids='12345678'),
            "indicator_update": falcon.indicator_update_v1(body={}),
            "indicator_search": falcon.indicator_search_v1(parameters={'limit': 1}),
            "devices_count": falcon.devices_count(type='domain', value='hax0r.ru'),
            "devices_ran_on": falcon.devices_ran_on(type='domain', value='hax0r.ru'),
            "processes_ran_on": falcon.processes_ran_on(type='domain', value='hax0r.ru', device_id=bogey),
            "entities_processes": falcon.entities_processes(ids=['12345678'])

        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
            # print(tests[key])
            # print(f"{key} operation returned a {tests[key]['status_code']} status code")

        return error_checks

    def test_all_functionality(self):
        assert self.ioc_run_all_tests() is True
