# test_real_time_response.py
# This class tests the real_time_response service class

import os
import pytest
import sys
import platform
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# flake8: noqa: E402
from falconpy import RealTimeResponse
from falconpy import Hosts

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = RealTimeResponse(auth_object=config)
# Testing direct credential specification here - jshcodes 08.14.21
falcon_hosts = Hosts(client_id=auth.config["falcon_client_id"],
    client_secret=auth.config["falcon_client_secret"],
    base_url=auth.config["falcon_base_url"]
    )
AllowedResponses = [200, 204, 400, 404, 429]  # Adding rate-limiting as an allowed response for now


class TestRTR:

    def rtr_list_all_sessions(self):
        if falcon.RTR_ListAllSessions(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def rtr_session_tester(self):
        returned = False
        # This will have to be periodically updated using this solution, but for now it provides the necessary code coverage.
        # Highly dependant upon my test CID / API keys
        aid_lookup = falcon_hosts.QueryDevicesByFilter(filter="hostname:'falconpy-unit-testing'")
        try:
            if aid_lookup["body"]["resources"]:
                aid_to_check = aid_lookup["body"]["resources"][0]
            else:
                aid_to_check = "1234567890"
                # pytest.skip("Race condition met, skipping.")
        except KeyError:
            aid_to_check = "1234567890"
            # pytest.skip("Race condition met, skipping.")

        if aid_to_check:
            result = falcon.batch_init_sessions(host_ids=aid_to_check)
            if "resources" in result["body"]:
                if result["body"]["resources"]:
                    session_id = result["body"]["resources"][aid_to_check]["session_id"]
                    batch_id = result["body"].get("combined")
                    falcon.batch_get_command(batch_id=batch_id, file_path="/tmp/testfile.txt")
                    if falcon.RTR_DeleteSession(session_id=session_id)["status_code"] in AllowedResponses:
                        returned = True
                    else:
                        returned = False
                else:
                    # Fine if get a session back
                    returned = True
            else:
                pytest.skip("API communication failure")
                
        return returned

    def rtr_test_all_paths_with_errors(self):
        falcon.base_url = "nowhere"
        error_checks = True
        # "base_command": "string",
        # "batch_id": "string",
        # "command_string": "string",
        # "optional_hosts": [
        #     "string"
        # ],
        # "file_path": "string",
        # "persist_all": true,
        # "existing_batch_id": "string",
        # "host_ids": [
        #     "string"
        # ],
        # "queue_offline": true,
        # "hosts_to_remove": [
        #     "string"
        # ]
        # "device_id": "string",
        # "id": integer,
        # "persist": boolean,
        # "session_id": "string",
        # "origin": "string"
        commands = [
            ["RTR_AggregateSessions", falcon.aggregate_sessions()],
            ["BatchActiveResponderCmd", falcon.batch_active_responder_command(body={})],
            ["BatchCmd", falcon.batch_command(batch_id="12345678",
                                              optional_hosts=["12345678"],
                                              persist_all=True,
                                              queue_offline=True
                                              )],
            ["BatchGetCmdStatus", falcon.batch_get_command_status(parameters={})],
            ["BatchGetCmd", falcon.batch_get_command(file_path="whatevers")],
            ["BatchInitSessions", falcon.batch_init_sessions(existing_batch_id="12345678",
                                                             host_ids="12345678")],
            ["BatchRefreshSessions", falcon.batch_refresh_sessions(body={})],
            ["RTR_CheckActiveResponderCommandStatus", falcon.check_active_responder_command_status(parameters={})],
            ["RTR_ExecuteActiveResponderCommand", falcon.execute_active_responder_command(base_command="ls",
                                                                                          command_string="ls",
                                                                                          device_id="12345678",
                                                                                          persist=True,
                                                                                          id=0
                                                                                          )],
            ["RTR_CheckCommandStatus", falcon.check_command_status(parameters={})],
            ["RTR_ExecuteCommand", falcon.execute_command()],
            ["RTR_GetExtractedFileContents", falcon.get_extracted_file_contents(parameters={})],
            ["RTR_ListFiles", falcon.list_files(parameters={})],
            ["RTR_ListFilesV2", falcon.list_files_v2(parameters={})],
            ["RTR_DeleteFile", falcon.delete_file(ids='12345678', parameters={})],
            ["RTR_DeleteFileV2", falcon.delete_file_v2(ids='12345678', parameters={})],
            ["RTR_ListQueuedSessions", falcon.list_queued_sessions(body={})],
            ["RTR_DeleteQueuedSession", falcon.delete_queued_session(parameters={})],
            ["RTR_PulseSession", falcon.pulse_session(hosts_to_remove="BobJustBecause,AndLarry",
                                                      origin="Somewheres",
                                                      session_id="12345678"
                                                      )],
            ["RTR_ListSessions", falcon.list_sessions(body={})],
            ["RTR_InitSession", falcon.init_session(body={})],
            ["RTR_DeleteSession", falcon.delete_session(parameters={})],
            ["RTR_ListAllSessions", falcon.list_all_sessions()]
        ]
        for cmd in commands:
            if cmd[1]["status_code"] != 500:
                error_checks = False

        return error_checks

    def test_rtr_list_all_sessions(self):
        assert self.rtr_list_all_sessions() is True

    @pytest.mark.skipif(sys.version_info.minor < 10 and platform.system() != "Darwin", reason="Frequency reduced due to potential race condition")
    def test_rtr_session_connect(self):
        assert self.rtr_session_tester() is True

    def test_all_code_paths_with_five_hundreds(self):
        assert self.rtr_test_all_paths_with_errors() is True