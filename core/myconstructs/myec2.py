from typing import Any

from aws_cdk.aws_ec2 import (
    CfnInternetGateway,
    CfnRoute,
    CfnRouteTable,
    CfnSubnet,
    CfnSubnetRouteTableAssociation,
    CfnVPC,
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
        # もしmyifの内容を補正する必要があるならここで！
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
        # もしmyifの内容を補正する必要があるならここで！
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
        # もしmyifの内容を補正する必要があるならここで！
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
        # もしmyifの内容を補正する必要があるならここで！
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
        # もしmyifの内容を補正する必要があるならここで！
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
        # もしmyifの内容を補正する必要があるならここで！
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
        # もしmyifの内容を補正する必要があるならここで！
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnVPCGatewayAttachment:
        rsc = CfnVPCGatewayAttachment(**rscif)
        return rsc
