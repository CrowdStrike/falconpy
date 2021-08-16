"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

real_time_response_admin - CrowdStrike Falcon Real Time Response Administration API interface class

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
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._real_time_response_admin import _real_time_response_admin_endpoints as Endpoints


class RealTimeResponseAdmin(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def batch_admin_command(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Batch executes a RTR administrator command across the hosts mapped to the given batch ID.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/BatchAdminCmd
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BatchAdminCmd",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def check_admin_command_status(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get status of an executed RTR administrator command on a single host.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /real-time-response-admin/RTR_CheckAdminCommandStatus
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CheckAdminCommandStatus",
            keywords=kwargs,
            params=parameters
            )

    def execute_admin_command(self: object, body: dict) -> dict:
        """
        Execute a RTR administrator command on a single host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /real-time-response-admin/RTR_ExecuteAdminCommand
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ExecuteAdminCommand",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_put_files(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get put-files based on the ID's given. These are used for the RTR `put` command.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_GetPut_Files
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_GetPut_Files",
            keywords=kwargs,
            params=parameters
            )

    def create_put_files(self: object, data: dict, files: list) -> dict:
        """
        Upload a new put-file to use for the RTR `put` command.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_CreatePut_Files
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CreatePut_Files",
            data=data,
            files=files
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_put_files(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a put-file based on the ID given. Can only delete one file at a time.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_DeletePut_Files
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeletePut_Files",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scripts(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_GetScripts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_GetScripts",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["files"], default_types=["list"])
    def create_scripts(self: object, data, files: list = None) -> dict:
        """
        Upload a new custom-script to use for the RTR `runscript` command.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_CreateScripts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_CreateScripts",
            data=data,
            files=files
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_scripts(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a custom-script based on the ID given. Can only delete one script at a time.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_DeleteScripts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_DeleteScripts",
            keywords=kwargs,
            params=parameters
            )

    def update_scripts(self: object, data, files) -> dict:
        """
        Upload a new scripts to replace an existing one.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_UpdateScripts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_UpdateScripts",
            data=data,
            files=files
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_put_files(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get a list of put-file ID's that are available to the user for the `put` command.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_ListPut_Files
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RTR_ListPut_Files",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_scripts(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get a list of custom-script ID's that are available to the user for the `runscript` command.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin/RTR_ListScripts
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
    RTR_GetPut_Files = get_put_files
    RTR_CreatePut_Files = create_put_files
    RTR_DeletePut_Files = delete_put_files
    RTR_GetScripts = get_scripts
    RTR_CreateScripts = create_scripts
    RTR_DeleteScripts = delete_scripts
    RTR_UpdateScripts = update_scripts
    RTR_ListPut_Files = list_put_files
    RTR_ListScripts = list_scripts


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Real_Time_Response_Admin = RealTimeResponseAdmin  # pylint: disable=C0103
