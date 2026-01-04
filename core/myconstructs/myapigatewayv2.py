import copy
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
        tmp_rscif: dict = copy.deepcopy(rscif)
        if "domain_name_configurations" in tmp_rscif:
            configurations_list = []
            for configuration in tmp_rscif["domain_name_configurations"]:
                configurations_list.append(
                    CfnDomainName.DomainNameConfigurationProperty(**configuration)
                )
            tmp_rscif["domain_name_configurations"] = configurations_list
        rsc = CfnDomainName(**tmp_rscif)
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
        tmp_rscif: dict = copy.deepcopy(rscif)
        action_list: list = []
        condition_list: list = []
        if "actions" in tmp_rscif:
            for action in tmp_rscif["actions"]:
                invoke_api = CfnRoutingRule.ActionProperty(
                    invoke_api=CfnRoutingRule.ActionInvokeApiProperty(
                        **action["invoke_api"]
                    )
                )
                action_list.append(invoke_api)
        tmp_rscif["actions"] = action_list
        if "conditions" in tmp_rscif:
            for condition in tmp_rscif["conditions"]:
                condition_list.append(CfnRoutingRule.ConditionProperty(**condition))
        tmp_rscif["conditions"] = condition_list
        rsc = CfnRoutingRule(**tmp_rscif)
        return rsc
