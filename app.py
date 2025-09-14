#!/usr/bin/env python3
import os

from aws_cdk import App, Environment

from core.apigw_lambda_stack import ApigwLambdaStack
from core.apigw_lambda_stack2 import ApigwLambdaStack2
from core.myconstructs.myctrl import MyCtrl

#from core.first_vpc_stack import FirstVpcStack
#from core.s3event_stack import S3EventStack
from core.pwork_vpc_stack import PworkVpcStack
from core.utils.configread import configread, configread2

app = App()
#myctrl = MyCtrl(config=configread("core/parameters/first_vpc_params.yaml"))
#myctrl = MyCtrl(config=configread("core/parameters/s3event_params.yaml"))
myctrl = MyCtrl(config=configread2("core/parameters","stacks.yaml"))
env = Environment(region=myctrl.common.region, account=myctrl.common.account)
#FirstVpcStack(app, "FirstVpcStack", myctrl=myctrl, env=env)
#S3EventStack(app, "S3EventStack", myctrl=myctrl, env=env)
pworkvpcstack=PworkVpcStack(app, "PworkVpcStack", myctrl=myctrl, env=env)
#apigwlambdastack=ApigwLambdaStack(app, "ApigwLambdaStack", myctrl=myctrl, env=env)
#apigwlambdastack.add_dependency(pworkvpcstack)
apigwlambdastack2=ApigwLambdaStack2(app, "ApigwLambdaStack2", myctrl=myctrl, env=env)
apigwlambdastack2.add_dependency(pworkvpcstack)
app.synth()