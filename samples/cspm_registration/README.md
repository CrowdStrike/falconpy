![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon CSPM Registration samples
The examples within this folder focus on leveraging CrowdStrike's Falcon CSPM Registration API.

- [Get all CSPM policies](#get-all-cspm-policies)

## Get all CSPM policies
Retrieves all CSPM policies for your environment and displays the associated benchmarks.

### Dependencies
This sample is dependent upon the [`python-tabulate`](https://github.com/gregbanks/python-tabulate) library.

#### Installing tabulate
Tabulate can be installed using the Python Package Index:

```shell
python3 -m pip install tabulate
```

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| CSPM Registration | __READ__ |


### Execution syntax
The following command will retrieve a list of hosts matching the specified CVE.

#### Basic usage
Display all policies and their associated benchmarks.

```shell
python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Instead of displaying to the console, you can instead export results to a file in CSV format using the `-o` argument.

```shell
python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o filename.csv
```

> To limit your results to a specific cloud provider, use the `-c` argument.

```shell
python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c aws
```

```shell
python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
```
> To activate debugging, use the `-d` argument.
#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_cspm_policies.py -h
usage: get_cspm_policies.py [-h] [-f FALCON_CLIENT_ID] [-s FALCON_CLIENT_SECRET] [-o OUTPUT_FILE] [-c CLOUD]

CrowdStrike Horizon - Retrieve CSPM Policies

  ___  ____  ____     ___  ____  ____  _  _    ____   __   __    __  ___  __  ____  ____
 / __)(  __)(_  _)   / __)/ ___)(  _ \( \/ )  (  _ \ /  \ (  )  (  )/ __)(  )(  __)/ ___)
( (_ \ ) _)   )(    ( (__ \___ \ ) __// \/ \   ) __/(  O )/ (_/\ )(( (__  )(  ) _) \___ \
 \___/(____) (__)    \___)(____/(__)  \_)(_/  (__)   \__/ \____/(__)\___)(__)(____)(____/

This example uses the CSPM Registration Class to output Horizon policies to CSV.

This sample requires FalconPy v0.7.4+.

Input parameters:

  --falcon_client_id or -f (client id of the API credentials with Horizon read capabilities)
  --falcon_client_secret or -s (secret associated with the client_id)
  --output_file or -o (the output file name and path (.csv extentions recommended))
  --cloud or -c (optional: the target cloud platform policies)

Examples:
Using client_id and client_secret as environment variables and will output all of the policies.

 python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET \
             -o ~/Documents/policies.csv

Using client_id and client_secret as environment variables and will output only the azure policies.

 python3 get_cspm_policies.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET \
             -c azure -o ~/Documents/azure-policies.csv

The script can also be ran using the config.json example credential file.

 python3 get_cspm_policies.py -c azure -o ~/Documents/azure-policies.csv

optional arguments:
  -h, --help            show this help message and exit
  -f FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Falcon Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Falcon Client Secret
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Policy report output file (CSV format)
  -c CLOUD, --cloud CLOUD
                        Cloud provider (aws, azure, gcp)
  -d, --debug,          Activates debugging 
```

### Example source code
The source code for this example can be found [here](get_cspm_policies.py).
