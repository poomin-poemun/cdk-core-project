from aws_cdk import Stack
from constructs import Construct

from core.myconstructs.myctrl import MyCtrl
from core.myconstructs.myec2 import (
    MyRouteTable,
    MySubnet,
    MySubnetRouteTableAssociation,
    MyVpc,
)


class PworkVpcStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.myctrl = myctrl
        myctrl.add_common_tags(self)
        # VPC
        pwrokvpc = myctrl.create(MyVpc(obj=self, name="pwork.vpcs.pworkvpc"))

        # pwork_pub_subnet_az1
        pworkpubsubnetaz1 = myctrl.create(MySubnet(obj=self, name="pwork.subnets.pwork_pub_subnet_az1"))
        # pwork_pub_subnet_az3
        pworkpubsubnetaz3 = myctrl.create(MySubnet(obj=self, name="pwork.subnets.pwork_pub_subnet_az3"))
        # pwork_pri_subnet_az1
        pworkprisubnetaz1 = myctrl.create(MySubnet(obj=self, name="pwork.subnets.pwork_pri_subnet_az1"))
        # pwork_pri_subnet_az3
        pworkprisubnetaz3 = myctrl.create(MySubnet(obj=self, name="pwork.subnets.pwork_pri_subnet_az3"))

        # route-table public
        pworkpubroutetbl = myctrl.create(MyRouteTable(self, name="pwork.route_tables.pwork-pub-routetbl"))
        # route-table private
        pworkpriroutetbl = myctrl.create(MyRouteTable(self, name="pwork.route_tables.pwork-pri-routetbl"))

        # pwork_pub_subnet_route_az1
        pworkpubsubnetaz1 = myctrl.create(MySubnetRouteTableAssociation(obj=self, name="pwork.subnet-routes.pwork_pub_subnet_route_az1"))
        # pwork_pub_subnet_route_az3
        pworkpubsubnetaz3 = myctrl.create(MySubnetRouteTableAssociation(obj=self, name="pwork.subnet-routes.pwork_pub_subnet_route_az3"))
        # pwork_pri_subnet_route_az1
        pworkprisubnetaz1 = myctrl.create(MySubnetRouteTableAssociation(obj=self, name="pwork.subnet-routes.pwork_pri_subnet_route_az1"))
        # pwork_pri_subnet_route_az3
        pworkprisubnetaz3 = myctrl.create(MySubnetRouteTableAssociation(obj=self, name="pwork.subnet-routes.pwork_pri_subnet_route_az3"))
