from aws_cdk import Stack
from constructs import Construct

from core.myconstructs.myctrl import MyCtrl
from core.myconstructs.myec2 import (
    MyInternetGateway,
    MyRoute,
    MyRouteTable,
    MyVpc,
    MyVPCGatewayAttachment,
)


class FirstVpcStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # VPC
        self.myctrl = myctrl
        firstvpc = myctrl.create(MyVpc(obj=self, name="firstvpc.vpcs.first_vpc"))
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
