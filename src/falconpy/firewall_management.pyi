"""Type stubs for firewall_management."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FirewallManagement(ServiceClass):

    def aggregate_events(
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

    def aggregate_policy_rules(
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

    def aggregate_rule_groups(
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

    def aggregate_rules(
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

    def get_events(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_firewall_fields(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_network_locations_details(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_network_locations_metadata(
        self,
        *,
        comment: Optional[str] = None,
        cid: Optional[str] = None,
        dns_resolution_targets_polling_interval: Optional[int] = None,
        https_reachable_hosts_polling_interval: Optional[int] = None,
        icmp_request_targets_polling_interval: Optional[int] = None,
        location_precedence: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_network_locations_precedence(
        self,
        *,
        comment: Optional[str] = None,
        cid: Optional[str] = None,
        location_precedence: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_network_locations(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_network_locations(
        self,
        *,
        clone_id: Optional[str] = None,
        add_fw_rules: Optional[bool] = None,
        comment: Optional[str] = None,
        connection_types: Optional[dict] = None,
        default_gateways: Optional[Union[str, List[str]]] = None,
        description: Optional[str] = None,
        dhcp_servers: Optional[Union[str, List[str]]] = None,
        dns_resolution_targets: Optional[dict] = None,
        dns_servers: Optional[Union[str, List[str]]] = None,
        enabled: Optional[bool] = None,
        host_addresses: Optional[Union[str, List[str]]] = None,
        https_reachable_hosts: Optional[dict] = None,
        icmp_request_targets: Optional[dict] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def upsert_network_locations(
        self,
        *,
        comment: Optional[str] = None,
        connection_types: Optional[dict] = None,
        created_by: Optional[str] = None,
        created_on: Optional[str] = None,
        default_gateways: Optional[Union[str, List[str]]] = None,
        description: Optional[str] = None,
        dhcp_servers: Optional[Union[str, List[str]]] = None,
        dns_resolution_targets: Optional[dict] = None,
        dns_servers: Optional[Union[str, List[str]]] = None,
        enabled: Optional[bool] = None,
        host_addresses: Optional[Union[str, List[str]]] = None,
        https_reachable_hosts: Optional[dict] = None,
        icmp_request_targets: Optional[dict] = None,
        id: Optional[str] = None,
        modified_by: Optional[str] = None,
        modified_on: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_network_locations(
        self,
        *,
        comment: Optional[str] = None,
        connection_types: Optional[dict] = None,
        created_by: Optional[str] = None,
        created_on: Optional[str] = None,
        default_gateways: Optional[Union[str, List[str]]] = None,
        description: Optional[str] = None,
        dhcp_servers: Optional[Union[str, List[str]]] = None,
        dns_resolution_targets: Optional[dict] = None,
        dns_servers: Optional[Union[str, List[str]]] = None,
        enabled: Optional[bool] = None,
        host_addresses: Optional[Union[str, List[str]]] = None,
        https_reachable_hosts: Optional[dict] = None,
        icmp_request_targets: Optional[dict] = None,
        id: Optional[str] = None,
        modified_by: Optional[str] = None,
        modified_on: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_network_locations(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_platforms(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_policy_containers(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_container_v1(
        self,
        *,
        default_inbound: Optional[str] = None,
        default_outbound: Optional[str] = None,
        enforce: Optional[bool] = None,
        is_default_policy: Optional[bool] = None,
        local_logging: Optional[bool] = None,
        platform_id: Optional[str] = None,
        policy_id: Optional[str] = None,
        rule_group_ids: Optional[Union[str, List[str]]] = None,
        test_mode: Optional[bool] = None,
        tracking: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_container(
        self,
        *,
        default_inbound: Optional[str] = None,
        default_outbound: Optional[str] = None,
        enforce: Optional[bool] = None,
        is_default_policy: Optional[bool] = None,
        local_logging: Optional[bool] = None,
        platform_id: Optional[str] = None,
        policy_id: Optional[str] = None,
        rule_group_ids: Optional[Union[str, List[str]]] = None,
        test_mode: Optional[bool] = None,
        tracking: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule_groups(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule_group(
        self,
        *,
        clone_id: Optional[str] = None,
        library: Optional[str] = None,
        comment: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        name: Optional[str] = None,
        platform: Optional[str] = None,
        rules: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rule_groups(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule_group(
        self,
        *,
        comment: Optional[str] = None,
        diff_operations: Optional[list] = None,
        diff_type: Optional[str] = None,
        id: Optional[str] = None,
        rule_ids: Optional[Union[str, List[str]]] = None,
        rule_versions: Optional[list] = None,
        tracking: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rule_group_validation(
        self,
        *,
        clone_id: Optional[str] = None,
        library: Optional[str] = None,
        comment: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        name: Optional[str] = None,
        platform: Optional[str] = None,
        rules: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rule_group_validation(
        self,
        *,
        comment: Optional[str] = None,
        diff_operations: Optional[list] = None,
        diff_type: Optional[str] = None,
        id: Optional[str] = None,
        rule_ids: Optional[Union[str, List[str]]] = None,
        rule_versions: Optional[list] = None,
        tracking: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def validate_filepath_pattern(
        self,
        *,
        filepath_pattern: Optional[str] = None,
        filepath_test_string: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_events(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        offset: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_firewall_fields(
        self,
        *,
        platform_id: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_network_locations(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        offset: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_platforms(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_policy_rules(
        self,
        *,
        id: Optional[str] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rule_groups(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        offset: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rules(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        offset: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    update_policy_container_v2 = update_policy_container
