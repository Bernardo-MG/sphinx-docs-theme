#!/bin/bash
# This script runs the documentation tests
#
# The following environmental variables are used:
# - TEST_DOCS: boolean, control flag for testing, should be true to run tests

if [ "$TEST_DOCS" == "true" ]; then

    tox -e docs

fi
