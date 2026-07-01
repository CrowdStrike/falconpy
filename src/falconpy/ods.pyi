"""Type stubs for ods."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ODS(ServiceClass):

    def aggregate_scan_hosts(
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

    def aggregate_scans(
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

    def aggregate_scheduled_scans(
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

    def get_malicious_files(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cancel_scans(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scan_hosts(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scans_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scans(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_scan(
        self,
        *,
        cloud_ml_level_detection: Optional[int] = None,
        cloud_ml_level_prevention: Optional[int] = None,
        cloud_pup_adware_level_detection: Optional[int] = None,
        cloud_pup_adware_level_prevention: Optional[int] = None,
        cpu_priority: Optional[int] = None,
        description: Optional[str] = None,
        endpoint_notification: Optional[bool] = None,
        file_paths: Optional[Union[str, List[str]]] = None,
        host_groups: Optional[Union[str, List[str]]] = None,
        hosts: Optional[Union[str, List[str]]] = None,
        initiated_from: Optional[str] = None,
        mac_cloud_ml_level_detection: Optional[int] = None,
        mac_cloud_ml_level_prevention: Optional[int] = None,
        mac_cloud_pup_adware_level_detection: Optional[int] = None,
        mac_cloud_pup_adware_level_prevention: Optional[int] = None,
        mac_scan_exclusions: Optional[Union[str, List[str]]] = None,
        mac_scan_inclusions: Optional[Union[str, List[str]]] = None,
        mac_sensor_ml_level_detection: Optional[int] = None,
        mac_sensor_ml_level_prevention: Optional[int] = None,
        mac_sensor_pup_adware_level_detection: Optional[int] = None,
        mac_sensor_pup_adware_level_prevention: Optional[int] = None,
        max_duration: Optional[int] = None,
        pause_duration: Optional[int] = None,
        quarantine: Optional[bool] = None,
        scan_exclusions: Optional[Union[str, List[str]]] = None,
        scan_inclusions: Optional[Union[str, List[str]]] = None,
        sensor_ml_level_detection: Optional[int] = None,
        sensor_ml_level_prevention: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scheduled_scans(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def schedule_scan(
        self,
        *,
        cloud_ml_level_detection: Optional[int] = None,
        cloud_ml_level_prevention: Optional[int] = None,
        cloud_pup_adware_level_detection: Optional[int] = None,
        cloud_pup_adware_level_prevention: Optional[int] = None,
        cpu_priority: Optional[int] = None,
        description: Optional[str] = None,
        endpoint_notification: Optional[bool] = None,
        file_paths: Optional[Union[str, List[str]]] = None,
        host_groups: Optional[Union[str, List[str]]] = None,
        initiated_from: Optional[str] = None,
        mac_cloud_ml_level_detection: Optional[int] = None,
        mac_cloud_ml_level_prevention: Optional[int] = None,
        mac_cloud_pup_adware_level_detection: Optional[int] = None,
        mac_cloud_pup_adware_level_prevention: Optional[int] = None,
        mac_scan_exclusions: Optional[Union[str, List[str]]] = None,
        mac_scan_inclusions: Optional[Union[str, List[str]]] = None,
        mac_sensor_ml_level_detection: Optional[int] = None,
        mac_sensor_ml_level_prevention: Optional[int] = None,
        mac_sensor_pup_adware_level_detection: Optional[int] = None,
        mac_sensor_pup_adware_level_prevention: Optional[int] = None,
        max_duration: Optional[int] = None,
        max_file_size: Optional[int] = None,
        pause_duration: Optional[int] = None,
        quarantine: Optional[bool] = None,
        scan_exclusions: Optional[Union[str, List[str]]] = None,
        scan_inclusions: Optional[Union[str, List[str]]] = None,
        schedule: Optional[dict] = None,
        sensor_ml_level_detection: Optional[int] = None,
        sensor_ml_level_prevention: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_scheduled_scans(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_malicious_files(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_scan_hosts(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_scans(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_scheduled_scans(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    get_malicious_files_by_ids = get_malicious_files
    get_scan_host_metadata_by_ids = get_scan_hosts
    get_scans_by_scan_ids = get_scans
    get_scans_by_scan_ids_v1 = get_scans_v1
    get_scans_by_scan_ids_v2 = get_scans
    get_scheduled_scans_by_scan_ids = get_scheduled_scans
    query_scan_host_metadata = query_scan_hosts
    aggregate_query_scan_host_metadata = aggregate_scan_hosts
