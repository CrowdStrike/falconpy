r"""Duplicate sensor detection and removal.

 ______               __ __            __           ______         __              __
|   _  \ .--.--.-----|  |__.----.---.-|  |_.-----. |   _  \ .-----|  |_.-----.----|  |_.-----.----.
|.  |   \|  |  |  _  |  |  |  __|  _  |   _|  -__| |.  |   \|  -__|   _|  -__|  __|   _|  _  |   _|
|.  |    |_____|   __|__|__|____|___._|____|_____| |.  |    |_____|____|_____|____|____|_____|__|
|:  1    /     |__|                                |:  1    /
|::.. . /                                          |::.. . /            CrowdStrike FalconPy v1.2
`------'                                           `------'

01.25.23 - jshcodes@CrowdStrike
"""
from argparse import ArgumentParser, RawTextHelpFormatter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from json import loads, dumps
from os.path import exists
from tabulate import tabulate
from falconpy import Hosts


MAX_RECORDS_PER_CALL = 5000
TABLE_HEADERS = {
    "device_id": "ID",
    "hostname": "Hostname",
    "mac_address": "MAC Address",
    "platform_name": "Platform",
    "os_version": "Version",
    "first_seen": "First Seen",
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
    parser.add_argument("-d", "--delete_duplicates",
                        help="Remove duplicate hosts from the CrowdStrike console.",
                        action="store_true",
                        required=False,
                        default=False
                        )
    parser.add_argument("-r", "--restore_duplicates",
                        help="Restores prevously deleted duplicates using a save file.",
                        required=False,
                        default=None
                        )
    parser.add_argument("-a", "--all",
                        help="Display all hosts, not just duplicates.",
                        action="store_true",
                        required=False,
                        default=False
                        )
    parser.add_argument("-m", "--mssp",
                        help="CID of a child tenant to access.",
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
            print(f"{len(id_list)} duplicate hosts removed successfully.")
        else:
            errs = []
            for err in res["body"]["errors"]:
                errs.append(f"[{err['code']}] {err['message']}")
            print("\n".join(errs))

    tstamp = str(int(datetime.now().timestamp()))
    with open(f"{tstamp}.dlt", "w", encoding="utf-8") as save_file:
        for aid in host_list:
            save_file.write(f"{aid}\n")
    batches = [host_list[i:i+100] for i in range(0, len(host_list), 100)]
    with ThreadPoolExecutor() as executor:
        executor.map(do_delete, batches)
    print(f"List of removed duplicates saved to '{tstamp}.dlt'.")


def unhide_hosts(host_list: list, sdk: Hosts):
    """Restore the hosts provided in the host list."""
    def do_restore(id_list):
        """Perform threaded host restore."""
        res = sdk.perform_action(action_name="unhide_host", ids=id_list)
        if res["status_code"] == 202:
            print(f"{len(id_list)} duplicate hosts restored successfully.")
        else:
            errs = []
            for err in res["body"]["errors"]:
                errs.append(f"[{err['code']}] {err['message']}")
            print("".join(errs))
    batches = [host_list[i:i+100] for i in range(0, len(host_list), 100)]
    with ThreadPoolExecutor() as executor:
        executor.map(do_restore, batches)


def get_host_list(sdk: Hosts, max_limit):
    """Get a list of all hosts."""
    all_host_ids = []
    hosts_found = []
    running = True
    offset = None
    while running:
        host_lookup = sdk.query_devices_by_filter_scroll(limit=max_limit,
                                                         offset=offset,
                                                         sort="last_seen.desc"
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
                    "mac_address": host.get("mac_address", "Not found"),
                    "platform_name": host.get("platform_name", "Not found"),
                    "os_version": host.get("os_version", "Not found"),
                    "first_seen": host["first_seen"],
                    "last_seen": host["last_seen"]
                }
                hosts_found.append(result)

        offset = host_lookup["body"]["meta"]["pagination"]["offset"]
        if host_lookup["body"]["meta"]["pagination"]["total"] <= len(all_host_ids):
            running = False

    return hosts_found, all_host_ids


def identify_duplicates(full: list, model: dict):
    """Compare each host in the list for duplicates."""
    full = sorted(full,
                  key=lambda k: (k["hostname"], k["mac_address"], k["os_version"], k["last_seen"]),
                  reverse=True
                  )
    last = model
    last.pop("device_id")
    last.pop("last_seen")
    last.pop("first_seen")
    dupeids = []
    dupelist = []
    for host in full:
        save = loads(dumps(host))  # Quick deepcopy
        save.pop("device_id")
        save.pop("last_seen")
        save.pop("first_seen")
        if save == last:
            host["hostname"] = f"{host['hostname']} (DUPLICATE)"
            dupeids.append(host["device_id"])
            dupelist.append(host)
        last = save

    return full, dupeids, dupelist


if __name__ == "__main__":
    cmd_line = consume_arguments()

    hosts = Hosts(client_id=cmd_line.falcon_client_id,
                client_secret=cmd_line.falcon_client_secret,
                base_url=cmd_line.base_url,
                member_cid=cmd_line.mssp
                )

    if cmd_line.restore_duplicates:
        if not exists(cmd_line.restore_duplicates):
            raise SystemExit("Unable to find file containing list of IDs to restore!")
        print(f"Restoring duplicates from {cmd_line.restore_duplicates}.")
        with open(cmd_line.restore_duplicates, "r", encoding="utf-8") as load_file:
            restores = [line.rstrip() for line in load_file]
            unhide_hosts(restores, hosts)

    found, host_ids = get_host_list(hosts, MAX_RECORDS_PER_CALL)
    found, duplicate_ids, dupe_list = identify_duplicates(found, TABLE_HEADERS)
    print(tabulate(tabular_data=found if cmd_line.all else dupe_list, headers=TABLE_HEADERS))
    total = f"{len(duplicate_ids)} duplicate{'s' if len(duplicate_ids) > 1 else ''}"
    total = f"{total} identified within {len(host_ids)} total hosts found."
    print(total)
    if cmd_line.delete_duplicates and not cmd_line.restore_duplicates:
        print(f"Removing {len(duplicate_ids)} duplicates.")
        hide_hosts(duplicate_ids, hosts)
