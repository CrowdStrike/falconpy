![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)
![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# Analyze a single file with Falcon Intelligence Sandbox
These examples upload a single file you specify to the CrowdStrike Sample Uploads API.
The file is then submitted to the CrowdStrike Falcon Intelligence Sandbox for detonation and analysis.
Results for the analysis are displayed upon completion, and then the file is removed from the 
CrowdStrike sandbox.

> This example requires FalconPy v0.6.3+

## Procedure
1. Arguments are consumed. The submitted filename and environment are confirmed to be valid.
    - The procedure will halt if either of these are found not to be true.
2. Provided API credentials are used to connect to the CrowdStrike Falcon Intelligence Sandbox and Sample Uploads APIs.
3. The target file is uploaded to the CrowdStrike Sample Uploads API.
4. The file is submitted to the CrowdStrike Falcon Intelligence Sandbox API for analysis.
    - The procedure starts a progress indicator and will wait for this analysis to complete. Depending on file type and other factors this may take up to 15 minutes.
5. When results are ready, the analysis is retrieved.
6. The uploaded file is removed from the CrowdStrike Sample Uploads API.
7. Analysis results are displayed.
    - If an error was encountered during the analysis it will be displayed at this time.
    - If an error was encountered removing the file from the sandbox, it will be displayed after the results are shown.

## Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Falcon Intelligence Sandbox | __READ__, __WRITE__ |
| Sample Uploads | __READ__, __WRITE__ |

### Execution syntax
The following command will perform an analysis of a single file.

```shell
python3 falconx_scan_example.py -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET -f FILE_TO_SCAN -e ENVIRONMENT
```

##### Uber class variation
There is no functional difference between the Service and Uber Class examples.
```shell
python3 falconx_scan_example_uber.py -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET -f FILE_TO_SCAN -e ENVIRONMENT
```

### Selecting the detonation environment
The Falcon Intelligence Sandbox API supports the following environments. If you wish to specify the sandbox environment where your file is detonated, you may do so using the `-e` argument. You must provide one of the identifiers from the list below.  When not provided, this example will default to Windows 10 64-bit.
| Identifier | Environment |
| :--- | :--- |
| `win7` | Windows 7, 32-bit |
| `win7_64` | Windows 7, 64-bit |
| `win10` | Windows 10, 64-bit |
| `droid` | Android (static analysis) |
| `linux` | Ubuntu 16.04, 64-bit |
| `macos` | macOS Catalina 10.15 |

### Command-line help
Command-line help is available via the `-h` argument.

```shell
% python3 falconx_scan_example.py -h
usage: falconx_scan_example.py [-h] -f FILE [-e ENVIRONMENT] -k KEY -s SECRET

Falcon X Sandbox example

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File to analyze
  -e ENVIRONMENT, --environment ENVIRONMENT
                        Environment to use for analysis (win7, win7_64, win10, droid, linux)
  -k KEY, --key KEY     Your CrowdStrike API key ID Required Scopes Sample Uploads: WRITE Sandbox: WRITE
  -s SECRET, --secret SECRET
                        Your CrowdStrike API key secret
```

## Example source code
The source code for this example can be found at [Service Class](falconx_scan_example.py) and [Uber Class](falconx_scan_example_uber.py).
