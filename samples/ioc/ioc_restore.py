"""Restore deleted IOCs.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

╦╔═╗╔═╗  ╦═╗┌─┐┌─┐┌┬┐┌─┐┬─┐┌─┐
║║ ║║    ╠╦╝├┤ └─┐ │ │ │├┬┘├┤
╩╚═╝╚═╝  ╩╚═└─┘└─┘ ┴ └─┘┴└─└─┘

This sample demonstrates restoring previously deleted IOCs.

~~~ API Scope Requirements ~~~
IOC Management - Read / Write
IOCs (Indicators of Compromise) - Read / Write

Creation date: 11.06.2024 - am-cs-se@CrowdStrike
Modification: 11.07.2024 - jshcodes@CrowdStrike
"""
import os
import logging
from argparse import ArgumentParser, RawDescriptionHelpFormatter, Namespace, ArgumentTypeError
from datetime import datetime
from tabulate import tabulate
from falconpy import HostGroup, IOC, Result


class FalconIOCRestore:
    """Class to handle API interactions."""

    def __init__(self, cmd: Namespace):
        """Construct an instance of the class."""
        if cmd.debug:
            logging.basicConfig(level=logging.DEBUG)
        self.api: IOC = IOC(client_id=cmd.client_id,
                            client_secret=cmd.client_secret,
                            base_url=cmd.base_url,
                            debug=cmd.debug,
                            pythonic=True
                            )
        self.hg_api: HostGroup = HostGroup(auth_object=self.api)
        self.target_date: str = cmd.date
        self.modified_by: str = cmd.modified_by
        self.host_group: str = cmd.hostgroup
        self.group_name: str = cmd.groupname

    def get_host_group_id(self):
        """Return the ID of the specified host group."""
        # Host Group names must be searched in LOWERCASE regardless of the actual case of the name
        hg_id = self.hg_api.query_host_groups(filter=f"name:'{self.group_name.lower()}'").data
        if not hg_id:
            raise SystemExit("Invalid Host Group name specified.")
        self.host_group = hg_id[0]

    def check_ioc_exists(self, ioc_type, ioc_value):
        """Check if an IOC already exists."""
        filter_query = f"type:'{ioc_type}'+value:'{ioc_value}'+deleted:false"
        response: Result = self.api.indicator_search(filter=filter_query)
        returned = False
        if response.status_code == 200:
            returned = bool(len(response.data) > 0)

        return returned

    def get_deleted_iocs(self):  # pylint: disable=R0912
        """Get a list of deleted IOCs from specific date and modifier."""
        filter_query = (f"deleted:true"
                        f"+modified_on:>='{self.target_date}T00:00:00Z'"
                        f"+modified_on:<='{self.target_date}T23:59:59Z'"
                        )
        if self.modified_by:
            filter_query = f"{filter_query}+modified_by:'{self.modified_by}'"

        if self.host_group:
            filter_query = f"{filter_query}+host_groups:['{self.host_group}']"
        else:
            filter_query = f"{filter_query}+applied_globally:true"

        after = None
        all_ioc_ids = []

        delete_msg = f"Querying for IOCs modified on {self.target_date}"
        if self.modified_by:
            delete_msg = f"{delete_msg} by {self.modified_by}..."
        else:
            delete_msg = f"{delete_msg}..."
        print(delete_msg)

        while True:
            response: Result = self.api.indicator_search(filter=filter_query,
                                                         limit=1000,
                                                         after=after
                                                         )

            if response.status_code == 200:
                ioc_ids = response.data
                all_ioc_ids.extend(ioc_ids)
                if response.after and ioc_ids:
                    after = response.after
                else:
                    break
            else:
                raise SystemExit(f"API request failed: {response.errors}")

        if not all_ioc_ids:
            print("No deleted IOCs found for the specified criteria")
            return []

        all_iocs = []
        chunk_size = 100
        for i in range(0, len(all_ioc_ids), chunk_size):
            id_list = all_ioc_ids[i:i + chunk_size]
            detail_response: Result = self.api.indicator_get(ids=id_list)
            if detail_response.status_code == 200:
                all_iocs.extend(detail_response.data)
            else:
                print(f"Detail request failed for chunk {i//chunk_size + 1}: "
                      f"{detail_response.status_code}"
                      )
                print(f"Detail response: {detail_response.errors}")

        return all_iocs

    def restore_ioc(self, ioc):
        """Restore a single IOC."""
        if self.check_ioc_exists(ioc.get('type'), ioc.get('value')):
            return False, "IOC already exists (skipping)"

        platforms = ioc.get('platforms', ['windows'])
        if isinstance(platforms, str):
            platforms = [platforms]

        indicator = {
            "type": ioc.get('type'),
            "value": ioc.get('value'),
            "action": ioc.get('action', 'prevent'),
            "severity": ioc.get('severity', 'high'),
            "platforms": platforms,
            "source": ioc.get('source', 'API Restoration'),
            "description": ioc.get('description', f"Restored {ioc.get('type')} indicator")
        }
        if self.host_group:
            indicator["host_groups"] = [self.host_group]
        else:
            indicator["applied_globally"] = True

        request_body = {
            "comment": f"Restored deleted IOC: {ioc.get('value')} ({ioc.get('type')})",
            "indicators": [indicator],
        }

        response: Result = self.api.indicator_create(**request_body)

        if response.status_code == 201:
            return True, "Successfully restored"

        if response.status_code == 400:
            print("\nRetrying with ignore_warnings enabled...")
            response = self.api.indicator_update(**request_body, ignore_warnings=True)
            if response.status_code == 201:
                return True, "Successfully restored with warnings ignored"

        error_message = response.errors
        return False, f"Failed to restore: {error_message}"


