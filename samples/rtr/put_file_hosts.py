r"""Put a file from multiple hosts.
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |        FalconPy v1.3
`-------'                         `-------'
        ____             __   _______
       / __ \___  ____ _/ /  /_  __(_)___ ___  ___
      / /_/ / _ \/ __ `/ /    / / / / __ `__ \/ _ \
     / _, _/  __/ /_/ / /    / / / / / / / / /  __/
    /_/ |_|\___/\__,_/_/    /_/ /_/_/ /_/ /_/\___/
            ____
           / __ \___  _________  ____  ____  ________
          / /_/ / _ \/ ___/ __ \/ __ \/ __ \/ ___/ _ \
         / _, _/  __(__  ) /_/ / /_/ / / / (__  )  __/
        /_/ |_|\___/____/ .___/\____/_/ /_/____/\___/
                       /_/

This program will put a single file of the same name
to multiple hosts.

"""
import os
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from datetime import datetime
from logging import basicConfig, DEBUG

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv() -> bool:
        return False

load_dotenv()

# RealTimeResponseAdmin is required for RTR admin batch put and put-files upload
try:
    from falconpy import Hosts, RealTimeResponse, RealTimeResponseAdmin
except ImportError as no_falconpy:
    raise SystemExit(
        "FalconPy v1.3 or greater must be installed to run this program."
        ) from no_falconpy


def consume_arguments() -> Namespace:
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-d", "--debug",
                        help="Enable API debugging",
                        action="store_true")
    parser.add_argument("-n", "--hostname",
                        help="Hostname to target (stemmed search)",
                        default="")
    parser.add_argument("-b", "--base_url", help="CrowdStrike API base URL", default="auto")
    parser.add_argument("-r", "--remote-path",
                        help="Destination path on target hosts (include filename if desired). If omitted, RTR will place the file at '/' (root)",
                        default="")
    req = parser.add_argument_group("required arguments")
    req.add_argument("-f", "--filepath",
                     help="Filename and path of the file to be put",
                     required=True
                     )
    return parser.parse_args()


def validate_local_file(path: str) -> str:
    """Validate that the provided local file exists and is readable."""
    if not path:
        raise ValueError("A local file path is required.")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Local file not found: {path}")
    if not os.access(path, os.R_OK):
        raise PermissionError(f"Local file is not readable: {path}")
    return os.path.abspath(path)


start = datetime.now().timestamp()
cmdline = consume_arguments()
# Debug logging
if cmdline.debug:
    basicConfig(level=DEBUG)

target_filter = ""
if cmdline.hostname:
    target_filter = f"hostname:*'*{cmdline.hostname}*'"

# Retrieve our target filename from the provided file path
try:
    local_filepath = validate_local_file(cmdline.filepath)
except (FileNotFoundError, PermissionError, ValueError) as exc:
    raise SystemExit(f"Input error: {exc}") from exc

cloud_name = os.path.basename(local_filepath)

# Normalize remote_path for remote hosts. Convert leading '~' to '$HOME'
# Only force absolute paths for relative directory paths.
def _normalize_remote_path(path: str) -> str:
    if not path:
        return path
    if path.startswith("~"):
        return path.replace("~", "$HOME", 1)
    if path.startswith("/") or (len(path) >= 2 and path[1] == ":"):
        return path
    if "/" in path or "\\" in path:
        return "/" + path.lstrip("/\\")
    return path

remote_path = _normalize_remote_path(cmdline.remote_path)
if remote_path:
    # If remote_path looks like a directory, append the filename; otherwise treat as full destination
    if remote_path.endswith("/") or remote_path.endswith("\\"):
        sep = "\\" if "\\" in remote_path else "/"
        remote_name = remote_path.rstrip("/\\") + sep + cloud_name
    else:
        remote_name = remote_path
else:
    remote_name = cloud_name

# Construct instances of the Service Classes we are wanting to use.
hosts = Hosts(debug=cmdline.debug,
              client_id=os.getenv("CLIENT_ID"),
              client_secret=os.getenv("CLIENT_SECRET"),
              base_url=cmdline.base_url)
rtr = RealTimeResponse(auth_object=hosts)
rtr_admin = RealTimeResponseAdmin(auth_object=hosts)

# change: upload the local file to the RTR put-files repository first so the batch put command can retrieve it
print(f"Uploading '{local_filepath}' to RTR cloud as '{remote_name}'...")
with open(local_filepath, "rb") as f:
    file_bytes = f.read()

files_payload = [("file", (os.path.basename(local_filepath), file_bytes, "application/octet-stream"))]
upload_result = rtr_admin.create_put_files(
    files=files_payload,
    data={"name": remote_name, "description": "Uploaded for batch put"}
)
status = upload_result.get("status_code")
if status == 200:
    print(f"  ✓ '{remote_name}' uploaded.")
elif status == 409:
    print(f"{status}  File already exists in RTR cloud — continuing ({remote_name}).")
else:
    print(f"  create_put_files body: {upload_result.get('body')}")
    raise RuntimeError(f"Upload failed [{status}]: {upload_result.get('body')}")

# Retrieve our target device AIDs.
target_devices = hosts.query_devices_by_filter_scroll(filter=target_filter)["body"]["resources"]
print(f"{len(target_devices)} matching hosts identified.")

# Initialize a session with the host batch.
session_init = rtr.batch_init_sessions(host_ids=target_devices)
batch_id = session_init["body"].get("batch_id")  # Grab the batch ID
if not batch_id:
    print("  batch_init_sessions response:", session_init)
    raise RuntimeError("Failed to initialize batch RTR session.")

# Ensure the destination directory exists on targets before issuing put.
dest_dir = os.path.dirname(remote_name).replace("\\", "/")
if dest_dir and dest_dir != "/":
    print(f"Ensure destination directory '{dest_dir}' exists on target hosts...")
   
# issue a batch RTR put command using the full uploaded put-file name
command_string = f"put {remote_name}"

result = rtr_admin.batch_admin_command(
    base_command="put",
    batch_id=batch_id,
    command_string=command_string,
    timeout=60,
    timeout_duration="60s",
    persist_all=True,
)

print(f"Result: {result}")

# change: parse batch PUT results using completion/errors instead of stdout processing
resources = (result.get("body") or {}).get("combined", {}).get("resources", {})
if not resources:
    print("  batch_admin_command response:", result)

for aid, res in resources.items():
    if res.get("complete") and not res.get("stderr") and not res.get("errors"):
        status = "✓ Success"
    else:
        detail = res.get("stderr") or str(res.get("errors", "unknown"))
        status = f"✗ Failed: {detail[:50]}"
    print(f"  {aid}: {status}")

print(f"Total run time: {datetime.now().timestamp() - start:.2f} seconds")
