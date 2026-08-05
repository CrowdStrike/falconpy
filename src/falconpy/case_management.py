"""CrowdStrike Falcon CaseManagement API interface class.

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
# pylint: disable=C0302
from typing import Dict, Union
from ._result import Result
from ._service_class import ServiceClass
from ._util import force_default, process_service_request, generate_error_result, handle_single_argument
from ._payload import entities_merge_post_v1_payload
from ._endpoint._case_management import _case_management_endpoints as Endpoints
from ._payload._case_management import (
    case_management_notification_groups_payload,
    case_management_create_notification_payload,
    case_management_sla_payload,
    case_management_template_payload,
    case_management_file_ids_payload,
    case_management_rtr_file_metadata_payload,
    case_management_rtr_file_payload,
    case_management_rtr_recent_file_payload,
    specified_case_payload,
    case_manage_payload,
    case_evidence_payload,
    update_case_payload
    )


# pylint: disable=R0904
class CaseManagement(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials.
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py).
    - a valid token provided by the authentication service class (oauth2.py).
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregates_file_details_post_v1(self: object,
                                        parameters: dict = None,
                                        **kwargs
                                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get file details aggregates as specified via json in the request body.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/aggregates.file-details.post.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs. String or a.
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
        filter : str
            FQL filter expression.
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
            operation_id="aggregates_file_details_post_v1",
            keywords=kwargs,
            params=parameters,
            body={}
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_file_details(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query file details.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/combined.file-details.get.v1

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        limit : int
            Page size.
        offset : int
            Page offset.
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
            operation_id="combined_file_details_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_file_details(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get file details by id.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/entities.file-details.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
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
            operation_id="entities_file_details_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_file_details(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update file details.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/entities.file-details.patch.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "description": "string",
                    "id": "string"
                }
        description : str
            File details update desecription.
        id : str
            File details ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            keys = ["description", "id"]
            for key in keys:
                if kwargs.get(key, None) is not None:
                    body[key] = kwargs.get(key, None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_file_details_patch_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def bulk_download_files(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download multiple existing file from case as a ZIP.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/entities.files_bulk-download.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            List of files to download.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_file_ids_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_files_bulk_download_post_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def download_existing_files(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download existing file from case.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/entities.files_download.get.v1

        Keyword arguments
        -----------------
        id : str
            Resource ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_files_download_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def upload_file(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Upload file for case.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/entities.files_upload.post.v1

        Keyword arguments
        -----------------
        file : str
            Local file to Upload.
        description : str
            Description of the file.
        case_id : str
            Case ID for the file.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        file = kwargs.get("file", None)
        if file:
            try:
                with open(file, "rb") as upload_file:
                    # Create a multipart form payload for our upload file
                    file_extended = {"file": upload_file}
                    # case_id and description are formData fields, not query params.
                    # Pass them via data= so they're sent as multipart form data.
                    data_fields = {}
                    if kwargs.get("case_id", None):
                        data_fields["case_id"] = kwargs.get("case_id")
                    if kwargs.get("description", None):
                        data_fields["description"] = kwargs.get("description")
                    returned = process_service_request(calling_object=self,
                                                       endpoints=Endpoints,
                                                       operation_id="entities_files_upload_post_v1",
                                                       params=parameters,
                                                       files=file_extended,
                                                       data=data_fields
                                                       )
            except FileNotFoundError:
                returned = generate_error_result("Invalid upload file specified.")
        else:
            returned = generate_error_result("You must provide a file "
                                             "argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_file_details(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete file details by id.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/entities.files.delete.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_files_delete_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_file_detail_ids(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for ids of file details.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/queries.file-details.get.v1

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        limit : int
            Page size.
        offset : int
            Page offset.
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
            operation_id="queries_file_details_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_rtr_file_metadata(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get metadata for a file via RTR without retrieving it.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/entities.get-rtr-file-metadata.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "aid": "string",
                    "file_path": "string"
                }
        aid : str
            The agent ID of the host to retrieve file metadata from.
        file_path : str
            The path to the file on the host.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_rtr_file_metadata_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_get_rtr_file_metadata_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def retrieve_rtr_file(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a file from host using RTR and add it to a case.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/entities.retrieve-rtr-file.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "aid": "string",
                    "case_id": "string",
                    "description": "string",
                    "file_path": "string"
                }
        aid : str
            The agent ID of the host to retrieve the file from.
        case_id : str
            The ID of the case to add the file to.
        description : str
            A description of the file being retrieved.
        file_path : str
            The path to the file on the host.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_rtr_file_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_retrieve_rtr_file_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def retrieve_rtr_recent_file(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a recently fetched RTR file and add it to a case.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-files/entities.retrieve-rtr-recent-file.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "aid": "string",
                    "case_id": "string",
                    "description": "string",
                    "session_id": "string",
                    "sha256": "string"
                }
        aid : str
            The agent ID of the host.
        case_id : str
            The ID of the case to add the file to.
        description : str
            A description of the file being retrieved.
        session_id : str
            The RTR session ID for the file retrieval.
        sha256 : str
            The SHA256 hash of the file to retrieve.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_rtr_recent_file_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_retrieve_rtr_recent_file_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_notification_groups_aggregation(self: object,
                                            body: dict = None,
                                            **kwargs
                                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get notification groups aggregations.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/aggregates.notification-groups.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "name": "string",
                        "size": 0,
                        "sort": "string",
                        "type": "terms"
                    }
                ]
        date_ranges : list[dict]
            Date range timeframe.
        field : str
            Field to aggregate on.
        filter : str
            Filter criteria in the form of an FQL query.
        from : int
            Starting index of overall result set.
        name : str
            Name of the aggregation.
        size : int
            Maximum number of records to return.
        sort : str
            The field to sort on.
        type : str
            Type of aggregation to perform.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_notification_groups_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregates_notification_groups_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_notification_groups_aggregation_v2(self: object,
                                               body: dict = None,
                                               **kwargs
                                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get notification groups aggregations.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/aggregates.notification-groups.post.v2

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "name": "string",
                        "size": 0,
                        "sort": "string",
                        "type": "terms"
                    }
                ]
        date_ranges : list[dict]
            Date range timeframe.
        field : str
            Field to aggregate on.
        filter : str
            Filter criteria in the form of an FQL query.
        from : int
            Starting index of overall result set.
        name : str
            Name of the aggregation.
        size : int
            Maximum number of records to return.
        sort : str
            The field to sort on.
        type : str
            Type of aggregation to perform.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_notification_groups_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregates_notification_groups_post_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_sla_aggregations(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get SLA aggregations.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/aggregates.slas.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "name": "string",
                        "size": 0,
                        "sort": "string",
                        "type": "terms"
                    }
                ]
        date_ranges : list[dict]
            Date range timeframe.
        field : str
            Field to aggregate on.
        filter : str
            Filter criteria in the form of an FQL query.
        from : int
            Starting index of overall result set.
        name : str
            Name of the aggregation.
        size : int
            Maximum number of records to return.
        sort : str
            The field to sort on.
        type : str
            Type of aggregation to perform.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_notification_groups_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregates_slas_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_template_aggregations(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get templates aggregations.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/aggregates.templates.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "name": "string",
                        "size": 0,
                        "sort": "string",
                        "type": "terms"
                    }
                ]
        date_ranges : list[dict]
            Date range timeframe.
        field : str
            Field to aggregate on.
        filter : str
            Filter criteria in the form of an FQL query.
        from : int
            Starting index of overall result set.
        name : str
            Name of the aggregation.
        size : int
            Maximum number of records to return.
        sort : str
            The field to sort on.
        type : str
            Type of aggregation to perform.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_notification_groups_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregates_templates_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_access_tag_aggregations(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get access tag aggregates.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/aggregates.access-tags.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "name": "string",
                        "size": 0,
                        "sort": "string",
                        "type": "terms"
                    }
                ]
        date_ranges : list[dict]
            Date range timeframe.
        field : str
            Field to aggregate on.
        filter : str
            Filter criteria in the form of an FQL query.
        from : int
            Starting index of overall result set.
        name : str
            Name of the aggregation.
        size : int
            Maximum number of records to return.
        sort : str
            The field to sort on.
        type : str
            Type of aggregation to perform.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_notification_groups_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregates_access_tags_post_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_access_tags(self: object,
                        *args,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get access tags.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.access-tags.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
        with_has_access : bool
            Evaluate FGAC and return has_access property.
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
            operation_id="entities_access_tags_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_fields(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get fields by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.fields.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
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
            operation_id="entities_fields_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notification_groups(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get notification groups by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.notification-groups.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
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
            operation_id="entities_notification_groups_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_notification_group(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create notification group.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.notification-groups.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "channels": [
                        {
                            "config_id": "string",
                            "config_name": "string",
                            "recipients": [
                                "string"
                            ],
                            "severity": "string",
                            "type": "email"
                        }
                    ],
                    "description": "string",
                    "name": "string"
                }
        channels : list[dict]
            The notification group channel configuration parameters.
        description : str
            Notification group description.
        name : str
            Notification group name.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_create_notification_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_notification_groups_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_notification_group(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update notification group.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.notification-groups.patch.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "channels": [
                        {
                        "config_id": "string",
                        "config_name": "string",
                        "recipients": [
                            "string"
                        ],
                        "severity": "string",
                        "type": "email"
                        }
                    ],
                    "description": "string",
                    "id": "string",
                    "name": "string"
                }
        channels : list[dict]
            The notification group channel configuration parameters.
        description : str
            Notification group description.
        id : str
            The ID of the notification group.
        name : str
            Notification group name.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_create_notification_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_notification_groups_patch_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_notification_group(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete notification groups by ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.notification-groups.delete.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
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
            operation_id="entities_notification_groups_delete_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_notification_groups_v2(self: object,
                                   *args,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get notification groups by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.notification-groups.get.v2

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
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
            operation_id="entities_notification_groups_get_v2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_notification_group_v2(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create notification group.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.notification-groups.post.v2

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "channels": [
                        {
                        "config_id": "string",
                        "config_name": "string",
                        "params": {},
                        "type": "email"
                        }
                    ],
                    "description": "string",
                    "name": "string"
                }
        channels : list[dict]
            The notification group channel configuration parameters.
        description : str
            Notification group description.
        name : str
            Notification group name.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_create_notification_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_notification_groups_post_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_notification_group_v2(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update notification group.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.notification-groups.patch.v2

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "channels": [
                        {
                        "config_id": "string",
                        "config_name": "string",
                        "params": {},
                        "type": "email"
                        }
                    ],
                    "description": "string",
                    "id": "string",
                    "name": "string"
                }
        channels : list[dict]
            The notification group channel configuration parameters.
        description : str
            Notification group description.
        id : str
            The ID of the notification group.
        name : str
            Notification group name.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_create_notification_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_notification_groups_patch_v2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_notification_group_v2(self: object,
                                     *args,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete notification groups by ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.notification-groups.delete.v2

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
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
            operation_id="entities_notification_groups_delete_v2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_slas(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get SLAs by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.slas.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
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
            operation_id="entities_slas_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_sla(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create SLA.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.slas.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "description": "string",
                    "goals": [
                        {
                        "duration_seconds": 0,
                        "escalation_policy": {
                            "steps": [
                            {
                                "escalate_after_seconds": 0,
                                "notification_group_id": "string"
                            }
                            ]
                        },
                        "type": "string"
                        }
                    ],
                    "name": "string"
                }
        description : str
            The description of the SLA.
        goals : list[dict]
            The SLA goals.
        name : str
            The name of the SLA.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_sla_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_slas_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_sla(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update SLA.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.slas.patch.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "description": "string",
                    "goals": [
                        {
                        "duration_seconds": 0,
                        "escalation_policy": {
                            "steps": [
                            {
                                "escalate_after_seconds": 0,
                                "notification_group_id": "string"
                            }
                            ]
                        },
                        "type": "string"
                        }
                    ],
                    "name": "string"
                }
        description : str
            The description of the SLA.
        goals : list[dict]
            The SLA goals.
        name : str
            The name of the SLA.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_sla_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_slas_patch_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_sla(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete SLAs.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.slas.delete.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
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
            operation_id="entities_slas_delete_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_template_snapshots(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get template snapshots.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.template-snapshots.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Snapshot IDs.
        template_ids : str or list[str]
            Retrieves the latest snapshot for all Template IDs.
        versions : str or list[str]
            Retrieve a specific version of the template from the parallel array `template_ids`.
            A value of zero will return the latest snapshot.
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
            operation_id="entities_template_snapshots_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def export_templates(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Export templates to files in a zip archive.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.templates_export.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Template IDs.
        filter : str
            FQL filter expression.
        format : str
            Export file format.
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
            operation_id="entities_templates_export_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def import_template(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Import a template from a file.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.templates_import.post.v1

        Keyword arguments
        -----------------
        file : bytes
            Local file.
        dry_run : bool
            Run validation only.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        file = kwargs.get("file", None)
        if file:
            # Pop the path variables from the keywords dictionary
            # before processing query string arguments.
            try:
                with open(file, "rb") as upload_file:
                    # Create a multipart form payload for our upload file
                    file_extended = {"file": upload_file}
                    returned = process_service_request(calling_object=self,
                                                       endpoints=Endpoints,
                                                       operation_id="entities_templates_import_post_v1",
                                                       keywords=kwargs,
                                                       params=parameters,
                                                       files=file_extended
                                                       )
            except FileNotFoundError:
                returned = generate_error_result("Invalid upload file specified.")
        else:
            returned = generate_error_result("You must provide a file "
                                             "argument in order to use this operation."
                                             )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_templates(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get templates by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.templates.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
        with_has_access : bool
            Evaluate FGAC and return has_access property.
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
            operation_id="entities_templates_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_template(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create template.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.templates.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "description": "string",
                    "fields": [
                        {
                        "data_type": "string",
                        "default_value": "string",
                        "input_type": "string",
                        "multivalued": true,
                        "name": "string",
                        "options": [
                            {
                            "value": "string"
                            }
                        ],
                        "required": true
                        }
                    ],
                    "name": "string",
                    "sla_id": "string"
                }
        description : str
            The description of the template.
        fields : list[dict]
            The fields required to create a template.
        name : str
            The name of the template.
        sla_id : str
            The ID of the SLA.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_template_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_templates_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_template(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update template.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.templates.patch.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "description": "string",
                    "fields": [
                        {
                        "data_type": "string",
                        "default_value": "string",
                        "id": "string",
                        "input_type": "string",
                        "multivalued": true,
                        "name": "string",
                        "options": [
                            {
                            "id": "string",
                            "value": "string"
                            }
                        ],
                        "required": true
                        }
                    ],
                    "id": "string",
                    "name": "string",
                    "sla_id": "string"
                }
        description : str
            The description of the template.
        fields : list[dict]
            The fields required to create a template.
        id : str
            The ID of the template to update.
        name : str
            The name of the template.
        sla_id : str
            The ID of the SLA.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_template_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_templates_patch_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_templates(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete templates.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities.templates.delete.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            Resource IDs.
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
            operation_id="entities_templates_delete_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_access_tags(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query access tags.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/queries.access-tags.get.v1

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        sort : str
            Sort expression.
        limit : int
            Page size.
        after : str
            Pagination token.
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
            operation_id="queries_access_tags_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_fields(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query fields.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/queries.fields.get.v1

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        limit : int
            Page size.
        offset : int
            Page offset.
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
            operation_id="queries_fields_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_notification_groups(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query notification groups.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/queries.notification-groups.get.v1

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        sort : str
            Sort expression.
        limit : int
            Page size.
        offset : int
            Page offset.
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
            operation_id="queries_notification_groups_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_notification_groups_v2(self: object,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query notification groups.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/queries.notification-groups.get.v2

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        sort : str
            Sort expression.
        limit : int
            Page size.
        offset : int
            Page offset.
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
            operation_id="queries_notification_groups_get_v2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_slas(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query SLAs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/queries.slas.get.v1

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        sort : str
            Sort expression.
        limit : int
            Page size.
        offset : int
            Page offset.
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
            operation_id="queries_slas_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_template_snapshots(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query template snapshots.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/queries.template-snapshots.get.v1

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        limit : int
            Page size.
        offset : int
            Page offset.
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
            operation_id="queries_template_snapshots_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_templates(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query templates.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/queries.templates.get.v1

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        sort : str
            Sort expression.
        limit : int
            Page size.
        offset : int
            Page offset.
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
            operation_id="queries_templates_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_case_alert_evidence(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add the given list of alert evidence to the specified case.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cases/entities.alert-evidence.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "alerts": [
                        {
                        "id": "string"
                        }
                    ],
                    "id": "string"
                }
        alerts : list
            The alert IDs.
        id : str
            The specified case ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = specified_case_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_alert_evidence_post_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_case_tags(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add the given list of tags to the specified case.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cases/entities.case-tags.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "id": "string",
                    "tags": [
                        "string"
                    ]
                }
        id : str
            The specified case ID.
        tags : str or list[str]
            The given list of tags.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = specified_case_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_case_tags_post_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_case_tags(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove the specified tags from the specified case.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cases/entities.case-tags.delete.v1

        Keyword arguments
        -----------------
        id : str
            The ID of the case to remove tags from.
        tag : str or list[str]
            The tag to remove from the case.
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
            operation_id="entities_case_tags_delete_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_case(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create the given Case.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cases/entities.cases.put.v2

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "assigned_to_user_uuid": "string",
                    "description": "string",
                    "evidence": {
                        "alerts": [
                        {
                            "id": "string"
                        }
                        ],
                        "events": [
                        {
                            "id": "string"
                        }
                        ],
                        "leads": [
                        {
                            "id": "string"
                        }
                        ]
                    },
                    "name": "string",
                    "severity": 0,
                    "status": "string",
                    "tags": [
                        "string"
                    ],
                    "template": {
                        "id": "string"
                    }
                }
        assigned_to_user_uuid : str
            UUID of the user to assign the case to.
        description : str
            The description of the case.
        evidence : dict
            The case evidence info.
        name : str
            The name of the case.
        severity : int
            The severity level of the case.
        status : str
            The current status of the case.
        tags : str or list[str]
            The tags to be attached to the case.
        template : dict
            The template case to utilize.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_manage_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_cases_put_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_cases(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve all Cases given their IDs.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cases/entities.cases.post.v2

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "ids": [
                        "string"
                    ]
                }



        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_management_file_ids_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_cases_post_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_case_fields(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update given fields on the specified case.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cases/entities.cases.patch.v2

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "expected_consistency_version": 0,
                    "expected_version": 0,
                    "fields": {
                        "assigned_to_user_uuid": "string",
                        "custom_fields": [
                        {
                            "id": "string",
                            "values": [
                            "string"
                            ]
                        }
                        ],
                        "description": "string",
                        "name": "string",
                        "remove_user_assignment": true,
                        "severity": 0,
                        "slas_active": true,
                        "status": "string",
                        "template": {
                        "id": "string"
                        }
                    },
                    "id": "string"
                }
        expected_consistency_version : int
            The consistency version.
        expected_version : int
            The version.
        fields : dict
            The updated given fields for the specified case.
        id : str
            The specified case ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_case_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_cases_patch_v2",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_case_event_evidence(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add the given list of event evidence to the specified case.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cases/entities.event-evidence.post.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "events": [
                        {
                        "id": "string"
                        }
                    ],
                    "id": "string"
                }
        events : list[dict]
            The event evidence field.
        id : str
            The specified case ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = case_evidence_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_event_evidence_post_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_case_ids(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve all Cases IDs that match a given query.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cases/queries.cases.get.v1

        Keyword arguments
        -----------------
        limit : int
            The maximum number of Cases to return in this response (default: 100; max: 10000). Integer.
            Use this parameter together with the `offset` parameter to manage pagination of the results.
        offset : int
            The first case to return, where `0` is the latest case. Integer.
            Use with the `offset` parameter to manage pagination of results.
        sort : str
            The field to sort on. Sort parameter takes the form <field|direction>. String.
            The sorting fields can be any keyword field that is part of #domain.Case except for the text based fields.
            If the fields are missing from the Cases, the service will fallback to its default ordering.
        filter : str
            FQL filter expression. String.
            Filter fields can be any keyword field that is part of #domain.Case.
        q : str
            Search all Case metadata for the provided.
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
            operation_id="queries_cases_get_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def entities_merge_post_v1(self: object,
                               body: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Merge a source case into a destination case.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/case-management/entities_merge_post_v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "destination_id": "string",
                    "source_id": "string"
                }
        destination_id : str
            The destination_id value.
        source_id : str
            The source_id value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = entities_merge_post_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entities_merge_post_v1",
            body=body
            )

    aggregates_file_details_post_v1 = aggregates_file_details_post_v1
    combined_file_details_get_v1 = query_file_details
    entities_file_details_get_v1 = get_file_details
    entities_file_details_patch_v1 = update_file_details
    entities_files_bulk_download_post_v1 = bulk_download_files
    entities_files_download_get_v1 = download_existing_files
    entities_files_upload_post_v1 = upload_file
    entities_files_delete_v1 = delete_file_details
    queries_file_details_get_v1 = query_file_detail_ids
    entities_get_rtr_file_metadata_post_v1 = get_rtr_file_metadata
    entities_retrieve_rtr_file_post_v1 = retrieve_rtr_file
    entities_retrieve_rtr_recent_file_post_v1 = retrieve_rtr_recent_file
    aggregates_notification_groups_post_v1 = get_notification_groups_aggregation
    aggregates_notification_groups_post_v2 = get_notification_groups_aggregation_v2
    aggregates_slas_post_v1 = get_sla_aggregations
    aggregates_templates_post_v1 = get_template_aggregations
    aggregates_access_tags_post_v1 = get_access_tag_aggregations
    entities_access_tags_get_v1 = get_access_tags
    entities_fields_get_v1 = get_fields
    entities_notification_groups_get_v1 = get_notification_groups
    entities_notification_groups_post_v1 = create_notification_group
    entities_notification_groups_patch_v1 = update_notification_group
    entities_notification_groups_delete_v1 = delete_notification_group
    entities_notification_groups_get_v2 = get_notification_groups_v2
    entities_notification_groups_post_v2 = create_notification_group_v2
    entities_notification_groups_patch_v2 = update_notification_group_v2
    entities_notification_groups_delete_v2 = delete_notification_group_v2
    entities_slas_get_v1 = get_slas
    entities_slas_post_v1 = create_sla
    entities_slas_patch_v1 = update_sla
    entities_slas_delete_v1 = delete_sla
    entities_template_snapshots_get_v1 = get_template_snapshots
    entities_templates_export_get_v1 = export_templates
    entities_templates_import_post_v1 = import_template
    entities_templates_get_v1 = get_templates
    entities_templates_post_v1 = create_template
    entities_templates_patch_v1 = update_template
    entities_templates_delete_v1 = delete_templates
    queries_fields_get_v1 = query_fields
    queries_access_tags_get_v1 = query_access_tags
    queries_notification_groups_get_v1 = query_notification_groups
    queries_notification_groups_get_v2 = query_notification_groups_v2
    queries_slas_get_v1 = query_slas
    queries_template_snapshots_get_v1 = query_template_snapshots
    queries_templates_get_v1 = query_templates
    entities_alert_evidence_post_v1 = add_case_alert_evidence
    entities_case_tags_post_v1 = add_case_tags
    entities_case_tags_delete_v1 = delete_case_tags
    entities_cases_put_v2 = create_case
    entities_cases_post_v2 = get_cases
    entities_cases_patch_v2 = update_case_fields
    entities_event_evidence_post_v1 = add_case_event_evidence
    queries_cases_get_v1 = query_case_ids
