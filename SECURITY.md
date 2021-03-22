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

We release patches for security vulnerabilities as they are discovered. 

Version eligibility for receiving patches depends on the CVSS v3.0 Rating:

| CVSS v3.0 | Supported Versions |
| :------- | :-------------------- |
| 9.0 - 10.0 | Releases within the past three months |
| 4.0 - 8.9 | Most recent release |

## Reporting a potential security vulnerability

Please report suspected security vulnerabilities to __falconpy@crowdstrike.com__. 

## Disclosure and mitigation process

Upon receiving a security bug report, the issue will be assigned to one of the project maintainers. This person will coordinate the related fix and release
process, involving the following steps:
+ Communicate with you to confirm we have received the report and provide you with a status update.
    - You should receive this message within 48 hours.
+ Confirmation of the issue and a determination of affected versions.
+ An audit of the codebase to find any potentially similar problems.
+ Preparation of patches for all releases still under maintenance.
    - These patches will be submitted as a separate pull request and contain a version update.
    - This pull request will be flagged as a security fix.
    - Once merged, and after post-merge unit testing has been completed, the patch will be immediately published to both PyPI repositories.
