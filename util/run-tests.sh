#!/bin/bash
#
coverage run --rcfile=util/coverage.config -m pytest -s -v
coverage report
bandit -r src
