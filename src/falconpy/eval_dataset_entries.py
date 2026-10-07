"""CrowdStrike Falcon EvalDatasetEntries API interface class.

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
from ._util import force_default, process_service_request
from ._payload import create_eval_dataset_entry_payload, update_eval_dataset_entry_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._eval_dataset_entries import _eval_dataset_entries_endpoints as Endpoints


class EvalDatasetEntries(ServiceClass):
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
    def get_eval_dataset_entries(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve evaluation dataset entry entities for the provided id.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-dataset-entries/EntitiesEvalDatasetEntriesV1

        Keyword arguments
        -----------------
        ids : list
            IDs of entities to retrieve.
        project_id : str
            Scope the operation to a project.
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
            operation_id="EntitiesEvalDatasetEntriesV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_eval_dataset_entry(self: object,
                                  body: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing evaluation dataset entry.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-dataset-entries/EntitiesEvalDatasetEntriesUpdateV1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "created_at": "string",
                    "created_by": {
                        "access_granted_at": "string",
                        "cid": "string",
                        "created_at": "string",
                        "factors": [
                            "string"
                        ],
                        "first_name": "string",
                        "last_login_at": "string",
                        "last_name": "string",
                        "status": "string",
                        "uid": "string",
                        "updated_at": "string",
                        "user_type": "string",
                        "uuid": "string",
                        "api_client_id": "string",
                        "email": "string",
                        "name": "string"
                    },
                    "data": "string",
                    "dataset_id": "string",
                    "description": "string",
                    "id": "string",
                    "is_deleted": true,
                    "metadata": "string",
                    "name": "string",
                    "owner": "string",
                    "project_id": "string",
                    "tags": [
                        "string"
                    ],
                    "updated_at": "string",
                    "updated_by": {
                        "access_granted_at": "string",
                        "cid": "string",
                        "created_at": "string",
                        "factors": [
                            "string"
                        ],
                        "first_name": "string",
                        "last_login_at": "string",
                        "last_name": "string",
                        "status": "string",
                        "uid": "string",
                        "updated_at": "string",
                        "user_type": "string",
                        "uuid": "string",
                        "api_client_id": "string",
                        "email": "string",
                        "name": "string"
                    }
                }
        created_at : str
            The created_at value.
        created_by : dict
            The created_by value.
        data : dict
            The data value.
        dataset_id : str
            The dataset_id value.
        description : str
            The description value.
        id : str
            The id value.
        is_deleted : bool
            The is_deleted value.
        metadata : dict
            The metadata value.
        name : str
            The name value.
        owner : str
            The owner value.
        project_id : str
            The project_id value.
        tags : list
            The tags value.
        updated_at : str
            The updated_at value.
        updated_by : dict
            The updated_by value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_eval_dataset_entry_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesEvalDatasetEntriesUpdateV1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_eval_dataset_entry(self: object,
                                  body: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new evaluation dataset entry.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-dataset-entries/EntitiesEvalDatasetEntriesCreateV1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "created_at": "string",
                    "created_by": {
                        "access_granted_at": "string",
                        "cid": "string",
                        "created_at": "string",
                        "factors": [
                            "string"
                        ],
                        "first_name": "string",
                        "last_login_at": "string",
                        "last_name": "string",
                        "status": "string",
                        "uid": "string",
                        "updated_at": "string",
                        "user_type": "string",
                        "uuid": "string",
                        "api_client_id": "string",
                        "email": "string",
                        "name": "string"
                    },
                    "data": "string",
                    "dataset_id": "string",
                    "description": "string",
                    "id": "string",
                    "is_deleted": true,
                    "metadata": "string",
                    "name": "string",
                    "owner": "string",
                    "project_id": "string",
                    "tags": [
                        "string"
                    ],
                    "updated_at": "string",
                    "updated_by": {
                        "access_granted_at": "string",
                        "cid": "string",
                        "created_at": "string",
                        "factors": [
                            "string"
                        ],
                        "first_name": "string",
                        "last_login_at": "string",
                        "last_name": "string",
                        "status": "string",
                        "uid": "string",
                        "updated_at": "string",
                        "user_type": "string",
                        "uuid": "string",
                        "api_client_id": "string",
                        "email": "string",
                        "name": "string"
                    }
                }
        created_at : str
            The created_at value.
        created_by : dict
            The created_by value.
        data : dict
            The data value.
        dataset_id : str
            The dataset_id value.
        description : str
            The description value.
        id : str
            The id value.
        is_deleted : bool
            The is_deleted value.
        metadata : dict
            The metadata value.
        name : str
            The name value.
        owner : str
            The owner value.
        project_id : str
            The project_id value.
        tags : list
            The tags value.
        updated_at : str
            The updated_at value.
        updated_by : dict
            The updated_by value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = create_eval_dataset_entry_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesEvalDatasetEntriesCreateV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_eval_dataset_entry(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an evaluation dataset entry.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-dataset-entries/EntitiesEvalDatasetEntriesDeleteV1

        Keyword arguments
        -----------------
        id : str
            ID of the dataset entry to delete.
        project_id : str
            Scope the operation to a project.
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
            operation_id="EntitiesEvalDatasetEntriesDeleteV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_eval_dataset_entries(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query evaluation dataset entries based on the provided filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-dataset-entries/QueriesEvalDatasetEntriesV1

        Keyword arguments
        -----------------
        offset : int
            Starting index of overall result set from which to return ids.
        limit : int
            Number of IDs to return. Offset + limit should NOT be above 10K.
        sort : str
            Possible order by fields: name, created_at. Ex: 'created_at|desc' or 'name|asc'
        filter : str
            FQL query specifying the filter parameters.
        project_id : str
            Scope the operation to a project.
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
            operation_id="QueriesEvalDatasetEntriesV1",
            keywords=kwargs,
            params=parameters
            )
    EntitiesEvalDatasetEntriesV1 = get_eval_dataset_entries
    EntitiesEvalDatasetEntriesUpdateV1 = update_eval_dataset_entry
    EntitiesEvalDatasetEntriesCreateV1 = create_eval_dataset_entry
    EntitiesEvalDatasetEntriesDeleteV1 = delete_eval_dataset_entry
    QueriesEvalDatasetEntriesV1 = query_eval_dataset_entries
