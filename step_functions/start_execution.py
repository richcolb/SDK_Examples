import boto3
from botocore.config import Config
import uuid

ident = str(uuid.uuid1())

my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

client = boto3.client('stepfunctions', config=my_config)


response = client.start_execution(
    stateMachineArn='arn:aws:states:us-east-1:160620582525:stateMachine:MyStateMachine',
    name=ident,
    input='{"A":3, "B":2}',
    traceHeader='string'
)

print(response)