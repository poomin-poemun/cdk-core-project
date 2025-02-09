from aws_cdk import Stack
from constructs import Construct

from core.myconstructs.ec2.myInternetgateway import MyInternetGateway
from core.myconstructs.ec2.myroute import MyRoute
from core.myconstructs.ec2.myroutetable import MyRouteTable
from core.myconstructs.ec2.myvpc import MyVpc
from core.myconstructs.ec2.myvpc_gateway_attachment import MyVPCGatewayAttachment
from core.servicetypes.first_vpc_types import FirstVpcTypes


class FirstVpcStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myif: FirstVpcTypes, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # VPC
        vpfif = myif.firstvpc.vpcs["first-vpc"]
        firstvpc = MyVpc(self, myif=vpfif)
        # route-table public
        pub_routetblif = myif.firstvpc.route_tables["first-public-routetbl"]
        pub_routetblif.vpc_id = firstvpc.attr_vpc_id
        firstpubroutetbl = MyRouteTable(self, myif=pub_routetblif)
        # route-table private
        pri_routetblif = myif.firstvpc.route_tables["first-private-routetbl"]
        pri_routetblif.vpc_id = firstvpc.attr_vpc_id
        firstpriroutetbl = MyRouteTable(self, myif=pri_routetblif)
        # igw
        igwif = myif.firstvpc.igws["first-igw"]
        firstigw = MyInternetGateway(self, myif=igwif)
        # route-igw
        routeigwif = myif.firstvpc.routes["first-igw-rute"]
        routeigwif.route_table_id = firstpubroutetbl.attr_route_table_id
        routeigwif.gateway_id = firstigw.attr_internet_gateway_id
        routeigw = MyRoute(self, myif=routeigwif)
        # vpcgatewayattach
        vpcgatewayattachif = myif.firstvpc.vpcgatewayattachs["first-vpcgatewayattach"]
        vpcgatewayattachif.vpc_id = firstvpc.attr_vpc_id
        vpcgatewayattachif.internet_gateway_id = routeigw.gateway_id
        vpcgatewayattach = MyVPCGatewayAttachment(self, myif=vpcgatewayattachif)
