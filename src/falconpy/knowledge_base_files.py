"""CrowdStrike Falcon KnowledgeBaseFiles API interface class.

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
from ._endpoint._knowledge_base_files import _knowledge_base_files_endpoints as Endpoints


class KnowledgeBaseFiles(ServiceClass):
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
    def entities_knowledge_base_files_download_v1(self: object,
                                                  parameters: dict = None,
                                                  **kwargs
                                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download knowledge base file entities for the provided id.

        Keyword arguments:
        knowledge_base_id -- ID of the knowledge base String.
        id -- ID of entities to retrieve. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-base-files/EntitiesKnowledgeBaseFilesDownloadV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesKnowledgeBaseFilesDownloadV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def entities_knowledge_base_files_v1(self: object,
                                         parameters: dict = None,
                                         **kwargs
                                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve knowledge base file entities for the provided id.

        Keyword arguments:
        knowledge_base_id -- ID of the knowledge base String.
        ids -- IDs of entities to retrieve. List.
        include_deleted -- Include deleted knowledge base files in the result. Defaults to false. Boolean.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-base-files/EntitiesKnowledgeBaseFilesV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesKnowledgeBaseFilesV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def entities_knowledge_base_files_update_v1(self: object,
                                                parameters: dict = None,
                                                **kwargs
                                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing file in a knowledge base.

        Keyword arguments:
        file_name -- Name to use for the uploaded file. String.
        id -- ID of the document to update. String.
        file -- New file content to replace the existing document. String.
        file_description -- New description for the document. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PUT

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-base-files/EntitiesKnowledgeBaseFilesUpdateV1
        """
        kwargs = params_to_keywords(["id", "file", "file_description"],
                                    parameters,
                                    kwargs
                                    )
        file_name = kwargs.get("file_name", None)
        file_data = kwargs.get("file", None)
        if not file_data:
            return generate_error_result("You must provide a file to upload.", code=400)
        file_extended = {}
        if kwargs.get("id", None) is not None:
            file_extended["id"] = kwargs.get("id")
        if kwargs.get("file_description", None) is not None:
            file_extended["file_description"] = kwargs.get("file_description")
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesKnowledgeBaseFilesUpdateV1",
            data=file_extended,
            files=[("file", (file_name, file_data))]
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def entities_knowledge_base_files_create_v1(self: object,
                                                parameters: dict = None,
                                                **kwargs
                                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload a file to a knowledge base.

        Keyword arguments:
        file_name -- Name to use for the uploaded file. String.
        knowledge_base_id -- ID of the knowledge base. String.
        file -- File to be uploaded. String.
        file_description -- Description for the uploaded file. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-base-files/EntitiesKnowledgeBaseFilesCreateV1
        """
        kwargs = params_to_keywords(["knowledge_base_id", "file", "file_description"],
                                    parameters,
                                    kwargs
                                    )
        file_name = kwargs.get("file_name", None)
        file_data = kwargs.get("file", None)
        if not file_data:
            return generate_error_result("You must provide a file to upload.", code=400)
        file_extended = {}
        if kwargs.get("knowledge_base_id", None) is not None:
            file_extended["knowledge_base_id"] = kwargs.get("knowledge_base_id")
        if kwargs.get("file_description", None) is not None:
            file_extended["file_description"] = kwargs.get("file_description")
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesKnowledgeBaseFilesCreateV1",
            data=file_extended,
            files=[("file", (file_name, file_data))]
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def entities_knowledge_base_files_delete_v1(self: object,
                                                parameters: dict = None,
                                                **kwargs
                                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete document from knowledge base.

        Keyword arguments:
        knowledge_base_id -- ID of the knowledge base String.
        id -- ID of the document to delete String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-base-files/EntitiesKnowledgeBaseFilesDeleteV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesKnowledgeBaseFilesDeleteV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queries_knowledge_base_files_v1(self: object,
                                        parameters: dict = None,
                                        **kwargs
                                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query knowledge base files based on the provided filters.

        Keyword arguments:
        knowledge_base_id -- ID of the knowledge base String.
        offset -- Starting index of overall result set from which to return ids. Integer.
        limit -- Number of IDs to return. Offset + limit should NOT be above 10K. Integer.
        filter -- FQL query specifying the filter parameters. String.
        include_deleted -- Include deleted knowledge base files in the result. Defaults to false. Boolean.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-base-files/QueriesKnowledgeBaseFilesV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueriesKnowledgeBaseFilesV1",
            keywords=kwargs,
            params=parameters
            )
    EntitiesKnowledgeBaseFilesDownloadV1 = entities_knowledge_base_files_download_v1
    EntitiesKnowledgeBaseFilesV1 = entities_knowledge_base_files_v1
    EntitiesKnowledgeBaseFilesUpdateV1 = entities_knowledge_base_files_update_v1
    EntitiesKnowledgeBaseFilesCreateV1 = entities_knowledge_base_files_create_v1
    EntitiesKnowledgeBaseFilesDeleteV1 = entities_knowledge_base_files_delete_v1
    QueriesKnowledgeBaseFilesV1 = queries_knowledge_base_files_v1
