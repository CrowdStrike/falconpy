![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Intel examples
The examples within this folder focus on leveraging CrowdStrike Falcon Intel service collection.

- [Get MITRE ATT&CK reports](#get-mitre-attck-reports)
- [Intel Search](#intel-search)

## Get MITRE ATT&CK Reports
Retrieves MITRE ATT&CK reports for specified adversaries.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Intel | __READ__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Retrieve all available MITRE ATT&CK reports.

```shell
python3 get_mitre_reports.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Execute the routine for GovCloud customers.

```shell
python3 get_mitre_reports.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -g
```

> Only retrieve available kitten reports.

```shell
python3 get_mitre_reports.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i kitten
```

> Retrieve all available reports for bears, jackals, spiders and also grab Stardust Chollima.

```shell
python3 get_mitre_reports.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i bear,jackal,spider,stardust
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_mitre_reports.py -h
usage: get_mitre_reports.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-g] [-f FORMAT] [-i ID_SEARCH]

Retrieve MITRE reports for adversaries.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |       FalconPy v1.2.10
`-------'                         `-------'

 _   _  _  ___  ___ ___      _  ___  ___ _    __  _  _
| \_/ || ||_ _|| o \ __|    / \|_ _||_ _(o)  / _|| |//
| \_/ || | | | |   / _|    | o || |  | |/oV7( (_ |  (
|_| |_||_| |_| |_|\\___|   |_n_||_|  |_|\_n\ \__||_|\\

____ ____ ___  ____ ____ ___   ___  ____ _ _ _ _  _ _    ____ ____ ___
|__/ |___ |__] |  | |__/  |    |  \ |  | | | | |\ | |    |  | |__| |  \
|  \ |___ |    |__| |  \  |    |__/ |__| |_|_| | \| |___ |__| |  | |__/

Download MITRE ATT&CK reports for specified (or all) adversaries.

This application requires:
    colorama
    crowdstrike-falconpy v1.2.10+

Created: 02.24.23 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -g, --usgov           US GovCloud customers
  -f FORMAT, --format FORMAT
                        Report format (csv [default] or json)
  -i ID_SEARCH, --id_search ID_SEARCH
                        Filter by actor slug (stemmed search, comma delimit)

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client Secret
```

### Example source code
The source code for this example can be found [here](get_mitre_reports.py).

## Intel Search
Quickly search CrowdStrike Falcon Intelligence data for string matches.
Displays lists of matches and extended details for individual records when only one result is returned.
When a value for output prefix (`-o`) is provided, results will also be written to individual files in CSV format.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Actors (Falcon Intelligence) | __READ__ |
| Indicators (Falcon Intelligence) | __READ__ |
| Reports (Falcon Intelligence) | __READ__ |

#### Required Python libraries
In addition to FalconPy (`crowdstrike-falconpy`), this application requires the following Python packages:

- `pyfiglet`
- `tabulate`
- `termcolor`

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Search for all actors, indicators and reports containing the string `spider`.

```shell
python3 intel_search.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f spider
```

> Providing a file prefix with the `-o` argument will also output the results in CSV format to individual files.

```shell
python3 intel_search.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f spider -o example
```

##### Result

```shell
Searching Falcon Threat Intelligence for spider.
Retrieving XX actor results.
Retrieving X,XXX indicator results.
Retrieving X,XXX report results.
 _______ _______ _______  _____   ______ _______
 |_____| |          |    |     | |_____/ |______
 |     | |_____     |    |_____| |    \_ ______|

╒═══════════════════╤════════════╕
│ Name              │ ID         │
╞═══════════════════╪════════════╡
│ ADVERSARY NAME    │ ADV-ID     │
├───────────────────┼────────────┤
│ ADVERSARY NAME    │ ADV-ID     │
├───────────────────┼────────────┤
│ ADVERSARY NAME    │ ADV-ID     │
├───────────────────┼────────────┤
│ etc...            │ etc...     │
╘═══════════════════╧════════════╛

 _____ __   _ ______  _____ _______ _______ _______  _____   ______ _______
   |   | \  | |     \   |   |       |_____|    |    |     | |_____/ |______
 __|__ |  \_| |_____/ __|__ |_____  |     |    |    |_____| |    \_ ______|

╒══════════════════════════════════════════════════════════════════════════════════════════╕
│ Indicator                                                                      │ Type    │
╞══════════════════════════════════════════════════════════════════════════════════════════╡
│ INDICATOR VALUE                                                                │ TYPE    │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ INDICATOR VALUE                                                                │ TYPE    │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ INDICATOR VALUE                                                                │ TYPE    │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ etc...                                                                         │ etc...  │
╘════════════════════════════════════════════════════════════════════════════════╧═════════╛

  ______ _______  _____   _____   ______ _______ _______
 |_____/ |______ |_____] |     | |_____/    |    |______
 |    \_ |______ |       |_____| |    \_    |    ______|

╒══════════════════════════════════════════════════════════════════════════════════════════╕
│ NName                                                                          │ Type    │
╞══════════════════════════════════════════════════════════════════════════════════════════╡
│ REPORT_ID REPORT TITLE                                                         │ TYPE    │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ REPORT_ID REPORT TITLE                                                         │ TYPE    │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ REPORT_ID REPORT TITLE                                                         │ TYPE    │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ etc...                                                                         │ etc...  │
╘════════════════════════════════════════════════════════════════════════════════╧═════════╛

Total actors: XX
Total indicators: X,XXX
Total reports: X,XXX
Execution time: 4.81 seconds
```

Search for a specific actor. (Any time only one result is returned, the application defaults to a detailed display.)

```shell
python3 intel_search.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f "fancy bear" -t actor
```

##### Result

```shell
Searching Falcon Threat Intelligence for fancy bear.
Retrieving 1 actor results.
 _______                             ______
|    ___|.---.-.-----.----.--.--.   |   __ \.-----.---.-.----.
|    ___||  _  |     |  __|  |  |   |   __ <|  -__|  _  |   _|
|___|    |___._|__|__|____|___  |   |______/|_____|___._|__|
                          |_____|

First activity: mm-dd-YYYY     Most recent activity: mm-dd-YYYY

Otherwise known as
List of actor aliases and personas

Adversary description
FANCY BEAR is an adversary attributed to the lorem ipsum dolor sit amet, consectetur adipiscing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Iaculis nunc sed augue
lacus viverra vitae congue eu consequat. Sem nulla pharetra diam sit amet nisl suscipit. Sed id
semper risus in hendrerit gravida rutrum. Odio ut sem nulla pharetra diam sit amet nisl suscipit.
At imperdiet dui accumsan sit amet nulla. At in tellus integer feugiat scelerisque varius. Sem et
tortor consequat id porta nibh venenatis. Scelerisque eu ultrices vitae auctor eu augue ut lectus
arcu. Risus ultricies tristique nulla aliquet enim. Sit amet dictum sit amet justo donec enim diam
vulputate. Parturient montes nascetur ridiculus mus mauris vitae ultricies leo. Commodo nulla 
facilisi nullam vehicula ipsum a arcu. Quam elementum pulvinar etiam non quam. Vitae ultricies leo 
integer malesuada nunc. Ornare arcu odio ut sem nulla pharetra diam.

Sodales ut etiam sit amet nisl purus in mollis nunc. Tellus rutrum tellus pellentesque eu tincidunt 
tortor aliquam nulla facilisi. Libero id faucibus nisl tincidunt eget. Pharetra magna ac placerat 
vestibulum lectus mauris. Enim sit amet venenatis urna cursus eget nunc. Sagittis purus sit amet 
volutpat consequat mauris nunc. Enim nec dui nunc mattis enim ut tellus elementum sagittis. Massa 
eget egestas purus viverra accumsan in nisl. Egestas sed tempus urna et. Tincidunt vitae semper quis 
lectus nulla at. At urna condimentum mattis pellentesque id. Massa tincidunt nunc pulvinar sapien et 
ligula. Aliquam vestibulum morbi blandit cursus risus at ultrices mi. Et leo duis ut diam quam nulla 
porttitor. Ut placerat orci nulla pellentesque. Id diam maecenas ultricies mi. Sagittis eu volutpat 
odio facilisis mauris.

Actor type: Actor Type     Capability: Actor Capability     Origins: Actor Origin

Motivations: Motivation detail

Objectives: Objective list

Targeted regions: List of targeted regions

Targeted countries
List of targeted countries

Targeted industries
List of targeted industries

Tactics, Techniques and Procedures
Actions and Objectives: Action and Objectives detail

Command and Control: Command and Control detail

Delivery: Delivery detail

Exploitation: List of exploited CVEs

Installation: Installation detail

Reconnaissance: Reconnaissance detail

Weaponization: Weaponization detail

Total actors: 1
Execution time: 1.10 seconds
```

Search for all CrowdStrike annual reports.

```shell
python3 intel_search.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f csar -t report
```

##### Result

```shell
Searching Falcon Threat Intelligence for csar.
Retrieving XX report results.
  ______ _______  _____   _____   ______ _______ _______
 |_____/ |______ |_____] |     | |_____/    |    |______
 |    \_ |______ |       |_____| |    \_    |    ______|

╒═══════════════════════════════════════════════════════╤═════════════════╕
│ Name                                                  │ Type            │
╞═══════════════════════════════════════════════════════╪═════════════════╡
│ CSAR-REPORT_ID CrowdStrike Intelligence Report Name   │ Report Type     │
├───────────────────────────────────────────────────────┼─────────────────┤
│ CSAR-REPORT_ID CrowdStrike Intelligence Report Name   │ Report Type     │
├───────────────────────────────────────────────────────┼─────────────────┤
│ CSAR-REPORT_ID CrowdStrike Intelligence Report Name   │ Report Type     │
├───────────────────────────────────────────────────────┼─────────────────┤
│ etc...                                                │ etc...          │
╘═══════════════════════════════════════════════════════╧═════════════════╛

Total reports: XX
Execution time: 1.57 seconds
```

Review the details for a single CrowdStrike report.

> Note: _you do not have to limit results to the reports category for this example._

```shell
python3 intel_search.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f CSIT-IDHERE -t report
```

##### Result

```shell
Searching Falcon Threat Intelligence for CSIT-IDHERE.
Retrieving 0 actor results.
Retrieving 1 report results.
Retrieving 0 indicator results.
  ______     _______. __  .___________.    __   _______   __    __   _______ .______       _______
 /      |   /       ||  | |           |   |  | |       \ |  |  |  | |   ____||   _  \     |   ____|
|  ,----'  |   (----`|  | `---|  |----`   |  | |  .--.  ||  |__|  | |  |__   |  |_)  |    |  |__
|  |        \   \    |  |     |  |        |  | |  |  |  ||   __   | |   __|  |      /     |   __|
|  `----.----)   |   |  |     |  |        |  | |  '--'  ||  |  |  | |  |____ |  |\  \----.|  |____
 \______|_______/    |__|     |__|        |__| |_______/ |__|  |__| |_______|| _| `._____||_______|

Report Title

Created on: mm-dd-YYYY HH:MM:SS     Last modification:: mm-dd-YYYY HH:MM:SS

Tags: List of report tags

Motivations: Motivation list

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Neque vitae tempus quam pellentesque nec. Euismod quis viverra nibh cras 
pulvinar mattis nunc. Sed libero enim sed faucibus. Bibendum ut tristique et egestas quis. 
Pellentesque diam volutpat commodo sed. Suspendisse interdum consectetur libero id faucibus. In hac 
habitasse platea dictumst quisque sagittis purus sit amet. Tortor posuere ac ut consequat semper. 
Morbi leo urna molestie at elementum eu facilisis sed. Purus viverra accumsan in nisl. Diam in arcu 
cursus euismod quis viverra nibh. Euismod quis viverra nibh cras pulvinar mattis nunc. Aenean vel 
elit scelerisque mauris pellentesque pulvinar pellentesque. Pretium aenean pharetra magna ac 
placerat vestibulum. Malesuada fames ac turpis egestas integer eget.

At tempor commodo ullamcorper a lacus vestibulum. Tristique senectus et netus et. Sit amet est 
placerat in egestas erat. Proin libero nunc consequat interdum varius sit. Nulla porttitor massa id 
neque. Felis eget nunc lobortis mattis aliquam. Mi sit amet mauris commodo quis imperdiet massa. 
Ipsum dolor sit amet consectetur adipiscing elit ut aliquam purus. Euismod in pellentesque massa 
placerat duis. Turpis massa tincidunt dui ut ornare lectus sit amet est. Lectus quam id leo in vitae 
turpis massa sed. Cras tincidunt lobortis feugiat vivamus at augue. Facilisis volutpat est velit 
egestas dui id ornare arcu.

Semper auctor neque vitae tempus quam pellentesque nec. Ac placerat vestibulum lectus mauris 
ultrices eros in. Eu tincidunt tortor aliquam nulla facilisi cras fermentum. Praesent tristique 
magna sit amet purus gravida quis blandit. Accumsan tortor posuere ac ut consequat semper viverra. 
Sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum. Purus gravida quis blandit 
turpis. Dui nunc mattis enim ut tellus elementum sagittis vitae et. Id velit ut tortor pretium 
viverra suspendisse potenti nullam. Augue ut lectus arcu bibendum at. At varius vel pharetra vel 
turpis nunc eget lorem dolor.

Vel risus commodo viverra maecenas accumsan lacus vel facilisis volutpat. Nunc aliquet bibendum enim 
facilisis gravida neque convallis a. Donec et odio pellentesque diam volutpat commodo sed egestas 
egestas. Faucibus turpis in eu mi bibendum neque egestas congue. Cursus mattis molestie a iaculis at 
erat. Est placerat in egestas erat imperdiet sed. Id nibh tortor id aliquet lectus. Duis at tellus 
at urna condimentum mattis pellentesque id nibh. Gravida cum sociis natoque penatibus. Egestas purus 
viverra accumsan in nisl. Vel turpis nunc eget lorem dolor. Curabitur vitae nunc sed velit dignissim 
sodales ut eu sem. Arcu cursus vitae congue mauris rhoncus aenean vel. Facilisis volutpat est velit 
egestas dui id ornare arcu odio. Et odio pellentesque diam volutpat commodo sed egestas egestas. 
Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat. Mauris commodo quis imperdiet 
massa. Nunc eget lorem dolor sed.

Total actors: 0
Total indicators: 0
Total reports: 1
Execution time: 2.88 seconds
```

Search for a specific indicator.

> Note: _you do not have to limit results to the indicators category for this example._

```shell
python3 intel_search.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f some_malicious_indicator.url -t indicator
```

##### Result

```shell
Searching Falcon Threat Intelligence for some_malicious_indicator.url.
Retrieving 1 indicator results.

some_malicious_indicator.url

Publish date: mm-dd-YYYY HH:MM:SS
Last updated: mm-dd-YYYY HH:MM:SS
Indicator type: domain
Domain types: domain type detail

Confidence: low/medium/high
Malware families: MalwareFamily

Threat types: Threat1, Threat2, etc.

Kill chain: Kill chain detail

Labels: Label1 (mm-dd-YYYY), Label2 (mm-dd-YYYY), Label3 (mm-dd-YYYY), 
Label4 (mm-dd-YYYY), Label5 (mm-dd-YYYY)

Related indicators
  • indicator1
  • indicator2
  • etc...

Total indicators: 1
Execution time: 2.86 seconds
```

Show the debug output.
```shell
python3 intel_search.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f "FROZEN SPIDER" -d 
```
##### Result
```shell
DEBUG:falconpy._auth_object._falcon_interface:CREATED: OAuth2 interface class
DEBUG:falconpy._auth_object._falcon_interface:AUTH: Configured for Direct Authentication
DEBUG:falconpy._auth_object._falcon_interface:CONFIG: Base URL set to https://api.crowdstrike.com
DEBUG:falconpy._auth_object._falcon_interface:CONFIG: SSL verification is set to True
DEBUG:falconpy._auth_object._falcon_interface:CONFIG: Timeout set to None seconds
DEBUG:falconpy._auth_object._falcon_interface:CONFIG: Proxy dictionary: None
DEBUG:falconpy._auth_object._falcon_interface:CONFIG: User-Agent string set to: None
DEBUG:falconpy._auth_object._falcon_interface:CONFIG: Token renewal window set to 120 seconds
DEBUG:falconpy._auth_object._falcon_interface:CONFIG: Maximum number of records to log: 100
DEBUG:falconpy._auth_object._falcon_interface:CONFIG: Log sanitization is enabled
DEBUG:falconpy._auth_object._falcon_interface:CONFIG: Pythonic responses are disabled
DEBUG:falconpy._auth_object._falcon_interface:OPERATION: oauth2AccessToken
DEBUG:falconpy._auth_object._falcon_interface:ENDPOINT: https://api.crowdstrike.com/oauth2/token (POST)
DEBUG:falconpy._auth_object._falcon_interface:HEADERS: {'User-Agent': 'crowdstrike-falconpy/1.4.4', 'CrowdStrike-SDK': 'crowdstrike-falconpy/1.4.4'}
DEBUG:falconpy._auth_object._falcon_interface:PARAMETERS: None
DEBUG:falconpy._auth_object._falcon_interface:BODY: None
DEBUG:falconpy._auth_object._falcon_interface:DATA: {'client_id': 'REDACTED', 'client_secret': 'REDACTED'}
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): api.crowdstrike.com:443
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 intel_search.py -h

CrowdStrike Falcon Intel API search example using the FalconPy library.

usage: intel_search.py [-h] -f FIND -k CLIENT_ID -s CLIENT_SECRET [-r] [-t TYPES] [-tf TABLE_FORMAT]
                       [-o OUTPUT_PREFIX] [-d]

CrowdStrike Falcon Intel API search example using the FalconPy library.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |   Falcon Intelligence
`-------'                         `-------'

This sample searches Falcon Intelligence for all actor,
indicator or report matches to a specified string.

If only one result is returned for a category, full details
for the record are displayed.

A maximum of 50,000 results per category will be returned.

Creation date: 03.30.23 - jshcodes@CrowdStrike

This application requires:
    pyfiglet
    termcolor
    tabulate
    crowdstrike-falconpy v1.3.0+

options:
  -h, --help            show this help message and exit
  -r, --reverse         Reverse the sort.
  -t TYPES, --types TYPES
                        Types to search (indicator, report or actor). Comma delimited.
  -tf TABLE_FORMAT, --table_format TABLE_FORMAT
                        Set the table format.
  -o OUTPUT_PREFIX, --output_prefix OUTPUT_PREFIX
                        Output filename prefix for storing results (CSV format).
  -d, --debug           Enable API debugging

required arguments:
  -f FIND, --find FIND  Search string to identify
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike API client secret

For a list of table formats check this page: https://github.com/astanin/python-tabulate#table-format
```

### Example source code
The source code for this example can be found [here](intel_search.py).
