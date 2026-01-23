#!/usr/bin/env python3
import os

from aws_cdk import App, Environment

from core.ec2_ssm_stack import Ec2SsmStack
from core.myconstructs.myctrl import MyCtrl
from core.pwork_vpc_endpoint_stack import PworkVpcEndpointStack
from core.pwork_vpc_stack import PworkVpcStack
from core.utils.configread import configread, configread2

app = App()
myctrl = MyCtrl(config=configread2("core/parameters", "stacks.yaml"))
env = Environment(region=myctrl.common.region, account=myctrl.common.account)
pworkvpcstack = PworkVpcStack(app, "PworkVpcStack", myctrl=myctrl, env=env)
vpcendpointstack = PworkVpcEndpointStack(
    app, "PworkVpcEndpointStack", myctrl=myctrl, env=env
)
vpcendpointstack.add_dependency(pworkvpcstack)
ec2ssmstack = Ec2SsmStack(app, "Ec2SsmStack", myctrl=myctrl, env=env)
ec2ssmstack.add_dependency(vpcendpointstack)

app.synth()
