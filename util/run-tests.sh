#!/bin/bash
coverage run --source src/falconpy -m pytest -s -v
coverage report
