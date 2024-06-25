r"""CrowdStrike Falcon Discover real-time audit report utility.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |      FalconPy v1.2.11
`-------'                         `-------'

  ⢀⣀⣀           _______                     __
⢀⣾⡿⠛⠉          |     __|.-----.--.--.-----.|  |.---.-.-----.-----.
⢸⡟ ⣾⣿⣷⣤⡀       |__     ||  _  |  |  |  _  ||  ||  _  |__ --|__ --|
   ⠙⣿⣿⠟⢁⣤⡤     |_______||   __|___  |___  ||__||___._|_____|_____|
    ⠈⠁⣴⡿⢋⣤⣶⣶⣄⡀          |__|  |_____|_____|
      ⠋⢠⣿⣿⣿⣿⣿⣿⡦
       ⠘⢿⣿⣿⣿⠟⢁⣤⣶⠿⠛
        ⠈⠻⡿⠁⣴⡿⠋⣀⣴⣾⣿⣿⣷⣤⡀
           ⣼⡟⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠦        Requirements
           ⠛ ⣾⣿⣿⣿⣿⣿⡿⠟⣉⣤⣶⣶⣶⣶⡄       crowdstrike-falconpy (v1.2.11+)
             ⢿⣿⣿⣿⣿⠏⣠⣾⡿⠛⢉⣠⣤⣄⠈       pyfiglet
              ⠹⣿⣿⠃⣼⣿⠏ ⠔⣫⣿⣿⣿⡇       termcolor
               ⠈⠃⢰⣿⠃  ⢰⣿⣿⣿⡿
                 ⠸⣿   ⠈⣩⠿⠋
                  ⠉⠑ ⠈⠉

Created: 03.06.2023 - jshcodes@CrowdStrike
"""
# pylint: disable=R0902,R0904,R0912,R0914,R0915
import os
import json
import logging
from datetime import datetime
from argparse import ArgumentParser, RawTextHelpFormatter
from concurrent.futures import ThreadPoolExecutor
from signal import signal, SIGINT, SIGTERM, SIGQUIT
try:
    from termcolor import colored
except ImportError as no_termcolor:
    raise SystemExit("The termcolor library must be installed.\n"
                     "Install with: python3 -m pip install termcolor"
                     ) from no_termcolor
try:
    from pyfiglet import figlet_format
except ImportError as no_figlet:
    raise SystemExit("The pyfiglet library must be installed.\n"
                     "Install with: python3 -m pip install pyfiglet"
                     ) from no_figlet
try:
    from falconpy import Discover, Hosts
except ImportError as no_falconpy:
    raise SystemExit("The crowdstrike-falconpy library (v1.2.11+) "
                     "must be installed to use this application.\n"
                     "Install with: python3 -m pip install crowdstrike-falconpy"
                     ) from no_falconpy


