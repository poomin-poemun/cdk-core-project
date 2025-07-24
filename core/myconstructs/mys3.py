from typing import Any

from aws_cdk.aws_s3 import CfnBucket, CfnBucketPolicy
from constructs import Construct

from core.myconstructs.mybase import MyBase


# ==============================
# CfnBucket
# ==============================
class MyBucket(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        # もしmyifの内容を補正する必要があるならここで！
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnBucket:
        rsc = CfnBucket(**rscif)
        return rsc

# ==============================
# CfnBucketPolicy
# ==============================
class MyBucketPolicy(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        # もしmyifの内容を補正する必要があるならここで！
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnBucketPolicy:
        rsc = CfnBucketPolicy(**rscif)
        return rsc