![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)
![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# MalQuery examples
The examples in this folder focus on leveraging CrowdStrike's Hosts API to perform administrative operations.
- [MalQueryinator - Search and Download samples](#search-and-download-samples-from-malquery)

## Search and Download samples from MalQuery
Downloads a specified number of examples from MalQuery that match the search term and type you specify.
Results will be stored in _zip_ archive format with the password of `infected`.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| MalQuery | __READ__ |

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

### Example source code
The source code for this example can be found [here](malqueryinator.py).
