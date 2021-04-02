![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) 

[![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

# FalconPy usage examples
These examples are provided as a quick start for your project.

+ [Authentication for Examples](#authentication-for-these-examples)
+ [Samples by API](#samples-by-api)
+ [Suggestions](#suggestions)

## Authentication for these Examples
In order to expedite sample delivery, we will be following a standard pattern for defining and providing credentials to the API.
This is not the only method of providing these values, and not recommended for production deployments as the config.json file is
**not encrypted**.

In order to test these samples locally in your development environment, rename the file `config_sample.json` to `config.json` and then
update this file to reflect your current development API credentials.

## Samples by API
These samples are categorized by API service collection.

### Sample Uploads API
+ [Upload, Retrieve and then Delete a file](sample_uploads/sample_uploads.py)

## Suggestions
Got a suggestion for an example you'd like to see? Let us know by posting a message to our [discussion board](https://github.com/CrowdStrike/falconpy/discussions).

Have an example you've developed yourself that you'd like to share?  **_Excellent!_** Please review our [contributing guidelines](https://github.com/CrowdStrike/falconpy/CONTRIBUTING.md) and then submit a pull request.