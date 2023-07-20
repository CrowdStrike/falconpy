#!/bin/bash
# Uses Docker, Python and a requirements.txt
# file to generate a zip archive to be used 
# as an AWS lambda layer.

# Tested on Darwin and AWS Linux 2
# Assumes the docker service is running.
#
# Currently targets Python 3.8
cat - << EOF > lambda-requirements.txt
crowdstrike-falconpy
urllib3 < 2.0
EOF
# Remove any old copies
rm falconpy-layer.zip >/dev/null 2>&1
# Run the lambci image and install the requirements
docker run --rm --entrypoint '' -v $(pwd):/foo -w /foo public.ecr.aws/lambda/python:3.8 \
pip install -r lambda-requirements.txt -t python
# Create the layer archive
zip -r falconpy-layer.zip python
# Clean up
rm -fR python
rm lambda-requirements.txt
