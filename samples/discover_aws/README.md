![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon Discover for Cloud and Containers samples
The examples within this folder focus on leveraging CrowdStrike's Falcon Discover for Cloud and Containers API.

- [Manage Discover accounts](#manage-discover-accounts-aws)

## Manage Discover accounts (AWS)
Register, confirm or delete Falcon Discover account registrations (AWS).

Two samples are provided, one using Service Classes, and another using the Uber class. Both examples implement the same functionality.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| D4C Registration | __READ__, __WRITE__ |

### Execution syntax
Register, check, update or delete accounts within CrowdStrike Discover for Cloud and Containers (AWS specific).

#### Basic usage
Check the status of registered accounts.

> To use the Uber Class example, execute the `manage_discover_accounts_uber.py` sample instead.

```shell
python3 manage_discover_accounts_service.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c check
```

> Log all accounts identified as registered or partially registered.

```shell
python3 manage_discover_accounts_service.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c check -l
```

> Register a new account.

```shell
python3 manage_discover_accounts_service.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c register \
    -a AWS_ACCOUNT_ID -r CLOUDTRAIL_REGION -o CLOUDTRAIL_OWNER_ID -e EXTERNAL_ID -i IAM_ROLE_ARN
```

> Delete a registered account.

```shell
python3 manage_discover_accounts_service.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c delete -a AWS_ACCOUNT_ID
```

> Update an account registration.

```shell
python3 manage_discover_accounts_service.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f update \
    -a AWS_ACCOUNT_ID -r CLOUDTRAIL_REGION -o CLOUDTRAIL_OWNER_ID -e EXTERNAL_ID -i IAM_ROLE_ARN
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 manage_discover_accounts_service.py -h
usage: manage_discover_accounts_service.py [-h] [-q QUERY_LIMIT] [-l] [-r CLOUDTRAIL_BUCKET_REGION] [-o CLOUDTRAIL_BUCKET_OWNER_ID] [-a LOCAL_ACCOUNT] [-e EXTERNAL_ID] [-i IAM_ROLE_ARN] -c COMMAND -f FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET

Get Params to send notification to CRWD topic

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY_LIMIT, --query_limit QUERY_LIMIT
                        The query limit used for check account commands
  -l, --log_enabled     Save results to a file?
  -r CLOUDTRAIL_BUCKET_REGION, --cloudtrail_bucket_region CLOUDTRAIL_BUCKET_REGION
                        AWS Region where the S3 bucket is hosted
  -o CLOUDTRAIL_BUCKET_OWNER_ID, --cloudtrail_bucket_owner_id CLOUDTRAIL_BUCKET_OWNER_ID
                        Account where the S3 bucket is hosted
  -a LOCAL_ACCOUNT, --local_account LOCAL_ACCOUNT
                        This AWS Account
  -e EXTERNAL_ID, --external_id EXTERNAL_ID
                        External ID used to assume role in account
  -i IAM_ROLE_ARN, --iam_role_arn IAM_ROLE_ARN
                        IAM AWS IAM Role ARN that grants access to resources for Crowdstrike
  -c COMMAND, --command COMMAND
                        Troubleshooting action to perform
  -f FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Falcon Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Falcon Client Secret
```

### Example source code
The source code for this example can be found here:
- [Service Class Example](manage_discover_accounts_service.py)
- [Uber Class Example](manage_discover_accounts_uber.py)
