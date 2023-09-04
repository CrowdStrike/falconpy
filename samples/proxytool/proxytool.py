#!/usr/bin/env python3

r"""ProxyTool - Update Falcon Sensor proxy configurations remotely.
     ___                   ______          __       ____
    / _ \_______ __ ____ _/_  __/__  ___  / / _  __|_  /
   / ___/ __/ _ \\ \ / // // / / _ \/ _ \/ / | |/ //_ <
  /_/  /_/  \___/_\_\\_, //_/  \___/\___/_/  |___/____/
                    /___/

 Use RTR API to change Falcon sensor proxy configuration across CID or host group
 FalconPy v1.0

 CHANGE LOG

 04/09/2023   v3.6    Handle API authentication errors
 16/08/2023   v3.5    Add sanity check when using CID as scope
 28/02/2023   v3.4    Add ability to disable/delete proxy config
 27/10/2022   v3.3    Use command line arguments instead of external file for config
 26/10/2022   v3.2    Add support for Host Group or CID selection
 25/10/2022   v3.1    Ported to falconpy SDK instead of reinventing the wheel
 23/10/2022   v3.0    Rewrote 2.0 for error handling, logging and fetching host IDs from API
"""

# Import dependencies
import datetime
from argparse import ArgumentParser, RawTextHelpFormatter

# Define logging function
def log(msg):
    """Print the log message to the terminal."""
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") + '  ' + str(msg))

# Import SDK
try:
    from falconpy import(
        Hosts,
        OAuth2,
        RealTimeResponse,
        HostGroup,
        SensorDownload
    )
except ImportError as err:
    log(err)
    log("Python falconpy library is required.\n"
        "Install with: python3 -m pip install crowdstrike-falconpy"
        )
    raise SystemExit("Python falconpy library is required.\n"
                     "Install with: python3 -m pip install crowdstrike-falconpy"
                     ) from err

# Process command line arguments
parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
req = parser.add_argument_group("required arguments")

req.add_argument("--falcon_client_id",
                 help="CrowdStrike Falcon API Client ID",
                 required=True
                 )

req.add_argument("--falcon_client_secret",
                 help="CrowdStrike Falcon API Client Secret",
                 required=True
                 )

req.add_argument("--proxy_hostname",
                 help="CrowdStrike Falcon proxy hostname/FQDN",
                 required=False
                 )

req.add_argument("--proxy_port",
                 help="CrowdStrike Falcon proxy port number",
                 required=False
                 )

req.add_argument("--proxy_disable",
                 help="Flag to delete proxy config and disable proxy",
                 action='store_true',
                 required=False
                 )

req.add_argument("--scope",
                 help="Which hosts to change, can be 'cid' or 'hostgroup'",
                 choices=['cid', 'hostgroup'],
                 required=True
                 )

req.add_argument("--scope_id",
                 help="CID or Host Group ID",
                 required=True
                 )

req.add_argument("-b", "--base_url",
                    help="CrowdStrike base URL (only required for GovCloud, pass usgov1)",
                    required=False,
                    default="auto"
                    )

args = parser.parse_args()

if args.scope.lower() not in ["cid", "hostgroup"]:
    log("The scope needs to be 'cid' or 'hostgroup'")
    raise SystemExit("The scope needs to be 'cid' or 'hostgroup'")




