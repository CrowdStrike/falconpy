"""CrowdStrike Falcon ExposureManagement API interface class.

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
from ._payload import aggregate_payload, fem_asset_payload, fem_add_asset_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._exposure_management import _exposure_management_endpoints as Endpoints


class ExposureManagement(ServiceClass):
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
    def aggregate_assets(self: object, body: list = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get detect aggregates as specified via json in request body.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/aggregate-external-assets

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
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
            If peforming a date range query specify the from and to date ranges.
            These can be in common date formats like 2019-07-18 or now.
        exclude : str
            Fields to exclude.
        field : str
            Term you want to aggregate on. If doing a date_range query,
            this is the date field you want to apply the date ranges to.
        filter : str
            Optional filter criteria in the form of an FQL query.
            For more information about FQL queries, see our FQL documentation in Falcon.
        from : int
        include : str
            Fields to include.
        interval : str
        max_doc_count : int
            Maximum number of documents.
        min_doc_count : int
            Minimum number of documents.
        missing : str
        name : str
            Scan name.
        q : str
            FQL syntax.
        ranges : list[dict]
        size : int
        sort : str
            FQL syntax.
        sub_aggregates : list[str]
        time_zone : str
        type : str

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
            operation_id="aggregate_external_assets",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_ecosystem_subsidiaries(self: object,
                                              parameters: dict = None,
                                              **kwargs
                                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a list of ecosystem subsidiaries with their detailed information.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/combined-ecosystem-subsidiaries

        Keyword arguments
        -----------------
        offset : int
            Starting index of result set from which to return IDs.
        limit : int
            Number of IDs to return.
        sort : str
            Order by fields.
        filter : str
            Filter ecosystem subsidiaries using an FQL query.
        version_id : str
            The version ID of the ecosystem subsidiaries data, represented as a hash string.
            This parameter is required to ensure data consistency and prevent stale data.
            If a new version of the ecosystem subsidiaries data is written, the version ID
            will be updated. By including this parameter in the request, the client can ensure
            that the response will be invalidated if a new version is written.
            This is a required field.
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
            operation_id="combined_ecosystem_subsidiaries",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def download_assets(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download the entire contents of the blob. The relative link to this endpoint is returned from query_external_assets.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/blob-download-external-assets

        Keyword arguments
        -----------------
        assetId : str
            The Asset ID.
        hash : str
            The File Hash.
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
            operation_id="blob_download_external_assets",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def preview_assets(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download a preview of the blob. The relative link to this endpoint is returned from query_external_assets.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/blob-preview-external-assets

        Keyword arguments
        -----------------
        assetId : str
            The Asset ID.
        hash : str
            The File Hash.
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
            operation_id="blob_preview_external_assets",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ecosystem_subsidiaries(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve detailed information about ecosystem subsidiaries by ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/get-ecosystem-subsidiaries

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more ecosystem subsidiary IDs (max: 100)
        version_id : str
            The version ID of the ecosystem subsidiaries data, represented as a hash string.
            This parameter is required to ensure data consistency and prevent stale data.
            If a new version of the ecosystem subsidiaries data is written, the version ID will
            be updated. By including this parameter in the request, the client can ensure that
            the response will be invalidated if a new version is written.
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
            operation_id="get_ecosystem_subsidiaries",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_assets(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the details of external assets.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/post-external-assets-inventory-v1

        Keyword arguments
        -----------------
        assets : list[dict]
            List of assets to be added.
        body : dict
            Full body payload as a dictionary. Not required when using other keywords.
                {
                    "data": [
                        {
                            "assets": [
                                {
                                    "id": "string",
                                    "value": "string"
                                }
                            ],
                            "subsidiary_id": "string"
                        }
                    ]
                }
        id : str
            Asset ID to be added.
        subsidiary_id : str
            Subsidiary ID of the asset to be added.
        value : str
            Asset value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = fem_add_asset_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="post_external_assets_inventory_v1",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_assets(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get details on external assets by providing one or more IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/get-external-assets

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more asset IDs (max: 100). Find asset IDs with `query_external_assets`.
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
            operation_id="get_external_assets",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def delete_assets(self: object,
                      *args,
                      body: dict = None,
                      parameters: dict = None,
                      **kwargs
                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete external assets by providing one or more IDs.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/delete-external-assets

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a dictionary. Not required if using other keywords.
        description : str
            Delete operation description.
        ids : str or list[str]
            One or more asset IDs (max: 100). Find asset IDs with query_external_assets.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            if kwargs.get("description", None):
                body["description"] = kwargs.get("description")
                kwargs.pop("description")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="delete_external_assets",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids"),
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_assets(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the details of external assets.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/patch-external-assets

        Keyword arguments
        -----------------
        action : str
            The asset triage action.
        assigned_to : str
            The user assigned to triage the asset.
        body : dict
            Full body payload as a dictionary. Not required when using other keywords.
        cid : str
            Falcon Customer ID.
        criticality : str
            The criticality level manually assigned to this asset.
        criticality_description : str
            The criticality description assigned to this asset.
        description : str
            The asset triage description.
        id : str
            The unique ID of the asset.
        status : str
            The asset trriage status.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = fem_asset_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="patch_external_assets",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_ecosystem_subsidiaries(self: object,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a list of IDs for ecosystem subsidiaries that match the provided filter conditions.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/query-ecosystem-subsidiaries

        Keyword arguments
        -----------------
        offset : int
            Starting index of result set from which to return IDs.
        limit : int
            Number of IDs to return.
        sort : str
            Order by fields.
        filter : str
            Filter ecosystem subsidiaries using an FQL query.
        version_id : str
            The version ID of the ecosystem subsidiaries data, represented as a hash string.
            This parameter is required to ensure data consistency and prevent stale data.
            If a new version of the ecosystem subsidiaries data is written, the version ID
            will be updated. By including this parameter in the request, the client can ensure
            that the response will be invalidated if a new version is written.
            This is a required field.
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
            operation_id="query_ecosystem_subsidiaries",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_assets_v1(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of external asset IDs that match the provided filter conditions.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/query-external-assets

        Keyword arguments
        -----------------
        offset : str
            Starting index of result set from which to return IDs.
        limit : int
            Number of IDs to return.
        sort : str
            Order by fields.
        filter : str
            Filter assets using an FQL query.
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
            operation_id="query_external_assets",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_assets(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of external asset IDs that match the provided filter conditions.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/exposure-management/query-external-assets-v2

        Keyword arguments
        -----------------
        offset : int
            Starting index of result set from which to return IDs.
        limit : int
            Number of IDs to return.
        sort : str
            Order by fields.
        filter : str
            Filter assets using an FQL query. String.
            Available filter fields that support exact match:
              asset_id                                        ip.cloud_vm.region
              asset_type                                      ip.cloud_vm.security_groups
              confidence                                      ip.cloud_vm.source
              connectivity_status                             ip.cloud_vm.status
              criticality                                     ip.fqdns
              criticality_description                         ip.ip_address
              criticality_timestamp                           ip.isp
              criticality_username                            ip.location.area_code
              data_providers                                  ip.location.city
              discovered_by                                   ip.location.country_code
              dns_domain.fqdn                                 ip.location.country_name
              dns_domain.isps                                 ip.location.postal_code
              dns_domain.parent_domain                        ip.location.region_code
              dns_domain.resolved_ips                         ip.location.region_name
              dns_domain.services.applications.category       ip.location.timezone
              dns_domain.services.applications.cpe            ip.ptr
              dns_domain.services.applications.name           ip.aid
              dns_domain.services.applications.vendor         ip.services.applications.category
              dns_domain.services.applications.version        ip.services.applications.cpe
              dns_domain.services.cloud_provider              ip.services.applications.name
              dns_domain.services.cpes                        ip.services.applications.vendor
              dns_domain.services.hosting_provider            ip.services.applications.version
              dns_domain.services.last_seen                   ip.services.cloud_provider
              dns_domain.services.platform_name               ip.services.cpes
              dns_domain.services.port                        ip.services.first_seen
              dns_domain.services.protocol                    ip.services.last_seen
              dns_domain.services.protocol_port               ip.services.platform_name
              dns_domain.services.status                      ip.services.port
              dns_domain.services.status_code                 ip.services.protocol
              dns_domain.services.transport                   ip.services.protocol_port
              dns_domain.type                                 ip.services.status
              first_seen                                      ip.services.status_code
              id                                              ip.services.transport
              internet_exposure                               last_seen
              ip.asn                                          manual
              ip.cloud_provider                               perimeter
              ip.cloud_vm.description                         subsidiaries.id
              ip.cloud_vm.instance_id                         subsidiaries.name
              ip.cloud_vm.lifecycle                           triage.action
              ip.cloud_vm.mac_address                         triage.assigned_to
              ip.cloud_vm.owner_id                            triage.status
              ip.cloud_vm.platform                            triage.updated_by
              ip.cloud_vm.private_ip                          triage.updated_timestamp
              ip.cloud_vm.public_ip
            Available filter fields that supports wildcard (*):
              asset_id                                        ip.cloud_vm.security_groups
              asset_type                                      ip.cloud_vm.source
              confidence                                      ip.cloud_vm.status
              connectivity_status                             ip.fqdns
              criticality                                     ip.ip_address
              criticality_username                            ip.isp
              data_providers                                  ip.location.area_code
              discovered_by                                   ip.location.city
              dns_domain.fqdn                                 ip.location.country_code
              dns_domain.isps                                 ip.location.country_name
              dns_domain.parent_domain                        ip.location.postal_code
              dns_domain.resolved_ips                         ip.location.region_code
              dns_domain.services.applications.category       ip.location.region_name
              dns_domain.services.applications.cpe            ip.location.timezone
              dns_domain.services.applications.name           ip.ptr
              dns_domain.services.applications.vendor         ip.aid
              dns_domain.services.applications.version        ip.services.applications.category
              dns_domain.services.cloud_provider              ip.services.applications.cpe
              dns_domain.services.cpes                        ip.services.applications.name
              dns_domain.services.hosting_provider            ip.services.applications.vendor
              dns_domain.services.id                          ip.services.applications.version
              dns_domain.services.platform_name               ip.services.cloud_provider
              dns_domain.services.port                        ip.services.cpes
              dns_domain.services.protocol                    ip.services.platform_name
              dns_domain.services.protocol_port               ip.services.port
              dns_domain.services.status                      ip.services.protocol
              dns_domain.services.status_code                 ip.services.protocol_port
              dns_domain.services.transport                   ip.services.status
              dns_domain.type                                 ip.services.status_code
              id                                              ip.services.transport
              internet_exposure                               manual
              ip.asn                                          perimeter
              ip.cloud_vm.instance_id                         subsidiaries.id
              ip.cloud_vm.lifecycle                           subsidiaries.name
              ip.cloud_vm.mac_address                         triage.action
              ip.cloud_vm.owner_id                            triage.assigned_to
              ip.cloud_vm.platform                            triage.status
              ip.cloud_vm.private_ip                          triage.updated_by
              ip.cloud_vm.public_ip                           ip.cloud_vm.region
            Available filter fields that supports in ([v1, v2]):
              asset_id                                        ip.cloud_vm.source
              asset_type                                      ip.cloud_vm.status
              confidence                                      ip.fqdns
              connectivity_status                             ip.isp
              criticality                                     ip.location.area_code
              criticality_username                            ip.location.city
              data_providers                                  ip.location.country_code
              discovered_by                                   ip.location.country_name
              dns_domain.fqdn                                 ip.location.postal_code
              dns_domain.isps                                 ip.location.region_code
              dns_domain.parent_domain                        ip.location.region_name
              dns_domain.services.applications.category       ip.location.timezone
              dns_domain.services.applications.cpe            ip.ptr
              dns_domain.services.applications.name           ip.aid
              dns_domain.services.applications.vendor         ip.services.applications.category
              dns_domain.services.applications.version        ip.services.applications.cpe
              dns_domain.services.cloud_provider              ip.services.applications.name
              dns_domain.services.cpes                        ip.services.applications.vendor
              dns_domain.services.id                          ip.services.applications.version
              dns_domain.services.platform_name               ip.services.cloud_provider
              dns_domain.services.port                        ip.services.cpes
              dns_domain.services.protocol                    ip.services.platform_name
              dns_domain.services.protocol_port               ip.services.port
              dns_domain.services.status                      ip.services.protocol
              dns_domain.services.status_code                 ip.services.protocol_port
              dns_domain.services.transport                   ip.services.status
              dns_domain.type                                 ip.services.status_code
              id                                              ip.services.transport
              internet_exposure                               manual
              ip.asn                                          perimeter
              ip.cloud_vm.instance_id                         subsidiaries.id
              ip.cloud_vm.lifecycle                           subsidiaries.name
              ip.cloud_vm.mac_address                         triage.action
              ip.cloud_vm.owner_id                            triage.assigned_to
              ip.cloud_vm.platform                            triage.status
              ip.cloud_vm.region                              triage.updated_by
              ip.cloud_vm.security_groups
            Available filter fields that supports range comparisons (>, <, >=, <=):
              criticality_timestamp                           ip.cloud_vm.public_ip
              dns_domain.resolved_ips                         ip.ip_address
              dns_domain.services.first_seen                  ip.services.first_seen
              dns_domain.services.last_seen                   ip.services.last_seen
              dns_domain.services.port                        ip.services.port
              dns_domain.services.status_code                 ip.services.status_code
              first_seen                                      last_seen
              ip.cloud_vm.private_ip                          triage.updated_timestamp
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
            operation_id="query_external_assets_v2",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # does not conform to snake_case / PEP8 and are defined here
    # for backwards compatibility / ease of use purposes
    aggregate_external_assets = aggregate_assets
    combined_ecosystem_subsidiaries = query_combined_ecosystem_subsidiaries
    blob_download_external_assets = download_assets
    blob_preview_external_assets = preview_assets
    post_external_assets_inventory_v1 = add_assets
    get_external_assets = get_assets
    delete_external_assets = delete_assets
    patch_external_assets = update_assets
    query_external_assets_v1 = query_assets_v1
    query_external_assets = query_assets
    query_external_assets_v2 = query_assets
