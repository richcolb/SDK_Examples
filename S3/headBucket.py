import boto3
import botocore

client = boto3.client('s3')

def verifyBucketName(client, bucket):
    try:
        response = client.head_bucket(Bucket=bName)
        print("The bucket exists in your account")
    
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        print(e.response)
        if error_code == 404:
            print('Existing bucket not found, please proceed')
            
        if error_code == 403:
            print(e.response)
            print('This Bucket already exists in another account')


bName = input("What is the bucket name to test? ")
verifyBucketName(client, bName)