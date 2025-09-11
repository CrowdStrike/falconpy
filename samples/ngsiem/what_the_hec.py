r"""FalconPy NG-SIEM HEC tester and event simulator.

██╗    ██╗██╗  ██╗ █████╗ ████████╗    ████████╗██╗  ██╗███████╗
██║    ██║██║  ██║██╔══██╗╚══██╔══╝    ╚══██╔══╝██║  ██║██╔════╝
██║ █╗ ██║███████║███████║   ██║          ██║   ███████║█████╗
██║███╗██║██╔══██║██╔══██║   ██║          ██║   ██╔══██║██╔══╝
╚███╔███╔╝██║  ██║██║  ██║   ██║          ██║   ██║  ██║███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚══════╝

                ██╗  ██╗███████╗ ██████╗██████╗ ██╗
                ██║  ██║██╔════╝██╔════╝╚════██╗██║
                ███████║█████╗  ██║       ▄███╔╝██║
                ██╔══██║██╔══╝  ██║       ▀▀══╝ ╚═╝
                ██║  ██║███████╗╚██████╗  ██╗   ██╗
                ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═╝   ╚═╝

                                                🦅 FalconPy v1.5.1

This sample simulates events and imports them into a CrowdStrike Falcon NGSIEM tenant.

The sample can be used to demonstrate importing standard JSON events and raw new line
delimited JSON, XML and CSV files. This sample is intended to provide developers with a
starting point to begin working with the HTTP event collector that is provided by the 
CrowdStrike FalconPy library.

Creation date: 05.02.2025 - jshcodes@CrowdStrike

██  ███ █ █ ███ █   ███ ███ ███ ███   █   █ ███ ███ ███
█ █ █   █ █ █   █   █ █ █ █ █   █ █   ██  █ █ █  █  █
█ █ ███ █ █ ███ █   █ █ ███ ███ ██    █ █ █ █ █  █  ███
█ █ █   █ █ █   █   █ █ █   █   █ █   █  ██ █ █  █  █
██  ███  █  ███ ███ ███ █   ███ █ █   █   █ ███  █  ███

This solution demonstrates HTTP event ingestion, but does not discuss parsing. Parsers
should be developed specifically to handle the data being ingested. More information
regarding parsers can be found by navigating to Support and Resources -> Documentation
in the Falcon console and selecting "Falcon Next-Gen SIEM".
"""
from argparse import Namespace, ArgumentParser, RawTextHelpFormatter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from json import load
from logging import getLogger, Logger, basicConfig, DEBUG
from multiprocessing import cpu_count
from os import remove, path
from time import time
from falconpy import HTTPEventCollector, IngestPayload, TimeUnit, Indicator, Color, random_string


def format_time(length: float):
    """Format the reported execution time into hours / minutes / seconds."""
    delta = str(timedelta(seconds=length))
    parts = delta.split(":")
    stub = "seconds"
    if int(f"{parts[2]:.2}") < 2:
        stub = "second"
    if int(parts[1]) > 0:
        stub = "minutes"
        if int(parts[1]) < 2:
            stub = "minute"
    if int(parts[0]) > 0:
        stub = "hours"
        if int(parts[0]) < 2:
            stub = "hour"

    return f"{delta} {stub}"


