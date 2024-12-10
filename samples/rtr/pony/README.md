![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# My Little RTR
### Using Real Time Response to retrieve basic system information

This example leverages an open-source project that retrieves system information to pull details for a specific host attached to your CID. In order to retrieve system information detail (and draw ponies), this example installs __git__ (when not present) and then clones the [ASCII-Pony](https://gitlab.com/mattia.basaglia/ASCII-Pony) repo. Once successfully cloned, the executable _systempony_ is executed with its output being saved to a local file. Finally, the contents of this output file are retrieved and all artifacts are removed from the target system. The pony that is displayed is selected at random (the example can be configured to display a specific pony if desired).

> This example requires FalconPy v0.6.0+

### Example output
```shell
                                                .....-----...
                                         __  .-`             `.
                                        /  \`             .:'--:.
                                       ( /  \               `-.__..-;
                                       | |   `-..__  .,            -
                                       ( '.  \ ____`\ )`-._     _-`
                                       '\   __/   __\' / `:``''`
                                       .|\_  (   / .-| |'.|           User     : root
                                       |' / ,'\ ( (WW| \W)j           Hostname : sample-host.us-west-1.compute.internal
                                      .|  |    \_\_`/   ``-.          IP       :
            .--''''````-.             |'  l            \__/           Distro   :
           /             `.           |    `.  -,______.-'            Kernel   : 4.14.232-177.418.amzn2.x86_64 x86_64
          /                `.________.|      `.   /                   Uptime   : 48 days, 2:50
         (         ,.--''>-',:       |'        | (                    Load     : 0.00, 0.00, 0.00
         |        |     /   (_)     .|        ,'),-``''-.             Shell    : /bin/bash
         |       .'    | ,;         |'       / ,'        `.           Packages :
        .|       |.    | (_)  ;,    '.      (.(            :          RAM      : 237M / 1.9G
        |'       '|    |     (_)      `'---'`  `.       `:`;          CPU      : Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
        |         '.  / \        /           `:. ;        ':          Swap     : 0B / 0B
        |.          `.   |      /-,_______\   ' `     .-;  |          Disk     : 1.8G / 13G
        '|            \_/      /     |    |\   `----'`.' .'
         |             )      /     |     | `--,    \`''`
         '.           /      |      |     |   /      )
           `--_____--'|      |      |      | (       |
      `:._.`       '. |      |      |      |  \      |
       '        .-.  )|       \     |       \  `.___/
        `---;    ) )'  \_______)     \_______)
          .:___-'
```

## Procedure
1. The AID for the provided hostname is retrieved.
    - If not found, the routine will stop at this point.
2. A Real Time Response session is initialized between your host and the target host.
    - If a session cannot be instantiated, the routine will stop processing.
3. Three scripts are uploaded to CrowdStrike cloud for execution:
    - `install-pony` - Installs git and clones the ASCII-Pony repo.
    - `create-pony` - Executes the _systempony_ command and saves the output to a file in /root.
    - `cleanup-pony` - Removes the results of the _systempony_ command and removes the cloned ASCII-Pony repo.
4. The `install-pony` command is executed and the repo is cloned.
5. The `create-pony` command is executed and the system information output file is generated.
6. A stand-alone command, `retrieve-pony` is executed. 

    **Command contents**
    ```bash
    cat ~/pony.txt
    ```
    - The results of this command are temporarily stored in memory.
7. The `cleanup-pony` command is executed, all artifacts are removed from the target system.
> If any of these commands fail on execution, the procedure will be halted.
8. All three uploaded 'pony' scripts are removed from CrowdStrike cloud.
9. The Real Time Response session is closed and deleted.
10. The results of our _systempony_ command are displayed.

## Running the program
In order to run this demonstration, you will need a partial hostname for the target system and access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Real Time Response | __READ__, __WRITE__ |
| Real Time Response Admin | __READ__, __WRITE__ |

### Execution syntax
The following command should execute the demonstration in your environment.

```shell
python3 my_little_rtr.py -t TARGET_HOSTNAME -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET
```

A small command-line syntax help utility is available using the `-h` flag.

```shell
% python3 my_little_rtr.py -h
usage: my_little_rtr.py [-h] -t TARGET -k KEY -s SECRET

 ⠴⢮⠭⠍⠉⠉⠒⠤⣀
⢀⢊　　　　　　 ⢱⠊⠑⡀
⠋⡎  ⣀⡠⠤⠠⠖⠋⢉⠉  ⡄⢸
⣘⡠⠊⣩⡅  ⣴⡟⣯⠙⣊  ⢁⠜   The My Little RTR demo
　　 ⣿⡇⢸⣿⣷⡿⢀⠇⢀⢎          FalconPy v0.6.0+
　 ⠰⡉  ⠈⠛⠛⠋⠁⢀⠜ ⢂
　 　 ⠈⠒⠒⡲⠂⣠⣔⠁   ⡇  ⢀⡴⣾⣛⡛⠻⣦
　　　　⢠⠃  ⢠⠞    ⡸⠉⠲⣿⠿⢿⣿⣿⣷⡌⢷
   ⢀⠔⠂⢼    ⡎⡔⡄⠰⠃      ⢣  ⢻⣿⣿⣿⠘⣷
 ⡐⠁    ⠸⡀  ⠏  ⠈⠃      ⢸　 ⣿⣿⣿⡇⣿⡇
 ⡇    ⡎⠉⠉⢳    ⡤⠤⡤⠲⡀   ⢇   ⣿⣿⣿⣇⣿⣷
 ⡇  ⡠⠃    ⡸    ⡇ ⡇ ⢱⡀ ⢣   ⠙⣿⣿⣿⣿⣿⡄
 ⠑⠊ 　 　⢰　   ⠇⢸  ⡇⡇ ⡇    ⢳⣿⣿⣿⣿⡇
　　　　⢠⠃    ⡸⡎  ⡜⡇  ⡇     ⠻⡏⠻⣿⣿⣄
　　　 ⣔⣁⣀⣀⡠⠁ ⠈⠉⠉⠁⣎⣀⣀⡸

   CrowdStrike - We STOP Breaches

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Hostname of your target.
                        Must be part of your CID.
  -k KEY, --key KEY     Your CrowdStrike API key ID
                             Required Scopes
                             Hosts:     READ
                             RTR:       WRITE
                             RTR Admin: WRITE
  -s SECRET, --secret SECRET
                        Your CrowdStrike API key secret
```

## Example source code
The source code for this example can be found [here](my_little_rtr.py).

## The open-source system information project - ASCII-Pony
<table><tr>
<td align="center"><img src="../../../docs/asset/glax.png" width="200"></td>
<td align="left">
The <a href="https://gitlab.com/mattia.basaglia/ASCII-Pony">ASCII-Pony</a> repo was developed by <a href="https://dragon.best/">Mattia "Glax" Basaglia</a>, and has been around for many years. It is a fun (and useful) project <a href="https://github.com/jshcodes">@jshcodes</a> has used in several places over time.<BR/><BR/>Glax is best Dragon!
</td>
</tr></table>
