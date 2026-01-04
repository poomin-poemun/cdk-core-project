import copy
from typing import Any

from aws_cdk.aws_iam import CfnInstanceProfile, CfnRole
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
        tmp_rscif: dict = copy.deepcopy(rscif)
        if "policies" in tmp_rscif:
            policie_list = []
            for policie in tmp_rscif["policies"]:
                policie_list.append(CfnRole.PolicyProperty(**policie))
            tmp_rscif["policies"] = policie_list
        rsc = CfnRole(**tmp_rscif)
        # attr_arn
        myif["attr_arn"] = rsc.attr_arn
        myif["ref"] = rsc.ref
        return rsc


# ==============================
# CfnInstanceProfile
# ==============================
class MyInstanceProfile(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnInstanceProfile:
        rsc = CfnInstanceProfile(**rscif)
        myif["ref"] = rsc.ref
        return rsc