# ____ ___  ___  _    _ ____ ____ ___ _ ____ _  _    ____ ____ _  _ ____ _ ____
# |__| |__] |__] |    | |    |__|  |  | |  | |\ |    |    |  | |\ | |___ | | __
# |  | |    |    |___ | |___ |  |  |  | |__| | \|    |___ |__| | \| |    | |__]
#
# All application configuration, process status and performance monitoring is
# handled using this class. Consumes command line arguments and sets defaults
# during instantiation. Implements graceful shutdown handling in the case of
# a quit or interrupt signal being received.
#
class Application:
    """Class to store configuration and performance detail."""

    _debug = False

    _timing = {
        "start_time": datetime.now().timestamp(),
        "end_time": 0,
        "api_calls": 0
    }
    _configuration = {
        "show_updates": True,
        "sdk": None,
        "hosts": None,
        "categories": [],
        "save_results": False,
        "data_batch_size": 100,
        "extra": {
            "logins_sort": "login_timestamp.desc",
            "accounts_sort": "username.asc",
            "hosts_sort": "last_seen_timestamp.desc",
            "applications_sort": "hostname.asc"
        }
    }
    _status = {"running": True, "cancelled": False}

    def __init__(self):
        """Construct an instance of the application."""
        self.configure_application()
        if not self.show_updates:
            print("Depending on the size of your environment, "
                  "this process may take several minutes.\nPlease wait..."
                  )

    def hard_finish(self, _sig, _frame):
        """Perform a hard finish when an interrupt signal is received."""
        self.cancelled = True
        self.finish()

    def finish(self):
        """Perform end of routine procedures like setting the end time."""
        self.end_time = datetime.now().timestamp()
        self.running = False

    def graceful_finish(self):
        """Gracefully end the routine."""
        if self.running:
            self.finish()
        print(f"Routine {self.quit_status} execution of {self.api_calls:,} "
              f"API calls in {self.run_time:,.2f} seconds on {self.formatted_end_time}."
              )

    def configure_application(self):
        """Consume any provided command line arguments and configure the application."""
        signal(SIGINT, self.hard_finish)
        signal(SIGQUIT, self.hard_finish)
        signal(SIGTERM, self.hard_finish)
        category_list = ["accounts", "applications", "hosts", "logins"]
        parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
        reqgrp = parser.add_argument_group("required arguments")
        reqgrp.add_argument("-k", "--falcon_client_id",
                            help="Falcon API Client ID",
                            required=True
                            )
        reqgrp.add_argument("-s", "--falcon_client_secret",
                            help="Falcon API Client Secret",
                            required=True
                            )
        parser.add_argument("-r", "--region",
                            help="CrowdStrike region.\nChoose from:\n"
                            "   ▪ us1\n   ▪ us2\n   ▪ eu1\n   ▪ usgov1\n   ▪ auto\n"
                            "Only required for GovCloud users.",
                            default="auto",
                            required=False
                            )
        parser.add_argument("-c", "--categories",
                            help="Discover categories to review.\nChoose from:\n"
                            "   ▪ accounts\n   ▪ applications\n   ▪ hosts\n   ▪ logins\n   ▪ all\n"
                            "Comma delimited strings are accepted.",
                            default="all",
                            required=False
                            )
        parser.add_argument("-d", "--disable_dynamic_updates",
                            help="Show dynamic update messages as API calls are performed.",
                            action="store_true",
                            required=False,
                            default=False
                            )
        parser.add_argument("-j", "--json",
                            help="Output results to JSON save files.",
                            action="store_true",
                            default=False,
                            required=False
                            )
        parser.add_argument("--accounts_filter",
                            help="Filter accounts results using FQL syntax.\n"
                            "Example: --accounts_filter \"account_name:*'*PRODUCTION*'\"\n"
                            f"{bold('Filter must be enclosed in double quotes')}",
                            default=None,
                            required=False
                            )
        parser.add_argument("--accounts_sort",
                            help="Sort accounts results using FQL syntax.\n"
                            "You may sort asc or desc by first_seen_timestamp or username.\n"
                            "Examples: --accounts_sort first_seen_timestamp.desc\n"
                            "          --accounts_sort username.asc",
                            default=None,
                            required=False
                            )
        parser.add_argument("--applications_filter",
                            help="Filter applications results using FQL syntax.\n"
                            "Example: --applications_filter \"is_suspicious:true\"\n"
                            f"{bold('Filter must be enclosed in double quotes')}",
                            default=None,
                            required=False
                            )
        parser.add_argument("--applications_sort",
                            help="Sort applications results using FQL syntax.\n"
                            "You may sort asc or desc by hostname or name (application).\n"
                            "Examples: --applications_sort hostname.asc\n"
                            "          --applications_sort name.desc",
                            default=None,
                            required=False
                            )
        parser.add_argument("--hosts_filter",
                            help="Filter hosts results using FQL syntax.\n"
                            "Example: --applications_filter \"hostname:*'*search_string*'\"\n"
                            f"{bold('Filter must be enclosed in double quotes')}",
                            default=None,
                            required=False
                            )
        parser.add_argument("--hosts_sort",
                            help="Sort hosts results using FQL syntax.\n"
                            "You may sort asc or desc by hostname or last_seen_timestamp.\n"
                            "Examples: --hosts_sort hostname.asc\n"
                            "          --hosts_sort last_seen_timestamp.desc",
                            default=None,
                            required=False
                            )
        parser.add_argument("--logins_filter",
                            help="Filter logins results using FQL syntax.\n"
                            "Example: --logins_filter \"username:*'*larry*'\"\n"
                            f"{bold('Filter must be enclosed in double quotes')}",
                            default=None,
                            required=False
                            )
        parser.add_argument("--logins_sort",
                            help="Sort logins results using FQL syntax.\n"
                            "You may sort asc or desc by login_timestamp or username.\n"
                            "Examples: --logins_sort login_timestamp.desc\n"
                            "          --logins_sort username.asc",
                            default=None,
                            required=False
                            )
        parser.add_argument("--debug",
                            help="Enable API debugging",
                            action="store_true",
                            default=False
                            )
        parsed = parser.parse_args()
        cats = parsed.categories.split(",")
        if "all" in cats:
            self.categories = category_list
        else:
            self.categories = [c for c in cats if c in category_list]
        if not self.categories:
            raise SystemExit("No valid categories specified (Choose one or multiple "
                             "from accounts, applications, hosts, logins or all). [Comma delimit]"
                             )
        print(f"Retrieving requested Falcon Discover audit results on {self.formatted_start_time}.")
        self.show_updates = not bool(parsed.disable_dynamic_updates)
        self.save_results = parsed.json
        if parsed.accounts_filter:
            self.accounts_filter = parsed.accounts_filter
        if parsed.accounts_sort:
            self.accounts_sort = parsed.accounts_sort
        if parsed.hosts_filter:
            self.hosts_filter = parsed.hosts_filter
        if parsed.hosts_sort:
            self.hosts_sort = parsed.hosts_sort
        if parsed.logins_filter:
            self.logins_filter = parsed.logins_filter
        if parsed.logins_sort:
            self.logins_sort = parsed.logins_sort
        if parsed.applications_filter:
            self.applications_filter = parsed.applications_filter
        if parsed.applications_sort:
            self.applications_sort = parsed.applications_sort
        if parsed.debug:
            self.debug = True
            self.show_updates = False
            logging.basicConfig(level=logging.DEBUG)

        # Everything before this moment happens within milliseconds
        self.sdk = Discover(client_id=parsed.falcon_client_id,
                            client_secret=parsed.falcon_client_secret,
                            base_url=parsed.region,
                            debug=self.debug
                            )
        self.hosts = Hosts(auth_object=self.sdk)

    # Immutable
    @property
    def run_time(self) -> int:
        """Retrieve the calculated (read only) run time property."""
        return self.end_time - self.start_time

    @property
    def start_time(self) -> int:
        """Retrieve the start time property."""
        return self._timing["start_time"]

    @property
    def data_batch_size(self) -> int:
        """Return the data batch size constant."""
        return self._configuration["data_batch_size"]

    @property
    def formatted_start_time(self) -> str:
        """Return the end time property as a cleanly formatted date string."""
        return datetime.fromtimestamp(self.start_time).strftime("%m-%d-%Y %H:%M:%S")

    @property
    def formatted_end_time(self) -> str:
        """Return the end time property as a cleanly formatted date string."""
        return datetime.fromtimestamp(self.end_time).strftime("%m-%d-%Y %H:%M:%S")

    @property
    def quit_status(self) -> str:
        """Return the quit status string."""
        return "completed" if not self.cancelled else "was cancelled before finishing. Completed"

    @property
    def extra(self) -> dict:
        """Retrieve the extra configuration options dictionary."""
        return self._configuration["extra"]

    # Mutable
    @property
    def debug(self) -> bool:
        """Retrieve the end time property."""
        return self._debug

    @debug.setter
    def debug(self, val: bool):
        """Set the end time property."""
        self._debug = val

    @property
    def end_time(self) -> int:
        """Retrieve the end time property."""
        return self._timing["end_time"]

    @end_time.setter
    def end_time(self, val: int):
        """Set the end time property."""
        self._timing["end_time"] = val

    @property
    def api_calls(self) -> int:
        """Return the current API call count."""
        return self._timing["api_calls"]

    @api_calls.setter
    def api_calls(self, val: int):
        """Set the API call count."""
        self._timing["api_calls"] = val

    @property
    def show_updates(self) -> bool:
        """Return the show dynamic updates property."""
        return self._configuration["show_updates"]

    @show_updates.setter
    def show_updates(self, val: bool):
        """Set the show dynamic updates property."""
        self._configuration["show_updates"] = val

    @property
    def save_results(self) -> bool:
        """Return the save results to file property."""
        return self._configuration["save_results"]

    @save_results.setter
    def save_results(self, val: bool):
        """Set the save results to file property."""
        self._configuration["save_results"] = val

    @property
    def sdk(self) -> Discover:
        """Return the Discover SDK property."""
        return self._configuration["sdk"]

    @sdk.setter
    def sdk(self, val: Discover):
        """Set the Discover SDK property."""
        self._configuration["sdk"] = val

    @property
    def categories(self) -> list:
        """Return the categories to review property."""
        return self._configuration["categories"]

    @categories.setter
    def categories(self, val: list):
        """Set the categories to review property."""
        self._configuration["categories"] = val

    @property
    def running(self) -> bool:
        """Retrieve the running status property."""
        return self._status["running"]

    @running.setter
    def running(self, val: bool):
        """Set the running status property."""
        self._status["running"] = val

    @property
    def cancelled(self) -> bool:
        """Retrieve the cancelled status property."""
        return self._status["cancelled"]

    @cancelled.setter
    def cancelled(self, val: bool):
        """Set the cancelled status property."""
        self._status["cancelled"] = val

    @property
    def accounts_filter(self) -> str:
        """Retrieve the current accounts filter property."""
        return self.extra.get("accounts_filter", None)

    @accounts_filter.setter
    def accounts_filter(self, val: str):
        """Set the accounts filter property."""
        self.extra["accounts_filter"] = val

    @property
    def accounts_sort(self) -> str:
        """Retrieve the current accounts sort property."""
        return self.extra.get("accounts_sort", None)

    @accounts_sort.setter
    def accounts_sort(self, val: str):
        """Set the accounts sort property."""
        self.extra["accounts_sort"] = val

    @property
    def hosts_filter(self) -> str:
        """Retrieve the current hosts filter property."""
        return self.extra.get("hosts_filter", None)

    @hosts_filter.setter
    def hosts_filter(self, val: str):
        """Set the hosts filter property."""
        self.extra["hosts_filter"] = val

    @property
    def hosts_sort(self) -> str:
        """Retrieve the current hosts sort property."""
        return self.extra.get("hosts_sort", None)

    @hosts_sort.setter
    def hosts_sort(self, val: str):
        """Set the hosts sort property."""
        self.extra["hosts_sort"] = val

    @property
    def logins_filter(self) -> str:
        """Retrieve the current logins filter property."""
        return self.extra.get("logins_filter", None)

    @logins_filter.setter
    def logins_filter(self, val: str):
        """Set the logins filter property."""
        self.extra["logins_filter"] = val

    @property
    def logins_sort(self) -> str:
        """Retrieve the current logins sort property."""
        return self.extra.get("logins_sort", None)

    @logins_sort.setter
    def logins_sort(self, val: str):
        """Set the logins sort property."""
        self.extra["logins_sort"] = val

    @property
    def applications_filter(self) -> str:
        """Retrieve the current applications filter property."""
        return self.extra.get("applications_filter", None)

    @applications_filter.setter
    def applications_filter(self, val: str):
        """Set the applications filter property."""
        self.extra["applications_filter"] = val

    @property
    def applications_sort(self) -> str:
        """Retrieve the current applications sort property."""
        return self.extra.get("applications_sort", None)

    @applications_sort.setter
    def applications_sort(self, val: str):
        """Set the applications sort property."""
        self.extra["applications_sort"] = val


