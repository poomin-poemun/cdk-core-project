from typing import Any

from aws_cdk.aws_apigateway import (
    CfnAccount,
    CfnDeployment,
    CfnMethod,
    CfnResource,
    CfnRestApi,
    CfnStage,
    CfnAuthorizer,
)
from constructs import Construct

from core.myconstructs.mybase import MyBase


# ==============================
# CfnRestApi
# ==============================
class MyRestApi(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnRestApi:
        rsc = CfnRestApi(**rscif)
        myif["attr_rest_api_id"] = rsc.attr_rest_api_id
        myif["attr_root_resource_id"] = rsc.attr_root_resource_id
        return rsc

# ==============================
# CfnResource
# ==============================
class MyResource(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnResource:
        rsc = CfnResource(**rscif)
        myif["attr_resource_id"] = rsc.attr_resource_id
        return rsc

# ==============================
# CfnDeployment
# ==============================
class MyDeployment(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnDeployment:
        rsc = CfnDeployment(**rscif)
        myif["attr_deployment_id"] = rsc.attr_deployment_id
        return rsc

# ==============================
# CfnStage
# ==============================
class MyStage(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnStage:
        # もしmyifの内容を補正する必要があるならここで！
        rsc = CfnStage(**rscif)
        return rsc

# ==============================
# CfnMethod
# ==============================
class MyMethod(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnMethod:
        if "integration" in rscif:
            rscif["integration"]=CfnMethod.IntegrationProperty(**rscif["integration"])
        rsc = CfnMethod(**rscif)
        #rsc.integration=CfnMethod.IntegrationProperty(**rscif["integration"])
        return rsc

# ==============================
# CfnAccount
# ==============================
class MyAccount(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnAccount:
        rsc = CfnAccount(**rscif)
        return rsc

# ==============================
# CfnAuthorizer
# ==============================
class MyAuthorizer(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnAuthorizer:
        rsc = CfnAuthorizer(**rscif)
        myif["attr_authorizer_id"] = rsc.attr_authorizer_id
        return rsc