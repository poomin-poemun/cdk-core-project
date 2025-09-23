from typing import Any

from aws_cdk.aws_apigatewayv2 import CfnDomainName, CfnRoutingRule
from constructs import Construct

from core.myconstructs.mybase import MyBase


# ==============================
# CfnDomainName
# ==============================
class MyDomainName(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnDomainName:
        if "domain_name_configurations" in rscif:
            configurations_list = []
            for configuration in rscif["domain_name_configurations"]:
                configurations_list.append(
                    CfnDomainName.DomainNameConfigurationProperty(**configuration)
                )
            rscif["domain_name_configurations"] = configurations_list
        rsc = CfnDomainName(**rscif)
        myif["domain_name"] = rsc.domain_name
        myif["attr_domain_name_arn"] = rsc.attr_domain_name_arn
        myif["attr_regional_domain_name"] = rsc.attr_regional_domain_name
        myif["attr_regional_hosted_zone_id"] = rsc.attr_regional_hosted_zone_id
        return rsc


# ==============================
# CfnRoutingRule
# ==============================
class MyRoutingRule(MyBase):
    def __init__(self, obj: Any, name: str):
        super().__init__(obj, name)

    def create(self, myif: dict) -> Any:
        return super().create(myif)

    def _rsc_(self, rscif: dict, myif: dict) -> CfnRoutingRule:
        action_list: list = []
        condition_list: list = []
        if "actions" in rscif:
            for action in rscif["actions"]:
                invoke_api = CfnRoutingRule.ActionProperty(
                    invoke_api=CfnRoutingRule.ActionInvokeApiProperty(
                        **action["invoke_api"]
                    )
                )
                action_list.append(invoke_api)
        rscif["actions"] = action_list
        if "conditions" in rscif:
            for condition in rscif["conditions"]:
                condition_list.append(CfnRoutingRule.ConditionProperty(**condition))
        rscif["conditions"] = condition_list
        rsc = CfnRoutingRule(**rscif)
        return rsc
