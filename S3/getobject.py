import boto3

s3 = boto3.resource('s3')

def get_object():
    obj = s3.Object("rc-rekognition","people.jpg")
    body = obj.get()['Body'].read()
    return body

object = get_object()
print(object)
print(type(object))


