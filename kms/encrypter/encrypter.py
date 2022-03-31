import boto3
import base64
from cryptography.fernet import Fernet
import uuid

client = boto3.client('kms')

#aliases = client.list_aliases(Limit=30) 


def getAliases():
    aliases = client.list_aliases(Limit=30) 
    keyList = [] 
    for x in aliases["Aliases"]:
        alias = x["AliasName"]
        keyList.append(alias)
    return keyList

def getKeyInput():
    for x in keyList:
        print(keyList.index(x),". ",x)
    num = input("Please choose the number of the key you would like to use to encrypt the text: ")
    return num

def getText():
    text = input("Please input some text that you would like to encrypt: ")
    return text
    
def getDataKey(alias):
    datakey = client.generate_data_key(KeyId=alias,KeySpec='AES_256')
    print("\nKMS returned the following keys \nPlain text key: {plain} \nEncrypted key: {encrypted}\n".format (plain = datakey["Plaintext"], encrypted = datakey["CiphertextBlob"]))
    return datakey
    
def encrypt(text, datakey):
    plainkeyb64 = base64.b64encode(datakey['Plaintext'])
    f = Fernet(plainkeyb64)
    encryptedText = f.encrypt(bytes(text, "utf-8"))
    return encryptedText
    
def writefile(text, datakey, encryptedText):
    fn = input("What is the Filename: ")
    filedata = {"uuid": str(uuid.uuid4()),"filename": fn,  "text": text, "datakey": datakey, "encryptedtext": encryptedText}
    return filedata

def writetoDDB(input):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('encrypted')
    response = table.put_item(
        Item={
            'uuid': input["uuid"],
            'filename' : input["filename"], 
            'datakey': input["datakey"],
            'encryptedtext': input["encryptedtext"] 
        }
    )
    
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print("Saved to Database")
        print("Request ID: {ID}".format (ID = response["ResponseMetadata"]["RequestId"] ))
    

keyList = getAliases()
userKeyNum = int(getKeyInput())
print("You have chosen number {num} which has an alias of '{alias}'".format(num = (userKeyNum), alias = keyList[userKeyNum]))
text = getText()
datakey = getDataKey(keyList[userKeyNum])
encryptedText = encrypt(text,datakey)
filedata = writefile(text, datakey["CiphertextBlob"], encryptedText)
writetoDDB(filedata)










