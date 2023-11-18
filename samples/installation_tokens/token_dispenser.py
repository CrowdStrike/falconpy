r"""Installation Token management utility.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |       FalconPy v1.3.4
`-------'                         `-------'

_______  _____  _     _ _______ __   _
   |    |     | |____/  |______ | \  |
   |    |_____| |    \_ |______ |  \_|

______  _____ _______  _____  _______ __   _ _______ _______  ______
|     \   |   |______ |_____] |______ | \  | |______ |______ |_____/
|_____/ __|__ ______| |       |______ |  \_| ______| |______ |    \_

               .-------.            with    ________)
               |Jackpot|                   (, /     /) ,     /)
   ____________|_______|____________         /___, //    _  (/  _/_
  |  __    __    ___  _____   __    |     ) /     (/__(_(_/_/ )_(__
  | / _\  / /   /___\/__   \ / _\   |    (_/           .-/
  | \ \  / /   //  //  / /\ \\ \  25|                 (_/  )   ___
  | _\ \/ /___/ \_//  / /  \/_\ \ []|  __                 (__/_____)                   /)
  | \__/\____/\___/   \/     \__/ []| (__)                  /       _____  _/_ __  ___//
  |===_______===_______===_______===|  ||                  /       (_) / (_(__/ (_(_)(/_
  ||*| _____ |*|       |*|  ___  |*||  ||                 (______)
  ||*||     ||*|  /\ _ |*| |_  | |*||  ||
  ||*||*BAR*||*|  \_(_)|*|  / /  |*||  ||
  ||*||_____||*|  (_)  |*| /_/   |*||  ||
  ||*|_______|*|_______|*|_______|*||_//                 Creation date: 11.15.2023
  | \=___________________________=/ |_/                       jshcodes@CrowdStrike
 _|    \_______________________/    |_                            WE STOP BREACHES
(_____________________________________)
"""
#  _____ _______  _____   _____   ______ _______ _______
#    |   |  |  | |_____] |     | |_____/    |    |______
#  __|__ |  |  | |       |_____| |    \_    |    ______|
#
import sys
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter, _SubParsersAction
from copy import deepcopy
from csv import writer
from datetime import datetime, timedelta
from json import dump
from logging import basicConfig, DEBUG
from os import getenv
from secrets import randbelow
from time import sleep
from typing import Tuple, Callable, List, Dict
try:
    from pyfiglet import figlet_format
except ImportError as no_figlet:
    raise SystemExit("The pyfiglet library is required to use this program.") from no_figlet
try:
    from tabulate import tabulate
except ImportError as no_tabulate:
    raise SystemExit("The tabulate library is required to use this program.") from no_tabulate
try:
    from falconpy import (
        APIError,
        InstallationTokens,
        SensorDownload,
        FlightControl,
        Result,
        version
        )
except ImportError as no_falconpy:
    raise SystemExit("The CrowdStrike FalconPy library (version 1.3.4 or greater) is required "
                     "to use this program."
                     ) from no_falconpy


#   _____   _____  _______ _____  _____  __   _ _______
#  |     | |_____]    |      |   |     | | \  | |_____| |
#  |_____| |          |    __|__ |_____| |  \_| |     | |_____
#  _______  ______  ______ _     _ _______ _______ __   _ _______ _______
#  |_____| |_____/ |  ____ |     | |  |  | |______ | \  |    |    |______
#  |     | |    \_ |_____| |_____| |  |  | |______ |  \_|    |    ______|
#
def add_opt_arguments(sbp: ArgumentParser) -> ArgumentParser:
    """Add shared optional arguments to the provided command line argument subparser."""
    sbp.add_argument("-d", "--debug", help="Enable debug.", default=False, action="store_true")
    sbp.add_argument("-f", "--filter",
                     help="Filter results by searching token labels (stemmed search)."
                     )
    sbp.add_argument("-o", "--order-by",
                     help="Sort key to use for tabular displays.",
                     dest="order_by",
                     default="label"
                     )
    sbp.add_argument("-r", "--reverse",
                     help="Reverses the sort order.",
                     default=False,
                     action="store_true"
                     )
    sbp.add_argument("-t", "--table-format",
                     dest="table_format",
                     help="Format to use for tabular output.",
                     default="simple"
                     )
    sbp.add_argument("-v", "--show-version",
                     dest="show_version",
                     help="Show FalconPy version in output.",
                     default=False,
                     action="store_true"
                     )
    sbp.add_argument("--output-file",
                     dest="output_file",
                     help="Output token list results to a CSV or JSON file.",
                     default=None
                     )
    sbp.add_argument("--output-format",
                     dest="output_format",
                     help="Set output file format.",
                     default="csv",
                     choices=["csv", "json"]
                     )
    auth = sbp.add_argument_group("authentication arguments "
                                  "(not required if using environment authentication)")
    auth.add_argument("-k", "--client_id",
                      help="Falcon API client ID",
                      default=getenv("FALCON_CLIENT_ID")
                      )
    auth.add_argument("-s", "--client_secret",
                      help="Falcon API client secret",
                      default=getenv("FALCON_CLIENT_SECRET")
                      )
    mssp = sbp.add_argument_group("mssp arguments")
    mssp.add_argument("-c", "--child",
                      dest="child",
                      help="CID of the child tenant to target.",
                      default=None
                      )
    mssp.add_argument("-m", "--mssp",
                      dest="mssp",
                      help="Flight Control (MSSP) mode.",
                      default=False,
                      action="store_true"
                      )
    mssp.add_argument("--skip-parent",
                      dest="skip_parent",
                      help="Do not take action within the parent tenant.",
                      action="store_true",
                      default=False
                      )
    mssp.add_argument("--show-tenant",
                      dest="show_tenant",
                      help="Display tenant CID values.",
                      action="store_true",
                      default=False
                      )
    return sbp


