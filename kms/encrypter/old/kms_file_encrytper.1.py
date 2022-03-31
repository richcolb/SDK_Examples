#Import the required modules
#Test Comment
from cryptography.fernet import Fernet
import boto3
import base64


client = boto3.client('kms')

string= input("Please enter a string of text that you would like to be encrypted: ")

def get_aliases():
    #Create an empty list
    outlist = []
    #Query for the list of aliases from KMS
    response = client.list_aliases(Limit=30)
    #Loop through the 'response' object to extract the actual alias names
    for alias_data in response['Aliases']:
        alias_names = alias_data['AliasName']
        #Append the alias names to the 'outlist' list
        outlist.append(alias_names)
    #Return the final list as the output from the function
    return outlist
    
    
#Function to print the list of aliases and ask the user to select the key(alias) they will use to generate key
def print_keys(keylist):
    #Loop through the provided list
    for x in keylist: 
        #Print out each key with the index number
        print(keylist.index(x),". ",x)
    
    key = input("Please select the number of the key that you would like to use: ")
    keyint = int(key)
    return keyint

# Create variable to hold the list of KMS key aliases    
keylist = (get_aliases())

# run the function to print the list of keys an ask the user to select one of the keys
keynum = (print_keys(keylist))

def generate_data_key(key):
    key = keylist[key]
    datakey = client.generate_data_key(KeyId=key,KeySpec='AES_256')
    return datakey
    
#call function to generate data key
dk = (generate_data_key(keynum))

print(dk)
print(dk['Plaintext'])






