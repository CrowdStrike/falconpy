![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# MalQuery examples
The examples in this folder focus on leveraging CrowdStrike's MalQuery API to perform threat hunting operations.
- [MalQueryinator - Search and Download samples](#search-and-download-samples-from-malquery)

## Search and Download samples from MalQuery
Downloads a specified number of examples from MalQuery that match the search term and type you specify.
Results will be stored in _zip_ archive format with the password of `infected`.

> [!WARNING]
> Samples downloaded from MalQuery have been confirmed as __malware__. 
> __*Handle with extreme caution*__.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| MalQuery | __READ__, __WRITE__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose |
| :--- | :--- |
| `-t`, `--type` | Type of pattern for the query. Select from __ASCII__, __HEX__, or __WIDE__. Defaults to __ASCII__. |
| `-v`, `--value` | The value for malquery to search. |
| `-f`, `--file` | Filename to save the downloaded samples to. File will be in _zip_ format. |
| `-e`, `--examples` | Number of examples to download. Integer only. |
| `-k`, `--key` | Your CrowdStrike Falcon API Client ID |
| `-s`, `--secret` | Your CrowdStrike Falcon API Client Secret |

Downloads 3 `trickbot` samples from MalQuery
```shell
python3 malqueryinator.py -v trickbot -f samples.zip -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -e 3
```

#### Command-line help
Command-line help is available using the `-h` or `--help` parameters.

```shell
% python3 malqueryinator.py -h
usage: malquery.py [-h] [-t TYPE] -v VALUE -f FILE [-e EXAMPLES] -k KEY -s SECRET

Malquerinator

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  Type of pattern for the malware query: ascii, hex, or wide
  -v VALUE, --value VALUE
                        Value for malware query of type determined by --t/--type arg
  -f FILE, --file FILE  Name of file to write to
  -e EXAMPLES, --examples EXAMPLES
                        Number of examples to download
  -k KEY, --key KEY     Falcon API Client ID
  -s SECRET, --secret SECRET
                        Falcon API Client secret
```

### Example source code
The source code for this example can be found [here](malqueryinator.py).