def add_force_argument(sbp: ArgumentParser) -> ArgumentParser:
    """Add shared optional arguments to the provided command line argument subparser."""
    sbp.add_argument("--force",
                     help="Perform the operation without asking for confirmation.",
                     action="store_true",
                     default=False
                     )
    return sbp


def extra_args(subp: ArgumentParser) -> ArgumentParser:
    """Add in optional arguments along with the force argument."""
    subp = add_force_argument(subp)
    subp = add_opt_arguments(subp)
    return subp


#  |      _____ _______ _______
#  |        |   |______    |
#  |_____ __|__ ______|    |
#  _______  ______  ______ _     _ _______ _______ __   _ _______ _______
#  |_____| |_____/ |  ____ |     | |  |  | |______ | \  |    |    |______
#  |     | |    \_ |_____| |_____| |  |  | |______ |  \_|    |    ______|
#
def handle_list_arguments(sub: _SubParsersAction, head: str) -> ArgumentParser:
    """Handle list command arguments."""
    do_list: ArgumentParser = sub.add_parser("list",
                                             help="List all tokens [default]",
                                             aliases=["l"],
                                             description=figlet_format("List", font=head),
                                             formatter_class=RawTextHelpFormatter
                                             )
    do_list = add_opt_arguments(do_list)
    return do_list


def show_tenant_list(arg_list: Namespace, cids_to_show: list):
    """Show CIDs for all tenants searched."""
    if arg_list.mssp and arg_list.show_tenant:
        parent = False
        for kid in cids_to_show:
            if not parent:
                print(f"Tenant: {kid}")
                parent = True
            else:
                print(f"Child tenant: {kid}")


#  |      _____ _______ _______
#  |        |   |______    |
#  |_____ __|__ ______|    |
#
def show_all_tokens(sdk: InstallationTokens, cmdline: str, filter_str: str = None):
    """Display every token in the tenant (or across all tenants)."""
    hold_creds = sdk.auth_object.creds
    this_cid, cid_list = get_cid_ids(sdk, cmdline)
    show_tenant_list(cmdline, cid_list)
    token_details = []
    ptokens = []
    for cid in cid_list:
        if cid != this_cid:
            hold_creds["member_cid"] = cid
        api = sdk
        if cmdline.mssp and (len(cid_list) > 1 and ptokens):
            api = InstallationTokens(creds=hold_creds, pythonic=True, debug=cmdline.debug)
        token_details = get_all_tokens(api, cmdline, filter_str, cid, token_details)
        if cid == this_cid and not ptokens:
            ptokens = deepcopy(token_details)
    display_tokens(token_details, cmdline, ptokens)


#  _______  ______ _______ _______ _______ _______
#  |       |_____/ |______ |_____|    |    |______
#  |_____  |    \_ |______ |     |    |    |______
#  _______  ______  ______ _     _ _______ _______ __   _ _______ _______
#  |_____| |_____/ |  ____ |     | |  |  | |______ | \  |    |    |______
#  |     | |    \_ |_____| |_____| |  |  | |______ |  \_|    |    ______|
#
def handle_create_arguments(sub: _SubParsersAction, head: str) -> ArgumentParser:
    """Handle create command arguments."""
    do_create: ArgumentParser = sub.add_parser("create",
                                               help="Create tokens",
                                               aliases=["c"],
                                               description=figlet_format("Create", font=head),
                                               formatter_class=RawTextHelpFormatter
                                               )
    create_req = do_create.add_argument_group("required arguments")
    create_req.add_argument("-l", "--token-label",
                            dest="token_label",
                            help="Label for the token.",
                            required=True
                            )
    create_req.add_argument("-e", "--expiration",
                            help="Token expiration (number of days or YYYY-mm-ddTHH:MM:SSZ).",
                            required=True
                            )
    do_create.add_argument("-n", "--count", help="Number of tokens to create.", type=int, default=1)
    do_create = extra_args(do_create)
    return do_create


#  _______  ______ _______ _______ _______ _______
#  |       |_____/ |______ |_____|    |    |______
#  |_____  |    \_ |______ |     |    |    |______
#
def create_token(sdk: InstallationTokens, cmdline: Namespace):
    """Create a token with the specified expiration and label."""
    hold_creds = sdk.auth_object.creds
    this_cid, cids = get_cid_ids(sdk, cmdline)
    token_expiration = cmdline.expiration
    cids_to_process = [
        c for c in cids if (cmdline.skip_parent and not c == this_cid) or not cmdline.skip_parent
        ]
    for cid in cids_to_process:
        if cid != this_cid:
            hold_creds["member_cid"] = cid
        api = sdk
        if cmdline.mssp and len(cids) > 1:
            api = InstallationTokens(creds=hold_creds, pythonic=True, debug=cmdline.debug)
        try:
            if int(cmdline.expiration) > 0:
                token_expiration = (
                    datetime.now() + timedelta(days=int(cmdline.expiration))
                    ).strftime("%Y-%m-%dT%H:%M:%SZ")
            else:
                raise SystemExit("Token expiration days must be an integer greater than zero.")
        except ValueError:
            pass

        for num in range(1, cmdline.count+1):
            label = f"{cmdline.token_label}{num if cmdline.count > 1 else ''}"
            create_result = sdk_operation(api.tokens_create,
                                          LONG_WAIT,
                                          cmdline.debug,
                                          label=label,
                                          expires_timestamp=token_expiration
                                          )
        if create_result.errors:
            for error in create_result.errors:
                print(f"NONFATAL {error['code']} ERROR: {error['message']}")


