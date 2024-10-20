from typing import Mapping,Optional
from pydantic import BaseModel


# ==============================
# VPC Define START
# ==============================
class MyVPCIF(BaseModel):
    construct_id: str
    cidr_block: Optional[str]=None
    enable_dns_hostnames: Optional[bool]=None
    enable_dns_support: Optional[bool]=None
    instance_tenancy: Optional[str]=None
    ipv4_ipam_pool_id: Optional[str]=None
    ipv4_netmask_length: Optional[int]=None
    tags: Optional[Mapping[str,str]]=None
