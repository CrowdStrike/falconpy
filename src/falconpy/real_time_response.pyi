"""Type stubs for real_time_response."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class RealTimeResponse(ServiceClass):

    def aggregate_sessions(
        self,
        *,
        date_ranges: Optional[list] = None,
        exclude: Optional[str] = None,
        extended_bounds: Optional[dict] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        filters_spec: Optional[dict] = None,
        include: Optional[str] = None,
        interval: Optional[str] = None,
        max_doc_count: Optional[int] = None,
        min_doc_count: Optional[int] = None,
        missing: Optional[str] = None,
        name: Optional[str] = None,
        percents: Optional[list] = None,
        q: Optional[str] = None,
        ranges: Optional[list] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        sub_aggregates: Optional[list] = None,
        time_zone: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[list] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def batch_active_responder_command(
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

    def batch_command(
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

    def batch_get_command_status(
        self,
        *args: Union[str, List[str]],
        timeout: Optional[int] = None,
        timeout_duration: Optional[str] = None,
        batch_get_cmd_req_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def batch_get_command(
        self,
        *,
        timeout: Optional[int] = None,
        timeout_duration: Optional[str] = None,
        host_timeout_duration: Optional[str] = None,
        batch_id: Optional[str] = None,
        file_path: Optional[str] = None,
        optional_hosts: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def batch_init_sessions(
        self,
        *,
        timeout: Optional[int] = None,
        timeout_duration: Optional[str] = None,
        host_timeout_duration: Optional[str] = None,
        existing_batch_id: Optional[str] = None,
        host_ids: Optional[Union[str, List[str]]] = None,
        queue_offline: Optional[bool] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def batch_refresh_sessions(
        self,
        *,
        timeout: Optional[int] = None,
        timeout_duration: Optional[str] = None,
        batch_id: Optional[str] = None,
        hosts_to_remove: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def check_active_responder_command_status(
        self,
        *args: Union[str, List[str]],
        cloud_request_id: Optional[str] = None,
        sequence_id: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_active_responder_command(
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

    def check_command_status(
        self,
        *args: Union[str, List[str]],
        cloud_request_id: Optional[str] = None,
        sequence_id: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def execute_command(
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

    def get_extracted_file_contents(
        self,
        *,
        session_id: Optional[str] = None,
        sha256: Optional[str] = None,
        filename: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_files(
        self,
        *args: Union[str, List[str]],
        session_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_files_v2(
        self,
        *args: Union[str, List[str]],
        session_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_file(
        self,
        *,
        ids: Optional[str] = None,
        session_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_file_v2(
        self,
        *,
        ids: Optional[str] = None,
        session_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def pulse_session(
        self,
        *,
        device_id: Optional[str] = None,
        origin: Optional[str] = None,
        queue_offline: Optional[bool] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_sessions(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_queued_sessions(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def init_session(
        self,
        *,
        timeout: Optional[int] = None,
        timeout_duration: Optional[str] = None,
        device_id: Optional[str] = None,
        origin: Optional[str] = None,
        queue_offline: Optional[bool] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_session(
        self,
        *args: Union[str, List[str]],
        session_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_queued_session(
        self,
        *,
        session_id: Optional[str] = None,
        cloud_request_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_all_sessions(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

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
    RTR_ListFilesV2 = list_files_v2
    RTR_DeleteFile = delete_file
    RTR_DeleteFileV2 = delete_file_v2
    RTR_ListQueuedSessions = list_queued_sessions
    RTR_DeleteQueuedSession = delete_queued_session
    RTR_PulseSession = pulse_session
    RTR_ListSessions = list_sessions
    RTR_InitSession = init_session
    RTR_DeleteSession = delete_session
    RTR_ListAllSessions = list_all_sessions
