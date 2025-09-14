from aws_cdk import RemovalPolicy, Stack
from constructs import Construct
from core.myconstructs.myapigateway import (
    MyAccount,
    MyDeployment,
    MyMethod,
    MyResource,
    MyRestApi,
    MyStage,
    MyAuthorizer,
)
from core.myconstructs.myctrl import MyCtrl
from core.myconstructs.myec2 import MySecurityGroup
from core.myconstructs.myiam import MyRole
from core.myconstructs.mylambda import MyFunction, MyPermission
from core.myconstructs.mylogs import MyLogGroup


class ApigwLambdaStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, myctrl: MyCtrl, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.myctrl = myctrl
        myctrl.add_common_tags(self)

        # Role
        account_log_role = myctrl.create(MyRole(obj=self, name="apigwlambda.roles.apigw_account_log"))
        fnc_cat_role = myctrl.create(MyRole(obj=self, name="apigwlambda.roles.apigw_test_fnc_cat"))
        fnc_dog_role = myctrl.create(MyRole(obj=self, name="apigwlambda.roles.apigw_test_fnc_dog"))
        fnc_aut_role = myctrl.create(MyRole(obj=self, name="apigwlambda.roles.apigw_test_authorizer_fnc"))

        # Log
        log_group = myctrl.create(MyLogGroup(obj=self, name="apigwlambda.logs.apigw_test_loggrp"))
        log_group.apply_removal_policy(policy=RemovalPolicy.RETAIN_ON_UPDATE_OR_DELETE)

        # SecurityGroup
        func_cat_sg = myctrl.create(MySecurityGroup(obj=self, name="apigwlambda.securitygrps.apigw_test_fnc_cat"))
        func_dog_sg = myctrl.create(MySecurityGroup(obj=self, name="apigwlambda.securitygrps.apigw_test_fnc_dog"))
        func_aut_sg = myctrl.create(MySecurityGroup(obj=self, name="apigwlambda.securitygrps.apigw_test_fnc_aut"))

        # ApiGw Account
        apigw_account = myctrl.create(MyAccount(obj=self, name="apigwlambda.accounts.apigw_account"))
        apigw_account.add_dependency(account_log_role)

        # ApiGateWay
        apigw = myctrl.create(MyRestApi(obj=self, name="apigwlambda.apigws.apigw_test"))

        # Function
        fnc_cat = myctrl.create(MyFunction(obj=self, name="apigwlambda.functions.apigw_test_fnc_cat"))
        fnc_dog = myctrl.create(MyFunction(obj=self, name="apigwlambda.functions.apigw_test_fnc_dog"))
        fnc_aut = myctrl.create(MyFunction(obj=self, name="apigwlambda.functions.apigw_test_fnc_authorizer"))
        fnc_cat.add_dependency(fnc_cat_role)
        fnc_dog.add_dependency(fnc_dog_role)
        fnc_aut.add_dependency(fnc_aut_role)

        # Role
        auth_role = myctrl.create(MyRole(obj=self, name="apigwlambda.roles.apigw_test_authorizer"))
        auth_role.add_dependency(fnc_aut)

        # authorizers
        authrize = myctrl.create(MyAuthorizer(obj=self, name="apigwlambda.authorizers.apigw_test_authorizer"))
        auth_role.add_dependency(auth_role)

        # Permission
        fnc_cat_permssn = myctrl.create(MyPermission(obj=self, name="apigwlambda.permissions.apigw_test_fnc_cat_permssn"))
        fnc_dog_permssn = myctrl.create(MyPermission(obj=self, name="apigwlambda.permissions.apigw_test_fnc_dog_permssn"))
        fnc_cat_permssn.add_dependency(fnc_cat)
        fnc_dog_permssn.add_dependency(fnc_dog)

        # Resource
        api_rsc_v2 = myctrl.create(MyResource(obj=self, name="apigwlambda.apiresources.api_test_rsc_v2"))
        api_rsc_first = myctrl.create(MyResource(obj=self, name="apigwlambda.apiresources.api_test_rsc_first"))
        api_rsc_cat = myctrl.create(MyResource(obj=self, name="apigwlambda.apiresources.api_test_rsc_cat"))
        api_rsc_user_id = myctrl.create(MyResource(obj=self, name="apigwlambda.apiresources.api_test_rsc_user_id"))
        api_rsc_dog = myctrl.create(MyResource(obj=self, name="apigwlambda.apiresources.api_test_rsc_dog"))
        api_rsc_v2.add_dependency(apigw)
        api_rsc_first.add_dependency(api_rsc_v2)
        api_rsc_cat.add_dependency(api_rsc_first)
        api_rsc_user_id.add_dependency(api_rsc_cat)
        api_rsc_dog.add_dependency(api_rsc_first)
        
        # Method
        api_method_cat = myctrl.create(MyMethod(obj=self, name="apigwlambda.apimethods.api_test_method_cat"))
        api_method_user_id = myctrl.create(MyMethod(obj=self, name="apigwlambda.apimethods.api_test_method_user_id"))
        api_method_dog = myctrl.create(MyMethod(obj=self, name="apigwlambda.apimethods.api_test_method_dog"))
        api_method_cat.add_dependency(api_rsc_cat)
        api_method_user_id.add_dependency(api_rsc_user_id)
        api_method_dog.add_dependency(api_rsc_dog)

        # Deployment
        api_deployment = myctrl.create(MyDeployment(obj=self, name="apigwlambda.apideployments.api_test_deployment"))
        api_deployment.add_dependency(api_method_cat)
        api_deployment.add_dependency(api_method_user_id)
        api_deployment.add_dependency(api_method_dog)

        # Stage
        api_stage = myctrl.create(MyStage(obj=self, name="apigwlambda.apistages.api_test_stage"))
        api_stage.add_dependency(log_group)
        api_stage.add_dependency(api_deployment)