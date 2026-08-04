"""CrowdStrike Falcon Real Time Response Administration API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

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
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import command_payload, data_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._real_time_response_admin import _real_time_response_admin_endpoints as Endpoints


class RealTimeResponseAdmin(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def batch_admin_command(self: object,
                            body: dict = None,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Batch executes a RTR administrator command across the hosts mapped to a given batch ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/BatchAdminCmd

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if keywords are used.
                {
                    "base_command": "string",
                    "batch_id": "string",
                    "command_string": "string",
                    "optional_hosts": [
                        "string"
                    ],
                    "persist_all": true
                }
        base_command : str
            Active-Responder command type we are going to execute,
            for example: `get` or `cp`.  String.
            Refer to the RTR documentation for the full list of commands.
        batch_id : str
            Batch ID to execute the command on. Received from batch_init_session.
        command_string : str
            Full command string for the command. For example `get some_file.txt`.
        host_timeout_duration : str
            Timeout duration for how long a host has time to complete processing.
            Default value is slightly less than the overall timeout value.
            This value cannot be greater than the overall request timeout. Max < 10 minutes.
            Example: 10s  Valid units: ns, us, ms, s, m, h
        optional_hosts : str or list[str]
            List of a subset of hosts we want to run the command on.
            If this list is supplied, only these hosts will receive the command.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        persist_all : bool
        timeout : int
            Timeout for how long to wait for the request in seconds.
            Default timeout: 30 seconds  Max timeout: 10 minutes
        timeout_duration : str
            Timeout duration for how long to wait for the request in duration
            syntax. Example: `10s`.   Default value: `30s`. Maximum is `10m`.
            Valid units: `ns`, `us`, `ms`, `s`, `m`, `h`

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = command_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchAdminCmd",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def check_admin_command_status(self: object,
                                   *args,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get status of an executed RTR administrator command on a single host.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /real-time-response-admin/RTR_CheckAdminCommandStatus

        Keyword arguments
        -----------------
        cloud_request_id : str
            Cloud Request ID of the executed command to query.
        sequence_id : int
            Sequence ID that we want to retrieve. Command responses are
            chunked across sequences. Default value: 0
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'cloud_request_id'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not kwargs.get("sequence_id", None) and not parameters.get("sequence_id", None):
            parameters["sequence_id"] = 0

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CheckAdminCommandStatus",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cloud_request_id")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def execute_admin_command(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute a RTR administrator command on a single host.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /real-time-response-admin/RTR_ExecuteAdminCommand

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if keywords are used.
                {
                    "base_command": "string",
                    "command_string": "string",
                    "device_id": "string",
                    "id": integer,
                    "persist": boolean,
                    "session_id": "string"
                }
        base_command : str
            Active-Responder command type we are going to execute,
            for example: `get` or `cp`.  String.
            Refer to the RTR documentation for the full list of commands.
        command_string : str
            Full command string for the command. For example `get some_file.txt`.
        device_id : str
            ID of the device to execute the command on.
        id : int
            Command sequence.
        persist : bool
            Execute this command when host returns to service.
        session_id : str
            RTR session ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = command_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ExecuteAdminCommand",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_falcon_scripts(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Falcon scripts with metadata and content of script.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_GetFalconScripts

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of Falcon Script IDs to retrieve.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_GetFalconScripts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_put_file_contents(self: object,
                              *args,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get put-file contents for a given put file ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-GetPutFileContents

        Keyword arguments
        -----------------
        id : str
            Put file ID to retrieve.
        parameters : dict
            full parameters payload, not required if id is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_GetPutFileContents",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_put_files(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get put-files based on the ID's given. These are used for the RTR `put` command.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_GetPut_Files

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of File IDs to retrieve.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_GetPut_Files",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_put_files_v2(self: object,
                         *args,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get put-files based on the ID's given. These are used for the RTR `put` command.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-GetPut-FilesV2

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of File IDs to retrieve.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_GetPut_FilesV2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["data"], default_types=["dict"])
    def create_put_files(self: object,
                         files: list,
                         data: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload a new put-file to use for the RTR `put` command.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-CreatePut-Files

        Keyword arguments
        -----------------
        data : str
            full formData payload, not required if other keywords are used.
            {
                "description": "string",
                "name": "string",
                "comments_for_audit_log": "string"
            }
        files : str
            File to be uploaded. List of tuples. *REQUIRED*
            Ex: [('file', ('file.ext', open('file.ext','rb').read(), 'application/script'))]
        description : str
            File description.
        name : str
            File name (if different than actual file name)
        comments_for_audit_log : str
            Audit log comment.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not data:
            data = data_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CreatePut_Files",
            data=data,
            files=files
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_put_files(self: object,
                         *args,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a put-file based on the ID given. Can only delete one file at a time.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_DeletePut_Files

        Keyword arguments
        -----------------
        ids : str
            File ID to delete. String. Only one file can be deleted per request.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeletePut_Files",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["data", "files"], default_types=["dict", "list"])
    def create_put_files_v2(self: object,
                            files: list,
                            data: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload a new put-file to use for the RTR `put` command.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-CreatePut-FilesV2

        Keyword arguments
        -----------------
        data : str
            full formData payload, not required if other keywords are used. formData.
            {
                "description": "string",
                "name": "string",
                "comments_for_audit_log": "string"
            }
        files : str
            File to be uploaded. List of tuples. *REQUIRED*
            Ex: [('file', ('file.ext', open('file.ext','rb').read(), 'application/script'))]
        description : str
            File description.
        name : str
            File name (if different than actual file name)
        comments_for_audit_log : str
            Audit log comment.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not data:
            data = data_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CreatePut_FilesV2",
            data=data,
            files=files
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scripts(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get custom-scripts based on the ID's given.

        These are used for the RTR `runscript` command.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-GetScripts

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of Script IDs to retrieve.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_GetScripts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scripts_v2(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get custom-scripts based on the ID's given.

        These are used for the RTR `runscript` command.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-GetScriptsV2

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of Script IDs to retrieve.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_GetScriptsV2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["data", "files"], default_types=["dict", "list"])
    def create_scripts(self: object,
                       data: dict = None,
                       files: list = None,
                       **kwargs
                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload a new custom-script to use for the RTR `runscript` command.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-CreateScripts

        Keyword arguments
        -----------------
        data : str
            full formData payload, not required if other keywords are used.
            {
                "description": "string",
                "name": "string",
                "comments_for_audit_log": "string",
                "content": "string",
                "platform": "string",
                "permission_type": "string"
            }
        files : str
            File to be uploaded. List of tuples. *REQUIRED*
            Ex: [('file', ('file.ext', open('file.ext','rb').read(), 'application/script'))]
        description : str
            File description.
        name : str
            File name (if different than actual file name)
        comments_for_audit_log : str
            Audit log comment.
        permission_type : str
            Permission for the custom-script.
            Valid permission values:
              `private` - usable by only the user who uploaded it
              `group` - usable by all RTR Admins
              `public` - usable by all active-responders and RTR admins
        content : str
            The script text that you want to use to upload.
        platform : str
            Platforms for the file. Currently supports: windows, mac, linux.
            If no platform is provided, it will default to 'windows'.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not data:
            data = data_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CreateScripts",
            data=data,
            files=files
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_scripts(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a custom-script based on the ID given. Can only delete one script at a time.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_DeleteScripts

        Keyword arguments
        -----------------
        ids : str
            Script ID to delete. String. Only one file can be deleted per request.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeleteScripts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["data", "files"], default_types=["dict", "list"])
    def create_scripts_v2(self: object,
                          data: dict = None,
                          files: list = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload a new custom-script to use for the RTR `runscript` command.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-CreateScriptsV2

        Keyword arguments
        -----------------
        data : str
            full formData payload, not required if other keywords are used. formData.
            {
                "description": "string",
                "name": "string",
                "comments_for_audit_log": "string",
                "content": "string",
                "platform": "string",
                "permission_type": "string"
            }
        files : str
            File to be uploaded. List of tuples. *REQUIRED*
            Ex: [('file', ('file.ext', open('file.ext','rb').read(), 'application/script'))]
        description : str
            File description.
        name : str
            File name (if different than actual file name)
        comments_for_audit_log : str
            Audit log comment.
        permission_type : str
            Permission for the custom-script. STring.
            Valid permission values:
              `private` - usable by only the user who uploaded it
              `group` - usable by all RTR Admins
              `public` - usable by all active-responders and RTR admins
        content : str
            The script text that you want to use to upload.
        platform : str
            Platforms for the file. Currently supports: windows, mac, linux. String.
            If no platform is provided, it will default to 'windows'.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not data:
            data = data_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CreateScriptsV2",
            data=data,
            files=files
            )

    @force_default(defaults=["data", "files"], default_types=["dict", "list"])
    def update_scripts_v2(self: object,
                          data: dict = None,
                          files: list = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload a new scripts to replace an existing one.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-UpdateScriptsV2

        Keyword arguments
        -----------------
        data : str
            full formData payload, not required if other keywords are used. formData.
            {
                "id": "string",
                "description": "string",
                "name": "string",
                "comments_for_audit_log": "string",
                "content": "string",
                "platform": "string",
                "permission_type": "string"
            }
        files : str
            File to be uploaded. List of tuples. *REQUIRED*
            Ex: [('file', ('file.ext', open('file.ext','rb').read(), 'application/script'))]
        description : str
            File description.
        id : str
            Script ID to be updated.
        name : str
            File name (if different than actual file name)
        comments_for_audit_log : str
            Audit log comment.
        permission_type : str
            Permission for the custom-script. String.
            Valid permission values:
              `private` - usable by only the user who uploaded it
              `group` - usable by all RTR Admins
              `public` - usable by all active-responders and RTR admins
        content : str
            The script text that you want to use to upload.
        platform : str
            Platforms for the file. Currently supports: windows, mac, linux. String.
            If no platform is provided, it will default to 'windows'.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not data:
            data = data_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_UpdateScriptsV2",
            data=data,
            files=files
            )

    @force_default(defaults=["data", "files"], default_types=["dict", "list"])
    def update_scripts(self: object,
                       data: dict = None,
                       files: list = None,
                       **kwargs
                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload a new scripts to replace an existing one.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-UpdateScripts

        Keyword arguments
        -----------------
        data : str
            full formData payload, not required if other keywords are used.
            {
                "id": "string",
                "description": "string",
                "name": "string",
                "comments_for_audit_log": "string",
                "content": "string",
                "platform": "string",
                "permission_type": "string"
            }
        files : str
            File to be uploaded. List of tuples. *REQUIRED*
            Ex: [('file', ('file.ext', open('file.ext','rb').read(), 'application/script'))]
        description : str
            File description.
        id : str
            Script ID to be updated.
        name : str
            File name (if different than actual file name)
        comments_for_audit_log : str
            Audit log comment.
        permission_type : str
            Permission for the custom-script.
            Valid permission values:
              `private` - usable by only the user who uploaded it
              `group` - usable by all RTR Admins
              `public` - usable by all active-responders and RTR admins
        content : str
            The script text that you want to use to upload.
        platform : str
            Platforms for the file. Currently supports: windows, mac, linux.
            If no platform is provided, it will default to 'windows'.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not data:
            data = data_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_UpdateScripts",
            data=data,
            files=files
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_falcon_scripts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of Falcon script IDs available to the user to run.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_ListFalconScripts

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        limit : int
            The maximum number of IDs to return in this response. [Integer, 1-5000]
            Use with the offset parameter to manage pagination of results.
        offset : int
            The offset to start retrieving IDs from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. Ex: `created_at|asc`

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListFalconScripts",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_put_files(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of put-file ID's that are available to the user for the `put` command.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-ListPut-Files

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-5000]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. Ex: `created_at|desc`

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListPut_Files",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_scripts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of custom-script ID's that are available for the `runscript` command.

        Only displays scripts the user has permissions to access.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR-ListScripts

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-5000]
            Use with the offset parameter to manage pagination of results.
        offset : str
            The offset to start retrieving records from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. Ex: `created_at|desc`

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListScripts",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    BatchAdminCmd = batch_admin_command
    RTR_CheckAdminCommandStatus = check_admin_command_status
    RTR_ExecuteAdminCommand = execute_admin_command
    RTR_GetFalconScripts = get_falcon_scripts
    RTR_GetPutFileContents = get_put_file_contents
    RTR_GetPut_Files = get_put_files
    RTR_GetPut_FilesV2 = get_put_files_v2
    RTR_CreatePut_Files = create_put_files
    RTR_DeletePut_Files = delete_put_files
    RTR_CreatePut_FilesV2 = create_put_files_v2
    RTR_GetScripts = get_scripts
    RTR_GetScriptsV2 = get_scripts_v2
    RTR_CreateScripts = create_scripts
    RTR_DeleteScripts = delete_scripts
    RTR_CreateScriptsV2 = create_scripts_v2
    RTR_UpdateScriptsV2 = update_scripts_v2
    RTR_UpdateScripts = update_scripts
    RTR_ListFalconScripts = list_falcon_scripts
    RTR_ListPut_Files = list_put_files
    RTR_ListScripts = list_scripts


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Real_Time_Response_Admin = RealTimeResponseAdmin  # pylint: disable=C0103
