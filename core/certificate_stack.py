from aws_cdk import Stack
from constructs import Construct

from core.myconstructs.mycertificatemanager import MyCertificate
from core.myconstructs.myctrl import MyCtrl


class CertificateStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.myctrl = myctrl
        myctrl.add_common_tags(self)
        # Certificate
        certificate = myctrl.create(
            MyCertificate(obj=self, name="certificate.certificates.pworks")
        )
