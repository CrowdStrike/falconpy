r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

This sample utilizes the Threat Graph service collection
to ingest IOCs, then identify if they exist within your environment.

This project only accepts STIX2.x format for the IOC file.
This project only ingests IP addresses (IPv4, IPv6), domain names, and hashes (MD5, SHA256).

USAGE EXAMPLES:
    # Display findings in terminal
    python3 threat_finder.py -k $KEY -s $SECRET -o stix2_example.json
    
    # Export findings to JSON
    python3 threat_finder.py -k $KEY -s $SECRET -o stix2_example.json -e json
    
    # Export findings to CSV
    python3 threat_finder.py -k $KEY -s $SECRET -o stix2_example.json -e csv

Creation date: 12.9.25 - alhumaw
"""

import json
import logging
import re
import csv
from dataclasses import dataclass, asdict
from datetime import datetime
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
try:
    from stix2 import parse
except ImportError as no_stix2:
    raise SystemExit("The stix2 library must be installed.\n"
                     "Install it with `python3 -m pip install stix2`."
                     ) from no_stix2
try:
    from falconpy import ThreatGraph, Hosts, APIError
except ImportError as no_falconpy:
    raise SystemExit("The CrowdStrike FalconPy library must be installed.\n"
                     "Install it with `python3 -m pip install crowdstrike-falconpy`."
                     ) from no_falconpy


def parse_command_line() -> Namespace:
    """Parse any provided command line arguments and return the namespace."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)

    require = parser.add_argument_group("required arguments")
    require.add_argument("-k", "--client_id", required=True, help="CrowdStrike API client ID")
    require.add_argument("-s", "--client_secret", required=True, help="CrowdStrike API client secret")

    parser.add_argument("-d", "--debug", help="Enable API debugging", action="store_true", default=False)

    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument("-f", "--file", help="The file containing the IOCs")
    parser.add_argument("-o", "--output", default=None, help="File name to output results.")
    parser.add_argument("--type", default=None, help="Type of export: csv, json(default).", choices=['json', 'csv'])
    parsed = parser.parse_args()

    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)

    if parsed.type and not parsed.output:
        parser.error("Must specify output file name with type.")

    return parsed


def connect_api(key: str, secret: str, debug: bool) -> tuple:
    """Connect to the CrowdStrike API and return an MessageCenter instance.
    
    Parameters:
        key -- CrowdStrike API client ID. String.
        secret -- CrowdStrike API client secret. String.
        debug -- Enable debug logging. Boolean.
    
    Returns: MessageCenter service class instance.
    """
    try:
        if debug:
            logging.basicConfig(level=logging.DEBUG)
        return (
            ThreatGraph(client_id=key, client_secret=secret, debug=debug),
            Hosts(client_id=key, client_secret=secret, debug=debug)
            )
    except APIError as e:
        print(f"Failed to connect to API: {e}")
        return e

@dataclass
class Device:
    """Represents a single Device."""
    device_id: str
    external_ip: str
    hostname: str
    last_seen: str
    local_ip: str
    os_version: str

@dataclass
class IOCObservation:
    """Represents a single IOC observation on a device."""
    ioc_value: str
    ioc_type: str
    device_id: str
    vertex_id: str
    timestamp: str
    device_info: Device = None
    processes: list = None

    def __post_init__(self):
        if self.processes is None:
            self.processes = []

