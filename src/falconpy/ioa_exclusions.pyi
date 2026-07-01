"""Type stubs for ioa_exclusions."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class IOAExclusions(ServiceClass):

    def get_ss_exclusion_aggregates(
        self,
        *,
        ifn_regex: Optional[str] = None,
        cl_regex: Optional[str] = None,
        parent_ifn_regex: Optional[str] = None,
        parent_cl_regex: Optional[str] = None,
        grandparent_ifn_regex: Optional[str] = None,
        grandparent_cl_regex: Optional[str] = None,
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
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_ss_exclusion_reports_v2(
        self,
        *,
        report_format: Optional[str] = None,
        search: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_ss_exclusion_rules_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_ss_exclusions(
        self,
        *,
        exclusions: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_ss_exclusions(
        self,
        *,
        exclusions: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_ss_exclusions(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_ss_exclusion_matched_rules(
        self,
        *,
        aid: Optional[str] = None,
        command_line: Optional[str] = None,
        grandparent_command_line: Optional[str] = None,
        grandparent_image_file_name: Optional[str] = None,
        image_file_name: Optional[str] = None,
        parent_command_line: Optional[str] = None,
        parent_image_file_name: Optional[str] = None,
        pattern_ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_default_ss_exclusions(
        self,
        *,
        aid: Optional[str] = None,
        command_line: Optional[str] = None,
        grandparent_command_line: Optional[str] = None,
        grandparent_image_file_name: Optional[str] = None,
        image_file_name: Optional[str] = None,
        parent_command_line: Optional[str] = None,
        parent_image_file_name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_ss_exclusions(
        self,
        *,
        filter: Optional[str] = None,
        ifn_regex: Optional[str] = None,
        cl_regex: Optional[str] = None,
        parent_ifn_regex: Optional[str] = None,
        parent_cl_regex: Optional[str] = None,
        grandparent_ifn_regex: Optional[str] = None,
        grandparent_cl_regex: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_exclusions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_exclusions(
        self,
        *,
        cl_regex: Optional[str] = None,
        comment: Optional[str] = None,
        description: Optional[str] = None,
        detection_json: Optional[str] = None,
        groups: Optional[Union[str, List[str]]] = None,
        ifn_regex: Optional[str] = None,
        name: Optional[str] = None,
        pattern_id: Optional[str] = None,
        pattern_name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_exclusions(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_exclusions(
        self,
        *,
        cl_regex: Optional[str] = None,
        comment: Optional[str] = None,
        description: Optional[str] = None,
        detection_json: Optional[str] = None,
        groups: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        ifn_regex: Optional[str] = None,
        name: Optional[str] = None,
        pattern_id: Optional[str] = None,
        pattern_name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_exclusions(
        self,
        *,
        filter: Optional[str] = None,
        ifn_regex: Optional[str] = None,
        cl_regex: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    getIOAExclusionsV1 = get_exclusions
    createIOAExclusionsV1 = create_exclusions
    deleteIOAExclusionsV1 = delete_exclusions
    updateIOAExclusionsV1 = update_exclusions
    queryIOAExclusionsV1 = query_exclusions
    ss_ioa_exclusions_aggregates_v2 = get_ss_exclusion_aggregates
    ss_ioa_exclusions_get_reports_v2 = get_ss_exclusion_reports_v2
    ss_ioa_exclusions_get_v2 = get_ss_exclusion_rules_v2
    ss_ioa_exclusions_create_v2 = create_ss_exclusions
    ss_ioa_exclusions_update_v2 = update_ss_exclusions
    ss_ioa_exclusions_delete_v2 = delete_ss_exclusions
    ss_ioa_exclusions_matched_rule_v2 = get_ss_exclusion_matched_rules
    ss_ioa_exclusions_new_rules_v2 = get_default_ss_exclusions
    ss_ioa_exclusions_query_v2 = query_ss_exclusions
