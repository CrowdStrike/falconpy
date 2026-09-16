"""CrowdStrike Falcon ApplicationAbuseExclusions API interface class.

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
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import aggregate_payload, create_app_abuse_exclusion_payload, create_app_abuse_report_payload
from ._payload import update_app_abuse_exclusions_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._application_abuse_exclusions import _application_abuse_exclusions_endpoints as Endpoints


class ApplicationAbuseExclusions(ServiceClass):
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

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_app_abuse_exclusions(self: object,
                                       body: list = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Application Abuse Exclusion aggregates as specified via json in the request body.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/application-abuse-exclusions/app-abuse-exclusions.aggregates.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted list. Not required if using other keywords.
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
        date_ranges : list[dict]
            List of date range objects.
        field : str
            The field to aggregate on.
        filter : str
            FQL filter expression.
        interval : str
            Time interval for aggregation.
        min_doc_count : int
            Minimum document count threshold.
        missing : str
            Missing value handling.
        name : str
            Name of the aggregation.
        q : str
            Full text search across all metadata fields.
        ranges : list[dict]
            List of range objects.
        size : int
            Maximum number of results.
        sort : str
            Sort expression.
        sub_aggregates : list[str]
            List of sub-aggregate expressions.
        time_zone : str
            Time zone for date operations.
        type : str
            Type of aggregation (terms, date_histogram, etc.)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="app_abuse_exclusions_aggregates_v1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_app_abuse_report(self: object,
                                body: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a report of Application Abuse Exclusions scoped by the given filters.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/application-abuse-exclusions/app-abuse-exclusions.report.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "report_format": "string",
                    "search": {
                        "filter": "string",
                        "sort": "string"
                    }
                }
        report_format : str
            The report_format value.
        search : dict
            The search value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = create_app_abuse_report_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="app_abuse_exclusions_report_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_app_abuse_exclusions(self: object,
                                 *args,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Application Abuse Exclusions by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/application-abuse-exclusions/app-abuse-exclusions.get.v1

        Keyword arguments
        -----------------
        ids : str or list[str]
            The ids of the exclusions to retrieve.
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
            operation_id="app_abuse_exclusions_get_v1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_app_abuse_exclusion(self: object,
                                   body: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create new Application Abuse Exclusions.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/application-abuse-exclusions/app-abuse-exclusions.create.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "exclusions": [
                        {
                            "applied_globally": true,
                            "children_cids": [
                                "string"
                            ],
                            "comment": "string",
                            "description": "string",
                            "host_groups": [
                                "string"
                            ],
                            "tag": "string"
                        }
                    ]
                }
        exclusions : list
            The exclusions value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = create_app_abuse_exclusion_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="app_abuse_exclusions_create_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_app_abuse_exclusions(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete Application Abuse Exclusions by IDs.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/application-abuse-exclusions/app-abuse-exclusions.delete.v1

        Keyword arguments
        -----------------
        ids : list
            The ids of the exclusions to delete.
        comment : str
            The comment why these exclusions were deleted.
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
            operation_id="app_abuse_exclusions_delete_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_app_abuse_exclusions(self: object,
                                    body: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update existing Application Abuse Exclusions.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/application-abuse-exclusions/app-abuse-exclusions.update.v1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "exclusions": [
                        {
                            "applied_globally": true,
                            "children_cids": [
                                "string"
                            ],
                            "comment": "string",
                            "description": "string",
                            "host_groups": [
                                "string"
                            ],
                            "id": "string",
                            "tag": "string"
                        }
                    ]
                }
        exclusions : list
            The exclusions value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_app_abuse_exclusions_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="app_abuse_exclusions_update_v1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_app_abuse_apps_by_category(self: object,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get available applications filtered by Application Abuse Prevention category.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/application-abuse-exclusions/app-abuse-exclusions.get-apps-by-category.v1

        Keyword arguments
        -----------------
        category : str
            Filter applications by category (e.g. rmm)
        show_available_only : bool
            Filter out applications that already have exclusions.
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
            operation_id="app_abuse_exclusions_get_apps_by_category_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_app_abuse_categories(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get available Application Abuse Prevention categories.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/application-abuse-exclusions/app-abuse-exclusions.get-categories.v1

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
            operation_id="app_abuse_exclusions_get_categories_v1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_app_abuse_exclusions(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for Application Abuse Exclusions.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/application-abuse-exclusions/app-abuse-exclusions.query.v1

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results.
        offset : int
            The offset to start retrieving records from.
        limit : int
            The maximum records to return. [1-100]
        sort : str
            The sort expression that should be used to sort the results.
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
            operation_id="app_abuse_exclusions_query_v1",
            keywords=kwargs,
            params=parameters
            )
    app_abuse_exclusions_aggregates_v1 = aggregate_app_abuse_exclusions
    app_abuse_exclusions_report_v1 = create_app_abuse_report
    app_abuse_exclusions_get_v1 = get_app_abuse_exclusions
    app_abuse_exclusions_create_v1 = create_app_abuse_exclusion
    app_abuse_exclusions_delete_v1 = delete_app_abuse_exclusions
    app_abuse_exclusions_update_v1 = update_app_abuse_exclusions
    app_abuse_exclusions_get_apps_by_category_v1 = get_app_abuse_apps_by_category
    app_abuse_exclusions_get_categories_v1 = get_app_abuse_categories
    app_abuse_exclusions_query_v1 = query_app_abuse_exclusions
