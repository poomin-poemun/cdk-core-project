import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_core_project.cdk_core_project_stack import CdkCoreProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_core_project_tmp/cdk_core_project_tmp_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkCoreProjectStack(app, "CdkCoreProjectStack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
