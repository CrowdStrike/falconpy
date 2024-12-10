![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Identity Protection examples
The examples within this folder focus on leveraging CrowdStrike Falcon Identity Protection.

- [GraphQL Pagination](#graphql-pagination)

## GraphQL Pagination
Demonstrates pagination using GraphQL.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Identity Protection | __READ__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Retrieve the primaryDisplayName and the secondaryDisplayName for all identities within the tenant.

```shell
python3 graphql_pagination -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Adjust the limit to show pagination differences with the `-l` argument.

```shell
python3 graphql_pagination -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -l 10
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 graphql_pagination.py -h
usage: graphql_pagination.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-l LIMIT]

Identity Protection pagination example.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |       FalconPy v1.2.11
`-------'                         `-------'

_____ ______  _______ __   _ _______ _____ _______ __   __
  |   |     \ |______ | \  |    |      |      |      \_/
__|__ |_____/ |______ |  \_|    |    __|__    |       |

 _____   ______  _____  _______ _______ _______ _______ _____  _____  __   _
|_____] |_____/ |     |    |    |______ |          |      |   |     | | \  |
|       |    \_ |_____|    |    |______ |_____     |    __|__ |_____| |  \_|

This sample demonstrates pagination within the IDP service collection using GraphQL syntax.

Creation: 02.15.23 - jshcodes@CrowdStrike

This example requires crowdstrike-falconpy v1.2.11+.

optional arguments:
  -h, --help            show this help message and exit
  -l LIMIT, --limit LIMIT
                        Number of records to handle per batch

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API client Secret
```

### Example source code
The source code for this example can be found [here](graphql_pagination.py).