#   ______ _______ _    _  _____  _     _ _______
#  |_____/ |______  \  /  |     | |____/  |______
#  |    \_ |______   \/   |_____| |    \_ |______
#  _______  ______  ______ _     _ _______ _______ __   _ _______ _______
#  |_____| |_____/ |  ____ |     | |  |  | |______ | \  |    |    |______
#  |     | |    \_ |_____| |_____| |  |  | |______ |  \_|    |    ______|
#
def handle_revoke_arguments(sub: _SubParsersAction, head: str) -> ArgumentParser:
    """Handle revoke command arguments."""
    do_revoke: ArgumentParser = sub.add_parser("revoke",
                                               help="Revoke tokens",
                                               aliases=["x"],
                                               description=figlet_format("Revoke", font=head),
                                               formatter_class=RawTextHelpFormatter
                                               )
    revoke_req = do_revoke.add_argument_group("required arguments (mutually exclusive)")
    revoke_grp = revoke_req.add_mutually_exclusive_group(required=True)
    revoke_grp.add_argument("-i", "--token-id", dest="token_id", help="ID of the token to revoke.")
    revoke_grp.add_argument("-l", "--token-label",
                            dest="token_label",
                            help="Label of the token to revoke (starts with match)."
                            )
    do_revoke = extra_args(do_revoke)
    return do_revoke


#   ______ _______ _______ _______  _____   ______ _______
#  |_____/ |______ |______    |    |     | |_____/ |______
#  |    \_ |______ ______|    |    |_____| |    \_ |______
#  _______  ______  ______ _     _ _______ _______ __   _ _______ _______
#  |_____| |_____/ |  ____ |     | |  |  | |______ | \  |    |    |______
#  |     | |    \_ |_____| |_____| |  |  | |______ |  \_|    |    ______|
#
def handle_restore_arguments(sub: _SubParsersAction, head: str) -> ArgumentParser:
    """Handle restore command arguments."""
    do_restore: ArgumentParser = sub.add_parser("restore",
                                                help="Restore tokens",
                                                aliases=["r"],
                                                description=figlet_format("Restore", font=head),
                                                formatter_class=RawTextHelpFormatter
                                                )
    restore_req = do_restore.add_argument_group("required arguments (mutually exclusive)")
    restore_grp = restore_req.add_mutually_exclusive_group(required=True)
    restore_grp.add_argument("-i", "--token-id",
                             dest="token_id",
                             help="ID of the token to restore."
                             )
    restore_grp.add_argument("-l", "--token-label",
                             dest="token_label",
                             help="Label of the token to restore (starts with match)."
                             )
    do_restore = extra_args(do_restore)
    return do_restore


#   ______ _______ _    _  _____  _     _ _______      _______ __   _ ______
#  |_____/ |______  \  /  |     | |____/  |______      |_____| | \  | |     \
#  |    \_ |______   \/   |_____| |    \_ |______      |     | |  \_| |_____/
#   ______ _______ _______ _______  _____   ______ _______
#  |_____/ |______ |______    |    |     | |_____/ |______
#  |    \_ |______ ______|    |    |_____| |    \_ |______
#
def token_revocation(sdk: InstallationTokens, cmdline: Namespace, revoking: bool = False):
    """Revoke a token by ID or name."""
    hold_creds = sdk.auth_object.creds
    this_cid, cids = get_cid_ids(sdk, cmdline)
    cids_to_process = [
        c for c in cids if (cmdline.skip_parent and not c == this_cid) or not cmdline.skip_parent
        ]
    for cid in cids_to_process:
        if cid != this_cid:
            hold_creds["member_cid"] = cid
        api = sdk
        if cmdline.mssp and len(cids) > 1:
            api = InstallationTokens(creds=hold_creds, pythonic=True, debug=cmdline.debug)

        if cmdline.token_id:
            revoke_result = sdk_operation(api.tokens_update,
                                          SHORT_WAIT,
                                          cmdline.debug,
                                          ids=cmdline.token_id,
                                          revoked=revoking
                                          )
            if revoke_result.errors:
                for error in revoke_result.errors:
                    print(f"NONFATAL {error['code']} ERROR: {error['message']} ({error['id']})")
        if cmdline.token_label:
            token_lookup = sdk_operation(api.tokens_query,
                                         LONG_WAIT,
                                         cmdline.debug,
                                         filter=f"label:*'{cmdline.token_label}*'"
                                         )
            if token_lookup.status_code == 200 and len(token_lookup.data):
                for returned_token_id in token_lookup.data:
                    sdk_operation(api.tokens_update,
                                  LONG_WAIT,
                                  cmdline.debug,
                                  ids=returned_token_id,
                                  revoked=revoking
                                  )
            else:
                print(f"NONFATAL 404 ERROR: Not Found ({cmdline.token_label})")


