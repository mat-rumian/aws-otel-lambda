from os import environ
import boto3
from opentelemetry.sdk.resources import *


class AwsLambdaResourceDetector(ResourceDetector):
    def detect(self) -> "Resource":
        account_id = boto3.client('sts').get_caller_identity()['Account']
        aws_region = environ.get("AWS_REGION")
        lambda_name = environ.get("AWS_LAMBDA_FUNCTION_NAME")
        function_version = environ.get("AWS_LAMBDA_FUNCTION_VERSION")

        env_resource_map = {
            CLOUD_ACCOUNT_ID: account_id,
            CLOUD_PROVIDER: "aws",
            CLOUD_REGION: aws_region,
            FAAS_NAME: lambda_name,
            FAAS_VERSION: function_version,
        }

        return Resource(env_resource_map)
