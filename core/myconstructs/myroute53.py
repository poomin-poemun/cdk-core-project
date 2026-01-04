import copy
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
        tmp_rscif: dict = copy.deepcopy(rscif)
        if "alias_target" in tmp_rscif:
            alias_target = CfnRecordSet.AliasTargetProperty(**tmp_rscif["alias_target"])
            tmp_rscif["alias_target"] = alias_target
        if "cidr_routing_config" in tmp_rscif:
            cidr_routing_config = CfnRecordSet.CidrRoutingConfigProperty(
                **tmp_rscif["cidr_routing_config"]
            )
            tmp_rscif["cidr_routing_config"] = cidr_routing_config
        if "geo_location" in tmp_rscif:
            geo_location = CfnRecordSet.GeoLocationProperty(**tmp_rscif["geo_location"])
            tmp_rscif["geo_location"] = geo_location
        if "geo_proximity_location" in tmp_rscif:
            geo_proximity_location = CfnRecordSet.GeoProximityLocationProperty(
                **tmp_rscif["geo_proximity_location"]
            )
            tmp_rscif["geo_proximity_location"] = geo_proximity_location
        rsc = CfnRecordSet(**tmp_rscif)
        return rsc
