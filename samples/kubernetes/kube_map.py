r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

         _  ___   _ ____  _____
        | |/ / | | | __ )| ____|
        | ' /| | | |  _ \|  _|
        | . \| |_| | |_) | |___
  __  __|_|\_\\___/|____/|_____|__ ____
 |  \/  |  / \  |  _ \|  _ \| ____|  _ \
 | |\/| | / _ \ | |_) | |_) |  _| | |_) |
 | |  | |/ ___ \|  __/|  __/| |___|  _ <
 |_|  |_/_/   \_\_|   |_|   |_____|_| \_\


This sample utilizes the KubernetesProtection sample to map out
your kubenetes assets. Kubernetes assets are found via the Falcon Sensor.

Creation date: 06.26.23 - alhumaw


"""


import logging
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime
from dataclasses import dataclass
from typing import Dict
try:
    from termcolor import colored # type: ignore
except ImportError as no_termcolor:
    raise SystemExit("The termcolor library must be installed.\n"
                     "Install it with `python3 -m pip install termcolor"
                     ) from no_termcolor
try:
    from tabulate import tabulate # type: ignore
except ImportError as no_tabulate:
    raise SystemExit("The tabulate library must be installed.\n"
                     "Install it with `python3 -m pip install tabulate`."
                     ) from no_tabulate
try:
    from falconpy import KubernetesProtection, APIError, RealTimeResponseAdmin, Hosts
except ImportError as no_falconpy:
    raise SystemExit("The CrowdStrike FalconPy library must be installed.\n"
                     "Install it with `python3 -m pip install crowdstrike-falconpy`."
                     ) from no_falconpy


def parse_command_line() -> Namespace:
    """Parse any provided command line arguments and return the namespace."""
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter
                            )
    require = parser.add_argument_group("required arguments")
    require.add_argument("-k", "--client_id",
                         required=True,
                         help="CrowdStrike API client ID"
                         )
    require.add_argument("-s", "--client_secret",
                         required=True,
                         help="CrowdStrike API client secret"
                         )
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-c", "--cluster_id",
                        help="Display cluster and it's nodes/pods"
                        )

    parsed = parser.parse_args()

    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)

    return parsed


@dataclass
class Cluster:
    """Kubernetes cluster dataclass"""
    cluster_id: str
    cluster_name: str
    version: str
    cloud_type: str
    node_count: int


@dataclass
class Node:
    """Kubernetes nodes dataclass"""
    node_id: str
    node_name: str
    parent_cluster_id: str
    ip: str
    architecture: str
    operating_system: str
    cpu: str
    storage: str
    pod_count: int


@dataclass
class Pod:
    """Kubernetes pods dataclass"""
    pod_id: str
    pod_name: str
    parent_node_name: str
    containers: list
    namespace: str
    container_count: int


class KubernetesEnvironment:
    """Kubernetes comprehensive environment"""
    def __init__(self):
        self.clusters: list[Cluster] = []
        self.nodes: list[Node] = []
        self.pods: list[Pod] = []

    def add_clusters(self, cluster: Cluster) -> None:
        """Appends cluster to list of clusters"""
        self.clusters = cluster

    def add_nodes(self, node: Node) -> None:
        """Appends node to list of nodes"""
        self.nodes = node

    def add_pods(self, pod: Pod) -> None:
        """Appends pod to list of pods"""
        self.pods = pod


def generate_clusters(falcon: KubernetesProtection) -> list:
    """Retrieves and returns a list of clusters"""
    limit = 100
    total = 1
    offset = 0
    all_resp = []
    clusters = []
    while len(all_resp) < total:
        resp = falcon.ReadClusterCombined(limit=limit, offset=offset)['body']['resources']
        if resp['status_code'] == 200:
            page = resp['body']['meta']['pagination']
            total = page['total']
            offset += 100
            all_resp.extend(resp['body']['resources'])
            print(resp['body']['meta'])
            print(len(all_resp))
        else:
            total = 0
            errors = resp['body']['resources']
            for err in errors:
                ecode = err['code']
                emsg = err['message']
                print(f"[{ecode}] {emsg}")
    
    for batch in all_resp:
        new_cluster = Cluster(
            cluster_id=batch.get('cluster_id'),
            cluster_name=batch.get('cluster_name'),
            version=batch.get('kubernetes_version'),
            cloud_type=batch.get('cloud_name'),
            node_count=batch.get('node_count')
        )
        clusters.append(new_cluster)
    return clusters


def generate_nodes(falcon: KubernetesProtection) -> list:
    """Retrieves and returns a list of nodes"""
    total = falcon.ReadNodeCombined()['body']['meta']['pagination']['total']
    all_resp = concurent_response(falcon, 'ReadNodeCombined', total)
    nodes = []
    print(total)
    print(len(all_resp))
    for batch in all_resp:
        new_node = Node(
            node_id=batch.get('node_id'),
            node_name=batch.get('node_name'),
            parent_cluster_id=batch.get('cluster_id'),
            ip=batch.get('ipv4'),
            architecture=batch.get('architecture'),
            operating_system=batch.get('operating_system'),
            cpu=batch.get('cpu'),
            storage=batch.get('storage'),
            pod_count=int(batch.get('pod_count'))
        )
        nodes.append(new_node)
    return nodes


def generate_pods(falcon: KubernetesProtection) -> list:
    """Retrieves and returns a list of pods"""
    pods = []
    total = falcon.ReadPodCombined()['body']['meta']['pagination']['total']
    all_resp = concurent_response(falcon, 'ReadPodCombined', total)
    print(total)
    print(len(all_resp))
    for batch in all_resp:
        new_pod = Pod(
            pod_id=batch.get('pod_id'),
            pod_name=batch.get('pod_name'),
            parent_node_name=batch.get('node_name'),
            containers=[],
            namespace=batch.get('namespace'),
            container_count=batch.get('countainer_count')
        )
        container_list = batch.get('containers')
        if container_list:
            for container in container_list:
                new_pod.containers.append(container.get('name'))
        pods.append(new_pod)

    return pods


def response_processing(falcon: KubernetesProtection, endpoint: str, filt: str, limit: int, offset: int) -> list:
    """Dynamic API caller for multi-proccessing"""
    method = getattr(falcon, endpoint, None)
    print("worker generated")
    if method is None:
        raise AttributeError(f"API object has no method named '{endpoint}'")
    if filt:
        resp = method(filter=filt, limit=limit, offset=offset)['body']['resources']
    else:
        resp = method(limit=limit, offset=offset)['body']['resources']
    return resp


def concurent_response(falcon: KubernetesProtection, endpoint: str, total: str, filt=None) -> list:
    """Utilizes current futures to asynchronously handle paginated API calls at once"""
    chunk_size = 200
    workers = int(total / chunk_size) + 1
    offsets = [i * chunk_size for i in range(workers)]
    print(offsets)
    all_resp = []
    with ThreadPoolExecutor(max_workers=workers) as e:
        future = {
            e.submit(response_processing, falcon, endpoint, filt, chunk_size, offset)
            for offset in offsets
        }
    for f in future:
        all_resp.extend(f.result())
    return all_resp


def generate_containers(falcon: KubernetesProtection) -> list:
    """Retrieves and returns a list of RUNNING containers"""
    running_containers = {}
    filt = "running_status:'true'"
    total = falcon.ReadContainerCombined()['body']['meta']['pagination']['total']

    all_resp = concurent_response(falcon, "ReadContainerCombined", filt, total)
    for container in all_resp:
        container_id = container.get('container_id')
        container_name = container.get('container_name')
        running_containers[container_id] = container_name
    return running_containers.keys()


def aggregate_kube(clusters: list, nodes: list, pods: list) -> KubernetesEnvironment:
    """Organizes clusters, nodes, and pods into a data structure"""
    kube = KubernetesEnvironment()
    kube.add_clusters(clusters)
    kube.add_nodes(nodes)
    kube.add_pods(pods)

    return kube


def connect_api(key: str, secret: str, debug: bool) -> KubernetesProtection:
    """Connects and returns an instance of the Uber class."""
    try:
        if debug:
            logging.basicConfig(level=logging.DEBUG)
        return KubernetesProtection(client_id=key, client_secret=secret, debug=debug)
    except APIError as e:
        print(f"Failed to connect to API: {e}")
        return e


def main():
    """Start Main Execution Routine"""
    args = parse_command_line()
    falcon = connect_api(key=args.client_id, secret=args.client_secret, debug=args.debug)
    #clusters = generate_clusters(falcon)
    #nodes = generate_nodes(falcon)
    #pods = generate_pods(falcon)
    #kube = aggregate_kube(clusters, nodes, pods)
    generate_nodes(falcon)


if __name__ == "__main__":
    main()
