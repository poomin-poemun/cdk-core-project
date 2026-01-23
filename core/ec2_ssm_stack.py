from aws_cdk import Fn, Stack
from constructs import Construct

from core.myconstructs.myctrl import MyCtrl
from core.myconstructs.myec2 import MyInstance, MySecurityGroup
from core.myconstructs.myiam import MyInstanceProfile, MyRole


class Ec2SsmStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.myctrl = myctrl
        myctrl.add_common_tags(self)
        # EC2-Instance
        ec2sg = myctrl.create(
            MySecurityGroup(
                obj=self, name="PWorkInstSSM.securitygrps.pwork_instance_ssm_sg"
            )
        )
        ec2role = myctrl.create(
            MyRole(obj=self, name="PWorkInstSSM.roles.pwork_instance_ssm_role")
        )
        ec2prof = myctrl.create(
            MyInstanceProfile(
                obj=self, name="PWorkInstSSM.instanceprofiles.pwork_instance_ssm_prof"
            )
        )
        ec2prof.add_dependency(ec2role)
        ec2inst = myctrl.create(
            MyInstance(obj=self, name="PWorkInstSSM.instances.pwork_instance_ssm")
        )
        ec2inst.add_dependency(ec2prof)
        ec2inst.add_dependency(ec2sg)
