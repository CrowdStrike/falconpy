"""CrowdStrike Falcon Discover API Interface Class.

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
from ._util import process_service_request, force_default, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._discover import _discover_endpoints as Endpoints


class Discover(ServiceClass):
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
    def get_accounts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get details on accounts by providing one or more IDs.

        Find account IDs with `query_accounts`.

        Keyword arguments:
        ids -- One or more account IDs (max: 100). String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/discover/get-accounts
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_accounts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_hosts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get details on assets by providing one or more IDs.

        Find asset IDs with `query_hosts`.

        Keyword arguments:
        ids -- One or more asset IDs (max: 100). String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/discover/get-hosts
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_hosts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_logins(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get details on logins by providing one or more IDs.

        Find login IDs with `query_logins`.

        Keyword arguments:
        ids -- One or more login IDs (max: 100). String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/discover/get-logins
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_logins",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_accounts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Search for accounts in your environment.

        Supports providing a FQL (Falcon Query Language) filter and paging details.
        Returns a set of account IDs which match the filter criteria.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
                  Common filter options include:
                    account_type:'Local'
                    admin_privileges:'Yes'
                    first_seen_timestamp:<'now-7d'
                    last_successful_login_type:'Terminal server'
                  Available Filters:
                    id                            last_successful_login_timestamp
                    cid                           last_successful_login_hostname
                    user_sid                      last_successful_login_remote_ip
                    login_domain                  last_successful_login_host_country
                    account_name                  last_successful_login_host_city
                    username                      last_failed_login_type
                    account_type                  last_failed_login_timestamp
                    admin_privileges              last_failed_login_hostname
                    first_seen_timestamp          password_last_set_timestamp
                    last_successful_login_type
        limit -- The number of account IDs to return in this response. (Max: 100, default: 100)
                 Use with the offset parameter to manage pagination of results.
        offset -- An offset used with the limit parameter to manage pagination of results.
                  On your first request, don’t provide an offset. On subsequent requests,
                  provide the offset from the previous response to continue from that place
                  in the results.
        parameters - full parameters payload, not required if using other keywords.
        sort -- Sort assets by their properties. A single sort field is allowed.
                Common sort options include:
                  username|asc
                  last_failed_login_timestamp|desc

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/discover/query-accounts
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_accounts",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_hosts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Search for assets in your environment.

        Supports providing a FQL (Falcon Query Language) filter and paging details.
        Returns a set of asset IDs which match the filter criteria.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
                  Available Filters:
                    agent_version                   kernel_version
                    aid                             last_discoverer_aid
                    bios_manufacturer               last_seen_timestamp
                    bios_version                    local_ips_count
                    cid                             machine_domain
                    city                            network_interfaces
                    confidence                      network_interfaces.interface_alias
                    country                         network_interfaces.interface_description
                    current_local_ip                network_interfaces.local_ip
                    discoverer_aids                 network_interfaces.mac_address
                    discoverer_count                network_interfaces.network_prefix
                    discoverer_platform_names       os_version
                    discoverer_product_type_descs   ou
                    discoverer_tags                 platform_name
                    entity_type                     product_type
                    external_ip                     product_type_desc
                    first_discoverer_aid            site_name
                    first_discoverer_ip             system_manufacturer
                    first_seen_timestamp            system_product_name
                    groups                          system_serial_number
                    hostname                        tags
                    id
        limit -- The number of asset IDs to return in this response. (Max: 100, default: 100)
                 Use with the offset parameter to manage pagination of results.
        offset -- An offset used with the limit parameter to manage pagination of results.
                  On your first request, don’t provide an offset. On subsequent requests,
                  provide the offset from the previous response to continue from that place
                  in the results.
        parameters - full parameters payload, not required if using other keywords.
        sort -- Sort assets by their properties. A single sort field is allowed.
                Common sort options include:
                  hostname|asc
                  product_type|desc

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/discover/query-hosts
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_hosts",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_logins(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Search for logins in your environment.

        Supports providing a FQL (Falcon Query Language) filter and paging details.
        Returns a set of asset IDs which match the filter criteria.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
                  Common sort options include:
                    account_type:'Local'
                    login_type:'Interactive'
                    first_seen_timestamp:<'now-7d'
                    admin_privileges:'No'
                  Available Filters:
                    id                  login_timestamp
                    cid                 login_domain
                    login_status        admin_privileges
                    account_id          local_ip
                    host_id             remote_ip
                    user_sid            host_country
                    aid                 host_city
                    account_name        is_suspicious
                    username            failure_description
                    hostname            login_event_count
                    account_type        aggregation_time_interval
                    login_type
        limit -- The number of login IDs to return in this response. (Max: 100, default: 100)
                 Use with the offset parameter to manage pagination of results.
        offset -- An offset used with the limit parameter to manage pagination of results.
                  On your first request, don’t provide an offset. On subsequent requests,
                  provide the offset from the previous response to continue from that place
                  in the results.
        parameters - full parameters payload, not required if using other keywords.
        sort -- Sort logins by their properties. A single sort field is allowed.
                Common sort options include:
                  account_name|asc
                  login_timestamp|desc

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/discover/query-logins
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_logins",
            keywords=kwargs,
            params=parameters
            )
