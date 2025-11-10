#!/usr/bin/env python3
"""
Top 10 Noisy Hosts – CrowdStrike Falcon
PhD Research Lab | Manjula Wickramasuriya
US PhD 2027 – Endpoint Security
"""
from falconpy import Hosts

# Demo mode – no real credentials needed for PR
falcon = Hosts(client_id="demo", client_secret="demo")

def top_noisy_hosts(days=7, limit=10):
    # In real use: query hosts with high login_count
    print(f"[DEMO] Top {limit} Noisy Hosts (last {days} days):")
    print("HOST123456.example.com          2025-11-10T08:00:00Z     1247 logins")
    print("HOST789012.example.com          2025-11-10T07:30:00Z     987 logins")
    print("... (requires Falcon API key for real data)")

if __name__ == "__main__":
    top_noisy_hosts()
