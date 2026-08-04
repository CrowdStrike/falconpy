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
# pylint: disable=C0302,R0904,R0912
from typing import Dict, Union
from requests import Response
from ._util import (
    force_default,
    process_service_request,
    generate_error_result,
    handle_single_argument
)
from ._payload import (
    ngsiem_search_payload,
    ngsiem_parser_payload,
    ngsiem_auto_update_policy_payload,
    ngsiem_install_parser_payload,
    ngsiem_bulk_install_parsers_payload,
    ngsiem_data_connection_payload,
    ngsiem_connector_config_payload,
    ngsiem_clone_parser_payload,
    bulk_create_dashboards_from_template_payload,
    bulk_create_lookup_files_payload,
    bulk_create_saved_queries_from_template_payload,
    bulk_update_dashboards_from_template_payload,
    bulk_update_lookup_files_payload,
    bulk_update_saved_queries_from_template_payload,
    create_parser_extension_payload,
    update_parser_extension_payload,
    add_dashboard_labels_payload,
    add_file_labels_payload,
    add_saved_query_labels_payload,
    bulk_add_dashboard_labels_payload,
    bulk_add_lookup_file_labels_payload,
    bulk_add_saved_query_labels_payload,
    bulk_remove_dashboard_labels_payload,
    bulk_remove_lookup_file_labels_payload,
    bulk_remove_saved_query_labels_payload,
    bulk_update_dashboard_labels_payload,
    bulk_update_lookup_file_labels_payload,
    bulk_update_saved_query_labels_payload,
    update_dashboard_labels_payload,
    update_file_labels_payload,
    update_saved_query_labels_payload,
    )
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

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UploadLookupV1

        Keyword arguments
        -----------------
        lookup_file : str
            File to be uploaded. Binary data.  (CSV format)
        repository : str
            Name of the repository.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("lookup_file", None):
            lookup_file = kwargs.get("lookup_file", None)
        else:
            lookup_file = kwargs.get("file", None)
        repository = kwargs.get("repository", None)
        if repository and lookup_file:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            try:
                with open(lookup_file, "rb") as upload_file:
                    # Create a multipart form payload for our upload file
                    file_extended = {"file": upload_file}
                    raw = process_service_request(calling_object=self,
                                                  endpoints=Endpoints,
                                                  operation_id="UploadLookupV1",
                                                  keywords=kwargs,
                                                  params=parameters,
                                                  repository=repository,
                                                  files=file_extended,
                                                  stream=True
                                                  )
                    # The humio upload API returns a plain text file ID
                    # instead of standard JSON. Parse the raw response
                    # and wrap it in the standard FalconPy result format.
                    if isinstance(raw, Response):
                        content_type = raw.headers.get("Content-Type", "")
                        if content_type.startswith("text/plain"):
                            returned = Result(status_code=raw.status_code,
                                              headers=raw.headers,
                                              body={"resources": [raw.content.decode("utf-8")]}
                                              ).full_return
                        else:
                            returned = Result(status_code=raw.status_code,
                                              headers=raw.headers,
                                              body=raw.json()
                                              ).full_return
                    else:
                        returned = raw
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
                 **kwargs) -> Union[Dict[str, Union[int, dict]], Result, Response]:
        """Download lookup file from NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/GetLookupV1

        Keyword arguments
        -----------------
        repository : str
            Name of the repository.
        filename : str
            Name of the lookup file.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        stream : bool
            Enable streaming download of the returned file.

        This method only supports keywords for providing arguments.

        Returns
        -------
        binary object on SUCCESS, dict object containing API response on FAILURE.
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
                filename=filename,
                stream=kwargs.get("stream", False)
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
                                             ) -> Union[Dict[str, Union[int, dict]], Result, Response]:
        """Download lookup file in namespaced package from NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /humio-auth-proxy/GetLookupFromPackageWithNamespaceV1

        Keyword arguments
        -----------------
        repository : str
            Name of repository.
        namespace : str
            Name of namespace.
        package : str
            Name of package.
        filename : str
            Name of lookup file.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        stream : bool
            Enable streaming download of the returned file.

        This method only supports keywords for providing arguments.

        Returns
        -------
        binary object on SUCCESS, dict object containing API response on FAILURE.
        """
        repository = kwargs.get("repository", False)
        filename = kwargs.get("filename", False)
        namespace = kwargs.get("namespace", False)
        package = kwargs.get("package", False)
        if min(repository, filename, namespace, package):
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
                package=package,
                stream=kwargs.get("stream", False)
                )
        else:
            returned = generate_error_result("You must provide a repository, namespace, package and"
                                             " filename argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_file_from_package(self: object,
                              parameters: dict = None,
                              **kwargs) -> Union[Dict[str, Union[int, dict]], Result, Response]:
        """Download lookup file in package from NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/GetLookupFromPackageV1

        Keyword arguments
        -----------------
        repository : str
            Name of repository.
        package : str
            Name of package.
        filename : str
            Name of lookup file.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        stream : bool
            Enable streaming download of the returned response.

        This method only supports keywords for providing arguments.

        Returns
        -------
        binary object on SUCCESS, dict object containing API response on FAILURE.
        """
        repository = kwargs.get("repository", None)
        filename = kwargs.get("filename", None)
        package = kwargs.get("package", None)
        if repository and filename and package:
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
                package=package,
                stream=kwargs.get("stream", False)
                )
        else:
            returned = generate_error_result("You must provide a repository, package and"
                                             " filename argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def start_search(self: object,
                     body: dict = None,
                     parameters: dict = None,
                     **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Initiate search.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/StartSearchV1

        Keyword arguments
        -----------------
        allow_event_skipping : bool
            Flag indicating if event skipping is allowed.
        arguments : dict
            Search arguments in JSON format.
        around : dict
            Search proximity arguments.
        autobucket_count : int
            Number of events per bucket.
        body : dict
            Full body payload as a JSON dictionary.
            Not required if using the search argument or other keywords.
                {
                    "allowEventSkipping": boolean,
                    "arguments": {},
                    "around": {
                        "eventId": "string",
                        "numberOfEventsAfter": integer,
                        "numberOfEventsBefore": integer,
                        "timestamp": integer
                    },
                    "autobucketCount": integer,
                    "end": "string",
                    "ingestEnd": "string",
                    "ingestStart": "string",
                    "isLive": boolean,
                    "queryString": "string",
                    "start": "string",
                    "timeZone": "string",
                    "timeZoneOffsetMinutes": integer,
                    "useIngestTime": boolean
                }
        end : str
            Last event limit.
        ingest_end : int
            Ingest maximum.
        ingest_start : int
            Ingest start.
        is_live : bool
            Flag indicating if this is a live search.
        parameters : dict
            Full parameters payload dictionary. Not required if using repository keyword.
        query_string : str
            Search query.
        repository : str (required)
            Name of repository.
        search : str
            Search to perform. JSON formatted string. Can be used instead of body.
            Not required if using other keywords.
            {
              "allowEventSkipping": boolean,
              "arguments": {},
              "around": {
                  "eventId": "string",
                  "numberOfEventsAfter": integer,
                  "numberOfEventsBefore": integer,
                  "timestamp": integer
              },
              "autobucketCount": integer,
              "end": "string",
              "ingestEnd": "string",
              "ingestStart": "string",
              "isLive": boolean,
              "queryString": "string",
              "start": "string",
              "timeZone": "string",
              "timeZoneOffsetMinutes": integer,
              "useIngestTime": boolean
            }
        start : str
            Search starting time range. Start.
        timezone : str
            Timezone applied to the search.
        timezone_offset_minutes : int
            Timezone offset.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        repository = kwargs.get("repository", None)
        search = kwargs.get("search", None) or body

        if not search:
            search = ngsiem_search_payload(kwargs)

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
                                             "arguments in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_search_status(self: object,
                          parameters: dict = None,
                          **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get status of search.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/GetSearchStatusV1

        Keyword arguments
        -----------------
        repository : str
            Name of repository.
        id : str
            ID of the query. String. Can be used instead of search_id keyword.
        search_id : str
            ID of the query. String. Can be used instead of id keyword.
        paginationLimit : int
            Optional pagination limit.
        paginationOffset : int
            Optional pagination offset.
        pagination_limit : int
            Optional pagination limit (alias for paginationLimit)
        pagination_offset : int
            Optional pagination offset (alias for paginationOffset)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        repository = kwargs.get("repository", None)
        search_id = kwargs.get("id", kwargs.get("search_id", None))
        # Allow pythonic aliasing for query string parameters (Issue #1383)
        if "pagination_limit" in kwargs and "paginationLimit" not in kwargs:
            kwargs["paginationLimit"] = kwargs.pop("pagination_limit")
        if "pagination_offset" in kwargs and "paginationOffset" not in kwargs:
            kwargs["paginationOffset"] = kwargs.pop("pagination_offset")
        if repository and search_id:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            if "id" in kwargs:
                kwargs.pop("id")
            if "search_id" in kwargs:
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
            returned = generate_error_result("You must provide a repository and id "
                                             "argument in order to use this operation."
                                             )

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def stop_search(self: object,
                    parameters: dict = None,
                    **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Stop search.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/humio-auth-proxy/StopSearchV1

        Keyword arguments
        -----------------
        repository : str
            Name of repository.
        id : str
            ID of the query. String. Can be used instead of search_id keyword.
        search_id : str
            ID of the query. String. Can be used instead of id keyword.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        repository = kwargs.get("repository", None)
        search_id = kwargs.get("id", kwargs.get("search_id", None))
        if repository and search_id:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            kwargs.pop("repository")
            if "id" in kwargs:
                kwargs.pop("id")
            if "search_id" in kwargs:
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
            returned = generate_error_result("You must provide a repository and id "
                                             "argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_dashboard_template(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Dashboard in NGSIEM as LogScale YAML Template.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/GetDashboardTemplate

        Keyword arguments
        -----------------
        ids : str or list[str]
            Dashboard ID value.
        search_domain : str
            Name of search domain (view or repo). String.
            Allowed options:
              all              falcon
              third-party      dashboards
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDashboardTemplate",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def create_dashboard_from_template(self: object,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Dashboard from LogScale YAML Template in NGSIEM.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/CreateDashboardFromTemplate

        Keyword arguments
        -----------------
        search_domain : str
            Name of search domain (view or repo). String.
            Allowed options:
              all
              falcon
              third-party
        name : str
            Name of the dashboard.
        yaml_template : bytes
            LogScale dashboard YAML template content, see schema at https://schemas.humio.com/
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        yaml_data = kwargs.get("yaml_template", None)
        file_extended = {}
        if kwargs.get("search_domain", None):
            file_extended["search_domain"] = kwargs.get("search_domain")
        if kwargs.get("name", None):
            file_extended["name"] = kwargs.get("name")
        if yaml_data:
            kwargs.pop("yaml_template", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="CreateDashboardFromTemplate",
                data=file_extended,
                files=[("yaml_template", (file_extended["name"], yaml_data))],
                params=parameters,
                keywords=kwargs
                )
        else:
            returned = generate_error_result("You must provide a YAML template to upload", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_dashboard_from_template(self: object,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Dashboard from LogScale YAML Template in NGSIEM.

        Please note a successful update will result in a new ID value being returned.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UpdateDashboardFromTemplate

        Keyword arguments
        -----------------
        search_domain : str
            Name of search domain (view or repo). String.
            Allowed options:
              all
              falcon
              third-party
        name : str
            Name of the dashboard.
        yaml_template : bytes
            LogScale dashboard YAML template content, see schema at https://schemas.humio.com/
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        yaml_data = kwargs.get("yaml_template", None)
        file_extended = {}
        if kwargs.get("search_domain", None):
            file_extended["search_domain"] = kwargs.get("search_domain")
        if kwargs.get("name", None):
            file_extended["name"] = kwargs.get("name")
        if yaml_data:
            kwargs.pop("yaml_template", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="UpdateDashboardFromTemplate",
                data=file_extended,
                files=[("yaml_template", (None, yaml_data))],
                params=parameters,
                keywords=kwargs
                )
        else:
            returned = generate_error_result("You must provide the dashboard template to update", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_dashboard(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete Dashboard in NGSIEM.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/DeleteDashboard

        Keyword arguments
        -----------------
        ids : str or list[str]
            Dashboard ID to be removed.
        search_domain : str
            name of search domain (view or repo). String.
            Allowed options:
              all
              falcon
              third-party
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteDashboard",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_lookup_file(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Lookup File in NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/GetLookupFile

        Keyword arguments
        -----------------
        filename : str
            Lookup file filename.
        search_domain : str
            Name of search domain (view or repo). String.
            Allowed options:
              all                  falcon
              third-party          dashboards
              parsers-repository
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetLookupFile",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def create_lookup_file(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Lookup File in NGSIEM.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/CreateLookupFile

        Keyword arguments
        -----------------
        search_domain : str
            Name of search domain (view or repo). String.
            Allowed options:
              all              falcon
              third-party      parsers-repository
        filename : str
            Filename of the lookup file to create.
        file : bytes
            File content to upload.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        file_name = kwargs.get("filename", None)
        file_data = kwargs.get("file", None)
        file_extended = {"search_domain": kwargs.get("search_domain", "all")}
        if file_name and file_data:
            kwargs.pop("file", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="CreateLookupFile",
                keywords=kwargs,
                params=parameters,
                data=file_extended,
                files=[("file", (file_name, file_data))]
                )
        else:
            returned = generate_error_result("You must provide the filename and file in order to use this method.", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_lookup_file(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Lookup File in NGSIEM.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UpdateLookupFile

        Keyword arguments
        -----------------
        search_domain : str
            Name of search domain (view or repo). String.
            Allowed options:
              all              falcon
              third-party      parsers-repository
        filename : str
            Filename of the lookup file to create.
        file : bytes
            File content to upload.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        file_name = kwargs.get("filename", None)
        file_data = kwargs.get("file", None)
        file_extended = {"search_domain": kwargs.get("search_domain", "all")}
        if file_name and file_data:
            kwargs.pop("file", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="UpdateLookupFile",
                keywords=kwargs,
                params=parameters,
                data=file_extended,
                files=[("file", (file_name, file_data))]
                )
        else:
            returned = generate_error_result("You must provide the filename and file in order to use this method.", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_lookup_file(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete Lookup File in NGSIEM.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/DeleteLookupFile

        Keyword arguments
        -----------------
        filename : str or list[str]
            Lookup file filename.
        search_domain : str
            Name of search domain (view or repo). String.
            Allowed options:
              all                  falcon
              third-party          dashboards
              parsers-repository
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteLookupFile",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def clone_parser(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Clone an existing parser with a new name.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/CloneParser

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "new_name": "string",
                    "source_id": "string"
                }
        new_name : str (required)
            The name for the cloned parser.
        source_id : str (required)
            The ID of the source parser to clone.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_clone_parser_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CloneParser",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def test_parser_from_template(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Test Parser from LogScale YAML Template in NGSIEM.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/TestParserFromTemplate

        Keyword arguments
        -----------------
        yaml_template : bytes
            LogScale Parser YAML template content, see schema at https://schemas.humio.com/
        schema_validation_enabled : bool
            When true, schema validation is enforced (CPS) and validates against Crowdstrike Parsing
            Standard.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        yaml_data = kwargs.get("yaml_template", None)
        if yaml_data:
            kwargs.pop("yaml_template", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="TestParserFromTemplate",
                files=[("yaml_template", (None, yaml_data))],
                params=parameters,
                keywords=kwargs
                )
        else:
            returned = generate_error_result("You must provide a YAML template to test.", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_parser_template(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Parser in NGSIEM as LogScale YAML Template.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/GetParserTemplate

        Keyword arguments
        -----------------
        ids : str
            Parser ID to retrieve.
        repository : str
            Name of repository. String.
            Allowed options: parsers-repository
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetParserTemplate",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def create_parser_from_template(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Parser from LogScale YAML Template in NGSIEM.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/CreateParserFromTemplate

        Keyword arguments
        -----------------
        repository : str
            Name of repository. String.
            Allowed options: parsers-repository
        name : str
            Name of the parser.
        yaml_template : bytes
            LogScale dashboard YAML template content, see schema at https://schemas.humio.com/
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        yaml_data = kwargs.get("yaml_template", None)
        file_extended = {}
        if kwargs.get("repository", None):
            file_extended["repository"] = kwargs.get("repository")
        if kwargs.get("name", None):
            file_extended["name"] = kwargs.get("name")
        if yaml_data:
            kwargs.pop("yaml_data", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="CreateParserFromTemplate",
                keywords=kwargs,
                params=parameters,
                data=file_extended,
                files=[("yaml_template", (file_extended["name"], yaml_data))]
                )
        else:
            returned = generate_error_result("You must provide a YAML template for the parser to upload", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_parser(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Parser in NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/GetParser

        Keyword arguments
        -----------------
        ids : str
            Parser ID to retrieve.
        repository : str
            Name of repository. String.
            Allowed options: parsers-repository
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetParser",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_parser(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Parser in NGSIEM.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/CreateParser

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "fields_to_be_removed_before_parsing": [
                        "string"
                    ],
                    "fields_to_tag": [
                        "string"
                    ],
                    "name": "string",
                    "repository": "string",
                    "script": "string",
                    "test_cases": [
                        {
                            "event": {
                                "raw_string": "string"
                            },
                            "output_assertions": [
                                {
                                    "assertions": {
                                        "fields_have_values": [
                                            {
                                                "expected_value": "string",
                                                "field_name": "string"
                                            }
                                        ],
                                        "fields_not_present": [
                                            "string"
                                        ]
                                    },
                                    "output_event_index": 0
                                }
                            ]
                        }
                    ]
                }
        fields_to_be_removed_before_parsing : str or list[str]
            List of fields to remove before parsing.
        fields_to_tag : str or list[str]
            List of fields to tag.
        name : str
            Parser name.
        repository : str
            Parser repository.
        script : str
            Parser script.
        test_cases : list[dict]
            List of test cases to apply to the parser.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_parser_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateParser",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_parser(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Parser in NGSIEM.

        Please note that name changes are not supported, but rather should be created as a new parser.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UpdateParser

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "fields_to_be_removed_before_parsing": [
                        "string"
                    ],
                    "fields_to_tag": [
                        "string"
                    ],
                    "name": "string",
                    "repository": "string",
                    "script": "string",
                    "test_cases": [
                        {
                            "event": {
                                "raw_string": "string"
                            },
                            "output_assertions": [
                                {
                                    "assertions": {
                                        "fields_have_values": [
                                            {
                                                "expected_value": "string",
                                                "field_name": "string"
                                            }
                                        ],
                                        "fields_not_present": [
                                            "string"
                                        ]
                                    },
                                    "output_event_index": 0
                                }
                            ]
                        }
                    ]
                }
        fields_to_be_removed_before_parsing : str or list[str]
            List of fields to remove before parsing.
        fields_to_tag : str or list[str]
            List of fields to tag.
        id : str
            ID of the parser to be updated.
        name : str
            Parser name.
        repository : str
            Parser repository.
        script : str
            Parser script.
        test_cases : list[dict]
            List of test cases to apply to the parser.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_parser_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateParser",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_parser_from_template(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Parser in NGSIEM from YAML Template.

        Please note that name changes are not supported, but rather should be
        created as a new parser.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UpdateParserFromTemplate

        Keyword arguments
        -----------------
        repository : str
            Name of repository. String.
            Allowed options: parsers-repository
        ids : str
            ID of the parser.
        yaml_template : bytes
            LogScale Parser YAML template content, see schema at https://schemas.humio.com/
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        yaml_data = kwargs.get("yaml_template", None)
        file_extended = {}
        if kwargs.get("repository", None):
            file_extended["repository"] = kwargs.get("repository")
        if kwargs.get("ids", None):
            file_extended["ids"] = kwargs.get("ids")
        if yaml_data:
            kwargs.pop("yaml_data", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="UpdateParserFromTemplate",
                keywords=kwargs,
                params=parameters,
                data=file_extended,
                files=[("yaml_template", (file_extended.get("ids", "parser"), yaml_data))]
                )
        else:
            returned = generate_error_result("You must provide a YAML template for the parser to upload", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_parser(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete Parser in NGSIEM.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/DeleteParser

        Keyword arguments
        -----------------
        ids : str
            Parser ID to be removed.
        repository : str
            Name of repository.
            Allowed options: parsers-repository
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteParser",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_parser_auto_update_policy(self: object,
                                         body: dict = None,
                                         **kwargs
                                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a parser auto update policy.

        Enables or disables auto-updates for parsers.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UpdateParserAutoUpdatePolicy

        Keyword arguments
        -----------------
        autoupdate_policy : str
            The auto update policy setting ('on' or 'off')
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "autoupdate_policy": "string",
                    "reason": "string"
                }
        reason : str
            Reason for changing the auto update policy.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_auto_update_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateParserAutoUpdatePolicy",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def install_parser(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Install a CrowdStrike-managed out-of-the-box (OOTB) parser.

        Provisions a pre-built parser with a specific version for the requesting customer ID (CID).
        The parser is installed as-is and cannot be modified by the customer.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/InstallParser

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "parser_id": "string",
                    "version": "string"
                }
        parser_id : str
            The unique identifier of the parser to install.
        version : str
            The version of the parser to install.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_install_parser_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="InstallParser",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_install_parsers(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Install multiple CrowdStrike-managed out-of-the-box (OOTB) parsers.

        Provisions multiple pre-built parsers with their specific versions for the requesting
        customer ID (CID). The parsers are installed as-is and cannot be modified by the customer.
        Maximum 100 parsers per request.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/BulkInstallParsers

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "parsers": [
                        {
                            "parser_id": "string",
                            "version": "string"
                        }
                    ]
                }
        parsers : list[dict]
            List of parser objects containing parser_id and version.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_bulk_install_parsers_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BulkInstallParsers",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_saved_query_template(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Saved Query in NGSIEM as LogScale YAML Template.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/GetSavedQueryTemplate

        Keyword arguments
        -----------------
        ids : str or list[str]
            Saved query ID to retrieve.
        search_domain : str
            Name of search domain (view or repo).
            Allowed options:
              all              falcon
              third-party      dashboards
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSavedQueryTemplate",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def create_saved_query(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a Saved Query from LogScale YAML Template in NGSIEM.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/CreateSavedQuery

        Keyword arguments
        -----------------
        search_domain : str
            Name of search domain (view or repo). String.
            Allowed options:
              all
              falcon
              third-party
        yaml_template : bytes
            LogScale saved query YAML template content, see schema at https://schemas.humio.com/
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        yaml_data = kwargs.get("yaml_template", None)
        file_extended = {}
        if kwargs.get("search_domain", None):
            file_extended["search_domain"] = kwargs.get("search_domain")
        if yaml_data:
            kwargs.pop("yaml_template", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="CreateSavedQuery",
                data=file_extended,
                files=[("yaml_template", (None, yaml_data))],
                params=parameters,
                keywords=kwargs
                )
        else:
            returned = generate_error_result("You must provide the YAML template in order to create a saved query.", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_saved_query_from_template(self: object,
                                         parameters: dict = None,
                                         **kwargs
                                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Saved Query from LogScale YAML Template in NGSIEM.

        Please note a successful update will result in a new ID value being returned.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UpdateSavedQueryFromTemplate

        Keyword arguments
        -----------------
        ids : str
            ID of the saved query to update.
        search_domain : str
            Name of search domain (view or repo). String.
            Allowed options:
              all
              falcon
              third-party
        yaml_template : bytes
            LogScale saved query YAML template content, see schema at https://schemas.humio.com/
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        yaml_data = kwargs.get("yaml_template", None)
        file_extended = {}
        if kwargs.get("search_domain", None):
            file_extended["search_domain"] = kwargs.get("search_domain")
        if yaml_data:
            kwargs.pop("yaml_template", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="UpdateSavedQueryFromTemplate",
                data=file_extended,
                files=[("yaml_template", (None, yaml_data))],
                params=parameters,
                keywords=kwargs
                )
        else:
            returned = generate_error_result("You must provide the YAML template in order to update a saved query.", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_saved_query(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete Saved Query in NGSIEM.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/DeleteSavedQuery

        Keyword arguments
        -----------------
        ids : str or list[str]
            Saved query ID to retrieve.
        search_domain : str
            Name of search domain (view or repo).
            Allowed options:
              all
              falcon
              third-party
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteSavedQuery",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_dashboards(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """List Dashboards in NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ListDashboards

        Keyword arguments
        -----------------
        limit : str
            Maximum number of results to return. Integer string. Default value: 50
        offset : str
            Number of results to offset the returned results by. Integer string. Default value: 0
        filter : str
            FQL filter to apply to the name of the content. String.
            Only currently support text match on name field: name:~'value'
        search_domain : str
            Name of search domain (view or repo).
            Allowed options:
              all              falcon
              third-party      dashboards
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ListDashboards",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_lookup_files(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """List Lookup Files in NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ListLookupFiles

        Keyword arguments
        -----------------
        limit : str
            Maximum number of results to return. Integer string. Default value: 50
        offset : str
            Number of results to offset the returned results by. Integer string. Default value: 0
        filter : str
            FQL filter to apply to the name of the content. String.
            Only currently support text match on name field: name:~'value'
        search_domain : str
            Name of search domain (view or repo).
            Allowed options:
              all              falcon
              third-party      dashboards
              parsers-repository
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ListLookupFiles",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_parsers(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """List Parsers in NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ListParsers

        Keyword arguments
        -----------------
        limit : str
            Maximum number of results to return. Integer string. Default value: 50
        offset : str
            Number of results to offset the returned results by. Integer string. Default value: 0
        filter : str
            FQL filter to apply to the name of the content. String.
            Only currently support text match on name field: name:~'value'
        repository : str
            Name of repository.
            Allowed options: parsers-repository
        update_available : str
            Filter parsers by update availability. String.
            Allowed values: true, false
        parser_type : str
            Filter parsers by type. String.
            Allowed values: ootb, custom
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ListParsers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_saved_queries(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Saved Queries in NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ListSavedQueries

        Keyword arguments
        -----------------
        limit : str
            Maximum number of results to return. Integer string. Default value: 50
        offset : str
            Number of results to offset the returned results by. Integer string. Default value: 0
        filter : str
            FQL filter to apply to the name of the content. String.
            Only currently support text match on name field: name:~'value'
        search_domain : str
            name of search domain (view or repo).
            Allowed options:
              all              falcon
              third-party      dashboards
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ListSavedQueries",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_lookup_file_entries(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update entries in an existing Lookup File in NGSIEM.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UpdateLookupFileEntries

        Keyword arguments
        -----------------
        search_domain : str
            name of search domain (view or repo)
        filename : str
            Filename of the lookup file to update.
        file : bytes
            The file content for updating or appending the entries.
        update_mode : str
            How to update the file entries. String.
            Available values:
                 append      update
        key_columns : str
            For update mode, the comma separated list of key columns to use when matching entries. String.
            (REQUIRED when update_mode=update)
        ignore_case : str
            For update mode, whether to ignore case when matching keys. String.
                           Available values:
                                true    false
            (REQUIRED when update_mode=update)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        file_name = kwargs.get("filename", None)
        file_data = kwargs.get("file", None)
        file_extended = {"search_domain": kwargs.get("search_domain", "all")}
        if file_name and file_data:
            kwargs.pop("file", None)
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="UpdateLookupFileEntries",
                keywords=kwargs,
                params=parameters,
                data=file_extended,
                files=[("file", (file_name, file_data))]
                )
        else:
            returned = generate_error_result("You must provide the filename and file in order to use this method.", code=400)

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_data_connections(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List and search data connections.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalListDataConnections

        Keyword arguments
        -----------------
        filter : str
            Optional filter criteria in FQL format.
        offset : int
            Starting position for pagination.
        limit : int
            Maximum number of items to return.
        sort : str
            Sort field and direction.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalListDataConnections",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_data_connectors(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """List available data connectors.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalListDataConnectors

        Keyword arguments
        -----------------
        filter : str
            Optional filter criteria in FQL format.
        offset : int
            Starting position for pagination.
        limit : int
            Maximum number of items to return.
        sort : str
            Sort field and direction.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalListDataConnectors",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_provisioning_status(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get data connection provisioning status.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalGetDataConnectionStatus

        Keyword arguments
        -----------------
        ids : str or list[str]
            Unique identifier of the data connection.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalGetDataConnectionStatus",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_connection_status(self: object,
                                 body: dict = None,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update data connection status.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalUpdateDataConnectionStatus

        Keyword arguments
        -----------------
        ids : str
            Unique identifier of the data connection.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "status": "string"
                }
        status : str
            The status of the data connection.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body["status"] = kwargs.get("status", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalUpdateDataConnectionStatus",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ingest_token(self: object,
                         *args,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Ingest token for data connection.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalGetDataConnectionToken

        Keyword arguments
        -----------------
        ids : str
            Unique identifier of the data connection.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalGetDataConnectionToken",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def regenerate_ingest_token(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Regenerate Ingest token for data connection.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalRegenerateDataConnectionToken

        Keyword arguments
        -----------------
        ids : str
            Unique identifier of the data connection.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalRegenerateDataConnectionToken",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_connection_by_id(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get data connection by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalGetDataConnectionByID

        Keyword arguments
        -----------------
        ids : str or list[str]
            Unique identifier of the data connection.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalGetDataConnectionByID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_data_connection(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new data connection.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalCreateDataConnection

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "config": {
                        "auth": {},
                        "name": "string",
                        "params": {}
                    },
                    "config_id": "string",
                    "connector_id": "string",
                    "connector_type": "string",
                    "custom": {
                        "additionalProp1": "string"
                    },
                    "description": "string",
                    "enable_host_enrichment": true,
                    "enable_user_enrichment": true,
                    "log_sources": [
                        "string"
                    ],
                    "name": "string",
                    "parser": "string",
                    "vendor_name": "string",
                    "vendor_product_name": "string"
                }
        config : dict
            Configuration settings for the data connection, including auth and params.
        config_id : str
            Identifier of the connector configuration to use.
        connector_id : str
            Identifier of the connector for this data connection.
        connector_type : str
            Type of the connector.
        custom : dict
            Custom properties for the data connection, such as connector-specific configuration
            keys (e.g., PluginConfigID). Dictionary of string key/value pairs.
        description : str
            Description of the data connection.
        enable_host_enrichment : bool
            Flag to enable host enrichment on ingested data.
        enable_user_enrichment : bool
            Flag to enable user enrichment on ingested data.
        log_sources : str or list[str]
            Log sources associated with this data connection.
        name : str
            Name of the data connection.
        parser : str
            Parser to use for processing ingested data.
        vendor_name : str
            Name of the vendor providing the data.
        vendor_product_name : str
            Name of the vendor product providing the data.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_data_connection_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalCreateDataConnection",
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_data_connection(self: object,
                               body: dict = None,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a data connection.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalUpdateDataConnection

        Keyword arguments
        -----------------
        ids : str
            Unique identifier of the data connection.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "config": {
                        "auth": {},
                        "name": "string",
                        "params": {}
                    },
                    "config_id": "string",
                    "description": "string",
                    "enable_host_enrichment": true,
                    "enable_user_enrichment": true,
                    "name": "string",
                    "parser": "string"
                }
        config : dict
            Configuration settings for the data connection, including auth and params.
        config_id : str
            Identifier of the connector configuration to use.
        description : str
            Description of the data connection.
        enable_host_enrichment : bool
            Flag to enable host enrichment on ingested data.
        enable_user_enrichment : bool
            Flag to enable user enrichment on ingested data.
        name : str
            Name of the data connection.
        parser : str
            Parser to use for processing ingested data.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_data_connection_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalUpdateDataConnection",
            body=body,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_data_connection(self: object,
                               *args,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a data connection.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalDeleteDataConnection

        Keyword arguments
        -----------------
        ids : str
            Unique identifier of the data connection.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalDeleteDataConnection",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_connector_configs(self: object,
                               *args,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List configurations for a data connector.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalListConnectorConfigs

        Keyword arguments
        -----------------
        ids : str
            Unique identifier of the data connector.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalListConnectorConfigs",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_connector_config(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new configuration for a data connector.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalCreateConnectorConfig

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "config": {
                        "auth": {},
                        "name": "string",
                        "params": {}
                    },
                    "connector_id": "string"
                }
        config : dict
            Configuration details for the connector including authentication and parameters.
        connector_id : str
            Unique identifier of the data connector.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_connector_config_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalCreateConnectorConfig",
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def patch_connector_config(self: object,
                               body: dict = None,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Patch configurations for a data connector.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalPatchConnectorConfig

        Keyword arguments
        -----------------
        ids : str
            Unique id of the config to update.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "config": {
                        "auth": {},
                        "name": "string",
                        "params": {}
                    },
                    "connector_id": "string"
                }
        config : dict
            Configuration details for the connector including authentication and parameters.
        connector_id : str
            Unique identifier of the data connector.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = ngsiem_connector_config_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalPatchConnectorConfig",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_connector_configs(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete data connection config.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/ExternalDeleteConnectorConfigs

        Keyword arguments
        -----------------
        connector_id : str
            Unique identifier of the connector.
        ids : str or list[str]
            Unique identifiers of the config(s) to delete.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExternalDeleteConnectorConfigs",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_create_dashboards_from_template(self: object,
                                             body: dict = None,
                                             **kwargs
                                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Multiple Dashboards from YAML Templates.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/BulkCreateDashboardsFromTemplate

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "dashboard_items": [
                        {
                            "name": "string",
                            "yaml_template": "string"
                        }
                    ],
                    "search_domain": "string"
                }
        dashboard_items : list
            List of dashboards to create.
        search_domain : str
            The name of the search domain where the dashboards will be created.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_create_dashboards_from_template_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BulkCreateDashboardsFromTemplate",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_create_lookup_files(self: object,
                                 body: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Multiple Lookup Files.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/BulkCreateLookupFiles

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "lookup_files": [
                        {
                            "content": "string",
                            "filename": "string"
                        }
                    ],
                    "search_domain": "string"
                }
        lookup_files : list
            List of lookup files to create.
        search_domain : str
            The name of the search domain where the lookup files will be created.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_create_lookup_files_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BulkCreateLookupFiles",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_create_saved_queries_from_template(self: object,
                                                body: dict = None,
                                                **kwargs
                                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create Multiple Saved Queries from LogScale YAML Templates.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/BulkCreateSavedQueriesFromTemplate

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "saved_query_items": [
                        {
                            "yaml_template": "string"
                        }
                    ],
                    "search_domain": "string"
                }
        saved_query_items : list
            List of saved queries to create.
        search_domain : str
            The name of the search domain where saved queries will be created.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_create_saved_queries_from_template_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BulkCreateSavedQueriesFromTemplate",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def bulk_get_lookup_files(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Multiple Lookup Files by Filenames in NGSIEM.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/BulkGetLookupFiles

        Keyword arguments
        -----------------
        filename : str or list[str]
            Lookup file filename(s) (required, multiple allowed)
        search_domain : str
            name of search domain (view or repo). Available values: all, falcon, third-party, dashboards,
            parsers-repository.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BulkGetLookupFiles",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_update_dashboards_from_template(self: object,
                                             body: dict = None,
                                             **kwargs
                                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Multiple Dashboards from YAML Templates.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/BulkUpdateDashboardsFromTemplate

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "dashboard_items": [
                        {
                            "id": "string",
                            "yaml_template": "string"
                        }
                    ],
                    "search_domain": "string"
                }
        dashboard_items : list
            Array of dashboards to update with their IDs and YAML templates.
        search_domain : str
            The name of the search domain containing the dashboards.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_update_dashboards_from_template_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BulkUpdateDashboardsFromTemplate",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_update_lookup_files(self: object,
                                 body: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Multiple Lookup Files.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/BulkUpdateLookupFiles

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "lookup_files": [
                        {
                            "content": "string",
                            "filename": "string"
                        }
                    ],
                    "search_domain": "string"
                }
        lookup_files : list
            List of lookup files to update.
        search_domain : str
            The name of the search domain containing the lookup files.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_update_lookup_files_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BulkUpdateLookupFiles",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_update_saved_queries_from_template(self: object,
                                                body: dict = None,
                                                **kwargs
                                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Multiple Saved Queries from LogScale YAML Templates.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/BulkUpdateSavedQueriesFromTemplate

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "saved_query_items": [
                        {
                            "id": "string",
                            "yaml_template": "string"
                        }
                    ],
                    "search_domain": "string"
                }
        saved_query_items : list
            Array of saved queries to update with their IDs and YAML templates.
        search_domain : str
            The name of the search domain containing the saved queries.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_update_saved_queries_from_template_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="BulkUpdateSavedQueriesFromTemplate",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_parser_extension(self: object,
                                body: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a Parser extension in NGSIEM for the provided base parser.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/CreateParserExtension

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "base_parser_id": "string",
                    "extension_name": "string",
                    "parser_id": "string",
                    "post_processing_script": "string",
                    "pre_processing_script": "string",
                    "test_cases": [
                        {
                            "event": {
                                "raw_string": "string"
                            },
                            "output_assertions": [
                                {
                                    "assertions": {
                                        "fields_have_values": [
                                            {
                                                "expected_value": "string",
                                                "field_name": "string"
                                            }
                                        ],
                                        "fields_not_present": [
                                            "string"
                                        ]
                                    },
                                    "output_event_index": 0
                                }
                            ]
                        }
                    ]
                }
        base_parser_id : str
            The base_parser_id value.
        extension_name : str
            The extension_name value.
        parser_id : str
            The parser_id value.
        post_processing_script : str
            The post_processing_script value.
        pre_processing_script : str
            The pre_processing_script value.
        test_cases : list
            The test_cases value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = create_parser_extension_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateParserExtension",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_parser_extension(self: object,
                                body: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing Parser extension in NGSIEM.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/UpdateParserExtension

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "extension_id": "string",
                    "post_processing_script": "string",
                    "pre_processing_script": "string",
                    "test_cases": [
                        {
                            "event": {
                                "raw_string": "string"
                            },
                            "output_assertions": [
                                {
                                    "assertions": {
                                        "fields_have_values": [
                                            {
                                                "expected_value": "string",
                                                "field_name": "string"
                                            }
                                        ],
                                        "fields_not_present": [
                                            "string"
                                        ]
                                    },
                                    "output_event_index": 0
                                }
                            ]
                        }
                    ]
                }
        extension_id : str
            The unique identifier of the parser extension to update.
        post_processing_script : str
            Optional - update postprocessing logic.
        pre_processing_script : str
            Optional - update preprocessing logic.
        test_cases : list
            Optional - update test cases.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_parser_extension_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateParserExtension",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_dashboard_labels(self: object,
                             body: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add multiple labels to a single dashboard.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/addDashboardLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "id": "string",
                    "labels": [
                        "string"
                    ],
                    "search_domain": "string"
                }
        id : str
            The unique identifier of the dashboard.
        labels : list
            The labels to add (max 10 labels, max 60 chars each)
        search_domain : str
            The search domain (view or repository) containing the dashboard.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = add_dashboard_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="addDashboardLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_file_labels(self: object,
                        body: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add multiple labels to a single file.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/addFileLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "filename": "string",
                    "labels": [
                        "string"
                    ],
                    "search_domain": "string"
                }
        filename : str
            The name of the lookup file.
        labels : list
            The labels to add (max 10 total labels per file, max 60 chars each)
        search_domain : str
            The search domain (view or repository) containing the file.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = add_file_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="addFileLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_saved_query_labels(self: object,
                               body: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add multiple labels to a saved query.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/addSavedQueryLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "id": "string",
                    "labels": [
                        "string"
                    ],
                    "search_domain": "string"
                }
        id : str
            The unique identifier of the saved query.
        labels : list
            The labels to add (max 10 labels, max 60 chars each)
        search_domain : str
            The search domain (view or repository) containing the saved query.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = add_saved_query_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="addSavedQueryLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_add_dashboard_labels(self: object,
                                  body: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add labels to multiple dashboards (max 100 items, non-transactional).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/bulkAddDashboardLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "items": [
                        {
                            "id": "string",
                            "labels": [
                                "string"
                            ]
                        }
                    ],
                    "search_domain": "string"
                }
        items : list
            List of dashboards with labels to add/remove/replace (max 100 items)
        search_domain : str
            The search domain (view or repository) containing the dashboards.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_add_dashboard_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="bulkAddDashboardLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_add_lookup_file_labels(self: object,
                                    body: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add labels to multiple lookup files (max 100 items, non-transactional).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/bulkAddLookupFileLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "items": [
                        {
                            "filename": "string",
                            "labels": [
                                "string"
                            ]
                        }
                    ],
                    "search_domain": "string"
                }
        items : list
            List of files with labels to add/remove/replace (max 100 items)
        search_domain : str
            The search domain (view or repository) containing the files.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_add_lookup_file_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="bulkAddLookupFileLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_add_saved_query_labels(self: object,
                                    body: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add labels to multiple saved queries (max 100 items, non-transactional).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/bulkAddSavedQueryLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "items": [
                        {
                            "id": "string",
                            "labels": [
                                "string"
                            ]
                        }
                    ],
                    "search_domain": "string"
                }
        items : list
            List of saved queries with labels to add/remove/replace (max 100 items)
        search_domain : str
            The search domain (view or repository) containing the saved queries.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_add_saved_query_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="bulkAddSavedQueryLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_remove_dashboard_labels(self: object,
                                     body: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove labels from multiple dashboards (max 100 items, non-transactional).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/bulkRemoveDashboardLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "items": [
                        {
                            "id": "string",
                            "labels": [
                                "string"
                            ]
                        }
                    ],
                    "search_domain": "string"
                }
        items : list
            List of dashboards with labels to add/remove/replace (max 100 items)
        search_domain : str
            The search domain (view or repository) containing the dashboards.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_remove_dashboard_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="bulkRemoveDashboardLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_remove_lookup_file_labels(self: object,
                                       body: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove labels from multiple lookup files (max 100 items, non-transactional).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/bulkRemoveLookupFileLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "items": [
                        {
                            "filename": "string",
                            "labels": [
                                "string"
                            ]
                        }
                    ],
                    "search_domain": "string"
                }
        items : list
            List of files with labels to add/remove/replace (max 100 items)
        search_domain : str
            The search domain (view or repository) containing the files.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_remove_lookup_file_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="bulkRemoveLookupFileLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_remove_saved_query_labels(self: object,
                                       body: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove labels from multiple saved queries (max 100 items, non-transactional).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/bulkRemoveSavedQueryLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "items": [
                        {
                            "id": "string",
                            "labels": [
                                "string"
                            ]
                        }
                    ],
                    "search_domain": "string"
                }
        items : list
            List of saved queries with labels to add/remove/replace (max 100 items)
        search_domain : str
            The search domain (view or repository) containing the saved queries.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_remove_saved_query_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="bulkRemoveSavedQueryLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_update_dashboard_labels(self: object,
                                     body: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Replace all labels on multiple dashboards (max 100 items, non-transactional).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/bulkUpdateDashboardLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "items": [
                        {
                            "id": "string",
                            "labels": [
                                "string"
                            ]
                        }
                    ],
                    "search_domain": "string"
                }
        items : list
            List of dashboards with labels to add/remove/replace (max 100 items)
        search_domain : str
            The search domain (view or repository) containing the dashboards.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_update_dashboard_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="bulkUpdateDashboardLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_update_lookup_file_labels(self: object,
                                       body: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Replace all labels on multiple lookup files (max 100 items, non-transactional).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/bulkUpdateLookupFileLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "items": [
                        {
                            "filename": "string",
                            "labels": [
                                "string"
                            ]
                        }
                    ],
                    "search_domain": "string"
                }
        items : list
            List of files with labels to add/remove/replace (max 100 items)
        search_domain : str
            The search domain (view or repository) containing the files.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_update_lookup_file_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="bulkUpdateLookupFileLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_update_saved_query_labels(self: object,
                                       body: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Replace all labels on multiple saved queries (max 100 items, non-transactional).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/bulkUpdateSavedQueryLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "items": [
                        {
                            "id": "string",
                            "labels": [
                                "string"
                            ]
                        }
                    ],
                    "search_domain": "string"
                }
        items : list
            List of saved queries with labels to add/remove/replace (max 100 items)
        search_domain : str
            The search domain (view or repository) containing the saved queries.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = bulk_update_saved_query_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="bulkUpdateSavedQueryLabels",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def remove_dashboard_labels(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove multiple labels from a single dashboard.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/removeDashboardLabels

        Keyword arguments
        -----------------
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="removeDashboardLabels",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def remove_file_labels(self: object,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove multiple labels from a single file.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/removeFileLabels

        Keyword arguments
        -----------------
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="removeFileLabels",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def remove_saved_query_labels(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove multiple labels from a saved query.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/removeSavedQueryLabels

        Keyword arguments
        -----------------
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="removeSavedQueryLabels",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_dashboard_labels(self: object,
                                body: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Replace all labels on a single dashboard.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/updateDashboardLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "id": "string",
                    "labels": [
                        "string"
                    ],
                    "search_domain": "string"
                }
        id : str
            The unique identifier of the dashboard.
        labels : list
            The new labels (replaces all existing, max 10 labels, max 60 chars each)
        search_domain : str
            The search domain (view or repository) containing the dashboard.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_dashboard_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateDashboardLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_file_labels(self: object,
                           body: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Replace all labels on a single file.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/updateFileLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "filename": "string",
                    "labels": [
                        "string"
                    ],
                    "search_domain": "string"
                }
        filename : str
            The name of the lookup file.
        labels : list
            The new labels (replaces all existing labels, max 10 labels, max 60 chars each)
        search_domain : str
            The search domain (view or repository) containing the file.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_file_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateFileLabels",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_saved_query_labels(self: object,
                                  body: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Replace all labels on a single saved query.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ngsiem/updateSavedQueryLabels

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "id": "string",
                    "labels": [
                        "string"
                    ],
                    "search_domain": "string"
                }
        id : str
            The unique identifier of the saved query.
        labels : list
            The new labels (replaces all existing labels, max 10 labels, max 60 chars each)
        search_domain : str
            The search domain (view or repository) containing the saved query.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_saved_query_labels_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateSavedQueryLabels",
            body=body
            )

    addDashboardLabels = add_dashboard_labels
    addFileLabels = add_file_labels
    addSavedQueryLabels = add_saved_query_labels
    bulkAddDashboardLabels = bulk_add_dashboard_labels
    bulkAddLookupFileLabels = bulk_add_lookup_file_labels
    bulkAddSavedQueryLabels = bulk_add_saved_query_labels
    BulkCreateDashboardsFromTemplate = bulk_create_dashboards_from_template
    BulkCreateLookupFiles = bulk_create_lookup_files
    BulkCreateSavedQueriesFromTemplate = bulk_create_saved_queries_from_template
    BulkGetLookupFiles = bulk_get_lookup_files
    bulkRemoveDashboardLabels = bulk_remove_dashboard_labels
    bulkRemoveLookupFileLabels = bulk_remove_lookup_file_labels
    bulkRemoveSavedQueryLabels = bulk_remove_saved_query_labels
    bulkUpdateDashboardLabels = bulk_update_dashboard_labels
    BulkUpdateDashboardsFromTemplate = bulk_update_dashboards_from_template
    bulkUpdateLookupFileLabels = bulk_update_lookup_file_labels
    BulkUpdateLookupFiles = bulk_update_lookup_files
    BulkUpdateSavedQueriesFromTemplate = bulk_update_saved_queries_from_template
    bulkUpdateSavedQueryLabels = bulk_update_saved_query_labels
    CreateParserExtension = create_parser_extension
    removeDashboardLabels = remove_dashboard_labels
    removeFileLabels = remove_file_labels
    removeSavedQueryLabels = remove_saved_query_labels
    updateDashboardLabels = update_dashboard_labels
    updateFileLabels = update_file_labels
    UpdateParserExtension = update_parser_extension
    updateSavedQueryLabels = update_saved_query_labels
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
