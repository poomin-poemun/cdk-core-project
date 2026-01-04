import copy
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
        tmp_rscif: dict = copy.deepcopy(rscif)
        if "vpc_config" in tmp_rscif:
            tmp_rscif["vpc_config"] = CfnFunction.VpcConfigProperty(
                **tmp_rscif["vpc_config"]
            )
        if "code" in tmp_rscif:
            tmp_rscif["code"] = CfnFunction.CodeProperty(**tmp_rscif["code"])
        rsc = CfnFunction(**tmp_rscif)
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
