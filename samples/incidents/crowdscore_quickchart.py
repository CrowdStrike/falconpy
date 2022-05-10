r"""CrowdScore QuickChart.

  ___   __ __  ____    __  __  _     __  __ __   ____  ____  ______
 /   \ |  T  Tl    j  /  ]|  l/ ]   /  ]|  T  T /    T|    \|      T
Y     Y|  |  | |  T  /  / |  ' /   /  / |  l  |Y  o  ||  D  )      |
|  Q  ||  |  | |  | /  /  |    \  /  /  |  _  ||     ||    /l_j  l_j
|     ||  :  | |  |/   \_ |     Y/   \_ |  |  ||  _  ||    \  |  |
l     |l     | j  l\     ||  .  |\     ||  |  ||  |  ||  .  Y |  |
 \__,_j \__,_j|____j\____jl__j\_j \____jl__j__jl__j__jl__j\_j l__j

                                                for your CrowdScore

Quickly displays your current CrowdScore and charts a histogram
of your score over the past 24 to 36 hours.

Requirements
  asciichartpy
  crowdstrike-falconpy
  pyfiglet
  tabulate
"""
from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime, timedelta
import pyfiglet
import asciichartpy
import tabulate
from falconpy import Incidents


def connect_api(key: str, secret: str, base: str):
    """Return a connected instance of the Incidents Service Class."""
    return Incidents(client_id=key, client_secret=secret, base_url=base)