def valid_date(strdate: str) -> datetime:
    """Confirm the command line provided date is valid."""
    try:
        return datetime.strptime(strdate, "%Y-%m-%d")
    except ValueError as bad_date:
        raise ArgumentTypeError(f"not a valid date: {strdate!r}") from bad_date


def consume_arguments():
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        default=False,
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-c", "--client_id",
                        help="CrowdStrike API client ID",
                        default=os.getenv("FALCON_CLIENT_ID"),
                        required=False
                        )
    parser.add_argument("-k", "--client_secret",
                        help="CrowdStrike API client secret",
                        default=os.getenv("FALCON_CLIENT_SECRET"),
                        required=False
                        )
    parser.add_argument("-b", "--base_url",
                        help="CrowdStrike Region (US1, US2, EU1, USGOV1, USGOV2) \n"
                             "Full URL is also supported.",
                        required=False,
                        default="auto"
                        )
    parser.add_argument("-dt", "--date",
                        help="Date to target (YYYY-MM-DD)",
                        default=datetime.now().strftime("%Y-%m-%d"),
                        required=False,
                        type=valid_date
                        )
    parser.add_argument("-m", "--modified_by",
                        help="User who modified the deleted IOCs",
                        required=False,
                        default=None
                        )
    parser.add_argument("-hg", "--hostgroup",
                        help="ID of the Host Group associated with the IOC\n"
                             "Not required when --groupname is specified.",
                        required=False,
                        default=None
                        )
    parser.add_argument("-g", "--groupname",
                        help="Name of the Host Group associated with the IOC\n"
                             "Not required when --hostgroup is specified.",
                        required=False,
                        default=None
                        )
    parser.add_argument("-l", "--list",
                        help="List deleted IOCs but take no action",
                        default=False,
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-t", "--table-format",
                        dest="table_format",
                        help="Tabular display format",
                        required=False,
                        default="simple"
                        )

    parsed = parser.parse_args()
    parsed.date = str(parsed.date).split(" ", maxsplit=1)[0]

    return parsed


def main():  # pylint: disable=R0912,R0915
    """Execute the main routine."""
    cmd_line = consume_arguments()
    falcon = FalconIOCRestore(cmd_line)
    if falcon.group_name:
        falcon.get_host_group_id()
    deleted_iocs = falcon.get_deleted_iocs()

    if deleted_iocs and not cmd_line.list:
        print(f"\nFound {len(deleted_iocs)} deleted IOCs for {cmd_line.date} "
              f"modified by {cmd_line.modified_by}"
              )
        print("-" * 100)

        successful_restores = 0
        failed_restores = 0
        skipped_restores = 0
        failed_details = []

        for ioc in deleted_iocs:
            print("\nProcessing IOC:")
            print(f"Type: {ioc.get('type')}")
            print(f"Value: {ioc.get('value')}")
            print(f"Action: {ioc.get('action', 'prevent')}")
            print(f"Severity: {ioc.get('severity', 'high')}")
            print(f"Platforms: {', '.join(ioc.get('platforms', ['windows']))}")
            print(f"Modified On: {ioc.get('modified_on')}")
            print(f"Modified By: {ioc.get('modified_by')}")

            success, message = falcon.restore_ioc(ioc)

            if success:
                successful_restores += 1
                print("✓ Successfully restored")
            elif "already exists" in message:
                skipped_restores += 1
                print(f"⚠ {message}")
            else:
                failed_restores += 1
                failed_details.append(f"{ioc.get('value')} - {message}")
                print(f"✗ Failed to restore: {message}")

            print("-" * 100)

        print("\nRestoration Summary:")
        print(f"Total IOCs processed: {len(deleted_iocs)}")
        print(f"Successfully restored: {successful_restores}")
        print(f"Skipped (already exist): {skipped_restores}")
        print(f"Failed to restore: {failed_restores}")

        if failed_details:
            print("\nFailed IOCs details:")
            for detail in failed_details:
                print(f"- {detail}")
    elif deleted_iocs and cmd_line.list:
        display_keys = {"id": "ID",
                        "type": "Type",
                        "value": "Value",
                        "action": "Action",
                        "severity": "Severity",
                        "target": "Target",
                        "modification": "Modification"
                        }
        pop_keys = ["source",
                    "mobile_action",
                    "description",
                    "expired",
                    "platforms",
                    "host_groups",
                    "deleted",
                    "applied_globally",
                    "from_parent",
                    "created_on",
                    "created_by",
                    "modified_on",
                    "modified_by"
                    ]
        show_iocs = []
        for ioc in deleted_iocs:
            if ioc.get("applied_globally"):
                ioc["target"] = "Global"
            else:
                ioc["target"] = falcon.hg_api.get_host_groups(
                    ids=falcon.host_group
                    ).data[0].get("name")
            ioc["modification"] = f"{ioc['modified_by']}\n{ioc['modified_on']}"
            if ioc["expired"]:
                ioc["id"] = f"{ioc['id']}\nEXPIRED"
            for key in pop_keys:
                ioc.pop(key)
            show_iocs.append(ioc)
        print(tabulate(show_iocs, headers=display_keys, tablefmt=cmd_line.table_format))
    else:
        print(f"No deleted IOCs found for the specified criteria on {cmd_line.date}")


if __name__ == "__main__":
    main()
