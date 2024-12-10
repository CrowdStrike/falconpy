![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon Discover samples
The examples within this folder focus on leveraging CrowdStrike's Falcon Discover API.

- [List discovered hosts](#list-discovered-hosts)
- [Spyglass](#spyglass)

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

> Activate API debugging with the `-d` argument.

```shell
python3 list_discovered_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
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
usage: list_discovered_hosts.py [-h] [-k CLIENT_ID] [-s CLIENT_SECRET] [-b BASE_URL] [-r] [-d] [-f FORMAT]

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

options:
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
  -d, --debug           Enable API debugging
  -f FORMAT, --format FORMAT
                        Table format to use for display.
                        (plain, simple, github, grid, fancy_grid, pipe, orgtbl, jira, presto,
                        pretty, psql, rst, mediawiki, moinmoin, youtrack, html, unsafehtml,
                        latext, latex_raw, latex_booktabs, latex_longtable, textile, tsv)
```

### Example source code
The source code for this example can be found [here](list_discovered_hosts.py).

## Spyglass
Review Discover audit results for accounts, applications, hosts and logins.  Supports output to standalone JSON files.

### Dependencies
- `pyfiglet`
- `termcolor`

#### Installing dependencies
Dependencies can be installed using the Python Package Index:

```shell
python3 -m pip install pyfiglet termcolor
```

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Discover | __READ__ |
| Hosts | __READ__ |


### Execution syntax
The following commands demonstrate different audit variations. Command line arguments may be mixed and provided
to the application in any order.

#### Basic usage
Display all discovered accounts, applications, hosts and logins.

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Change your CrowdStrike region using the `-r` argument.

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r usgov1
```

> Limit audit categories with the `-c` argument.

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c accounts,logins
```

> Output results to JSON dump files (as well as the terminal).

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -j
```

> Disable dynamic screen updates (for automation / terminal output redirection).

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
```

> Filter examples

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --accounts_filter "account_name:*'*PRODUCTION*'"
```

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --applications_filter "is_suspicious:true"
```

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --hosts_filter "hostname:*'*search*'"
```

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --logins_filter "username:*'*larry*'"
```

> Sort examples

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --accounts_sort first_seen_timestamp.desc
```

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --applications_sort hostname.asc
```

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --hosts_sort last_seen_timestamp.desc
```

```shell
python3 spyglass.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --logins_sort login_timestamp.desc
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 spyglass.py -h
usage: spyglass.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-r REGION] [-c CATEGORIES] [-d] [-j] [--accounts_filter ACCOUNTS_FILTER] [--accounts_sort ACCOUNTS_SORT]
                   [--applications_filter APPLICATIONS_FILTER] [--applications_sort APPLICATIONS_SORT] [--hosts_filter HOSTS_FILTER] [--hosts_sort HOSTS_SORT]
                   [--logins_filter LOGINS_FILTER] [--logins_sort LOGINS_SORT]

CrowdStrike Falcon Discover real-time audit report utility.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |      FalconPy v1.2.11
`-------'                         `-------'

  ⢀⣀⣀           _______                     __
⢀⣾⡿⠛⠉          |     __|.-----.--.--.-----.|  |.---.-.-----.-----.
⢸⡟ ⣾⣿⣷⣤⡀       |__     ||  _  |  |  |  _  ||  ||  _  |__ --|__ --|
   ⠙⣿⣿⠟⢁⣤⡤     |_______||   __|___  |___  ||__||___._|_____|_____|
    ⠈⠁⣴⡿⢋⣤⣶⣶⣄⡀          |__|  |_____|_____|
      ⠋⢠⣿⣿⣿⣿⣿⣿⡦
       ⠘⢿⣿⣿⣿⠟⢁⣤⣶⠿⠛
        ⠈⠻⡿⠁⣴⡿⠋⣀⣴⣾⣿⣿⣷⣤⡀
           ⣼⡟⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠦        Requirements
           ⠛ ⣾⣿⣿⣿⣿⣿⡿⠟⣉⣤⣶⣶⣶⣶⡄       crowdstrike-falconpy (v1.2.11+)
             ⢿⣿⣿⣿⣿⠏⣠⣾⡿⠛⢉⣠⣤⣄⠈       pyfiglet
              ⠹⣿⣿⠃⣼⣿⠏ ⠔⣫⣿⣿⣿⡇       termcolor
               ⠈⠃⢰⣿⠃  ⢰⣿⣿⣿⡿
                 ⠸⣿   ⠈⣩⠿⠋
                  ⠉⠑ ⠈⠉

Created: 03.06.2023 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -r REGION, --region REGION
                        CrowdStrike region.
                        Choose from:
                           ▪ us1
                           ▪ us2
                           ▪ eu1
                           ▪ usgov1
                           ▪ auto
                        Only required for GovCloud users.
  -c CATEGORIES, --categories CATEGORIES
                        Discover categories to review.
                        Choose from:
                           ▪ accounts
                           ▪ applications
                           ▪ hosts
                           ▪ logins
                           ▪ all
                        Comma delimited strings are accepted.
  -d, --disable_dynamic_updates
                        Show dynamic update messages as API calls are performed.
  -j, --json            Output results to JSON save files.
  --accounts_filter ACCOUNTS_FILTER
                        Filter accounts results using FQL syntax.
                        Example: --accounts_filter "account_name:*'*PRODUCTION*'"
                        Filter must be enclosed in double quotes
  --accounts_sort ACCOUNTS_SORT
                        Sort accounts results using FQL syntax.
                        You may sort asc or desc by first_seen_timestamp or username.
                        Examples: --accounts_sort first_seen_timestamp.desc
                                  --accounts_sort username.asc
  --applications_filter APPLICATIONS_FILTER
                        Filter applications results using FQL syntax.
                        Example: --applications_filter "is_suspicious:true"
                        Filter must be enclosed in double quotes
  --applications_sort APPLICATIONS_SORT
                        Sort applications results using FQL syntax.
                        You may sort asc or desc by hostname or name (application).
                        Examples: --applications_sort hostname.asc
                                  --applications_sort name.desc
  --hosts_filter HOSTS_FILTER
                        Filter hosts results using FQL syntax.
                        Example: --applications_filter "hostname:*'*search_string*'"
                        Filter must be enclosed in double quotes
  --hosts_sort HOSTS_SORT
                        Sort hosts results using FQL syntax.
                        You may sort asc or desc by hostname or last_seen_timestamp.
                        Examples: --hosts_sort hostname.asc
                                  --hosts_sort last_seen_timestamp.desc
  --logins_filter LOGINS_FILTER
                        Filter logins results using FQL syntax.
                        Example: --logins_filter "username:*'*larry*'"
                        Filter must be enclosed in double quotes
  --logins_sort LOGINS_SORT
                        Sort logins results using FQL syntax.
                        You may sort asc or desc by login_timestamp or username.
                        Examples: --logins_sort login_timestamp.desc
                                  --logins_sort username.asc

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Falcon API Client Secret
```

### Example results
Example results from each category.

#### Accounts
Results from a sample accounts audit.

```shell
____ ____ ____ ____ _  _ _  _ ___ ____
|__| |    |    |  | |  | |\ |  |  [__
|  | |___ |___ |__| |__| | \|  |  ___]

--------------------------------------
Account              : WORKGROUP1\Administrator
Username             : Administrator (A Local account with admin privileges)
Domain               : WORKGROUP1
SID                  : S-1-5-21-1234567890-12345678-1234567890-500
First seen           : 02-17-2023 17:18:11
Last login success   : 02-17-2023 17:00:00 (Terminal server) (Some City, Some Country, 18.X.X.X)
Last password reset  : 02-17-2023 16:28:39
----------------------
Account              : DOMAIN1\USERNAME1
Username             : USERNAME1 (A Local account without admin privileges)
Domain               : DOMAIN1
SID                  : S-1-5-21-2345678901-23456781-2345678901-500
First seen           : 02-17-2023 17:19:18
Last login success   : 02-17-2023 16:00:00 (Interactive) (Some City, Some Country, 73.X.X.X)
Last password reset  : 02-17-2023 16:28:27
----------------------
Account              : WORKGROUP2\USERNAME2
Username             : USERNAME2 (A Local account with unknown admin privileges)
Domain               : WORKGROUP2
SID                  : S-1-5-21-3456789012-34567812-3456789012-500
First seen           : 02-17-2023 17:38:18
Last login success   : 02-17-2023 17:00:00 (Terminal server) (Some City, Some Country, 13.X.X.X)
Last password reset  : 02-17-2023 16:28:43
----------------------
```

#### Applications
Results from a sample applications audit.

```shell
____ ___  ___  _    _ ____ ____ ___ _ ____ _  _ ____
|__| |__] |__] |    | |    |__|  |  | |  | |\ | [__
|  | |    |    |___ | |___ |  |  |  | |__| | \| ___]

