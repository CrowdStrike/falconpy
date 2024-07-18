"""CrowdStrike Falcon Datascanner API interface class.

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
from ._service_class import ServiceClass
from ._endpoint._datascanner import _datascanner_endpoints as Endpoints


class DataScanner(ServiceClass):
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
    def get_image_registry_credentials(self: object) -> Dict[str, Union[int, dict]]:
        """Retrieve the registry credentials.

        HTTP Method: GET

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/datascanner/get-image-registry-credentials

        Keyword arguments
        ----
        This method does not accept keyword arguments.

        Arguments
        ----
        This method does not accept arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_image_registry_credentials",
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_data_scanner_tasks(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Retrieve data scanner tasks identified by the id.

        HTTP Method: GET

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/datascanner/get-data-scanner-tasks

        Keyword arguments
        ----
        X-Scanner-Id : str (required)
            id of the data scanner.

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_data_scanner_tasks",
            keywords=kwargs,
            params=parameters
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_data_scanner_tasks(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Update data scanner tasks, as identified by the X-Scanner-Id.

        HTTP Method: PATCH

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/datascanner/update-data-scanner-tasks

        Keyword arguments
        ----
        X-Scanner-Id : str
            ID of the data scanner
        X-Machine-Id : str
            Provider ID of the machine

        This method only supports keywords for providing arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_data_scanner_tasks",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    get_image_registry_credentials = get_image_registry_credentials
    get_data_scanner_tasks = get_data_scanner_tasks
    update_data_scanner_tasks = update_data_scanner_tasks
