#!/usr/bin/env python3
import os

from aws_cdk import App, Environment

from core.apigw_lambda_stack import ApigwLambdaStack
from core.myconstructs.myctrl import MyCtrl
from core.pwork_vpc_stack import PworkVpcStack
from core.utils.configread import configread2

app = App()
myctrl = MyCtrl(config=configread2("core/parameters","stacks.yaml"))
env = Environment(region=myctrl.common.region, account=myctrl.common.account)
pworkvpcstack=PworkVpcStack(app, "PworkVpcStack", myctrl=myctrl, env=env)
apigwlambdastack=ApigwLambdaStack(app, "ApigwLambdaStack", myctrl=myctrl, env=env)
apigwlambdastack.add_dependency(pworkvpcstack)
app.synth()