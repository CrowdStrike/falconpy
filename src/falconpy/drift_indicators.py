"""CrowdStrike Falcon Drift Indicators API interface class.

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
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._drift_indicators import _drift_indicators_endpoints as Endpoints


class DriftIndicators(ServiceClass):
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
    def get_drift_indicators_by_date(self: object,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return the count of Drift Indicators by the date. by default it's for 7 days.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/drift-indicators/GetDriftIndicatorsValuesByDate

        Keyword arguments
        -----------------
        filter : str
            Filter drift indicators using a query in Falcon Query Language (FQL). String.
            Supported filters:
              cid                     namespace
              cloud_name              occurred_at
              command_line            parent_process_id
              container_id            pod_name
              file_name               prevented
              file_sha256             scheduler_name
              host_id                 severity
              indicator_process_id    worker_node_name
        limit : int
            The upper-bound on the number of records to retrieve.
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
            operation_id="GetDriftIndicatorsValuesByDate",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_drift_indicator_counts(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return the total count of Drift indicators over a time period.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/drift-indicators/ReadDriftIndicatorsCount

        Keyword arguments
        -----------------
        filter : str
            Filter images using a query in Falcon Query Language (FQL). String.
            Supported filters:
              cid                     namespace
              cloud_name              occurred_at
              command_line            parent_process_id
              container_id            pod_name
              file_name               prevented
              file_sha256             scheduler_name
              host_id                 severity
              indicator_process_id    worker_node_name
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
            operation_id="ReadDriftIndicatorsCount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_and_read_drift_indicators(self: object,
                                         parameters: dict = None,
                                         **kwargs
                                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Drift Indicators by the provided search criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/drift-indicators/SearchAndReadDriftIndicatorEntities

        Keyword arguments
        -----------------
        filter : str
            Filter Drift Indicators using a query in Falcon Query Language (FQL). String.
            Supported filters:
              cid                     namespace
              cloud_name              occurred_at
              command_line            parent_process_id
              container_id            pod_name
              file_name               prevented
              file_sha256             scheduler_name
              host_id                 severity
              indicator_process_id    worker_node_name
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            The fields to sort the records on.
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
            operation_id="SearchAndReadDriftIndicatorEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_drift_indicator_entities(self: object,
                                      *args,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Drift Indicator entities identified by the provided IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/drift-indicators/ReadDriftIndicatorEntities

        Keyword arguments
        -----------------
        ids : str or list[str]
            AID(s) of the hosts to retrieve.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

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
            operation_id="ReadDriftIndicatorEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_drift_indicators(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve all drift indicators that match the given query.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/drift-indicators/SearchDriftIndicators

        Keyword arguments
        -----------------
        filter : str
            Filter Drift Indicators using a query in Falcon Query Language (FQL). String.
            Supported filters:
              cid                     namespace
              cloud_name              occurred_at
              command_line            parent_process_id
              container_id            pod_name
              file_name               prevented
              file_sha256             scheduler_name
              host_id                 severity
              indicator_process_id    worker_node_name
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            The fields to sort the records on.
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
            operation_id="SearchDriftIndicators",
            keywords=kwargs,
            params=parameters
            )

    GetDriftIndicatorsValuesByDate = get_drift_indicators_by_date
    ReadDriftIndicatorsCount = read_drift_indicator_counts
    ReadDriftIndicatorEntities = read_drift_indicator_entities
    SearchAndReadDriftIndicatorEntities = search_and_read_drift_indicators
    SearchDriftIndicators = search_drift_indicators
