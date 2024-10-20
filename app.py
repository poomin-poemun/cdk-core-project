#!/usr/bin/env python3
import os

from aws_cdk import App,Environment
from core.utils.configread import configread
from core.servicetypes.first_vpc_types import FirstVpcTypes
from core.first_vpc_stack import FirstVpcStack


app = App()
tmpif=FirstVpcTypes(**configread("core/parameters/first_vpc_params.yaml"))
env=Environment(region=tmpif.common.region,account=tmpif.common.account)
FirstVpcStack(app,"FirstVpcStack",myif=tmpif,env=env)
app.synth()