"""Type stubs for foundry_lookup_files."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FoundryLookupFiles(ServiceClass):

    def create_file_v1(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_file_v1(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    CreateFileV1 = create_file_v1
    UpdateFileV1 = update_file_v1