class STIXHandler:
    """STIX2 Interface."""
    def __init__(self, file_name):
        self.file_name = file_name
        self.objects = {}

    def parse_file(self) -> None:
        """Parse the file to instantiate a STIX2 object."""
        indicators = {}
        try:
            with open(self.file_name, "r", encoding='utf-8') as f:
                file = f.read()
                indicators = json.loads(file)
        except FileNotFoundError:
            print(f"File not found: {self.file_name}")
            return
        try:
            stix_obj = parse(indicators)
        except Exception as e:
            print(e)
            return

        if stix_obj.type == 'bundle':
            obj = stix_obj.objects
            return self._set_objects(stix_obj=obj)
        obj = [stix_obj]
        return self._set_objects(stix_obj=obj)

    def _set_objects(self, stix_obj: list[str]) -> None:
        print(f"\n[1] Collecting indicators from file: {self.file_name}....")
        threat_graph_map = {
            'file:hashes.SHA256': 'sha256',
            'file:hashes.MD5': 'md5',
            'file:hashes.SHA1': 'sha1',
            'ipv4-addr:value': 'ipv4',
            'ipv6-addr:value': 'ipv6',
            'domain-name:value': 'domain'
        }
        for obj in stix_obj:
            if obj.type != 'indicator':
                print(f'\tObject is not an indicator: {obj.type}')
                continue

            pattern = obj.pattern
            ioc_type = None
            for stix_key, graph_type in threat_graph_map.items():
                if stix_key in pattern:
                    ioc_type = graph_type
                    break

            if not ioc_type:
                print(f"\tUnsupported type -> {pattern}, skipping.")
                continue

            value_match = re.search(r"'([^']+)'", pattern)

            if value_match:
                ioc_value = value_match.group(1)
                self.objects[ioc_type] = self.objects.get(ioc_type, [])
                self.objects[ioc_type].append(ioc_value)

