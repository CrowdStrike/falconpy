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
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
try:
    from termcolor import colored  # type: ignore
except ImportError as no_termcolor:
    raise SystemExit("The termcolor library must be installed.\n"
                     "Install it with `python3 -m pip install termcolor"
                     ) from no_termcolor
try:
    from tabulate import tabulate  # type: ignore
except ImportError as no_tabulate:
    raise SystemExit("The tabulate library must be installed.\n"
                     "Install it with `python3 -m pip install tabulate`."
                     ) from no_tabulate
try:
    from falconpy import KubernetesProtection, APIError
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
    parser.add_argument("-c", "--cluster",
                        help="Display clusters and it's nodes",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-n", "--node",
                        help="Display nodes and it's pods",
                        action="store_true",
                        default=False
                        )
    parser.add_argument("-p", "--pod_id",
                        help="Display specific pod information"
                        )
    parser.add_argument("-t", "--thread",
                        help="Enables asynchronous API calls for faster returns",
                        action="store_true",
                        default=False
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
    parent_cluster_name: str
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


def generate_clusters(falcon: KubernetesProtection, thread: bool) -> list:
    """Retrieves and returns a list of clusters"""
    print("Locating Clusters...")
    if thread:
        total = falcon.ReadClusterCombined()['body']['meta']['pagination']['total']
        all_resp = concurent_response(falcon, 'ReadClusterCombined', total)
    else:
        all_resp = normal_response(falcon, "ReadClusterCombined")
    clusters = []
    for batch in all_resp:
        new_cluster = Cluster(
            cluster_id=batch['cluster_id'],
            cluster_name=batch['cluster_name'],
            version=batch['kubernetes_version'],
            cloud_type=batch['cloud_name'],
            node_count=batch['node_count']
        )
        clusters.append(new_cluster)
    return clusters


def generate_nodes(falcon: KubernetesProtection, thread: bool) -> list:
    """Retrieves and returns a list of nodes"""
    print("Discovering Nodes...")
    if thread:
        total = falcon.ReadNodeCombined()['body']['meta']['pagination']['total']
        all_resp = concurent_response(falcon, 'ReadNodeCombined', total)
    else:
        all_resp = normal_response(falcon, "ReadNodeCombined")
    nodes = []
    for batch in all_resp:
        new_node = Node(
            node_id=batch['node_id'],
            node_name=batch['node_name'],
            parent_cluster_name=batch['cluster_name'],
            ip=batch['ipv4'],
            architecture=batch['architecture'],
            operating_system=batch['os'],
            cpu=batch['cpu'],
            storage=batch['storage'],
            pod_count=(batch['pod_count'])
        )
        nodes.append(new_node)
    return nodes


def generate_pods(falcon: KubernetesProtection, thread: bool) -> list:
    """Retrieves and returns a list of pods"""
    print("Finding Pods...")
    if thread:
        total = falcon.ReadPodCombined()['body']['meta']['pagination']['total']
        all_resp = concurent_response(falcon, 'ReadPodCombined', total)
    else:
        all_resp = normal_response(falcon, "ReadPodCombined")
    pods = []
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
    if method is None:
        raise AttributeError(f"API object has no method named '{endpoint}'")
    if filt:
        resp = method(filter=filt, limit=limit, offset=offset)['body']['resources']
    else:
        resp = method(limit=limit, offset=offset)['body']['resources']
    return resp


def normal_response(falcon: KubernetesProtection, endpoint: str, filt=None):
    """Normal API caller"""
    limit = 200
    all_resp = []
    total = 1
    offset = 0
    method = getattr(falcon, endpoint, None)
    if method is None:
        raise AttributeError(f"API object has no method named '{endpoint}'")

    while len(all_resp) < total:
        resp = method(limit=limit, offset=offset, filt=(filt if filt else None))
        if resp['status_code'] == 200:
            total = resp['body']['meta']['pagination']['total']
            offset += 200
            all_resp.extend(resp['body']['resources'])

    return all_resp


def concurent_response(falcon: KubernetesProtection, endpoint: str, total: str, filt=None) -> list:
    """Utilizes concurrent futures to asynchronously handle paginated API calls at once"""
    chunk_size = 200
    workers = int(total / chunk_size) + 1
    offsets = [i * chunk_size for i in range(workers)]
    all_resp = []
    if workers > 10:
        batches = [offsets[x: x + 10] for x in range(0, len(offsets), 10)]
        for batch in batches:
            with ThreadPoolExecutor(max_workers=workers) as e:
                future = {
                    e.submit(response_processing, falcon, endpoint, filt, chunk_size, offset)
                    for offset in batch
                }
            for f in future:
                all_resp.extend(f.result())
    else:
        with ThreadPoolExecutor(max_workers=workers) as e:
            future = {
                e.submit(response_processing, falcon, endpoint, filt, chunk_size, offset)
                for offset in offsets
            }
        for f in future:
            all_resp.extend(f.result())

    return all_resp


def generate_containers(falcon: KubernetesProtection, thread: bool) -> list:
    """Retrieves and returns a list of RUNNING containers"""
    print("Generating Containers...")
    running_containers = {}
    filt = "running_status:'true'"
    if thread:
        total = falcon.ReadContainerCombined()['body']['meta']['pagination']['total']
        all_resp = concurent_response(falcon, "ReadContainerCombined", filt, total)
    else:
        all_resp = normal_response(falcon, "ReadContainerCombined", filt)
    for container in all_resp:
        container_id = container.get('container_id')
        container_name = container.get('container_name')
        running_containers[container_id] = container_name
    return running_containers.keys()


def aggregate_kube(clusters: list, nodes: list, pods=None) -> KubernetesEnvironment:
    """Organizes clusters, nodes, and pods into a data structure"""
    kube = KubernetesEnvironment()
    kube.add_clusters(clusters)
    kube.add_nodes(nodes)
    if pods:
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


def form_relations(kube: KubernetesEnvironment, args: Namespace) -> dict:
    """Prints out the kubernetes environment"""
    cluster_groups = {}
    node_groups = {}
    node_list = []
    if args.cluster:
        for cluster in kube.clusters:
            cluster_groups[cluster.cluster_name] = {
                'cluster id': cluster.cluster_id,
                'cluster name': cluster.cluster_name,
                'version': cluster.version,
                'cloud type': cluster.cloud_type,
                'connected nodes': cluster.node_count
            }
            if cluster.node_count > 0:
                cluster_groups[cluster.cluster_name]['nodes'] = []
                for node in kube.nodes:
                    if node.parent_cluster_name == cluster.cluster_name:
                        cluster_groups[cluster.cluster_name]['nodes'].append(node.node_id)
        return cluster_groups
    if args.node:
        for node in kube.nodes:
            node_groups[node.node_name] = {
                'node id': node.node_id,
                'node name': node.node_name,
                'ip': node.ip,
                'architecture': node.architecture,
                'operating system': node.operating_system,
                'cpu': node.cpu,
                'storage': node.storage,
                'pod count': node.pod_count
            }
            node_groups[node.node_name]['pods'] = []
            node_list.append(node_groups[node.node_name])
            #for pod in kube.pods:
            #    if pod.parent_node_name == node.node_name:
            #        node_groups[node.node_name]['pods'].append(pod.pod_id)
        for node in node_list:
            print(node['node name'])

        # print(tabulate([[node_groups[node.node_name]['node id']]], headers=['node id']))
        return node_groups


def find_asset_count(falcon: KubernetesProtection) -> dict:
    """Find and output the initial count of all assets"""
    env = {}
    containers = colored(falcon.ReadContainerCount(filter="running_status: 'true'")['body']['resources'][0]['count'], 'red')
    pods = colored(falcon.ReadPodCount()['body']['resources'][0]['count'], 'red')
    nodes = colored(falcon.ReadNodeCount()['body']['resources'][0]['count'], 'red')
    clusters = colored(falcon.ReadClusterCount()['body']['resources'][0]['count'], 'red')
    env = {
        'Asset': [colored('Clusters', "yellow"), colored('Nodes', "blue"), 'Pods', 'Containers'],
        'Count': [clusters, nodes, pods, containers]

    }

    return (tabulate(env, headers="keys", tablefmt='heavy_grid', colalign=("left", "left")))


def main():
    """Start Main Execution Routine"""
    args = parse_command_line()
    falcon = connect_api(key=args.client_id, secret=args.client_secret, debug=args.debug)
    if args.cluster or args.node:
        clusters = generate_clusters(falcon, args.thread)
        nodes = generate_nodes(falcon, args.thread)
        if args.node:
            pods = generate_pods(falcon, args.thread)
            kube = aggregate_kube(clusters, nodes, pods)
            kube_dictionary = form_relations(kube, args)
        else:
            kube = aggregate_kube(clusters, nodes)
            kube_dictionary = form_relations(kube, args)
            print(kube_dictionary)
        print("DONE")
    else:
        print(find_asset_count(falcon))
        cluster_info = f"Use {colored("-c", "yellow")} to print cluster information"
        node_info = f"Use {colored("-n", "blue")} to print node information"
        print(tabulate([[cluster_info], [node_info]], tablefmt="mixed_grid"))


if __name__ == "__main__":
    main()
