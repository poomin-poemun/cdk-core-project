from typing import Any

from aws_cdk.aws_logs import CfnLogGroup, CfnLogStream
from constructs import Construct

from core.myconstructs.mybase import MyBase


# ==============================
# CfnLogGroup
# ==============================
class MyLogGroup(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnLogGroup:
        rsc = CfnLogGroup(**rscif)
        # attr_arn
        myif["attr_arn"] = rsc.attr_arn
        return rsc

# ==============================
# CfnLogStream
# ==============================
class MyLogStream(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnLogStream:
        rsc = CfnLogStream(**rscif)
        return rsc