#  _     _  _____  ______  _______ _______ _______
#  |     | |_____] |     \ |_____|    |    |______
#  |_____| |       |_____/ |     |    |    |______
#  _______  ______  ______ _     _ _______ _______ __   _ _______ _______
#  |_____| |_____/ |  ____ |     | |  |  | |______ | \  |    |    |______
#  |     | |    \_ |_____| |_____| |  |  | |______ |  \_|    |    ______|
#
def handle_update_arguments(sub: _SubParsersAction, head: str) -> ArgumentParser:
    """Handle update command arguments."""
    do_update: ArgumentParser = sub.add_parser("update",
                                               help="Update tokens",
                                               aliases=["u"],
                                               description=figlet_format("Update", font=head),
                                               formatter_class=RawTextHelpFormatter
                                               )
    update_req = do_update.add_argument_group("required arguments")
    update_grp1 = update_req.add_mutually_exclusive_group(required=True)
    update_grp1.add_argument("-i", "--token-id",
                             dest="token_id",
                             help="ID of the token to update."
                             )
    update_grp1.add_argument("-l", "--token-label",
                             dest="token_label",
                             help="Label of the token to update (starts with match)."
                             )
    update_grp2 = update_req.add_mutually_exclusive_group(required=True)
    update_grp2.add_argument("-a", "--add-days",
                             help="Add specified number of days to token expiration."
                             )
    update_grp2.add_argument("-e", "--expiration", help="Token expiration (YYYY-mm-ddTHH:MM:SSZ).")
    update_grp2.add_argument("-n", "--new-label",
                             dest="new_token_label",
                             help="New label for the token."
                             )
    do_update = extra_args(do_update)
    return do_update


#  _     _  _____  ______  _______ _______ _______      ______  __   __     _____ ______
#  |     | |_____] |     \ |_____|    |    |______      |_____]   \_/         |   |     \
#  |_____| |       |_____/ |     |    |    |______      |_____]    |        __|__ |_____/
#
def update_token_by_id(sdk: InstallationTokens, cmdline: Namespace):
    """Update a token by ID."""
    hold_creds = sdk.auth_object.creds
    this_cid, cids = get_cid_ids(sdk, cmdline)
    cids_to_process = [
        c for c in cids if (cmdline.skip_parent and not c == this_cid) or not cmdline.skip_parent
        ]
    for cid in cids_to_process:
        if cid != this_cid:
            hold_creds["member_cid"] = cid
        api = sdk
        if cmdline.mssp and len(cids) > 1:
            api = InstallationTokens(creds=hold_creds, pythonic=True, debug=cmdline.debug)
        updates = {}
        if cmdline.new_token_label:
            updates["label"] = cmdline.new_token_label
        if cmdline.expiration:
            updates["expires_timestamp"] = cmdline.expiration
        if cmdline.add_days:
            exp = sdk_operation(api.tokens_read,
                                LONG_WAIT,
                                cmdline.debug,
                                ids=cmdline.token_id
                                )
            if exp.status_code == 200 and len(exp.data):
                new_exp = datetime.strptime(exp.data[0]["expires_timestamp"], "%Y-%m-%dT%H:%M:%SZ")
                updates["expires_timestamp"] = (
                    new_exp + timedelta(days=int(cmdline.add_days))
                    ).strftime("%Y-%m-%dT%H:%M:%SZ")
        if updates:
            updates["ids"] = cmdline.token_id
            update_result = sdk_operation(api.tokens_update, SHORT_WAIT, cmdline.debug, **updates)
            if update_result.errors:
                for error in update_result.errors:
                    print(f"NONFATAL {error['code']} ERROR: {error['message']} ({error['id']})")


#  _     _  _____  ______  _______ _______ _______
#  |     | |_____] |     \ |_____|    |    |______
#  |_____| |       |_____/ |     |    |    |______
#  ______  __   __            _______ ______  _______
#  |_____]   \_/       |      |_____| |_____] |______ |
#  |_____]    |        |_____ |     | |_____] |______ |_____
#
def update_token_by_label(sdk: InstallationTokens, cmdline: Namespace):
    """Update a token by label."""
    hold_creds = sdk.auth_object.creds
    this_cid, cids = get_cid_ids(sdk, cmdline)
    cids_to_process = [
        c for c in cids if (cmdline.skip_parent and not c == this_cid) or not cmdline.skip_parent
        ]
    for cid in cids_to_process:
        if cid != this_cid:
            hold_creds["member_cid"] = cid
        api = sdk
        if cmdline.mssp and len(cids) > 1:
            api = InstallationTokens(creds=hold_creds, pythonic=True, debug=cmdline.debug)
        updates = {}
        if cmdline.new_token_label:
            updates["label"] = cmdline.new_token_label
        if cmdline.expiration:
            updates["expires_timestamp"] = cmdline.expiration
        token_lookup = sdk_operation(api.tokens_query,
                                     LONG_WAIT,
                                     cmdline.debug,
                                     filter=f"label:*'{cmdline.token_label}*'"
                                     )
        if token_lookup.status_code == 200 and len(token_lookup.data):
            loop = 1
            for returned_token_id in token_lookup.data:
                if cmdline.add_days:
                    exp = sdk_operation(api.tokens_read,
                                        LONG_WAIT,
                                        cmdline.debug,
                                        ids=returned_token_id
                                        )
                    if exp.status_code == 200 and len(exp.data):
                        new_exp = datetime.strptime(exp.data[0]["expires_timestamp"],
                                                    "%Y-%m-%dT%H:%M:%SZ"
                                                    )
                        updates["expires_timestamp"] = (
                            new_exp + timedelta(days=int(cmdline.add_days))
                            ).strftime("%Y-%m-%dT%H:%M:%SZ")
                if cmdline.new_token_label and len(token_lookup.data) > 1:
                    updates["label"] = f"{cmdline.new_token_label}{loop}"
                if updates:
                    updates["ids"] = returned_token_id
                    sdk_operation(api.tokens_update, LONG_WAIT, cmdline.debug, **updates)
                    loop += 1
        else:
            print(f"NONFATAL 404 ERROR: Not Found ({cmdline.token_label})")


