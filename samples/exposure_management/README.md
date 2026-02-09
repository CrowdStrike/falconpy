![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Exposure Management examples
The examples in this folder focus on leveraging CrowdStrike's Falcon Exposure Management (EASM) service collection.
- [em_manager - Generate Executive Security Reports](#Generate-Executive-Security-Reports)

## Generate Executive Security Reports
Generates comprehensive executive-level security reports from your external attack surface data. This tool discovers exposed assets, analyzes security posture, and produces professional PDF reports suitable for C-suite presentations, board meetings, and compliance documentation.

> [!IMPORTANT]
> This sample requires a Falcon EASM subscription and is designed for generating executive reports from external attack surface monitoring data.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Exposure Management | __READ__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose |
| :--- | :--- |
| `-d`, `--debug` | Enable API debugging. |
| `-o`, `--output` | Output filename (default: Executive_Report.pdf). |
| `-f`, `--format` | Export format: pdf, json, csv (default: pdf). |
| `--dark` | Enable dark mode for PDF reports. |
| `--subsidiary` | Filter by specific subsidiary name. |
| `--logo` | Path to logo image for PDF reports (default: img/cs-logo.png). |
| `-k`, `--client_id` | Your CrowdStrike Falcon API Client ID |
| `-s`, `--client_secret` | Your CrowdStrike Falcon API Client Secret |

Generate PDF report with default settings.
```shell
python3 em_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

Generate dark mode PDF with custom filename.
```shell
python3 em_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o my_report.pdf --dark
```

Export to JSON format.
```shell
python3 em_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f json -o report.json
```

Export to CSV format.
```shell
python3 em_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f csv -o report.csv
```

Filter by specific subsidiary.
```shell
python3 em_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --subsidiary "Company Name"
```

Use custom logo for branded reports.
```shell
python3 em_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --logo /path/to/logo.png
```

Enable API debugging.
```shell
python3 em_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
```

### Report Contents

The generated PDF report includes:

#### Executive Summary
- Total exposed assets across all subsidiaries
- Critical and high-risk asset counts
- Risk classification overview

#### Enhanced Attack Surface Analysis
- Internet exposure statistics with percentages
- Shadow IT identification (unofficial perimeter assets)
- Triage status and remediation progress
- Online/offline asset status
- Discovery method breakdown (auto vs manual)
- Geographic distribution (top 10 countries)
- Top hosting providers (ISPs/cloud providers)

#### Asset Discovery Intelligence
- Example discovery chains showing how assets were found
- Visual paths: Parent Company → Domain → Subdomain → IP
- Helps identify shadow IT and third-party dependencies

#### Per-Subsidiary Details
- Asset summary by criticality level
- Exposed applications inventory
- Critical and high-risk asset details with:
  - FQDN and IP address
  - Asset type and status
  - Confidence level
  - Geographic location
  - Hosting provider information

#### Understanding Your Attack Surface
- Explanations of key EASM concepts
- Criticality classification definitions
- Organizational structure overview

### Required Python Libraries
In addition to FalconPy (`crowdstrike-falconpy`), this application requires the following Python package:

- `reportlab` (for PDF generation)

Install dependencies:
```shell
pip install crowdstrike-falconpy reportlab
```

Or using pipenv:
```shell
pipenv install crowdstrike-falconpy reportlab
```

#### Command-line help
Command-line help is available using the `-h` or `--help` parameters.

```shell
python3 em_manager.py -h
usage: em_manager.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-d] [-o OUTPUT] [-f {pdf,json,csv}]
                     [--dark] [--subsidiary SUBSIDIARY] [--logo LOGO]

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

This sample utilizes the Exposure Management service collection
to identify exposed assets and return the results as a PDF report.

USAGE EXAMPLES:
    # Generate PDF report with default settings
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET

    # Generate dark mode PDF with custom filename
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET -o my_report.pdf --dark

    # Export to JSON format
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET -f json -o report.json

    # Export to CSV format
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET -f csv -o report.csv

    # Filter by specific subsidiary
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET --subsidiary "Company Name"

Creation date: 12.10.25 - alhumaw

required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike API client secret

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -o OUTPUT, --output OUTPUT
                        Output filename (default: Executive_Report.pdf)
  -f {pdf,json,csv}, --format {pdf,json,csv}
                        Export format: pdf, json, csv (default: pdf)
  --dark                Enable dark mode for PDF reports
  --subsidiary SUBSIDIARY
                        Filter by specific subsidiary name
  --logo LOGO           Path to logo image for PDF reports (default: img/cs-logo.png)
```

### Use Cases

This tool is designed for:
- **Executive presentations** - Board meetings and C-suite briefings
- **Compliance reporting** - Demonstrating external attack surface management
- **Security assessments** - Quarterly business reviews and risk analysis
- **MSSP/consultant reports** - Monthly client security posture reports
- **M&A due diligence** - Assessing acquisition target security posture
- **Customer security questionnaires** - Demonstrating EASM capabilities

### Example source code
The source code for this example can be found [here](em_manager.py).
