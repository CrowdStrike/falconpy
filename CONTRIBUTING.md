# Contributing to this repository <!-- omit in toc -->

## Getting started <!-- omit in toc -->
_Welcome!_ We're excited you want to take part in the FalconPy community! 

Please review this document for details regarding getting started with your first contribution, packages you'll need to install as a developer, and our pull request process. If you have any questions, please let us know by
posting in your question in the [discussion board](https://github.com/CrowdStrike/falconpy/discussions).

### Before you begin
- Have you read the [Code of Conduct](CODE_OF_CONDUCT.md)?

### Table of Contents
- [How you can contribute](#how-you-can-contribute)
- [Pull Requests](#pull-requests)
- [Suggestions](#suggestions)

## How you can contribute
- Submit a [bug report](https://github.com/CrowdStrike/falconpy/issues).
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
+ All new contributions __must__ pass unit testing before they will be merged.
    - For scenarios where unit testing passes in the PR and fails post-merge, a maintainer will address the issue. If the problem is programmatic and related to code within the pull request, the merge may be reverted.
+ The util folder contains BASH scripts for triggering unit tests that match unit testing performed as part of our GitHub workflows.

### Linting
All submitted code must meet minimum linting requirements. We use `flake8` for linting. Refer to the "lint.sh" script within the util folder to review our standard linting parameters.

### Branch targeting
_Please do not target the `main` branch with your Pull Request unless directed to do so by a maintainer_. Instead, target your PR at the most recent development branch. 

We use [SemVer](https://semver.org/) as our versioning scheme. (Example branch name: _ver_0.4.3_) 

If you are unable to identify the current development branch, please reach out to the maintainers or post a message to the general discussion board.

### Pull Request template
Please use the pull request template provided, making sure the following details are included in your request:
+ Is this a breaking change?
+ Are all new or changed code paths covered by unit testing?
+ A complete listing of issues addressed or closed with this change.
+ A complete listing of any enhancements provided by this change.
+ Any usage details developers may need to make use of this new functionality.
    - Does additional documentation need to be developed beyond what is listed in your pull request?
+ Any other salient points of interest.

### Approval / Merging
All Pull Requests must be approved by at least one maintainer. Once approved, a maintainer will perform the merge and execute any backend 
processes related to package deployment. At this time, contributors _do not_ have the ability to merge to the `main` branch.

## Suggestions
If you have suggestions on how this process could be improved, please let us know by [starting a new discussion](https://github.com/CrowdStrike/falconpy/discussions).
