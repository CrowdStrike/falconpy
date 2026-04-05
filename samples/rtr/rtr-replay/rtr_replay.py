#!/usr/bin/env python3
"""
Falcon RTR Session Replay – CrowdStrike FalconPy
Enterprise Security Lab | Manjula Wickramasuriya
Endpoint Behavior Analytics
"""
import os
import sys
from falconpy import RealTimeResponse

class FalconRTRReplay:
    """Handler for CrowdStrike Falcon RTR session replay."""

    def __init__(self, client_id=None, client_secret=None, demo_mode=False):
        self.demo_mode = demo_mode
        if demo_mode:
            print("[INFO] Running in DEMO mode - no real API calls\n")
            self.rtr = None
        else:
            client_id = client_id or os.getenv('FALCON_CLIENT_ID')
            client_secret = client_secret or os.getenv('FALCON_CLIENT_SECRET')
            if not client_id or not client_secret:
                raise ValueError("Set FALCON_CLIENT_ID and FALCON_CLIENT_SECRET or use --demo")
            self.rtr = RealTimeResponse(client_id=client_id, client_secret=client_secret)

    def replay_session(self, session_id):
        if self.demo_mode:
            self._demo_replay(session_id)
            return
        # ... (keep Claude's full logic here — it's perfect)

    def _demo_replay(self, session_id):
        print("="*60)
        print("RTR SESSION REPLAY [DEMO MODE]")
        print("="*60)
        # ... (keep demo data)
        print("[INFO] Connect with real credentials for actual sessions")

def main():
    demo_mode = "--demo" in sys.argv or not os.getenv('FALCON_CLIENT_ID')
    replay = FalconRTRReplay(demo_mode=demo_mode)
    session_id = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "--demo" else "demo-session-123"
    replay.replay_session(session_id)

if __name__ == "__main__":
    main()
