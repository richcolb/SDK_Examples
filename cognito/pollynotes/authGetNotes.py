import boto3
import getpass
import requests

def call(url, headers):
    response = requests.get(url=url, headers=headers)
    return response.json()


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
    
    print(resp)
    
    return(resp['AuthenticationResult']['AccessToken'], resp['AuthenticationResult']['IdToken'])

username = getpass.getpass(prompt="username:")
password = getpass.getpass(prompt="password:")
    
url = "https://kg6sq0mhh0.execute-api.eu-west-1.amazonaws.com/Prod/notes"
tokens = authenticate_and_get_token(username = username, password = password, user_pool_id = "eu-west-1_Xev95q6v9", app_client_id = "5nibl4fdhabmv2n2navke3fpsc")
auth_header = {"Authorization":tokens[1]}
response = call(url, auth_header)
print(response)
    
    
