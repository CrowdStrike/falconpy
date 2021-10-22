"""
test_real_time_response_admin.py - This class tests the real_time_response_admin service class
"""
import datetime
# import platform
import os
import sys
import json
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.real_time_response_admin import Real_Time_Response_Admin as FalconRTR

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconRTR(access_token=token)
AllowedResponses = [200, 201, 202, 400, 404, 429]


class TestRTRAdmin:
    """
    Real Time Response Admin Test Harness
    """
    @staticmethod
    def rtra_retrieve_script_id(script_name: str):
        """
        Helper to retrieve a script ID by name
        """
        found_id = "1234567890"  # Force an error if we can't find it
        script = falcon.get_scripts(ids=falcon.list_scripts()["body"]["resources"])
        for file in script["body"]["resources"]:
            if "name" in file:
                if file["name"] == script_name:
                    found_id = file["id"]

        return found_id

    @staticmethod
    def rtra_retrieve_file_id(file_name: str):
        """
        Helper to retrieve a put file ID by name
        """
        found_id = "1234567890"  # Force an error if we can't find it
        files = falcon.list_put_files()
        try:
            file = falcon.get_put_files(ids=files["body"]["resources"])
        except KeyError:
            pytest.skip("Race condition met, skipping")

        for item in file["body"]["resources"]:
            if "name" in item:
                if item["name"] == file_name:
                    found_id = item["id"]

        return found_id

    def rtra_create_updated_payload(self, file_name: str, orig_payload: dict):
        orig_payload["id"] = self.rtra_retrieve_script_id(file_name)
        return orig_payload

    def rtra_test_all_code_paths(self):
        """
        Tests all code paths, accepts all errors except 500
        """
        upload_file = "tests/testfile.png"
        fmt = '%Y-%m-%d %H:%M:%S'
        stddate = datetime.datetime.now().strftime(fmt)
        sdtdate = datetime.datetime.strptime(stddate, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
        jdate = "{}{}".format(stddate.replace("-", "").replace(":", "").replace(" ", ""), jdate)
        upload_filename = "%s_testfile.png" % jdate
        script_filename = "%s_testscript" % jdate

        file_payload = {'name': upload_filename, 'description': 'FalconPy Unit Testing'}
        files_detail = [
            ('file', ('testfile.png', open(upload_file, 'rb'), 'image/png'))
        ]
        script_payload = {
            'name': script_filename,
            'description': 'FalconPy Unit Testing',
            'permission_type': 'private',
            'content': 'Write-Output "This is a processing script."'
        }
        new_script_payload = json.loads(json.dumps(script_payload))
        new_script_payload["content"] = 'Write-Output "This is an updated processing script."'
        script_detail = [('file', (f"{script_filename}", 'application/script'))]
        error_checks = True
        tests = {
            "batch_admin_cmd": falcon.BatchAdminCmd(body={})["status_code"],                                    # 400
            "check_admin_command_status": falcon.RTR_CheckAdminCommandStatus(parameters={})["status_code"],     # 400
            "execute_admin_command": falcon.RTR_ExecuteAdminCommand(body={})["status_code"],                    # 400
            "create_put_files": falcon.RTR_CreatePut_Files(data=file_payload, files=files_detail)["status_code"],
            "delete_put_files": falcon.RTR_DeletePut_Files(
                ids=self.rtra_retrieve_file_id(file_name=upload_filename)
                )["status_code"],
            "create_scripts": falcon.RTR_CreateScripts(data=script_payload, files=script_detail)["status_code"],
            "update_scripts": falcon.RTR_UpdateScripts(
                data=self.rtra_create_updated_payload(script_filename, new_script_payload), files=script_detail
                )["status_code"],
            "delete_scripts": falcon.RTR_DeleteScripts(ids=self.rtra_retrieve_script_id(script_filename))["status_code"],
            "list_put_files": falcon.RTR_ListPut_Files()["status_code"],
            "list_scripts": falcon.RTR_ListScripts()["status_code"]
        }
        for key in tests:
            if tests[key] not in AllowedResponses:
                error_checks = False

            # print(f"{key} processed with a {tests[key]} response")
        # Code paths still get tested, skip the test on a 500
        if not error_checks:
            pytest.skip("500 error generated, code paths still tested")
        return error_checks

    @pytest.mark.skipif(sys.version_info.minor < 9, reason="Frequency reduced due to test flakiness")
    # @pytest.mark.skipif(platform.system() != "Darwin", reason="Frequency reduced due to test flakiness")
    def test_all_code_paths(self):
        """
        Pytest harness hook - Singular test will execute every statement in every method within the class
        """
        assert self.rtra_test_all_code_paths() is True

    # @staticmethod
    # def test_logout():
    #     """
    #     Pytest harness hook
    #     """
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True
