import aws_cdk as core
import aws_cdk.assertions as assertions

from serverless_data_platform.serverless_data_platform_stack import ServerlessDataPlatformStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serverless_data_platform/serverless_data_platform_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessDataPlatformStack(app, "serverless-data-platform")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
