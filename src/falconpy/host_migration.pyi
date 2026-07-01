"""Type stubs for host_migration."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class HostMigration(ServiceClass):

    def aggregate_host_migration(
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

    def aggregate_migration(
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

    def perform_host_migration_action(
        self,
        *,
        id: Optional[str] = None,
        action_name: Optional[str] = None,
        action_parameters: Optional[list] = None,
        filter: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_host_migration_details(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_migration_destination(
        self,
        *,
        device_ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def perform_migration_job_action(
        self,
        *,
        action_name: Optional[str] = None,
        action_parameters: Optional[list] = None,
        filter: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_migration_job_details(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_migration(
        self,
        *,
        device_ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        name: Optional[str] = None,
        target_cid: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_host_migration_ids(
        self,
        *,
        id: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_migration_jobs(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    HostMigrationAggregatesV1 = aggregate_host_migration
    MigrationAggregatesV1 = aggregate_migration
    HostMigrationsActionsV1 = perform_host_migration_action
    GetHostMigrationsV1 = get_host_migration_details
    GetMigrationDestinationsV1 = get_migration_destination
    MigrationsActionsV1 = perform_migration_job_action
    GetMigrationsV1 = get_migration_job_details
    CreateMigrationV1 = create_migration
    GetHostMigrationIDsV1 = query_host_migration_ids
    GetMigrationIDsV1 = query_migration_jobs
