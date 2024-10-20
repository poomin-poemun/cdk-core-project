from aws_cdk import Stack
from constructs import Construct
from core.servicetypes.first_vpc_types import FirstVpcTypes
from core.myconstructs.ec2_myvpc import Ec2MyVpc


class FirstVpcStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,myif: FirstVpcTypes, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        #VPC
        vpfif=myif.firstvpc.vpcs['firstvpc']
        firstvpc=Ec2MyVpc(self,vpfif.construct_id,myif=vpfif)
