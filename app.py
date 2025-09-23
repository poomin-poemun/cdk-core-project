#!/usr/bin/env python3
import os

from aws_cdk import App, Environment

from core.apigw_lambda_stack3 import ApigwLambdaStack3
from core.certificate_stack import CertificateStack
from core.domain_stack import DomainStack
from core.myconstructs.myctrl import MyCtrl
from core.pwork_vpc_stack import PworkVpcStack
from core.utils.configread import configread2

app = App()
myctrl = MyCtrl(config=configread2("core/parameters", "stacks.yaml"))
env = Environment(region=myctrl.common.region, account=myctrl.common.account)
pworkvpcstack = PworkVpcStack(app, "PworkVpcStack", myctrl=myctrl, env=env)
apigwlambdastack3 = ApigwLambdaStack3(app, "ApigwLambdaStack3", myctrl=myctrl, env=env)
certificatestack = CertificateStack(app, "CertificateStack", myctrl=myctrl, env=env)
domainstack = DomainStack(app, "DomainStack", myctrl=myctrl, env=env)
apigwlambdastack3.add_dependency(pworkvpcstack)
certificatestack.add_dependency(apigwlambdastack3)
domainstack.add_dependency(certificatestack)
app.synth()
