from typing import Any

from aws_cdk.aws_route53 import CfnRecordSet
from constructs import Construct

from core.myconstructs.mybase import MyBase


# ==============================
# CfnRecordSet
# ==============================
class MyRecordSet(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnRecordSet:
        if "alias_target" in rscif:
            alias_target = CfnRecordSet.AliasTargetProperty(**rscif["alias_target"])
            rscif["alias_target"] = alias_target
        if "cidr_routing_config" in rscif:
            cidr_routing_config = CfnRecordSet.CidrRoutingConfigProperty(
                **rscif["cidr_routing_config"]
            )
            rscif["cidr_routing_config"] = cidr_routing_config
        if "geo_location" in rscif:
            geo_location = CfnRecordSet.GeoLocationProperty(**rscif["geo_location"])
            rscif["geo_location"] = geo_location
        if "geo_proximity_location" in rscif:
            geo_proximity_location = CfnRecordSet.GeoProximityLocationProperty(
                **rscif["geo_proximity_location"]
            )
            rscif["geo_proximity_location"] = geo_proximity_location
        rsc = CfnRecordSet(**rscif)
        return rsc
