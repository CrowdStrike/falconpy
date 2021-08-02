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
# pylint: disable=C0103  # Aligning method names to API operation IDs
# pylint: disable=R0904  # Aligning method count to API service collection operation count
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._real_time_response import _real_time_response_endpoints as Endpoints


class Real_Time_Response(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def RTR_AggregateSessions(self: object, body: dict) -> dict:
        """
        Get aggregates on session data.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_AggregateSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_AggregateSessions",
            method="POST",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def BatchActiveResponderCmd(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch executes a RTR active-responder command across the hosts mapped to the given batch ID.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchActiveResponderCmd",
            method="POST",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def BatchCmd(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch executes a RTR read-only command across the hosts mapped to the given batch ID.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchCmd",
            method="POST",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def BatchGetCmdStatus(self: object, parameters: dict = None, **kwargs) -> dict:
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
    def BatchGetCmd(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch executes `get` command across hosts to retrieve files.
        After this call is made `/real-time-response/combined/get-command-status/v1` is used to query for the results.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchGetCmd",
            method="POST",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def BatchInitSessions(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch initialize a RTR session on multiple hosts.
        Before any RTR commands can be used, an active session is needed on the host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchInitSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchInitSessions",
            method="POST",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def BatchRefreshSessions(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch refresh a RTR session on multiple hosts. RTR sessions will expire after 10 minutes unless refreshed.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchRefreshSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchRefreshSessions",
            method="POST",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RTR_CheckActiveResponderCommandStatus(self: object, parameters: dict = None, **kwargs) -> dict:
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

    def RTR_ExecuteActiveResponderCommand(self: object, body: dict) -> dict:
        """
        Execute an active responder command on a single host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchRefreshSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ExecuteActiveResponderCommand",
            method="POST",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RTR_CheckCommandStatus(self: object, parameters: dict = None, **kwargs) -> dict:
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

    def RTR_ExecuteCommand(self: object, body: dict) -> dict:
        """
        Execute a command on a single host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ExecuteCommand
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ExecuteCommand",
            method="POST",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RTR_GetExtractedFileContents(self: object, parameters: dict = None, **kwargs) -> dict:
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
    def RTR_ListFiles(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get a list of files for the specified RTR session.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListFiles
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListFiles",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RTR_DeleteFile(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a RTR session file.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteFile
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeleteFile",
            method="DELETE",
            keywords=kwargs,
            params=parameters
            )

    def RTR_PulseSession(self: object, body: dict) -> dict:
        """
        Refresh a session timeout on a single host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_PulseSession
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_PulseSession",
            method="POST",
            body=body
            )

    def RTR_ListSessions(self: object, body: dict) -> dict:
        """
        Get session metadata by session id.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListSessions",
            method="POST",
            body=body
            )

    def RTR_ListQueuedSessions(self: object, body: dict) -> dict:
        """
        Get session metadata by session id.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListSessions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListQueuedSessions",
            method="POST",
            body=body
            )

    def RTR_InitSession(self: object, body: dict) -> dict:
        """
        Initialize a new session with the RTR cloud.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/InitSessionMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_InitSession",
            method="POST",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RTR_DeleteSession(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a session.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteSession
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeleteSession",
            method="DELETE",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RTR_DeleteQueuedSession(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a queued session.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteSession
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeleteQueuedSession",
            method="DELETE",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RTR_ListAllSessions(self: object, parameters: dict = None, **kwargs) -> dict:
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
