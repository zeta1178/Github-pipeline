#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import (
    App, Tags, Duration, Stack
)

from stacks.lambda_stack import LambdaCronStack

props = {'namespace': 'IaC-Project'}

# modify for desired region
env_USA_east1 = cdk.Environment(region="us-east-1")

app = cdk.App()

# lambda stack
lambda_stack = LambdaCronStack(app, f"{props['namespace']}-Lambda", props, env=env_USA_east1)

#Modify as needed
Tags.of(lambda_stack).add("TagNameLambda", "TagValueLambda")

app.synth()
