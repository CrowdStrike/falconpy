#!/bin/bash
# Uses Docker, Python and requirements.txt to
# generates a zip archive to be used for an 
# AWS lambda layer.

# Tested on Darwin and AWS Linux 2

# Currently targets Python 3.8
echo "crowdstrike-falconpy" > lambda-requirements.txt
# Remove any old copies
rm falconpy-layer.zip >/dev/null 2>&1
# Fire up docker
docker-machine start
docker-machine env default
# Connect to the default environment
eval $(docker-machine env default)
# Run the lambci image and install the requirements
docker run --rm -v $(pwd):/foo -w /foo lambci/lambda:build-python3.8 \
pip install -r lambda-requirements.txt -t python
# Create the layer archive
zip -r falconpy-layer.zip python
# Clean up
rm -fR python
rm lambda-requirements.txt