class ThreatGraphManager:
    """ThreatGraph Interface for finding threats and correlating threats."""
    def __init__(self, threat_graph: ThreatGraph, hosts: Hosts, indicators: STIXHandler):
        self.threat_graph = threat_graph
        self.hosts = hosts
        self.indicators = indicators

        self.observations = []  # List[IOCObservation]
        self.process_cache = {}  # Cache for process details
        self.ioc_groups:dict[str:IOCObservation] = {}

    def get_all_vertex(self) -> list[IOCObservation]:
        """Query ThreatGraph and create observation records."""
        print("\n[2] Using ThreatGraph to search for indicators...")

        for ioc_type, values in self.indicators.objects.items():
            for value in values:
                response = self.threat_graph.combined_ran_on_get(
                    type=ioc_type, value=value
                )
                processes = []
                if response['status_code'] == 200:
                    resources = response['body'].get('resources', [])

                    for resource in resources:
                        device_id = resource.get('device_id')
                        if not device_id:
                            continue

                        vertex_id = resource.get('id')
                        vertex_response = self.threat_graph.get_summary(
                            ids=[vertex_id],
                            vertex_type='any-vertex'
                        )
                        if vertex_response['status_code'] == 200:
                            vertex_data = vertex_response['body'].get('resources', [])
                            if vertex_data:
                                edges = vertex_data[0].get('edges', {})
                                processes = []
                                for edge_type, edge_list in edges.items():
                                    cur_observation = {}
                                    for edge in edge_list:
                                        entity_id = edge.get('id', '')
                                        if entity_id.startswith('pid:'):
                                            cur_observation['process_id'] = entity_id
                                            cur_observation['edge_type'] = edge_type
                                            cur_observation['direction'] = edge.get('direction')
                                            cur_observation['timestamp'] = edge.get('timestamp')
                                            cur_observation['details'] = None
                                            processes.append(cur_observation)

                        observation = IOCObservation(
                            ioc_value=value,
                            ioc_type=ioc_type,
                            device_id=device_id,
                            vertex_id=vertex_id,
                            timestamp=resource.get('timestamp'),
                            processes=processes
                        )

                        self.observations.append(observation)

                    print(f"\t{value} -- FOUND on {len(resources)} device(s)")
                else:
                    print(f"\t{value} -- NOT FOUND")

        return self.observations

    def identify_all_hosts(self) -> None:
        """Get device details and map to observations."""
        print("\n[3] Locating hosts related to each IOC...")

        # Get unique device IDs from observations
        device_ids = list(obs.device_id for obs in self.observations)

        if not device_ids:
            print("\tNo devices to query")
            return

        print(f"\tSearching for {len(device_ids)} unique device(s).")

        responses = self.hosts.get_device_details(ids=device_ids)

        if responses['status_code'] in [200, 404]:
            device_details = responses['body'].get('resources', [])

            device_map = {}
            for device in device_details:
                device_id = device.get('device_id')
                device_map[device_id] = Device(
                    device_id=device_id,
                    external_ip=device.get('external_ip', 'N/A'),
                    hostname=device.get('hostname', 'Unknown'),
                    last_seen=device.get('last_seen', 'N/A'),
                    local_ip=device.get('local_ip', 'N/A'),
                    os_version=device.get('os_version', 'Unknown')
                )

            # map device info back to observations
            for observation in self.observations:
                if observation.device_id in device_map:
                    observation.device_info = device_map[observation.device_id]

            active = len(device_map)
            total = len(device_ids)
            print(f"\tSuccessfully identified {active}/{total} total device(s).")
        else:
            print(f"\tError retrieving hosts: {responses['status_code']}")

    def get_process_details(self) -> None:
        """Query process details and map to observations."""
        print("\n[4] Retrieving process information...")
        process_ids = set()
        for observation in self.observations:
            for process in observation.processes:
                process_ids.add(process['process_id'])

        if not process_ids:
            print("\tNo process information found")
            return

        print(f"\tQuerying details for {len(process_ids)} unique process(es)")

        response = self.threat_graph.get_summary(
            ids=list(process_ids),
            vertex_type='process'
        )

        if response['status_code'] == 200:
            for process in response['body'].get('resources', []):
                process_id = process.get('id')
                props = process.get('properties', {})
                edges = process.get('edges', {})

                self.process_cache[process_id] = {
                    'command_line': props.get('CommandLine'),
                    'image_file': props.get('ImageFileName'),
                    'sha256': props.get('SHA256HashData'),
                    'user_sid': props.get('UserSid'),
                    'parent_pid': props.get('ParentProcessId'),
                    'start_time': props.get('ProcessStartTime_formatted'),
                    'raw_pid': props.get('RawProcessId'),

                    'dns_queries': [
                        {
                            'domain': e.get('id', '').split(':')[-1],
                            'timestamp': e.get('timestamp')
                        }
                        for e in edges.get('dns', [])
                        ],

                    'ipv4_connections': [
                        {
                            'ip': e.get('id', '').split(':')[-1],
                            'timestamp': e.get('timestamp'),
                            'direction': e.get('direction')
                        }
                        for e in edges.get('ipv4', [])
                        ],

                    'files_written': [
                        {
                            'path': e.get('properties', {}).get('TargetFileName', 'Unknown'),
                            'timestamp': e.get('timestamp')
                        }
                        for e in edges.get('module_written', [])
                        ]
                    }

            # Map process details back to observations
            for observation in self.observations:
                for process in observation.processes:
                    pid = process['process_id']
                    if pid in self.process_cache:
                        process['details'] = self.process_cache[pid]

            print(f"\tSuccessfully retrieved details for {len(self.process_cache)} process(es)")
        else:
            print(f"\tError retrieving process details: {response['status_code']}")

        # Group observations by IOC
        self._set_ioc_groups()

    def _set_ioc_groups(self) -> None:
        for obs in self.observations:
            if obs.ioc_value not in self.ioc_groups:
                self.ioc_groups[obs.ioc_value] = []
            self.ioc_groups[obs.ioc_value].append(obs)

    def display_findings(self) -> None:
        """Display findings with process edge information."""
        print("\n" + "="*80)
        print("THREAT INTELLIGENCE FINDINGS")
        print("="*80)

        if not self.observations:
            print("\nNo threats found")
            return

        for ioc_value, observations in self.ioc_groups.items():
            active_obs = [obs for obs in observations if obs.device_info]

            print(f"\nIOC: {ioc_value} ({observations[0].ioc_type})")
            print(f"\tFound on {len(active_obs)} active device(s):")

            for obs in active_obs:
                print(f"\n\tDevice: {obs.device_info.hostname}")
                print(f"\t\tDevice ID: {obs.device_id}")
                print(f"\t\tOS: {obs.device_info.os_version}")
                print(f"\t\tLocal IP: {obs.device_info.local_ip}")
                print(f"\t\tExternal IP: {obs.device_info.external_ip}")
                print(f"\t\tLast Seen: {obs.device_info.last_seen}")

                if obs.processes:
                    print(f"\n\t\tProcess Activity: {len(obs.processes)} process(es) found")

                    for proc in obs.processes:
                        if proc.get('details'):
                            d = proc['details']
                            print(f"\n\t\t\tProcess: {d.get('image_file', 'Unknown')}")
                            print(f"\t\t\t\tCommand Line: {d.get('command_line', 'N/A')[:50] + '...'}")
                            print(f"\t\t\t\tUser SID: {d.get('user_sid', 'N/A')}")
                            print(f"\t\t\t\tStart Time: {d.get('start_time', 'N/A')}")
                            print(f"\t\t\t\tSHA256: {d.get('sha256', 'N/A')}")

                            if d.get('dns_queries'):
                                print(f"\n\t\t\t\tDNS Queries ({len(d['dns_queries'])} total):")
                                for dns in d['dns_queries']:
                                    print(f"\t\t\t\t\t- {dns['domain']}")

                            if d.get('ipv4_connections'):
                                print(f"\n\t\t\t\tIP Connections ({len(d['ipv4_connections'])} total):")
                                for conn in d['ipv4_connections']:
                                    print(f"\t\t\t\t\t- {conn['ip']} ({conn['direction']})")

                            if d.get('files_written'):
                                print(f"\n\t\t\t\tFiles Written ({len(d['files_written'])} total):")
                                for file in d['files_written']:
                                    filename = file['path'].split('\\')[-1] if file['path'] else 'Unknown'
                                    print(f"\t\t\t\t\t- {filename}")
                else:
                    print("\n\t\tProcess Activity: No process details available")

        # Summary
        total_obs = len(self.observations)
        active_obs = sum(1 for obs in self.observations if obs.device_info)
        with_processes = sum(1 for obs in self.observations if obs.processes)

        print("\n" + "="*80)
        print("Summary:")
        print(f"\t- {len(self.ioc_groups)} unique IOC(s) detected")
        print(f"\t- {total_obs} total observation(s)")
        print(f"\t- {active_obs} active device(s)")
        print(f"\t- {with_processes} observation(s) with process details")
        print("="*80)

