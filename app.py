#!/usr/bin/env python3
import os

from aws_cdk import App,Environment
from cdk_core_project.cdk_core_project_stack import CdkCoreProjectStack

app = App()
env = Environment(account='123456789099', region='ap-northeast-1')
CdkCoreProjectStack(app,"CdkCoreProjectStack",env=env)
app.synth()