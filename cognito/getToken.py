import boto3
import json
import getpass
import hmac, hashlib, base64

def hashgen(username, app_client_id, key):
    username = username
    app_client_id = app_client_id
    key = key
    message = bytes(username+app_client_id, 'utf-8')
    key = bytes(key,'utf-8')
    secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()
    return secret_hash
    

def authenticate_and_get_token(username: str, password: str, 
                               user_pool_id: str, app_client_id: str, secret_hash: str) -> None:
    
    client = boto3.client('cognito-idp')

    resp = client.initiate_auth(
        ClientId=app_client_id,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            "USERNAME": username,
            "PASSWORD": password,
            "SECRET_HASH" : secret_hash
        }
    )
    return(resp['AuthenticationResult']['AccessToken'], resp['AuthenticationResult']['IdToken'])

username = getpass.getpass(prompt="username:")
password = getpass.getpass(prompt="password:")
user_pool_id = "eu-west-1_9gHcGr1Pw"
app_client_id = "coegvugjnt9hhkfa7d2p2b6or"
client_secret = "2bldjk8g17gdlpq0vja83lvtqipocckiqsqgcosa5qd49gpi9i8"
secret_hash = hashgen(username, app_client_id, client_secret)  
    
tokens = authenticate_and_get_token(username = username, password = password, user_pool_id = user_pool_id , app_client_id = app_client_id, secret_hash = secret_hash)
print("Access token:",tokens[0])
print("ID token:",tokens[1])