----------------------------------------------------
Host                 : WinHost1
Operating system     : Windows 10
Application          : Adobe WebInstaller
Last seen            : 01-30-2023 22:00:00 (SingleClientServicesUpdater.exe)
----------------------
Host                 : WinHost2
Operating system     : Windows Server 2019
Application          : PuTTY suite (Suspicious)
Last seen            : 02-27-2023 06:00:00 (pscp.exe)
----------------------
Host                 : WinHost3
Operating system     : Windows Server 2019
Application          : Windows
Last seen            : 03-15-2022 02:00:00 (MsMpEng.exe)
----------------------
Host                 : MacHost
Operating system     : Monterey (12)
Application          : Unknown
Last seen            : 02-21-2023 14:00:00 (usbmuxd)
Application          : Unknown
Last seen            : 01-14-2023 04:00:00 (CalendarWidgetExtension)
Application          : Unknown
Last seen            : 01-14-2023 04:00:00 (backupd)
Application          : Unknown
Last seen            : 01-16-2023 03:00:00 (ImageIOXPCService)
Application          : Unknown
Last seen            : 02-21-2023 15:00:00 (secd)
Application          : Unknown
Last seen            : 01-14-2023 04:00:00 (bootinstalld)
Application          : Unknown
Last seen            : 02-08-2023 14:00:00 (digest-service)
Application          : Creative Cloud Helper.app
Last seen            : 03-01-2023 20:00:00 (Creative Cloud Helper)
Application          : Unknown
Last seen            : 02-21-2023 15:00:00 (media-indexer)
Application          : Unknown
Last seen            : 02-21-2023 14:00:00 (talagent)
Application          : Unknown
Last seen            : 02-08-2023 14:00:00 (Basecamp 3 Helper)
Application          : Unknown
Last seen            : 02-21-2023 14:00:00 (knowledge-agent)
----------------------
Host                 : WinHost4
Operating system     : Windows Server 2016
Application          : Photo Viewer
Application          : Stxhd.HostAgents.ChannelRegistrar
Last seen            : 03-03-2023 07:00:00 (Stxhd.HostAgents.ChannelRegistrar.exe)
----------------------
Host                 : LinuxHost
Operating system     : Amazon Linux 2
Application          : hunspell-en
Application          : python-markupsafe
Application          : popt
Application          : python-backports
Application          : nss-softokn-freebl
Application          : python
Application          : mlocate
Application          : gettext
Application          : lm_sensors-libs
Application          : ncurses
Application          : crontabs
Application          : git
Application          : grub2-common
Application          : yum-langpacks
----------------------
```

#### Hosts
Results from a sample hosts audit.

```shell
_  _ ____ ____ ___ ____
|__| |  | [__   |  [__
|  | |__| ___]  |  ___]

