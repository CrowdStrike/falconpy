![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

![GitHub top language](https://img.shields.io/github/languages/top/crowdstrike/falconpy?logo=python&logoColor=white)
![GitHub issues](https://img.shields.io/github/issues-raw/crowdstrike/falconpy?logo=github)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/crowdstrike/falconpy?color=green&logo=github)


# Security Policy
This document outlines security policy and procedures for the CrowdStrike `falconpy` project.

+ [Supported Python versions](#supported-python-versions)
+ [Supported Operating Systems](#supported-operating-systems)
+ [Supported CrowdStrike regions](#supported-crowdstrike-regions)
+ [Supported FalconPy versions](#supported-falconpy-versions)
+ [Reporting a potential security vulnerability](#reporting-a-potential-security-vulnerability)
+ [Disclosure and Mitigation Process](#disclosure-and-mitigation-process)

## Supported Python versions

FalconPy functionality is unit tested to run under the following versions of Python. Unit testing is performed with every pull request or commit to `main`.

| Version | Supported |
| :------- | :--------: |
| 3.12.x  | ![Yes](https://img.shields.io/badge/-YES-green) |
| 3.11.x  | ![Yes](https://img.shields.io/badge/-YES-green) |
| 3.10.x  | ![Yes](https://img.shields.io/badge/-YES-green) |
| 3.9.x   | ![Yes](https://img.shields.io/badge/-YES-green) |
| 3.8.x   | ![Yes](https://img.shields.io/badge/-YES-green) |
| 3.7.x   | ![Yes](https://img.shields.io/badge/-YES-green) |
| 3.6.x   | ![Partial](https://img.shields.io/badge/-FalconPy_<=_v1.3.x-darkgreen) |
| <= 3.5  | ![No](https://img.shields.io/badge/-NO-red) |
| <= 2.x.x | ![No](https://img.shields.io/badge/-NO-red) |

## Supported Operating Systems

Unit testing for FalconPy is performed using Apple macOS, Microsoft Windows and Ubuntu Linux.

| Operating System | Most Recent Result |
| :--- | :--- |
| [![macOS](https://img.shields.io/badge/-macOS-silver?logo=apple&style=for-the-badge&labelColor=gray)](https://www.apple.com/macos/) | [![Unit testing (MacOS)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_macos.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_macos.yml) |
| [![Ubuntu](https://img.shields.io/badge/-Ubuntu-964?logo=ubuntu&style=for-the-badge&labelColor=tan)](https://ubuntu.com/) | [![Unit testing (Ubuntu)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_ubuntu.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_ubuntu.yml)<BR/>[![Unit testing (US2)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_us2.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_us2.yml)<BR/>[![Unit testing (EU1)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_eu1.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_eu1.yml)<BR/>[![Unit testing (USGOV1)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_usgov1.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_usgov1.yml) |
| [![Windows](https://img.shields.io/badge/-Windows-blue?logo=windows&style=for-the-badge&labelColor=darkblue)](https://www.microsoft.com/en-us/windows/) | [![Unit testing (Windows)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_windows.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_windows.yml) |

FalconPy has been used and should have no issues running on the following additional operating systems.

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

## Supported CrowdStrike regions

FalconPy is unit tested for functionality across all CrowdStrike regions.

| Region | Most Recent Result |
| :--- | :--- |
| US-1 | [![Unit testing (MacOS)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_macos.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_macos.yml)<BR/>[![Unit testing (Ubuntu)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_ubuntu.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_ubuntu.yml)<BR/>[![Unit testing (Windows)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_windows.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_windows.yml) |
| US-2 | [![Unit testing (US2)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_us2.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_us2.yml) |
| EU-1 | [![Unit testing (EU1)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_eu1.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_eu1.yml) |
| US-GOV-1 | [![Unit testing (USGOV1)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_usgov1.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/unit_testing_usgov1.yml) |

## Supported FalconPy versions

When discovered, we release security vulnerability patches for the most recent release at an accelerated cadence.  

## Reporting a potential security vulnerability

We have multiple avenues to receive security-related vulnerability reports.

Please report suspected security vulnerabilities by:
+ Submitting a [bug](https://github.com/CrowdStrike/falconpy/issues/new?assignees=&labels=bug+%3Abug%3A&template=bug_report.md&title=%5B+BUG+%5D+...).
+ Starting a new [discussion](https://github.com/CrowdStrike/falconpy/discussions).
+ Submitting a [pull request](https://github.com/CrowdStrike/falconpy/pulls) to potentially resolve the issue. (New contributors: please review the content located [here](https://github.com/CrowdStrike/falconpy/blob/main/CONTRIBUTING.md).)
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

<BR/><BR/>

<p align="center"><img src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-footer.png"><BR/><img width="300px" src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-goblin-panda.png"></P>
<h3><P align="center">WE STOP BREACHES</P></h3>
