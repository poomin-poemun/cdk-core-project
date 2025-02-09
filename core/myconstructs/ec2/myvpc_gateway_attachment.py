from aws_cdk.aws_ec2 import CfnVPCGatewayAttachment

from core.basetypes.myec2 import MyVPCGatewayAttachmentIF


def MyVPCGatewayAttachment(
    self: any, myif: MyVPCGatewayAttachmentIF
) -> CfnVPCGatewayAttachment:
    rsc = CfnVPCGatewayAttachment(
        self,
        myif.construct_id,
        vpc_id=myif.vpc_id,
        internet_gateway_id=myif.internet_gateway_id,
        vpn_gateway_id=myif.vpn_gateway_id,
    )
    return rsc
