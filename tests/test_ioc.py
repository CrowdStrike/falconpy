# test_ioc.py
# This class tests the IOC service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import IOC

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = IOC(auth_object=config)
AllowedResponses = [200, 201, 400, 404, 429]
Allowed403 = ["indicator_aggregate", "GetIndicatorsReport"]


class TestIOC:
    def ioc_run_all_tests(self):
        error_checks = True
        bogey = "1a2bcde34f5c6d789012fe3fa456f7e8"
        tests = {
            "indicator_combined": falcon.indicator_combined_v1(limit=1),
            "indicator_get": falcon.indicator_get_v1(ids='12345678'),
            "indicator_create": falcon.indicator_create_v1(body={},
                                                           comment="Unit testing",
                                                           indicators=[{
                                                               "type": "ipv4",
                                                               "value": "1.2.3.4",
                                                               "platforms": ["linux"]
                                                           }]
                                                           ),
            "indicator_create_also": falcon.indicator_create_v1(body={},
                                                                type="ipv4",
                                                                value="1.2.3.4",
                                                                platforms="linux,windows",
                                                                applied_globally=True
                                                                ),
            "indicator_delete": falcon.indicator_delete_v1(ids='12345678'),
            "indicator_update": falcon.indicator_update_v1(body={},
                                                           id="12345678",
                                                           mobile_action=["whatever"],
                                                           action="whatever",
                                                           description="Unit testing",
                                                           expiration="2021-10-22T11:03:16.123Z",
                                                           filter="",
                                                           severity="HIGH",
                                                           source="somewheres",
                                                           tags=["Bob"],
                                                           host_groups=["12345678"],
                                                           filename="something.txt",
                                                           metadata={"filename": "something.txt"},
                                                           comment="Unit testing",
                                                           applied_globally=True
                                                           ),
            "indicator_update_too": falcon.indicator_update_v1(bulk_update={"filter": "banana"}, indicators=[{"type": "ipv4"}]),
            "indicator_search": falcon.indicator_search_v1(parameters={'limit': 1}),
            "devices_count_legacy": falcon.devices_count_legacy(type='domain', value='hax0r.ru'),
            "devices_ran_on_legacy": falcon.devices_ran_on_legacy(type='domain', value='hax0r.ru'),
            "processes_ran_on_legacy": falcon.processes_ran_on_legacy(type='domain', value='hax0r.ru', device_id=bogey),
            "devices_count": falcon.devices_count(type='domain', value='hax0r.ru'),
            "devices_ran_on": falcon.devices_ran_on(type='domain', value='hax0r.ru'),
            "processes_ran_on": falcon.processes_ran_on(type='domain', value='hax0r.ru', device_id=bogey),
            "entities_processes": falcon.entities_processes(ids=['12345678']),
            "indicator_aggregate": falcon.indicator_aggregate(),
            "action_get": falcon.action_get("123456789"),
            "GetIndicatorsReport": falcon.get_indicators_report(filter="FQL something", search={"filter": "FQL"}, from_parent=False),
            "action_query": falcon.action_query(),
            "ioc_type_query": falcon.ioc_type_query(),
            "platform_query": falcon.platform_query(),
            "severity_query": falcon.severity_query()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                if not (tests[key]["status_code"] in [403, 500] and key in Allowed403):
                    error_checks = False
                    # print(tests[key])
                    # print(f"{key} operation returned a {tests[key]['status_code']} status code")

        return error_checks

    def test_all_functionality(self):
        assert self.ioc_run_all_tests() is True