def parse_command_line() -> Namespace:
    """Ingest the provided command line parameters."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-t", "--test_connection",
                        help="Run API connectivity test",
                        action="store_true",
                        default=False
                        )
    asynch = parser.add_argument_group("asynchronous processing configuration")
    asynch.add_argument("-tc", "--threads",
                        help="Set the number of asynchronous threads to use "
                        "(applies to single [-as], list and json file processing)",
                        default=270
                        )
    asynch.add_argument("-as", "--asynchronous",
                        help="Run single event simulation asynchronously "
                        "(applies to single processing only)",
                        action="store_true",
                        default=False
                        )
    asynch.add_argument("-p", "--progress",
                        help="Show asynchronous progress (applies to list and json processing only)",
                        action="store_true",
                        default=False
                        )
    simulate = parser.add_argument_group("event simulation configuration")
    simulate.add_argument("-s", "--single",
                          help="Import simulated events individually",
                          action="store_true",
                          default=False
                          )
    simulate.add_argument("-l", "--list",
                          help="Import a list of simulated events",
                          action="store_true",
                          default=False
                          )
    simulate.add_argument("-n", "--number",
                          help="Number of host messages to simulate "
                          "(applies to single and list processing only)",
                          default=5
                          )
    files = parser.add_argument_group("file import configuration")
    mutual = files.add_mutually_exclusive_group()
    mutual.add_argument("-j", "--json",
                        help="Import a JSON file of events",
                        action="store_true",
                        default=False
                        )
    mutual.add_argument("-r", "--raw",
                        help="Import a raw file of events",
                        action="store_true",
                        default=False
                        )
    files.add_argument("-fn", "--filename",
                       help="Filename to import",
                       default=5
                       )
    files.add_argument("-g", "--generate_file",
                       help="Generate the raw file to be loaded (raw import only)",
                       action="store_true",
                       default=False
                       )
    files.add_argument("-w", "--wrap",
                       help="Disable wrapping of individual events with an event delimiter.\n"
                       "CSV formatting does not support event wrapping.\n"
                       "XML documents without a root element are not considered well-formed.",
                       default=True,
                       action="store_false"
                       )
    config = parser.add_argument_group("ingest configuration")
    config.add_argument("-a", "--ngsiem_api_key",
                        help="CrowdStrike Falcon NGSIEM API key",
                        default=None,
                        required=True
                        )
    config.add_argument("-u", "--ngsiem_url_key",
                        help="CrowdStrike Falcon NGSIEM URL key",
                        default=None,
                        required=True
                        )
    config.add_argument("-f", "--format",
                        help="Ingest format\nDefaults to \"json\"",
                        choices=["json", "csv", "yaml", "xml"],
                        default="json"
                        )
    config.add_argument("-c", "--cloud_region",
                        help="CrowdStrike Falcon cloud region\nDefaults to \"us1\"",
                        choices=["us1", "us2", "eu1", "gov1"],
                        default="us1"
                        )
    config.add_argument("-tu", "--timeunit",
                        help="Set the time unit used for timestamps\nDefaults to \"nanoseconds\"",
                        choices=["seconds", "milliseconds", "nanoseconds"],
                        default="nanoseconds"
                        )
    config.add_argument("-to", "--timeout",
                        help="Set the request timeout",
                        default=None
                        )
    config.add_argument("-rc", "--retry_count",
                        help="Set the request retry count",
                        default=5
                        )
    logging = parser.add_argument_group("logging configuration")
    logging.add_argument("-d", "--debug",
                         help="Enable API debugging",
                         action="store_true",
                         default=False
                         )
    logging.add_argument("-df", "--debugfile",
                         help="Write debug logs to a file",
                         default=None
                         )
    logging.add_argument("-cl", "--clear_log",
                         help="Clear the debug log file before processing",
                         action="store_true",
                         default=False
                         )
    logging.add_argument("--no_sanitize",
                         help="Disable log sanitization",
                         action="store_false",
                         default=True
                         )

    return parser.parse_args()


def connectivity_test(hec: HTTPEventCollector):
    """Run an API connectivity test using the provided credentials."""
    return hec.test_connection()


def thread_count() -> int:
    """Calculate the default thread count."""
    cores = cpu_count()
    return min(cores * 2, 20)


def single_import(hec: HTTPEventCollector, num_hosts: int):
    """Import singular events."""
    run_start = time()
    set_ingest_destination(hec, False)
    print(f"Randomly generating {num_hosts:,} events")
    host_list = [random_string(8).upper() for _ in range(num_hosts)]
    print(f"Processing {num_hosts:,} simulated events")
    gen_stop = time()
    for hostname in host_list:
        payload = {"host": hostname, "message": random_string(20), "fields": {"#falconpy": "HEC testing"}}
        hec.send_event(payload)
    print(f"Run complete with {num_hosts:,} event{'s' if num_hosts > 1 else ''} processed."
          f"{' '*20}\n{format_time(gen_stop - run_start)} spent generating events.\n"
          f"{format_time(time() - gen_stop)} spent importing events.\n"
          f"{format_time(time() - run_start)} total time elapsed."
          )


def single_import_async(hec: HTTPEventCollector, num_hosts: int, threads: int = None):
    """Import singular events asynchronously."""
    run_start = time()
    success_count = 0
    set_ingest_destination(hec, False)
    print(f"Randomly generating {num_hosts:,} events")
    host_list = [random_string(8).upper() for _ in range(num_hosts)]
    payloads = [
        {"host": hostname, "message": random_string(20),"fields": {"#falconpy": "HEC testing"}} for hostname in host_list
        ]
    print(f"Processing {len(payloads):,} simulated events")
    gen_stop = time()
    with ThreadPoolExecutor(max_workers=threads if threads else thread_count(),
                            thread_name_prefix="thread"
                            ) as executor:
        futures = executor.map(hec.send_event, payloads)
        success_count = sum(1 for future in futures if future == 200)
    print(f"Run complete with {success_count:,} event{'s' if success_count > 1 else ''} processed."
          f"{' '*20}\n{format_time(gen_stop - run_start)} spent generating events.\n"
          f"{format_time(time() - gen_stop)} spent importing events.\n"
          f"{format_time(time() - run_start)} total time elapsed."
          )


def list_import(hec: HTTPEventCollector, num_hosts: int, show_progress: bool = False, debug: bool = False):
    """Import a list of events."""
    run_start = time()
    progress = Indicator()
    set_ingest_destination(hec, False)
    print(f"Randomly generating {num_hosts:,} events")
    host_list = [random_string(8).upper() for _ in range(num_hosts)]
    event_list = [
        {"host": hostname, "message": random_string(20), "fields": {"#falconpy": "HEC testing"}} for hostname in host_list
        ]
    print(f"Processing a list of {len(event_list):,} simulated events")
    gen_stop = time()
    if show_progress:
        returned = 0
        for returned in hec.send_event_list(event_list, show_progress):
            print(f"  {progress} Processed {returned:,} events, "
                  f"{format_time(time() - run_start)} elapsed.",
                  end="\r"
                  )
        if debug:
            hec.log_activity(f"EVENT LIST: Processing of {len(event_list)} "
                             f"events completed with {returned} successes"
                             )
    else:
        returned = hec.send_event_list(event_list)
    print(f"Run complete with {returned:,} events processed.{' '*20}\n"
          f"{format_time(gen_stop - run_start)} spent generating events.\n"
          f"{format_time(time() - gen_stop)} spent importing events.\n"
          f"{format_time(time() - run_start)} total time elapsed."
          )


def json_import(hec: HTTPEventCollector, filename: str, show_progress: bool = False):
    """Run a JSON file import."""
    run_start = time()
    progress = Indicator()
    set_ingest_destination(hec, False)
    with open(filename, "r", encoding="utf-8") as json_input:
        event_list = load(json_input)
    print(f"Processing {len(event_list):,} JSON file events")
    gen_stop = time()
    if show_progress:
        for returned in hec.send_event_list(event_list, show_progress):
            print(f"  {progress} Processed {returned:,} events", end="\r")
    else:
        returned = hec.send_event_list(event_list)

    print(f"Run complete with {returned:,} events processed.{' '*20}\n"
          f"{format_time(gen_stop - run_start)} spent generating events.\n"
          f"{format_time(time() - gen_stop)} spent importing events.\n"
          f"{format_time(time() - run_start)} total time elapsed."
          )


# pylint: disable=R0913,R0917
def raw_import(hec: HTTPEventCollector, filename: str, generate: bool, count: int, fmt: str, wrap: bool):
    """Run a raw file import."""
    run_start = time()
    if generate:
        print(f"Generating the raw file {filename}")
        with open(filename, "w", encoding="utf-8") as generated:
            for _ in range(0, count):
                tstamp = int(datetime.now(timezone.utc).timestamp()*TimeUnit["NANOSECONDS"].value)
                payload = IngestPayload(host=random_string(8).upper(),
                                        message=random_string(20),
                                        timestamp=tstamp,
                                        )
                if fmt == "json":
                    generated.write(
                        f"{payload.to_json(raw=True, nowrap=not wrap)}\n"
                        )
                elif fmt == "csv":
                    # Example output headers: category,host,kind,module,timestamp,timeunit,type,message
                    output = payload.to_csv().split("\n")
                    generated.write(f"{output[1]}\n")
                elif fmt == "xml":
                    generated.write(
                        f"{payload.to_xml(raw=True, nowrap=not wrap)}\n"
                        )
                else:
                    raise SystemExit("Invalid format specified or not yet implemented.")
    gen_stop = time()
    print(f"Processing the raw file {filename}")
    set_ingest_destination(hec, True)
    response = hec.send_event_file(filename)
    print(f"Run complete.{' '*40}")
    if response == 500:
        print("Response failed with an error. Check timeout and retry counts.")
    else:
        print(f"{format_time(gen_stop - run_start)} spent generating events.\n"
              f"{format_time(time() - gen_stop)} spent importing events.\n"
              f"{format_time(time() - run_start)} total time elapsed."
              )


def set_ingest_destination(hec: HTTPEventCollector, raw: bool = False):
    """Set the raw ingest flag on the HEC collector."""
    hec.raw_ingest = raw


def show_logo(hec: HTTPEventCollector):
    """Show the startup logo. Yes, I know it's a little ridiculous... it was late."""
    print(f"{Color.BLUE}┏{'━'*55}┓{Color.END}")
    for line in hec.__doc__.split("\n")[2:-1]:
        for element in ["⣠", "⣴", "⣾", "⣿", "⣶", "⣤", "⣄", "⣷", "⣆", "⠚", "⢛", "⠿", "⠈", "⠙", "⠉",
                        "⠿", "⠻", "⡇", "⡿", "⠋", "⠁", "⠏", "⠃", "⣦", "⢉", "⡀", "⡄", "⠹", "⡏", "⢠",
                        "⢀", "⠸", "⢸"
                        ]:
            line = line.replace(element, f"{Color.RED}{element}{Color.END}")
        if "CrowdStrike Falcon" in line:
            line = line.replace("CrowdStrike Falcon",
                                f"{Color.BOLD}{Color.RED}CrowdStrike {Color.END}"
                                f"{Color.LIGHTRED}Falcon{Color.END}"
                                )
            line = f"{line}{' '*13}"
        if "FalconPy" in line:
            line = line.replace("FalconPy", f"{Color.BOLD}FalconPy{Color.END}")
        line = line.replace("█", f"{Color.GREEN}█{Color.END}")
        linecheck = line
        for element in [Color.GREEN, Color.RED, Color.LIGHTRED, Color.END, Color.BOLD]:
            linecheck = linecheck.replace(element, "")
        if len(linecheck) < 51:
            line = f"{line}{' '*(50-len(linecheck)+1)}"
        print(f"{Color.BLUE}┃{Color.END}  {line} {' '*(50-len(line)+1)} {Color.BLUE}┃{Color.END}")
    print(f"{Color.BLUE}┗{'━'*55}┛{Color.END}")


