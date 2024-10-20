from aws_cdk import Environment
from constructs import Construct
from aws_cdk.aws_ec2 import CfnVPC
from core.basetypes.myec2 import MyVPCIF
from core.myconstructs.mytags import MyTags


class Ec2MyVpc(Construct):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        myif: MyVPCIF,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        tags=MyTags(myif.tags)
        self.sg=CfnVPC(
            self,
            construct_id,
            cidr_block=myif.cidr_block,
            enable_dns_hostnames=myif.enable_dns_hostnames,
            enable_dns_support=myif.enable_dns_support,
            instance_tenancy=myif.instance_tenancy,
            ipv4_ipam_pool_id=myif.ipv4_ipam_pool_id,
            ipv4_netmask_length=myif.ipv4_netmask_length,
            tags=tags
        )