import boto3
# Retrieve the list of existing buckets
client = boto3.client('sns')


response = client.publish(
    TopicArn='arn:aws:sns:eu-west-1:160620582525:tester',
    Message='howdy!!'
    
)


