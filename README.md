![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)<br/>

# FalconPy - The CrowdStrike Falcon SDK for Python

[![Package Status](https://img.shields.io/pypi/status/crowdstrike-falconpy?label=package%20status)](https://pypi.org/project/crowdstrike-falconpy/)
[![PyPI](https://img.shields.io/pypi/v/crowdstrike-falconpy?label=current%20version)](https://pypi.org/project/crowdstrike-falconpy/#history)
[![Release date](https://img.shields.io/github/release-date/CrowdStrike/falconpy)](https://github.com/CrowdStrike/falconpy/releases)
[![Repo status](https://img.shields.io/osslifecycle/crowdstrike/falconpy?label=repo%20status)](https://github.com/CrowdStrike/falconpy/graphs/code-frequency)
[![Commit activity](https://img.shields.io/github/commits-since/CrowdStrike/falconpy/latest)](https://github.com/CrowdStrike/falconpy/commits/main)
![GitHub forks](https://img.shields.io/github/forks/crowdstrike/falconpy)

The FalconPy SDK contains a collection of Python classes that abstract CrowdStrike Falcon OAuth2 API interaction, removing duplicative code and allowing developers to focus on just the logic of their solution requirements.

+ [Overview](#overview-)
+ [Quick Start](#quick-start-)
+ [Documentation and Support](#documentation-and-support-)
+ [Contribute to FalconPy](#contribute-to-falconpy-)

## Overview 🔎
There are many CrowdStrike Falcon API [service collections](https://www.falconpy.io/Operations/Operations-by-Collection.html) collectively containing hundreds of [individual operations](https://www.falconpy.io/Operations/All-Operations.html), all of which are accessible to your project via FalconPy.

The CrowdStrike Falcon SDK for Python completely abstracts token management, while also supporting interaction with all CrowdStrike regions, custom connection and response timeouts, routing requests through a list of proxies, disabling SSL verification, and custom header configuration.

> If the CrowdStrike APIs were rings of great power, that the Dark Lord Sauron gifted to the kings of dwarves, elves and men, then CrowdStrike's FalconPy would be the One Ring.
> 
> _"One SDK to rule them all, One SDK to find them, One SDK to bring them all and in the darkness bind them."_

[![Downloads](https://static.pepy.tech/personalized-badge/crowdstrike-falconpy?left_text=package%20installs/month&left_color=grey&right_color=blue&period=month)](https://pepy.tech/project/crowdstrike-falconpy)
[![Development Installs](https://static.pepy.tech/personalized-badge/crowdstrike-falconpy-dev?left_text=development%20package%20installs/month&left_color=grey&right_color=blue&period=month)](https://pepy.tech/project/crowdstrike-falconpy-dev)

#### Supported versions of Python
The CrowdStrike Falcon SDK for Python was developed for Python 3. Current versions of FalconPy provide support for Python versions `3.7` - `3.12`. Every commit to the FalconPy code base is unit tested for functionality using all versions of Python the library currently supports.

> [!NOTE]
> Developers working with Python version `3.6` will need to leverage versions of FalconPy less than `1.4.0`.

[![PyPI - Implementation](https://img.shields.io/pypi/implementation/crowdstrike-falconpy)](https://pypi.org/project/crowdstrike-falconpy/#files)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/crowdstrike-falconpy)](https://pypi.org/project/crowdstrike-falconpy/#files)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/crowdstrike-falconpy?label=supported%20versions)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_ubuntu.yml)

#### Supported Operating Systems
The FalconPy SDK is unit tested on the following operating systems.

[![macOS](https://img.shields.io/badge/-macOS-silver?logo=apple&style=for-the-badge&labelColor=gray)](https://www.apple.com/macos/)
[![Ubuntu](https://img.shields.io/badge/-Ubuntu-964?logo=ubuntu&style=for-the-badge&labelColor=tan)](https://ubuntu.com/)
[![Windows](https://img.shields.io/badge/-Windows-blue?logo=windows&style=for-the-badge&labelColor=darkblue)](https://www.microsoft.com/en-us/windows/)

FalconPy will also run on any of the following operating systems.

[![Amazon Linux](https://img.shields.io/badge/-Amazon-darkgreen?logo=amazon&style=for-the-badge&labelColor=teal)](https://aws.amazon.com/amazon-linux-ami/)
[![CentOS](https://img.shields.io/badge/-CentOS-magenta?logo=centos&style=for-the-badge&labelColor=purple)](https://www.centos.org/)
[![Fedora](https://img.shields.io/badge/-Fedora-teal?logo=fedora&style=for-the-badge&labelColor=darkblue)](https://getfedora.org/)
[![RedHat](https://img.shields.io/badge/-RedHat-red?logo=redhat&style=for-the-badge&labelColor=maroon)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)
[![Arch](https://img.shields.io/badge/-Arch-darkgray?logo=archlinux&style=for-the-badge&labelColor=gray)](https://archlinux.org/)

[![Debian](https://img.shields.io/badge/-Debian-darkred?logo=debian&style=for-the-badge&labelColor=red)](https://www.debian.org/)
[![Kali](https://img.shields.io/badge/-Kali-gray?logo=kalilinux&logoColor=red&style=for-the-badge&labelColor=black)](https://www.kali.org/)
[![Pop! OS](https://img.shields.io/badge/-Pop!%20OS-orange?logo=popos&logoColor=black&style=for-the-badge&labelColor=yellow)](https://pop.system76.com/)
[![SUSE](https://img.shields.io/badge/-SUSE-yellow?logo=suse&style=for-the-badge&labelColor=orange)](https://www.suse.com/)
[![openSUSE](https://img.shields.io/badge/-openSUSE-orange?logo=opensuse&style=for-the-badge&labelColor=darkorange)](https://www.opensuse.org/)

Details regarding supported operating systems and Python versions, and project security and testing procedures can be found [here](https://github.com/CrowdStrike/falconpy/blob/main/SECURITY.md).

### Components
The FalconPy SDK provides two distinct methods for interacting with CrowdStrike's API. 

| **[Service Classes](#service-classes)** | **[The Uber Class](#the-uber-class)** |
| :-- | :-- |
| <BR/>[![Service Classes](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/service-class-relationships.png)](#service-classes) | [![The Uber Class](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/uber-class-relationships.png)](#the-uber-class) | 
| Each Service Class represents a single CrowdStrike API service collection providing an interface to the [operations available](https://www.falconpy.io/Operations/Operations-by-Collection.html) within that service collection.| An all-in-one class that provides a singular interface for [all operations](https://www.falconpy.io/Operations/All-Operations.html) in every CrowdStrike API service collection. |


### Service Classes
Representing a single CrowdStrike Falcon API service collection, each Service Class has a method defined for [every operation available](https://www.falconpy.io/Operations/Operations-by-Collection.html) within that service collection.

#### Available Service Classes
For each CrowdStrike Falcon API service collection, a matching Service Class is available in the FalconPy library. For a complete list of service collections and their related Service Class, please review the [Operations by Collection](https://www.falconpy.io/Operations/Operations-by-Collection.html) page on [falconpy.io](https://falconpy.io).


#### Service Class benefits

- Closely follows Python and OpenAPI best practice for code style and syntax. PEP-8 compliant.
- Completely abstracts token management, automatically refreshing your token when it expires.
- Provides simple programmatic patterns for interacting with CrowdStrike Falcon APIs.
- Supports [cloud region autodiscovery](https://www.falconpy.io/Usage/Environment-Configuration.html#cloud-region-autodiscovery) for the CrowdStrike `US-1`, `US-2` and `EU-1` regions.
- Supports dynamic [configuration](https://www.falconpy.io/Usage/Environment-Configuration.html) based upon the needs of your environment.
- Supports CrowdStrike Falcon API [parameter abstraction](https://www.falconpy.io/Usage/Payload-Handling.html#parameter-abstraction) functionality.
- Supports CrowdStrike Falcon API [body payload abstraction](https://www.falconpy.io/Usage/Payload-Handling.html#body-payload-abstraction) functionality.

### The Uber Class
Operating as a single harness for interacting with the entire CrowdStrike Falcon API, the _Uber Class_ can access [every available operation](https://www.falconpy.io/Operations/All-Operations.html) within [every API service collection](https://www.falconpy.io/Operations/Operations-by-Collection.html).


#### Uber Class benefits

- Access every CrowdStrike Falcon API service collection with only one import and only one class.
- Completely abstracts token management, automatically refreshing your token when it expires.
- Interact with newly released API operations not yet available in the library via the [`override`](https://www.falconpy.io/Usage/Basic-Uber-Class-usage.html#the-command-method) keyword.
- Provides simple programmatic patterns for interacting with CrowdStrike Falcon APIs.
- Supports [cloud region autodiscovery](https://www.falconpy.io/Usage/Environment-Configuration.html#cloud-region-autodiscovery) for the CrowdStrike `US-1`, `US-2` and `EU-1` regions.
- Supports CrowdStrike Falcon API [parameter abstraction](https://www.falconpy.io/Usage/Payload-Handling.html#parameter-abstraction) functionality.
- Supports all [environment configuration](https://www.falconpy.io/Usage/Environment-Configuration.html) options supported by FalconPy Service Classes.


### Comparing FalconPy class types
While the [usage syntax](https://www.falconpy.io/Usage/Basic-Uber-Class-usage.html) varies slightly, the Uber Class provides the same performance and [output](https://www.falconpy.io/Usage/Response-Handling.html) as FalconPy Service Classes, and can perform all of the same [operations](https://www.falconpy.io/Operations/All-Operations.html). The Uber Class does **not** support [body payload abstraction](https://www.falconpy.io/Usage/Payload-Handling.html#body-payload-abstraction).


<img width="1" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==">

![CrowdStrike Divider](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-lineup-1.png)


## Quick Start 💫

Stable releases of FalconPy are available on the Python Package Index. In a terminal, execute the following command:

```shell
python3 -m pip install crowdstrike-falconpy
```

Once installed, you can immediately begin using CrowdStrike functionality in your Python projects.

```python
"""CrowdStrike FalconPy Quick Start."""
import os
from falconpy import Hosts

# Use the API Clients and Keys page within your Falcon console to generate credentials.
# You will need to assign the Hosts: READ scope to your client to run this example.

# CrowdStrike does not recommend you hardcode credentials within source code.
# Instead, provide these values as variables that are retrieved from the environment,
# read from an encrypted file or secrets store, provided at runtime, etc.
# This example retrieves credentials from the environment as the variables
# "FALCON_CLIENT_ID" and "FALCON_CLIENT_SECRET".

hosts = Hosts(client_id=os.getenv("FALCON_CLIENT_ID"),
              client_secret=os.getenv("FALCON_CLIENT_SECRET")
              )

SEARCH_FILTER = "hostname-search-string"

# Retrieve a list of hosts that have a hostname that matches our search filter
hosts_search_result = hosts.query_devices_by_filter(filter=f"hostname:*'*{SEARCH_FILTER}*'")

# Confirm we received a success response back from the CrowdStrike API
if hosts_search_result["status_code"] == 200:
    hosts_found = hosts_search_result["body"]["resources"]
    # Confirm our search produced results
    if hosts_found:
        # Retrieve the details for all matches
        hosts_detail = hosts.get_device_details(ids=hosts_found)["body"]["resources"]
        for detail in hosts_detail:
            # Display the AID and hostname for this match
            aid = detail["device_id"]
            hostname = detail["hostname"]
            print(f"{hostname} ({aid})")
    else:
        print("No hosts found matching that hostname within your Falcon tenant.")
else:
    # Retrieve the details of the error response
    error_detail = hosts_search_result["body"]["errors"]
    for error in error_detail:
        # Display the API error detail
        error_code = error["code"]
        error_message = error["message"]
        print(f"[Error {error_code}] {error_message}")
```

### More samples
If you are interested in reviewing more examples of FalconPy usage, this repository also maintains a collection of [samples](https://github.com/CrowdStrike/falconpy/tree/main/samples) to help get you started with integrating CrowdStrike Falcon into your DevOps processes.

## Documentation and Support 📖
FalconPy is a community-driven, open source project designed to assist developers in leveraging the power of CrowdStrike APIs within their solutions. While not a formal CrowdStrike product, FalconPy is maintained by CrowdStrike and supported in partnership with the open source developer community.

### Official Project Documentation: [falconpy.io](https://falconpy.io)

[![Website](https://img.shields.io/website?down_color=lightgrey&down_message=offline&label=falconpy.io&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABIAAAAOCAYAAAAi2ky3AAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TpaIVBzuIOGSoDmJBVEQ3rUIRKoRaoVUHk5f%2BCE0akhQXR8G14ODPYtXBxVlXB1dBEPwBcXNzUnSREu9LCi1ifPB4H%2Be9c7jvXkColZhmtY0Cmm6bqURczGRXxNAruhAEMI1hmVnGrCQl4bu%2B7hHg512MZ%2Fm%2F%2B3N1qzmLAQGReIYZpk28Tjy5aRuc94kjrCirxOfEIyYVSPzIdcXjN84FlwWeGTHTqTniCLFYaGGlhVnR1IgniKOqplO%2BkPFY5bzFWStVWKNO%2FsNwTl9e4jrtASSwgEVIEKGggg2UYCNGp06KhRTdx338%2Fa5fIpdCrg0wcsyjDA2y6wefwe%2FeWvnxMS8pHAfaXxznYxAI7QL1quN8HztO%2FQQIPgNXetNfrgFTn6RXm1r0COjZBi6um5qyB1zuAH1PhmzKrsTnL%2BTzwPsZjSkL9N4Cnate3xr3OH0A0tSr5A1wcAgMFSh7zeffHa19%2B%2FdNo38%2Fhq9yr%2BiELI0AAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQflDAsTByz7Va2cAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAYBJREFUKM%2BlkjFIlVEYht%2Fzn3sFkYYUyUnIRcemhCtCU6JQOLiIU%2BQeJEQg6BBIm0s4RBCBLjq5OEvgJC1uOniJhivesLx17%2F97%2FvO9b4NK4g25157hfHCGB773%2FcA0HZIEAKiMj%2BLWiOxljG%2Fi96pnCFP58XHnrWX2%2B9cj0dYl9Yu2FE9%2F9rXrcAAgs2eSyiBfOe%2FXRD503h%2FCuffOubQVUXL%2BJh9BllzBbyJJBgDclVkO4Kukd8zzkXJbeUljIldFTstsmSHM6S81ma2KfPKlFdkGAMY4wzx%2FbbXapMy21My%2BYizdKNq5mDzLkrxafSxySFKjSWX2oTmjKzz4vN0r2lOFcL%2FQ3V0%2FmX95ILMXTTGYVfaut%2FaP2%2BoCMAvnZgCcsF5fcR0dg65YHAdwB%2BQApADvu0AuOe%2FftlJAD7Nsgmm6yBjDtfWORJZlNtFyo%2FlR5Z7MyheKA5ktSur7sTAHazSG27pehjAiaVfkN8b4XFIJ%2FwOzbOx07VNRUuHy7w98CzCcGPyWywAAAABJRU5ErkJggg%3D%3D&up_color=green&up_message=online&url=https%3A%2F%2Ffalconpy.io)](https://falconpy.io)
![Documentation Version](https://img.shields.io/endpoint?url=https%3A%2F%2Ffalconpy.io%2F_version.json&label=documentation%20version)

Extended documentation is also available via the [wiki](https://github.com/CrowdStrike/falconpy/wiki) for this repository.

### Issues and Questions

Is something going wrong? 🔥

GitHub Issues are used to report bugs and errors.

[![Report Issue](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/report-issue.png)](https://github.com/CrowdStrike/falconpy/issues/new/choose)

Have a question you can't find answered in the documentation?

Please submit usage questions to the Q&A section of our discussion board.

[![Discussions](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/ask-a-question.png)](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A)

### Community forums

The discussion board for this repository also provides the community with means to communicate regarding [enhancements ideas](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AIdeas), [integration examples](https://github.com/CrowdStrike/falconpy/discussions/496) and [new releases](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3A%22Show+and+tell%22).

[![Discussions](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/join-the-discussion.png)](https://github.com/CrowdStrike/falconpy/discussions)

> More information regarding FalconPy documentation and support can be found [here](https://github.com/CrowdStrike/falconpy/blob/main/SUPPORT.md).


## Contribute to FalconPy ☕
Interested in [being acknowledged](https://github.com/CrowdStrike/falconpy/blob/main/AUTHORS.md#contributors) as a member of an elite community of security-focused Python developers that **stop breaches**? 

There are *many* ways you can contribute to the FalconPy project! 

- _Providing feedback_ by opening a GitHub ticket. Even a fly-by "hey, this worked..." is appreciated and helps validate approaches. Ideas on improving the project are most welcome.
- _Documenting, blogging, or creating videos_, of how you've used FalconPy. This type of content is *invaluable* and helps our community grow. Post these in the [Show and Tell](https://github.com/CrowdStrike/falconpy/discussions/categories/show-and-tell) category of our [discussion board](https://github.com/CrowdStrike/falconpy/discussions).
- _Submit a sample_ demonstrating how you're using FalconPy by opening a pull request for inclusion in the [Samples Library](https://github.com/CrowdStrike/falconpy/tree/main/samples).
- _Fix a bug or implement a new feature_. Check out our [open issues on GitHub](https://github.com/CrowdStrike/falconpy/issues) or our [discussion board](https://github.com/CrowdStrike/falconpy/discussions) for inspiration.
- _Review pull requests_ by going through the queue of [open pull requests on GitHub](https://github.com/CrowdStrike/falconpy/pulls) and giving feedback to the authors.

To get started, review the [Code of Conduct](https://github.com/CrowdStrike/falconpy/blob/main/CODE_OF_CONDUCT.md) for community guidelines, and the [contribution guide](https://github.com/CrowdStrike/falconpy/blob/main/CONTRIBUTING.md) for more detail regarding contributing to the CrowdStrike FalconPy project.


---


<p align="center"><img src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-footer.png"><BR/><img width="250px" src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-red-eyes.png"></P>
<h3><P align="center">WE STOP BREACHES</P></h3>
