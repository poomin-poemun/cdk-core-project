import aws_cdk as core
import aws_cdk.assertions as assertions

from core.apigw_lambda_stack import ApigwLambdaStack


# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_core_project_tmp/cdk_core_project_tmp_stack.py
def test_apigw_lambda_stack():
    app = core.App()
    stack = ApigwLambdaStack(app, "ApigwLambdaStack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
