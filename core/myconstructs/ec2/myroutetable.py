from aws_cdk.aws_ec2 import CfnRouteTable

from core.basetypes.myec2 import MyRouteTableIF
from core.myconstructs.mytags import MyTags


def MyRouteTable(self: any, myif: MyRouteTableIF) -> CfnRouteTable:
    tags = MyTags(myif.tags)
    rsc = CfnRouteTable(self, myif.construct_id, vpc_id=myif.vpc_id, tags=tags)
    return rsc
