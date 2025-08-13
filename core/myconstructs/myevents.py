from typing import Any

from aws_cdk.aws_events import CfnRule
from constructs import Construct

from core.myconstructs.mybase import MyBase


# ==============================
# CfnRule
# ==============================
class MyRule(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self,myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnRule:
        rsc = CfnRule(**rscif)
        return rsc