from aws_cdk.aws_ec2 import CfnVPC

from core.basetypes.myec2 import MyVPCIF
from core.myconstructs.mytags import MyTags


def MyVpc(self: any, myif: MyVPCIF) -> CfnVPC:
    tags = MyTags(myif.tags)
    rsc = CfnVPC(
        self,
        myif.construct_id,
        cidr_block=myif.cidr_block,
        enable_dns_hostnames=myif.enable_dns_hostnames,
        enable_dns_support=myif.enable_dns_support,
        instance_tenancy=myif.instance_tenancy,
        ipv4_ipam_pool_id=myif.ipv4_ipam_pool_id,
        ipv4_netmask_length=myif.ipv4_netmask_length,
        tags=tags,
    )
    return rsc
