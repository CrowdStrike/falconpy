"""Type stubs for real_time_response_audit."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class RealTimeResponseAudit(ServiceClass):

    def audit_sessions(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        with_command_info: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    RTRAuditSessions = audit_sessions