-----------------------
Host                 : LinuxHost (Amazon Linux 2) (Sensor installed: 1a2bcde34f5a6b789012cd3ef456a7b8, 6.25.12207.0)
First seen           : 07-14-2021 18:35:27
Last seen            : 03-08-2023 16:00:00
Discovering device   : Yes
Current IP address   : 172.31.X.X
Network interface    : 172.17.X.X (02-XX-XX-06-D1-XX)
Network interface    : 172.31.X.X (02-XX-XX-70-7F-XX)
External IP address  : 18.X.X.X
----------------------
Host                 : WinHost (Windows Server 2019) (Sensor installed: fed098c7bafe654dc32b1a0f98765432, 6.33.14704.0)
First seen           : 11-18-2022 17:24:30
Last seen            : 03-08-2023 15:00:00
Discovering device   : Yes
Current IP address   : 10.12.X.X
Network interface    : 10.12.X.X (0A-XX-XX-D2-1D-XX)
External IP address  : 3.X.X.X
----------------------
Host                 : Unknown (Device not supported)
First seen           : 03-01-2023 23:00:00
Last seen            : 03-02-2023 00:00:00
Discovered by device : LinuxHost
Current IP address   : 192.168.X.X
Network interface    : 192.168.X.X (6C-XX-XX-E2-8E-XX)
----------------------
```

#### Logins
Results from a sample logins audit.

```shell
_    ____ ____ _ _  _ ____
|    |  | | __ | |\ | [__
|___ |__| |__] | | \| ___]