#  ______  _______        _______ _______ _______
#  |     \ |______ |      |______    |    |______
#  |_____/ |______ |_____ |______    |    |______
#  _______  ______  ______ _     _ _______ _______ __   _ _______ _______
#  |_____| |_____/ |  ____ |     | |  |  | |______ | \  |    |    |______
#  |     | |    \_ |_____| |_____| |  |  | |______ |  \_|    |    ______|
#
def handle_delete_arguments(sub: _SubParsersAction, head: str) -> ArgumentParser:
    """Handle delete command arguments."""
    do_delete: ArgumentParser = sub.add_parser("delete",
                                               help="Delete tokens",
                                               aliases=["d"],
                                               description=figlet_format("Delete", font=head),
                                               formatter_class=RawTextHelpFormatter
                                               )
    delete_req = do_delete.add_argument_group("required arguments (mutually exclusive)")
    delete_grp = delete_req.add_mutually_exclusive_group(required=True)
    delete_grp.add_argument("-i", "--token-id", dest="token_id", help="ID of the token to remove.")
    delete_grp.add_argument("-l", "--token-label",
                            dest="token_label",
                            help="Label of the token to remove (starts with match)."
                            )
    do_delete = extra_args(do_delete)
    return do_delete


#  ______  _______        _______ _______ _______
#  |     \ |______ |      |______    |    |______
#  |_____/ |______ |_____ |______    |    |______
#
def delete_token(sdk: InstallationTokens, cmdline: Namespace):
    """Delete a token by ID or name."""
    hold_creds = sdk.auth_object.creds
    this_cid, cids = get_cid_ids(sdk, cmdline)
    cids_to_process = [
        c for c in cids if (cmdline.skip_parent and not c == this_cid) or not cmdline.skip_parent
        ]
    for cid in cids_to_process:
        if cid != this_cid:
            hold_creds["member_cid"] = cid
        api = sdk
        if cmdline.mssp and len(cids) > 1:
            api = InstallationTokens(creds=hold_creds, pythonic=True, debug=cmdline.debug)
        if cmdline.token_id:
            delete_result = sdk_operation(api.tokens_delete,
                                          SHORT_WAIT,
                                          cmdline.debug,
                                          ids=cmdline.token_id
                                          )
            if delete_result.errors:
                for error in delete_result.errors:
                    print(f"NONFATAL {error['code']} ERROR: {error['message']} ({error['id']})")
        if cmdline.token_label:
            token_lookup = sdk_operation(api.tokens_query,
                                         LONG_WAIT,
                                         cmdline.debug,
                                         filter=f"label:*'{cmdline.token_label}*'"
                                         )
            if token_lookup.status_code == 200 and len(token_lookup.data):
                for returned_token_id in token_lookup.data:
                    sdk_operation(api.tokens_delete,
                                  LONG_WAIT,
                                  cmdline.debug,
                                  ids=returned_token_id
                                  )
            else:
                print(f"NONFATAL 404 ERROR: Not Found ({cmdline.token_label})")


#   _____  _______  ______ _______ _______
#  |_____] |_____| |_____/ |______ |______
#  |       |     | |    \_ ______| |______
#  _______  _____  _______ _______ _______ __   _ ______              _____ __   _ _______
#  |       |     | |  |  | |  |  | |_____| | \  | |     \      |        |   | \  | |______
#  |_____  |_____| |  |  | |  |  | |     | |  \_| |_____/      |_____ __|__ |  \_| |______
#  _______  ______  ______ _     _ _______ _______ __   _ _______ _______
#  |_____| |_____/ |  ____ |     | |  |  | |______ | \  |    |    |______
#  |     | |    \_ |_____| |_____| |  |  | |______ |  \_|    |    ______|
#
def consume_arguments() -> Tuple[Namespace, ArgumentParser]:
    """Retrieve any provided command line arguments."""
    subcommands = [
        "create", "c", "list", "l", "delete", "d", "revoke", "x", "restore", "r", "update", "u"
        ]
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    header_font = "big"
    subparsers = parser.add_subparsers(help="Command description",
                                       dest="subcommand",
                                       required=False,
                                       metavar="Token command"
                                       )
    handle_list_arguments(subparsers, header_font)  # List
    handle_create_arguments(subparsers, header_font)  # Create
    handle_revoke_arguments(subparsers, header_font)  # Revoke
    handle_restore_arguments(subparsers, header_font)  # Restore
    handle_update_arguments(subparsers, header_font)  # Update
    handle_delete_arguments(subparsers, header_font)  # Delete
    # Force "list" as the default subcommand without breaking the help processor
    if len(sys.argv) == 1:
        sys.argv.append("list")
    if sys.argv[1].lower() not in subcommands and "-h" not in sys.argv:
        sys.argv.insert(1, "list")
    else:
        if sys.argv[1].lower() not in subcommands:
            sys.argv = [sys.argv[0], "-h"]
    return parser.parse_args(), parser


