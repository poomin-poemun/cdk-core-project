from typing import Any

from aws_cdk.aws_lambda import CfnFunction, CfnPermission
from constructs import Construct
from core.myconstructs.mybase import MyBase


# ==============================
# CfnFunction
# ==============================
class MyFunction(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnFunction:
        if "vpc_config" in rscif:
          rscif["vpc_config"] = CfnFunction.VpcConfigProperty(**rscif["vpc_config"])
        if "code" in rscif:
          rscif["code"] = CfnFunction.CodeProperty(**rscif["code"])
        rsc = CfnFunction(**rscif)
        # attr_function_arn
        myif["attr_arn"] = rsc.attr_arn
        return rsc

# ==============================
# CfnPermission
# ==============================
class MyPermission(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnPermission:
        rsc = CfnPermission(**rscif)
        return rsc