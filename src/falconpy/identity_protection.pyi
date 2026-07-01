"""Type stubs for identity_protection."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class IdentityProtection(ServiceClass):

    def graphql(
        self,
        *,
        query: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sensor_aggregates(
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

    def get_sensor_details(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_policy_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_policy_rule(
        self,
        *,
        action: Optional[str] = None,
        activity: Optional[dict] = None,
        destination: Optional[dict] = None,
        enabled: Optional[bool] = None,
        name: Optional[str] = None,
        simulationMode: Optional[bool] = None,
        sourceEndpoint: Optional[dict] = None,
        sourceUser: Optional[dict] = None,
        trigger: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_policy_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_sensors(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_policy_rules(
        self,
        *,
        enabled: Optional[bool] = None,
        simulation_mode: Optional[bool] = None,
        name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GraphQL = graphql
    api_preempt_proxy_post_graphql = graphql
    post_graphql = graphql
    post_policy_rules = create_policy_rule
    get_policy_rules_query = query_policy_rules
    GetSensorAggregates = get_sensor_aggregates
    GetSensorDetails = get_sensor_details
    QuerySensorsByFilter = query_sensors
    query_sensors_by_filter = query_sensors
