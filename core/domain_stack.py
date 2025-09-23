from aws_cdk import Stack
from constructs import Construct

from core.myconstructs.myapigatewayv2 import MyDomainName, MyRoutingRule
from core.myconstructs.myctrl import MyCtrl
from core.myconstructs.myroute53 import MyRecordSet


class DomainStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.myctrl = myctrl
        myctrl.add_common_tags(self)
        # DomainName
        domainname = myctrl.create(
            MyDomainName(obj=self, name="domain.domainnames.apigw_test_domain")
        )
        # Routing
        routing = myctrl.create(
            MyRoutingRule(obj=self, name="domain.routingrules.apigw_test_routingrule")
        )
        routing.add_dependency(domainname)

        # route53
        route53_record_set = myctrl.create(
            MyRecordSet(obj=self, name="domain.route53.apigw_test_recordset")
        )
        route53_record_set.add_dependency(domainname)