def export_findings(args: Namespace, threats: ThreatGraphManager) -> None:
    """Export threat findings to CSV or JSON format.
    
    Parameters:
        args -- Command line arguments including export filename
        threats -- ThreatGraphManager instance with collected findings
    """
    if not threats.observations:
        print("\n[5] No findings to export")
        return

    if args.type is None:
        args.type = 'json'

    print(f"\n[5] Exporting findings to {args.output}...")

    if args.type == 'json':
        export_to_json(args.output, threats)
    elif args.type == 'csv':
        export_to_csv(args.output, threats)
    else:
        print(f"Unsupported file format: {args.output}. Please use .json or .csv")
        return

    print(f"\tSuccessfully exported {len(threats.observations)} observation(s) to {args.output}")


def export_to_json(filename: str, threats: ThreatGraphManager) -> None:
    """Export findings to JSON format with full nested structure.
    
    Parameters:
        filename -- Output filename
        threats -- ThreatGraphManager instance with collected findings
    """
    export_data = {
        'export_timestamp': datetime.now().isoformat(),
        'summary': {
            'total_iocs': len(threats.ioc_groups),
            'total_observations': len(threats.observations),
            'active_devices': sum(1 for obs in threats.observations if obs.device_info),
            'observations_with_processes': sum(1 for obs in threats.observations if obs.processes)
        },
        'findings': []
    }

    for ioc_value, observations in threats.ioc_groups.items():
        ioc_data = {
            'ioc_value': ioc_value,
            'ioc_type': observations[0].ioc_type if observations else 'unknown',
            'devices': []
        }

        for obs in observations:
            device_data = {
                'device_id': obs.device_id,
                'vertex_id': obs.vertex_id,
                'observation_timestamp': obs.timestamp,
                'device_info': asdict(obs.device_info) if obs.device_info else None,
                'processes': []
            }

            for process in obs.processes:
                process_data = {
                    'process_id': process.get('process_id'),
                    'edge_type': process.get('edge_type'),
                    'direction': process.get('direction'),
                    'timestamp': process.get('timestamp'),
                    'details': process.get('details')
                }
                device_data['processes'].append(process_data)

            ioc_data['devices'].append(device_data)

        export_data['findings'].append(ioc_data)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)


