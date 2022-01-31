![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)<br/>[![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)<br/>

# Utilities
These utilities are meant to assist developers working on FalconPy, the CrowdStrike SDK for Python.

## Inventory
All of these utilities are designed to be executed from within the parent folder.

| File | Purpose |
| :--- | :--- |
| `coverage.config` | Configuration settings for coverage.py integration. |
| `create-lambda-layer.sh` | Leverages docker to create a ZIP archive of FalconPy to be used as an AWS lambda layer. A modified version of this utility is used to generate the download available on [falconpy.io](https://falconpy.io/downloads/falconpy-layer.zip). |
| `debug.sh` | Starts the FalconPy interactive debugger. Execute this from the main directory. Example: `util/debug.sh` |
| `docstyle.sh` | Lints the package docstrings using `pydocstyle` and returns the result. |
| `lint.sh` | Lints the package source with `flake8` and `pylint` and returns the result. |
| `run-tests.sh` | Runs a complete unit test series, reports code coverage and runs a bandit analysis. |
| `unit-test.sh` | Runs a single unit test series and reports code coverage. Execute individual tests by specifying their module name. Example: `util/unit-test.sh real_time_response` |

## Discussion forums
Our community maintains a discussion board for interacting about FalconPy usage and for handling questions.  This content is labeled by API and fully searchable.

[![Discussions](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/join-the-discussion.png)](https://github.com/CrowdStrike/falconpy/discussions)

## Issues
Think perhaps the error your receiving is a [bug](https://github.com/CrowdStrike/falconpy/issues?q=is%3Aissue+label%3A%22bug+%3Abug%3A%22+) within FalconPy? 

Have you found a piece of documentation that is [incorrect](https://github.com/CrowdStrike/falconpy/issues?q=is%3Aissue+label%3A%22documentation+%3Abook%3A%22), [missing](https://github.com/CrowdStrike/falconpy/issues?q=is%3Aissue+label%3A%22documentation+%3Abook%3A%22), or pointing to a [broken link](https://github.com/CrowdStrike/falconpy/issues?q=is%3Aissue+label%3A%22broken+link+%3Alink%3A%22)?

Please let us know by [submitting an issue](https://github.com/CrowdStrike/falconpy/issues/new/choose)!

[![Report Issue](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/report-issue.png)](https://github.com/CrowdStrike/falconpy/issues/new/choose)


---


<p align="center"><img src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-footer.png"><BR/><img width="350px" src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-jackal.png"></P>
<h3><P align="center">WE STOP BREACHES</P></h3>
