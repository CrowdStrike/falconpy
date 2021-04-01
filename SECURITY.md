# Security Policy
This document outlines security policy and procedures for the CrowdStrike `falconpy` project.
+ [Supported Python versions](#supported-python-versions)
+ [Supported FalconPy versions](#supported-falconpy-versions)
+ [Reporting a potential security vulnerability](#reporting-a-potential-security-vulnerability)
+ [Disclosure and Mitigation Process](#disclosure-and-mitigation-process)

## Supported Python versions

FalconPy functionality is only tested to run under the following versions of Python.

| Version | Supported |
| :------- | :--------- |
| 3.9.x   | :white_check_mark: |
| 3.8.x   | :white_check_mark: |
| 3.7.x   | :white_check_mark: |
| 3.6.x   | :white_check_mark: |
| <= 3.5  | :x: |
| <= 2.x.x | :x: |

## Supported FalconPy versions

When discovered, we release security vulnerability patches for the most recent release at an accelerated cadence.  

## Reporting a potential security vulnerability

We have multiple avenues to receive security-related vulnerability reports.

Please report suspected security vulnerabilities by:
+ Submitting a [bug](https://github.com/CrowdStrike/falconpy/issues)
+ Starting a new [discussion](https://github.com/CrowdStrike/falconpy/discussions)
+ Submitting a [pull request](https://github.com/CrowdStrike/falconpy/pulls) to potentially resolve the issue
+ Sending an email to __falconpy@crowdstrike.com__. 

## Disclosure and mitigation process

Upon receiving a security bug report, the issue will be assigned to one of the project maintainers. This person will coordinate the related fix and release
process, involving the following steps:
+ Communicate with you to confirm we have received the report and provide you with a status update.
    - You should receive this message within 48 - 72 business hours.
+ Confirmation of the issue and a determination of affected versions.
+ An audit of the codebase to find any potentially similar problems.
+ Preparation of patches for all releases still under maintenance.
    - These patches will be submitted as a separate pull request and contain a version update.
    - This pull request will be flagged as a security fix.
    - Once merged, and after post-merge unit testing has been completed, the patch will be immediately published to both PyPI repositories.

## Comments
If you have suggestions on how this process could be improved, please let us know by [starting a new discussion](https://github.com/CrowdStrike/falconpy/discussions).