--------------------------
 03-07-2023 00:00:00  : Username4 succeeded on WinHost4 (13.X.X.X, Some City, Some Country)
 03-06-2023 00:00:00  : Username1 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 03-04-2023 00:00:00  : Username3 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 03-03-2023 00:00:00  : Username1 failed on WinHost1 (73.X.X.X, Some City, Some Country)
 03-03-2023 00:00:00  : Username2 succeeded on WinHost3 (3.X.X.X, Some City, Some Country)
 03-02-2023 00:00:00  : Username1 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 03-02-2023 00:00:00  : Username1 failed on WinHost1 (73.X.X.X, Some City, Some Country)
 03-01-2023 00:00:00  : Username1 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 02-28-2023 00:00:00  : Username1 succeeded on WinHost5 (18.X.X.X, Some City, Some Country)
 02-28-2023 00:00:00  : Username2 failed on WinHost1 (73.X.X.X, Some City, Some Country)
 02-25-2023 00:00:00  : Username2 succeeded on WinHost4 (13.X.X.X, Some City, Some Country)
 02-24-2023 00:00:00  : Username5 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 02-24-2023 00:00:00  : Username1 failed on WinHost1 (73.X.X.X, Some City, Some Country)
 02-21-2023 00:00:00  : usertwo succeeded on MacHost (174.X.X.X, Some City, Some Country)
 02-21-2023 00:00:00  : Username1 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 02-17-2023 00:00:00  : Administrator succeeded on WinHost2 (18.X.X.X, Some City, Some Country)
 02-17-2023 00:00:00  : Administrator succeeded on WinHost3 (3.X.X.X, Some City, Some Country)
 02-17-2023 00:00:00  : Administrator succeeded on WinHost4 (13.X.X.X, Some City, Some Country)
 02-17-2023 00:00:00  : Administrator succeeded on WinHost5 (18.X.X.X, Some City, Some Country)
 02-17-2023 00:00:00  : Username1 failed on WinHost1 (73.X.X.X, Some City, Some Country)
 02-17-2023 00:00:00  : Username1 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 02-16-2023 00:00:00  : Username3 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 02-14-2023 00:00:00  : usertwo succeeded on MacHost (24.X.X.X, Some City, Some Country)
 02-13-2023 00:00:00  : Username4 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 02-11-2023 00:00:00  : Username3 succeeded on WinHost2 (18.X.X.X, Some City, Some Country)
 02-08-2023 00:00:00  : usertwo succeeded on MacHost (24.X.X.X, Some City, Some Country)
 02-07-2023 00:00:00  : Username1 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 02-06-2023 00:00:00  : Username1 succeeded on WinHost2 (18.X.X.X, Some City, Some Country)
 02-05-2023 00:00:00  : Username4 succeeded on WinHost4 (13.X.X.X, Some City, Some Country)
 02-05-2023 00:00:00  : Username4 failed on WinHost1 (73.X.X.X, Some City, Some Country)
 02-03-2023 00:00:00  : Username1 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 02-02-2023 00:00:00  : Username1 failed on WinHost1 (73.X.X.X, Some City, Some Country)
 02-02-2023 00:00:00  : Username1 succeeded on WinHost3 (3.X.X.X, Some City, Some Country)
 02-01-2023 00:00:00  : Username3 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 01-31-2023 00:00:00  : Username3 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 01-30-2023 00:00:00  : Username2 succeeded on WinHost5 (18.X.X.X, Some City, Some Country)
 01-26-2023 00:00:00  : Username3 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
 01-26-2023 00:00:00  : Username1 failed on WinHost1 (73.X.X.X, Some City, Some Country)
 01-23-2023 00:00:00  : Username1 succeeded on WinHost1 (73.X.X.X, Some City, Some Country)
----------------------
```

### Example source code
The source code for this example can be found [here](spyglass.py).
