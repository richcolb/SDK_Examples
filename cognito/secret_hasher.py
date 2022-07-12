import sys
import hmac, hashlib, base64

# def gethash(username, app_client_id, key):
#     username = sys.argv[1]
#     app_client_id = sys.argv[2]
#     key = sys.argv[3]
#     message = bytes(sys.argv[1]+sys.argv[2],'utf-8')
#     key = bytes(sys.argv[3],'utf-8')
#     secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()
#     return secret_hash
# print("SECRET HASH:",secret_hash)


def gethash(username, app_client_id, key):
    username = username
    app_client_id = app_client_id
    key = key
    message = bytes(username+app_client_id, 'utf-8')
    key = bytes(key,'utf-8')
    secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()
    return secret_hash
#print("SECRET HASH:",secret_hash)


print(gethash("richcolb@gmail.com", "coegvugjnt9hhkfa7d2p2b6or", "2bldjk8g17gdlpq0vja83lvtqipocckiqsqgcosa5qd49gpi9i8"))