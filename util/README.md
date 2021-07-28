# Utilities
Utilities for developers of the crowdstrike-falconpy project.

## Inventory
+ `coverage.config` - configuration settings for coverage.py integration.
+ `create-lambda-layer.sh` - Leverages docker to create a ZIP archive of FalconPy to be used as an AWS lambda layer.
+ `lint.sh` - Lints the package source and returns the result.
+ `run-tests.sh` - Runs a complete unit test series, reports code coverage and runs a bandit analysis.