# ____ ___  _    _ _  _ ___ ____ ____ ____ ____ ____ ____
# |__| |__] |    | |\ |  |  |___ |__/ |___ |__| |    |___
# |  | |    |    | | \|  |  |___ |  \ |    |  | |___ |___
#
# Leverages the normalized naming convention for Discover operations to abstract API interaction.
#
def batch_get_details(sdk, cat):
    """Retrieve all details for all discovered elements."""
    cmd = getattr(sdk, f"get_{cat}")
    func = getattr(sdk, f"query_{cat}")

    def get_detail(ids):
        """Retrieve detail information for the ID list provided."""
        returned = False
        if APP.running:  # pylint: disable=E0606
            APP.api_calls += 1
            returned = cmd(ids=ids)["body"]["resources"]
        return returned

    running = True
    returned = []
    details = []
    offset = None
    running_total = 0
    filter_string = APP.extra.get(f"{cat}_filter")
    while running:
        APP.api_calls += 1
        result = func(limit=APP.data_batch_size, offset=offset, filter=filter_string)
        if result["status_code"] != 200:
            print(f"{colored('Errors occurred retrieving data', attrs=['bold', 'underline'])}")
            for err in result["body"]["errors"]:
                print(f"[{bold(err['code'])}] "
                      f"{colored(err['message'], color='red', attrs=['bold'])}"
                      )
            print("")
        if result["body"]["resources"]:
            offset = result["body"]["meta"]["pagination"]["offset"]
            total = result["body"]["meta"]["pagination"]["total"]
            returned = result["body"]["resources"]
            running_total += len(returned)
            details.extend(get_detail(returned))
            if APP.show_updates:
                print(f"  Details for {len(details)} {cat} retrieved.",
                      end=f"{' '*40}\r",
                      flush=True
                      )
            if running_total >= total or not APP.running:
                running = False
        else:
            running = False
    return details


