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
from ._util import parse_id_list, service_request
from ._service_class import ServiceClass


class Real_Time_Response(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def RTR_AggregateSessions(self: object, body: dict) -> dict:
        """ Get aggregates on session data. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_AggregateSessions
        FULL_URL = self.base_url+'/real-time-response/aggregates/sessions/GET/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def BatchActiveResponderCmd(self: object, body: dict, parameters: dict = None) -> dict:
        """ Batch executes a RTR active-responder command across the hosts mapped to the given batch ID. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        FULL_URL = self.base_url+'/real-time-response/combined/batch-active-responder-command/v1'
        HEADERS = self.headers
        BODY = body
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def BatchCmd(self: object, body: dict, parameters: dict = None) -> dict:
        """ Batch executes a RTR read-only command across the hosts mapped to the given batch ID. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        FULL_URL = self.base_url+'/real-time-response/combined/batch-command/v1'
        HEADERS = self.headers
        BODY = body
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def BatchGetCmdStatus(self: object, parameters: dict) -> dict:
        """ Retrieves the status of the specified batch get command.
            Will return successful files when they are finished processing.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchGetCmdStatus
        FULL_URL = self.base_url+'/real-time-response/combined/batch-get-command/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def BatchGetCmd(self: object, body: dict, parameters: dict = None) -> dict:
        """ Batch executes `get` command across hosts to retrieve files.
            After this call is made `/real-time-response/combined/get-command-status/v1` is used to query for the results.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchActiveResponderCmd
        FULL_URL = self.base_url+'/real-time-response/combined/batch-get-command/v1'
        HEADERS = self.headers
        BODY = body
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def BatchInitSessions(self: object, body: dict, parameters: dict = None) -> dict:
        """ Batch initialize a RTR session on multiple hosts.
            Before any RTR commands can be used, an active session is needed on the host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchInitSessions
        FULL_URL = self.base_url+'/real-time-response/combined/batch-init-session/v1'
        HEADERS = self.headers
        BODY = body
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def BatchRefreshSessions(self: object, body: dict, parameters: dict = None) -> dict:
        """ Batch refresh a RTR session on multiple hosts. RTR sessions will expire after 10 minutes unless refreshed. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchRefreshSessions
        FULL_URL = self.base_url+'/real-time-response/combined/batch-refresh-session/v1'
        HEADERS = self.headers
        BODY = body
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_CheckActiveResponderCommandStatus(self: object, parameters: dict) -> dict:
        """ Get status of an executed active-responder command on a single host. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /real-time-response/RTR_CheckActiveResponderCommandStatus
        FULL_URL = self.base_url+'/real-time-response/entities/active-responder-command/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_ExecuteActiveResponderCommand(self: object, body: dict) -> dict:
        """ Execute an active responder command on a single host. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/BatchRefreshSessions
        FULL_URL = self.base_url+'/real-time-response/entities/active-responder-command/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_CheckCommandStatus(self: object, parameters: dict) -> dict:
        """ Get status of an executed command on a single host. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_CheckCommandStatus
        FULL_URL = self.base_url+'/real-time-response/entities/command/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_ExecuteCommand(self: object, body: dict) -> dict:
        """ Execute a command on a single host. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ExecuteCommand
        FULL_URL = self.base_url+'/real-time-response/entities/command/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_GetExtractedFileContents(self: object, parameters: dict) -> dict:
        """ Get RTR extracted file contents for specified session and sha256. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_GetExtractedFileContents
        FULL_URL = self.base_url+'/real-time-response/entities/extracted-file-contents/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_ListFiles(self: object, parameters: dict) -> dict:
        """ Get a list of files for the specified RTR session. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListFiles
        FULL_URL = self.base_url+'/real-time-response/entities/file/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_DeleteFile(self: object, ids, parameters: dict) -> dict:
        """ Delete a RTR session file. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteFile
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/real-time-response/entities/file/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_PulseSession(self: object, body: dict) -> dict:
        """ Refresh a session timeout on a single host. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_PulseSession
        FULL_URL = self.base_url+'/real-time-response/entities/refresh-session/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_ListSessions(self: object, body: dict) -> dict:
        """ Get session metadata by session id. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListSessions
        FULL_URL = self.base_url+'/real-time-response/entities/sessions/GET/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_ListQueuedSessions(self: object, body: dict) -> dict:
        """ Get session metadata by session id. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListSessions
        FULL_URL = self.base_url+'/real-time-response/entities/queued-sessions/GET/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_InitSession(self: object, body: dict) -> dict:
        """ Initialize a new session with the RTR cloud. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/InitSessionMixin0
        FULL_URL = self.base_url+'/real-time-response/entities/sessions/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_DeleteSession(self: object, parameters: dict) -> dict:
        """ Delete a session. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteSession
        FULL_URL = self.base_url+'/real-time-response/entities/sessions/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_DeleteQueuedSession(self: object, parameters: dict) -> dict:
        """ Delete a queued session. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_DeleteSession
        FULL_URL = self.base_url+'/real-time-response/entities/queued-sessions/command/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_ListAllSessions(self: object, parameters: dict = None) -> dict:
        """ Get a list of session_ids. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response/RTR_ListAllSessions
        FULL_URL = self.base_url+'/real-time-response/queries/sessions/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned
