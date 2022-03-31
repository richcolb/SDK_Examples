import boto3
import json
import getpass

username = getpass.getpass(prompt="username:")
password = getpass.getpass(prompt="password:")


def authenticate_and_get_token(username: str, password: str, 
                               user_pool_id: str, app_client_id: str) -> None:
    client = boto3.client('cognito-idp')

    resp = client.admin_initiate_auth(
        UserPoolId=user_pool_id,
        ClientId=app_client_id,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            "USERNAME": username,
            "PASSWORD": password
        }
    )
    
    return(resp['AuthenticationResult']['AccessToken'], resp['AuthenticationResult']['IdToken'])
    
    
tokens = authenticate_and_get_token(username = username, password = password, user_pool_id = "eu-west-1_HSqHWksN5", app_client_id = "1io9becicqp4gduc9gcbhvlrir")
print("Access token:",tokens[0])
print("ID token:",tokens[1])