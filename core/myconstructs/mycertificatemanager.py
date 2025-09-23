from typing import Any

from aws_cdk.aws_certificatemanager import CfnCertificate
from constructs import Construct

from core.myconstructs.mybase import MyBase


# ==============================
# CfnCertificate
# ==============================
class MyCertificate(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnCertificate:
        if "domain_validation_options" in rscif:
            option_list = []
            for option in rscif["domain_validation_options"]:
                option_list.append(
                    CfnCertificate.DomainValidationOptionProperty(**option)
                )
            rscif["domain_validation_options"] = option_list
        rsc = CfnCertificate(**rscif)
        myif["certificate_authority_arn"] = rsc.certificate_authority_arn
        myif["ref"] = rsc.ref
        return rsc
