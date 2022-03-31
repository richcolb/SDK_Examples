import boto3

client = boto3.client('s3')

bName = "rc-s3-operations"
kName = "first.html"

response = client.head_object(Bucket=bName,Key=kName)
print(response)

