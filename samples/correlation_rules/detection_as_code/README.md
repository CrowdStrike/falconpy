<!--
 Copyright 2025 CrowdStrike.
-->

# Detection Rules as Code

This repository contains tooling to manage CrowdStrike Correlation Rules as code, enabling version control and automated deployment of detection rules.

## Overview

The project provides a Python-based solution for managing CrowdStrike Correlation Detection Rules through code, supporting:
- Synchronization between local rules and the API
- Creation of new rules
- Updates to existing rules
- Deletion of rules
- Version control through Git

## Prerequisites

- Python 3.x
-  CrowdStrike API Credential for read & write permission on the `Correlation Rules` scope
- Required Python packages: [crowdstrike-falconpy](https://github.com/CrowdStrike/falconpy)
  ```bash
  pip install crowdstrike-falconpy
  ```
## Setup
- Clone the repository:
```bash
git clone <repository-url>
cd detection-as-code
```
- Set up environment variables:
```bash
export FALCON_CLIENT_ID="your-client-id"
export FALCON_CLIENT_SECRET="your-client-secret"
export FALCON_BASE_URL="your-base-url"  # Optional
export LOG_LEVEL="as-desired"  # Optional
  - Valid values: DEBUG, INFO, WARNING, ERROR, CRITICAL
```
## Usage
### Initial Sync
To perform initial synchronization with the API:
```bash
python scripts/sync_detections.py
```
This will create/update `rules/rules.json` with the current state from the API.
### Creating New Rules
1) Add a new rule to `rules.json` without an ID:
```json
{
  "id": "",
  "name": "New Detection Rule",
  "severity": 50,
  "customer_id": "<<CID>>",
  "search": {
    "filter": "your-query-here",
    "outcome": "detection",
    "lookback": "75m",
    "trigger_mode": "summary"
  },
  "operation": {
    "schedule": {
      "definition": "@every 1h"
    },
    "start_on": "2025-02-18T22:30:00Z",
  }
  "status": "active"
}
```
2) Run the sync script to create the rule in the API.
### Updating Rules
1) Modify the desired rule in `rules.json`
2) Run the sync script to apply changes
### Deleting Rules
1) Add `"deleted": true` to the rule in rules.json
2) Run the sync script to delete the rule from the API
## File Structure
```bash
.
├── README.md
├── rules/
│   └── rules.json
└── scripts/
    └── sync_detections.py
```
## GitHub Actions
This repository includes a GitHub Actions workflow that:

- Runs on changes to rules.json
- Validates and syncs rules with the API

## Required GitHub Secrets
- FALCON_CLIENT_ID
- FALCON_CLIENT_SECRET
- FALCON_BASE_URL (optional)
- LOG_LEVEL (optional)
