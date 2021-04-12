"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

iocs - CrowdStrike Falcon Real Time Response Administration API interface class

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


class Real_Time_Response_Admin(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def BatchAdminCmd(self: object, body: dict, parameters: dict = None) -> dict:
        """ Batch executes a RTR administrator command across the hosts mapped to the given batch ID. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/BatchAdminCmd
        FULL_URL = self.base_url+'/real-time-response/combined/batch-admin-command/v1'
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

    def RTR_CheckAdminCommandStatus(self: object, parameters: dict) -> dict:
        """ Get status of an executed RTR administrator command on a single host. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /real-time-response-admin/RTR_CheckAdminCommandStatus
        FULL_URL = self.base_url+'/real-time-response/entities/admin-command/v1'
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

    def RTR_ExecuteAdminCommand(self: object, body: dict) -> dict:
        """ Execute a RTR administrator command on a single host. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /real-time-response-admin/RTR_ExecuteAdminCommand
        FULL_URL = self.base_url+'/real-time-response/entities/admin-command/v1'
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

    def RTR_GetPut_Files(self: object, ids) -> dict:
        """ Get put-files based on the ID's given. These are used for the RTR `put` command. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_GetPut_Files
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/real-time-response/entities/put-files/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_CreatePut_Files(self: object, data, files) -> dict:
        """ Upload a new put-file to use for the RTR `put` command. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_CreatePut_Files
        FULL_URL = self.base_url+'/real-time-response/entities/put-files/v1'
        HEADERS = self.headers
        HEADERS['Content-Type'] = 'multipart/form-data'
        DATA = data
        FILES = files
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   data=DATA,
                                   files=FILES,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_DeletePut_Files(self: object, ids) -> dict:
        """ Delete a put-file based on the ID given. Can only delete one file at a time. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_DeletePut_Files
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/real-time-response/entities/put-files/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_GetScripts(self: object, ids) -> dict:
        """ Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_GetScripts
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/real-time-response/entities/scripts/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_CreateScripts(self: object, data, files) -> dict:
        """ Upload a new custom-script to use for the RTR `runscript` command. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_CreateScripts
        FULL_URL = self.base_url+'/real-time-response/entities/scripts/v1'
        HEADERS = self.headers
        HEADERS['Content-Type'] = 'multipart/form-data'
        DATA = data
        FILES = files
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   data=DATA,
                                   files=FILES,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_DeleteScripts(self: object, ids) -> dict:
        """ Delete a custom-script based on the ID given. Can only delete one script at a time. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_DeleteScripts
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/real-time-response/entities/scripts/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_UpdateScripts(self: object, data, files) -> dict:
        """ Upload a new scripts to replace an existing one. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_UpdateScripts
        FULL_URL = self.base_url+'/real-time-response/entities/scripts/v1'
        HEADERS = self.headers
        HEADERS['Content-Type'] = 'multipart/form-data'
        DATA = data
        FILES = files
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   data=DATA,
                                   files=FILES,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def RTR_ListPut_Files(self: object, parameters: dict = None) -> dict:
        """ Get a list of put-file ID's that are available to the user for the `put` command. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_ListPut_Files
        FULL_URL = self.base_url+'/real-time-response/queries/put-files/v1'
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

    def RTR_ListScripts(self: object, parameters: dict = None) -> dict:
        """ Get a list of custom-script ID's that are available to the user for the `runscript` command. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_ListScripts
        FULL_URL = self.base_url+'/real-time-response/queries/scripts/v1'
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