def consume_command_line():
    """Ingest and parse any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-c", "--hide-chart",
                        help="Hides the chart display",
                        required=False,
                        action="store_true",
                        dest="hide_chart"
                        )
    parser.add_argument("-d", "--show-data",
                        help="Shows the data table display",
                        required=False,
                        action="store_true",
                        dest="show_data"
                        )
    parser.add_argument("-r", "--reverse",
                        help="Reverse the data table sort\nWill not impact chart display",
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-n", "--no-color",
                        help="Disable color output",
                        dest="no_color",
                        required=False,
                        action="store_true"
                        )
    parser.add_argument("-x", "--chart-size",
                        dest="chart_size",
                        help="Size of the chart to display (Max: 100, Default: 25)",
                        required=False
                        )
    parser.add_argument("-m", "--max-rows",
                        dest="max_rows",
                        help="Maximum number of rows to return (5 - 250, Default: 100)",
                        required=False
                        )
    parser.add_argument("-b", "--base-url",
                        dest="base_url",
                        help="CrowdStrike cloud region. (auto or usgov1, Default: auto)",
                        required=False,
                        default="auto"
                        )
    req = parser.add_argument_group("required arguments")
    req.add_argument("-k", "--falcon_client_id", help="Search string", required=True)
    req.add_argument("-s", "--falcon_client_secret", help="Search string", required=True)

    return parser.parse_args()


def get_crowdscore_data(client_id: str, client_secret: str, base_url: str, max_rows: str = None):
    """Retrieve the CrowdScore dataset using the Incidents Service Class."""
    # Connect to the API
    incidents_api = connect_api(client_id, client_secret, base_url)
    ts_range = (datetime.now() + timedelta(hours=-36)).strftime("%Y-%m-%dT%H:%M:%SZ")
    row_limit = DEFAULT_ROW_LIMIT
    if max_rows:
        row_limit = max(min(int(max_rows), 250), 5)
    returned = incidents_api.crowdscore(sort="timestamp.desc",
                                        filter=f"timestamp:>='{ts_range}'",
                                        limit=row_limit
                                        )
    if returned["status_code"] != 200:
        raise SystemExit("Unable to retrieve CrowdScores.")

    return returned


def format_current_score(current_score: str, chart_hidden: bool):
    """Use figlet to create a banner with our current CrowdScore."""
    padding = ""
    if not chart_hidden:
        padding = f"{' ' * 11}"
    crowdscore = pyfiglet.figlet_format(f"{padding}CrowdScore :   {current_score}",
                                        font="cricket",
                                        width=220
                                        )
    cs_color = YELLOW
    if current_score < 10:
        cs_color = GREEN
    if current_score >= 50:
        cs_color = LIGHTRED
    tmp = []
    for line in crowdscore.split("\n"):
        new_line = f"{RED}{line}{ENDMARK}"
        new_line = new_line.replace(
            "                        __ _______                        __",
            f"                        __ _______                        {ENDMARK}__{cs_color}"
            )
        new_line = new_line.replace("-----.|__|", f"-----.{ENDMARK}|__|{cs_color}")
        new_line = new_line.replace("|   _|  -__| __", f"|   _|  -__| {ENDMARK}__{cs_color}")
        new_line = new_line.replace(
            "_____|__| |_____||__|",
            f"_____|__| |_____|{ENDMARK}|__|{cs_color}"
            )
        new_line = new_line.replace(
            "|:  1   |                         |:  1   |",
            f"|:  1   |                         |:  1   |{ENDMARK}{cs_color}"
            )
        new_line = new_line.replace(
            "|::.. . |                         |::.. . |",
            f"|::.. . |                         |::.. . |{ENDMARK}{cs_color}"
            )
        new_line = new_line.replace(
            "`-------'                         `-------'",
            f"`-------'                         `-------'{ENDMARK}{cs_color}"
            )
        tmp.append(f"{RED}{new_line}{ENDMARK}")
    crowdscore = "\n".join(tmp)
    return crowdscore


def format_data_table(crowdscore_lookup: dict, do_reverse: bool):
    """Format the values in our data table."""
    score_data = []
    for score in crowdscore_lookup:
        score_reg = score["score"]
        score_adj = score["adjusted_score"]
        if score_reg != score_adj:
            score["score"] = score_adj
        cs_color = YELLOW
        if score["score"] < 10:
            cs_color = GREEN
        if score["score"] >= 50:
            cs_color = LIGHTRED
        score["score"] = f"{cs_color}{score['score']}{ENDMARK}"
        score.pop("cid")
        score.pop("adjusted_score")
        score.pop("id")
        score["timestamp"] = f"\t\t{score['timestamp']}"
        score_data.append(score)
    if do_reverse:
        score_data.reverse()
    score_headers = {
        "timestamp": f"{BOLD}Time{ENDMARK}",
        "score": f"{BOLD}CrowdScore{ENDMARK}"
    }
    return score_data, score_headers


def display_data_table(dataset: dict, reverse: bool):
    """Format and then display our data table."""
    # Format our scores list and table headers
    scores, headers = format_data_table(dataset, reverse)
    tabulate.PRESERVE_WHITESPACE = True
    data_table = tabulate.tabulate(scores, headers)
    data_table = data_table.replace(
        "--------------------------",
        "\t\t--------------------------"
        )
    print(f"\n\t\t{data_table}")
    print(f"\n\t\t{BOLD}{len(dataset)}{ENDMARK} scores returned.\n")


def display_chart(dataset: dict, chart_size: int = None):
    """Format and display our ascii histogram."""
    # Create our list of scores for our ASCII chart
    scores = [x["score"] for x in dataset]
    # We pull the list in desc order to make it easy to get our most recent score
    # Reverse this list to make an accurate histogram that doesn't confuse viewers
    scores.reverse()
    # Calculate our chart size
    chart_height = DEFAULT_CHART_SIZE
    if chart_size:
        chart_height = max(min(int(chart_size), 100), 5)
    chart_settings = {}
    chart_settings["height"] = chart_height
    # Display our ascii chart
    print(asciichartpy.plot(scores, chart_settings))


def display_crowdscores(arguments: ArgumentParser):
    """Execute main routine and display the current CrowdScore result."""
    # Grab all the CrowdScores
    current_crowdscore_lookup = get_crowdscore_data(arguments.falcon_client_id,
                                                    arguments.falcon_client_secret,
                                                    arguments.base_url,
                                                    arguments.max_rows
                                                    )
    # Grab the most recent CrowdScore, format and display it
    print(format_current_score(current_crowdscore_lookup['body']['resources'][0]['score'],
                               arguments.hide_chart
                               ))
    if not arguments.hide_chart:
        # Display the chart
        display_chart(current_crowdscore_lookup["body"]["resources"], arguments.chart_size)
    if arguments.show_data:
        # Display the data table
        display_data_table(current_crowdscore_lookup["body"]["resources"], arguments.reverse)


# Default chart size (Max: 100, Min: 5)
DEFAULT_CHART_SIZE = 25
# Default row limit (Max: 250, Min: 1, Default: 100)
DEFAULT_ROW_LIMIT = 100
# Color codes for terminal output
YELLOW = "\033[93m"
GREEN = "\033[32m"
LIGHTRED = "\033[91m"
RED = "\033[31m"
ENDMARK = "\033[0m"
BOLD = "\033[1m"
# Ingest any provided command line arguments
args = consume_command_line()
if args.no_color:
    # Turn off our flash since they asked nicely
    YELLOW = ""
    GREEN = ""
    LIGHTRED = ""
    RED = ""
    ENDMARK = ""
    BOLD = ""

# Run the main routine
display_crowdscores(args)
