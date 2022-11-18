import requests
from getpass import getpass


auth_endpoint = "http://127.0.0.1:8000/api/auth/"
password = getpass()

auth_response = requests.post(auth_endpoint, json={
    'username':'staff','password':password
})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        # "Authorization": f"Token {token}"  #to change this Token to Bearer whic is generally used go to api>>create authentication.py and follow stuffs 
        "Authorization" : f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(endpoint,headers=headers)
    print(get_response.json())