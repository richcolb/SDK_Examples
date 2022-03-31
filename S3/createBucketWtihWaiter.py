import boto3
client = boto3.client('s3')

bName = input("What is the bucket name? ")

def create_bucket(name):
    response = client.create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
    waiter = client.get_waiter('bucket_exists')
    waiter.wait(Bucket=name)
    print(response) 

def delete_bucket(name):
    client.delete_bucket(Bucket=bName)
    waiter = client.get_waiter('bucket_not_exists')
    waiter.wait(Bucket=bName, WaiterConfig={'Delay':5, 'MaxAttempts':10})
    print("Ok, Bucket has been deleted!!")
    
create_bucket(bName)

delete = input('Do you now what to delete the bukcet? (Y/N): ')

if delete.upper() == "Y":
    delete_bucket(bName)
    
else: 
    print("Ok, I'll keep the bucket!!")


    