def export_to_csv(filename: str, threats: ThreatGraphManager) -> None:
    """Export findings to CSV format with flattened structure.
    
    Parameters:
        filename -- Output filename
        threats -- ThreatGraphManager instance with collected findings
    """
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'ioc_value', 'ioc_type', 'device_id', 'hostname', 'os_version',
            'local_ip', 'external_ip', 'last_seen', 'vertex_id',
            'observation_timestamp', 'process_count', 'process_id',
            'edge_type', 'process_timestamp', 'image_file', 'command_line',
            'process_sha256', 'user_sid', 'start_time', 'raw_pid',
            'dns_query_count', 'dns_queries', 'ip_connection_count',
            'ip_connections', 'files_written_count', 'files_written'
        ]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for obs in threats.observations:
            base_row = {
                'ioc_value': obs.ioc_value,
                'ioc_type': obs.ioc_type,
                'device_id': obs.device_id,
                'hostname': obs.device_info.hostname if obs.device_info else 'N/A',
                'os_version': obs.device_info.os_version if obs.device_info else 'N/A',
                'local_ip': obs.device_info.local_ip if obs.device_info else 'N/A',
                'external_ip': obs.device_info.external_ip if obs.device_info else 'N/A',
                'last_seen': obs.device_info.last_seen if obs.device_info else 'N/A',
                'vertex_id': obs.vertex_id,
                'observation_timestamp': obs.timestamp,
                'process_count': len(obs.processes)
            }

            if obs.processes:
                for process in obs.processes:
                    row = base_row.copy()
                    row['process_id'] = process.get('process_id', '')
                    row['edge_type'] = process.get('edge_type', '')
                    row['process_timestamp'] = process.get('timestamp', '')

                    if process.get('details'):
                        d = process['details']
                        row['image_file'] = d.get('image_file', '')
                        row['command_line'] = d.get('command_line', '')
                        row['process_sha256'] = d.get('sha256', '')
                        row['user_sid'] = d.get('user_sid', '')
                        row['start_time'] = d.get('start_time', '')
                        row['raw_pid'] = d.get('raw_pid', '')

                        # Serialize complex fields
                        dns_queries = d.get('dns_queries', [])
                        row['dns_query_count'] = len(dns_queries)
                        row['dns_queries'] = '; '.join([q['domain'] for q in dns_queries])

                        ip_conns = d.get('ipv4_connections', [])
                        row['ip_connection_count'] = len(ip_conns)
                        row['ip_connections'] = '; '.join([f"{c['ip']}({c['direction']})" for c in ip_conns])

                        files = d.get('files_written', [])
                        row['files_written_count'] = len(files)
                        row['files_written'] = '; '.join([f['path'] for f in files])

                    writer.writerow(row)
            else:
                # Write row even if no processes
                writer.writerow(base_row)


def find_threats(args: Namespace, threat_graph: ThreatGraph, hosts: Hosts) -> None:
    """ThreatGraphManager handler for finding threats.

    Parameters:
        args -- ArgumentHandler for parsing arguments.
        threat_graph -- ThreatGraph API interface.
        hosts -- Hosts API interface.
    """
    indicators = STIXHandler(file_name=args.file)
    indicators.parse_file()

    threats = ThreatGraphManager(threat_graph=threat_graph, hosts=hosts, indicators=indicators)
    threats.get_all_vertex()
    threats.identify_all_hosts()
    threats.get_process_details()
    if args.output:
        export_findings(args, threats)
    else:
        threats.display_findings()

def main():
    """Start Main Execution Routine."""
    args = parse_command_line()
    threat_graph, hosts = connect_api(key=args.client_id, secret=args.client_secret, debug=args.debug)

    find_threats(args, threat_graph, hosts)

if __name__ == "__main__":
    main()
