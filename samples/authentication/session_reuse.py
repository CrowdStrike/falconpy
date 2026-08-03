"""CrowdStrike FalconPy Persistent Session (Connection Reuse) Example.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

Every FalconPy client accepts an optional `session` keyword: an existing
`requests.Session` to reuse for connection pooling across login, every API
call, token renewal, and logout. This avoids repeating the TCP/TLS handshake
for each request, which matters most for workloads issuing many sequential
calls.

FalconPy never closes a session provided this way. The caller retains full
ownership of its lifecycle, most naturally by using it as a context manager
as demonstrated below.

If you share one session across multiple threads, you are responsible for
your own synchronization; requests.Session is not guaranteed safe for
concurrent use without care.

This sample requires API credentials with READ access to the Hosts service
collection, provided via the FALCON_CLIENT_ID and FALCON_CLIENT_SECRET
environment variables.
"""
import os
import requests
from falconpy import OAuth2, Hosts


def main():
    """Demonstrate session reuse across authentication and multiple API calls."""
    client_id = os.getenv("FALCON_CLIENT_ID")
    client_secret = os.getenv("FALCON_CLIENT_SECRET")

    # The session is created (and closed) entirely by the caller.
    with requests.Session() as session:
        # Login and every request made by this auth_object reuse `session`.
        auth = OAuth2(client_id=client_id, client_secret=client_secret, session=session)

        # Service Classes constructed from a shared auth_object inherit its session.
        hosts = Hosts(auth_object=auth)

        for _ in range(3):
            response = hosts.query_devices_by_filter(limit=1)
            print(f"Status: {response['status_code']}")

        auth.logout()
    # The session is closed here, by the caller's `with` block, not by FalconPy.


if __name__ == "__main__":
    main()
