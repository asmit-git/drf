import requests

#endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/"

#get_response = requests.get(endpoint)
#print(get_response.text)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON


#endpoint = "https://httpbin.org/anything"

# get_response = requests.get(endpoint)
# print(get_response.json())

# get_response = requests.get(endpoint,json={"query":"Hello World"})
# print(get_response.json())
# print(get_response.status_code)

#get_response = requests.get(endpoint,data={"query":"Hello World"})
#print(get_response.json()) 

# #GET METHOD
# endpoint = "http://127.0.0.1:8000/api"
# get_response = requests.get(endpoint,json={"product_id":123})
# print(get_response.json())

#POST METHOD
endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.post(endpoint,json={"title":"Product 8","content":"Hello World"})
print(get_response.json())