#!/usr/bin/env python3
import os

from aws_cdk import App, Environment

from core.ec2_stack import Ec2Stack
from core.myconstructs.myctrl import MyCtrl
from core.nyan_vpc_stack import NyanVpcStack
from core.utils.configread import configread2

app = App()
myctrl = MyCtrl(config=configread2("core/parameters", "stacks.yaml"))
env = Environment(region=myctrl.common.region, account=myctrl.common.account)
nyanvpcstack = NyanVpcStack(app, "NyanVpcStack", myctrl=myctrl, env=env)
ec2stack = Ec2Stack(app, "Ec2Stack", myctrl=myctrl, env=env)
ec2stack.add_dependency(nyanvpcstack)

app.synth()
