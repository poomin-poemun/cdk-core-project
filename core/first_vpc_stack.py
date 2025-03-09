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


class FirstVpcStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.myctrl = myctrl
        # VPC
        firstvpc = myctrl.create(MyVpc(obj=self, name="firstvpc.vpcs.first_vpc"))

        # first_pub_subnet_az1
        firstpubsubnetaz1 = myctrl.create(MySubnet(obj=self, name="firstvpc.subnets.first_pub_subnet_az1"))
        # first_pub_subnet_az3
        firstpubsubnetaz3 = myctrl.create(MySubnet(obj=self, name="firstvpc.subnets.first_pub_subnet_az3"))
        # first_pri_subnet_az1
        firstprisubnetaz1 = myctrl.create(MySubnet(obj=self, name="firstvpc.subnets.first_pri_subnet_az1"))
        # first_pri_subnet_az3
        firstprisubnetaz3 = myctrl.create(MySubnet(obj=self, name="firstvpc.subnets.first_pri_subnet_az3"))

        # route-table public
        firstpubroutetbl = myctrl.create(
            MyRouteTable(self, name="firstvpc.route_tables.first-public-routetbl")
        )
        # route-table private
        firstpriroutetbl = myctrl.create(
            MyRouteTable(self, name="firstvpc.route_tables.first-private-routetbl")
        )

        # igw
        firstigw = myctrl.create(
            MyInternetGateway(self, name="firstvpc.igws.first-igw")
        )

        # route-igw
        routeigw = myctrl.create(MyRoute(self, name="firstvpc.routes.first-igw-rute"))

        # vpcgatewayattach
        vpcgatewayattach = myctrl.create(
            MyVPCGatewayAttachment(
                self, name="firstvpc.vpcgatewayattachs.first-vpcgatewayattach"
            )
        )

        # first_pub_subnet_route_az1
        firstpubsubnetaz1 = myctrl.create(MySubnetRouteTableAssociation(obj=self, name="firstvpc.subnet-routes.first_pub_subnet_route_az1"))
        # first_pub_subnet_route_az3
        firstpubsubnetaz3 = myctrl.create(MySubnetRouteTableAssociation(obj=self, name="firstvpc.subnet-routes.first_pub_subnet_route_az3"))
        # first_pri_subnet_route_az1
        firstprisubnetaz1 = myctrl.create(MySubnetRouteTableAssociation(obj=self, name="firstvpc.subnet-routes.first_pri_subnet_route_az1"))
        # first_pri_subnet_route_az3
        firstprisubnetaz3 = myctrl.create(MySubnetRouteTableAssociation(obj=self, name="firstvpc.subnet-routes.first_pri_subnet_route_az3"))