# _  _ ____ _    ___  ____ ____ ____
# |__| |___ |    |__] |___ |__/ [__
# |  | |___ |___ |    |___ |  \ ___]
#
# Helper methods to handle file dumps and terminal output formatting.
#
def do_file_dump(dump_type, dump_data):
    """Dump a result to a JSON file."""
    dump_file = f"{dump_type}_{int(APP.start_time)}.json"
    if os.path.exists(dump_file):
        os.remove(dump_file)
    with open(dump_file, "w", encoding="utf-8") as json_output:
        json.dump(dump_data, json_output, indent=4)


def bold(inbound, underscore: bool = False):
    """Format a terminal string for bold and optionally underline."""
    attrs = ['bold']
    if underscore:
        attrs.append('underline')
    return colored(inbound, attrs=attrs)


def header_column(inbound):
    """Create a fixed width header column."""
    return f"{inbound:21s}: "


def row_break(inc: int = 22):
    """Print a row break."""
    print(f"{'-'*inc}")


def category_header(header_string):
    """Leverage Figlet to show a category header."""
    if APP.show_updates:
        print(" " * 80, end="\r", flush=True)
    figure = figlet_format(header_string, font="cybermedium")
    return colored(figure, color="magenta", attrs=["bold"])


# ____ ____ ____ ___ _ _  _ ____
# [__  |  | |__/  |  | |\ | | __
# ___] |__| |  \  |  | | \| |__]
#
# Helper methods leveraged to sort result lists returned from the API.
#
def logins_sort(login_event, sort_key):
    """Sort the logins list by the specified key."""
    returned = login_event[sort_key]
    if "login_timestamp" in sort_key:
        returned = datetime.strptime(login_event[sort_key], "%Y-%m-%dT%H:%M:%SZ")
    return returned


