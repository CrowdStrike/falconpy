#!/bin/bash
# At this point in time we are excluding FalconShell and FalconDebug from unit testing
#
coverage run --source=src/falconpy --omit=src/falconpy/debug.py -m pytest -s -v
coverage report
bandit -r src
