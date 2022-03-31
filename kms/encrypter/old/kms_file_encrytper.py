#This script is a work in process. The intention is to use KMS to generate a data key and then use that data key to encrypt a string of text. The string of text will be stored in the local directory with a copy of the encrytped data key.

#Import the required modules
#Test Comment
from cryptography.fernet import Fernet
import boto3
import base64

#Setup Variables
#aliaslist = get_aliases()
#keynumber = print_keys(aliaslist)


#Setuo a boto3 KMS client
client = boto3.client('kms')

#Function to get the list of KMS key aliases
#To call the function - listname = (getaliases())
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
    
#aliaslist = get_aliases()
    
#Function to print the list of aliases and ask the user to select the key(alias) they will use to generate key
def print_keys(keylist):
    #Loop through the provided list
    for x in keylist: 
        #Print out each key with the index number
        print(keylist.index(x),". ",x)
    
    key = input("Please select the number of the key that you would like to use: ")
    keyint = int(key)
    return keyint


#Function to generate a data key from the selected KMS key
def generate_data_key(keynumber):
    key = aliaslist[keynumber]
    datakey = client.generate_data_key(KeyId=key,KeySpec='AES_256')
    return datakey

def encrypt(text, key):
    f = Fernet(key)
    encrytpedfile = f.encrypt(text)
    return encrytpedfile
    
def decrypt(text, key):
    f = Fernet(key)
    decrypt = f.decrypt(text)
    return decrypt
    
def retrievedatakey(encrypteddatakey):
    plainkeyreturned = client.decrypt(encrypteddatakey)
    return(plainkeyreturned)
    
#Setup Variables
aliaslist = get_aliases()
keynumber = print_keys(aliaslist)
datakey = generate_data_key(keynumber)
plainkeyb64 = base64.b64encode(datakey['Plaintext'])
plainkey = datakey['Plaintext']
encryptedkey = datakey['CiphertextBlob']
textinput = input("Please input some text that you would like to encrypt: ")
textinputbytes = bytes(textinput, 'utf-8')
encryptedtext = encrypt(textinputbytes, plainkeyb64)
decryptedtext = decrypt(encryptedtext, plainkeyb64)
print("This is the encrypted text: ", encryptedtext)
print("This is the decrytped text: ", decryptedtext)
string = decryptedtext.decode('utf-8')
print("This is the decrypted string:", string)
print("The plaintext data key will now be deleted")
del plainkey
del plainkeyb64

#retrievedkey = retrievedatakey(encryptedkey)
#print(retrievedkey)
    
#print_keys()


#def get_user_input():
    #input("Please input some text that you would like to encrypt: ")
