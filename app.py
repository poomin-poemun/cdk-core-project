#!/usr/bin/env python3
import os

from aws_cdk import App, Environment

from core.myconstructs.myctrl import MyCtrl

#from core.first_vpc_stack import FirstVpcStack
from core.s3event_stack import S3EventStack
from core.utils.configread import configread

app = App()
#myctrl = MyCtrl(config=configread("core/parameters/first_vpc_params.yaml"))
myctrl = MyCtrl(config=configread("core/parameters/s3event_params.yaml"))
env = Environment(region=myctrl.common.region, account=myctrl.common.account)
#FirstVpcStack(app, "FirstVpcStack", myctrl=myctrl, env=env)
S3EventStack(app, "S3EventStack", myctrl=myctrl, env=env)
app.synth()
