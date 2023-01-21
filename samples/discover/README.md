![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

# Falcon Discover samples
The examples within this folder focus on leveraging CrowdStrike's Falcon Discover API.

- [List discovered hosts](#list-discovered-hosts)

## List discovered hosts
Displays the hostname, local IP, external IP, OS platform and OS version for discovered hosts.

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
| Discover | __READ__ |


### Execution syntax
The following command will retrieve a list of discovered hosts.

#### Basic usage
Display all discovered hosts.

```shell
python3 list_discovered_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Reverse the sort using the `-r` argument.

```shell
python3 list_discovered_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r
```

> Change your CrowdStrike region using the `-b` argument.

```shell
python3 list_discovered_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

> Change the table format using the `-f` argument.

```shell
python3 list_discovered_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f simple
```

##### Available table formats
Tabular results may be formatted using any of the format options listed below.

- `plain`
- `simple`
- `github`
- `grid`
- `fancy_grid`
- `pipe`
- `orgtbl`
- `jira`
- `presto`
- `pretty`
- `psql`
- `rst`
- `mediawiki`
- `moinmoin`
- `youtrack`
- `html`
- `unsafehtml`
- `latext`
- `latex_raw`
- `latex_booktabs`
- `latex_longtable`
- `textile`
- `tsv`

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 list_discovered_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -h
usage: list_discovered_hosts.py [-h] [-k CLIENT_ID] [-s CLIENT_SECRET] [-b BASE_URL] [-r] [-f FORMAT]

CrowdStrike Falcon Discover simple example.

             ______
          .-'      `-.
        .'            `.
       /                \
      ;                 ;`
      |   CrowdStrike   |;
      ;      Falcon     ;|
      '\               / ;
       \`.           .' /
        `.`-._____.-' .'
          / /`_____.-'
         / / /
        / / /   ______   __
       / / /   |   _  \ |__.-----.----.-----.--.--.-----.----.
      / / /    |.  |   \|  |__ --|  __|  _  |  |  |  -__|   _|
     / / /     |.  |    |__|_____|____|_____|\___/|_____|__|
    / / /      |:  1    /
   / / /       |::.. . /           FalconPy v1.0.1
  / / /        `------'
 / / /
 \/_/

Creation date: 02.08.2022 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key ID.
                        You can also use the `FALCON_CLIENT_ID` environment variable to specify this value.
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API key secret.
                        You can also use the `FALCON_CLIENT_SECRET` environment variable to specify this value.
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike API region (us1, us2, eu1, usgov1) NOT required unless you are using `usgov1`.
  -r, --reverse         Reverse sort (defaults to ASC)
  -f FORMAT, --format FORMAT
                        Table format to use for display.
                        (plain, simple, github, grid, fancy_grid, pipe, orgtbl, jira, presto,
                        pretty, psql, rst, mediawiki, moinmoin, youtrack, html, unsafehtml,
                        latext, latex_raw, latex_booktabs, latex_longtable, textile, tsv)
```

### Example source code
The source code for this example can be found [here](list_discovered_hosts.py).