# Main routine
def main():  # pylint: disable=R0912,R0915,C0116
    log("Starting execution of ProxyTool")

    log("Authenticating to API")
    auth = OAuth2(client_id=args.falcon_client_id,
                  client_secret=args.falcon_client_secret,
                  base_url=args.base_url
                  )

    # Check which CID the API client is operating in, as sanity check. Exit if operating CID does not match provided scope_id.
    falcon = SensorDownload(auth_object=auth, base_url=args.base_url)
    response = falcon.get_sensor_installer_ccid()

    if response["status_code"] < 300:
        log(f"-- Authentication correct.")
    else:
        log(f"-- Authentication error: {response['status_code']} - {response['body']['errors'][0]['message']}")
        raise SystemExit(f"-- Authentication error: {response['status_code']} - {response['body']['errors'][0]['message']}")

    current_cid = response["body"]["resources"][0][:-3]
    if (args.scope.lower() == "cid" and (args.scope_id.lower() != current_cid.lower())):
        log(f"The entered CID [{args.scope_id.upper()}] does not match the API client CID [{current_cid.upper()}].")
        raise SystemExit(f"The entered CID [{args.scope_id.upper()}] does not match the API client CID [{current_cid.upper()}].")   


    # Fetch list of hosts
    if args.scope.lower() == "cid":
        log(f"Getting all hosts from CID [{args.scope_id}]")
        falcon = Hosts(auth_object=auth, base_url=args.base_url)
    else:
        log(f"Getting all hosts from host group ID [{args.scope_id}]")
        falcon = HostGroup(auth_object=auth, base_url=args.base_url)


    offset = ""
    hosts_all = []

    while True:
        batch_size = 5000 # 5000 is max supported by API

        if args.scope.lower() == "cid":
            # Fetch all Windows CID hosts
            response = falcon.query_devices_by_filter_scroll(offset=offset,
                                                             limit=batch_size,
                                                             filter="platform_name:'Windows'"
                                                             )

        else:
            # Fetch all Windows host group ID hosts
            if offset == "":
                response = falcon.query_group_members(limit=batch_size,
                                                      filter="platform_name:'Windows'",
                                                      id=args.scope_id
                                                      )
            else:
                response = falcon.query_group_members(offset=offset,
                                                      limit=batch_size,
                                                      filter="platform_name:'Windows'",
                                                      id=args.scope_id
                                                      )

        offset = response['body']['meta']['pagination']['offset']

        for host_id in response['body']['resources']:
            hosts_all.append(host_id)

        log(f"-- Fetched {len(response['body']['resources'])} hosts, "
            f"{len(hosts_all)}/{response['body']['meta']['pagination']['total']}"
            )

        if len(hosts_all) >= int(response['body']['meta']['pagination']['total']):
            break

    log(f"-- Retrieved a total of {str(len(hosts_all))} hosts")


    # Now that we have the host IDs, we create a batch RTR list of commands to execute it in all hosts

    falcon = RealTimeResponse(auth_object=auth, base_url=args.base_url)

    # Get batch id

    response = falcon.batch_init_sessions(host_ids=hosts_all, queue_offline=True)
    batch_id = response['body']['batch_id']

    if batch_id:
        log(f"Initiated RTR batch with id {batch_id}")
    else:
        raise SystemExit("Unable to initiate RTR session with hosts.")


    # Commands to change proxy config

    registry_stores = [
        r"HKLM:\SYSTEM\Crowdstrike\{9b03c1d9-3138-44ed-9fae-d9f4c034b88d}\{16e0423f-7058-48c9-a204-725362b67639}\Default",
        r"HKLM:\SYSTEM\CurrentControlSet\Services\CSAgent\Sim"
        ]

    if not args.proxy_disable:
        # Setting new proxy settings
        # Delete DisableProxy, PAC, PN, PP in both locations. Change CsProxyHostname and CsProxyport with new values

        registry_keys_to_delete = ["DisableProxy", "PAC", "PN", "PP"]

        for store in registry_stores:
            for key in registry_keys_to_delete:
                response = falcon.batch_active_responder_command(batch_id=batch_id,
                                                                 base_command="reg delete",
                                                                 command_string=f"reg delete {store} {key}"
                                                                 )
                if response["status_code"] == 201:
                    log(f"-- Issuing registry deletion for {key} in {store}")
                else:
                    raise SystemExit(f"Error, Response: {response['status_code']} - {response.text}")
            cmd_string = f"reg set {store} CsProxyHostname -ValueType=REG_SZ -Value={args.proxy_hostname}"
            response = falcon.batch_active_responder_command(batch_id=batch_id,
                                                             base_command="reg set",
                                                             command_string=cmd_string
                                                             )
            if response["status_code"] == 201:
                log(f"-- Issuing registry setting of CsProxyHostname to {args.proxy_hostname} in {store}")
            else:
                raise SystemExit(f"Error, Response: {response['status_code']} - {response.text}")

            cmd_string = f"reg set {store} CsProxyport -ValueType=REG_DWORD -Value={args.proxy_port}"
            response = falcon.batch_active_responder_command(batch_id=batch_id,
                                                             base_command="reg set",
                                                             command_string=cmd_string
                                                             )
            if response["status_code"] == 201:
                log(f"-- Issuing registry setting of CsProxyport to {args.proxy_port} in {store}")
            else:
                raise SystemExit(f"Error, Response: {response['status_code']} - {response.text}")
    else:
        # Deleting and disabling proxy config
        # Delete PAC, PN, PP, CsProxyHostname, CsProxyport in both locations. Set DisableProxy with a non-zero value

        registry_keys_to_delete = ["PAC", "PN", "PP", "CsProxyHostname", "CsProxyport"]

        for store in registry_stores:
            for key in registry_keys_to_delete:
                response = falcon.batch_active_responder_command(batch_id=batch_id,
                                                                 base_command="reg delete",
                                                                 command_string=f"reg delete {store} {key}"
                                                                 )
                if response["status_code"] == 201:
                    log(f"-- Issuing registry deletion for {key} in {store}")
                else:
                    raise SystemExit(f"Error, Response: {response['status_code']} - {response.text}")
            cmd_string = f"reg set {store} DisableProxy -ValueType=REG_DWORD -Value=1"
            response = falcon.batch_active_responder_command(batch_id=batch_id,
                                                             base_command="reg set",
                                                             command_string=cmd_string
                                                             )
            if response["status_code"] == 201:
                log(f"-- Issuing registry setting of DisableProxy to a non-zero value in {store}")
            else:
                raise SystemExit(f"Error, Response: {response['status_code']} - {response.text}")

    log("-- Finished launching RTR commands, please check progress in the RTR audit logs")
    log("End")

if __name__ == "__main__":
    main()
