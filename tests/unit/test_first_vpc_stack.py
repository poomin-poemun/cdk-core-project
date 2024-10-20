import aws_cdk as core
import aws_cdk.assertions as assertions

from core.first_vpc_stack import FirstVpcStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_core_project_tmp/cdk_core_project_tmp_stack.py
def test_first_vpc_stack():
    app = core.App()
    stack = FirstVpcStack(app, "FirstVpcStack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
