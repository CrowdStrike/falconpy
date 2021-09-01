![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)
![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# My Little RTR
### Using Real Time Response to retrieve basic system information

This example leverages an open-source project that retrieves system information to pull details for a specific host attached to your CID. In order to retrieve system information detail (and draw ponies), this example installs __git__ (when not present) and then clones the [ASCII-Pony](https://gitlab.com/mattia.basaglia/ASCII-Pony) repo. Once successfully cloned, the executable _systempony_ is executed with its output being saved to a local file. Finally, the contents of this output file are retrieved and all artifacts are removed from the target system.

### Example output
```bash
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
7. The `cleanup-pony` command is executed, all artificts are removed from the target system.
> If any of these commands fail on execution, the procedure will be halted.
8. All three uploaded 'pony' scripts are removed from CrowdStrike cloud.
9. The Real Time Response session is closed and deleted.
10. The results of our _systempony_ command are displayed.

## Example source code
The source code for this example can be found [here](my_little_rtr.py).

## The open-source system information project - ASCII-Pony
<table>
<tr>
<td align="center">![Glax](https://raw.githubusercontent.com/CrowdStrike/falconpy/sep21-docs-samples/docs/asset/glax.png)</td></tr></table>
The [ASCII-Pony](https://gitlab.com/mattia.basaglia/ASCII-Pony) repo was developed by [Mattia "Glax" Basaglia](https://dragon.best/), and has been around for many years. It is a fun (and useful) project [@jshcodes](https://github.com/jshcodes) has used in several places over time. Glax is best Dragon!
