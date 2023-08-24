![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Utilities
These scripts are meant to assist developers working on FalconPy, the CrowdStrike Falcon SDK for Python, and are mostly focused on automating tasks that have to be performed consistently.

## Inventory
All of these utilities are designed to be executed from within the repository root folder, but several include functionality allowing for passing this location instead.

| File | Purpose |
| :--- | :--- |
| `babel_fish.py` | Lists all available operations, their HTTP method, endpoint and service collection. Can search for a specific string across all four columns. Must be run from the `src` folder or you must have FalconPy available within your environment. (Python application) |
| `coverage.config` | Configuration settings for coverage.py integration. |
| `create-lambda-layer.sh` | Leverages docker to create a ZIP archive of FalconPy to be used as an AWS lambda layer. A modified version of this utility is used to generate the download available on [falconpy.io](https://falconpy.io/downloads/falconpy-layer.zip). |
| `debug.sh` | Starts the FalconPy interactive debugger. Execute this from the repository root directory.<BR/>Example: `util/debug.sh` |
| `docstyle.sh` | Lints the package docstrings using `pydocstyle` and returns the result.<BR/>Execute from the root of the repository: `util/docstyle.sh` |
| `find-strings.sh`<BR/><img width=300> | Search the code base for a string or list of strings. Returns module file name and line number for all matches. Run from within the root of the repository folder or pass the folder location as the second argument.<BR/>`find-strings.sh SEARCH1,SEARCH2 /path/to/repo/home` |
| `lint.sh` | Lints the package source with `flake8` and `pylint` and returns the result. Execute from the root of the repository or pass the location you wish to lint as the first argument: `util/lint.sh /path/to/folder` |
| `public-modules.sh` | Returns a list of all public FalconPy modules and the count of their available methods. Execute from the root of the repository folder or pass this location as the first argument.<BR/>`public-modules.sh /path/to/repo/home`
| `run-tests.sh` | Runs a complete unit test series, reports code coverage and runs a bandit analysis.<BR/>Should be executed from the repository root: `util/run-tests.sh` |
| `unit-test.sh` | Runs a single unit test series and reports code coverage. Execute individual tests by specifying their module name. Example: `util/unit-test.sh real_time_response` |
| `vcheck.sh` | Checks your installed version of FalconPy against the latest release version.<BR/>Will attempt to detect `Pipenv` / `Poetry`.<BR/>Can be executed locally (`util/vcheck.sh`) or online with:<BR/>`curl https://falconpy.io/vcheck --silent \| bash` |

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
