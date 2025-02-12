"""CrowdStrike Falcon NGSIEM API interface class.

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
from ._util import force_default, process_service_request, generate_error_result
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._ngsiem import _ngsiem_endpoints as Endpoints


class NGSIEM(ServiceClass):
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
    def upload_file(self: object,
                    parameters: dict = None,
                    **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload file to NGSIEM.

        Keyword arguments:
        lookup_file -- File to be uploaded. Binary data.  (CSV format)
        repository -- Name of the repository. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UploadLookupV1
        """
        lookup_file = kwargs.get("lookup_file", None)
        repository = kwargs.get("repository", None)
        if repository and lookup_file:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            try:
                with open(lookup_file, "rb") as upload_file:
                    # Create a multipart form payload for our upload file
                    file_extended = {"file": upload_file}
                    returned = process_service_request(calling_object=self,
                                                       endpoints=Endpoints,
                                                       operation_id="UploadLookupV1",
                                                       keywords=kwargs,
                                                       params=parameters,
                                                       repository=repository,
                                                       files=file_extended
                                                       )
            except FileNotFoundError:
                returned = generate_error_result("Invalid upload file specified.")
        else:
            returned = generate_error_result("You must provide a repository and lookup_file "
                                             "argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_file(self: object,
                 parameters: dict = None,
                 **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download lookup file from NGSIEM.

        Keyword arguments:
        repository -- Name of the repository. String.
        filename -- Name of the lookup file. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/GetLookupV1
        """
        repository = kwargs.get("repository", None)
        filename = kwargs.get("filename", None)
        if repository and filename:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            kwargs.pop("filename")
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="GetLookupV1",
                keywords=kwargs,
                params=parameters,
                repository=repository,
                filename=filename
                )
        else:
            returned = generate_error_result("You must provide a repository and filename "
                                             "argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_file_from_package_with_namespace(self: object,
                                             parameters: dict = None,
                                             **kwargs
                                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download lookup file in namespaced package from NGSIEM.

        Keyword arguments:
        repository -- Name of repository. String.
        namespace -- Name of namespace. String.
        package -- Name of package. String.
        filename -- Name of lookup file. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
            /humio-auth-proxy/GetLookupFromPackageWithNamespaceV1
        """
        repository = kwargs.get("repository", None)
        filename = kwargs.get("filename", None)
        namespace = kwargs.get("namespace", None)
        package = kwargs.get("package", None)
        if min([repository, filename, namespace, package]):
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            kwargs.pop("namespace")
            kwargs.pop("package")
            kwargs.pop("filename")
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="GetLookupFromPackageWithNamespaceV1",
                keywords=kwargs,
                params=parameters,
                repository=repository,
                filename=filename,
                namespace=namespace,
                package=package
                )
        else:
            returned = generate_error_result("You must provide a repository, namespace, package and"
                                             " filename argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_file_from_package(self: object,
                              parameters: dict = None,
                              **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download lookup file in package from NGSIEM.

        Keyword arguments:
        repository -- Name of repository. String.
        package -- Name of package. String.
        filename -- Name of lookup file. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/GetLookupFromPackageV1
        """
        repository = kwargs.get("repository", None)
        filename = kwargs.get("filename", None)
        package = kwargs.get("package", None)
        if min([repository, filename, package]):
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            kwargs.pop("package")
            kwargs.pop("filename")
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="GetLookupFromPackageV1",
                keywords=kwargs,
                params=parameters,
                repository=repository,
                filename=filename,
                package=package
                )
        else:
            returned = generate_error_result("You must provide a repository, package and"
                                             " filename argument in order to use this operation."
                                             )
        return returned

    # @force_default(defaults=["parameters"], default_types=["dict"])
    # def start_streaming_search(self: object,
    #                            parameters: dict = None,
    #                            **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
    #     """Initiate streaming (synchronous) search.

    #     Keyword arguments:
    #     repository -- name of repository
    #     parameters -- Full parameters payload dictionary. Not required if using other keywords.

    #     This method only supports keywords for providing arguments.

    #     Returns: dict object containing API response.

    #     HTTP Method: POST

    #     Swagger URL

    #     """
    #     return process_service_request(
    #         calling_object=self,
    #         endpoints=Endpoints,
    #         operation_id="StartSearchStreamingV1",
    #         keywords=kwargs,
    #         params=parameters
    #         )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def start_search(self: object,
                     parameters: dict = None,
                     **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Initiate search.

        Keyword arguments:
        repository -- Name of repository. String.
        search -- Search to perform. JSON formatted string.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/StartSearchV1
        """
        repository = kwargs.get("repository", None)
        search = kwargs.get("search", None)
        if repository and search:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="StartSearchV1",
                keywords=kwargs,
                params=parameters,
                repository=repository,
                body=search
                )
            if "body" in returned:
                returned["resources"] = returned["body"]
                returned.pop("body")
        else:
            returned = generate_error_result("You must provide a repository and search "
                                             "argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_search_status(self: object,
                          parameters: dict = None,
                          **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get status of search.

        Keyword arguments:
        repository -- Name of repository. String.
        search_id -- ID of query. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/GetSearchStatusV1
        """
        repository = kwargs.get("repository", None)
        search_id = kwargs.get("search_id", None)
        if repository and search_id:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            kwargs.pop("search_id")
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="GetSearchStatusV1",
                keywords=kwargs,
                params=parameters,
                repository=repository,
                search_id=search_id
                )
        else:
            returned = generate_error_result("You must provide a repository and search_id "
                                             "argument in order to use this operation."
                                             )

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def stop_search(self: object,
                    parameters: dict = None,
                    **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Stop search.

        Keyword arguments:
        repository -- name of repository
        id -- id of query
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/StopSearchV1
        """
        repository = kwargs.get("repository", None)
        search_id = kwargs.get("search_id", None)
        if repository and search_id:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            kwargs.pop("search_id")
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="StopSearchV1",
                keywords=kwargs,
                params=parameters,
                repository=repository,
                search_id=search_id
                )
        else:
            returned = generate_error_result("You must provide a repository and search_id "
                                             "argument in order to use this operation."
                                             )
        return returned

    # @force_default(defaults=["parameters"], default_types=["dict"])
    # def proxy_http_get(self: object,
    #                    parameters: dict = None,
    #                    **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
    #     """Routes a GET request to NGSIEM.

    #     Keyword arguments:
    #     path -- LogScale path
    #     parameters -- Full parameters payload dictionary. Not required if using other keywords.

    #     This method only supports keywords for providing arguments.

    #     Returns: dict object containing API response.

    #     HTTP Method: GET

    #     Swagger URL

    #     """
    #     return process_service_request(
    #         calling_object=self,
    #         endpoints=Endpoints,
    #         operation_id="proxy_http_get",
    #         keywords=kwargs,
    #         params=parameters
    #         )

    # @force_default(defaults=["parameters"], default_types=["dict"])
    # def proxy_http_post(self: object,
    #                     parameters: dict = None,
    #                     **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
    #     """Routes a POST request to NGSIEM.

    #     Keyword arguments:
    #     path -- LogScale path
    #     parameters -- Full parameters payload dictionary. Not required if using other keywords.

    #     This method only supports keywords for providing arguments.

    #     Returns: dict object containing API response.

    #     HTTP Method: POST

    #     Swagger URL

    #     """
    #     return process_service_request(
    #         calling_object=self,
    #         endpoints=Endpoints,
    #         operation_id="proxy_http_post",
    #         keywords=kwargs,
    #         params=parameters
    #         )

    # @force_default(defaults=["parameters"], default_types=["dict"])
    # def proxy_http_delete(self: object,
    #                       parameters: dict = None,
    #                       **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
    #     """Routes a DELETE request to NGSIEM.

    #     Keyword arguments:
    #     path -- LogScale path
    #     parameters -- Full parameters payload dictionary. Not required if using other keywords.

    #     This method only supports keywords for providing arguments.

    #     Returns: dict object containing API response.

    #     HTTP Method: DELETE

    #     Swagger URL

    #     """
    #     return process_service_request(
    #         calling_object=self,
    #         endpoints=Endpoints,
    #         operation_id="proxy_http_delete",
    #         keywords=kwargs,
    #         params=parameters
    #         )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def create_file(self: object,
                    parameters: dict = None,
                    **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a lookup file.

        Keyword arguments:
        file -- File to be uploaded
        name -- Name used to identify the file
        description -- File description
        id -- Unique identifier of the file being updated.
        repo -- Name of repository or view to save the file
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL

        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateFileV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_file(self: object,
                    parameters: dict = None,
                    **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a lookup file.

        Keyword arguments:
        id -- Unique identifier of the file being updated.
        description -- File description
        file -- File to be uploaded
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL

        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateFileV1",
            keywords=kwargs,
            params=parameters
            )

    UploadLookupV1 = upload_file
    GetLookupV1 = get_file
    GetLookupFromPackageWithNamespaceV1 = get_file_from_package_with_namespace
    GetLookupFromPackageV1 = get_file_from_package
    # StartSearchStreamingV1 = start_streaming_search
    StartSearchV1 = start_search
    GetSearchStatusV1 = get_search_status
    StopSearchV1 = stop_search
    CreateFileV1 = create_file
    UpdateFileV1 = update_file