#   ______ _______ _______ _______             _____ _______ _____ _______
#  |_____/ |_____|    |    |______      |        |   |  |  |   |      |
#  |    \_ |     |    |    |______      |_____ __|__ |  |  | __|__    |
#  _     _ _______ __   _ ______         _______  ______
#  |_____| |_____| | \  | |     \ |      |______ |_____/
#  |     | |     | |  \_| |_____/ |_____ |______ |    \_
#
def rate_delay(wait_time: int):
    """Wait for the specified amount of time while informing the user."""
    for wait in range(wait_time, 0, -1):
        print(f" Rate limit exceeded, sleeping for {wait} seconds. ", end="\r")
        sleep(1)
    print(" " * 80, end="\r")


def sdk_operation(operation: Callable, delay_time: int, debugging: bool, **kwargs) -> Result:
    """Perform an operation against the CrowdStrike API, gracefully handling rate limit errors."""
    rate_limited = True
    while rate_limited:
        try:
            operation_result: Result = operation(**kwargs)
            rate_limited = False
        except APIError as rate_limit_met:
            if rate_limit_met.code == 429:
                rate_delay(delay_time)
            elif debugging:
                raise rate_limit_met
            else:
                failure = FAIL if randbelow(3000) % 2 == 0 else FAIL2
                raise SystemExit(
                    failure.format(rate_limit_met.code, rate_limit_met.message)
                    ) from rate_limit_met
    return operation_result


#  _     _ _______         _____  _______  ______ _______
#  |_____| |______ |      |_____] |______ |_____/ |______
#  |     | |______ |_____ |       |______ |    \_ ______|
#
def reorganize_token_dictionary(tenant: str, record: dict) -> Dict[str, str]:
    """Reorganize a token record dictionary to include the CID column."""
    cid_key = {"cid": tenant}
    cid_list = list(cid_key.items())
    token_keys = list(record.keys())
    token_values = list(record.values())
    token_keys.insert(token_keys.index("id")+1, cid_list[0][0])
    token_values.insert(token_keys.index("id")+1, cid_list[0][1])
    return {
        token_keys[i]: token_values[i]
        for i in range(0, len(token_keys))
    }


def get_all_tokens(api_sdk: InstallationTokens,
                   cmd_args: Namespace,
                   filt: str,
                   cur_cid: str,
                   returning: List[Dict[str, str]]
                   ) -> List[Dict[str, str]]:
    """Retrieve all tokens across all tenants."""
    offset = None
    running = True
    while running:
        token_lookup = sdk_operation(api_sdk.tokens_query,
                                     LONG_WAIT,
                                     cmd_args.debug,
                                     limit=1000,
                                     offset=offset,
                                     filter=f"label:*'*{filt}*'" if filt else None
                                     )
        if not token_lookup.data:
            running = False
        batches = [token_lookup.data[i:i+100] for i in range(0, len(token_lookup.data), 100)]
        for batch in batches:
            token_detail = sdk_operation(api_sdk.tokens_read, LONG_WAIT, cmd_args.debug, ids=batch)
            found = token_detail.data
            if cmd_args.mssp:
                found = []
                for token_det in token_detail.data:
                    new_dict = reorganize_token_dictionary(cur_cid, token_det)
                    found.append(new_dict)
            returning.extend(found)

        offset = len(returning)
        if token_lookup.total <= len(returning):
            running = False
    return returning


def confirm(msg: str):
    """Request confirmation from the user and return a boolean of the response."""
    return input(msg) in ["y", "yes", "Y", "YES"]


def get_this_cid(auth: InstallationTokens, debug_mode: bool = False):
    """Retrieve the CID for the current tenant."""
    my_id = "Not available"
    running = True
    while running:
        try:
            my_id = sdk_operation(
                SensorDownload(auth_object=auth).get_sensor_installer_ccid,
                SHORT_WAIT,
                debug_mode
            ).data[0][:-3].lower()
            running = False
        except APIError as no_sensor_dl:
            if no_sensor_dl.code != 429:
                print("NONFATAL 403 ERROR: This API client is not scoped for Sensor Downloads.")
                running = False
            else:
                rate_delay(SHORT_WAIT)
    return my_id


def check_mssp_scope(auth: InstallationTokens):
    """Confirm if this API client has access to Flight Control."""
    valid = False
    running = True
    while running:
        try:
            valid = bool(FlightControl(auth_object=auth).query_children(limit=1).status_code == 200)
            running = False
        except APIError as rate_limit_met:
            if rate_limit_met.code != 429:
                running = False
                raise rate_limit_met
            rate_delay(SHORT_WAIT)
    return valid


