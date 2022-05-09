#!/usr/bin/env python3
r"""We're pleased to present...

 The CrowdStrike
     _______       __          __  _______ __       __
    |   _   .---.-|  |--.-----|  ||   _   |__.-----|  |--.
    |.  1   |  _  |  _  |  -__|  ||.  1___|  |__ --|     |
    |.  _   |___._|_____|_____|__||.  __) |__|_____|__|__|
    |:  1    \                    |:  |
    |::.. .  /                    |::.|    for FalconPy
    `-------'                     `---'

                       __....---------------.       _.-'' |
                    ,:'_ \__      '._`-.,--- `.    / _.-' |
          _       ,'',-.`.  |_____   `-:_`-.,- \  / / _.- |
         | `.   ,' : `-' ;_,'---. `--..__`-:._`-`' /,'__. :
         |:  `.' o-'`---'  |    |     .--`---<----<:-..__ /
         |::--._.      __.-'  _ |.--.-'---.   )-,. \\`. . \
         |:  ,.  `'`.,'  , , / |:| _|    ,' ,`-/  \ \\ `. :
         |_,'  `-.    _.',' (_ |:| _| _,','`- /    \ \`.  |
                  `-.__  [|_| ||:|__,','`--- /      \ \ ` |
                       `-..._______.:..-----' SSt    \_`. |
                                                       `-.'
Searches for a string within:
    - Operation IDs
    - HTTP methods
    - Endpoints URLs
    - Collection names

If no search string is provided, all results are returned.
"""
from argparse import ArgumentParser, RawTextHelpFormatter
from falconpy._endpoint import api_endpoints, deprecated_endpoints
from tabulate import tabulate


class Color:  # pylint: disable=R0903
    """Class to represent the text color codes used for terminal output."""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    LIGHTBLUE = "\033[94m"
    GREEN = "\033[32m"
    LIGHTGREEN = "\033[92m"
    LIGHTYELLOW = "\033[93m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    LIGHTRED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
parser.add_argument("-s", "--search", help="Search string", required=False)

args = parser.parse_args()

SEARCH = None
if args.search:
    SEARCH = args.search.lower()

grand_total = len(api_endpoints)
deprecated_total = len(deprecated_endpoints)
production_total = grand_total - deprecated_total

# print(f"Total available endpoints: {len(api_endpoints)}")
# print(f"Total deprecated endpoints: {len(deprecated_endpoints)}")

deprecated = []
for dep in deprecated_endpoints:
    deprecated.append(dep[0])
headers = [
    f"{Color.BOLD}Operation{Color.END}",
    f"{Color.BOLD}Method{Color.END}",
    f"{Color.BOLD}Endpoint{Color.END}",
    f"{Color.BOLD}Collection{Color.END}"
    ]
prod_endpoints = []
for endpoint in api_endpoints:
    if endpoint[0] not in deprecated:
        op_id = endpoint[0]
        if SEARCH:
            endpoint[0] = op_id.replace(SEARCH.title(), f"{Color.BOLD}{SEARCH.title()}{Color.END}")
            endpoint[0] = endpoint[0].replace(SEARCH, f"{Color.BOLD}{SEARCH}{Color.END}")
        op_method = endpoint[1]
        op_temp = op_method
        if SEARCH:
            op_temp = op_method.replace(SEARCH.upper(), f"{Color.BOLD}{SEARCH.upper()}{Color.END}")
        if op_method == "DELETE":
            endpoint[1] = f"{Color.RED}{op_temp}{Color.END}"
        if op_method == "POST":
            endpoint[1] = f"{Color.GREEN}{op_temp}{Color.END}"
        if op_method == "GET":
            endpoint[1] = f"{Color.DARKCYAN}{op_temp}{Color.END}"
        if op_method == "PATCH":
            endpoint[1] = f"{Color.MAGENTA}{op_temp}{Color.END}"
        if op_method == "PUT":
            endpoint[1] = f"{Color.LIGHTBLUE}{op_temp}{Color.END}"

        op_ep = endpoint[2]
        if SEARCH:
            endpoint[2] = op_ep.replace(SEARCH, f"{Color.BOLD}{SEARCH}{Color.END}")
        op_collect = endpoint[4]
        if SEARCH:
            endpoint[4] = op_collect.replace(SEARCH, f"{Color.BOLD}{SEARCH}{Color.END}")
        endpoint.pop(3)
        endpoint.pop(4)

        if SEARCH:
            if SEARCH in op_id.lower() or SEARCH in op_method.lower() \
                or SEARCH in op_ep.lower() or SEARCH in op_collect.lower():
                prod_endpoints.append(endpoint)
        else:
            prod_endpoints.append(endpoint)


BABEL_HEADER = fr"""{Color.BOLD}
     {Color.DARKCYAN}_______       __          __  _______ __       __
    |   _   .---.-|  |--.-----|  ||   _   |__.-----|  |--.
    |.  1   |  _  |  _  |  -__|  ||.  1___|  |__ --|     |
    |.  _   |___._|_____|_____|__||.  __) |__|_____|__|__|
    |:  1    \                    |:  |
    |::.. .  /                    |::.|  {Color.END}  for {Color.LIGHTRED}Falcon{Color.YELLOW}Py{Color.END}
 {Color.BOLD}{Color.DARKCYAN}   `-------'                     `---'{Color.END}
"""

print(BABEL_HEADER)
print(tabulate(prod_endpoints, headers, tablefmt="fancy_grid"))
print(f"Total available endpoints: {production_total}")
