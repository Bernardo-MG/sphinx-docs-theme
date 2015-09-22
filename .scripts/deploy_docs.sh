#!/bin/bash
# This script deploys the documentation
#
# Make sure you have the deployment configuration ready before using it.
#
# It is triggered only commits to the master or develop branches, ignoring pulls.
#
# Also, it will only deploy if the DEPLOY_DOCS environment variable is set to
# 'true'.
#
# For this it just pings ReadTheDocs, which will take care of building the new
# docs.
#
# The following environmental variables are used:
# - PULL_REQUEST: boolean, indicates if this is a pull request, should be false for deployment
# - DEPLOY_DOCS: boolean, control flag for deployment, should be true to deploy
# - SCM_BRANCH: string, the CMS branch from which the code has been taken

if [ "$PULL_REQUEST" == "false" ] && [ "$DEPLOY_DOCS" == "true" ] && [[ "$SCM_BRANCH" == "master" || "$SCM_BRANCH" == "develop" ]]; then

    echo "Deploying docs"
    curl -X POST http://readthedocs.org/build/cwr-dataapi

else

    echo "Docs won't be deployed"

fi