def get_cid_ids(interface: InstallationTokens, arguments: Namespace) -> Tuple[str, List[str]]:
    """Return all CIDs associated with the API client (if MSSP mode is enabled)."""
    this_cid = "NonMSSP"
    cid_list = [this_cid]
    if arguments.mssp:
        this_cid = get_this_cid(interface, arguments.debug)
        cid_list = [this_cid]
        try:
            mssp = FlightControl(auth_object=interface)
            cid_list.extend(mssp.query_children().data)
        except APIError:
            pass
    return this_cid, cid_list


def write_output_results(cmdline_args: Namespace, tresults: list):
    """Write the displayed token results to the requested file."""
    if cmdline_args.output_file:
        if cmdline_args.output_format.lower() == "csv":
            with open(cmdline_args.output_file, "w", newline="", encoding="utf-8") as csv_file:
                csv_writer = writer(csv_file)
                if tresults:
                    csv_writer.writerow(tresults[0].keys())
                    for token_row in tresults:
                        csv_writer.writerow(token_row.values())
                    print(f"CSV results output to {cmdline_args.output_file}.")
        elif cmdline_args.output_format.lower() == "json":
            with open(cmdline_args.output_file, "w", encoding="utf-8") as json_file:
                dump(tresults, json_file, indent=4)
            print(f"JSON results output to {cmdline_args.output_file}.")


def display_tokens(token_results: list, cmd_args: Namespace, parent_tokens: list):
    """Display the retrieved tokens in a tabular format."""
    new_token_results = token_results
    if cmd_args.mssp:
        new_token_results = []
        for tok in token_results:
            matched = False
            for ptok in parent_tokens:
                if ptok["cid"] == tok["cid"]:
                    if tok["id"] == ptok["id"] and tok["value"] == ptok["value"]:
                        matched = True
                elif ptok["cid"] != tok["cid"]:
                    matched = True
            if matched:
                new_token_results.append(tok)

    token_results = sorted(new_token_results,
                           key=lambda x: x[cmd_args.order_by],
                           reverse=cmd_args.reverse
                           )
    vers = ""
    if cmd_args.show_version:
        vers = f" (FalconPy v{version(agent_string=False)})"
    if token_results:
        tabular_display = tabulate(tabular_data=[t.values() for t in token_results],
                                   headers=token_results[0].keys(),
                                   tablefmt=cmd_args.table_format
                                   )
        print(tabular_display)
        print(f"{len(token_results)} total tokens found{vers}")
        write_output_results(cmd_args, token_results)
    else:
        print(NOT_FOUND.format(vers.replace("(", "").replace(")", "")))


def cross_tenant_action(action: Callable, msg: str, **kwargs):
    """Check and warn if this action impacts multiple CIDs."""
    proceed = True
    if not kwargs.get("cmdline").force:
        if kwargs.get("cmdline").mssp and check_mssp_scope(kwargs.get("sdk")):
            parent_to = "the parent and "
            if kwargs.get("cmdline").skip_parent:
                parent_to = ""
            proceed = confirm(WARNING.format(msg, parent_to))
    if proceed:
        action(**kwargs)
    else:
        print("Operation cancelled.")
        sys.exit(0)


#  _______  _____  __   _ _______ _______ _______ __   _ _______ _______
#  |       |     | | \  | |______    |    |_____| | \  |    |    |______
#  |_____  |_____| |  \_| ______|    |    |     | |  \_|    |    ______|
#
LONG_WAIT = 10
SHORT_WAIT = 5
FAIL = r"""
     ,     ,
    (\____/)   FATAL {} {}
     (_oo_)  /
       (O)
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\
(\   /____\
"""
FAIL2 = r"""
       _
      [ ]     FATAL {} {}
     (   )  /
      |>|
   __/===\__
  //| o=o |\\
<]  | o=o |  [>
    \=====/
   / / | \ \
  <_________>
"""
NOT_FOUND = r"""
         __  No tokens found!
 _(\    |@@|  /
(__/\__ \--/ __
   \___|----|  |   __
       \ CS /\ )_ / _\
       /\__/\ \__O (__
      (--/\--)    \__/
      _)(  )(_
     `---''---` {}
"""
WARNING = r"""
   __,_,
  [_|_/   ⚠️  Warning ⚠️
   //     This action will {} multiple tokens
 _//    __  /   across {}child tenants.
(_|)   |@@|
 \ \__ \--/ __
  \o__|----|  |   __
      \ CS /\ )_ / _\
      /\__/\ \__O (__
     (--/\--)    \__/
     _)(  )(_
    `---''---`

Are you sure you wish to proceed? (y/n) => """
#  _______ _______ _____ __   _       ______  _____  _     _ _______ _____ __   _ _______
#  |  |  | |_____|   |   | \  |      |_____/ |     | |     |    |      |   | \  | |______
#  |  |  | |     | __|__ |  \_|      |    \_ |_____| |_____|    |    __|__ |  \_| |______
#
if __name__ == "__main__":
    begin = datetime.now().timestamp()  # Start the timer
    if sys.version_info <= (3, 7):  # Make sure we're running the minimum version of Python
        raise SystemExit("This application only supports Python 3.7 or greater.")
    if not version(compare="1.3.4"):  # Check for 1.3.4 or greater
        raise SystemExit("In order to use this sample application, the CrowdStrike FalconPy "
                         "library (version 1.3.4 or greater) must be installed."
                         )
    parsed, handler = consume_arguments()  # Retrieve command line arguments and the parser
    # There are no credentials in the environment or command line, show help and quit
    if not parsed.client_id or not parsed.client_secret:
        handler.print_help()
        raise SystemExit(
                "\nYou must provide API credentials via the environment variables\n"
                "FALCON_CLIENT_ID and FALCON_CLIENT_SECRET or you must provide\n"
                "these values using the '-k' and '-s' command line arguments."
                )
    if parsed.debug:  # Enable debug logging to the console if requested
        basicConfig(level=DEBUG)
    # Construct an instance of the InstallationTokens Service Class
    tokens = InstallationTokens(client_id=parsed.client_id,
                                client_secret=parsed.client_secret,
                                debug=parsed.debug,
                                pythonic=True,
                                member_cid=parsed.child
                                )
    default_action_args = [tokens, parsed]  # We display all tokens regardless of command executed
    tcommand = parsed.subcommand.lower()  # Selected token command
    if tcommand in ["create", "c"]:  # Create
        cross_tenant_action(create_token, "create", sdk=tokens, cmdline=parsed)
    elif tcommand in ["delete", "d"]:  # Delete
        if parsed.token_label:
            cross_tenant_action(delete_token, "delete", sdk=tokens, cmdline=parsed)
        else:
            delete_token(tokens, parsed)
    elif tcommand in ["revoke", "x", "restore", "r"]:  # Revoke and Restore
        if parsed.token_label:
            cross_tenant_action(token_revocation,
                                "restore" if tcommand in ["restore", "r"] else "revoke",
                                sdk=tokens,
                                cmdline=parsed,
                                revoking=tcommand in ["revoke", "x"]
                                )
        else:
            token_revocation(tokens, parsed, tcommand in ["revoke", "x"])
    elif tcommand in ["update", "u"]:  # Update
        if parsed.token_id:
            update_token_by_id(tokens, parsed)
        elif parsed.token_label:
            cross_tenant_action(update_token_by_label, "update", sdk=tokens, cmdline=parsed)
    if parsed.filter:  # List / all commands
        # Add any provided command line filters to the arguments for the default action
        default_action_args.append(parsed.filter)
    show_all_tokens(*default_action_args)  # After all processing, display the list of tokens


