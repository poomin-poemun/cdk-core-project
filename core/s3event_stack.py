from aws_cdk import Stack
from constructs import Construct

from core.myconstructs.myctrl import MyCtrl
from core.myconstructs.mys3 import MyBucket


class S3EventStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.myctrl = myctrl
        myctrl.add_common_tags(self)
        # S3 Bucket
        tests3 = myctrl.create(MyBucket(obj=self, name="s3event.buckets.s3_event_test"))