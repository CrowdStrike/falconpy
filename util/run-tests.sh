#!/bin/bash
# At this point in time we are excluding FalconShell and FalconDebug from unit testing
#
coverage run --rcfile=util/coverage.config -m pytest -s -v
coverage report
bandit -r src
