from aws_cdk import Stack
from constructs import Construct

from core.myconstructs.myctrl import MyCtrl
from core.myconstructs.myec2 import (
    MyInternetGateway,
    MyRoute,
    MyRouteTable,
    MySubnet,
    MySubnetRouteTableAssociation,
    MyVpc,
    MyVPCGatewayAttachment,
)


class NyanVpcStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.myctrl = myctrl
        myctrl.add_common_tags(self)
        # VPC
        nyanvpc = myctrl.create(MyVpc(obj=self, name="pwork.vpcs.nyan_vpc"))

        # nyan_pub_subnet_az1
        nyanpubsubnetaz1 = myctrl.create(
            MySubnet(obj=self, name="pwork.subnets.nyan_pub_subnet_az1")
        )
        # nyan_pub_subnet_az3
        nyanpubsubnetaz3 = myctrl.create(
            MySubnet(obj=self, name="pwork.subnets.nyan_pub_subnet_az3")
        )
        # nyan_pri_subnet_az1
        nyanprisubnetaz1 = myctrl.create(
            MySubnet(obj=self, name="pwork.subnets.nyan_pri_subnet_az1")
        )
        # nyan_pri_subnet_az3
        nyanprisubnetaz3 = myctrl.create(
            MySubnet(obj=self, name="pwork.subnets.nyan_pri_subnet_az3")
        )

        # route-table public
        nyanpubroutetbl = myctrl.create(
            MyRouteTable(self, name="pwork.route_tables.nyan_pub_routetbl")
        )
        # route-table private
        nyanpriroutetbl = myctrl.create(
            MyRouteTable(self, name="pwork.route_tables.nyan_pri_routetbl")
        )

        # pwork_pub_subnet_route_az1
        nyanpubsubnetaz1 = myctrl.create(
            MySubnetRouteTableAssociation(
                obj=self, name="pwork.subnet_routes.nyan_pub_subnet_route_az1"
            )
        )
        # pwork_pub_subnet_route_az3
        nyanpubsubnetaz3 = myctrl.create(
            MySubnetRouteTableAssociation(
                obj=self, name="pwork.subnet_routes.nyan_pub_subnet_route_az3"
            )
        )
        # pwork_pri_subnet_route_az1
        nyanprisubnetaz1 = myctrl.create(
            MySubnetRouteTableAssociation(
                obj=self, name="pwork.subnet_routes.nyan_pri_subnet_route_az1"
            )
        )
        # pwork_pri_subnet_route_az3
        nyanprisubnetaz3 = myctrl.create(
            MySubnetRouteTableAssociation(
                obj=self, name="pwork.subnet_routes.nyan_pri_subnet_route_az3"
            )
        )

        # igw
        nyanigw = myctrl.create(MyInternetGateway(self, name="pwork.igws.nyan_igw"))

        # route-igw
        nyanrouteigw = myctrl.create(MyRoute(self, name="pwork.routes.nyan_igw_rute"))

        # vpcgatewayattach
        nyanvpcgatewayattach = myctrl.create(
            MyVPCGatewayAttachment(
                self, name="pwork.vpcgatewayattachs.nyan_vpcgatewayattach"
            )
        )
