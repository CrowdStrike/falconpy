r"""Remove sensors by name or AID sample.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |        FalconPy v1.2
`-------'                         `-------'

 __ __   ___    _____ ______      ____  ____   __ __  ____     ___  ____
|  T  T /   \  / ___/|      T    |    \|    \ |  T  T|    \   /  _]|    \
|  l  |Y     Y(   \_ |      |    |  o  )  D  )|  |  ||  _  Y /  [_ |  D  )
|  _  ||  O  | \__  Tl_j  l_j    |   _/|    / |  |  ||  |  |Y    _]|    /
|  |  ||     | /  \ |  |  |      |  |  |    \ |  :  ||  |  ||   [_ |    \
|  |  |l     ! \    |  |  |      |  |  |  .  Yl     ||  |  ||     T|  .  Y
l__j__j \___/   \___j  l__j      l__j  l__j\_j \__,_jl__j__jl_____jl__j\_j

Removes hosts by hostname or AID. Can restore hosts that have been removed.

02.11.23 - jshcodes@CrowdStrike
"""
from argparse import ArgumentParser, RawTextHelpFormatter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from os.path import exists
from tabulate import tabulate
from falconpy import Hosts


MAX_RECORDS_PER_CALL = 5000
TABLE_HEADERS = {
    "device_id": "ID",
    "hostname": "Hostname",
    "platform_name": "Platform",
    "os_version": "Version",
    "last_seen": "Last Seen"
}


def consume_arguments():
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-b", "--base_url",
                        help="CrowdStrike Region (us1, us2, eu1, usgov1)\n"
                        "Only required for GovCloud users.",
                        required=False,
                        default="auto"
                        )
    parser.add_argument("-f", "--find",
                        help="Hostname or AID string to use to identify hosts for removal.\n"
                        "Hostname searches are stemmed, AID searches must be an exact match.",
                        required=False,
                        default=None
                        )
    parser.add_argument("-r", "--restore",
                        help="Restores prevously deleted hosts using a save file or list of AIDs.\n"
                        "Specify the AID list or filename using the `-a` command line argument.",
                        required=False,
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-a", "--aids",
                        help="List of AIDs to restore (comma delimited string or a filename).",
                        required=False
                        )
    parser.add_argument("-d", "--delete",
                        help="Perform the delete, default behavior is to list only.",
                        required=False,
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-m", "--mssp",
                        help="CID of a child tenant to access (MSSP only).",
                        required=False,
                        default=None
                        )
    requir = parser.add_argument_group("required arguments")
    requir.add_argument("-k", "--falcon_client_id",
                        help="CrowdStrike Falcon API client ID.",
                        required=True
                        )
    requir.add_argument("-s", "--falcon_client_secret",
                        help="CrowdStrike Falcon API client secret.",
                        required=True
                        )

    return parser.parse_args()


def hide_hosts(host_list: list, sdk: Hosts):
    """Hide the hosts provided in the host list."""
    def do_delete(id_list):
        """Perform threaded host delete."""
        res = sdk.perform_action(action_name="hide_host", ids=id_list)
        if res["status_code"] == 202:
            print(f"{len(id_list)} hosts removed successfully.")
        else:
            errs = []
            for err in res["body"]["errors"]:
                errs.append(f"[{err['code']}] {err['message']}")
            print("\n".join(errs))

    tstamp = str(int(datetime.now().timestamp()))
    with open(f"{tstamp}.dlt", "w", encoding="utf-8") as save_file:
        for aid in host_list:
            save_file.write(f"{aid}\n")
    # Only 100 hosts can be removed at a time
    batches = [host_list[i:i+100] for i in range(0, len(host_list), 100)]
    with ThreadPoolExecutor() as executor:
        executor.map(do_delete, batches)
    print(f"List of removed hosts saved to '{tstamp}.dlt'.")


def unhide_hosts(host_list: list, sdk: Hosts):
    """Restore the hosts provided in the host list."""
    def do_restore(id_list):
        """Perform threaded host restore."""
        res = sdk.perform_action(action_name="unhide_host", ids=id_list)
        if res["status_code"] == 202:
            print(f"{len(id_list)} hosts restored successfully.")
        else:
            errs = []
            for err in res["body"]["errors"]:
                errs.append(f"[{err['code']}] {err['message']}")
            print("\n".join(errs))
    # Only 100 hosts can be restored at a time
    batches = [host_list[i:i+100] for i in range(0, len(host_list), 100)]
    with ThreadPoolExecutor() as executor:
        executor.map(do_restore, batches)


def get_host_list(sdk: Hosts, hostname, max_limit):
    """Get a list of all hosts."""
    all_host_ids = []
    hosts_found = []
    running = True
    offset = None
    filter_string = f"hostname:*'*{hostname}*',device_id:'{hostname}'"
    while running:
        host_lookup = sdk.query_devices_by_filter_scroll(limit=max_limit,
                                                         offset=offset,
                                                         sort="last_seen.desc",
                                                         filter=filter_string
                                                         )
        if host_lookup["status_code"] != 200:
            raise SystemExit("Unable to retrieve list of hosts from the CrowdStrike API.")
        if host_lookup["body"]["resources"]:
            all_host_ids.extend(host_lookup["body"]["resources"])
            details = sdk.get_device_details(host_lookup["body"]["resources"])["body"]["resources"]
            for host in details:
                result = {
                    "device_id": host["device_id"],
                    "hostname": host.get("hostname", "Not found"),
                    "platform_name": host.get("platform_name", "Not found"),
                    "os_version": host.get("os_version", "Not found"),
                    "last_seen": host["last_seen"]
                }
                hosts_found.append(result)

        offset = host_lookup["body"]["meta"]["pagination"]["offset"]
        if host_lookup["body"]["meta"]["pagination"]["total"] <= len(all_host_ids):
            running = False

    return hosts_found, all_host_ids


if __name__ == "__main__":
    cmd_line = consume_arguments()
    # Connect to the CrowdStrike API Hosts service collection
    hosts = Hosts(client_id=cmd_line.falcon_client_id,
                  client_secret=cmd_line.falcon_client_secret,
                  base_url=cmd_line.base_url,
                  member_cid=cmd_line.mssp
                  )
    # Restore hosts
    if cmd_line.restore:
        if exists(cmd_line.aids):
            print(f"Restoring hosts from {cmd_line.aids}.")
            with open(cmd_line.aids, "r", encoding="utf-8") as load_file:
                restores = [line.rstrip() for line in load_file]
                unhide_hosts(restores, hosts)
        else:
            unhide_hosts(cmd_line.aids.split(","), hosts)
        # Return a list of all identified hosts after performing a restore
        cmd_line.find = "*"
    # No action specified
    if not cmd_line.find and not cmd_line.restore:
        raise SystemExit(
            "Specify a hostname or AID string using the `-f` argument in order to remove hosts."
            )
    # Retrieve all hosts matching our search
    found, host_ids = get_host_list(hosts, cmd_line.find, MAX_RECORDS_PER_CALL)
    # Display the results
    if not found:
        raise SystemExit("\nNo hosts identified.")
    print(tabulate(tabular_data=found, headers=TABLE_HEADERS))
    # Remove hosts
    if not cmd_line.restore:
        if cmd_line.delete:
            if cmd_line.find.strip() == "*":
                raise SystemExit("\nUnacceptable search string provided for delete processing.")
            print(f"\nRemoving {len(found)} hosts.")
            hide_hosts(host_ids, hosts)
        else:
            print(f"\n{len(found)} hosts identified.")
            if cmd_line.find.strip() != "*":
                print("No action performed. Pass `-d` on the command line to remove these hosts.")
