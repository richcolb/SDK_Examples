import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket(name="rc-resource-bucket")

obj = s3.Object(bucket_name="rc-resource-bucket", key="Eagle-in-flight-Richard-Lee-Unsplash-1-edited-scaled.jpg")

response = obj.download_file("./")

print(response)