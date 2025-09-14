from typing import Any

from aws_cdk.aws_iam import CfnRole
from constructs import Construct

from core.myconstructs.mybase import MyBase


# ==============================
# CfnRole
# ==============================
class MyRole(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnRole:
        if "policies" in rscif:
            policie_list=[]
            for policie in rscif["policies"]:
                policie_list.append(CfnRole.PolicyProperty(**policie))
            rscif["policies"] = policie_list
        rsc = CfnRole(**rscif)
        # attr_arn
        myif["attr_arn"] = rsc.attr_arn
        return rsc