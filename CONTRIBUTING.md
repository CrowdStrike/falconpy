![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

[![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

# Contributing to this repository <!-- omit in toc -->

## Getting started <!-- omit in toc -->
_Welcome!_ We're excited you want to take part in the FalconPy community! 

Please review this document for details regarding getting started with your first contribution, packages you'll need to install as a developer, and our Pull Request process. If you have any questions, please let us know by
posting your question in the [discussion board](https://github.com/CrowdStrike/falconpy/discussions).

### Before you begin
- Have you read the [Code of Conduct](CODE_OF_CONDUCT.md)? The Code of Conduct helps us establish community norms and how they'll be enforced.

### Table of Contents
- [How you can contribute](#how-you-can-contribute)
    + [Bug reporting](#bug-reporting-is-handled-using-githubs-issues)
    + [All other discussions](#githubs-discussion-board-is-used-for-questions-suggestions-and-feedback)
- [Pull Requests](#pull-requests)
    + [Contributor dependencies](#additional-contributor-package-requirements)
    + [Unit testing](#unit-testing--code-coverage)
    + [Linting](#linting)
    + [Breaking changes](#breaking-changes)
    + [Branch targeting](#branch-targeting)
- [Suggestions](#suggestions)

![Adversary Bust Museum](docs/asset/musee-des-origines.png)

## How you can contribute
- See something? Say something! Submit a [bug report](https://github.com/CrowdStrike/falconpy/issues) to let the community know what you've experienced or found. Bonus points if you suggest possible fixes or what you feel may resolve the issue. For example: "_Attempted to use the XZY API class but it errored out. Could a more descriptive error code be returned?_"
- Join the [discussion board](https://github.com/CrowdStrike/falconpy/discussions) where you can:
    - [Interact](https://github.com/CrowdStrike/falconpy/discussions/categories/general) with other members of the community
    - Suggest [new functionality](https://github.com/CrowdStrike/falconpy/discussions/categories/ideas)
    - Provide [feedback](https://github.com/CrowdStrike/falconpy/discussions/categories/q-a)
    - [Show others](https://github.com/CrowdStrike/falconpy/discussions/categories/show-and-tell) how you are using FalconPy today
- Submit a [Pull Request](#pull-requests)

### Bug reporting is handled using GitHub's issues
We use GitHub issues to track bugs. Report a bug by opening a [new issue](https://github.com/CrowdStrike/falconpy/issues).

### GitHub's discussion board is used for questions, suggestions and feedback.
We use GitHub's discussion board functionality to handling community discussions related to 
[questions](https://github.com/CrowdStrike/falconpy/discussions/categories/q-a), 
[feedback](https://github.com/CrowdStrike/falconpy/discussions/categories/general) 
or [functionality enhancements](https://github.com/CrowdStrike/falconpy/discussions/categories/ideas).

## Pull Requests

### All contributions will be submitted under the Unlicense license
When you submit code changes, your submissions are understood to be under the same Unlicense [license](LICENSE) that covers the project. 
If this is a concern, contact the maintainers before contributing.

### Additional contributor package requirements
`requirements-dev.txt` contains Python modules required for unit test development and for accessing the integrated debugger within FalconShell. Review this file's contents and install missing requirements as needed.

### Unit testing & Code coverage
+ All submitted code must also have an associated unit test that tests __all__ code paths within this new segment. (:100: percent coverage)
    - If the code submission is already covered by an existing unit test, additional unit tests are not required.
    - Please include coverage testing results in your Pull Request. (Example: [PR #67](https://github.com/CrowdStrike/falconpy/pull/67))
+ Unit testing is intended to prove out code formatting and functionality, not necessarily API functionality. Unit testing does not need to communicate with the API in order to provide the necessary coverage. 
+ We use bandit for static code analysis.
    - Please include bandit analysis results in the section provided in your Pull Request.
    - Pull Requests that produce alerts in bandit may be closed without merging.
+ All new contributions __must__ pass unit testing before they will be merged.
    - For scenarios where unit testing passes in the PR and fails post-merge, a maintainer will address the issue. If the problem is programmatic and related to code within the pull request, the merge may be reverted.
+ The util folder contains a BASH script, `run-tests.sh`, that contains the parameters used that match unit testing performed as part of our GitHub workflows.
> You can run all unit tests and perform a bandit analysis by executing the command `util/run-tests.sh` from the root of the project directory.

#### Posting coverage results to Pull Requests
Our Pull Request template provides an area for you to post the coverage results from your local unit tests. This table is generated by the command `coverage report` and is executed when you use the "run-tests.sh" BASH script found in the util folder. This table is output only when all unit tests have passed successfully, and is a required element for Pull Request approval.

##### Example coverage results
```shell
Name                                        Stmts   Miss  Cover
---------------------------------------------------------------
src/falconpy/__init__.py                       10      0   100%
src/falconpy/_endpoint.py                       1      0   100%
src/falconpy/_result.py                         8      0   100%
src/falconpy/_service_class.py                 31      0   100%
src/falconpy/_util.py                          80      0   100%
src/falconpy/_version.py                        8      0   100%
src/falconpy/api_complete.py                   77      0   100%
src/falconpy/cloud_connect_aws.py              66      0   100%
src/falconpy/cspm_registration.py             114      0   100%
src/falconpy/detects.py                        34      0   100%
src/falconpy/device_control_policies.py        67      0   100%
src/falconpy/event_streams.py                  15      0   100%
src/falconpy/falconx_sandbox.py                78      0   100%
src/falconpy/firewall_management.py           130      0   100%
src/falconpy/firewall_policies.py              68      0   100%
src/falconpy/host_group.py                     61      0   100%
src/falconpy/hosts.py                          37      0   100%
src/falconpy/incidents.py                      39      0   100%
src/falconpy/intel.py                          89      0   100%
src/falconpy/iocs.py                           58      0   100%
src/falconpy/oauth2.py                         30      0   100%
src/falconpy/prevention_policy.py              67      0   100%
src/falconpy/real_time_response.py            135      0   100%
src/falconpy/real_time_response_admin.py       82      0   100%
src/falconpy/sensor_update_policy.py          103      0   100%
src/falconpy/spotlight_vulnerabilities.py      15      0   100%
src/falconpy/user_management.py                75      0   100%
---------------------------------------------------------------
TOTAL                                        1578      0   100%
```

#### Posting bandit results to Pull Requests
Our Pull Request template provides an area for you to post the bandit analysis results from your local unit tests. This detail is generated by the command `bandit ...` and is executed when you run the "run-tests.sh" BASH script found in the util folder. These results are produced only when all unit tests have passed successfully, and are required for Pull Request approval.

##### Example bandit analysis results
```shell
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.9.2
Run started:2021-03-26 21:13:00.083912

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 6415
	Total lines skipped (#nosec): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
	Total issues (by confidence):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
Files skipped (0):
```

#### More details regarding PyTest, Coverage and Bandit
For more information regarding PyTest, and how we leverage it to perform unit testing, refer to the [PyTest documentation](https://docs.pytest.org/en/stable/contents.html#toc).

To find out more above Coverage, review their [website](https://coverage.readthedocs.io/en/coverage-5.5/).

To read more about bandit, you can visit [their documentation website](https://bandit.readthedocs.io/en/latest/). 

### Linting
All submitted code must meet minimum linting requirements. 
+ We use `flake8` and `pylint` for linting. 
+ All code that is included within the installation package must pass linting workflows when the Pull Request checks have completed.
    - You will be asked to correct linting errors before your Pull Request will be approved.
+ Unit tests do not need to meet this requirement, but try to keep linting errors to a minimum.
+ Samples are checked for linting, but failures will not stop builds at this time.
+ Refer to the `lint.sh` script within the util folder to review our standard linting parameters.
> You can quickly check the linting for all code within the src folder by executing the command `util/lint.sh` from the root of the project directory.

More information about flake8 can be found [here](https://flake8.pycqa.org/en/latest/).

More information about pylint can be found [here](https://www.pylint.org/).

### Breaking changes
In an effort to maintain backwards compatibility, we thoroughly unit test every Pull Request for all versions of Python we support. These unit tests are intended to catch general programmatic errors, possible vulnerabilities (via bandit) and _potential breaking changes_. 

> If you have to adjust a unit test locally in order to produce passing results, there is a possibility you are working with a potential breaking change.

Please fully document changes to unit tests within your Pull Request. If you did not specify "Breaking Change" on the punch list in the description, and the change is identified as possibly breaking, this may delay or prevent approval of your PR.

### Branch targeting
_Please do not target the `main` branch with your Pull Request unless it is the only branch or you are directed to do so by a maintainer_. Instead, target your PR at the most recent development branch. 

We use [SemVer](https://semver.org/) as our versioning scheme. (Example branch name: _ver_0.4.3_) 

If you are unable to identify the current development branch, please reach out to the maintainers or post a message to the general discussion board.

### Pull Request template
Please use the pull request template provided, making sure the following details are included in your request:
+ Is this a breaking change?
+ Are all new or changed code paths covered by unit testing?
+ A complete listing of issues addressed or closed with this change.
+ A complete listing of any enhancements provided by this change.
+ Any usage details developers may need to make use of this new functionality.
    - Does additional documentation need to be developed beyond what is listed in your Pull Request?
+ Any other salient points of interest.

### Approval / Merging
All Pull Requests must be approved by at least one maintainer. Once approved, a maintainer will perform the merge and execute any backend 
processes related to package deployment. At this time, contributors _do not_ have the ability to merge to the `main` branch.

## Suggestions
If you have suggestions on how this process could be improved, please let us know by [starting a new discussion](https://github.com/CrowdStrike/falconpy/discussions).