def applications_sort(application_event, sort_key):
    """Sort the applications list by the specified key."""
    return application_event[sort_key]


def hosts_sort(hosts_event, sort_key):
    """Sort the hosts list by the specified key."""
    returned = hosts_event.get(sort_key, "Unknown").lower()
    if "last_seen_timestamp" in sort_key:
        returned = datetime.strptime(hosts_event[sort_key], "%Y-%m-%dT%H:%M:%SZ")
    return returned


def accounts_sort(accounts_event, sort_key):
    """Sort the accounts list by the specified key."""
    returned = accounts_event.get(sort_key, "Unknown").lower()
    if "last_seen_timestamp" in sort_key:
        returned = datetime.strptime(accounts_event[sort_key], "%Y-%m-%dT%H:%M:%SZ")
    return returned


# ___ ____ ____ _  _ _ _  _ ____ _       ____ _  _ ___ ___  _  _ ___
#  |  |___ |__/ |\/| | |\ | |__| |       |  | |  |  |  |__] |  |  |
#  |  |___ |  \ |  | | | \| |  | |___    |__| |__|  |  |    |__|  |
#
# Methods used to output results to the terminal.
#
def display_accounts(account_list: list):
    """Display the account results."""
    print(category_header("Accounts"), end="\r")
    row_break(38)
    if not account_list:
        print(colored("No accounts found", color="red", attrs=["bold"]))
    sorting = APP.accounts_sort.split(".")
    sort_type = sorting[0]
    sort_order = sorting[1]
    account_list = sorted(account_list,
                          key=lambda x: accounts_sort(x, sort_type),
                          reverse=bool(sort_order == "desc")
                          )
    for account in account_list:
        first_seen = ""
        last_success = ""
        last_fail = ""
        last_reset = ""
        account_name = bold(account.get("account_name", "Unknown"))
        username = bold(account.get("username", "Unknown"))
        domain = account.get("login_domain", "Unknown")
        if account.get("first_seen_timestamp", None):
            first_seen = datetime.strptime(account["first_seen_timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            first_seen = bold(first_seen.strftime("%m-%d-%Y %H:%M:%S"))
        if account.get("last_successful_login_timestamp", None):
            last_success = datetime.strptime(account["last_successful_login_timestamp"],
                                             "%Y-%m-%dT%H:%M:%SZ"
                                             )
            last_success = bold(last_success.strftime("%m-%d-%Y %H:%M:%S"))
        success_type = account.get("last_successful_login_type", None)
        success_type = " ("+bold(success_type)+")" if success_type else ""
        country = account.get("last_successful_login_host_country", None)
        city = account.get("last_successful_login_host_city", None)
        ipaddr = account.get("last_successful_login_remote_ip", None)
        sid = account.get("user_sid", None)
        if account.get("last_failed_login_timestamp"):
            last_fail = datetime.strptime(account["last_failed_login_timestamp"],
                                          "%Y-%m-%dT%H:%M:%SZ"
                                          )
            last_fail = bold(last_fail.strftime("%m-%d-%Y %H:%M:%S"))
        fail_type = account.get("last_failed_login_type", None)
        fail_type = " ("+bold(fail_type)+")" if fail_type else ""
        if account.get("password_last_set_timestamp", None):
            last_reset = datetime.strptime(
                account.get("password_last_set_timestamp", None),
                "%Y-%m-%dT%H:%M:%SZ"
                )
            last_reset = bold(last_reset.strftime("%m-%d-%Y %H:%M:%S") if last_reset else "Never")
        admin_priv = account.get("admin_privileges", None)
        acct_type = account.get("account_type", "Unspecified")
        username_extra = f"(A{'n' if acct_type[0] != 'L' else ''}"
        username_extra = f"{username_extra} {bold(acct_type)} account"
        with_str = "with"
        if admin_priv == "No":
            with_str = "without"
        elif admin_priv == "Unknown":
            with_str = "with unknown"
        with_extra = bold(with_str, underscore=True)
        username_extra = f"{username_extra} {with_extra} admin privileges)"
        extra = ""
        if country or city or ipaddr:
            res = []
            if city:
                res.append(city)
            if country:
                res.append(country)
            if ipaddr:
                res.append(ipaddr)
            extra = f"({', '.join(res)})"

        print(f"{header_column('Account')}{account_name}")
        print(f"{header_column('Username')}{username} {username_extra}")
        print(f"{header_column('Domain')}{bold(domain)}")
        if sid:
            print(f"{header_column('SID')}{bold(sid)}")
        if first_seen:
            print(f"{header_column('First seen')}{first_seen}")
        if last_success:
            print(f"{header_column('Last login success')}{last_success}{success_type} {extra}")
        if last_fail:
            print(f"{header_column('Last login failure')}{last_fail}{fail_type}")
        if last_reset:
            print(f"{header_column('Last password reset')}{last_reset}")
        row_break()


def display_hosts(hosts_list: list):  # noqa
    """Display the hosts results."""
    print(category_header("Hosts"), end="\r")
    row_break(23)
    if not hosts_list:
        print(colored("No hosts found", color="red", attrs=["bold"]))
    else:
        disco_aids = list({
            h["first_discoverer_aid"] for h in hosts_list if h.get("first_discoverer_aid", None)
        })
        discoverers = APP.hosts.get_device_details(disco_aids)["body"]["resources"]
        if discoverers:
            discoverers = {
                dis["device_id"]: dis.get("hostname", "Unidentified host") for dis in discoverers
            }
        else:
            discoverers = {}
    sorting = APP.hosts_sort.split(".")
    sort_type = sorting[0]
    sort_order = sorting[1]
    hosts_list = sorted(hosts_list,
                        key=lambda x: hosts_sort(x, sort_type),
                        reverse=bool(sort_order == "desc")
                        )
    for host in hosts_list:
        first_seen = ''
        last_seen = ''
        managed = ''
        if host.get("first_seen_timestamp", None):
            first_seen = datetime.strptime(host["first_seen_timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            first_seen = bold(first_seen.strftime("%m-%d-%Y %H:%M:%S"))
        if host.get("last_seen_timestamp", None):
            last_seen = datetime.strptime(host["last_seen_timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            last_seen = bold(last_seen.strftime("%m-%d-%Y %H:%M:%S"))
        if host["entity_type"] == "unmanaged":
            managed = "(No sensor installed)"
        elif host["entity_type"] == "managed":
            mextra = ""
            if host.get("aid"):
                mextra = f": {bold(host.get('aid'))}, "
                mextra = f"{mextra}{host.get('agent_version', 'unspecified version')}"
            managed = f"(Sensor installed{mextra})"
        elif host["entity_type"] == "unsupported":
            managed = "(Device not supported)"
        display_name = host.get("hostname")
        current_local = host.get("current_local_ip", "Unknown")
        current_external = host.get("external_ip", "Unknown")
        if not display_name:
            display_name = max(current_local, current_external)
        plat = host.get("os_version")
        if plat:
            display_name = f"{display_name} ({plat})"
        discovered_by = "Discovering device"
        discovered_plat = ""
        if host.get("first_discoverer_aid", None):
            discovered_by = discoverers.get(host["first_discoverer_aid"], "Unknown discoverer")
        if host.get("discoverer_platform_name"):
            discovered_plat = host["discoverer_platform_name"]
            discovered_by = f"{discovered_by} ({discovered_plat})"
        interfaces = host.get("network_interfaces", [])
        print(f"{header_column('Host')}{bold(display_name)} {managed}")
        if first_seen:
            print(f"{header_column('First seen')}{first_seen}")
        if last_seen:
            print(f"{header_column('Last seen')}{last_seen}")
        if discovered_by == "Discovering device":
            print(f"{header_column(discovered_by)}{bold('Yes')}")
        else:
            print(f"{header_column('Discovered by device')}{bold(discovered_by)}")
        if current_local != "Unknown":
            print(f"{header_column('Current IP address')}{bold(current_local)}")
        if interfaces:
            for interface in interfaces:
                print(f"{header_column('Network interface')}{bold(interface['local_ip'])} "
                      f"({bold(interface['mac_address'])})"
                      )
        if current_external != "Unknown":
            print(f"{header_column('External IP address')}{bold(current_external)}")
        row_break()


def display_logins(logins_list: list):
    """Display the logins results."""
    print(category_header("Logins"), end="\r")
    row_break(26)
    if not logins_list:
        print(colored("No logins found", color="red", attrs=["bold"]))
    else:
        sorting = APP.logins_sort.split(".")
        sort_type = sorting[0]
        sort_order = sorting[1]
        logins_list = sorted(logins_list,
                             key=lambda x: logins_sort(x, sort_type),
                             reverse=bool(sort_order == "desc")
                             )
        for login in logins_list:
            login_status_color = "red" if login["login_status"] == "Failed" else "green"
            login_status = login["login_status"].lower().replace("successful", "succeeded")
            location = [
                bold(login.get("local_ip")), login.get("host_city"), login.get("host_country")
            ]
            login_time = datetime.strptime(login["login_timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            login_time = login_time.strftime("%m-%d-%Y %H:%M:%S")
            print(f" {header_column(login_time)}{bold(login.get('username', 'Unknown user'))} "
                  f"{colored(login_status, color=login_status_color, attrs=['bold'])} on "
                  f"{colored(login['hostname'], attrs=['bold', 'dark'])} "
                  f"({', '.join(location)})"
                  )
        row_break()


def display_applications(applications_list: list):
    """Display the applications results."""
    print(category_header("Applications"), end="\r")
    row_break(52)
    if not applications_list:
        print(colored("No applications found", color="red", attrs=["bold"]))
    app_list = []
    for app in applications_list:
        item = {
            "name": app.get("name", "Unknown"),
            "vendor": app.get("vendor"),
            "version": app.get("version"),
            "category": app.get("category", "Uncatagorized"),
            "last_used_file_name": app.get("last_used_file_name", "Unknown"),
            "last_used_file_hash": app.get("last_used_file_hash", "Unknown"),
            "last_used_timestamp": app.get("last_used_timestamp", "Unknown"),
            "suspicious": app["is_suspicious"],
            "is_normalized": app["is_normalized"],
            "hostname": app["host"]["hostname"],
            "os_version": app["host"]["os_version"],
            "agent_version": app["host"]["agent_version"],
            "external_ip": app["host"].get("external_ip", "Not found"),
            "aid": app["host"]["aid"],
            "mac": app["host"].get("current_mac_address", "Unknown"),
            "internet_exposure": app["host"].get("internet_exposure", "Unknown")
        }
        if item not in app_list:
            app_list.append(item)

    sort_style = APP.applications_sort.split(".")[0]
    app_list = sorted(app_list,
                      key=lambda x: applications_sort(x, sort_style),
                      reverse=bool(".desc" in APP.applications_sort)
                      )
    displayed = []
    shown = []
    for app in app_list:
        display_name = app["hostname"] if sort_style == "hostname" else app["name"]
        display_main = app["name"] if sort_style == "hostname" else app["hostname"]
        header_name = "Application" if sort_style != "hostname" else "Host"
        sub_name = "Application" if sort_style == "hostname" else "Host"
        suspect = colored("Suspicious", color="red", attrs=["bold"]) if app["suspicious"] else ""
        if suspect:
            suspect = f" ({suspect})"
        last_time = "Unknown"
        if app["last_used_timestamp"] != "Unknown":
            last_time = datetime.strptime(app["last_used_timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            last_time = last_time.strftime("%m-%d-%Y %H:%M:%S")
        if display_name not in displayed:
            if displayed:
                row_break()
            print(f"{header_column(header_name)}{bold(display_name)}"
                  f"{suspect if sort_style != 'hostname' else ''}"
                  )
            displayed.append(display_name)
            shown = []
        if sort_style != "hostname":
            print(f"{header_column(sub_name)}{bold(display_main)}")
        if "os_version" not in shown:
            print(f"{header_column('Operating system')}{bold(app['os_version'])}")
            if sort_style == "hostname":
                shown.append("os_version")
        if sort_style == "hostname":
            print(f"{header_column(sub_name)}{bold(display_main)}"
                  f"{suspect}"
                  )
        if last_time != "Unknown":
            print(f"{header_column('Last seen')}{bold(last_time)} "
                  f"({bold(app['last_used_file_name'])})"
                  )
    row_break()


# _  _ ____ _ _  _    ___ _  _ ____ ____ ____ ___     _  _ ____ _  _ ___  _    ____ ____
# |\/| |__| | |\ |     |  |__| |__/ |___ |__| |  \    |__| |__| |\ | |  \ |    |___ |__/
# |  | |  | | | \|     |  |  | |  \ |___ |  | |__/    |  | |  | | \| |__/ |___ |___ |  \
#
# Handles asynchronous processing from the main thread (one thread per category reviewed).
#
def process_category(cat):
    """Process the Discover category by name."""
    if APP.show_updates:
        print(f"  Retrieving {cat}", end=f"{' '*40}\r", flush=True)
    item = batch_get_details(APP.sdk, cat)
    if APP.save_results:
        do_file_dump(cat, item)

    return cat, item


# _  _ ____ _ _  _    ____ ____ _  _ ___ _ _  _ ____
# |\/| |__| | |\ |    |__/ |  | |  |  |  | |\ | |___
# |  | |  | | | \|    |  \ |__| |__|  |  | | \| |___
#
# Primary process - Configures the application, executes
# the audit and then reports results and performance.
#
if __name__ == "__main__":
    # Configure the application global with command line parameters and start tracking performance.
    APP = Application()
    # Process each category within a separate thread.
    with ThreadPoolExecutor() as executor:
        futures = executor.map(process_category, APP.categories)
        # Process and display results for each category as they return.
        _ = [globals()[f"display_{fut[0]}"](fut[1]) for fut in futures]
    # Complete processing and display performance results.
    APP.graceful_finish()
