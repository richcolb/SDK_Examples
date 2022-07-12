import boto3
from boto3.dynamodb.conditions import Key

def create_record(fname, lname):
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('test') 
    
    
    table.put_item(Item={
        'fname': fname,
        'lname': lname
        })
        
create_record("Richard","Colborne")