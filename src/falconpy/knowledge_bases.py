"""CrowdStrike Falcon KnowledgeBases API interface class.

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
from ._payload import aggregate_payload, entities_knowledge_bases_create_v1_payload, entities_knowledge_bases_update_v1_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._knowledge_bases import _knowledge_bases_endpoints as Endpoints


class KnowledgeBases(ServiceClass):
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

    @force_default(defaults=["body", "parameters"], default_types=["list", "dict"])
    def aggregates_knowledge_bases_v1(self: object,
                                      body: list = None,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate knowledge bases based on the provided msa criteria.

        Keyword arguments:
        include_deleted -- Include deleted knowledge bases in the result. Defaults to false. Boolean.
        body -- Full body payload as a JSON formatted list. Not required if using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "exclude": "string",
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "include": "string",
                        "interval": "string",
                        "max_doc_count": 0,
                        "min_doc_count": 0,
                        "missing": "string",
                        "name": "string",
                        "q": "string",
                        "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                        ],
                        "size": 0,
                        "sort": "string",
                        "sub_aggregates": [
                            null
                        ],
                        "time_zone": "string",
                        "type": "string"
                    }
                ]
        date_ranges -- List of date range objects. List of dictionaries.
        field -- The field to aggregate on. String.
        filter -- FQL filter expression. String.
        interval -- Time interval for aggregation. String.
        min_doc_count -- Minimum document count threshold. Integer.
        missing -- Missing value handling. String.
        name -- Name of the aggregation. String.
        q -- Full text search across all metadata fields. String.
        ranges -- List of range objects. List of dictionaries.
        size -- Maximum number of results. Integer.
        sort -- Sort expression. String.
        sub_aggregates -- List of sub-aggregate expressions. List of strings.
        time_zone -- Time zone for date operations. String.
        type -- Type of aggregation (terms, date_histogram, etc.). String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-bases/AggregatesKnowledgeBasesV1
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregatesKnowledgeBasesV1",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def entities_knowledge_bases_v1(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve knowledge base entities for the provided id.

        Keyword arguments:
        ids -- IDs of entities to retrieve. List.
        include_deleted -- Include deleted knowledge bases in the result. Defaults to false. Boolean.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-bases/EntitiesKnowledgeBasesV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesKnowledgeBasesV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def entities_knowledge_bases_create_v1(self: object,
                                           body: dict = None,
                                           **kwargs
                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create or update a knowledge base.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "created_at": "string",
                    "created_by": {
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
                        "uuid": "string"
                    },
                    "description": "string",
                    "embedding_model": "string",
                    "files_count": 0,
                    "id": "string",
                    "is_deleted": true,
                    "name": "string",
                    "updated_at": "string",
                    "updated_by": {
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
                        "uuid": "string"
                    }
                }
        created_at -- The created_at value. String.
        created_by -- The created_by value. Dictionary.
        description -- The description value. String.
        embedding_model -- The embedding_model value. String.
        files_count -- The files_count value. Integer.
        id -- The id value. String.
        is_deleted -- The is_deleted value. Boolean.
        name -- The name value. String.
        updated_at -- The updated_at value. String.
        updated_by -- The updated_by value. Dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-bases/EntitiesKnowledgeBasesCreateV1
        """
        if not body:
            body = entities_knowledge_bases_create_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesKnowledgeBasesCreateV1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def entities_knowledge_bases_update_v1(self: object,
                                           body: dict = None,
                                           **kwargs
                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing knowledge base.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "created_at": "string",
                    "created_by": {
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
                        "uuid": "string"
                    },
                    "description": "string",
                    "embedding_model": "string",
                    "files_count": 0,
                    "id": "string",
                    "is_deleted": true,
                    "name": "string",
                    "updated_at": "string",
                    "updated_by": {
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
                        "uuid": "string"
                    }
                }
        created_at -- The created_at value. String.
        created_by -- The created_by value. Dictionary.
        description -- The description value. String.
        embedding_model -- The embedding_model value. String.
        files_count -- The files_count value. Integer.
        id -- The id value. String.
        is_deleted -- The is_deleted value. Boolean.
        name -- The name value. String.
        updated_at -- The updated_at value. String.
        updated_by -- The updated_by value. Dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-bases/EntitiesKnowledgeBasesUpdateV1
        """
        if not body:
            body = entities_knowledge_bases_update_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesKnowledgeBasesUpdateV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queries_knowledge_bases_v1(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query knowledge bases based on the provided filters.

        Keyword arguments:
        offset -- Starting index of overall result set from which to return ids. Integer.
        limit -- Number of IDs to return. Offset + limit should NOT be above 10K. Integer.
        sort -- Possible order by fields: name, created_at. Ex: 'created_at|desc' or 'name|asc'. String.
        filter -- FQL query specifying the filter parameters. String.
        include_deleted -- Include deleted knowledge bases in the result. Defaults to false. Boolean.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/knowledge-bases/QueriesKnowledgeBasesV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueriesKnowledgeBasesV1",
            keywords=kwargs,
            params=parameters
            )
    AggregatesKnowledgeBasesV1 = aggregates_knowledge_bases_v1
    EntitiesKnowledgeBasesV1 = entities_knowledge_bases_v1
    EntitiesKnowledgeBasesCreateV1 = entities_knowledge_bases_create_v1
    EntitiesKnowledgeBasesUpdateV1 = entities_knowledge_bases_update_v1
    QueriesKnowledgeBasesV1 = queries_knowledge_bases_v1
