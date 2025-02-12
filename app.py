#!/usr/bin/env python3
import os

from aws_cdk import App, Environment

from core.first_vpc_stack import FirstVpcStack
from core.myconstructs.myctrl import MyCtrl
from core.utils.configread import configread

app = App()
myctrl = MyCtrl(config=configread("core/parameters/first_vpc_params.yaml"))
env = Environment(region=myctrl.common.region, account=myctrl.common.account)
FirstVpcStack(app, "FirstVpcStack", myctrl=myctrl, env=env)
app.synth()