#    █                                                                                           █
#     █                                                                                        ██
#      ██                 _  _  _ _______      _______ _______  _____   _____                 ▓█
#      ▒▒███              |  |  | |______      |______    |    |     | |_____]             ██▓▒▓
#     ▒░▒▓████            |__|__| |______      ______|    |    |_____| |                █████▒▒▒▓
#    █▒▒▓████▒▓███                                                                   ▓██▓▓████▒░▒
#    ▒░▒████▒░░▒▒▓▓█▓▓                                                           ████▒▒▒░░▓███▓▒░▒
#   ▓░▒▒███▓░░▒▒▒▓██▓▒█▓█▓▓                                                 ▒▓█▓▓▒███▒▒▒▒░▒████▒░▒
#   ▒░▒▓███▓░░▒▒▒███▒░░░▓███▓█▓                                        █▓█▓███▒░░░▓██▓▒▒▒░▒████▒░▒
#   ▒░▒▓███▓░░▒▒▒███▒░░░▓███░░▒▓▓█▓                                 ▓██▒▒░▒███▒░░░▓██▓▒▒▒░▒████▒░▒
#   ▓░▒▒███▓░░▒▒▒▒██▓░░░░░░░░▒▒▒█████▓                           ▓█████░▒░░░░░░░░░███▒▒▒▒░▒████▒░▒
#    ▒░▒████▒░░▒▒▒▓███▒░▒▒▒▒░░████▒▒▒▓██                       █▓▓▒▒▓███▒░▒▒▒▒░░▓███▒▒▒▒░░▓███▓▒░▒
#    █▒▒▒████▒░▒▒▒▒▒████████████▓▒▒▒▒▒▒███                   █▓▒░▒▒▒▒▒████████████▓▒▒▒▒░░▓████▒▒▒
#     ▒░▒▓████▒░░▒▒▒▒▒▓███████▒▒▒▒▒▒░░▓███                  ████▒░▒▒▒▒▒▒▓███████▒▒▒▒▒▒░░▓████▒▒░▒
#      ▒░▒▓████▓▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒█▓███▓█               █▓████▓▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒█▓███▒▒▒▓
#       ▒░▒▒██████▒░░░▒▒▒▒▒▒▒▒▒░░▒▒█▓███▓▒▒▓█             █▒▒▒██████▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒█▓███▓▒▒▒▒
#        ▓▒▒▒▒███████▒▒▒▒▒▒▒▒▒▒▓███████▒▒▒▒                 ▒▒▒▒███████▒▒▒▒▒░▒▒▒▒▓███████▒▒░▒
#          ▒▒▒▒▒▓█████████▓█████████▒▒▒▒▒                    ▓▒▒▒▒▓█████████▓█████████▒▒▒░▒
#            ▓▒▒▒▒▒▒████████████▓▒▒▒▒▒▓                        █▒▒▒▒▒▒████████████▓▒▒▒▒░▒
#               ▓▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                              █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓
#                     ▓▒▓▓▓▓▒▓█                                         █▒░▓▓▓▒▓█
#
#                   ______   ______ _______ _______ _______ _     _ _______ _______
#                   |_____] |_____/ |______ |_____| |       |_____| |______ |______
#                   |_____] |    \_ |______ |     | |_____  |     | |______ ______|
