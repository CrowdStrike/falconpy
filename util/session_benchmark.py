"""Local loopback benchmark demonstrating requests.Session connection reuse.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

Compares per-request latency for module-level requests.request() calls (FalconPy's
default, no-session behavior) against a shared requests.Session (FalconPy's behavior
when session= is provided), both against a local unencrypted loopback HTTP server.

DISCLAIMER: These numbers measure requests/urllib3 connection-reuse overhead on an
unencrypted loopback HTTP server. They do NOT reflect real network/TLS/API latency
to api.crowdstrike.com. They demonstrate the mechanism (avoided TCP/TLS handshakes
per request) that produces the improvement documented in the associated pull request;
absolute before/after numbers against the live API will vary with network conditions
and were not reproduced by this script.

Execute from the root of the repository: util/session_benchmark.py
"""
import http.server
import statistics
import threading
import time
import requests

REQUEST_COUNT = 100
SIMULATED_SERVER_LATENCY_SECONDS = 0.0


class _LatencyHandler(http.server.BaseHTTPRequestHandler):
    """HTTP/1.1 handler that simulates a small amount of server-side processing time."""

    protocol_version = "HTTP/1.1"

    def do_GET(self):  # noqa: N802  (stdlib naming convention)
        time.sleep(SIMULATED_SERVER_LATENCY_SECONDS)
        body = b"{}"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):  # noqa: A002  (stdlib signature)
        """Silence default request logging to keep benchmark output clean."""


def _start_server():
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _LatencyHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def _time_requests(count, request_callable, url):
    durations = []
    for _ in range(count):
        start = time.perf_counter()
        request_callable(url)
        durations.append((time.perf_counter() - start) * 1000)  # milliseconds
    return durations


def _report(label, durations):
    print(f"{label}:")
    print(f"  min:    {min(durations):.2f} ms")
    print(f"  median: {statistics.median(durations):.2f} ms")
    print(f"  mean:   {statistics.mean(durations):.2f} ms")
    quantiles = statistics.quantiles(durations, n=20)  # 5th percentile buckets
    print(f"  p95:    {quantiles[18]:.2f} ms")
    print()


def main():
    """Run the loopback benchmark and print a comparison report."""
    server, thread = _start_server()
    url = f"http://127.0.0.1:{server.server_port}"

    try:
        # Baseline: matches FalconPy's default (no session) behavior.
        no_session_durations = _time_requests(REQUEST_COUNT, lambda u: requests.request("GET", u), url)

        # With session: matches FalconPy's behavior when session= is provided.
        with requests.Session() as session:
            with_session_durations = _time_requests(REQUEST_COUNT, lambda u: session.request("GET", u), url)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    print(f"Local loopback benchmark ({REQUEST_COUNT} requests per condition)")
    print("=" * 60)
    _report("Without session (requests.request per call)", no_session_durations)
    _report("With session (requests.Session reused)", with_session_durations)

    speedup = statistics.mean(no_session_durations) / statistics.mean(with_session_durations)
    print(f"Mean speedup: {speedup:.2f}x")
    print()
    print(__doc__.split("DISCLAIMER:")[1].split("Execute from")[0].strip())


if __name__ == "__main__":
    main()
