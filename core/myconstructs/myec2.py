import copy
from typing import Any

from aws_cdk.aws_ec2 import (
    CfnInstance,
    CfnInternetGateway,
    CfnRoute,
    CfnRouteTable,
    CfnSecurityGroup,
    CfnSubnet,
    CfnSubnetRouteTableAssociation,
    CfnVPC,
    CfnVPCEndpoint,
    CfnVPCGatewayAttachment,
)

from core.myconstructs.mybase import MyBase


# ==============================
# CfnVPC
# ==============================
class MyVpc(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnVPC:
        rsc = CfnVPC(**rscif)
        # vpc_id
        myif["vpc_id"] = rsc.attr_vpc_id
        return rsc


# ==============================
# CfnSubnet
# ==============================
class MySubnet(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnSubnet:
        rsc = CfnSubnet(**rscif)
        # subnet_id
        myif["attr_subnet_id"] = rsc.attr_subnet_id
        return rsc


# ==============================
# CfnRoute
# ==============================
class MyRoute(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnRoute:
        rsc = CfnRoute(**rscif)
        # gateway_id
        myif["gateway_id"] = rsc.gateway_id
        return rsc


# ==============================
# CfnInternetGateway
# ==============================
class MyInternetGateway(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnInternetGateway:
        rsc = CfnInternetGateway(**rscif)
        # attr_internet_gateway_id
        myif["attr_internet_gateway_id"] = rsc.attr_internet_gateway_id
        return rsc


# ==============================
# CfnRouteTable
# ==============================
class MyRouteTable(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnRouteTable:
        rsc = CfnRouteTable(**rscif)
        # attr_route_table_id
        myif["attr_route_table_id"] = rsc.attr_route_table_id
        return rsc


# ==============================
# CfnSubnetRouteTableAssociation
# ==============================
class MySubnetRouteTableAssociation(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnSubnetRouteTableAssociation:
        rsc = CfnSubnetRouteTableAssociation(**rscif)
        return rsc


# ==============================
# CfnVPCGatewayAttachment
# ==============================
class MyVPCGatewayAttachment(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnVPCGatewayAttachment:
        rsc = CfnVPCGatewayAttachment(**rscif)
        return rsc


# ==============================
# CfnSecurityGroup
# ==============================
class MySecurityGroup(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnSecurityGroup:
        tmp_rscif: dict = copy.deepcopy(rscif)
        if "security_group_egress" in tmp_rscif:
            egress: list = []
            for onegress in tmp_rscif["security_group_egress"]:
                egress.append(CfnSecurityGroup.EgressProperty(**onegress))
            tmp_rscif["security_group_egress"] = egress
        if "security_group_ingress" in tmp_rscif:
            ingress: list = []
            for oneingress in tmp_rscif["security_group_ingress"]:
                ingress.append(CfnSecurityGroup.IngressProperty(**oneingress))
            tmp_rscif["security_group_ingress"] = ingress
        rsc = CfnSecurityGroup(**tmp_rscif)
        # attr_group_id
        myif["attr_group_id"] = rsc.attr_group_id
        return rsc


# ==============================
# CfnInstance
# ==============================
class MyInstance(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnInstance:
        tmp_rscif: dict = copy.deepcopy(rscif)
        if "block_device_mappings" in tmp_rscif:
            blk_dev_map_list: list = []
            for blk_dev_map in tmp_rscif["block_device_mappings"]:
                if "ebs" in blk_dev_map:
                    blk_dev_map["ebs"] = CfnInstance.EbsProperty(**(blk_dev_map["ebs"]))
                blk_dev_map_list.append(
                    CfnInstance.BlockDeviceMappingProperty(**blk_dev_map)
                )
            tmp_rscif["block_device_mappings"] = blk_dev_map_list
        if "network_interfaces" in tmp_rscif:
            network_interface_list: list = []
            for network_interface in tmp_rscif["network_interfaces"]:
                network_interface_list.append(
                    CfnInstance.NetworkInterfaceProperty(**network_interface)
                )
            tmp_rscif["network_interfaces"] = network_interface_list
        rsc = CfnInstance(**tmp_rscif)
        return rsc


# ==============================
# CfnVPCEndpoint
# ==============================
class MyVPCEndpoint(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnVPCEndpoint:
        rsc = CfnVPCEndpoint(**rscif)
        return rsc
