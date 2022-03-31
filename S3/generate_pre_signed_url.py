import boto3

def presign(bucket, key, expiration):
    client = boto3.client('s3')
    response = client.generate_presigned_url('get_object', Params ={'Bucket':bucket, 'Key': key}, ExpiresIn=expiration)
    return response
    
presigned = presign('rc-rekognition', 'people.jpg', 10)
print(presigned)

    