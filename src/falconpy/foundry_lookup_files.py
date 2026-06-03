"""CrowdStrike Falcon FoundryLookupFiles API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
from typing import Dict, Union
from ._util import force_default, process_service_request, generate_error_result, params_to_keywords
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._foundry_lookup_files import _foundry_lookup_files_endpoints as Endpoints


class FoundryLookupFiles(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def create_file_v1(self: object,
                       parameters: dict = None,
                       **kwargs
                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a lookup file within a foundry app.

        Keyword arguments:
        file_name -- Name to use for the uploaded file. String.
        file -- File to be uploaded. String.
        name -- Name used to identify the file. String.
        description -- File description. String.
        id -- Unique identifier of the file being updated. String.
        repo -- Name of repository or view to save the file. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/foundry-lookup-files/CreateFileV1
        """
        kwargs = params_to_keywords(["file", "name", "description", "id", "repo"],
                                    parameters,
                                    kwargs
                                    )
        file_name = kwargs.get("file_name", None)
        file_data = kwargs.get("file", None)
        if not file_data:
            return generate_error_result("You must provide a file to upload.", code=400)
        file_extended = {}
        if kwargs.get("name", None) is not None:
            file_extended["name"] = kwargs.get("name")
        if kwargs.get("description", None) is not None:
            file_extended["description"] = kwargs.get("description")
        if kwargs.get("id", None) is not None:
            file_extended["id"] = kwargs.get("id")
        if kwargs.get("repo", None) is not None:
            file_extended["repo"] = kwargs.get("repo")
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateFileV1",
            data=file_extended,
            files=[("file", (file_name, file_data))]
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_file_v1(self: object,
                       parameters: dict = None,
                       **kwargs
                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a lookup file within a Foundry app.

        Keyword arguments:
        file_name -- Name to use for the uploaded file. String.
        id -- Unique identifier of the file being updated. String.
        description -- File description. String.
        file -- File to be uploaded. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/foundry-lookup-files/UpdateFileV1
        """
        kwargs = params_to_keywords(["id", "description", "file"],
                                    parameters,
                                    kwargs
                                    )
        file_name = kwargs.get("file_name", None)
        file_data = kwargs.get("file", None)
        file_extended = {}
        if kwargs.get("id", None) is not None:
            file_extended["id"] = kwargs.get("id")
        if kwargs.get("description", None) is not None:
            file_extended["description"] = kwargs.get("description")
        file_uploads = []
        if file_data:
            file_uploads = [("file", (file_name, file_data))]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateFileV1",
            data=file_extended,
            files=file_uploads
            )
    CreateFileV1 = create_file_v1
    UpdateFileV1 = update_file_v1
