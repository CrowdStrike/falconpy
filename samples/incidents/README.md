![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)
![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# Incidents examples
The examples in this folder focus on leveraging CrowdStrike's Incidents API.
- [CrowdScore QuickChart](#chart-your-crowdscore-for-the-past-day)

## Chart your CrowdScore for the past day
This example demonstrates retrieving CrowdScore detail and then charting it a simple histogram.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Incidents | __READ__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose | Category |
| :--- | :--- | :--- |
|  `-h`, `--help` | Show help message and exit | optional |
| `-c`, `--hide-chart` | Hides the chart display | optional |
| `-d`, `--show-data` | Shows the data table display | optional |
| `-r`, `--reverse` | Reverse the data table sort<BR/>Will not impact chart display | optional |
| `-n`, `--no-color` | Disable color output | optional |
| `-x` CHART_SIZE,<BR/>`--chart-size` CHART_SIZE | Size of the chart to display (Max: 100, Default: 25) | optional |
| `-m` MAX_ROWS,<BR/>`--max-rows` MAX_ROWS | Maximum number of rows to return (5 - 250, Default: 100) | optional |
| `-b` BASE_URL,<BR/>`--base-url` BASE_URL | CrowdStrike cloud region. (auto or usgov1, Default: auto) | optional |
|  `-f` FALCON_CLIENT_ID,<BR/>`--falcon_client_id` FALCON_CLIENT_ID | Falcon Client ID | always required |
|  `-s` FALCON_CLIENT_SECRET,<BR/>`--falcon_client_secret` FALCON_CLIENT_SECRET | Falcon Client Secret | always required |

#### Examples
These examples demonstrate command line usage of this sample. Commands may be chained on the same command line as long as all actions make sense for the arguments provided.

- [Show command line help.](#show-command-line-help)
- [Show your current CrowdScore and plot the past 24 hours](#show-your-current-crowdscore-and-plot-the-past-24-hours)
- [Show the data table for the chart display](#show-the-data-table-for-the-chart-display)
- [Reverse the table sort](#reverse-the-table-sort)
- [Create a chart in the US-GOV-1 region](#create-a-chart-in-the-us-gov-1-region)
- [Increase the number of rows returned](#increase-the-number-of-rows-returned)
- [Increase the chart size](#increase-the-chart-size)
- [Disable color output](#disable-color-output)
- [Disable chart display](#disable-chart-display)



##### Show command line help.
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -h
```

[See output example](#command-line-help).

##### Show your current CrowdScore and plot the past 24 hours
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

###### Result
```shell
            _______                        __ _______                        __    _______
           |   _   .----.-----.--.--.--.--|  |   _   .----.-----.----.-----.|__|  |   _   |
           |.  1___|   _|  _  |  |  |  |  _  |   1___|  __|  _  |   _|  -__| __   |.  |   |
           |.  |___|__| |_____|________|_____|____   |____|_____|__| |_____||__|  |.  |   |
           |:  1   |                         |:  1   |                            |:  1   |
           |::.. . |                         |::.. . |                            |::.. . |
           `-------'                         `-------'                            `-------'


   72.00  ┼   ╭────────────────╮
   69.12  ┤   │                ╰──────────╮
   66.24  ┤   │                           ╰────╮
   63.36  ┤   │                                ╰──╮
   60.48  ┤  ╭╯                                   ╰─╮
   57.60  ┤  │                                      ╰──╮
   54.72  ┼──╯                                         ╰─╮
   51.84  ┤                                              ╰─╮
   48.96  ┤                                                ╰──╮
   46.08  ┤                                                   ╰─╮
   43.20  ┤                                                     ╰─╮
   40.32  ┤                                                       ╰─╮
   37.44  ┤                                                         ╰╮
   34.56  ┤                                                          ╰─╮
   31.68  ┤                                                            ╰─╮
   28.80  ┤                                                              ╰╮
   25.92  ┤                                                               ╰─╮
   23.04  ┤                                                                 ╰─╮
   20.16  ┤                                                                   ╰─╮
   17.28  ┤                                                                     ╰──╮
   14.40  ┤                                                                        ╰─╮
   11.52  ┤                                                                          ╰─╮
    8.64  ┤                                                                            ╰──╮
    5.76  ┤                                                                               ╰────╮
    2.88  ┤                                                                                    ╰──────╮
    0.00  ┤                                                                                           ╰───────
```

##### Show the data table for the chart display
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
```

##### Reverse the table sort
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r
```

##### Create a chart in the `US-GOV-1` region
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

##### Increase the number of rows returned
This argument has a range of 5 - 250.
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -m 200
```

##### Increase the chart size
This argument has a range of 5 - 100.
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -x 100
```

##### Disable color output
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n
```

##### Disable chart display
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c
```

#### Command-line help
Command-line help is available using the `-h` or `--help` parameters.

```shell
% python3 crowdscore_quickchart.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -h
usage: crowdscore_quickchart.py [-h] [-c] [-d] [-r] [-n] [-x CHART_SIZE] [-m MAX_ROWS] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET

CrowdScore QuickChart.

  ___   __ __  ____    __  __  _     __  __ __   ____  ____  ______
 /   \ |  T  Tl    j  /  ]|  l/ ]   /  ]|  T  T /    T|    \|      T
Y     Y|  |  | |  T  /  / |  ' /   /  / |  l  |Y  o  ||  D  )      |
|  Q  ||  |  | |  | /  /  |    \  /  /  |  _  ||     ||    /l_j  l_j
|     ||  :  | |  |/   \_ |     Y/   \_ |  |  ||  _  ||    \  |  |
l     |l     | j  l\     ||  .  |\     ||  |  ||  |  ||  .  Y |  |
 \__,_j \__,_j|____j\____jl__j\_j \____jl__j__jl__j__jl__j\_j l__j

                                                for your CrowdScore

Quickly displays your current CrowdScore and charts a histogram
of your score over the past 24 to 36 hours.

Requirements
  asciichartpy
  crowdstrike-falconpy
  pyfiglet
  tabulate

optional arguments:
  -h, --help            show this help message and exit
  -c, --hide-chart      Hides the chart display
  -d, --show-data       Shows the data table display
  -r, --reverse         Reverse the data table sort
                        Will not impact chart display
  -n, --no-color        Disable color output
  -x CHART_SIZE, --chart-size CHART_SIZE
                        Size of the chart to display (Max: 100, Default: 25)
  -m MAX_ROWS, --max-rows MAX_ROWS
                        Maximum number of rows to return (5 - 250, Default: 100)
  -b BASE_URL, --base-url BASE_URL
                        CrowdStrike cloud region. (auto or usgov1, Default: auto)

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Search string
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Search string
```

### Example source code
The source code for this example can be found [here](crowdscore_quickchart.py).
