from typing import Any

from aws_cdk.aws_ec2 import (
    CfnInternetGateway,
    CfnRoute,
    CfnRouteTable,
    CfnSubnetRouteTableAssociation,
    CfnVPC,
    CfnVPCGatewayAttachment,
)

from core.basetypes.myec2 import (
    MyInternetGatewayIF,
    MyRouteIF,
    MyRouteTableIF,
    MySubnetRouteTableAssociationIF,
    MyVPCGatewayAttachmentIF,
    MyVPCIF,
)
from core.myconstructs.mybase import MyBase
from core.myconstructs.mytags import MyTags


# ==============================
# CfnVPC
# ==============================
class MyVpc(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        self.myif = myif
        return self._vpc_(myif=MyVPCIF(**myif), updif=self.myif)

    def _vpc_(self, myif: MyVPCIF, updif: dict) -> CfnVPC:
        tags = MyTags(myif.tags)
        rsc = CfnVPC(
            self.obj,
            myif.construct_id,
            cidr_block=myif.cidr_block,
            enable_dns_hostnames=myif.enable_dns_hostnames,
            enable_dns_support=myif.enable_dns_support,
            instance_tenancy=myif.instance_tenancy,
            ipv4_ipam_pool_id=myif.ipv4_ipam_pool_id,
            ipv4_netmask_length=myif.ipv4_netmask_length,
            tags=tags,
        )
        # vpc_id
        updif["vpc_id"] = rsc.attr_vpc_id
        return rsc


# ==============================
# CfnRoute
# ==============================
class MyRoute(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        self.myif = myif
        return self._route_(myif=MyRouteIF(**myif), updif=self.myif)

    def _route_(self, myif: MyRouteIF, updif: dict) -> CfnRoute:
        rsc = CfnRoute(
            self.obj,
            myif.construct_id,
            route_table_id=myif.route_table_id,
            carrier_gateway_id=myif.carrier_gateway_id,
            core_network_arn=myif.core_network_arn,
            destination_cidr_block=myif.destination_cidr_block,
            destination_ipv6_cidr_block=myif.destination_ipv6_cidr_block,
            destination_prefix_list_id=myif.destination_prefix_list_id,
            egress_only_internet_gateway_id=myif.egress_only_internet_gateway_id,
            gateway_id=myif.gateway_id,
            instance_id=myif.instance_id,
            local_gateway_id=myif.local_gateway_id,
            nat_gateway_id=myif.nat_gateway_id,
            network_interface_id=myif.network_interface_id,
            transit_gateway_id=myif.transit_gateway_id,
            vpc_endpoint_id=myif.vpc_endpoint_id,
            vpc_peering_connection_id=myif.vpc_peering_connection_id,
        )
        # gateway_id
        updif["gateway_id"] = rsc.gateway_id
        return rsc


# ==============================
# CfnInternetGateway
# ==============================
class MyInternetGateway(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        self.myif = myif
        return self._internet_gateway_(
            myif=MyInternetGatewayIF(**myif), updif=self.myif
        )

    def _internet_gateway_(
        self, myif: MyInternetGatewayIF, updif: dict
    ) -> CfnInternetGateway:
        tags = MyTags(myif.tags)
        rsc = CfnInternetGateway(self.obj, myif.construct_id, tags=tags)
        # attr_internet_gateway_id
        updif["attr_internet_gateway_id"] = rsc.attr_internet_gateway_id
        return rsc


# ==============================
# CfnRouteTable
# ==============================
class MyRouteTable(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        self.myif = myif
        return self._route_table_(myif=MyRouteTableIF(**myif), updif=self.myif)

    def _route_table_(self, myif: MyRouteTableIF, updif: dict) -> CfnRouteTable:
        tags = MyTags(myif.tags)
        rsc = CfnRouteTable(self.obj, myif.construct_id, vpc_id=myif.vpc_id, tags=tags)
        # attr_route_table_id
        updif["attr_route_table_id"] = rsc.attr_route_table_id
        return rsc


# ==============================
# CfnSubnetRouteTableAssociation
# ==============================
class MySubnetRouteTableAssociation(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        self.myif = myif
        return self._subnet_route_table_association_(
            myif=MySubnetRouteTableAssociationIF(**myif), updif=self.myif
        )

    def _subnet_route_table_association_(
        self, myif: MySubnetRouteTableAssociationIF, updif: dict
    ) -> CfnSubnetRouteTableAssociation:
        rsc = CfnSubnetRouteTableAssociation(
            self.obj,
            myif.construct_id,
            route_table_id=myif.route_table_id,
            subnet_id=myif.subnet_id,
        )
        return rsc


# ==============================
# CfnVPCGatewayAttachment
# ==============================
class MyVPCGatewayAttachment(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        self.myif = myif
        return self._vpc_gateway_attachment_(
            myif=MyVPCGatewayAttachmentIF(**myif), updif=self.myif
        )

    def _vpc_gateway_attachment_(
        self, myif: MyVPCGatewayAttachmentIF, updif: dict
    ) -> CfnVPCGatewayAttachment:

        rsc = CfnVPCGatewayAttachment(
            self.obj,
            myif.construct_id,
            vpc_id=myif.vpc_id,
            internet_gateway_id=myif.internet_gateway_id,
            vpn_gateway_id=myif.vpn_gateway_id,
        )
        return rsc
