# test_session_connection_reuse.py
# Local-only demonstration of HTTP/1.1 connection reuse via requests.Session.
#
# No credentials and no internet access are required: this spins up a loopback
# HTTP server and shows that a shared requests.Session reuses one TCP connection
# across multiple requests, while separate module-level requests.get() calls do not.
import http.server
import threading
import requests
import pytest


class _CountingHandler(http.server.BaseHTTPRequestHandler):
    """HTTP/1.1 handler that counts distinct accepted TCP connections."""

    protocol_version = "HTTP/1.1"

    def setup(self):
        super().setup()
        # A new connection is only ever set up once per TCP socket, even
        # when HTTP/1.1 keep-alive pipelines multiple requests over it.
        self.server.connection_count += 1

    def do_GET(self):  # noqa: N802  (stdlib naming convention)
        body = b"{}"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):  # noqa: A002  (stdlib signature)
        """Silence default request logging to keep test output clean."""


@pytest.fixture
def local_http_server():
    """Start a threaded loopback HTTP/1.1 server on an ephemeral port."""
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _CountingHandler)
    server.connection_count = 0
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}"
    try:
        yield base_url, server
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


class TestLocalConnectionReuseDemonstration:
    """Demonstrate the requests/urllib3 connection-reuse mechanism on loopback HTTP.

    This is a stand-in for, not a replacement of, a real benchmark against the
    live CrowdStrike API (not reachable from this environment).
    """

    def test_two_requests_without_session_open_two_connections(self, local_http_server):
        """Two independent module-level requests.get() calls open two connections."""
        base_url, server = local_http_server
        requests.get(base_url)
        requests.get(base_url)
        assert server.connection_count == 2

    def test_two_requests_with_session_reuse_one_connection(self, local_http_server):
        """Two calls through one requests.Session reuse a single connection."""
        base_url, server = local_http_server
        with requests.Session() as session:
            session.get(base_url)
            session.get(base_url)
        assert server.connection_count == 1
