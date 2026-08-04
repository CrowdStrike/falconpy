"""Type stubs for incidents."""
from typing import Dict, List, Optional, Union
from typing_extensions import deprecated
from ._service_class import ServiceClass
from ._result import Result


class Incidents(ServiceClass):

    @deprecated("This operation is no longer available in CrowdStrike's API. Calling this method will result in an error from the API.")
    def crowdscore(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This operation is no longer available in CrowdStrike's API. Calling this method will result in an error from the API.")
    def get_behaviors(
        self,
        *,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def perform_incident_action(
        self,
        *,
        update_detects: Optional[bool] = None,
        overwrite_detects: Optional[bool] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This operation is no longer available in CrowdStrike's API. Calling this method will result in an error from the API.")
    def get_incidents(
        self,
        *,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This operation is no longer available in CrowdStrike's API. Calling this method will result in an error from the API.")
    def query_behaviors(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This operation is no longer available in CrowdStrike's API. Calling this method will result in an error from the API.")
    def query_incidents(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    CrowdScore = crowdscore
    GetBehaviors = get_behaviors
    PerformIncidentAction = perform_incident_action
    GetIncidents = get_incidents
    QueryBehaviors = query_behaviors
    QueryIncidents = query_incidents
