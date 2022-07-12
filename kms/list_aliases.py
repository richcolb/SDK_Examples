#import modules
import boto3
#Setup an instance of the KMS client
client = boto3.client('kms')
#Create a response object to list the alises (returns an object of type 'dict')
response = client.list_aliases(Limit=30)
#Create an empty list

outlist = list(map(lambda alias: alias['AliasName'], response['Aliases']))

print(outlist)


