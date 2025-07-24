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
        # もしmyifの内容を補正する必要があるならここで！
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnFunction:
        rsc = CfnFunction(**rscif)
        return rsc

# ==============================
# CfnPermission
# ==============================
class MyPermission(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        # もしmyifの内容を補正する必要があるならここで！
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnPermission:
        rsc = CfnPermission(**rscif)
        return rsc