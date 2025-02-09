from aws_cdk.aws_ec2 import CfnInternetGateway

from core.basetypes.myec2 import MyInternetGatewayIF
from core.myconstructs.mytags import MyTags


def MyInternetGateway(self: any, myif: MyInternetGatewayIF) -> CfnInternetGateway:
    tags = MyTags(myif.tags)
    rsc = CfnInternetGateway(self, myif.construct_id, tags=tags)
    return rsc
