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
from operator import itemgetter
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

KUBE = r"""

                                           ....
                                       .-========-.
                                   .-================-.
                              .:-========================-:.
                          .:-================================-:.
                      .:-===================+====================-:.
                  .:-======================: .-======================-:.
              .-===========================    ===========================-.
           :==============================+:  :+==============================:
          =================================:  :=================================
         -============================+==--    --==+============================-
         ==========================-:.              .:-==========================
        :==========:  .-========:.                      .:========-.  :==========:
        ============.   .-=+=-       .::--:    :--:..      .-=+=-.   .============
       :==============-:          :-======:    :====+=-.          :-==============:
       ==================       :=========:    :=========:       =================-
      .=================-        .:======+.    .+======:.        -=================.
      =================-     :      .-=+==.    .==+=-.      :     -=================
     :=================     ===:       .:.      .:.       :===     =================:
     ================+:    -=====-                      -=====:    :+================
    .=================     ========-        ..       .-========     =================.
    -=================    .=========:     :====:     :=+=======.    =================-
    ==================    :===-::..       ======        .::-==+:    ==================
   -==================                    .-==-.                    ==================-
   =============----:               .               ..               ::---=============
  :==========-              ::--===+++-            -+=+===---:              -==========:
  ============:::-==+==.    :+========      ..      ========+:    .==+==-:::============
  -=====================     :=======      ====      =======:     =====================-
   -=====================.    .=====.     ======     .=====.    .=====================-
    .====================+-     .:=:     ========     :=-.     -+====================.
      :=====================:          .==========.          :=====================:
        -=====================:         .:::--:::.         :=====================-
         :=======================                        -======================:
           -===================+-   --:..        ..:--   -+===================-
            .=================+:   ======++====++======   :==================.
              :===============.   -====================-   .===============:
                -=============.  :+=====================:  .=============-
                 :============+=+========================+=+============:
                  .-==================================================-.
                    .================================================.
                      :============================================:
                       .==========================================.
                          .::::::::::::::::::::::::::::::::::::.
"""


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
    exclusive_group = parser.add_mutually_exclusive_group()
    exclusive_group.add_argument("-c", "--cluster",
                                 help="Display clusters and it's nodes",
                                 action="store_true",
                                 default=False
                                 )
    exclusive_group.add_argument("-n", "--node",
                                 help="Display nodes and it's pods",
                                 action="store_true",
                                 default=False
                                 )
    exclusive_group.add_argument("-nn", "--node_name",
                                 help="Display pods connected to a specific node"
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
    """Kubernetes cluster dataclass."""

    cluster_id: str
    cluster_name: str
    agent: str
    cloud_type: str
    node_count: int


@dataclass
class Node:
    """Kubernetes nodes dataclass."""

    node_name: str
    parent_cluster_name: str
    ip: str
    architecture: str
    cpu: str
    storage: str
    pod_count: int


@dataclass
class Pod:
    """Kubernetes pods dataclass."""

    pod_id: str
    pod_name: str
    parent_node_name: str
    containers: list
    namespace: str
    container_count: int


class KubernetesEnvironment:
    """Kubernetes comprehensive environment."""

    def __init__(self):
        self.clusters: list[Cluster] = []
        self.nodes: list[Node] = []
        self.pods: list[Pod] = []

    def add_clusters(self, cluster: Cluster) -> None:
        """Append cluster to list of clusters."""
        self.clusters = cluster

    def add_nodes(self, node: Node) -> None:
        """Append node to list of nodes."""
        self.nodes = node

    def add_pods(self, pod: Pod) -> None:
        """Append pod to list of pods."""
        self.pods = pod


def generate_clusters(falcon: KubernetesProtection, thread: bool) -> list:
    """Retrieve and return a list of clusters."""
    print("Locating Clusters...")
    if thread:
        print("Threading....")
        total = falcon.ReadClusterCombined()['body']['meta']['pagination']['total']
        all_resp = concurent_response(falcon, 'ReadClusterCombined', total)
    else:
        all_resp = normal_response(falcon, "ReadClusterCombined")
    clusters = []
    for batch in all_resp:
        new_cluster = Cluster(
            cluster_id=batch['cluster_id'],
            cluster_name=batch['cluster_name'],
            agent=batch['agent_status'],
            cloud_type=batch['cloud_name'],
            node_count=batch['node_count']
        )
        clusters.append(new_cluster)

    return clusters


def generate_nodes(falcon: KubernetesProtection, thread: bool) -> list:
    """Retrieve and return a list of nodes."""
    print("Discovering Nodes...")
    if thread:
        print("Threading....")
        total = falcon.ReadNodeCombined()['body']['meta']['pagination']['total']
        all_resp = concurent_response(falcon, 'ReadNodeCombined', total)
    else:
        all_resp = normal_response(falcon, "ReadNodeCombined")
    nodes = []
    real_cpu = ""
    for batch in all_resp:
        new_node = Node(
            node_name=batch['node_name'],
            parent_cluster_name=batch['cluster_name'],
            ip=batch['ipv4'],
            architecture=batch['architecture'],
            cpu=batch['cpu'],
            storage=batch['storage'],
            pod_count=(batch['pod_count'])
        )
        if len(new_node.cpu) > 0:
            cpu_set = new_node.cpu.split("/")
            real_cpu = f"{cpu_set[1]}/{cpu_set[0]}"
            new_node.cpu = real_cpu
        nodes.append(new_node)

    return nodes


def generate_pods(falcon: KubernetesProtection, thread: bool) -> list:
    """Retrieve and return a list of pods."""
    print("Finding Pods...")
    if thread:
        total = falcon.ReadPodCombined()['body']['meta']['pagination']['total']
        print("Threading....")
        all_resp = concurent_response(falcon, 'ReadPodCombined', total, filt="container_count:>'0'")
    else:
        all_resp = normal_response(falcon, "ReadPodCombined")
    pods = []
    for batch in all_resp:
        new_pod = Pod(
            pod_id=batch['pod_id'],
            pod_name=batch['pod_name'],
            parent_node_name=batch['node_name'],
            containers=[],
            namespace=batch['namespace'],
            container_count=batch['container_count']
        )
        container_list = batch['containers']
        if container_list:
            for container in container_list:
                new_pod.containers.append(container['id'])
        pods.append(new_pod)

    return pods


def find_active_pods(pods: list[Pod], containers: dict) -> list:
    """Cross-references running containers to find active pods."""
    active_pods = []
    for pod in pods:
        has_match = False
        for container in pod.containers:
            if container in containers:
                has_match = True
                break
        if has_match:
            active_pods.append(pod)

    return active_pods


def generate_containers(falcon: KubernetesProtection, thread: bool) -> dict:
    """Retrieve and return a list of RUNNING containers."""
    print("Tracking Down Containers...")
    running_containers = {}
    filt = "running_status:'true'"
    if thread:
        total = falcon.ReadContainerCombined(filter=filt)['body']['meta']['pagination']['total']
        all_resp = concurent_response(falcon, "ReadContainerCombined", total, filt)
    else:
        all_resp = normal_response(falcon, "ReadContainerCombined", filt)
    for container in all_resp:
        container_id = container.get('container_id')
        container_name = container.get('container_name')
        running_containers[container_id] = container_name

    return running_containers


def response_processing(falcon: KubernetesProtection,
                        endpoint: str, filt: str,
                        limit: int, offset: int) -> list:
    """Dynamic API caller for multi-proccessing."""
    method = getattr(falcon, endpoint, None)
    if method is None:
        raise AttributeError(f"API object has no method named '{endpoint}'")
    if filt:
        resp = method(filter=filt if filt else None,
                      limit=limit,
                      offset=offset)['body']['resources']
    else:
        resp = method(limit=limit, offset=offset)['body']['resources']

    return resp


def normal_response(falcon: KubernetesProtection, endpoint: str, filt=None) -> list:
    """Caller to handle pagination."""
    limit = 200
    all_resp = []
    total = 1
    offset = 0
    method = getattr(falcon, endpoint, None)
    if method is None:
        raise AttributeError(f"API object has no method named '{endpoint}'")

    while len(all_resp) < total:
        resp = method(limit=limit, offset=offset, filter=filt)
        if resp['status_code'] == 200:
            total = resp['body']['meta']['pagination']['total']
            offset += 200
            all_resp.extend(resp['body']['resources'])

    return all_resp


def concurent_response(falcon: KubernetesProtection, endpoint: str, total: str, filt=None) -> list:
    """Utilizes concurrent futures to asynchronously handle paginated API calls at once."""
    chunk_size = 200
    # Determine how many workers are needed to handle all chunks at once
    workers = int(total / chunk_size) + 1
    # Create a list of chunks of the total, incremented by the max limit (chunk_size)
    # (range(0,total), each list index is incremented by 200)
    offsets = [i * chunk_size for i in range(workers)]
    all_resp = []
    if workers > 10:
        # Splits the list into batches of 10 to distribute load
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


def aggregate_kube(clusters: list, nodes: list, pods=None) -> KubernetesEnvironment:
    """Organizes clusters, nodes, and pods into a data structure."""
    kube = KubernetesEnvironment()
    kube.add_clusters(clusters)
    kube.add_nodes(nodes)
    if pods:
        kube.add_pods(pods)

    return kube


def connect_api(key: str, secret: str, debug: bool) -> KubernetesProtection:
    """Connect and return an instance of the Uber class."""
    try:
        if debug:
            logging.basicConfig(level=logging.DEBUG)
        return KubernetesProtection(client_id=key, client_secret=secret, debug=debug)
    except APIError as e:
        print(f"Failed to connect to API: {e}")
        return e


def form_relations(kube: KubernetesEnvironment, args: Namespace) -> dict:
    """Return a tabulated kubernetes environment."""
    if args.cluster:
        cluster_data = []
        for cluster in kube.clusters:
            for node in kube.nodes:
                if node.parent_cluster_name == cluster.cluster_name:
                    cluster.node_count += 1
            cluster_data.append([
                cluster.cluster_name if cluster.cluster_name else cluster.cluster_id,
                cluster.agent,
                cluster.cloud_type,
                cluster.node_count
            ])
        headers = ['Cluster Name || ID', 'KPA Status', 'Cloud Type', 'Node Count']
        # Sort by node count
        cluster_data.sort(key=itemgetter(3))

        return tabulate(cluster_data, headers, tablefmt='grid')

    if args.node:
        node_data = []
        for node in kube.nodes:
            for pod in kube.pods:
                if pod.parent_node_name == node.node_name:
                    node.pod_count += 1
            node_data.append([
                node.node_name,
                node.ip,
                node.architecture,
                node.cpu,
                node.storage,
                node.pod_count
            ])
        headers = ['Node Name', 'IP', 'Arch', 'CPU', 'Storage', 'Active\nPod Count']
        # Sort by pod count
        node_data.sort(key=itemgetter(5))

        return tabulate(node_data, headers, tablefmt='grid')

    pod_data = []
    for pod in kube.pods:
        if pod.parent_node_name == args.node_name:
            pod_data.append([
                pod.pod_id,
                pod.pod_name,
                pod.namespace,
                pod.container_count
            ])
    headers = ['Pod ID', 'Pod Name', 'Namespace', 'Container Count']
    if len(pod_data) < 1:
        return f"Found 0 pods related to '{args.node_name}'"

    return tabulate(pod_data, headers, tablefmt='grid')


def find_asset_count(falcon: KubernetesProtection) -> dict:
    """Find and output the initial count of all assets."""
    env = {}
    containers = colored(falcon.ReadContainerCount(
        filter="running_status: 'true'")['body']['resources'][0]['count'], 'red')

    pods = colored(falcon.ReadPodCount()['body']['resources'][0]['count'], 'red')
    nodes = colored(falcon.ReadNodeCount()['body']['resources'][0]['count'], 'red')
    clusters = colored(falcon.ReadClusterCount()['body']['resources'][0]['count'], 'red')
    env = {
        'Asset': [colored('Clusters', "yellow"),
                  colored('Nodes', "blue"),
                  colored('Pods', 'green'),
                  'Containers'],
        'Count': [clusters, nodes, pods, containers]
    }

    return (tabulate(env, headers="keys", tablefmt='heavy_grid', colalign=("left", "left")))


def print_kube(args: Namespace, falcon: KubernetesProtection) -> None:
    """Print the kubernetes environment to the terminal."""
    if args.cluster or args.node or args.node_name:
        clusters = generate_clusters(falcon, args.thread)
        nodes = generate_nodes(falcon, args.thread)

        if args.node or args.node_name:
            # Compare all pods against active containers to find active pods
            pods = generate_pods(falcon, args.thread)
            containers = generate_containers(falcon, args.thread)
            active_pods = find_active_pods(pods, containers)
            # Creates kube instance, prints out table
            kube = aggregate_kube(clusters, nodes, active_pods)
            kube_table = form_relations(kube, args)
            print(kube_table)

        else:
            kube = aggregate_kube(clusters, nodes)
            kube_table = form_relations(kube, args)
            print(kube_table)

    else:
        print(KUBE)
        print(find_asset_count(falcon))
        cluster_info = f"Use {colored('-c', 'yellow')} to print cluster information"
        node_info = f"Use {colored('-n', 'blue')} to print node information"
        pod_info = (f"Use {colored('-nn', 'green')}"
                    " with a node name to print\nactive pods linked to that node")
        hint = (f"HINT: use {colored('-t', 'magenta')}"
                " along with any command to\nimprove speed using asynchronous processing")
        print(tabulate([[cluster_info], [node_info], [pod_info], [hint]], tablefmt="mixed_grid"))


def main():
    """Start Main Execution Routine."""
    args = parse_command_line()
    falcon = connect_api(key=args.client_id, secret=args.client_secret, debug=args.debug)
    print_kube(args, falcon)


if __name__ == "__main__":
    main()
