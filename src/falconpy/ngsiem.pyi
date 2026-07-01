"""Type stubs for ngsiem."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class NGSIEM(ServiceClass):

    def upload_file(
        self,
        *,
        repository: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_file(
        self,
        *,
        repository: Optional[str] = None,
        filename: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_file_from_package_with_namespace(
        self,
        *,
        repository: Optional[str] = None,
        namespace: Optional[str] = None,
        package: Optional[str] = None,
        filename: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_file_from_package(
        self,
        *,
        repository: Optional[str] = None,
        package: Optional[str] = None,
        filename: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def start_search(
        self,
        *,
        repository: Optional[str] = None,
        allowEventSkipping: Optional[bool] = None,
        arguments: Optional[dict] = None,
        around: Optional[dict] = None,
        autobucketCount: Optional[int] = None,
        end: Optional[str] = None,
        ingestEnd: Optional[str] = None,
        ingestStart: Optional[str] = None,
        isLive: Optional[bool] = None,
        queryString: Optional[str] = None,
        start: Optional[str] = None,
        timeZone: Optional[str] = None,
        timeZoneOffsetMinutes: Optional[int] = None,
        useIngestTime: Optional[bool] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_search_status(
        self,
        *,
        repository: Optional[str] = None,
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def stop_search(
        self,
        *,
        repository: Optional[str] = None,
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_dashboard_template(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_dashboard_from_template(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_dashboard_from_template(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_dashboard(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_lookup_file(
        self,
        *,
        filename: Optional[str] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_lookup_file(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_lookup_file(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_lookup_file(
        self,
        *,
        filename: Optional[Union[str, List[str]]] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def clone_parser(
        self,
        *,
        new_name: Optional[str] = None,
        source_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def test_parser_from_template(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_parser_template(
        self,
        *,
        ids: Optional[str] = None,
        repository: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_parser_from_template(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_parser(
        self,
        *,
        ids: Optional[str] = None,
        repository: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_parser(
        self,
        *,
        fields_to_be_removed_before_parsing: Optional[Union[str, List[str]]] = None,
        fields_to_tag: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        repository: Optional[str] = None,
        script: Optional[str] = None,
        test_cases: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_parser(
        self,
        *,
        fields_to_be_removed_before_parsing: Optional[Union[str, List[str]]] = None,
        fields_to_tag: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        repository: Optional[str] = None,
        script: Optional[str] = None,
        test_cases: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_parser_from_template(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_parser(
        self,
        *,
        ids: Optional[str] = None,
        repository: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_parser_auto_update_policy(
        self,
        *,
        autoupdate_policy: Optional[str] = None,
        reason: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def install_parser(
        self,
        *,
        parser_id: Optional[str] = None,
        version: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def bulk_install_parsers(
        self,
        *,
        parsers: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_saved_query_template(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_saved_query(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_saved_query_from_template(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_saved_query(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_dashboards(
        self,
        *,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        filter: Optional[str] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_lookup_files(
        self,
        *,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        filter: Optional[str] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_parsers(
        self,
        *,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        filter: Optional[str] = None,
        repository: Optional[str] = None,
        update_available: Optional[str] = None,
        parser_type: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_saved_queries(
        self,
        *,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        filter: Optional[str] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_lookup_file_entries(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_data_connections(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_data_connectors(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_provisioning_status(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_connection_status(
        self,
        *,
        ids: Optional[str] = None,
        status: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_ingest_token(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def regenerate_ingest_token(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_connection_by_id(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_data_connection(
        self,
        *,
        config: Optional[dict] = None,
        config_id: Optional[str] = None,
        connector_id: Optional[str] = None,
        connector_type: Optional[str] = None,
        custom: Optional[dict] = None,
        description: Optional[str] = None,
        enable_host_enrichment: Optional[bool] = None,
        enable_user_enrichment: Optional[bool] = None,
        log_sources: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        parser: Optional[str] = None,
        vendor_name: Optional[str] = None,
        vendor_product_name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_data_connection(
        self,
        *,
        ids: Optional[str] = None,
        config: Optional[dict] = None,
        config_id: Optional[str] = None,
        custom: Optional[dict] = None,
        description: Optional[str] = None,
        enable_host_enrichment: Optional[bool] = None,
        enable_user_enrichment: Optional[bool] = None,
        log_sources: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        parser: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_data_connection(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_connector_configs(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_connector_config(
        self,
        *,
        config: Optional[dict] = None,
        connector_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def patch_connector_config(
        self,
        *,
        ids: Optional[str] = None,
        config: Optional[dict] = None,
        connector_id: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_connector_configs(
        self,
        *,
        connector_id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def bulk_create_dashboards_from_template(
        self,
        *,
        dashboard_items: Optional[list] = None,
        search_domain: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def bulk_create_lookup_files(
        self,
        *,
        lookup_files: Optional[list] = None,
        search_domain: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def bulk_create_saved_queries_from_template(
        self,
        *,
        saved_query_items: Optional[list] = None,
        search_domain: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def bulk_get_lookup_files(
        self,
        *,
        filename: Optional[Union[str, List[str]]] = None,
        search_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def bulk_update_dashboards_from_template(
        self,
        *,
        dashboard_items: Optional[list] = None,
        search_domain: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def bulk_update_lookup_files(
        self,
        *,
        lookup_files: Optional[list] = None,
        search_domain: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def bulk_update_saved_queries_from_template(
        self,
        *,
        saved_query_items: Optional[list] = None,
        search_domain: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_parser_extension(
        self,
        *,
        base_parser_id: Optional[str] = None,
        extension_name: Optional[str] = None,
        parser_id: Optional[str] = None,
        post_processing_script: Optional[str] = None,
        pre_processing_script: Optional[str] = None,
        test_cases: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_parser_extension(
        self,
        *,
        extension_id: Optional[str] = None,
        post_processing_script: Optional[str] = None,
        pre_processing_script: Optional[str] = None,
        test_cases: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    BulkCreateDashboardsFromTemplate = bulk_create_dashboards_from_template
    BulkCreateLookupFiles = bulk_create_lookup_files
    BulkCreateSavedQueriesFromTemplate = bulk_create_saved_queries_from_template
    BulkGetLookupFiles = bulk_get_lookup_files
    BulkUpdateDashboardsFromTemplate = bulk_update_dashboards_from_template
    BulkUpdateLookupFiles = bulk_update_lookup_files
    BulkUpdateSavedQueriesFromTemplate = bulk_update_saved_queries_from_template
    CreateParserExtension = create_parser_extension
    UpdateParserExtension = update_parser_extension
    UploadLookupV1 = upload_file
    GetLookupV1 = get_file
    GetLookupFromPackageWithNamespaceV1 = get_file_from_package_with_namespace
    GetLookupFromPackageV1 = get_file_from_package
    StartSearchV1 = start_search
    GetSearchStatusV1 = get_search_status
    StopSearchV1 = stop_search
    GetDashboardTemplate = get_dashboard_template
    CreateDashboardFromTemplate = create_dashboard_from_template
    UpdateDashboardFromTemplate = update_dashboard_from_template
    DeleteDashboard = delete_dashboard
    GetLookupFile = get_lookup_file
    CreateLookupFile = create_lookup_file
    UpdateLookupFile = update_lookup_file
    DeleteLookupFile = delete_lookup_file
    CloneParser = clone_parser
    TestParserFromTemplate = test_parser_from_template
    GetParserTemplate = get_parser_template
    CreateParserFromTemplate = create_parser_from_template
    GetParser = get_parser
    CreateParser = create_parser
    UpdateParser = update_parser
    UpdateParserFromTemplate = update_parser_from_template
    DeleteParser = delete_parser
    UpdateParserAutoUpdatePolicy = update_parser_auto_update_policy
    InstallParser = install_parser
    BulkInstallParsers = bulk_install_parsers
    GetSavedQueryTemplate = get_saved_query_template
    CreateSavedQuery = create_saved_query
    UpdateSavedQueryFromTemplate = update_saved_query_from_template
    DeleteSavedQuery = delete_saved_query
    ListDashboards = list_dashboards
    ListLookupFiles = list_lookup_files
    ListParsers = list_parsers
    ListSavedQueries = list_saved_queries
    UpdateLookupFileEntries = update_lookup_file_entries
    ExternalListDataConnections = list_data_connections
    ExternalListDataConnectors = list_data_connectors
    ExternalGetDataConnectionStatus = get_provisioning_status
    ExternalUpdateDataConnectionStatus = update_connection_status
    ExternalGetDataConnectionToken = get_ingest_token
    ExternalRegenerateDataConnectionToken = regenerate_ingest_token
    ExternalGetDataConnectionByID = get_connection_by_id
    ExternalCreateDataConnection = create_data_connection
    ExternalUpdateDataConnection = update_data_connection
    ExternalDeleteDataConnection = delete_data_connection
    ExternalListConnectorConfigs = list_connector_configs
    ExternalCreateConnectorConfig = create_connector_config
    ExternalPatchConnectorConfig = patch_connector_config
    ExternalDeleteConnectorConfigs = delete_connector_configs