cmdline = parse_command_line()
if cmdline.clear_log and cmdline.debugfile:
    if path.exists(cmdline.debugfile):
        remove(cmdline.debugfile)
if cmdline.debug:
    basicConfig(level=DEBUG, filename=cmdline.debugfile, format="%(asctime)s:%(module)s:%(threadName)s:%(message)s")
    logger: Logger = getLogger("HEC Tester")

with HTTPEventCollector(api_key=cmdline.ngsiem_api_key,
                        api_url_key=cmdline.ngsiem_url_key,
                        ingest_format=cmdline.format,
                        ingest_region=cmdline.cloud_region,
                        ingest_timeunit=cmdline.timeunit,
                        ingest_timeout=int(cmdline.timeout) if cmdline.timeout else None,
                        raw_ingest=bool(cmdline.raw),
                        debug=cmdline.debug,
                        sanitize_log=cmdline.no_sanitize,
                        thread_count=int(cmdline.threads) if cmdline.threads else None,
                        retry_count=int(cmdline.retry_count)
                        ) as collector:

    if not (cmdline.debug) or (cmdline.debug and cmdline.debugfile):
        show_logo(collector)

    if cmdline.test_connection:
        if not connectivity_test(collector):
            raise SystemExit("Connection test failed")
        print("Connection test succeeded")

    if cmdline.single:
        if cmdline.asynchronous:
            single_import_async(collector, int(cmdline.number), int(cmdline.threads))
        else:
            single_import(collector, int(cmdline.number))

    if cmdline.list:
        list_import(collector, int(cmdline.number), bool(cmdline.progress), bool(cmdline.debug))

    if cmdline.json:
        json_import(collector, cmdline.filename, bool(cmdline.progress))

    if cmdline.raw:
        if not path.exists(cmdline.filename) and not cmdline.generate_file:
            raise SystemExit("You have specified an invalid raw file name "
                             "or not instructed me to generate new events."
                             )
        # XML events without a root element are not considered well-formed.
        if cmdline.format == "xml":
            cmdline.wrap = True
        raw_import(collector,
                   cmdline.filename,
                   cmdline.generate_file,
                   int(cmdline.number),
                   cmdline.format,
                   bool(cmdline.wrap)
                   )
