from aws_cdk.aws_ec2 import CfnRoute

from core.basetypes.myec2 import MyRouteIF


def MyRoute(self: any, myif: MyRouteIF) -> CfnRoute:
    rsc = CfnRoute(
        self,
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
    return rsc
