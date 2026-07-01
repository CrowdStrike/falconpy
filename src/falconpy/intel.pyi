"""Type stubs for intel."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Intel(ServiceClass):

    def query_actor_entities(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        fields: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_indicator_entities(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        include_relations: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_report_entities(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        fields: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_actor_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        fields: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_indicator_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_mitre_report(
        self,
        *,
        actor_id: Optional[str] = None,
        format: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def mitre_attacks(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_malware_report(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        format: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_malware_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_report_pdf(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_malware_entities(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        fields: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_report_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        fields: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule_file(
        self,
        *args: Union[str, List[str]],
        id: Optional[int] = None,
        format: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_latest_rule_file(
        self,
        *args: Union[str, List[str]],
        type: Optional[str] = None,
        format: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_actor_ids(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_indicator_ids(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        include_relations: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_mitre_attacks(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_mitre_attacks_for_malware(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_report_ids(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rule_ids(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        name: Optional[Union[str, List[str]]] = None,
        type: Optional[str] = None,
        description: Optional[Union[str, List[str]]] = None,
        tags: Optional[Union[str, List[str]]] = None,
        min_created_date: Optional[int] = None,
        max_created_date: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_malware(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_vulnerabilities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_vulnerabilities(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cao_incidents_aggregates_v1(
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
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cao_incidents_entities_v1(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cao_incidents_queries_v1(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    QueryIntelActorEntities = query_actor_entities
    QueryIntelIndicatorEntities = query_indicator_entities
    QueryIntelReportEntities = query_report_entities
    QueryVulnerabilities = query_vulnerabilities
    GetVulnerabilities = get_vulnerabilities
    GetIntelActorEntities = get_actor_entities
    GetIntelIndicatorEntities = get_indicator_entities
    GetMitreReport = get_mitre_report
    GetMalwareMitreReport = get_malware_report
    PostMitreAttacks = mitre_attacks
    GetMalwareEntities = get_malware_entities
    GetIntelReportPDF = get_report_pdf
    QueryMalwareEntities = query_malware_entities
    GetIntelReportEntities = get_report_entities
    GetIntelRuleFile = get_rule_file
    GetLatestIntelRuleFile = get_latest_rule_file
    GetIntelRuleEntities = get_rule_entities
    QueryMitreAttacks = query_mitre_attacks
    QueryMitreAttacksForMalware = query_mitre_attacks_for_malware
    QueryIntelActorIds = query_actor_ids
    QueryMalware = query_malware
    QueryIntelIndicatorIds = query_indicator_ids
    QueryIntelReportIds = query_report_ids
    QueryIntelRuleIds = query_rule_ids
