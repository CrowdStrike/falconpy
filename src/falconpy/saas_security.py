"""CrowdStrike Falcon SaasSecurity API interface class.

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
from ._endpoint._saas_security import _saas_security_endpoints as Endpoints


class SaasSecurity(ServiceClass):
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
    def get_metrics(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Metrics.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetMetricsV3

        Keyword arguments
        -----------------
        status : str
            Exposure status. String.
            Available values:
              Passed      Failed
              Dismissed   Pending
              Can't Run   Stale
        limit : int
            The maximum number of objects to return.
        offset : int
            The starting index of the results.
        integration_id : str
            Comma separated list of integration IDs.
        impact : str
            Impact. String.
            Available values:
              1   2   3
        compliance : bool
            Compliance.
        check_type : str
            Check Type. String.
            Available values:
              apps            devices
              users           assets
              permissions     Falcon Shield Security Check
              custom
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
            operation_id="GetMetricsV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_alerts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Alert by ID or GET Alerts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetAlertsV3

        Keyword arguments
        -----------------
        id : str
            Alert ID.
        limit : int
            The maximum number of objects to return.
        offset : int
            The starting index of the results.
        last_id : str
            The last id of the alert you want to get.
        type : str
            The type of alert you want to get. String.
            Available values:
                configuration_drift     check_degraded
                integration_failure     Threat
        integration_id : str
            Comma separated list of integration ID's of the alert you want to get.
        from_date : str
            The start date of the alert you want to get (in YYYY-MM-DD format)
        to_date : str
            The end date of the alert you want to get (in YYYY-MM-DD format)
        ascending : bool
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
            operation_id="GetAlertsV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_application_users(self: object,
                              *args,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Application Users.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetAppInventoryUsers

        Keyword arguments
        -----------------
        item_id : str
            Item ID in format: 'integration_id|||app_id' (item_id)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'item_id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAppInventoryUsers",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "item_id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_application_inventory(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Applications Inventory.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetAppInventory

        Keyword arguments
        -----------------
        type : str
            Comma separated list of app types.
        limit : int
            The maximum number of objects to return.
        offset : int
            The starting index of the results.
        status : str
            Comma separated list of application statuses. String.
            Available values:
              approved        in review
              rejected        unclassified
        access_level : str
            Comma separated list of access levels.
        scopes : str
            Comma separated list of scopes.
        users : str
            Users. Format: 'is equal value' or 'contains value' or 'value' (implies 'is equal value')
        groups : str
            Comma separated list of groups.
        last_activity : str
            Last activity was within or was not within the last 'value' days. String.
            Format: 'was value' or 'was not value' or 'value' (implies 'was value'). 'value' is an.
        integration_id : str
            Comma separated list of integration IDs.
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
            operation_id="GetAppInventory",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_security_check(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Security Check Affected.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetSecurityCheckAffectedV3

        Keyword arguments
        -----------------
        id : str
            Security Check ID.
        limit : int
            The maximum number of objects to return.
        offset : int
            The starting index of the results.
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
            operation_id="GetSecurityCheckAffectedV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def dismiss_affected_entity(self: object,
                                body: dict = None,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """POST Dismiss Affected Entity.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/DismissAffectedEntityV3

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "entities": "string",
                    "reason": "string"
                }
        entities : str
            Entities.
        reason : str
            Reason for dismiss.
        id : str
            Security Check ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            keys = ["entities", "reason"]
            for key in keys:
                if kwargs.get(key, None) is not None:
                    body[key] = kwargs.get(key, None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DismissAffectedEntityV3",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def dismiss_security_check(self: object,
                               body: dict = None,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """POST Dismiss Security Check by ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/DismissSecurityCheckV3

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "reason": "string"
                }
        reason : str
            The reason for dismissal.
        id : str
            Security Check ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            if kwargs.get("reason", None) is not None:
                body["reason"] = kwargs.get("reason", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DismissSecurityCheckV3",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_security_checks(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Security Check by ID or GET List Security Checks.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetSecurityChecksV3

        Keyword arguments
        -----------------
        id : str
            Security Check ID.
        limit : int
            The maximum number of objects to return.
        offset : int
            The starting index of the results.
        status : str
            Exposure status. String.
            Available values:
              Passsed         Failed
              Dismissed       Pending
              Can't Run       Stale
        integration_id : str
            Comma separated list of integration IDs.
        impact : str
            Impact. String.
            Available values:
              Low     Medium     High
        compliance : bool
            Compliance.
        check_type : str
            Check Type. String.
            Available values:
              apps            devices
              users           assets
              permissions     Falcon Shield Security Check
              custom
        check_tags : str
            Comma separated list of check tags names or ids.
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
            operation_id="GetSecurityChecksV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_security_check_compliance(self: object,
                                      *args,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Compliance.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetSecurityCheckComplianceV3

        Keyword arguments
        -----------------
        id : str
            Security Check ID.
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
            operation_id="GetSecurityCheckComplianceV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def complete_integration_upload(self: object,
                                    *args,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """POST Data Upload Transaction Completion.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/IntegrationBuilderEndTransactionV3

        Keyword arguments
        -----------------
        id : str
            Integration ID.
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
            operation_id="IntegrationBuilderEndTransactionV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def reset_integration_builder(self: object,
                                  *args,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Reset.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/IntegrationBuilderResetV3

        Keyword arguments
        -----------------
        id : str
            Integration ID.
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
            operation_id="IntegrationBuilderResetV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_integration_builder_status(self: object,
                                       *args,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Status.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/IntegrationBuilderGetStatusV3

        Keyword arguments
        -----------------
        id : str
            Integration ID.
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
            operation_id="IntegrationBuilderGetStatusV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def upload_integration_builder(self: object,
                                   body: dict = None,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """POST Upload.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/IntegrationBuilderUploadV3

        Keyword arguments
        -----------------
        body : dict
            Full body payload provided as a dictionary. Not required if using other keywords.
                {
                    "data": "string"
                }
        data : str
        id : str
            Integration ID.
        source_id : str
            Source ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            if kwargs.get("data", None) is not None:
                body["data"] = kwargs.get("data", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="IntegrationBuilderUploadV3",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_asset_inventory(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Data Inventory.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetAssetInventoryV3

        Keyword arguments
        -----------------
        integration_id : str
            Comma separated list of integration IDs.
        limit : int
            The maximum number of objects to return.
        offset : int
            The starting index of the results.
        resource_type : str
            Comma separated list of resource types.
        access_level : str
            Comma separated list of access levels.
        last_accessed : str
            Last accessed date was within or was not within the last 'value' days. String.
            Format: 'was value' or 'was not value' or 'value' (implies 'was value'). 'value' is an.
        last_modified : str
            Last modified date was within or was not within the last 'value' days. String.
            Format: 'was value' or 'was not value' or 'value' (implies 'was value'). 'value' is an.
        resource_name : str
            Resource name contains 'value' (case insensitive)
        password_protected : bool
            Password protected.
        resource_owner : str
            Resource owner contains 'value' (case insensitive)
        resource_owner_enabled : bool
            Resource owner enabled.
        unmanaged_domain : str
            Comma separated list of unmanaged domains.
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
            operation_id="GetAssetInventoryV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_device_inventory(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Device Inventory.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetDeviceInventoryV3

        Keyword arguments
        -----------------
        integration_id : str
            Comma separated integration ID's.
        limit : int
            The maximum number of objects to return.
        offset : int
            The starting index of the results.
        email : str
            Email.
        privileged_only : bool
            Privileged Only.
        unassociated_devices : bool
            Unassociated Devices.
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
            operation_id="GetDeviceInventoryV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_integrations(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Integrations.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetIntegrationsV3

        Keyword arguments
        -----------------
        saas_id : str
            Comma separated SaaS ID's.
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
            operation_id="GetIntegrationsV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_activity_monitor(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Activity Monitor.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetActivityMonitorV3

        Keyword arguments
        -----------------
        integration_id : str
            Integration ID.
        actor : str
            Actor.
        category : str
            Comma separated list of categories.
        projection : str
            Comma separated list of projections.
        from_date : str
            From Date.
        to_date : str
            To Date.
        limit : int
            Max number of logs to fetch.
        skip : int
            Number of logs to skip.
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
            operation_id="GetActivityMonitorV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_supported_saas(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET Supported SaaS.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetSupportedSaasV3

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
            operation_id="GetSupportedSaasV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_system_logs(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET System Logs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetSystemLogsV3

        Keyword arguments
        -----------------
        from_date : str
            From Date (in YYYY-MM-DD format)
        limit : int
            The maximum number of objects to return.
        offset : int
            The starting index of the results.
        to_date : str
            To Date (in YYYY-MM-DD format)
        total_count : bool
            Fetch Total Count?
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
            operation_id="GetSystemLogsV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_system_users(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET System Users.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetSystemUsersV3

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
            operation_id="GetSystemUsersV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_user_inventory(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """GET User Inventory.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/saas-security/GetUserInventoryV3

        Keyword arguments
        -----------------
        integration_id : str
            Comma separated integration ID's.
        limit : int
            The maximum number of objects to return.
        offset : int
            The starting index of the results.
        email : str
            Email.
        privileged_only : bool
            Privileged Only.
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
            operation_id="GetUserInventoryV3",
            keywords=kwargs,
            params=parameters
            )

    GetMetricsV3 = get_metrics
    GetAlertsV3 = get_alerts
    GetAppInventoryUsers = get_application_users
    GetAppInventory = get_application_inventory
    GetSecurityCheckAffectedV3 = get_security_check
    DismissAffectedEntityV3 = dismiss_affected_entity
    DismissSecurityCheckV3 = dismiss_security_check
    GetSecurityChecksV3 = get_security_checks
    GetSecurityCheckComplianceV3 = get_security_check_compliance
    IntegrationBuilderEndTransactionV3 = complete_integration_upload
    IntegrationBuilderResetV3 = reset_integration_builder
    IntegrationBuilderGetStatusV3 = get_integration_builder_status
    IntegrationBuilderUploadV3 = upload_integration_builder
    GetAssetInventoryV3 = get_asset_inventory
    GetDeviceInventoryV3 = get_device_inventory
    GetIntegrationsV3 = get_integrations
    GetActivityMonitorV3 = get_activity_monitor
    GetSupportedSaasV3 = get_supported_saas
    GetSystemLogsV3 = get_system_logs
    GetSystemUsersV3 = get_system_users
    GetUserInventoryV3 = get_user_inventory
