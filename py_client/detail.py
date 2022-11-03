import requests

endpoint = "http://127.0.0.1:8000/api/products/1/"
get_response = requests.get(endpoint,json={"title":"Product 8","content":"Hello World"})
print(get_response.json())