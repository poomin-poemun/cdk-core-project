from typing import Mapping, Optional

from pydantic import BaseModel


# ==============================
# VPC Define START
# ==============================
class MyVPCIF(BaseModel):
    construct_id: str
    cidr_block: Optional[str] = None
    enable_dns_hostnames: Optional[bool] = None
    enable_dns_support: Optional[bool] = None
    instance_tenancy: Optional[str] = None
    ipv4_ipam_pool_id: Optional[str] = None
    ipv4_netmask_length: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


# ==============================
# RouteTable Define START
# ==============================
class MyRouteTableIF(BaseModel):
    construct_id: str
    vpc_id: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


# ==============================
# Route Define START
# ==============================
class MyRouteIF(BaseModel):
    construct_id: str
    route_table_id: Optional[str] = None
    carrier_gateway_id: Optional[str] = None
    core_network_arn: Optional[str] = None
    destination_cidr_block: Optional[str] = None
    destination_ipv6_cidr_block: Optional[str] = None
    destination_prefix_list_id: Optional[str] = None
    egress_only_internet_gateway_id: Optional[str] = None
    gateway_id: Optional[str] = None
    instance_id: Optional[str] = None
    local_gateway_id: Optional[str] = None
    nat_gateway_id: Optional[str] = None
    network_interface_id: Optional[str] = None
    transit_gateway_id: Optional[str] = None
    vpc_endpoint_id: Optional[str] = None
    vpc_peering_connection_id: Optional[str] = None


# ==============================
# InternetGateway Define START
# ==============================
class MyInternetGatewayIF(BaseModel):
    construct_id: str
    tags: Optional[Mapping[str, str]] = None


# ==============================
# VPCGatewayAttachment Define START
# ==============================
class MyVPCGatewayAttachmentIF(BaseModel):
    construct_id: str
    vpc_id: Optional[str] = None
    internet_gateway_id: Optional[str] = None
    vpn_gateway_id: Optional[str] = None


# ==============================
# SubnetRouteTableAssociation Define START
# ==============================
class MySubnetRouteTableAssociationIF(BaseModel):
    construct_id: str
    route_table_id: Optional[str] = None
    subnet_id: Optional[str] = None
