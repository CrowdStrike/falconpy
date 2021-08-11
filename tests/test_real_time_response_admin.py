"""
test_real_time_response_admin.py - This class tests the real_time_response_admin service class
"""
import datetime
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.real_time_response_admin import Real_Time_Response_Admin as FalconRTR

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconRTR(creds={"client_id": auth.config["falcon_client_id"],
                          "client_secret": auth.config["falcon_client_secret"]
                          })
AllowedResponses = [200, 201, 400, 404, 429]


class TestRTR:
    """RTR Admin test harness"""
    @staticmethod
    def rtra_test_all_code_paths():
        """Tests all code paths, accepts all errors except 500"""
        upload_file = "tests/testfile.png"
        fmt = '%Y-%m-%d %H:%M:%S'
        stddate = datetime.datetime.now().strftime(fmt)
        sdtdate = datetime.datetime.strptime(stddate, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
        jdate = "{}{}".format(stddate.replace("-", "").replace(":", "").replace(" ", ""), jdate)
        upload_filename = "%s_testfile.png" % jdate

        file_payload = {'name': upload_filename, 'description': 'FalconPy Unit Testing'}
        files_detail = [
            ('file', ('testfile.png', open(upload_file, 'rb'), 'image/png'))
        ]

        error_checks = True
        tests = {
            "batch_admin_cmd": falcon.BatchAdminCmd(body={})["status_code"],
            "check_admin_command_status": falcon.RTR_CheckAdminCommandStatus(parameters={})["status_code"],
            "execute_admin_command": falcon.RTR_ExecuteAdminCommand(body={})["status_code"],
            "get_put_files": falcon.RTR_GetPut_Files(ids='12345678')["status_code"],
            "create_put_files": falcon.RTR_CreatePut_Files(data=file_payload, files=files_detail)["status_code"],
            "delete_put_files": falcon.RTR_DeletePut_Files(ids='12345678')["status_code"],
            "get_scripts": falcon.RTR_GetScripts(ids='12345678')["status_code"],
            "create_scripts": falcon.RTR_CreateScripts(data={}, files=[])["status_code"],
            "delete_scripts": falcon.RTR_DeleteScripts(ids='12345678')["status_code"],
            "update_scripts": falcon.RTR_UpdateScripts(data={}, files=[])["status_code"],
            "list_put_files": falcon.RTR_ListPut_Files()["status_code"],
            "list_scripts": falcon.RTR_ListScripts()["status_code"]
        }
        for key in tests:
            if tests[key] not in AllowedResponses:
                error_checks = False

        return error_checks

    @staticmethod
    def test_list_scripts():
        """Pytest harness hook"""
        assert bool(falcon.RTR_ListScripts(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    @staticmethod
    def test_list_put_files():
        """Pytest harness hook"""
        assert bool(falcon.RTR_ListPut_Files(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    def test_all_code_paths(self):
        """Pytest harness hook"""
        assert self.rtra_test_all_code_paths() is True

    @staticmethod
    def test_logout():
        """Pytest harness hook"""
        assert bool(falcon.auth_object.revoke(
            falcon.auth_object.token()["body"]["access_token"]
            )["status_code"] in [200, 201]) is True
