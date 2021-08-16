"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

iocs - CrowdStrike Falcon Real Time Response API interface class

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
# pylint: disable=R0904  # Aligning method count to API service collection operation count
from ._util import force_default, process_service_request, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._real_time_response import _real_time_response_endpoints as Endpoints


class RealTimeResponse(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def aggregate_sessions(self: object, body: dict) -> dict:
        """
        Get aggregates on session data.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_AggregateSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_AggregateSessions",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def batch_active_responder_command(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch executes a RTR active-responder command across the hosts mapped to the given batch ID.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchActiveResponderCmd",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def batch_command(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch executes a RTR read-only command across the hosts mapped to the given batch ID.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchCmd",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def batch_get_command_status(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieves the status of the specified batch get command.
        Will return successful files when they are finished processing.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchGetCmdStatus
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchGetCmdStatus",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def batch_get_command(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch executes `get` command across hosts to retrieve files.
        After this call is made `/real-time-response/combined/get-command-status/v1` is used to query for the results.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchGetCmd",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def batch_init_sessions(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch initialize a RTR session on multiple hosts.
        Before any RTR commands can be used, an active session is needed on the host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchInitSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchInitSessions",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def batch_refresh_sessions(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch refresh a RTR session on multiple hosts. RTR sessions will expire after 10 minutes unless refreshed.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchRefreshSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchRefreshSessions",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def check_active_responder_command_status(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get status of an executed active-responder command on a single host.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /real-time-response/RTR_CheckActiveResponderCommandStatus
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CheckActiveResponderCommandStatus",
            keywords=kwargs,
            params=parameters
            )

    def execute_active_responder_command(self: object, body: dict) -> dict:
        """
        Execute an active responder command on a single host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchRefreshSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ExecuteActiveResponderCommand",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def check_command_status(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get status of an executed command on a single host.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_CheckCommandStatus
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CheckCommandStatus",
            keywords=kwargs,
            params=parameters
            )

    def execute_command(self: object, body: dict) -> dict:
        """
        Execute a command on a single host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ExecuteCommand
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ExecuteCommand",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_extracted_file_contents(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get RTR extracted file contents for specified session and sha256.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_GetExtractedFileContents
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_GetExtractedFileContents",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_files(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get a list of files for the specified RTR session.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListFiles
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListFiles",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "session_id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_file(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a RTR session file.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteFile
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeleteFile",
            keywords=kwargs,
            params=parameters
            )

    def pulse_session(self: object, body: dict) -> dict:
        """
        Refresh a session timeout on a single host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_PulseSession
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_PulseSession",
            body=body
            )

    def list_sessions(self: object, body: dict) -> dict:
        """
        Get session metadata by session id.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListSessions",
            body=body
            )

    def list_queued_sessions(self: object, body: dict) -> dict:
        """
        Get session metadata by session id.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListQueuedSessions",
            body=body
            )

    def init_session(self: object, body: dict) -> dict:
        """
        Initialize a new session with the RTR cloud.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/InitSessionMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_InitSession",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_session(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a session.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteSession
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeleteSession",

            keywords=kwargs,
            params=handle_single_argument(args, parameters, "session_id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_queued_session(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a queued session.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteSession
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeleteQueuedSession",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_all_sessions(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get a list of session_ids.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListAllSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListAllSessions",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    RTR_AggregateSessions = aggregate_sessions
    BatchActiveResponderCmd = batch_active_responder_command
    BatchCmd = batch_command
    BatchGetCmdStatus = batch_get_command_status
    BatchGetCmd = batch_get_command
    BatchInitSessions = batch_init_sessions
    BatchRefreshSessions = batch_refresh_sessions
    RTR_CheckActiveResponderCommandStatus = check_active_responder_command_status
    RTR_ExecuteActiveResponderCommand = execute_active_responder_command
    RTR_CheckCommandStatus = check_command_status
    RTR_ExecuteCommand = execute_command
    RTR_GetExtractedFileContents = get_extracted_file_contents
    RTR_ListFiles = list_files
    RTR_DeleteFile = delete_file
    RTR_ListQueuedSessions = list_queued_sessions
    RTR_DeleteQueuedSession = delete_queued_session
    RTR_PulseSession = pulse_session
    RTR_ListSessions = list_sessions
    RTR_InitSession = init_session
    RTR_DeleteSession = delete_session
    RTR_ListAllSessions = list_all_sessions


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Real_Time_Response = RealTimeResponse  # pylint: disable=C0103
