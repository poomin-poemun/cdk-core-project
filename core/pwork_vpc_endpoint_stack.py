from aws_cdk import Stack
from constructs import Construct

from core.myconstructs.myctrl import MyCtrl
from core.myconstructs.myec2 import MySecurityGroup, MyVPCEndpoint


class PworkVpcEndpointStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.myctrl = myctrl
        myctrl.add_common_tags(self)
        # SecurityGroup
        pwrokvpcendpoint_sg = myctrl.create(
            MySecurityGroup(
                obj=self, name="PWorkSSMEndpoint.securitygrps.pwork_endpoint_sg"
            )
        )
        # VPC Endpoint - ec2messages
        # pworkendpoint_ec2messages = myctrl.create(
        #    MyVPCEndpoint(obj=self, name="PWorkSSMEndpoint.vpcendpoints.ec2messages")
        # )
        # pworkendpoint_ec2messages.add_dependency(pwrokvpcendpoint_sg)
        # VPC Endpoint - ssm
        pworkendpoint_ssm = myctrl.create(
            MyVPCEndpoint(obj=self, name="PWorkSSMEndpoint.vpcendpoints.ssm")
        )
        # pworkendpoint_ssm.add_dependency(pworkendpoint_ec2messages)
        # VPC Endpoint - ssmmessages
        pworkendpoint_ssmmessages = myctrl.create(
            MyVPCEndpoint(obj=self, name="PWorkSSMEndpoint.vpcendpoints.ssmmessages")
        )
        pworkendpoint_ssmmessages.add_dependency(pworkendpoint_ssm)
