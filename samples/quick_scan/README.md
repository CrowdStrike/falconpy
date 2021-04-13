![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) 

[![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

# Sandbox / Quick Scan sample
This is a proof of concept. Extensive performance testing has not been performed at this time.

## Notes
+ A **VOLUME** is a collection of files that are uploaded and then scanned as a singular batch.
+ The log file rotates to prevent file system bloat.

## Local Directory scanning
+ The folder is inventoried and then files are uploaded to the API in a linear fashion.
+ This method is impacted by data transfer speeds from the source file system location to CrowdStrike's cloud. 
+ Supports pattern matching to filter objects scanned using the "--pattern" or "-p" command line parameter.

## S3 Bucket scanning
+ The bucket contents are inventoried, and then the contents are downloaded to local memory and 
uploaded to the Sandbox API in a linear fashion. 
+ This method does NOT store the files on the local file system. 
+ Due to the nature of this solution, the method is heavily impacted by data transfer speeds. 
    - Recommended deployment pattern involves running in AWS within a container, an EC2 instance or as a serverless lambda. 
+ Currently scans the entire bucket only. 
+ You must specify a target that includes the string "s3://" in order to scan a bucket.

## Dependencies
+ boto3
+ crowdstrike-falconpy 0.4.5+

```shell
python3 -m pip install boto3 crowdstrike-falconpy
```

## Example config.json file:
```json
{
    "falcon_client_id": "API ID GOES HERE",
    "falcon_client_secret": "API SECRET GOES HERE"
}
```

## Alpha testing
This solution has been tested on Python 3.7 / 3.9 running under Amazon Linux 2 and MacOS 10.15.
