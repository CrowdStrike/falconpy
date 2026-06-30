"""Type stubs for custom_storage."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CustomStorage(ServiceClass):

    def list_collections(
        self,
        *,
        end: Optional[str] = None,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def describe_collections(
        self,
        *,
        names: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def describe_collection(
        self,
        *,
        collection_name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list(
        self,
        *,
        collection_name: Optional[str] = None,
        end: Optional[str] = None,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search(
        self,
        *,
        collection_name: Optional[str] = None,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get(
        self,
        *,
        collection_name: Optional[str] = None,
        object_key: Optional[str] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def upload(
        self,
        *,
        collection_name: Optional[str] = None,
        dry_run: Optional[bool] = None,
        object_key: Optional[str] = None,
        schema_version: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete(
        self,
        *,
        collection_name: Optional[str] = None,
        dry_run: Optional[bool] = None,
        object_key: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def metadata(
        self,
        *,
        collection_name: Optional[str] = None,
        object_key: Optional[str] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_schemas(
        self,
        *,
        collection_name: Optional[str] = None,
        end: Optional[str] = None,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_schema(
        self,
        *,
        collection_name: Optional[str] = None,
        schema_version: Optional[str] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def schema_metadata(
        self,
        *,
        collection_name: Optional[str] = None,
        schema_version: Optional[str] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_by_version(
        self,
        *,
        collection_name: Optional[str] = None,
        collection_version: Optional[str] = None,
        end: Optional[str] = None,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_by_version(
        self,
        *,
        collection_name: Optional[str] = None,
        collection_version: Optional[str] = None,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_version(
        self,
        *,
        collection_name: Optional[str] = None,
        collection_version: Optional[str] = None,
        object_key: Optional[str] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def upload_version(
        self,
        *,
        collection_name: Optional[str] = None,
        collection_version: Optional[str] = None,
        dry_run: Optional[bool] = None,
        object_key: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_version(
        self,
        *,
        collection_name: Optional[str] = None,
        collection_version: Optional[str] = None,
        dry_run: Optional[bool] = None,
        object_key: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def version_metadata(
        self,
        *,
        collection_name: Optional[str] = None,
        collection_version: Optional[str] = None,
        object_key: Optional[str] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ListCollections = list_collections
    DescribeCollections = describe_collections
    DescribeCollection = describe_collection
    ListObjects = list
    SearchObjects = search
    GetObject = get
    PutObject = upload
    DeleteObject = delete
    GetObjectMetadata = metadata
    ListSchemas = list_schemas
    GetSchema = get_schema
    GetSchemaMetadata = schema_metadata
    ListObjectsByVersion = list_by_version
    SearchObjectsByVersion = search_by_version
    GetVersionedObject = get_version
    PutObjectByVersion = upload_version
    DeleteVersionedObject = delete_version
    GetVersionedObjectMetadata = version_metadata
