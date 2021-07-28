# Utilities
Utilities for developers of the crowdstrike-falconpy project.

## Inventory
+ `coverage.config` - configuration settings for coverage.py integration.
+ `create-lambda-layer.sh` - leverages docker to create a ZIP archive of FalconPy to be used as an AWS lambda layer.
+ `lint.sh` - lints the package source and returns the result.
+ `run-tests.sh` - runs a complete unit test series, reports code coverage and runs a bandit analysis.