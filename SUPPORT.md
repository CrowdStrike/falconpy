![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# FalconPy Support

FalconPy is a community-driven, open source project designed to assist developers in leveraging the power of CrowdStrike APIs within their solutions. While not a formal CrowdStrike product, FalconPy is maintained by CrowdStrike and supported in partnership with the open source developer community.

- [Issue Reporting and Questions](#issue-reporting-and-questions-)
- [Community Forums](#community-forums)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Issue Reporting and Questions 🐛

Issues may be reported [here](https://github.com/CrowdStrike/falconpy/issues/new/choose) and are used to track bugs, documentation and link updates, enhancement requests and security concerns.

### Issue Formatting (MCVE)

Whenever possible, please try to format issues and questions in the [**M**inimal, **C**omplete, and **V**erifiable **E**xample](https://stackoverflow.com/help/minimal-reproducible-example) format. This format reduces "noise", allowing the community to better understand your concern, and provide you with a solution more quickly. This also reduces the likelihood of confidential environment details being accidentally shared within your post.

MCVE formatted code examples provided within issues or questions should be:

- _**Minimal**_: Provide as little as code as possible to produce the problem.
  - Only provide the [statements required](https://matthewrocklin.com/minimal-bug-reports#see-how-small-you-can-make-things) to create an example of the issue.
  - Use simple, descriptive names for functions and variables. Don't just copy your existing code.
  - [Do not include real data](https://matthewrocklin.com/minimal-bug-reports#don-t-post-data). [Mock data examples](https://matthewrocklin.com/minimal-bug-reports#actually-don-t-include-your-data-at-all) to describe the format used, but do not provide real values.
- _**Complete**_: Provide all the necessary programmatic pieces to recreate the issue.
  - Do _**not**_ provide screenshots of code.
  - Use `code blocks` for each file or snippet. Include a description with each block.
  - Provide all error messages received, including the [complete traceback](https://matthewrocklin.com/minimal-bug-reports#provide-complete-tracebacks).
- _**Reproducible**_: Provide code that reliably reproduces the problem.
  - Provide as much detail regarding the problem as possible.
  - Test your example to make sure it produces consistent results.

> To read more about _MCVE format_, review this post on [Stack Overflow](https://stackoverflow.com/help/minimal-reproducible-example). For tips on how to properly format questions, check out the blog post by [@mrocklin](https://github.com/mrocklin/) on [crafting minimal bug reports](https://matthewrocklin.com/minimal-bug-reports).

[![Report Issue](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/report-issue.png)](https://github.com/CrowdStrike/falconpy/issues/new/choose)

### Support Escalation

Generally, we endeavor to provide support for using FalconPy here within the repository. This expands our online knowledge base, enables self-help for our community, and can reduce the amount of time for you to receive answers. 

If you are a CrowdStrike customer and you would prefer to have your questions or issues handled directly with CrowdStrike Support, you are welcome to [contact the CrowdStrike technical support team](https://supportportal.crowdstrike.com/).

#### API or Out of Scope Issues

Depending on the root cause, there is a possibility that an identified issue exceeds the scope of the FalconPy SDK, and may require additional investigation. A maintainer may ask you to [contact the CrowdStrike technical support team](https://supportportal.crowdstrike.com/) directly should this occur.

#### Confidentiality

There are also situations where aspects of a support concern cannot be discussed in an online forum, such as:

- customer entitlement
- data sensitivity
- environment configuration

_MCVE format_ is designed to reduce the potential for encountering confidentiality concerns while describing your issue, but cannot speak to every scenario. If one of these concerns impacts your ability to post an issue to this repository, please [contact the CrowdStrike technical support team](https://supportportal.crowdstrike.com/) directly making sure to highlight the concern as part of your support request.

#### Questions

Have a question you can't find answered in the [documentation](https://falconpy.io) or [samples](https://github.com/CrowdStrike/falconpy/tree/main/samples)?

Find out if anyone else in the community is experiencing the same issue on our [discussion board](#community-forums).
Your questions are welcome; please submit them to the [Q&A section](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A).

[![Discussions](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/ask-a-question.png)](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A)

Not sure if you're asking a question or submitting an issue? 🤔

Issue reports that do not result in a bug finding, documentation or link update, security alert, or enhancement request are converted into discussions. Discussions that relate to potential errors, documentation and link updates, security concerns or enhancement requests will result in the generation of an issue report. Either button should get the job done.

[![GitHub issues](https://img.shields.io/github/issues-raw/crowdstrike/falconpy?logo=github)](https://github.com/CrowdStrike/falconpy/issues?q=is%3Aopen+is%3Aissue)
[![Percentage of issues still open](http://isitmaintained.com/badge/open/CrowdStrike/falconpy.svg)](http://isitmaintained.com/project/CrowdStrike/falconpy "Percentage of issues still open")
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/crowdstrike/falconpy?color=green&logo=github)](https://github.com/CrowdStrike/falconpy/issues?q=is%3Aissue+is%3Aclosed)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/CrowdStrike/falconpy.svg)](http://isitmaintained.com/project/CrowdStrike/falconpy "Average time to resolve an issue")

## Community Forums
The discussion board for this repository also provides the community with means to communicate regarding [enhancements ideas](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AIdeas), [integration examples](https://github.com/CrowdStrike/falconpy/discussions/496) and [new releases](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3A%22Show+and+tell%22).

There are four discussion categories:
| | <img width=100> Category | <BR/> Purpose |
| :--: | :--- | :--- |
| :speech_balloon: | [**General**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AGeneral) | Catch all for general discussions. |
| :bulb: | [**Ideas**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AIdeas) | Have a suggestion for a feature request? Is there something the community or project could improve upon? Let us know here. |
| :pray: | [**Q&A**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A) | Have a question about how to accomplish something? A usability question? Submit them here! |
| :raised_hands: | [**Show and Tell**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3A%22Show+and+tell%22) | Share with the community what you're up to! Perhaps this is letting everyone know about your upcoming conference talk, sharing a project that has embedded FalconPy, or your recent blog. |

[![GitHub Discussions](https://img.shields.io/github/discussions/CrowdStrike/falconpy?logo=github&logoColor=white)](https://github.com/CrowdStrike/falconpy/discussions)

## Documentation
### Official Project Documentation: [falconpy.io](https://falconpy.io)

Extended documentation is also available via the [wiki](https://github.com/CrowdStrike/falconpy/wiki) for this repository.

This content is updated as part of our release cycle and synchronized hourly.

[![Documentation Version](https://img.shields.io/endpoint?url=https%3A%2F%2Ffalconpy.io%2F_version.json&label=documentation%20version)](https://falconpy.io)

## Contributing
Interested in earning a place on our [contributors list](https://github.com/CrowdStrike/falconpy/blob/main/AUTHORS.md#contributors)?

Join an elite community of security-focused Python coders and help **stop breaches**.

We want your contributions!

### Start [here](https://github.com/CrowdStrike/falconpy/blob/main/CONTRIBUTING.md).

---


<p align="center"><img src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-footer.png"><BR/><img width="300px" src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-bear-1.png"></P>
<h3><P align="center">WE STOP BREACHES</P></h3>