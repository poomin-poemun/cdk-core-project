from aws_cdk.aws_ec2 import CfnSubnetRouteTableAssociation

from core.basetypes.myec2 import MySubnetRouteTableAssociationIF


def MySubnetRouteTableAssociation(
    self: any, myif: MySubnetRouteTableAssociationIF
) -> CfnSubnetRouteTableAssociation:
    rsc = CfnSubnetRouteTableAssociation(
        self,
        myif.construct_id,
        route_table_id=myif.route_table_id,
        subnet_id=myif.subnet_id,
    )
    return rsc
