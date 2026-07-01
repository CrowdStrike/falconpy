"""Type stubs for real_time_response_admin."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class RealTimeResponseAdmin(ServiceClass):

    def batch_admin_command(
        self,
        *,
        timeout: Optional[int] = None,
        timeout_duration: Optional[str] = None,
        host_timeout_duration: Optional[str] = None,
        base_command: Optional[str] = None,
        batch_id: Optional[str] = None,
        command_string: Optional[str] = None,
        optional_hosts: Optional[Union[str, List[str]]] = None,
        persist_all: Optional[bool] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def check_admin_command_status(
        self,
        *args: Union[str, List[str]],
        cloud_request_id: Optional[str] = None,
        sequence_id: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_admin_command(
        self,
        *,
        base_command: Optional[str] = None,
        command_string: Optional[str] = None,
        device_id: Optional[str] = None,
        id: Optional[int] = None,
        persist: Optional[bool] = None,
        session_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_falcon_scripts(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_put_file_contents(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_put_files(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_put_files_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_put_files(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_put_files(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_put_files_v2(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scripts(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scripts_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_scripts(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_scripts(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_scripts_v2(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_scripts_v2(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_scripts(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_falcon_scripts(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_put_files(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_scripts(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

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
