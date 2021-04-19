# Installation, Upgrades and Removal

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Installation, Upgrades & Removal

![PyPI - Status](https://img.shields.io/pypi/status/crowdstrike-falconpy) ![PyPI](https://img.shields.io/pypi/v/crowdstrike-falconpy) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/crowdstrike-falconpy) ![PyPI - Downloads](https://img.shields.io/pypi/dm/crowdstrike-falconpy) ![CI Tests](https://github.com/CrowdStrike/falconpy/workflows/Python%20package/badge.svg)  
 FalconPy leverages the Python Package Index for distribution, making installation and maintenance easy.

### Installing the stable release

Stable releases of FalconPy are available on the Python Package Index and are the default installation option:

```text
python3 -m pip install crowdstrike-falconpy
```

You may also call `pip3` directly to perform an installation:

```text
pip3 install crowdstrike-falconpy
```

### Installing the Bleeding Edge version

If you'd like to try the _absolute bleeding edge_, an automated GitHub action releases a test package with every merged pull request that has the string `[DEPLOY]` in the head of the commit.

To install this Bleeding Edge \(development\) version, you will need to use the _PyPI test index_:

```text
python3 -m pip install -i https://test.pypi.org/simple crowdstrike-falconpy
```

or:

```text
pip3 install -i https://test.pypi.org/simple crowdstrike-falconpy
```

### Upgrading

Upgrading the package to the latest stable release follows a similar pattern:

```text
python3 -m pip install crowdstrike-falconpy --upgrade
```

or:

```text
pip3 install crowdstrike-falconpy --upgrade
```

### Upgrading to the Bleeding Edge version

To upgrade to the Bleeding Edge version you can use the following command:

```text
python3 -m pip install -i https://test.pypi.org/simple crowdstrike-falconpy --upgrade
```

or:

```text
pip3 install -i https://test.pypi.org/simple crowdstrike-falconpy --upgrade
```

### Uninstalling and removing the package

To uninstall and remove the FalconPy package entirely:

```text
python3 -m pip uninstall crowdstrike-falconpy
```

or:

```text
pip3 uninstall crowdstrike-falconpy
```

> Please note: This will uninstall whichever version of FalconPy you have installed, bleeding edge or stable.

